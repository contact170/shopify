#!/usr/bin/env python3
"""Moteur de boîtes Daewoo : met en page une boîte à partir de produit.json + gabarit.json.

Usage :
  python3 construire.py <dossier_produit>              → tous les livrables
  python3 construire.py <dossier_produit> --brouillon  → rendu rapide + contrôles (sans CMJN ni 3D)

Le dossier produit contient :
  produit.json   textes, arguments, caractéristiques, EAN… (voir ../EF503/produit.json)
  gabarit.json   produit par gabarit.py à partir du PDF du fabricant, vérifié
  images/        visuel produit détouré (PNG ou WebP avec transparence)

Les faces rendues pour contrôle visuel sont écrites dans <dossier_temporaire>/faces/ (affiché en fin de build).
"""
import hashlib, json, math, os, re, shutil, subprocess, sys, tempfile, datetime
from PIL import Image

MOTEUR = os.path.dirname(os.path.abspath(__file__))
A = os.path.join(MOTEUR, 'assets')
sys.path.insert(0, MOTEUR)
from ean import modules as ean_modules, checksum as ean_checksum  # noqa: E402

Image.MAX_IMAGE_PIXELS = None
REF = {'hero': (227.9, 148.93), 'argument': (227.9, 92.96), 'application': (148.94, 92.96), 'dos': (227.89, 92.96),
       'fiche': (148.94, 92.96), 'rabat': (227.89, 141.75), 'identite': (148.94, 92.96)}


# ======================================================================== utilitaires
def deep_merge(a, b):
    out = dict(a)
    for k, v in b.items():
        out[k] = deep_merge(out[k], v) if isinstance(v, dict) and isinstance(out.get(k), dict) else v
    return out


def typo(s):
    """Typographie française : apostrophes, espaces insécables avant ponctuation double et unités."""
    if not isinstance(s, str) or '://' in s:
        return s
    s = re.sub(r"(\w)'(\w)", r'\1’\2', s)
    s = re.sub(r' ([:;?!])', r'&nbsp;\1', s)
    s = re.sub(r'(\d) (mm|cm|m|km|Go|GB|To|TB|V|W|mAh|Ah|°C|°|MP|dB|h|min|s|%|Mbps|GHz|MHz|kg|g|ans|jours)(?=[\s.,;:)<]|$)',
               r'\1&nbsp;\2', s)
    return s


def T(text, size, weight=400, color='#fff', ls=0, lh=1.25, extra='', chk=True, nom=None):
    cls = ' class="chk"' if chk else ''
    dn = f' data-nom="{nom}"' if nom else ''
    return (f'<div{cls}{dn} style="font-size:{size:.3f}mm;font-weight:{weight};color:{color};letter-spacing:{ls}em;'
            f'line-height:{lh};{extra}">{typo(text)}</div>')


def at(x, y, inner, w=None, h=None, style='', cls=''):
    s = f'left:{x:.3f}mm;top:{y:.3f}mm;'
    if w is not None:
        s += f'width:{w:.3f}mm;'
    if h is not None:
        s += f'height:{h:.3f}mm;'
    return f'<div class="abs {cls}" style="{s}{style}">{inner}</div>'


def center(cx, y, inner):
    return f'<div class="abs" style="left:{cx:.3f}mm;top:{y:.3f}mm;transform:translateX(-50%);white-space:nowrap">{inner}</div>'


_icons = {}


def lucide(name):
    if name not in _icons:
        p = os.path.join(A, 'icons', name + '.svg')
        if not os.path.exists(p):
            raise SystemExit(f'Icône inconnue « {name} » : ajouter le fichier SVG Lucide dans {os.path.dirname(p)}')
        s = re.sub(r'<!--.*?-->', '', open(p).read(), flags=re.S)
        _icons[name] = re.search(r'<svg[^>]*>(.*)</svg>', s, flags=re.S).group(1).strip()
    return _icons[name]


def icon(name, size, color='#fff', stroke_mm=0.3):
    sw = stroke_mm / size * 24
    if name == 'human-scan':
        inner = lucide('scan') + f'<g transform="translate(6.6 6.2) scale(0.45)" stroke-width="{sw/0.45:.3f}">' + lucide('person-standing') + '</g>'
    elif name == 'microsd':
        inner = '<path d="M8 2.5h7.2l3.3 3.3v4.4l-1.1 1.3v10H8z"/><path d="M10.6 5.6v2.6M13.1 5.6v2.6M15.6 6.8v1.4"/>'
    elif name == 'switch':
        inner = ('<rect x="2.5" y="7.5" width="19" height="9" rx="1.6"/>'
                 '<path d="M5.8 13.6v-2.4h2.4v2.4M10.8 13.6v-2.4h2.4v2.4M15.8 13.6v-2.4h2.4v2.4"/>')
    else:
        inner = lucide(name)
    return (f'<svg viewBox="0 0 24 24" style="width:{size:.3f}mm;height:{size:.3f}mm;display:block;flex:none" fill="none" '
            f'stroke="{color}" stroke-width="{sw:.3f}" stroke-linecap="round" stroke-linejoin="round">{inner}</svg>')


LOGO_D = re.search(r' d="([^"]+)"', open(os.path.join(A, 'logo.svg')).read()).group(1)


def logo(width, color):
    return (f'<svg class="chk" data-nom="logo" viewBox="20 20 3228 526" style="width:{width:.3f}mm;height:{width*526/3228:.3f}mm;'
            f'display:block"><path d="{LOGO_D}" fill="{color}" fill-rule="evenodd"/></svg>')


def trace_svg(name, height, color):
    s = open(os.path.join(A, name + '.svg')).read()
    W, H = [float(v) for v in re.search(r'viewBox="0 0 (\S+) (\S+)"', s).groups()]
    d = re.search(r' d="([^"]+)"', s).group(1)
    w = height * (W - 40) / (H - 40)
    return (f'<svg viewBox="20 20 {W-40} {H-40}" style="width:{w:.3f}mm;height:{height}mm;display:block;flex:none">'
            f'<path d="{d}" fill="{color}" fill-rule="evenodd"/></svg>'), w


def uri(path):
    return 'file://' + os.path.abspath(path)


def qr_svg(url, size):
    import segno
    q = segno.make(url, error='h', micro=False)
    m = [list(r) for r in q.matrix]
    n = len(m)
    d = []
    for y, row in enumerate(m):
        x = 0
        while x < n:
            if row[x]:
                s0 = x
                while x < n and row[x]:
                    x += 1
                d.append(f'M{s0} {y}h{x-s0}v1h-{x-s0}z')
            else:
                x += 1
    pad = 1.6 * size / 27
    inner = size - 2 * pad
    k = max(7, round(n * 0.24) // 2 * 2 + 1)       # pastille centrale ≈ 24 % (correction H)
    o = (n - k) // 2
    ic = inner * (k - 2) / n
    return (f'<div class="chk" data-nom="QR code" style="position:relative;width:{size:.3f}mm;height:{size:.3f}mm;background:#fff;border-radius:{size*0.06:.3f}mm">'
            f'<svg viewBox="0 0 {n} {n}" shape-rendering="crispEdges" style="position:absolute;left:{pad:.3f}mm;top:{pad:.3f}mm;width:{inner:.3f}mm;height:{inner:.3f}mm">'
            f'<path d="{"".join(d)}" fill="#000"/><rect x="{o}" y="{o}" width="{k}" height="{k}" fill="#fff"/></svg>'
            f'<img src="{uri(os.path.join(A, "app_icon.png"))}" style="position:absolute;left:{pad + inner*(o+1)/n:.3f}mm;top:{pad + inner*(o+1)/n:.3f}mm;width:{ic:.3f}mm;height:{ic:.3f}mm"></div>')


def ean_svg(code, mag):
    mods = ean_modules(code)
    mw, bar_h, guard_ext = 0.33 * mag, 22.85 * mag, 1.65 * mag
    qz_l, qz_r = 11, 7
    total_w = (qz_l + 95 + qz_r) * mw
    H = 25.93 * mag
    guards = set(list(range(0, 3)) + list(range(45, 50)) + list(range(92, 95)))
    rects, i = [], 0
    while i < 95:
        if mods[i] == '1':
            j = i
            while j < 95 and mods[j] == '1' and ((j in guards) == (i in guards)):
                j += 1
            rects.append(f'<rect x="{(qz_l+i)*mw:.4f}" y="0" width="{(j-i)*mw:.4f}" height="{bar_h + (guard_ext if i in guards else 0):.4f}"/>')
            i = j
        else:
            i += 1
    fs, ty = 2.75 * mag * 1.18, bar_h + 2.95 * mag
    txt = [f'<text x="{(qz_l-1.2)*mw - 0.1:.3f}" y="{ty:.3f}" text-anchor="end">{code[0]}</text>']
    txt += [f'<text x="{(qz_l+3+7*k+3.5)*mw:.3f}" y="{ty:.3f}" text-anchor="middle">{code[1+k]}</text>' for k in range(6)]
    txt += [f'<text x="{(qz_l+50+7*k+3.5)*mw:.3f}" y="{ty:.3f}" text-anchor="middle">{code[7+k]}</text>' for k in range(6)]
    txt.append(f'<text x="{(qz_l+95+1.2)*mw:.3f}" y="{ty:.3f}" text-anchor="start">&gt;</text>')
    svg = (f'<svg viewBox="0 -0.2 {total_w:.3f} {H+0.2:.3f}" style="width:{total_w:.3f}mm;height:{H+0.2:.3f}mm;display:block">'
           f'<g fill="#000">{"".join(rects)}</g><g font-family="JetBrains Mono, DejaVu Sans Mono, monospace" font-size="{fs:.3f}" fill="#000">{"".join(txt)}</g></svg>')
    return svg, total_w, H + 0.2


# ======================================================================== éclairages (raster opaque, sans transparence)
def lumiere(dossier_cache, w, h, bleed, halos, noir):
    import numpy as np
    key = hashlib.md5(json.dumps([w, h, bleed, halos, noir]).encode()).hexdigest()[:12]
    out = os.path.join(dossier_cache, f'lumiere_{key}.jpg')
    if os.path.exists(out):
        return out
    bl, bt, br, bb = bleed
    PX = 10
    nx, ny = int(round((w + bl + br) * PX)), int(round((h + bt + bb) * PX))
    X, Y = np.meshgrid((np.arange(nx) + 0.5) / PX - bl, (np.arange(ny) + 0.5) / PX - bt)
    hexc = lambda c: np.array([int(c.lstrip('#')[i:i+2], 16) for i in (0, 2, 4)], float)
    img = np.zeros((ny, nx, 3)) + hexc(noir)
    for cx, cy, rx, ry, stops, op in halos:
        d = np.clip(np.sqrt(((X - cx) / rx) ** 2 + ((Y - cy) / ry) ** 2), 0, 1)
        offs = np.array([s[0] for s in stops]); cols = np.array([hexc(s[1]) for s in stops]); al = np.array([s[2] for s in stops])
        c = np.stack([np.interp(d, offs, cols[:, k]) for k in range(3)], -1)
        a = (np.interp(d, offs, al) * op)[..., None]
        img = c * a + img * (1 - a)
    img += np.random.default_rng(503).uniform(-0.9, 0.9, img.shape)
    Image.fromarray(np.clip(np.round(img), 0, 255).astype('uint8'), 'RGB').save(out, quality=95, subsampling=0)
    return out


SPOT = [(0, '#30333A', 1), (0.45, '#1B1C20', 0.85), (1, '#0B0B0D', 0)]
SOFT = [(0, '#24262B', 1), (1, '#0B0B0D', 0)]
FLOOR = [(0, '#FFFFFF', 0.10), (1, '#FFFFFF', 0)]


# ======================================================================== gabarits de faces
class Ctx:
    def __init__(self, P, C, cache, img):
        self.P, self.C, self.cache, self.img = P, C, cache, img


def face_hero(c, w, h, zones):
    P, C = c.P, c.C
    s = max(0.75, min(1.5, min(w / REF['hero'][0], h / REF['hero'][1])))
    H = []
    portrait = w / h < 1.15
    pad = 11 * s
    if not portrait:
        col_w = min(104 * s, 0.47 * w)
        H.append(at(pad, 11.5 * s, logo(46 * s, C['rouge'])))
        main = (T(P['categorie'].upper(), 2.15 * s, 500, C['gris2'], 0.22, nom='catégorie') +
                T(P['modele'], 21 * s, 600, '#fff', -0.015, 1.0, f'margin-left:{-0.8*s:.2f}mm', nom='modèle') +
                T(P['sous_titre'], 4.05 * s, 300, '#E4E5E8', 0, 1.25, f'margin-top:{1.4*s:.2f}mm', nom='sous-titre') +
                f'<div style="width:{16*s:.2f}mm;height:{0.6*s:.2f}mm;background:{C["rouge"]};margin-top:{3.5*s:.2f}mm"></div>')
        args = P.get('arguments', [])[:3]
        n = max(1, len(args))
        tw = (col_w - (n - 1) * 4 * s) / n
        tiles = ''
        for a in args:
            tiles += (f'<div style="width:{tw:.3f}mm;flex:none">'
                      f'<div style="height:{0.25*s:.2f}mm;background:{C["trait"]};position:relative"><div style="position:absolute;left:0;top:{-0.15*s:.2f}mm;width:{5*s:.2f}mm;height:{0.55*s:.2f}mm;background:{C["rouge"]}"></div></div>'
                      + T(a['valeur'], 9.4 * s, 600, '#fff', -0.02, 1.0, f'margin-top:{3.2*s:.2f}mm;margin-left:{-0.4*s:.2f}mm;white-space:nowrap', nom='argument ' + a['valeur'])
                      + T(a['titre'], 2.35 * s, 500, '#fff', 0.01, 1.25, f'margin-top:{3.0*s:.2f}mm')
                      + T(a['detail'], 2.15 * s, 300, C['gris2'], 0, 1.25, f'margin-top:{0.45*s:.2f}mm') + '</div>')
        main += f'<div style="display:flex;gap:{4*s:.2f}mm;margin-top:{7.2*s:.2f}mm;width:{col_w:.3f}mm">{tiles}</div>'
        b = P.get('badge')
        if b:
            main += (f'<div style="display:flex;align-items:center;gap:{3.8*s:.2f}mm;margin-top:{7.5*s:.2f}mm">'
                     f'<div class="chk" data-nom="badge" style="flex:none;background:{C["rouge"]};border-radius:{3*s:.2f}mm;padding:{1.05*s:.2f}mm {3*s:.2f}mm {0.95*s:.2f}mm">'
                     + T(b['texte'], 2.45 * s, 600, '#fff', 0.14, 1.2, chk=False) + '</div>'
                     + T(b.get('detail', ''), 2.15 * s, 300, C['gris1'], 0, 1.3, nom='détail badge') + '</div>')
        H.append(at(pad, 32.5 * s, main, col_w))
        picts = P.get('pictos', [])[:4]
        if picts:
            row = ''.join(f'<div style="width:{col_w/len(picts) if len(picts) > 2 else 26.5*s:.3f}mm;display:flex;gap:{1.8*s:.2f}mm;flex:none">'
                          f'{icon(p["icone"], 5.6*s)}<div>' + T(p['titre'], 2.1 * s, 500, '#fff', 0, 1.25) +
                          T(p['detail'], 2.1 * s, 300, C['gris2'], 0, 1.25) + '</div></div>' for p in picts)
            H.append(at(pad, h - 30.7 * s, f'<div style="height:{0.2*s:.2f}mm;background:{C["trait"]};width:{col_w:.3f}mm"></div>'
                        f'<div style="display:flex;margin-top:{4.1*s:.2f}mm">{row}</div>', col_w))
        cl, ct = w * 0.508, 12.5 * s
        cw, ch = w - 6.4 * s - cl, h - 10.9 * s - ct
        pos = P.get('reglages', {}).get('hero_image_position', 'right bottom')
        H.append(at(cl, ct, f'<img class="chk img" data-nom="visuel produit" src="{uri(c.img)}" style="width:100%;height:100%;object-fit:contain;object-position:{pos};display:block">', cw, ch))
        icx, icy = cl + cw / 2, ct + ch / 2
        halos = [(icx - 3 * s, icy + 9 * s, 0.386 * w, 0.524 * h, SPOT, 1),
                 (icx - 9 * s, ct + ch + 3 * s, 0.228 * w, 5 * s, FLOOR, 1),
                 (0.175 * w, 0.134 * h, 0.307 * w, 0.302 * h, SOFT, 0.55)]
    else:
        pad = 10 * s
        inner_w = w - 2 * pad
        top = (logo(min(40 * s, inner_w * 0.5), C['rouge'])
               + T(P['categorie'].upper(), 2.1 * s, 500, C['gris2'], 0.2, 1.25, f'margin-top:{8*s:.2f}mm', nom='catégorie')
               + T(P['modele'], min(19 * s, inner_w * 0.2), 600, '#fff', -0.015, 1.0, nom='modèle')
               + T(P['sous_titre'], 3.6 * s, 300, '#E4E5E8', 0, 1.25, f'margin-top:{1.2*s:.2f}mm', nom='sous-titre'))
        args = P.get('arguments', [])[:3]
        tiles = ''.join(f'<div style="flex:1">'
                        f'<div style="height:{0.25*s:.2f}mm;background:{C["trait"]};position:relative"><div style="position:absolute;left:0;top:{-0.15*s:.2f}mm;width:{5*s:.2f}mm;height:{0.55*s:.2f}mm;background:{C["rouge"]}"></div></div>'
                        + T(a['valeur'], 7.5 * s, 600, '#fff', -0.02, 1.0, f'margin-top:{2.5*s:.2f}mm;white-space:nowrap')
                        + T(a['titre'], 2.2 * s, 500, '#fff', 0, 1.25, f'margin-top:{2.2*s:.2f}mm')
                        + T(a['detail'], 2.0 * s, 300, C['gris2'], 0, 1.25) + '</div>' for a in args)
        b = P.get('badge')
        bottom = f'<div style="display:flex;gap:{3.5*s:.2f}mm">{tiles}</div>'
        if b:
            bottom += (f'<div style="margin-top:{5*s:.2f}mm;display:inline-block;background:{C["rouge"]};border-radius:{3*s:.2f}mm;padding:{1*s:.2f}mm {3*s:.2f}mm" class="chk" data-nom="badge">'
                       + T(b['texte'], 2.4 * s, 600, '#fff', 0.14, 1.2, chk=False) + '</div>')
        H.append(f'<div class="abs" style="left:{pad:.2f}mm;top:{pad:.2f}mm;width:{inner_w:.2f}mm;height:{h-2*pad:.2f}mm;display:flex;flex-direction:column">'
                 f'<div>{top}</div><div style="flex:1;min-height:0;margin:{4*s:.2f}mm 0;position:relative">'
                 f'<img class="chk img" data-nom="visuel produit" src="{uri(c.img)}" style="position:absolute;inset:0;width:100%;height:100%;object-fit:contain"></div>'
                 f'<div>{bottom}</div></div>')
        halos = [(w / 2, h * 0.52, 0.6 * w, 0.32 * h, SPOT, 1), (0.2 * w, 0.1 * h, 0.5 * w, 0.2 * h, SOFT, 0.55)]
    return ''.join(H), halos


def face_argument(c, w, h, zones):
    P, C = c.P, c.C
    s = max(0.75, min(1.5, min(w / REF['argument'][0], h / REF['argument'][1])))
    A_ = P.get('face_argument', {})
    idt = A_.get('identite', {})
    H = []
    portrait = w / h < 1.6
    ident = (logo(36 * s, C['rouge']) + T(P['modele'], 11.5 * s, 600, '#fff', -0.015, 1.0, f'margin-top:{4.6*s:.2f}mm;margin-left:{-0.6*s:.2f}mm', nom='modèle')
             + T(idt.get('ligne1', ''), 3.0 * s, 500, '#fff', 0, 1.25, f'margin-top:{2.2*s:.2f}mm')
             + T(idt.get('ligne2', ''), 2.45 * s, 300, C['gris2'], 0, 1.25, f'margin-top:{0.6*s:.2f}mm'))
    badge = (f'<div class="chk" data-nom="badge" style="display:inline-block;border:{0.25*s:.2f}mm solid {C["rouge"]};border-radius:{2.6*s:.2f}mm;padding:{0.85*s:.2f}mm {2.6*s:.2f}mm {0.75*s:.2f}mm">'
             + T(P['badge']['texte'], 2.1 * s, 600, '#fff', 0.14, 1.2, chk=False) + '</div>') if P.get('badge') else ''
    story = ''
    if A_.get('surtitre'):
        story += T(A_['surtitre'], 2.1 * s, 600, C['rouge'], 0.24, 1.25)
    if A_.get('titre'):
        story += T(A_['titre'], 7.2 * s, 600, '#fff', -0.01, 1.08, f'margin-top:{1.2*s:.2f}mm;margin-left:{-0.4*s:.2f}mm', nom='titre')
    if A_.get('titre_2'):
        story += T(A_['titre_2'], 7.2 * s, 300, C['gris2'], -0.01, 1.08, f'margin-left:{-0.4*s:.2f}mm', nom='titre 2')
    if A_.get('texte'):
        story += T(A_['texte'], 2.4 * s, 300, C['gris1'], 0, 1.45, f'margin-top:{2.8*s:.2f}mm', nom='texte')
    note = A_.get('note')
    if note:
        story += (f'<div style="display:flex;align-items:center;gap:{1.6*s:.2f}mm;margin-top:{3.2*s:.2f}mm">{icon(note.get("icone", "plug"), 3.8*s, C["rouge"])}'
                  + T(f'<b style="font-weight:600;color:#fff">{note.get("gras", "")}</b> {note.get("texte", "")}', 2.4 * s, 300, C['gris1'], 0, 1.3, nom='note') + '</div>')
    sch = A_.get('schema')

    def diagram(x0, x1, cy):
        r = 7.2 * s
        out = ''
        def node(cx, n):
            return (at(cx - r, cy - r, f'<div class="chk" data-nom="nœud {n.get("label","")}" style="width:{2*r:.3f}mm;height:{2*r:.3f}mm;border-radius:50%;border:{0.25*s:.2f}mm solid #44474D;background:{C["encre2"]};box-sizing:border-box;display:flex;align-items:center;justify-content:center">{icon(n["icone"], 7*s)}</div>')
                    + center(cx, cy + r + 1.6 * s, T(n['label'], 2.05 * s, 500, C['gris1'], 0.02, 1.2)))
        lx0, lx1 = x0 + 8 * s, x1 - 9 * s
        out += at(lx0 + r, cy - 0.35 * s, '', lx1 - lx0 - 2 * r, 0.7 * s, f'background:{C["rouge"]}')
        out += node(lx0, sch['gauche']) + node(lx1, sch['droite'])
        chips = sch.get('pastilles', [])
        cw_ = 23 * s
        cs = [lx0 + (lx1 - lx0) * (k + 1) / (len(chips) + 1) for k in range(len(chips))]
        for cx, ch_ in zip(cs, chips):
            out += at(cx - cw_ / 2, cy - 2.9 * s, f'<div class="chk" data-nom="pastille {ch_["label"]}" style="width:{cw_:.3f}mm;height:{5.8*s:.3f}mm;border-radius:{2.9*s:.2f}mm;background:{C["noir"]};border:{0.25*s:.2f}mm solid {C["rouge"]};box-sizing:border-box;display:flex;align-items:center;justify-content:center;gap:{1.2*s:.2f}mm">'
                      + icon(ch_['icone'], 3.2 * s) + T(ch_['label'], 2.05 * s, 600, '#fff', 0.06, 1, chk=False) + '</div>')
        if sch.get('legende'):
            mid = (cs[0] + cs[-1]) / 2 if len(cs) >= 2 else (lx0 + lx1) / 2
            out += center(mid, cy + 4.6 * s, T(sch['legende'], 2.0 * s, 400, C['gris2'], 0.04, 1.2))
        return out

    if not portrait:
        H.append(at(11 * s, 12 * s, ident, 0.26 * w))
        if badge:
            H.append(at(11 * s, h - 22.2 * s, badge))
        H.append(at(0.342 * w, 12 * s, '', 0.2 * s, h - 24 * s, f'background:{C["trait"]}'))
        x0, x1 = 0.395 * w, w - 11 * s
        H.append(at(x0, 11.6 * s, story, x1 - x0 - 1 * s))
        if sch:
            H.append(diagram(x0 - 8 * s + 8 * s, x1, h - 29.5 * s))
        halos = [(0.684 * w, 0.667 * h, 0.351 * w, 0.43 * h, SOFT, 0.9)]
    else:
        pad = 10 * s
        diag = ''
        if sch:
            r = 7.2 * s
            def vnode(n):
                return (f'<div style="display:flex;flex-direction:column;align-items:center;flex:none">'
                        f'<div class="chk" data-nom="nœud {n.get("label","")}" style="width:{2*r:.3f}mm;height:{2*r:.3f}mm;border-radius:50%;border:{0.25*s:.2f}mm solid #44474D;background:{C["encre2"]};box-sizing:border-box;display:flex;align-items:center;justify-content:center">{icon(n["icone"], 7*s)}</div>'
                        + T(n['label'], 2.05 * s, 500, C['gris1'], 0.02, 1.2, f'margin-top:{1.4*s:.2f}mm;text-align:center') + '</div>')
            chips = sch.get('pastilles', [])
            cw_ = 23 * s
            chips_html = ''.join(
                f'<div class="chk" data-nom="pastille {c_["label"]}" style="position:absolute;left:50%;top:{(k+1)*100/(len(chips)+1):.2f}%;transform:translate(-50%,-50%);width:{cw_:.3f}mm;height:{5.8*s:.3f}mm;border-radius:{2.9*s:.2f}mm;background:{C["noir"]};border:{0.25*s:.2f}mm solid {C["rouge"]};box-sizing:border-box;display:flex;align-items:center;justify-content:center;gap:{1.2*s:.2f}mm">'
                + icon(c_['icone'], 3.2 * s) + T(c_['label'], 2.05 * s, 600, '#fff', 0.06, 1, chk=False) + '</div>' for k, c_ in enumerate(chips))
            leg = T(sch['legende'], 2.0 * s, 400, C['gris2'], 0.04, 1.2, f'position:absolute;left:{3*s:.2f}mm;top:50%;transform:translateY(-50%);white-space:nowrap;writing-mode:vertical-rl') if False else ''
            diag = (f'<div style="flex:1;min-height:{30*s:.2f}mm;display:flex;flex-direction:column;align-items:center;margin-top:{6*s:.2f}mm">'
                    + vnode(sch['gauche'])
                    + f'<div style="flex:1;width:{0.7*s:.2f}mm;background:{C["rouge"]};position:relative;margin:{2*s:.2f}mm 0">{chips_html}{leg}</div>'
                    + vnode(sch['droite']) + '</div>')
        H.append(f'<div class="abs" style="left:{pad:.2f}mm;top:{pad:.2f}mm;width:{w-2*pad:.2f}mm;height:{h-2*pad:.2f}mm;display:flex;flex-direction:column">'
                 f'<div>{ident}</div>' + (f'<div style="margin-top:{4*s:.2f}mm">{badge}</div>' if badge else '')
                 + f'<div style="margin-top:{7*s:.2f}mm">{story}</div>{diag}</div>')
        halos = [(0.6 * w, 0.7 * h, 0.5 * w, 0.35 * h, SOFT, 0.9)]
    return ''.join(H), halos


def face_application(c, w, h, zones):
    P, C = c.P, c.C
    s = max(0.75, min(1.5, min(w / REF['application'][0], h / REF['application'][1])))
    ap = P['application']
    H = []
    qs = 27 * s
    tx_w = w - 20 * s - qs - 10 * s
    txt = (T(ap['surtitre'], 2.1 * s, 600, C['rouge'], 0.24, 1.25)
           + T(ap['nom'], 5.6 * s, 600, '#fff', -0.01, 1.1, f'margin-top:{1.1*s:.2f}mm;margin-left:{-0.4*s:.2f}mm', nom="nom de l'application")
           + T(ap['texte_fr'], 2.35 * s, 300, C['gris1'], 0, 1.42, f'margin-top:{2.2*s:.2f}mm')
           + T(ap['texte_en'], 2.0 * s, 300, C['gris3'], 0, 1.4, f'margin-top:{1.2*s:.2f}mm;font-style:italic')
           + f'<div class="chk" data-nom="badges stores" style="display:flex;gap:{2.4*s:.2f}mm;margin-top:{3.2*s:.2f}mm;width:max-content">'
           f'<img src="{uri(os.path.join(A, "badge_gplay.png"))}" style="height:{7.6*s:.3f}mm;display:block">'
           f'<div style="border:{0.2*s:.2f}mm solid #A6A6A6;border-radius:{1.25*s:.2f}mm;overflow:hidden;line-height:0">'
           f'<img src="{uri(os.path.join(A, "badge_appstore.png"))}" style="height:{7.2*s:.3f}mm;display:block"></div></div>'
           + T(ap['disponibilite'], 2.0 * s, 400, C['gris2'], 0, 1.25, f'margin-top:{1.6*s:.2f}mm'))
    H.append(at(10 * s, 14.4 * s, txt, tx_w))
    H.append(at(w - 10.5 * s - qs, 14 * s, qr_svg(ap['qr_url'], qs)))
    H.append(at(w - 10.5 * s - qs - 3 * s, 14 * s + qs + 1.4 * s, T(ap['qr_legende'], 1.95 * s, 400, C['gris2'], 0, 1.3, 'text-align:center'), qs + 6 * s))
    eng = ap.get('engagements', [])[:3]
    if eng:
        cw = (w - 20 * s) / len(eng)
        H.append(at(10 * s, h - 30.4 * s, '', w - 20 * s, 0.2 * s, f'background:{C["trait"]}'))
        for k, e in enumerate(eng):
            H.append(at(10 * s + k * cw, h - 24.8 * s, f'<div style="display:flex;gap:{2*s:.2f}mm">{icon(e["icone"], 6*s)}<div>'
                        + T(e['titre'], 2.3 * s, 600, '#fff', 0, 1.2) + T(e['detail'], 2.0 * s, 300, C['gris2'], 0, 1.3) + '</div></div>', cw - 2 * s))
    halos = [(0.792 * w, 0.323 * h, 0.403 * w, 0.43 * h, SOFT, 0.8)]
    return ''.join(H), halos


def face_dos(c, w, h, zones):
    if w / h < 1.8:
        return face_dos_empile(c, w, h, zones)
    P, C = c.P, c.C
    H = []
    m = P['_marque']

    def col_top(x0, x1, default):
        t = default
        for z in zones:
            if z['x'] < x1 and z['x'] + z['w'] > x0 and z['y'] < default + 2:
                t = max(t, z['y'] + z['h'] + 1.5)
        return t
    f = w / REF['dos'][0]
    ax0, ax1 = 7, 7 + 50 * f
    bx0, bx1 = 61 * f, 61 * f + 86 * f
    cx0, cx1 = 152 * f, w - 7
    bottom = h - 10.4
    # colonne A
    colA = (T(P['titre_dos'], 3.2, 600, C['rouge'], 0, 1.25)
            + T(P['sous_titre_dos'], 2.05, 300, '#fff', 0, 1.3, 'margin-top:0.4mm')
            + f'<div style="display:flex;gap:1.4mm;align-items:center;margin-top:2.2mm">{icon("shield-check", 5.2)}<div>'
            + T(m['garantie'][0], 2.0, 500, '#fff', 0, 1.25) + T(m['garantie'][1], 2.0, 300, C['gris2'], 0, 1.25) + '</div></div>'
            + T('<b style="font-weight:600;color:#fff">IMPORTER IN EUROPE :</b><br>' + '<br>'.join(m['importateur']), 1.8, 400, C['gris1'], 0, 1.36, 'margin-top:2.6mm')
            + T('<b style="font-weight:600;color:#fff">SYSTEM REQUIREMENTS :</b><br>' + '<br>'.join(m['configuration']), 1.8, 400, C['gris1'], 0, 1.36, 'margin-top:2.2mm')
            + T(f'© {P["_annee"]} {m["copyright"]}<br>{m["origine"]}', 1.8, 400, C['gris1'], 0, 1.36, 'margin-top:2.2mm'))
    H.append(at(ax0, col_top(ax0, ax1, 7.2), colA, ax1 - ax0))
    certs, cx = '', 0
    for name, hgt in [('ce', 6.2), ('pointvert', 7.2), ('weee', 7.6), ('rohs', 5.6)]:
        if name in m['logos_reglementaires']:
            s_, wl = trace_svg(name, hgt, '#fff')
            certs += s_
    H.append(at(ax0, bottom - 7.6, f'<div class="chk" data-nom="logos réglementaires" style="display:flex;gap:3.4mm;align-items:flex-end;height:7.6mm">{certs}</div>'))
    # colonne B : 4 langues (2 × 2)
    langs = P.get('caracteristiques', {})
    blocks = ''
    for code in ('fr', 'en', 'es', 'de'):
        if code in langs:
            blocks += ('<div>' + T(m['titres_langues'][code], 1.8, 600, '#fff', 0.03, 1.3, 'margin-bottom:0.7mm')
                       + ''.join(T(it, 1.72, 300, C['gris1'], 0, 1.28, chk=False) for it in langs[code]) + '</div>')
    tB = col_top(bx0, bx1, 7.2)
    H.append(at(bx0, tB, f'<div class="chk" data-nom="caractéristiques 4 langues" style="display:grid;grid-template-columns:1fr 1fr;column-gap:2.5mm;row-gap:2.6mm">{blocks}</div>', bx1 - bx0))
    # colonne C : mentions, site, EAN + encart étiquette
    H.append(at(cx0, col_top(cx0, cx1, 7.2), T(m['mentions_legales'], 1.62, 400, C['gris1'], 0, 1.36, 'text-align:left', nom='mentions légales'), cx1 - cx0))
    esvg, ew, eh = ean_svg(P['ean'], P['_ean_mag'])
    box_h = eh + 2.3
    et = bottom - box_h
    H.append(at(cx0, et, f'<div class="chk" data-nom="EAN" style="background:#fff;border-radius:0.8mm;padding:1.4mm 0.9mm 0.9mm;width:{ew:.3f}mm">{esvg}</div>'))
    sw = cx1 - (cx0 + ew + 4.4)
    if sw > 12:
        H.append(at(cx0 + ew + 4.4, et, '', sw, box_h, 'background:#fff;border-radius:0.8mm', cls='chk'))
    H.append(at(cx0, et - 9.4, T('PLUS D’INFORMATIONS', 1.6, 500, C['gris3'], 0.14, 1.2) + T(m['site'], 2.7, 600, '#fff', 0, 1.3)))
    return ''.join(H), []


def dos_blocs(c):
    P, C = c.P, c.C
    m = P['_marque']
    tete = (T(P['titre_dos'], 3.2, 600, C['rouge'], 0, 1.25)
            + T(P['sous_titre_dos'], 2.05, 300, '#fff', 0, 1.3, 'margin-top:0.4mm')
            + f'<div style="display:flex;gap:1.4mm;align-items:center;margin-top:2.2mm">{icon("shield-check", 5.2)}<div>'
            + T(m['garantie'][0], 2.0, 500, '#fff', 0, 1.25) + T(m['garantie'][1], 2.0, 300, C['gris2'], 0, 1.25) + '</div></div>')
    admin = (T('<b style="font-weight:600;color:#fff">IMPORTER IN EUROPE :</b><br>' + '<br>'.join(m['importateur']), 1.8, 400, C['gris1'], 0, 1.36)
             + T('<b style="font-weight:600;color:#fff">SYSTEM REQUIREMENTS :</b><br>' + '<br>'.join(m['configuration']), 1.8, 400, C['gris1'], 0, 1.36, 'margin-top:2.2mm')
             + T(f'© {P["_annee"]} {m["copyright"]}<br>{m["origine"]}', 1.8, 400, C['gris1'], 0, 1.36, 'margin-top:2.2mm'))
    certs = ''.join(trace_svg(n, hg, '#fff')[0] for n, hg in [('ce', 6.2), ('pointvert', 7.2), ('weee', 7.6), ('rohs', 5.6)]
                    if n in m['logos_reglementaires'])
    certs = f'<div class="chk" data-nom="logos réglementaires" style="display:flex;gap:3.4mm;align-items:flex-end;height:7.6mm">{certs}</div>'
    langs = P.get('caracteristiques', {})
    blocks = ''.join('<div>' + T(m['titres_langues'][k], 1.8, 600, '#fff', 0.03, 1.3, 'margin-bottom:0.7mm')
                     + ''.join(T(it, 1.72, 300, C['gris1'], 0, 1.28, chk=False) for it in langs[k]) + '</div>'
                     for k in ('fr', 'en', 'es', 'de') if k in langs)
    langues = f'<div class="chk" data-nom="caractéristiques 4 langues" style="display:grid;grid-template-columns:1fr 1fr;column-gap:2.5mm;row-gap:2.6mm">{blocks}</div>'
    legal = T(m['mentions_legales'], 1.62, 400, C['gris1'], 0, 1.36, 'text-align:left', nom='mentions légales')
    esvg, ew, eh = ean_svg(P['ean'], P['_ean_mag'])
    ean = f'<div class="chk" data-nom="EAN" style="background:#fff;border-radius:0.8mm;padding:1.4mm 0.9mm 0.9mm;width:{ew:.3f}mm;flex:none">{esvg}</div>'
    site = T('PLUS D’INFORMATIONS', 1.6, 500, C['gris3'], 0.14, 1.2) + T(m['site'], 2.7, 600, '#fff', 0, 1.3)
    return tete, admin, certs, langues, legal, ean, ew, eh, site


def face_dos_empile(c, w, h, zones):
    tete, admin, certs, langues, legal, ean, ew, eh, site = dos_blocs(c)
    top = 7.2
    for z in zones:
        if z['y'] < 9:
            top = max(top, z['y'] + z['h'] + 1.5)
    box_h = eh + 2.3
    inner = (f'<div style="display:flex;flex-direction:column;gap:3mm;height:100%">'
             f'<div>{tete}</div>'
             f'<div style="display:grid;grid-template-columns:1fr 1.25fr;column-gap:3mm">{admin}<div>{legal}</div></div>'
             f'{langues}<div style="flex:1"></div>'
             f'<div style="display:flex;align-items:flex-end;justify-content:space-between;gap:3mm"><div>{site}</div>{certs}</div>'
             f'<div style="display:flex;gap:2.5mm;align-items:flex-end">{ean}<div class="chk" data-nom="encart étiquette" style="flex:1;max-width:40mm;height:{box_h:.2f}mm;background:#fff;border-radius:0.8mm"></div></div></div>')
    return at(7, top, inner, w - 14, h - top - 7), []


def face_fiche(c, w, h, zones):
    P, C = c.P, c.C
    H = []
    specs = P.get('fiche_technique', [])
    ncols = 2 if w >= 120 else 1
    rows = math.ceil(len(specs) / ncols) or 1
    etroit = w < 110
    top = 30.0 if etroit else 21.0
    rh = min(8.05, (h - top - 7.5) / rows)
    if rh < 6.3:
        c.warn.append({'face': 'fiche', 'type': f'trop de lignes ({len(specs)}) : interligne {rh:.1f} mm (< 6,3 mm)', 'element': 'fiche technique'})
    if etroit:
        H.append(at(10, 10, logo(min(22.3, w - 20), '#fff')))
        H.append(at(10, 18.5, T('FICHE TECHNIQUE<br>SPECIFICATIONS', 2.05, 600, C['rouge'], 0.2, 1.3), w - 20))
        H.append(at(10, 27.6, '', w - 20, 0.25, f'background:{C["trait"]}'))
    else:
        H.append(at(10, 13, T('FICHE TECHNIQUE · SPECIFICATIONS', 2.05, 600, C['rouge'], 0.2)))
        H.append(at(w - 10 - 22.3, 11.6, logo(22.3, '#fff')))
        H.append(at(10, 18.8, '', w - 20, 0.25, f'background:{C["trait"]}'))
    cw = (w - 20 - (ncols - 1) * 3.9) / ncols
    for k, (lab, val) in enumerate(specs):
        col, r = k // rows, k % rows
        x = 10 + col * (cw + 3.9)
        y = top + r * rh
        H.append(at(x, y, T(lab.upper(), 1.6, 500, C['gris3'], 0.08, 1.2) + T(val, 2.35, 400, '#fff', 0, 1.3), cw, cls=''))
        if r < rows - 1 and k < len(specs) - 1:
            H.append(at(x, y + rh - 0.9, '', cw, 0.15, 'background:#202226'))
    return ''.join(H), []


def face_rabat(c, w, h, zones):
    P, C = c.P, c.C
    s = max(0.75, min(1.4, min(w / REF['rabat'][0], h / REF['rabat'][1])))
    rb = P['rabat']
    H = []
    y0 = 30 * s if h >= 100 else 12 * s
    for z in zones:
        if z['y'] < y0 and z['x'] < w * 0.65 and z['x'] + z['w'] > w * 0.35:
            y0 = max(y0, z['y'] + z['h'] + 6 * s)
    H.append(at((w - 40 * s) / 2, y0, logo(40 * s, '#fff')))
    H.append(center(w / 2, y0 + 12.5 * s, T(rb['titre'], 5.0 * s, 500, '#fff', -0.005, 1.2)))
    H.append(center(w / 2, y0 + 20.4 * s, T(rb['sous_titre'], 3.3 * s, 300, C['gris2'], 0, 1.2)))
    H.append(at((w - 16 * s) / 2, y0 + 27.6 * s, '', 16 * s, 0.6 * s, f'background:{C["rouge"]}'))
    steps = rb.get('etapes', [])[:3] if h >= 100 else []
    gap = 9 * s
    sw_ = min(52 * s, (w - 20 - 2 * gap) / 3)
    x_start = (w - (len(steps) * sw_ + (len(steps) - 1) * gap)) / 2
    for k, st in enumerate(steps):
        H.append(at(x_start + k * (sw_ + gap), y0 + 40 * s, T(f'{k+1:02d}', 7 * s, 600, C['rouge'], -0.02, 1)
                    + T(st[0], 3.0 * s, 600, '#fff', 0, 1.3, f'margin-top:{1.6*s:.2f}mm') + T(st[1], 2.3 * s, 300, C['gris1'], 0, 1.4, f'margin-top:{0.6*s:.2f}mm'), sw_))
    H.append(center(w / 2, h - 29.75 * s if h > 100 else h - 12, T(rb['aide'], 2.3 * s, 400, C['gris2'], 0.02, 1.2)))
    return ''.join(H), [(0.5 * w, 0.564 * h, 0.439 * w, 0.423 * h, SOFT, 0.8)]


def face_identite(c, w, h, zones):
    P, C = c.P, c.C
    s = max(0.6, min(1.4, min(w / 120, h / 80)))
    inner = (f'<div style="display:flex;flex-direction:column;align-items:center;justify-content:center;width:{w:.2f}mm;height:{h:.2f}mm;gap:{2.5*s:.2f}mm">'
             + logo(36 * s, C['rouge']) + T(P['modele'], 11 * s, 600, '#fff', -0.015, 1.0, nom='modèle')
             + T(P['sous_titre'], 2.6 * s, 300, C['gris2'], 0, 1.25, 'text-align:center') + '</div>')
    return at(0, 0, inner), [(0.5 * w, 0.5 * h, 0.5 * w, 0.5 * h, SOFT, 0.7)]


TEMPLATES = {'hero': face_hero, 'argument': face_argument, 'application': face_application, 'dos': face_dos,
             'fiche': face_fiche, 'rabat': face_rabat, 'identite': face_identite}


# ======================================================================== assemblage
def bleed_for(role, faces, sans_encre):
    """Fond perdu de 3 mm sur les bords non partagés avec une autre face (repère à plat : g, h, d, b)."""
    x, y, w, h = faces[role]['rect']
    def shared(ex0, ey0, ex1, ey1):
        for r2, f2 in faces.items():
            if r2 == role:
                continue
            X, Y, W, H = f2['rect']
            if abs(ex0 - ex1) < 0.01:   # bord vertical
                if (abs(X - ex0) < 0.6 or abs(X + W - ex0) < 0.6) and min(ey1, Y + H) - max(ey0, Y) > 5:
                    return True
            else:
                if (abs(Y - ey0) < 0.6 or abs(Y + H - ey0) < 0.6) and min(ex1, X + W) - max(ex0, X) > 5:
                    return True
        return False
    b = [0 if shared(x, y, x, y + h) else 3, 0 if shared(x, y, x + w, y) else 3,
         0 if shared(x + w, y, x + w, y + h) else 3, 0 if shared(x, y + h, x + w, y + h) else 3]
    return faces[role].get('fond_perdu', b)


def build_html(P, G, mode, tmp, warn):
    C = P['couleurs']
    px, py, pw, ph = G['planche']
    band = 180 if mode == 'bat' else 0
    faces = G['faces']
    img = prepare_image(P, tmp)
    ctx = Ctx(P, C, tmp, img)
    ctx.warn = warn
    bg = []
    for t in G['traits']:
        if t['type'] != 'coupe' or t.get('fond') is False:
            continue
        x0, y0, x1, y1 = t['bbox']
        hole = any(x0 > f['rect'][0] + 1 and x1 < f['rect'][0] + f['rect'][2] - 1 and y0 > f['rect'][1] - 15
                   and y1 < f['rect'][1] + f['rect'][3] - 1 and (x1 - x0) < 0.6 * f['rect'][2] and (y1 - y0) < 0.6 * f['rect'][3]
                   for f in faces.values())
        if hole:
            continue
        bg.append(f'<path d="{t["d"]}" fill="{C["noir"]}" stroke="{C["noir"]}" stroke-width="6" stroke-linejoin="miter"/>')
    for r in G.get('sans_encre', []):
        bg.append(f'<rect x="{r[0]}" y="{r[1]}" width="{r[2]}" height="{r[3]}" fill="#FFFFFF"/>')

    H = []
    for role, f in faces.items():
        x, y, w, h = f['rect']
        rot = f.get('rotation', 0)
        tpl = f.get('gabarit', role if role in TEMPLATES else 'identite')
        zones = [z for z in G.get('zones_reservees', []) if z['face'] == role and z.get('h', 0) > 0]
        html, halos = TEMPLATES[tpl](ctx, w, h, zones)
        bl, bt, br, bb = bleed_for(role, faces, G.get('sans_encre', []))
        if rot == 180:
            bl, bt, br, bb = br, bb, bl, bt
        light = ''
        if halos:
            lp = lumiere(tmp, w, h, (bl, bt, br, bb), halos, C['noir'])
            light = f'<img src="{uri(lp)}" style="position:absolute;left:{-bl}mm;top:{-bt}mm;width:{w+bl+br}mm;height:{h+bt+bb}mm">'
        # zones réservées en repère page (pour les contrôles)
        zp = []
        mmpx = 96 / 25.4
        for z in zones:
            zx, zy = (w - z['x'] - z['w'], h - z['y'] - z['h']) if rot == 180 else (z['x'], z['y'])
            zp.append({'x': x + zx - px, 'y': y + zy - py, 'w': z['w'], 'h': z['h'], 'nom': z.get('type', 'zone')})
        H.append(f'<div class="abs face" data-role="{role}" data-zones=\'{json.dumps(zp)}\' style="left:{x}mm;top:{y}mm;width:{w}mm;height:{h}mm;'
                 f'transform:rotate({rot}deg);transform-origin:center">{light}{html}</div>')

    ov = []
    if mode == 'bat':
        ov = annotations(P, G, faces)
    ff = ''.join(f"@font-face{{font-family:'Poppins';font-weight:{wt};src:url('{uri(os.path.join(A, 'polices', f'poppins-latin-{wt}-normal.woff2'))}') format('woff2');}}"
                 for wt in (300, 400, 500, 600, 700))
    if mode == 'bat':
        ff += cjk_css(''.join(ov), tmp)
    W = pw + band
    return f'''<!doctype html><html lang="fr"><head><meta charset="utf-8"><style>{ff}
@page {{ size:{W}mm {ph}mm; margin:0 }}
html,body {{ margin:0; padding:0; background:#fff }}
body {{ font-family:'Poppins',sans-serif; -webkit-print-color-adjust:exact; print-color-adjust:exact; text-rendering:geometricPrecision }}
#sheet {{ position:relative; width:{W}mm; height:{ph}mm; overflow:hidden; background:#fff }}
.abs {{ position:absolute }}
#content {{ position:absolute; left:{-px}mm; top:{-py}mm; width:{abs(px)+pw+400}mm; height:{abs(py)+ph+400}mm }}
svg.layer {{ position:absolute; left:0; top:0 }}
</style></head><body><div id="sheet">
<svg class="layer" viewBox="{px} {py} {pw} {ph}" style="width:{pw}mm;height:{ph}mm">{''.join(bg)}</svg>
<div id="content">{''.join(H)}</div>
<svg class="layer" viewBox="{px} {py} {W} {ph}" style="width:{W}mm;height:{ph}mm">{''.join(ov)}</svg>
</div></body></html>''', W, ph


PHYS = {'dessus': ('TOP / LID', '盖面'), 'avant': ('FRONT', '正面'), 'droite': ('RIGHT SIDE', '右侧面'),
        'arriere': ('BACK', '背面'), 'gauche': ('LEFT SIDE', '左侧面'), 'rabat': ('INNER FLAP', '内折页')}


def annotations(P, G, faces):
    px, py, pw, ph = G['planche']
    MAG = '#EC008C'
    ANNO = "Poppins, 'Noto Sans SC', sans-serif"
    ov = []
    for t in G['traits']:
        col = {'coupe': MAG, 'special': '#00AEEF', 'repere': MAG}[t['type']]
        dash = ' stroke-dasharray="1.2 0.8"' if t['type'] == 'special' else ''
        ov.append(f'<path d="{t["d"]}" fill="none" stroke="{col}" stroke-width="0.18"{dash}/>')
    tops = [t['bbox'] for t in G['traits']]
    for role, f in faces.items():
        x, y, w, h = f['rect']
        en, cn = PHYS.get(f.get('physique', ''), (role.upper(), ''))
        lab = f'{en}   {cn}'
        if role == 'hero':
            lab = f'{en} · MAIN FACE   {cn}（主展示面）'
        if f.get('rotation') == 180:
            lab = f'{en} · PRINTED UPSIDE DOWN   {cn}（倒印）'
        half = len(lab) * 1.0
        span = [b for b in tops if b[0] < x + w / 2 + half and b[2] > x + w / 2 - half]
        if f.get('physique') in ('avant', 'droite', 'arriere', 'gauche'):
            yy = max(b[3] for b in span if b[1] >= y - 1) + 6
        else:
            yy = min(b[1] for b in span if b[3] <= y + h + 1) - 3.5
        ov.append(f'<text x="{x + w/2}" y="{yy}" text-anchor="middle" font-family="{ANNO}" font-weight="600" font-size="3.2" fill="{MAG}" letter-spacing="0.25">{lab}</text>')
    for r in G.get('sans_encre', []):
        ov.append(f'<text transform="translate({r[0] + r[2] - 4.5} {r[1] + r[3]/2}) rotate(-90)" text-anchor="middle" font-family="{ANNO}" '
                  f'font-weight="600" font-size="2.4" fill="{MAG}">GLUE · NO INK   糊口位不印刷</text>')
    fab = G.get('fabricant', {})
    L, Wd, Hd = G['dimensions_mm']
    v = P.get('version', '1')
    has_inner = any(f.get('rotation') == 180 and f.get('physique') == 'rabat' for f in faces.values())
    tb = [(f'DAEWOO {P["modele"]} — PACKAGING ARTWORK · 包装设计稿', 600, 3.4, '#111'),
          (f'Version {v} — {P["_date_en"]} · 第{v}版', 400, 2.6, '#555'), ('', 400, 1.2, '#111'),
          (f'Box size · 尺寸：{L:g} × {Wd:g} × {Hd:g} mm' + (f' (supplier dieline {fab["reference"]})' if fab.get('reference') else ''), 400, 2.6, '#111')]
    if fab.get('matiere_cn') or fab.get('matiere_en'):
        tb.append((f'Material · 材质：{fab.get("matiere_cn", "")}', 400, 2.6, '#111'))
        if fab.get('matiere_en'):
            tb.append((f'({fab["matiere_en"]})', 400, 2.4, '#555'))
    tb += [(f'Printing · 要求：{fab.get("impression_cn", "四色印刷")} CMYK, {fab.get("finition_en", "matte lamination")}', 400, 2.6, '#111'),
           ('', 400, 1.2, '#111'),
           ('Page 1: layout check with dieline · 第1页：刀模线对位稿', 600, 2.6, '#111'),
           ('Page 2: print-ready artwork, 3 mm bleed · 第2页：印刷文件（出血3mm）', 600, 2.6, '#111'),
           ('Page 3: 3D reference · 第3页：效果图', 600, 2.6, '#111'), ('', 400, 1.2, '#111'),
           ('Magenta line = die-cut / crease, do not print · 品红线 = 刀模线（不印刷）', 400, 2.6, MAG)]
    if any(t['type'] == 'special' for t in G['traits']):
        tb.append(('Cyan dashed line = hang tab / special cut · 青色虚线 = 挂钩位', 400, 2.6, '#0090C8'))
    if G.get('sans_encre'):
        tb.append(('Glue flap: no ink · 糊口位不印刷', 400, 2.6, '#111'))
    tb.append(('Lid artwork reads from the FRONT panel · 盖面文字朝正面方向', 400, 2.6, '#111'))
    if has_inner:
        tb.append(('Inner flap printed upside down · 内折页倒印', 400, 2.6, '#111'))
    tb += [('Factory label: white box next to barcode (back) · 贴纸位置：背面条码旁白框', 400, 2.6, '#111'),
           (f'Barcode EAN-13: {P["ean"]} ({round(P["_ean_mag"]*100)} %) · 条码', 400, 2.6, '#111'),
           ('All text converted to outlines · 文字已转曲', 400, 2.6, '#111')]
    x0 = px + pw + 6
    yy = py + 14
    for line, wgt, fs, col in tb:
        if line:
            ov.append(f'<text x="{x0+5}" y="{yy:.2f}" font-family="{ANNO}" font-weight="{wgt}" font-size="{fs}" fill="{col}">{line}</text>')
        yy += fs * 1.75
    ov.append(f'<rect x="{x0}" y="{py+5}" width="168" height="{yy - py - 5 + 1:.2f}" fill="none" stroke="#111" stroke-width="0.2"/>')
    return ov


def cjk_css(text, tmp):
    """Charge les fichiers Noto Sans SC couvrant les caractères chinois utilisés (téléchargement npm si besoin)."""
    chars = {ch for ch in text if ord(ch) >= 0x2E80}
    base = os.path.join(A, 'polices', 'notosc')
    css = open(os.path.join(base, 'notosc.css'), encoding='utf-8').read()
    def covered(css_text):
        cov = set()
        for block in re.findall(r'@font-face\s*\{.*?\}', css_text, re.S):
            if 'font-weight: 400' not in block and 'font-weight:400' not in block:
                continue
            for part in re.search(r'unicode-range:\s*([^;]+);', block).group(1).split(','):
                part = part.strip().replace('U+', '')
                a, b = (part.split('-') + [part])[:2]
                for ch in chars:
                    if int(a, 16) <= ord(ch) <= int(b, 16):
                        cov.add(ch)
        return cov
    missing = chars - covered(css)
    if missing:
        cache = os.path.expanduser('~/.cache/daewoo-boite/notosc')
        if not os.path.exists(os.path.join(cache, 'package', '400.css')):
            os.makedirs(cache, exist_ok=True)
            subprocess.run(['npm', 'pack', '@fontsource/noto-sans-sc', '--silent', '--pack-destination', cache], check=True)
            tgz = [f for f in os.listdir(cache) if f.endswith('.tgz')][0]
            subprocess.run(['tar', 'xzf', os.path.join(cache, tgz), '-C', cache], check=True)
        add = []
        for wt in ('400', '600'):
            full = open(os.path.join(cache, 'package', f'{wt}.css'), encoding='utf-8').read()
            for block in re.findall(r'@font-face\s*\{.*?\}', full, re.S):
                rng = re.search(r'unicode-range:\s*([^;]+);', block).group(1)
                if any(any(int((p.strip().replace('U+', '').split('-') + [p.strip().replace('U+', '')])[0], 16) <= ord(ch) <=
                           int((p.strip().replace('U+', '').split('-') + [p.strip().replace('U+', '')])[1], 16) for p in rng.split(','))
                       for ch in missing):
                    fn = re.search(r"url\(\./files/([^)]+\.woff2)\)", block).group(1)
                    shutil.copy(os.path.join(cache, 'package', 'files', fn), os.path.join(base, fn))
                    add.append(re.sub(r"src:[^;]+;", f"src:url('../assets/notosc/{fn}') format('woff2');", block))
        css += '\n' + '\n'.join(add)
        open(os.path.join(base, 'notosc.css'), 'w', encoding='utf-8').write(css)
        print(f'  police chinoise complétée ({len(missing)} caractères)')
    return css.replace("url('../assets/notosc/", f"url('{uri(base)}/")


def prepare_image(P, tmp):
    src = os.path.join(P['_dossier'], P['image'])
    im = Image.open(src).convert('RGBA')
    a = im.getchannel('A')
    if a.getextrema()[0] == 255:
        raise SystemExit(f'Le visuel {src} n’a pas de fond transparent : fournir un PNG/WebP détouré.')
    im = im.crop(a.point(lambda v: 255 if v > 8 else 0).getbbox())
    out = os.path.join(tmp, 'produit_detoure.png')
    im.save(out)
    dpi = im.height / (0.8 * 149 / 25.4)
    if im.height < 1200:
        print(f'  ⚠ visuel produit de {im.width}×{im.height} px : risque de flou à l’impression (viser 2000 px de haut)')
    return out


# ======================================================================== 3D et page de référence
def mockup_html(G, faces_png, view, out):
    by = {f['physique']: (r, f) for r, f in G['faces'].items()}
    k = 3.7
    L = G['dimensions_mm'][0] * k
    W = G['dimensions_mm'][1] * k
    Hh = G['dimensions_mm'][2] * k
    rot = 'rotateX(-27deg) rotateY(-29deg)' if view == 'avant' else 'rotateX(-27deg) rotateY(151deg)'
    def face(phys, w, h, tf, shade):
        if phys not in by:
            return f'<div class="f" style="width:{w}px;height:{h}px;margin-left:{-w/2}px;margin-top:{-h/2}px;transform:{tf};background:#0B0B0D"></div>'
        role, f = by[phys]
        return (f'<div class="f" style="width:{w}px;height:{h}px;margin-left:{-w/2}px;margin-top:{-h/2}px;transform:{tf};'
                f'background-image:url({uri(faces_png[role])})"><div class="sh" style="background:{shade}"></div></div>')
    fs = [face('avant', L, Hh, f'translateZ({W/2}px)', 'linear-gradient(180deg,rgba(255,255,255,.05),rgba(0,0,0,.10))'),
          face('droite', W, Hh, f'rotateY(90deg) translateZ({L/2}px)', 'linear-gradient(90deg,rgba(0,0,0,.30),rgba(0,0,0,.42))'),
          face('arriere', L, Hh, f'rotateY(180deg) translateZ({W/2}px)', 'linear-gradient(180deg,rgba(255,255,255,.04),rgba(0,0,0,.12))'),
          face('gauche', W, Hh, f'rotateY(-90deg) translateZ({L/2}px)', 'linear-gradient(90deg,rgba(0,0,0,.38),rgba(0,0,0,.28))'),
          face('dessus', L, W, f'rotateX(90deg) translateZ({Hh/2}px)', 'linear-gradient(160deg,rgba(255,255,255,.10),rgba(255,255,255,0) 55%)')]
    big = max(L, W, Hh)
    zoom = min(1.0, 900 / big)
    open(out, 'w').write(f'''<!doctype html><html><head><meta charset="utf-8"><style>
html,body{{margin:0;height:100%}}
body{{width:1600px;height:1100px;overflow:hidden;background:radial-gradient(ellipse 70% 60% at 50% 42%,#f4f5f6 0%,#e2e4e7 55%,#cfd2d6 100%)}}
.stage{{position:absolute;left:50%;top:50%;perspective:3600px;perspective-origin:50% 30%;zoom:{zoom:.3f}}}
.box{{position:absolute;transform-style:preserve-3d;transform:translate(0px,40px) {rot}}}
.f{{position:absolute;left:0;top:0;background-size:100% 100%;backface-visibility:hidden;outline:1px solid rgba(255,255,255,.05);outline-offset:-1px}}
.sh{{position:absolute;inset:0}}
.shadow{{position:absolute;left:50%;top:50%;width:1300px;height:340px;margin-left:-650px;margin-top:170px;
background:radial-gradient(ellipse 50% 50% at 50% 50%,rgba(0,0,0,.34),rgba(0,0,0,.14) 45%,rgba(0,0,0,0) 72%);filter:blur(8px)}}
</style></head><body><div class="shadow"></div><div class="stage"><div class="box">{"".join(fs)}</div></div></body></html>''')


def ref_html(P, out, front, back, W, H):
    ff = ''.join(f"@font-face{{font-family:'Poppins';font-weight:{wt};src:url('{uri(os.path.join(A, 'polices', f'poppins-latin-{wt}-normal.woff2'))}') format('woff2');}}" for wt in (400, 600))
    txt = ('For reference only: shows how each panel is oriented once the box is folded. · 仅供参考：展示折盒后各面方向。<br>'
           'Lid artwork reads from the FRONT panel. Inner flap is printed upside down so it reads correctly when the box is opened. · 盖面文字朝正面方向；内折页倒印，开盒时正向阅读。')
    ff += cjk_css(txt + '效果图正面背面', os.path.dirname(out))
    iw = (W - 54) / 2
    ih = min(H - 97, iw / 1.247)
    open(out, 'w', encoding='utf-8').write(f'''<!doctype html><html><head><meta charset="utf-8"><style>{ff}
@page {{ size:{W}mm {H}mm; margin:0 }}
html,body {{ margin:0; background:#fff; font-family:Poppins,'Noto Sans SC',sans-serif; -webkit-print-color-adjust:exact; print-color-adjust:exact }}
.sheet {{ position:relative; width:{W}mm; height:{H}mm; overflow:hidden }}
h1 {{ position:absolute; left:20mm; top:14mm; margin:0; font-size:7mm; font-weight:600; color:#111 }}
.note {{ position:absolute; left:20mm; top:26mm; font-size:3.6mm; color:#444; line-height:1.55 }}
.img {{ position:absolute; top:46mm; width:{iw:.2f}mm; height:{ih:.2f}mm; object-fit:cover; border-radius:3mm }}
.cap {{ position:absolute; top:{46+ih+6:.2f}mm; font-size:4mm; font-weight:600; color:#111 }}
</style></head><body><div class="sheet">
<h1>DAEWOO {P["modele"]} — 3D REFERENCE · 效果图</h1><div class="note">{txt}</div>
<img class="img" style="left:20mm" src="{uri(front)}"><img class="img" style="left:{34+iw:.2f}mm" src="{uri(back)}">
<div class="cap" style="left:20mm">FRONT VIEW · 正面效果</div><div class="cap" style="left:{34+iw:.2f}mm">BACK VIEW · 背面效果</div>
</div></body></html>''')


# ======================================================================== principal
def run(cmd):
    r = subprocess.run(cmd, capture_output=True, text=True)
    if r.returncode != 0:
        sys.exit(f'Échec : {" ".join(cmd)}\n{r.stderr[-2000:]}')
    return r.stdout


def main():
    if len(sys.argv) < 2:
        print(__doc__)
        sys.exit(1)
    dossier = os.path.abspath(sys.argv[1])
    brouillon = '--brouillon' in sys.argv
    marque = json.load(open(os.path.join(MOTEUR, 'marque.json'), encoding='utf-8'))
    produit = json.load(open(os.path.join(dossier, 'produit.json'), encoding='utf-8'))
    G = json.load(open(os.path.join(dossier, 'gabarit.json'), encoding='utf-8'))
    P = deep_merge({k: v for k, v in marque.items() if not k.startswith('_')}, produit)
    P['_marque'] = P
    P['_dossier'] = dossier
    today = datetime.date.today()
    P['_annee'] = P.get('annee', today.year)
    P['_date_en'] = P.get('date_en', today.strftime('%d %b %Y'))
    P['_ean_mag'] = P.get('ean_grossissement', 0.85)
    for k in ('modele', 'ean', 'image', 'categorie', 'sous_titre'):
        if not P.get(k):
            sys.exit(f'Champ obligatoire manquant dans produit.json : « {k} »')
    P.setdefault('titre_dos', f"{P['categorie']} {P['modele']}")
    P.setdefault('sous_titre_dos', f"DAEWOO – {P['sous_titre']}")
    if P['_ean_mag'] < 0.8:
        sys.exit('EAN : grossissement minimal 80 % (ean_grossissement ≥ 0.8)')
    ean = str(P['ean'])
    if not re.fullmatch(r'\d{13}', ean) or ean_checksum(ean[:12]) != ean[12]:
        sys.exit(f'EAN invalide : {ean} (13 chiffres, clé de contrôle attendue {ean_checksum(ean[:12]) if re.fullmatch(r"[0-9]{12,13}", ean) else "?"})')
    modele = re.sub(r'[^A-Za-z0-9_-]', '', P['modele'])
    tmp = os.path.join(tempfile.gettempdir(), f'boite_{modele}')
    os.makedirs(os.path.join(tmp, 'faces'), exist_ok=True)
    warn = []

    print(f'› Mise en page {P["modele"]}…')
    html, W, Hh = build_html(P, G, 'impression', tmp, warn)
    open(os.path.join(tmp, 'impression.html'), 'w', encoding='utf-8').write(html)
    run(['node', os.path.join(MOTEUR, 'outils.js'), 'pdf', os.path.join(tmp, 'impression.html'), os.path.join(tmp, 'impression'), str(W), str(Hh), '3'])
    warn += json.load(open(os.path.join(tmp, 'impression.controle.json'), encoding='utf-8'))

    # faces découpées (contrôle visuel + 3D), remises à l'endroit
    im = Image.open(os.path.join(tmp, 'impression.png'))
    sc = im.width / W
    px, py = G['planche'][0], G['planche'][1]
    faces_png = {}
    for role, f in G['faces'].items():
        x, y, w, h = f['rect']
        c = im.crop(tuple(int(round(v * sc)) for v in (x - px, y - py, x - px + w, y - py + h)))
        if f.get('rotation') == 180:
            c = c.rotate(180)
        faces_png[role] = os.path.join(tmp, 'faces', f'{role}.png')
        c.save(faces_png[role])

    fonts = run(['pdffonts', os.path.join(tmp, 'impression.pdf')])
    for line in fonts.splitlines()[2:]:
        name = line.split()[0].split('+')[-1]
        if not name.startswith(('Poppins', 'JetBrainsMono')):
            warn.append({'face': '-', 'type': f'police de secours utilisée ({name}) : un caractère manque dans Poppins', 'element': '-'})

    if not brouillon:
        print('› Planche BAT, 3D et dossier fournisseur…')
        html, Wb, _ = build_html(P, G, 'bat', tmp, [])
        open(os.path.join(tmp, 'bat.html'), 'w', encoding='utf-8').write(html)
        run(['node', os.path.join(MOTEUR, 'outils.js'), 'pdf', os.path.join(tmp, 'bat.html'), os.path.join(tmp, 'bat'), str(Wb), str(Hh), '1.5'])
        for v in ('avant', 'arriere'):
            mockup_html(G, faces_png, v, os.path.join(tmp, f'3d_{v}.html'))
            run(['node', os.path.join(MOTEUR, 'outils.js'), 'shot', os.path.join(tmp, f'3d_{v}.html'), os.path.join(tmp, f'3d_{v}.png'), '1600', '1100', '2'])
        ref_html(P, os.path.join(tmp, 'ref.html'), os.path.join(tmp, '3d_avant.png'), os.path.join(tmp, '3d_arriere.png'), W, Hh)
        run(['node', os.path.join(MOTEUR, 'outils.js'), 'pdf', os.path.join(tmp, 'ref.html'), os.path.join(tmp, 'ref'), str(W), str(Hh), '1'])
        gs = ['gs', '-q', '-dSAFER', '-dBATCH', '-dNOPAUSE', '-sDEVICE=pdfwrite', '-sColorConversionStrategy=CMYK',
              '-sProcessColorModel=DeviceCMYK', '-dCompatibilityLevel=1.6', '-dAutoRotatePages=/None', '-dNoOutputFonts']
        run(gs + [f'-sOutputFile={dossier}/{modele}_DAEWOO_dossier_fournisseur.pdf', f'{tmp}/bat.pdf', f'{tmp}/impression.pdf', f'{tmp}/ref.pdf'])
        run(gs + [f'-sOutputFile={dossier}/{modele}_impression_CMJN.pdf', f'{tmp}/impression.pdf'])
        shutil.copy(f'{tmp}/impression.pdf', f'{dossier}/{modele}_impression_RVB.pdf')
        for v in ('avant', 'arriere'):
            Image.open(f'{tmp}/3d_{v}.png').convert('RGB').save(f'{dossier}/{modele}_maquette_3D_{v}.jpg', quality=92, subsampling=0)
        b = Image.open(f'{tmp}/bat.png').convert('RGB')
        b.thumbnail((4000, 4000))
        b.save(f'{dossier}/{modele}_a_plat_avec_gabarit.png', optimize=True)
        hero = Image.open(faces_png['hero']).convert('RGB')
        hero.save(f'{dossier}/{modele}_face_principale.png', optimize=True)

    json.dump(warn, open(os.path.join(tmp, 'controles.json'), 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
    print(f'\nFaces à contrôler (à l’endroit) : {tmp}/faces/*.png')
    if warn:
        print(f'⚠ {len(warn)} alerte(s) de mise en page :')
        for x in warn:
            print(f'  - [{x["face"]}] {x["type"]} : {x["element"]}')
    else:
        print('✓ Aucun débordement, chevauchement ni empiètement détecté.')
    if not brouillon:
        print(f'Livrables écrits dans {dossier}')


if __name__ == '__main__':
    main()
