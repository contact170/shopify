#!/usr/bin/env python3
"""Analyse le gabarit (dieline) PDF d'un fabricant et propose gabarit.json.

Usage : python3 gabarit.py <gabarit_fabricant.pdf> <dossier_produit>

Écrit dans le dossier produit :
  - gabarit.json        : traits de découpe en mm + proposition de faces (à vérifier)
  - gabarit_apercu.png  : aperçu annoté (faces, zones réservées, patte de collage)

La proposition vise les étuis à rabats classiques (bande de 4 côtés + couvercle).
Toujours contrôler l'aperçu : en cas de doute, corriger gabarit.json à la main.
"""
import json, os, re, subprocess, sys, tempfile, math
from collections import defaultdict

PT2MM = 25.4 / 72


def parse_svg_paths(svg):
    """Retourne les chemins tracés (stroke) : couleur, épaisseur, points en mm."""
    out = []
    for m in re.finditer(r'<path[^>]*stroke="([^"]+)"[^>]*/>', svg):
        t = m.group(0)
        col = m.group(1)
        if col == 'none':
            continue
        d = re.search(r' d="([^"]+)"', t).group(1)
        mt = re.search(r'matrix\(([^)]+)\)', t)
        a, b, c, dd, e, f = [float(x) for x in mt.group(1).replace(',', ' ').split()] if mt else (1, 0, 0, 1, 0, 0)
        w = re.search(r'stroke-width="([^"]+)"', t)
        toks = re.findall(r'[MLCZ]|-?\d*\.?\d+(?:e-?\d+)?', d)
        outp, pts, i, closed = [], [], 0, False
        while i < len(toks):
            tk = toks[i]
            if tk in 'MLCZ':
                outp.append(tk)
                closed |= tk == 'Z'
                i += 1
                continue
            x, y = float(toks[i]), float(toks[i + 1])
            i += 2
            X, Y = (a * x + c * y + e) * PT2MM, (b * x + dd * y + f) * PT2MM
            pts.append((X, Y))
            outp.append(f'{X:.3f},{Y:.3f}')
        if not pts:
            continue
        xs, ys = [p[0] for p in pts], [p[1] for p in pts]
        out.append({'couleur': col, 'epaisseur': float(w.group(1)) if w else 1.0, 'd': ' '.join(outp),
                    'bbox': [min(xs), min(ys), max(xs), max(ys)], 'ferme': closed, 'nb_points': len(pts),
                    'cmds': ''.join(x for x in outp if x in 'MLCZ')})
    return out


def is_rect(p, tol=0.4):
    if p['cmds'].rstrip('M') not in ('MLLLZ', 'MLLLLZ'):
        return False
    nums = [tuple(map(float, s.split(','))) for s in p['d'].split() if ',' in s]
    xs = sorted({round(x / tol) for x, _ in nums})
    ys = sorted({round(y / tol) for _, y in nums})
    x0, y0, x1, y1 = p['bbox']
    return (x1 - x0) > 5 and (y1 - y0) > 5 and all(
        (abs(x - x0) < tol or abs(x - x1) < tol) and (abs(y - y0) < tol or abs(y - y1) < tol) for x, y in nums)


def classify(paths):
    groups = defaultdict(list)
    for p in paths:
        groups[p['couleur']].append(p)
    def score(g):
        return sum(1 for p in g if p['ferme']) * 10 + len(g)
    dominant = max(groups, key=lambda c: score(groups[c]))
    for col, g in groups.items():
        for p in g:
            x0, y0, x1, y1 = p['bbox']
            length = math.hypot(x1 - x0, y1 - y0)
            if col == dominant:
                p['type'] = 'coupe'
            elif all(q['cmds'] == 'ML' for q in g) and length > 8:
                p['type'] = 'cote'        # lignes de cotes : ignorées
            elif length <= 4:
                p['type'] = 'repere'
            else:
                p['type'] = 'special'
    return dominant, groups


def near(a, b, tol=0.6):
    return abs(a - b) <= tol


def propose(paths):
    cut = [p for p in paths if p['type'] == 'coupe']
    rects = [p for p in cut if is_rect(p)]
    R = [dict(bbox=p['bbox']) for p in rects]
    # bande : rectangles de même hauteur, contigus horizontalement
    best = []
    for r in R:
        x0, y0, x1, y1 = r['bbox']
        same = [q for q in R if near(q['bbox'][1], y0) and near(q['bbox'][3], y1)]
        same.sort(key=lambda q: q['bbox'][0])
        chain, cur = [], None
        for q in same:
            if cur is None or near(q['bbox'][0], cur['bbox'][2]):
                chain.append(q)
            else:
                if len(chain) > len(best):
                    best = chain
                chain = [q]
            cur = q
        if len(chain) > len(best):
            best = chain
    if len(best) < 4:
        return None, 'Bande de 4 côtés introuvable : faces à définir à la main.'
    strip = best[:4] if len(best) == 4 else best
    sy0, sy1 = strip[0]['bbox'][1], strip[0]['bbox'][3]
    H = sy1 - sy0
    widths = [q['bbox'][2] - q['bbox'][0] for q in strip]
    L, W = max(widths), min(widths)
    # fermetures attenantes (au-dessus ou en dessous de la bande)
    closures = []
    for q in R:
        x0, y0, x1, y1 = q['bbox']
        for i, s in enumerate(strip):
            if near(x0, s['bbox'][0]) and near(x1, s['bbox'][2]):
                if near(y1, sy0):
                    closures.append(dict(bbox=q['bbox'], panneau=i, cote='haut', h=y1 - y0))
                elif near(y0, sy1):
                    closures.append(dict(bbox=q['bbox'], panneau=i, cote='bas', h=y1 - y0))
    tops = [c for c in closures if c['cote'] == 'haut']
    lid = None
    for c in sorted(tops, key=lambda c: abs(c['h'] - W)):
        if abs(c['h'] - W) < 1.0 and abs((strip[c['panneau']]['bbox'][2] - strip[c['panneau']]['bbox'][0]) - L) < 1:
            lid = c
            break
    if lid is None:
        return None, 'Couvercle (L × l) introuvable au-dessus de la bande : faces à définir à la main.'
    n = len(strip)
    i_av = lid['panneau']
    order = [(i_av + k) % n for k in range(4)]
    faces_phys = {'avant': strip[order[0]]['bbox'], 'droite': strip[order[1]]['bbox'],
                  'arriere': strip[order[2]]['bbox'], 'gauche': strip[order[3]]['bbox'], 'dessus': lid['bbox']}
    inner = [c for c in tops if c is not lid and c['panneau'] == order[2] and c['h'] > 0.5 * W]
    # rôles : le héros est la plus grande face visible
    area = lambda b: (b[2] - b[0]) * (b[3] - b[1])
    if area(faces_phys['dessus']) >= area(faces_phys['avant']):
        roles = {'hero': 'dessus', 'argument': 'avant', 'application': 'droite', 'dos': 'arriere', 'fiche': 'gauche'}
    else:
        roles = {'hero': 'avant', 'argument': 'droite', 'application': 'dessus', 'dos': 'arriere', 'fiche': 'gauche'}
    faces = {}
    for role, phys in roles.items():
        x0, y0, x1, y1 = faces_phys[phys]
        faces[role] = {'rect': [round(x0, 3), round(y0, 3), round(x1 - x0, 3), round(y1 - y0, 3)], 'physique': phys,
                       'rotation': 0}
    if inner:
        x0, y0, x1, y1 = inner[0]['bbox']
        faces['rabat'] = {'rect': [round(x0, 3), round(y0, 3), round(x1 - x0, 3), round(y1 - y0, 3)],
                          'physique': 'rabat', 'rotation': 180}
    # patte de collage : forme fermée étroite accolée à une extrémité de la bande
    sx0, sx1 = strip[0]['bbox'][0], strip[-1]['bbox'][2]
    glue = None
    for p in cut:
        x0, y0, x1, y1 = p['bbox']
        if (x1 - x0) < 30 and y0 > sy0 - 2 and y1 < sy1 + 2 and (near(x1, sx0, 1.5) or near(x0, sx1, 1.5) or (x0 < sx0 < x1)):
            glue = p['bbox'] if glue is None else [min(glue[0], x0), min(glue[1], y0), max(glue[2], x1), max(glue[3], y1)]
    sans_encre = []
    if glue:
        if glue[2] <= sx0 + 4:   # à gauche de la bande
            sans_encre.append([round(glue[0] - 12, 2), round(sy0 - 12, 2), round(sx0 - 2 - (glue[0] - 12), 2), round(H + 24, 2)])
        else:
            sans_encre.append([round(sx1 + 2, 2), round(sy0 - 12, 2), round(glue[2] + 12 - (sx1 + 2), 2), round(H + 24, 2)])
    # zones réservées : traits spéciaux / repères / découpes internes qui touchent une face
    zones = []
    for role, f in faces.items():
        fx, fy, fw, fh = f['rect']
        for p in paths:
            if p['type'] not in ('special', 'repere', 'coupe'):
                continue
            x0, y0, x1, y1 = p['bbox']
            if p['type'] == 'coupe':
                inside = x0 > fx + 1 and x1 < fx + fw - 1 and y1 > fy + 1 and y0 < fy + fh - 1
                is_face_rect = near(x0, fx) and near(y0, fy) and near(x1, fx + fw) and near(y1, fy + fh)
                if not inside or is_face_rect or is_rect(p) and (x1 - x0) > 0.9 * fw:
                    continue
            ix0, iy0 = max(x0, fx), max(y0, fy)
            ix1, iy1 = min(x1, fx + fw), min(y1, fy + fh)
            if ix1 - ix0 > 0.5 and iy1 - iy0 > 0.5 or (p['type'] == 'repere' and fx <= x0 <= fx + fw and fy <= y0 <= fy + fh):
                zones.append({'face': role, 'type': p['type'], 'rect_page': [round(ix0 - 1.5, 2), round(iy0 - 1.5, 2),
                              round(ix1 - ix0 + 3, 2), round(iy1 - iy0 + 3, 2)]})
    # fusion des repères d'une même face en une seule zone (étiquette usine)
    merged, reps = [], defaultdict(list)
    for z in zones:
        (reps[z['face']] if z['type'] == 'repere' else merged).append(z)
    for face, zs in reps.items():
        xs = [z['rect_page'][0] for z in zs] + [z['rect_page'][0] + z['rect_page'][2] for z in zs]
        ys = [z['rect_page'][1] for z in zs]
        merged.append({'face': face, 'type': 'etiquette_usine', 'rect_page': [round(min(xs), 2), round(min(ys), 2),
                       round(max(xs) - min(xs), 2), 0], 'note': 'Repères d’étiquette usine (bas non défini)'})
    dims = [round(L, 1), round(W, 1), round(H, 1)]
    return {'dimensions_mm': dims, 'faces': faces, 'sans_encre': sans_encre, 'zones_page': merged}, None


def page_zones_to_local(prop):
    """Convertit les zones réservées (repère page) dans le repère de lecture de chaque face."""
    out = []
    for z in prop['zones_page']:
        f = prop['faces'][z['face']]
        fx, fy, fw, fh = f['rect']
        x, y, w, h = z['rect_page']
        lx, ly = x - fx, y - fy
        if f.get('rotation', 0) == 180:
            lx, ly = fw - (lx + w), fh - (ly + h)
        out.append({'face': z['face'], 'type': z['type'], 'x': round(lx, 2), 'y': round(ly, 2), 'w': round(w, 2),
                    'h': round(h, 2), **({'note': z['note']} if 'note' in z else {})})
    return out


def apercu(paths, prop, out_png, planche):
    px, py, pw, ph = planche
    col = {'coupe': '#EC008C', 'special': '#00AEEF', 'repere': '#EC008C', 'cote': '#BBBBBB'}
    s = [f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="{px} {py} {pw} {ph}" width="{pw*3:.0f}" height="{ph*3:.0f}">'
         f'<rect x="{px}" y="{py}" width="{pw}" height="{ph}" fill="#fff"/>']
    if prop:
        teintes = {'hero': '#FFE08A', 'argument': '#BDE3FF', 'application': '#C9F2C7', 'dos': '#FFD1D1',
                   'fiche': '#E3D4FF', 'rabat': '#EEEEEE'}
        for role, f in prop['faces'].items():
            x, y, w, h = f['rect']
            s.append(f'<rect x="{x}" y="{y}" width="{w}" height="{h}" fill="{teintes.get(role, "#eee")}"/>')
            s.append(f'<text x="{x+w/2}" y="{y+h/2}" font-size="{min(w, h)/9:.1f}" text-anchor="middle" font-family="sans-serif" '
                     f'font-weight="bold" fill="#333">{role} ({f["physique"]}{", 180°" if f["rotation"] else ""})</text>')
            s.append(f'<text x="{x+w/2}" y="{y+h/2 + min(w, h)/7:.1f}" font-size="{min(w, h)/13:.1f}" text-anchor="middle" '
                     f'font-family="sans-serif" fill="#333">{w:.1f} × {h:.1f} mm</text>')
        for r in prop['sans_encre']:
            s.append(f'<rect x="{r[0]}" y="{r[1]}" width="{r[2]}" height="{r[3]}" fill="none" stroke="#999" stroke-dasharray="2 1" stroke-width="0.4"/>')
        for z in prop['zones_page']:
            x, y, w, h = z['rect_page']
            s.append(f'<rect x="{x}" y="{y}" width="{w}" height="{max(h, 1)}" fill="#00AEEF" fill-opacity="0.25" stroke="#00AEEF" stroke-width="0.3"/>')
    for p in paths:
        if p['type'] == 'cote':
            continue
        s.append(f'<path d="{p["d"]}" fill="none" stroke="{col[p["type"]]}" stroke-width="0.35"/>')
    s.append('</svg>')
    tmp = out_png[:-4] + '.svg'
    open(tmp, 'w').write(''.join(s))
    js = ("const {chromium}=require('playwright');(async()=>{const b=await chromium.launch();const p=await b.newPage();"
          f"await p.goto('file://{os.path.abspath(tmp)}');const e=await p.$('svg');await e.screenshot({{path:'{os.path.abspath(out_png)}'}});await b.close();}})();")
    subprocess.run(['node', '-e', js], check=True)
    os.remove(tmp)


def main():
    if len(sys.argv) < 3:
        print(__doc__)
        sys.exit(1)
    pdf, dossier = sys.argv[1], sys.argv[2]
    os.makedirs(dossier, exist_ok=True)
    with tempfile.TemporaryDirectory() as td:
        svgp = os.path.join(td, 'g.svg')
        subprocess.run(['pdftocairo', '-svg', '-f', '1', '-l', '1', pdf, svgp], check=True)
        svg = open(svgp).read()
    paths, seen = [], set()
    for p in parse_svg_paths(svg):
        if p['d'] not in seen:
            seen.add(p['d'])
            paths.append(p)
    if not paths:
        sys.exit('Aucun trait trouvé : le gabarit est peut-être une image. Demander un PDF vectoriel (AI/PDF) au fabricant.')
    dominant, groups = classify(paths)
    print('Groupes de traits (couleur → nombre, type) :')
    for c, g in groups.items():
        print(f'  {c:42s} {len(g):4d}  {g[0]["type"]}')
    prop, err = propose(paths)
    traits = [{'type': p['type'], 'd': p['d'], 'bbox': [round(v, 3) for v in p['bbox']]} for p in paths if p['type'] != 'cote']
    xs = [t['bbox'][0] for t in traits] + [t['bbox'][2] for t in traits]
    ys = [t['bbox'][1] for t in traits] + [t['bbox'][3] for t in traits]
    planche = [round(min(xs) - 15, 2), round(min(ys) - 15, 2), round(max(xs) - min(xs) + 30, 2), round(max(ys) - min(ys) + 30, 2)]
    g = {'source': os.path.basename(pdf), 'planche': planche, 'traits': traits,
         'fabricant': {'reference': '', 'matiere_cn': '', 'matiere_en': '', 'impression_cn': '四色印刷',
                       'finition_en': 'matte lamination'}}
    if prop:
        g['dimensions_mm'] = prop['dimensions_mm']
        g['faces'] = prop['faces']
        g['sans_encre'] = prop['sans_encre']
        g['zones_reservees'] = page_zones_to_local(prop)
        print(f'\nBoîte détectée : {prop["dimensions_mm"][0]} × {prop["dimensions_mm"][1]} × {prop["dimensions_mm"][2]} mm')
        for role, f in prop['faces'].items():
            print(f'  {role:12s} → {f["physique"]:8s} {f["rect"][2]:.1f} × {f["rect"][3]:.1f} mm, rotation {f["rotation"]}°')
        for z in g['zones_reservees']:
            print(f'  zone réservée sur {z["face"]} ({z["type"]}) : x {z["x"]} y {z["y"]} {z["w"]} × {z["h"]} mm')
    else:
        print('\n' + err)
    out = os.path.join(dossier, 'gabarit.json')
    json.dump(g, open(out, 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
    apercu(paths, prop, os.path.join(dossier, 'gabarit_apercu.png'), planche)
    print(f'\nÉcrit : {out} et gabarit_apercu.png — compléter "fabricant" (matière en chinois/anglais, référence).')


if __name__ == '__main__':
    main()
