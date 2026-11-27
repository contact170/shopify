# Génère la maquette HTML/SVG de la boîte DAEWOO EF503 (coordonnées en mm, repère page du gabarit fabricant)
import json, re, os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from ean import modules as ean_modules

ROOT = os.path.dirname(os.path.abspath(__file__))
A = os.path.join(ROOT, '..', 'assets')
MODE = sys.argv[1] if len(sys.argv) > 1 else 'proof'   # proof | print
OUT = sys.argv[2] if len(sys.argv) > 2 else os.path.join(ROOT, f'box_{MODE}.html')

# ---------------------------------------------------------------- palette
BLACK = '#0B0B0D'
INK2 = '#141518'
LINE = '#2E3035'
GRAY1 = '#C9CBD0'
GRAY2 = '#9FA2A9'
GRAY3 = '#6E7178'
RED = '#E70808'
WHITE = '#FFFFFF'

# ---------------------------------------------------------------- artboard / panels (mm, repère page)
AB = (91, 239, 802, 397)
P = {
    'P1':  (124.53, 423.31, 227.90, 92.96),
    'P2':  (352.43, 423.31, 148.94, 92.96),
    'P3':  (501.37, 423.31, 227.89, 92.96),
    'P4':  (729.26, 423.31, 148.94, 92.96),
    'LID': (124.53, 274.38, 227.90, 148.93),
    'INNER': (501.37, 281.56, 227.89, 141.75),
}
diel = json.load(open(os.path.join(ROOT, 'dieline.json')))

# ---------------------------------------------------------------- helpers
def css(**kw):
    return ';'.join(f"{k.replace('_','-')}:{v}" for k, v in kw.items())

def box(panel, x, y, inner, w=None, h=None, style=''):
    px, py = P[panel][0], P[panel][1]
    s = f'left:{px+x:.3f}mm;top:{py+y:.3f}mm;'
    if w is not None: s += f'width:{w:.3f}mm;'
    if h is not None: s += f'height:{h:.3f}mm;'
    return f'<div class="abs" style="{s}{style}">{inner}</div>'

def local(x, y, inner, w=None, h=None, style=''):
    s = f'left:{x:.3f}mm;top:{y:.3f}mm;'
    if w is not None: s += f'width:{w:.3f}mm;'
    if h is not None: s += f'height:{h:.3f}mm;'
    return f'<div class="abs" style="{s}{style}">{inner}</div>'

def t(text, size, weight=400, color=WHITE, ls=0, lh=1.25, extra=''):
    return f'<div style="font-size:{size}mm;font-weight:{weight};color:{color};letter-spacing:{ls}em;line-height:{lh};{extra}">{text}</div>'

_icon_cache = {}
def lucide(name):
    if name not in _icon_cache:
        p = os.path.join(ROOT, '..', 'assets', 'icons', name + '.svg')
        s = open(p).read()
        s = re.sub(r'<!--.*?-->', '', s, flags=re.S)
        inner = re.search(r'<svg[^>]*>(.*)</svg>', s, flags=re.S).group(1)
        _icon_cache[name] = inner.strip()
    return _icon_cache[name]

def icon(name, size, color=WHITE, stroke_mm=0.32, extra_style=''):
    sw = stroke_mm / size * 24
    if name == 'human-scan':
        inner = (lucide('scan') + f'<g transform="translate(6.6 6.2) scale(0.45)" stroke-width="{sw/0.45:.3f}">' + lucide('person-standing') + '</g>')
    elif name == 'switch':
        inner = ('<rect x="2.5" y="7.5" width="19" height="9" rx="1.6"/>'
                 '<path d="M5.8 13.6v-2.4h2.4v2.4M10.8 13.6v-2.4h2.4v2.4M15.8 13.6v-2.4h2.4v2.4"/>')
    elif name == 'microsd':
        inner = ('<path d="M8 2.5h7.2l3.3 3.3v4.4l-1.1 1.3v10H8z"/><path d="M10.6 5.6v2.6M13.1 5.6v2.6M15.6 6.8v1.4"/>')
    else:
        inner = lucide(name)
    return (f'<svg viewBox="0 0 24 24" style="width:{size}mm;height:{size}mm;display:block;{extra_style}" fill="none" '
            f'stroke="{color}" stroke-width="{sw:.3f}" stroke-linecap="round" stroke-linejoin="round">{inner}</svg>')

LOGO_D = re.search(r' d="([^"]+)"', open(os.path.join(A, 'logo.svg')).read()).group(1)
LOGO_RATIO = 3228 / 526
def logo(width, color=RED):
    h = width / LOGO_RATIO
    return (f'<svg viewBox="20 20 3228 526" style="width:{width}mm;height:{h:.3f}mm;display:block">'
            f'<path d="{LOGO_D}" fill="{color}" fill-rule="evenodd"/></svg>')

def trace_svg(name, height, color):
    s = open(os.path.join(A, name + '.svg')).read()
    W, H = [float(v) for v in re.search(r'viewBox="0 0 (\S+) (\S+)"', s).groups()]
    d = re.search(r' d="([^"]+)"', s).group(1)
    w = height * (W - 40) / (H - 40)
    return (f'<svg viewBox="20 20 {W-40} {H-40}" style="width:{w:.3f}mm;height:{height}mm;display:block">'
            f'<path d="{d}" fill="{color}" fill-rule="evenodd"/></svg>'), w

def img(src, w=None, h=None, style=''):
    s = ''
    if w: s += f'width:{w}mm;'
    if h: s += f'height:{h}mm;'
    return f'<img src="../assets/{src}" style="display:block;{s}{style}">'

def qr(size):
    lines = open(os.path.join(A, 'qr_path.txt')).read().split('\n', 1)
    n = int(lines[0]); d = lines[1]
    pad = 1.6
    inner = size - 2 * pad
    ic = inner * 9 / n; icpad = inner * 11 / n
    return (f'<div style="position:relative;width:{size}mm;height:{size}mm;background:#fff;border-radius:1.6mm">'
            f'<svg viewBox="0 0 {n} {n}" shape-rendering="crispEdges" style="position:absolute;left:{pad}mm;top:{pad}mm;width:{inner}mm;height:{inner}mm">'
            f'<path d="{d}" fill="#000"/><rect x="13" y="13" width="11" height="11" fill="#fff"/></svg>'
            f'<img src="../assets/app_icon.png" style="position:absolute;left:{pad + inner*14/n:.3f}mm;top:{pad + inner*14/n:.3f}mm;width:{ic:.3f}mm;height:{ic:.3f}mm"></div>')

def ean_svg(code, mag=0.85):
    mods = ean_modules(code)
    mw = 0.33 * mag
    bar_h = 22.85 * mag
    guard_ext = 1.65 * mag
    qz_l, qz_r = 11, 7
    total_w = (qz_l + 95 + qz_r) * mw
    digit_h = 2.75 * mag
    H = 25.93 * mag
    guards = set(list(range(0, 3)) + list(range(45, 50)) + list(range(92, 95)))
    rects = []
    i = 0
    while i < 95:
        if mods[i] == '1':
            j = i
            while j < 95 and mods[j] == '1' and ((j in guards) == (i in guards)): j += 1
            x = (qz_l + i) * mw
            h = bar_h + (guard_ext if i in guards else 0)
            rects.append(f'<rect x="{x:.4f}" y="0" width="{(j-i)*mw:.4f}" height="{h:.4f}"/>')
            i = j
        else:
            i += 1
    txt = []
    fs = digit_h * 1.18
    ty = bar_h + 2.95 * mag
    txt.append(f'<text x="{(qz_l-1.2)*mw - 0.1:.3f}" y="{ty:.3f}" text-anchor="end">{code[0]}</text>')
    for k in range(6):
        cx = (qz_l + 3 + 7*k + 3.5) * mw
        txt.append(f'<text x="{cx:.3f}" y="{ty:.3f}" text-anchor="middle">{code[1+k]}</text>')
    for k in range(6):
        cx = (qz_l + 50 + 7*k + 3.5) * mw
        txt.append(f'<text x="{cx:.3f}" y="{ty:.3f}" text-anchor="middle">{code[7+k]}</text>')
    txt.append(f'<text x="{(qz_l+95+1.2)*mw:.3f}" y="{ty:.3f}" text-anchor="start">&gt;</text>')
    svg = (f'<svg viewBox="0 -0.2 {total_w:.3f} {H+0.2:.3f}" style="width:{total_w:.3f}mm;height:{H+0.2:.3f}mm;display:block">'
           f'<g fill="#000">{"".join(rects)}</g>'
           f'<g font-family="JetBrains Mono, DejaVu Sans Mono, monospace" font-size="{fs:.3f}" fill="#000">{"".join(txt)}</g></svg>')
    return svg, total_w, H

# ================================================================ BACKGROUND (SVG)
bg = []
bg.append('<defs>'
          '<radialGradient id="spot" cx="0.5" cy="0.5" r="0.5">'
          '<stop offset="0" stop-color="#30333A" stop-opacity="1"/>'
          '<stop offset="0.45" stop-color="#1B1C20" stop-opacity="0.85"/>'
          '<stop offset="1" stop-color="#0B0B0D" stop-opacity="0"/></radialGradient>'
          '<radialGradient id="soft" cx="0.5" cy="0.5" r="0.5">'
          '<stop offset="0" stop-color="#24262B" stop-opacity="1"/>'
          '<stop offset="1" stop-color="#0B0B0D" stop-opacity="0"/></radialGradient>'
          '<radialGradient id="floor" cx="0.5" cy="0.5" r="0.5">'
          '<stop offset="0" stop-color="#FFFFFF" stop-opacity="0.10"/>'
          '<stop offset="1" stop-color="#FFFFFF" stop-opacity="0"/></radialGradient>'
          '<linearGradient id="metal" x1="0" y1="0" x2="1" y2="0">'
          '<stop offset="0" stop-color="#7E8187"/><stop offset="0.28" stop-color="#E9EAEC"/>'
          '<stop offset="0.5" stop-color="#A4A7AC"/><stop offset="0.72" stop-color="#F3F4F5"/>'
          '<stop offset="1" stop-color="#83868C"/></linearGradient>'
          '<linearGradient id="redfade" x1="0" y1="0" x2="1" y2="0">'
          f'<stop offset="0" stop-color="{RED}"/><stop offset="1" stop-color="{RED}" stop-opacity="0"/></linearGradient>'
          '</defs>')
# fonds noirs + fond perdu 3 mm (contour épais de même couleur)
for it in diel:
    if it['kind'] != 'cut':
        continue
    x0, y0, x1, y1 = it['bbox']
    if x1 <= 128.1:            # patte de collage : laissée sans encre
        continue
    if abs((x1 - x0) - 40.99) < 0.1:   # encoche du couvercle
        continue
    bg.append(f'<path d="{it["d"]}" fill="{BLACK}" stroke="{BLACK}" stroke-width="6" stroke-linejoin="miter"/>')

# halos / lumières (découpés à la face concernée ; +3 mm uniquement sur les bords coupés)
def clip(cid, k, l=0, t_=0, r=0, b=0):
    x, y, w, h = P[k]
    return f'<clipPath id="{cid}"><rect x="{x-l}" y="{y-t_}" width="{w+l+r}" height="{h+t_+b}"/></clipPath>'
bg.append('<defs>' + clip('cLID', 'LID', 3, 3, 3, 0) + clip('cP1', 'P1') + clip('cP2', 'P2') + clip('cINNER', 'INNER', 3, 3, 3, 0) + '</defs>')
BLEED = {'LID': (3, 3, 3, 0), 'P1': (0, 0, 0, 0), 'P2': (0, 0, 0, 0), 'INNER': (3, 3, 3, 0)}
for k, (bl, bt, br, bb) in BLEED.items():
    x, y, w, h = P[k]
    bg.append(f'<image href="../assets/bg_{k}.jpg" x="{x-bl}" y="{y-bt}" width="{w+bl+br}" height="{h+bt+bb}" preserveAspectRatio="none"/>')

# patte de collage : zone non imprimée (2 mm d'encre au-delà du pli)
bg.append(f'<rect x="95" y="410" width="{122.53-95}" height="120" fill="#FFFFFF"/>')

# ================================================================ CONTENT (HTML)
H = []

# ---------------------------------------------------------------- COUVERCLE (face principale 228 x 149)
H.append(box('LID', 11, 11.5, logo(46, RED)))
H.append(box('LID', 11, 32.5, t('CAMÉRA DE SURVEILLANCE EXTÉRIEURE', 2.15, 500, GRAY2, 0.22)))
H.append(box('LID', 10.2, 35.2, t('EF503', 21, 600, WHITE, -0.015, 1)))
H.append(box('LID', 11, 57.6, t('Caméra PoE Full HD à structure métallique', 4.05, 300, '#E4E5E8', 0)))
H.append(box('LID', 11, 66.2, '', 16, 0.6, f'background:{RED}'))

tiles = [
    ('PoE', 'Alimentation PoE', 'Énergie + vidéo, 1 seul câble'),
    ('1080p', 'Résolution Full HD', '1920 × 1080 · 2 MP'),
    ('Métal', 'Structure métallique', 'Robuste, faite pour durer'),
]
for k, (v, l1, l2) in enumerate(tiles):
    x = 11 + k * 36
    H.append(box('LID', x, 74, '', 32, 0.25, f'background:{LINE}'))
    H.append(box('LID', x, 73.85, '', 5, 0.55, f'background:{RED}'))
    H.append(box('LID', x - 0.4, 77.2, t(v, 9.4, 600, WHITE, -0.02, 1)))
    H.append(box('LID', x, 89.6, t(l1, 2.35, 500, WHITE, 0.01)))
    H.append(box('LID', x, 93.0, t(l2, 2.15, 300, GRAY2, 0)))

H.append(box('LID', 11, 103.2,
             f'<div style="display:inline-block;background:{RED};border-radius:3mm;padding:1.05mm 3mm 0.95mm">'
             + t('SANS ABONNEMENT', 2.45, 600, WHITE, 0.14, 1.2) + '</div>'))
H.append(box('LID', 50.5, 103.9, t('Enregistrement local sur carte microSD<br>Application mobile gratuite', 2.15, 300, GRAY1, 0, 1.3), 62))

H.append(box('LID', 11, 118.2, '', 104, 0.2, f'background:{LINE}'))
feats = [('moon-star', 'Vision nocturne', 'jusqu’à 30&nbsp;m'),
         ('human-scan', 'Détection', 'humaine'),
         ('audio-lines', 'Audio', 'bidirectionnel'),
         ('smartphone', 'Accès', 'à distance')]
for k, (ic, a, b) in enumerate(feats):
    x = 11 + k * 26.5
    H.append(box('LID', x, 122.4, icon(ic, 5.6, WHITE, 0.3)))
    H.append(box('LID', x + 7.4, 122.3, t(a, 2.1, 500, WHITE, 0, 1.25) + t(b, 2.1, 300, GRAY2, 0, 1.25)))

# produit : visuel 3 (sans marquage fabricant), boîte utile du détourage = (101,95)-(1558,1914) px
sc = 125.5 / 1819
pw, ph = 1618 * sc, 2000 * sc
pxl = 221.5 - (1558 - 101) * sc - 101 * sc
pyt = 12.5 - 95 * sc
H.append(box('LID', pxl, pyt, img('product.png', w=f'{pw:.3f}', h=f'{ph:.3f}')))

# ---------------------------------------------------------------- FACE AVANT P1 (228 x 93) : histoire PoE
H.append(box('P1', 11, 12, logo(36, RED)))
H.append(box('P1', 10.4, 22.5, t('EF503', 11.5, 600, WHITE, -0.015, 1)))
H.append(box('P1', 11, 36.2, t('Caméra extérieure PoE', 3.0, 500, WHITE, 0)))
H.append(box('P1', 11, 40.6, t('Full HD 1080p · Structure métallique', 2.45, 300, GRAY2, 0)))
H.append(box('P1', 11, 70.8,
             f'<div style="display:inline-block;border:0.25mm solid {RED};border-radius:2.6mm;padding:0.85mm 2.6mm 0.75mm">'
             + t('SANS ABONNEMENT', 2.1, 600, WHITE, 0.14, 1.2) + '</div>'))
H.append(box('P1', 78, 12, '', 0.2, 69, f'background:{LINE}'))

H.append(box('P1', 90, 11.6, t('POWER OVER ETHERNET', 2.1, 600, RED, 0.24)))
H.append(box('P1', 89.6, 15.4, t('Un seul câble.', 7.2, 600, WHITE, -0.01, 1.08) + t('Image et alimentation.', 7.2, 300, GRAY2, -0.01, 1.08)))
H.append(box('P1', 90, 33.8, t('Le câble réseau RJ45 transporte à la fois l’électricité et la vidéo : '
                                 'pas besoin de prise électrique près de la caméra, une connexion filaire '
                                 'stable et une installation nette.', 2.4, 300, GRAY1, 0, 1.45), 118))

# schéma PoE
def node(cx, cy, ic, label):
    r = 7.2
    s = local(cx - r, cy - r, f'<div style="width:{2*r}mm;height:{2*r}mm;border-radius:50%;border:0.25mm solid #44474D;background:{INK2};box-sizing:border-box;display:flex;align-items:center;justify-content:center">{icon(ic, 7, WHITE, 0.3)}</div>')
    s += local(cx - 20, cy + r + 1.6, t(label, 2.05, 500, GRAY1, 0.02, 1.2, 'text-align:center'), 40)
    return s
p1 = ''
y0 = 61
p1 += node(98, y0, 'switch', 'Switch / injecteur PoE')
p1 += node(208, y0, 'cctv', 'Caméra EF503')
p1 += local(105.6, y0 - 0.35, '', 95.2, 0.7, f'background:{RED}')
# capsules sur le câble
def chip(cx, ic, label):
    w = 23
    return local(cx - w/2, y0 - 2.9, f'<div style="width:{w}mm;height:5.8mm;border-radius:2.9mm;background:{BLACK};border:0.25mm solid {RED};box-sizing:border-box;display:flex;align-items:center;justify-content:center;gap:1.2mm">{icon(ic, 3.2, WHITE, 0.28)}' + t(label, 2.05, 600, WHITE, 0.06, 1) + '</div>')
p1 += chip(139, 'zap', 'ÉNERGIE')
p1 += chip(173, 'video', 'VIDÉO')
p1 += local(146, y0 + 4.6, t('1 câble RJ45', 2.0, 400, GRAY2, 0.04, 1.2, 'text-align:center'), 20)
H.append(box('P1', 0, 0, p1))

# ---------------------------------------------------------------- CÔTÉ P2 (149 x 93) : application + promesses
H.append(box('P2', 10, 14.4, t('APPLICATION MOBILE', 2.1, 600, RED, 0.24)))
H.append(box('P2', 9.6, 18.1, t('Daewoo Home Connect', 5.6, 600, WHITE, -0.01, 1.1)))
H.append(box('P2', 10, 26.4, t('Contrôlez votre caméra à distance et sans contrainte grâce à notre application dédiée.', 2.35, 300, GRAY1, 0, 1.42), 84))
H.append(box('P2', 10, 34.4, t('Control your device remotely and without constraint thanks to our dedicated app.', 2.0, 300, GRAY3, 0, 1.4, 'font-style:italic'), 84))
H.append(box('P2', 10, 43.6, f'<div style="display:flex;gap:2.4mm">{img("badge_gplay.png", h=7.6)}<div style="border:0.2mm solid #A6A6A6;border-radius:1.25mm;overflow:hidden;line-height:0">{img("badge_appstore.png", h=7.2)}</div></div>'))
H.append(box('P2', 10, 52.8, t('Disponible gratuitement sur Google Play et l’App Store', 2.0, 400, GRAY2, 0), 90))
H.append(box('P2', 111.4, 14.0, qr(27)))
H.append(box('P2', 108.4, 42.4, t('Scannez pour télécharger<br>l’application', 1.95, 400, GRAY2, 0, 1.3, 'text-align:center'), 33))

H.append(box('P2', 10, 62.6, '', 128.9, 0.2, f'background:{LINE}'))
proms = [('cloud-off', 'Sans abonnement', 'Aucun frais mensuel requis'),
         ('microsd', 'Stockage local', 'microSD jusqu’à 256&nbsp;Go'),
         ('shield-check', 'Garantie 2 ans', 'Support en France')]
for k, (ic, a, b) in enumerate(proms):
    x = 10 + k * 44
    H.append(box('P2', x, 68.2, icon(ic, 6, WHITE, 0.3)))
    H.append(box('P2', x + 8, 68.1, t(a, 2.3, 600, WHITE, 0, 1.2) + t(b, 2.0, 300, GRAY2, 0, 1.3), 35))

# ---------------------------------------------------------------- DOS P3 (228 x 93) : multilingue + mentions légales
# zone languette de suspension réservée : x 93.95–133.94, y 0–20
H.append(box('P3', 7, 7.2, t('Caméra extérieure EF503', 3.2, 600, RED, 0)))
H.append(box('P3', 7, 11.6, t('DAEWOO – Caméra PoE Full HD<br>à structure métallique', 2.05, 300, WHITE, 0, 1.3), 52))
H.append(box('P3', 7, 18.8, icon('shield-check', 5.2, WHITE, 0.3)))
H.append(box('P3', 13.6, 19.0, t('Garantie limitée à deux ans', 2.0, 500, WHITE, 0, 1.25) + t('Two year limited warranty', 2.0, 300, GRAY2, 0, 1.25)))
legal_a = ('<b style="font-weight:600;color:#fff">IMPORTER IN EUROPE :</b><br>Liz Invest SAS<br>15 Allée James Watt<br>Immeuble 2000 Watt<br>'
           '33700 Mérignac<br>France<br>contact@daewoo-security.fr')
H.append(box('P3', 7, 27.4, t(legal_a, 1.8, 400, GRAY1, 0, 1.36), 50))
sysreq = ('<b style="font-weight:600;color:#fff">SYSTEM REQUIREMENTS :</b><br>iOS 9.0 or higher<br>Android 5.0 or higher<br>'
          'Compatible with most iOS™ &amp; Android™ Devices')
H.append(box('P3', 7, 46.6, t(sysreq, 1.8, 400, GRAY1, 0, 1.36), 50))
H.append(box('P3', 7, 60.4, t('© 2026 Liz Invest SAS – France<br>Made in China', 1.8, 400, GRAY1, 0, 1.36), 50))
# logos réglementaires
cx = 7
row = ''
for name, hgt in [('ce', 6.2), ('pointvert', 7.2), ('weee', 7.6), ('rohs', 5.6)]:
    s, w = trace_svg(name, hgt, WHITE)
    H.append(box('P3', cx, 82.6 - hgt, s))
    cx += w + 3.4

langs = [
 ('FR / CARACTÉRISTIQUES TECHNIQUES', ['Caméra extérieure EF503', 'Alimentation PoE (Power over Ethernet)', 'Structure métallique',
   'Résolution Full HD 1080p', 'Objectif 4 mm F2.0 · angle 82°', 'Vision nocturne infrarouge jusqu’à 30&nbsp;m',
   'Détection humaine et alertes en temps réel', 'Audio bidirectionnel', 'Wi-Fi 2,4 GHz et port RJ45',
   'Carte microSD jusqu’à 256&nbsp;Go', 'Application Daewoo Home Connect']),
 ('EN / TECHNICAL CHARACTERISTICS', ['EF503 outdoor camera', 'PoE power supply (Power over Ethernet)', 'Metal housing',
   'Full HD 1080p resolution', '4 mm F2.0 lens · 82° field of view', 'Infrared night vision up to 30 m',
   'Human detection with real-time alerts', 'Two-way audio', '2.4 GHz Wi-Fi and RJ45 port',
   'microSD card up to 256 GB', 'Daewoo Home Connect app']),
 ('ES / CARACTERÍSTICAS TÉCNICAS', ['Cámara exterior EF503', 'Alimentación PoE (Power over Ethernet)', 'Estructura metálica',
   'Resolución Full HD 1080p', 'Lente 4 mm F2.0 · ángulo de 82°', 'Visión nocturna infrarroja hasta 30 m',
   'Detección humana con alertas en tiempo real', 'Audio bidireccional', 'Wi-Fi 2,4 GHz y puerto RJ45',
   'Tarjeta microSD de hasta 256 GB', 'Aplicación Daewoo Home Connect']),
 ('DE / TECHNISCHE EIGENSCHAFTEN', ['EF503 Außenkamera', 'PoE-Stromversorgung (Power over Ethernet)', 'Metallgehäuse',
   'Full-HD-Auflösung 1080p', '4-mm-Objektiv F2.0 · 82° Blickwinkel', 'Infrarot-Nachtsicht bis 30 m',
   'Personenerkennung mit Echtzeit-Alarm', 'Zwei-Wege-Audio', '2,4-GHz-WLAN und RJ45-Anschluss',
   'microSD-Karte bis 256 GB', 'App Daewoo Home Connect']),
]
for k, (title, items) in enumerate(langs):
    col, rowi = k % 2, k // 2
    x = 61 + col * 44
    y = 22.4 + rowi * 31.4
    body = t(title, 1.8, 600, WHITE, 0.03, 1.3, 'margin-bottom:0.7mm') + \
        ''.join(t(it, 1.72, 300, GRAY1, 0, 1.28) for it in items)
    H.append(box('P3', x, y, body, 41.5))

legal_c = ('Apple and the Apple logo are trademarks of Apple Inc., registered in the U.S. and other countries. '
           'App Store is a service mark of Apple Inc., registered in the U.S. and other countries.<br>'
           'iOS is a trademark or registered trademark of Cisco in the U.S. and other countries and is used under license.<br>'
           'ANDROID is a trademark of Google Inc. All other logos, products or company names that are referred to on this '
           'packaging are trade names, trademarks or registered trademarks of their respective holders. The holders are '
           'not affiliated with Liz Invest, our products or our website.<br>'
           'DAEWOO is a trademark of POSCO International Corporation, 165, Convensia-daero, Yeonsu-gu, Incheon, 408-840, '
           'Korea and used under license by Focus Industries O/B Fortune Technology, Hong Kong.')
H.append(box('P3', 152, 7.2, t(legal_c, 1.62, 400, GRAY1, 0, 1.36, 'text-align:left;hyphens:manual'), 69))

esvg, ew, eh = ean_svg('3760285866513', 0.85)
ean_top = 82.6 - (eh + 0.2 + 2.3)
H.append(box('P3', 152, ean_top, f'<div style="background:#fff;border-radius:0.8mm;padding:1.4mm 0.9mm 0.9mm;width:{ew:.3f}mm">{esvg}</div>'))
H.append(box('P3', 152, ean_top - 9.4, t('PLUS D’INFORMATIONS', 1.6, 500, GRAY3, 0.14, 1.2) + t('daewoo-security.fr', 2.7, 600, WHITE, 0, 1.3)))
H.append(box('P3', 152 + ew + 1.8 + 2.6, ean_top, '', 221 - (152 + ew + 4.4), eh + 0.2 + 2.3,
             'background:#fff;border-radius:0.8mm'))

# ---------------------------------------------------------------- CÔTÉ P4 (149 x 93) : fiche technique
H.append(box('P4', 10, 13.0, t('FICHE TECHNIQUE · SPECIFICATIONS', 2.05, 600, RED, 0.2)))
H.append(box('P4', 116.6, 11.6, logo(22.3, WHITE)))
H.append(box('P4', 10, 18.8, '', 128.9, 0.25, f'background:{LINE}'))
specs = [
 ('Capteur · Sensor', 'CMOS 1/3,27" · 2 MP'),
 ('Résolution · Resolution', '1080p Full HD (1920 × 1080)'),
 ('Objectif · Lens', '4 mm · ouverture F2.0'),
 ('Angle de vue · Field of view', '82° (diagonale)'),
 ('Vision nocturne · Night vision', 'Infrarouge, jusqu’à 30&nbsp;m'),
 ('Compression', 'H.264 · MJPEG'),
 ('Audio', 'Micro et haut-parleur intégrés'),
 ('Détection · Detection', 'Mouvement, humaine, zones'),
 ('Alimentation · Power', 'PoE ou DC 12 V'),
 ('Réseau · Network', 'RJ45 10/100 Mbps · Wi-Fi 2,4 GHz'),
 ('Protocoles · Protocols', 'TCP/IP, RTSP, P2P, DHCP, NTP'),
 ('Stockage · Storage', 'microSD jusqu’à 256&nbsp;Go'),
 ('Boîtier · Housing', 'Structure métallique'),
 ('Température · Temperature', '−10 °C à +55 °C'),
 ('Dimensions', '183 × 71 × 73 mm'),
 ('Poids · Weight', '300 g'),
]
for k, (lab, val) in enumerate(specs):
    col, r = k // 8, k % 8
    x = 10 + col * 66.4
    y = 21.0 + r * 8.05
    H.append(box('P4', x, y, t(lab.upper(), 1.6, 500, GRAY3, 0.08, 1.2) + t(val, 2.35, 400, WHITE, 0, 1.3), 62.5))
    if r < 7:
        H.append(box('P4', x, y + 7.15, '', 62.5, 0.15, 'background:#202226'))

# ---------------------------------------------------------------- RABAT INTÉRIEUR (lu après ouverture, pivoté 180°)
inner = ''
W_, H_ = P['INNER'][2], P['INNER'][3]
inner += local((W_ - 40) / 2, 30, logo(40, WHITE))
inner += local(0, 42.5, t('Merci d’avoir choisi Daewoo Security.', 5.0, 500, WHITE, -0.005, 1.2, 'text-align:center'), W_)
inner += local(0, 50.4, t('Votre sécurité, sans abonnement.', 3.3, 300, GRAY2, 0, 1.2, 'text-align:center'), W_)
inner += local((W_ - 16) / 2, 57.6, '', 16, 0.6, f'background:{RED}')
steps = [('01', 'Téléchargez', 'l’application Daewoo Home Connect sur Google Play ou l’App Store.'),
         ('02', 'Raccordez', 'la caméra en PoE, ou sur une alimentation 12&nbsp;V.'),
         ('03', 'Ajoutez', 'la caméra dans l’application et laissez-vous guider.')]
for k, (n, a, b) in enumerate(steps):
    x = 26 + k * 61
    inner += local(x, 70, t(n, 7, 600, RED, -0.02, 1) + t(a, 3.0, 600, WHITE, 0, 1.3, 'margin-top:1.6mm') +
                   t(b, 2.3, 300, GRAY1, 0, 1.4, 'margin-top:0.6mm'), 52)
inner += local(0, 112, t('Besoin d’aide&nbsp;? contact@daewoo-security.fr · daewoo-security.fr', 2.3, 400, GRAY2, 0.02, 1.2, 'text-align:center'), W_)
H.append(f'<div class="abs" style="left:{P["INNER"][0]}mm;top:{P["INNER"][1]}mm;width:{W_}mm;height:{H_}mm;transform:rotate(180deg)">{inner}</div>')

# ================================================================ DIELINE / PROOF OVERLAY
ov = []
if MODE == 'proof':
    for it in diel:
        col = {'cut': '#EC008C', 'special': '#00AEEF', 'mark': '#EC008C'}[it['kind']]
        dash = ' stroke-dasharray="1.2 0.8"' if it['kind'] == 'special' else ''
        ov.append(f'<path d="{it["d"]}" fill="none" stroke="{col}" stroke-width="0.18"{dash}/>')
    labels = [('LID', 'COUVERCLE · FACE PRINCIPALE (lecture depuis la face avant)'),
              ('P1', 'FACE AVANT'), ('P2', 'CÔTÉ DROIT'), ('P3', 'DOS'), ('P4', 'CÔTÉ GAUCHE'),
              ('INNER', 'RABAT INTÉRIEUR (imprimé tête-bêche, lu à l’ouverture)')]
    for k, lab in labels:
        x, y, w, h = P[k]
        yy = 630 if k in ('P1','P2','P3','P4') else (249 if k=='LID' else y - 4.2)
        ov.append(f'<text x="{x + w/2}" y="{yy}" text-anchor="middle" font-family="Poppins" font-weight="600" font-size="3.2" fill="#EC008C" letter-spacing="0.3">{lab}</text>')
    tb = ['DAEWOO EF503 — Boîte 228 × 149 × 93 mm (gabarit fabricant TS58)',
          'Carton 300 g blanc + W9 renforcé, pelliculage mat · Impression quadri',
          'Magenta : découpe / plis · Cyan pointillé : languette de suspension · Fond perdu 3 mm',
          'Patte de collage laissée sans encre · EAN 3760285866513 (85 %)',
          'BAT v1 — 27/11/2026']
    for i, line in enumerate(tb):
        ov.append(f'<text x="742" y="{262 + i*5.2}" font-family="Poppins" font-weight="{600 if i==0 else 400}" font-size="{3.4 if i==0 else 2.7}" fill="#1A1A1A">{line}</text>')
    ov.append(f'<rect x="738" y="252" width="150" height="{10 + len(tb)*5.2}" fill="none" stroke="#1A1A1A" stroke-width="0.2"/>')

# ================================================================ PAGE
font_faces = ''.join(
    f"@font-face{{font-family:'Poppins';font-weight:{w};font-style:normal;src:url('../assets/poppins-latin-{w}-normal.woff2') format('woff2');}}"
    for w in (300, 400, 500, 600, 700))
html = f'''<!doctype html><html lang="fr"><head><meta charset="utf-8"><title>DAEWOO EF503 — boîte</title>
<style>
{font_faces}
@page {{ size: {AB[2]}mm {AB[3]}mm; margin: 0 }}
html,body {{ margin:0; padding:0; background:#fff }}
body {{ font-family:'Poppins',sans-serif; -webkit-print-color-adjust:exact; print-color-adjust:exact; text-rendering:geometricPrecision; font-kerning:normal }}
#sheet {{ position:relative; width:{AB[2]}mm; height:{AB[3]}mm; overflow:hidden; background:#fff }}
.abs {{ position:absolute }}
#content {{ position:absolute; left:-{AB[0]}mm; top:-{AB[1]}mm; width:1300mm; height:900mm }}
svg.layer {{ position:absolute; left:0; top:0 }}
</style></head><body>
<div id="sheet">
<svg class="layer" viewBox="{AB[0]} {AB[1]} {AB[2]} {AB[3]}" style="width:{AB[2]}mm;height:{AB[3]}mm">{''.join(bg)}</svg>
<div id="content">{''.join(H)}</div>
<svg class="layer" viewBox="{AB[0]} {AB[1]} {AB[2]} {AB[3]}" style="width:{AB[2]}mm;height:{AB[3]}mm">{''.join(ov)}</svg>
</div></body></html>'''
open(OUT, 'w').write(html)
print('written', OUT, len(html))
