# Génère snippets/pk-plan.liquid : un plan d'installation par pack (SVG + légende).
# Usage : python3 -I gen_plans.py <sortie.liquid> <test.html>
import math, sys, html

OUT, TEST = sys.argv[1], sys.argv[2]
INK = "#1d1d1f"
TYPES = {  # lettre, couleur, libellé court pour la légende
    "C": ("C", "#0c1e4a"),
    "M": ("M", "#4b5770"),
    "V": ("V", "#1d1d1f"),
    "S": ("S", "#c81e2e"),
    "F": ("F", "#e8590c"),
}


def pt(cx, cy, r, a):
    t = math.radians(a)
    return cx + r * math.cos(t), cy + r * math.sin(t)


def wedge(cx, cy, r, a0, a1, cls):
    x0, y0 = pt(cx, cy, r, a0)
    x1, y1 = pt(cx, cy, r, a1)
    large = 1 if (a1 - a0) % 360 > 180 else 0
    return f'<path class="{cls}" d="M{cx:.0f} {cy:.0f} L{x0:.1f} {y0:.1f} A{r} {r} 0 {large} 1 {x1:.1f} {y1:.1f} Z"/>'


def arc(cx, cy, r, a0, a1):
    x0, y0 = pt(cx, cy, r, a0)
    x1, y1 = pt(cx, cy, r, a1)
    large = 1 if (a1 - a0) % 360 > 180 else 0
    return f'<path class="pk-p-arc" d="M{x0:.1f} {y0:.1f} A{r} {r} 0 {large} 1 {x1:.1f} {y1:.1f}"/>'


def mark(x, y, t):
    letter, color = TYPES[t]
    return (f'<g class="pk-p-m"><circle cx="{x}" cy="{y}" r="12" fill="{color}"/>'
            f'<text x="{x}" y="{y + 4.5}" text-anchor="middle">{letter}</text></g>')


def ghost(x, y):
    return (f'<g class="pk-p-ghost"><circle cx="{x}" cy="{y}" r="12"/>'
            f'<text x="{x}" y="{y + 5}" text-anchor="middle">+</text></g>')


def sun(x, y, r=9):
    rays = "".join(
        f'<line x1="{pt(x, y, r + 3, a)[0]:.1f}" y1="{pt(x, y, r + 3, a)[1]:.1f}" x2="{pt(x, y, r + 8, a)[0]:.1f}" y2="{pt(x, y, r + 8, a)[1]:.1f}"/>'
        for a in range(0, 360, 45))
    return f'<g class="pk-p-sun"><circle cx="{x}" cy="{y}" r="{r}"/>{rays}</g>'


def label(x, y, txt, cls="pk-p-lab", anchor="middle"):
    return f'<text class="{cls}" x="{x}" y="{y}" text-anchor="{anchor}">{html.escape(txt)}</text>'


def house_base(extra_ground=""):
    """Maison de plain-pied vue de dessus : façade avant en bas (rue), terrasse en haut."""
    s = []
    s.append('<rect class="pk-p-ground" x="0" y="0" width="640" height="460" rx="18"/>')
    s.append('<rect class="pk-p-street" x="0" y="412" width="640" height="48"/>')
    s.append(label(560, 442, "Rue", "pk-p-lab pk-p-lab--muted"))
    s.append('<rect class="pk-p-path" x="262" y="330" width="56" height="82"/>')
    s.append('<line class="pk-p-gate" x1="246" y1="412" x2="334" y2="412"/>')
    s.append(label(290, 402, "Portail", "pk-p-lab pk-p-lab--small"))
    s.append('<rect class="pk-p-terrace" x="170" y="38" width="170" height="52"/>')
    s.append(label(255, 70, "Terrasse", "pk-p-lab pk-p-lab--muted"))
    s.append(label(70, 60, "Jardin", "pk-p-lab pk-p-lab--muted", "start"))
    s.append(extra_ground)
    s.append('<rect class="pk-p-house" x="150" y="90" width="340" height="240"/>')
    s.append('<path class="pk-p-wall" d="M340 90V330M150 250H340M250 250V330M340 220H490"/>')
    s.append(label(245, 175, "Séjour"))
    s.append(label(415, 160, "Cuisine"))
    s.append(label(415, 280, "Chambre"))
    s.append(label(200, 295, "Chambre"))
    s.append(label(295, 295, "Entrée"))
    return s


def svg(body, aria, code):
    clip = f'<defs><clipPath id="pk-clip-{code}"><rect x="0" y="0" width="640" height="460" rx="18"/></clipPath></defs>'
    return (f'<svg class="pk-plan__svg" viewBox="0 0 640 460" role="img" aria-label="{html.escape(aria)}" '
            f'xmlns="http://www.w3.org/2000/svg">{clip}<g clip-path="url(#pk-clip-{code})">{"".join(body)}</g></svg>')


PLANS = {}

# ---------------- Essentiel : appartement ----------------
s = ['<rect class="pk-p-ground pk-p-ground--flat" x="0" y="0" width="640" height="460" rx="18"/>',
     '<rect class="pk-p-street" x="20" y="40" width="110" height="380"/>',
     label(75, 230, "Palier", "pk-p-lab pk-p-lab--muted"),
     '<rect class="pk-p-terrace" x="530" y="120" width="92" height="220"/>',
     label(576, 236, "Balcon", "pk-p-lab pk-p-lab--muted"),
     '<rect class="pk-p-house" x="130" y="40" width="400" height="380"/>',
     '<path class="pk-p-wall" d="M260 40V170M130 170H330M330 170V420M330 300H530"/>',
     label(195, 110, "Entrée"), label(420, 140, "Séjour"), label(230, 300, "Chambre"), label(430, 365, "Cuisine"),
     wedge(300, 52, 140, 25, 100, "pk-p-cone"),
     wedge(515, 55, 120, 100, 175, "pk-p-fan"),
     mark(130, 105, "C"), mark(530, 220, "C"), mark(230, 420, "C"),
     mark(515, 55, "M"), mark(300, 52, "V"), mark(576, 150, "S"),
     ghost(576, 305), ghost(450, 395)]
PLANS["ess"] = (svg(s, "Exemple d'installation du Pack Essentiel dans un appartement", "ess"), [
    ("C", "3 contacteurs 2-en-1", "porte d'entrée, porte-fenêtre du séjour, fenêtre de la chambre"),
    ("M", "1 détecteur de mouvement", "dans le séjour, la pièce de passage"),
    ("V", "1 caméra intérieure", "elle pivote pour couvrir le séjour"),
    ("S", "1 sirène solaire", "sur le balcon, visible de l'extérieur"),
    ("+", "Des emplacements libres", "pour ajouter une caméra extérieure ou des détecteurs plus tard"),
])

# ---------------- Sécurité Intégrale : maison + allée ----------------
s = house_base()
s += [wedge(478, 334, 175, 70, 182, "pk-p-cone"), arc(478, 334, 175, 70, 182),
      wedge(162, 102, 120, 5, 85, "pk-p-fan"), wedge(328, 102, 110, 100, 170, "pk-p-cone pk-p-cone--in"),
      mark(290, 330, "C"), mark(245, 90, "C"), mark(490, 150, "C"), mark(150, 290, "C"),
      mark(162, 102, "M"), mark(328, 102, "V"), mark(478, 334, "V"), mark(170, 330, "S")]
PLANS["psi"] = (svg(s, "Exemple d'installation du Pack Sécurité Intégrale dans une maison avec allée", "psi"), [
    ("C", "4 contacteurs 2-en-1", "porte d'entrée, baie vitrée, fenêtres de la cuisine et d'une chambre"),
    ("M", "1 détecteur de mouvement", "dans le séjour"),
    ("V", "2 caméras", "intérieure dans le séjour, extérieure rotative qui balaie l'allée et le portail"),
    ("S", "1 sirène solaire", "sur la façade, côté rue"),
])

# ---------------- Vision Duo : devant et derrière ----------------
s = house_base()
s += [wedge(305, 334, 150, 55, 125, "pk-p-cone"), wedge(205, 88, 130, 215, 325, "pk-p-cone"),
      wedge(162, 102, 120, 5, 85, "pk-p-fan"), wedge(258, 258, 80, 0, 90, "pk-p-fan"),
      wedge(328, 102, 110, 100, 170, "pk-p-cone pk-p-cone--in"),
      mark(270, 330, "C"), mark(285, 90, "C"), mark(490, 150, "C"), mark(150, 290, "C"), mark(490, 285, "C"),
      mark(162, 102, "M"), mark(258, 258, "M"), mark(328, 102, "V"), mark(305, 334, "V"), mark(205, 88, "V"),
      mark(170, 330, "S"),
      label(305, 380, "Avant", "pk-p-lab pk-p-lab--accent"), label(120, 30, "Arrière", "pk-p-lab pk-p-lab--accent", "start")]
PLANS["vdu"] = (svg(s, "Exemple d'installation du Pack Vision Duo : une caméra devant, une caméra derrière", "vdu"), [
    ("C", "5 contacteurs 2-en-1", "porte d'entrée, baie vitrée, fenêtres de la cuisine et des chambres"),
    ("M", "2 détecteurs de mouvement", "séjour et entrée"),
    ("V", "3 caméras", "une à l'entrée, une côté terrasse, une à l'intérieur"),
    ("S", "1 sirène solaire", "sur la façade, côté rue"),
])

# ---------------- Panorama : grand terrain, caméra rotative, fumée ----------------
extra = (label(580, 60, "Grand terrain", "pk-p-lab pk-p-lab--muted", "end"))
s = house_base(extra)
s += [wedge(490, 90, 190, 180, 395, "pk-p-cone"), arc(490, 90, 190, 180, 395),
      wedge(162, 102, 120, 5, 85, "pk-p-fan"), wedge(258, 258, 80, 0, 90, "pk-p-fan"),
      wedge(328, 102, 110, 100, 170, "pk-p-cone pk-p-cone--in"),
      mark(290, 330, "C"), mark(245, 90, "C"), mark(470, 220, "C"), mark(150, 290, "C"), mark(490, 285, "C"), mark(150, 170, "C"),
      mark(162, 102, "M"), mark(258, 258, "M"), mark(328, 102, "V"), mark(490, 90, "V"),
      mark(322, 264, "F"), mark(170, 330, "S")]
PLANS["pan"] = (svg(s, "Exemple d'installation du Pack Panorama : une caméra rotative qui balaie le terrain", "pan"), [
    ("C", "6 contacteurs 2-en-1", "portes d'entrée et de service, baie vitrée, fenêtres"),
    ("M", "2 détecteurs de mouvement", "séjour et entrée"),
    ("V", "2 caméras", "extérieure rotative à l'angle de la maison, intérieure dans le séjour"),
    ("F", "1 détecteur de fumée", "dans l'entrée, près des chambres"),
    ("S", "1 sirène solaire", "sur la façade, côté rue"),
])

# ---------------- Vision Duo Solaire ----------------
s = house_base(sun(600, 40, 14))
s += [wedge(305, 334, 150, 55, 125, "pk-p-cone"), wedge(205, 88, 130, 215, 325, "pk-p-cone"),
      wedge(162, 102, 120, 5, 85, "pk-p-fan"), wedge(258, 258, 80, 0, 90, "pk-p-fan"),
      wedge(328, 102, 110, 100, 170, "pk-p-cone pk-p-cone--in"),
      mark(270, 330, "C"), mark(285, 90, "C"), mark(490, 150, "C"), mark(150, 290, "C"), mark(490, 285, "C"), mark(150, 170, "C"),
      mark(162, 102, "M"), mark(258, 258, "M"), mark(328, 102, "V"), mark(305, 334, "V"), mark(205, 88, "V"),
      sun(333, 352, 6), sun(181, 70, 6),
      mark(322, 264, "F"), mark(170, 330, "S"),
      label(305, 392, "Avant", "pk-p-lab pk-p-lab--accent"), label(120, 30, "Arrière", "pk-p-lab pk-p-lab--accent", "start")]
PLANS["vds"] = (svg(s, "Exemple d'installation du Pack Vision Duo Solaire : deux caméras extérieures rechargées par panneau solaire", "vds"), [
    ("C", "6 contacteurs 2-en-1", "portes, baie vitrée et fenêtres"),
    ("M", "2 détecteurs de mouvement", "séjour et entrée"),
    ("V", "3 caméras", "deux extérieures avec panneau solaire (soleil sur le plan), une intérieure"),
    ("F", "1 détecteur de fumée", "dans l'entrée, près des chambres"),
    ("S", "1 sirène solaire", "sur la façade, côté rue"),
])

# ---------------- Panorama Duo : deux niveaux ----------------
s = ['<rect class="pk-p-ground" x="0" y="0" width="640" height="460" rx="18"/>',
     label(170, 34, "Rez-de-chaussée", "pk-p-lab pk-p-lab--title"), label(470, 34, "Étage", "pk-p-lab pk-p-lab--title"),
     # rez-de-chaussée
     '<rect class="pk-p-house" x="40" y="70" width="260" height="300"/>',
     '<path class="pk-p-wall" d="M170 70V250M40 250H300M200 250V370M170 160H300"/>',
     label(105, 160, "Séjour"), label(235, 120, "Cuisine"), label(235, 210, "Bureau"), label(120, 315, "Garage"), label(250, 315, "Entrée"),
     # étage
     '<rect class="pk-p-house" x="340" y="70" width="260" height="300"/>',
     '<path class="pk-p-wall" d="M470 70V200M340 200H600M430 200V280M340 280H430M510 200V370"/>',
     label(405, 140, "Chambre"), label(535, 140, "Chambre"), label(385, 245, "Bain"), label(385, 330, "Chambre"), label(555, 290, "Palier"),
     '<rect class="pk-p-street" x="0" y="412" width="640" height="48"/>', label(560, 442, "Rue", "pk-p-lab pk-p-lab--muted"),
     # caméras rotatives : avant (rez-de-chaussée) et arrière (étage)
     wedge(300, 370, 150, 20, 180, "pk-p-cone"), arc(300, 370, 150, 20, 180),
     wedge(600, 70, 150, 182, 360, "pk-p-cone"), arc(600, 70, 150, 182, 360),
     wedge(52, 82, 110, 5, 85, "pk-p-fan"), wedge(212, 258, 80, 0, 90, "pk-p-fan"), wedge(588, 212, 90, 95, 175, "pk-p-fan"),
     wedge(158, 82, 100, 100, 170, "pk-p-cone pk-p-cone--in"),
     mark(250, 370, "C"), mark(105, 70, "C"), mark(300, 115, "C"), mark(40, 315, "C"), mark(300, 205, "C"),
     mark(405, 70, "C"), mark(600, 140, "C"), mark(340, 330, "C"),
     mark(52, 82, "M"), mark(212, 258, "M"), mark(588, 212, "M"),
     mark(158, 82, "V"), mark(300, 370, "V"), mark(600, 70, "V"),
     mark(262, 290, "F"), mark(555, 330, "F"), mark(60, 370, "S")]
PLANS["pdu"] = (svg(s, "Exemple d'installation du Pack Panorama Duo dans une maison à étage", "pdu"), [
    ("C", "8 contacteurs 2-en-1", "5 au rez-de-chaussée, 3 à l'étage"),
    ("M", "3 détecteurs de mouvement", "séjour, entrée et palier"),
    ("V", "3 caméras", "deux extérieures rotatives sur deux façades, une intérieure"),
    ("F", "2 détecteurs de fumée", "un par niveau"),
    ("S", "1 sirène solaire", "sur la façade, côté rue"),
])


def legend(items):
    out = []
    for t, title, detail in items:
        if t == "+":
            sym = '<span class="pk-plan__sym pk-plan__sym--ghost" aria-hidden="true">+</span>'
        else:
            letter, color = TYPES[t]
            sym = f'<span class="pk-plan__sym" style="background:{color}" aria-hidden="true">{letter}</span>'
        out.append(f'<li>{sym}<span><strong>{html.escape(title)}</strong> · {html.escape(detail)}</span></li>')
    return '<ul class="pk-plan__legende">' + "".join(out) + "</ul>"


parts = ["{%- comment -%}\n  Plan d'installation propre à chaque pack de la gamme 2026 (fichier généré).\n"
         "  Paramètres : code (ess, psi, vdu, pan, vds, pdu) et part ('svg' ou 'legende').\n"
         "  Lettres : C contacteur, M détecteur de mouvement, V caméra, S sirène, F détecteur de fumée.\n"
         "  Les zones colorées montrent le champ des caméras (couleur du pack) et des détecteurs.\n{%- endcomment -%}\n",
         "{%- case code -%}\n"]
for code, (sv, items) in PLANS.items():
    parts.append(f"{{%- when '{code}' -%}}\n{{%- if part == 'legende' -%}}{legend(items)}{{%- else -%}}{sv}{{%- endif -%}}\n")
parts.append("{%- endcase -%}\n")
open(OUT, "w").write("".join(parts))

CSS = """
.pk-plan__svg{width:100%;height:auto;display:block;font-family:inherit;}
.pk-p-ground{fill:#eef3ea;}
.pk-p-ground--flat{fill:#f1f1f4;}
.pk-p-street{fill:#dfe0e6;}
.pk-p-path{fill:#e6e1d6;}
.pk-p-terrace{fill:#e9e5dc;}
.pk-p-gate{stroke:#8a8a92;stroke-width:4;stroke-dasharray:8 5;}
.pk-p-house{fill:#fff;stroke:#1d1d1f;stroke-width:5;}
.pk-p-wall{fill:none;stroke:#1d1d1f;stroke-width:2.5;opacity:.55;}
.pk-p-lab{font-size:15px;fill:#6e6e73;font-weight:600;}
.pk-p-lab--muted{fill:#8a8f88;font-weight:500;}
.pk-p-lab--small{font-size:12px;}
.pk-p-lab--title{font-size:16px;fill:#1d1d1f;font-weight:700;}
.pk-p-lab--accent{fill:var(--pk-accent,#0c1e4a);font-weight:700;font-size:14px;letter-spacing:.06em;text-transform:uppercase;}
.pk-p-cone{fill:var(--pk-accent,#0c1e4a);opacity:.18;}
.pk-p-cone--in{opacity:.12;}
.pk-p-fan{fill:#4b5770;opacity:.1;}
.pk-p-arc{fill:none;stroke:var(--pk-accent,#0c1e4a);stroke-width:2;stroke-dasharray:6 6;opacity:.7;}
.pk-p-m circle{stroke:#fff;stroke-width:3;}
.pk-p-m text{fill:#fff;font-size:13px;font-weight:700;}
.pk-p-ghost circle{fill:#fff;stroke:var(--pk-accent,#0c1e4a);stroke-width:2;stroke-dasharray:4 3;}
.pk-p-ghost text{fill:var(--pk-accent,#0c1e4a);font-size:18px;font-weight:700;}
.pk-p-sun circle{fill:#f5b400;}
.pk-p-sun line{stroke:#f5b400;stroke-width:2.5;stroke-linecap:round;}
.pk-plan__legende{list-style:none;margin:22px 0 0;padding:0;display:grid;gap:12px;}
.pk-plan__legende li{display:flex;gap:12px;align-items:flex-start;font-size:15px;line-height:1.45;}
.pk-plan__sym{flex-shrink:0;width:26px;height:26px;border-radius:50%;color:#fff;font-size:13px;font-weight:700;display:inline-flex;align-items:center;justify-content:center;}
.pk-plan__sym--ghost{background:#fff;color:var(--pk-accent,#0c1e4a);border:2px dashed var(--pk-accent,#0c1e4a);}
"""
ACC = {"ess": "#1d5fd1", "psi": "#c81e2e", "vdu": "#0f766e", "pan": "#2f7a3b", "vds": "#b45309", "pdu": "#5b2fb0"}
cards = "".join(
    f'<section style="--pk-accent:{ACC[c]};display:grid;grid-template-columns:1.2fr 1fr;gap:28px;align-items:center;margin:0 0 40px;font-family:system-ui,sans-serif">'
    f'<div>{sv}</div><div><h2 style="color:{ACC[c]};margin:0">{c}</h2>{legend(items)}</div></section>'
    for c, (sv, items) in PLANS.items())
open(TEST, "w").write(f"<!doctype html><meta charset=utf-8><style>body{{margin:24px;max-width:1200px}}{CSS}</style>{cards}")
open(OUT.replace('.liquid', '.css'), "w").write(CSS)
print("ok", len(open(OUT).read()), "octets")
