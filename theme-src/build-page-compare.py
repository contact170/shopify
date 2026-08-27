#!/usr/bin/env python3
"""Construit les sections + le template de la page comparatif (page.compare.json)."""
import io, json, os, re

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SRC  = os.path.join(ROOT, 'theme-src', 'page-compare')
OUT  = os.path.join(ROOT, 'sections')
TPL  = os.path.join(ROOT, 'templates', 'page.compare.json')

SECTIONS = [
    ('01-intro.liquid',       'cp-intro',       'Comparatif — Intro'),
    ('02-orienteur.liquid',   'cp-orienteur',   'Comparatif — Choix'),
    ('03-gammes.liquid',      'cp-gammes',      'Comparatif — Gammes'),
    ('04-tableau.liquid',     'cp-tableau',     'Comparatif — Tableau'),
    ('05-differences.liquid', 'cp-differences', 'Comparatif — Écarts'),
    ('06-cta.liquid',         'cp-cta',         'Comparatif — CTA'),
]
ORDER = [s[1] for s in SECTIONS]

HEADER = ("/*\n * ------------------------------------------------------------\n"
          " * IMPORTANT: The contents of this file are auto-generated.\n *\n"
          " * This file may be updated by the Shopify admin theme editor\n"
          " * or related systems. Please exercise caution as any changes\n"
          " * made to this file may be overwritten.\n"
          " * ------------------------------------------------------------\n */\n")

os.makedirs(OUT, exist_ok=True)
for fname, sid, label in SECTIONS:
    assert len(label) <= 25, f'{label!r} dépasse 25 caractères'
    body = io.open(os.path.join(SRC, fname), encoding='utf-8').read().rstrip('\n')
    schema = '{%% schema %%}\n{\n  "name": %s,\n  "settings": []\n}\n{%% endschema %%}\n' % json.dumps(label, ensure_ascii=False)
    io.open(os.path.join(OUT, sid + '.liquid'), 'w', encoding='utf-8').write(body + '\n\n' + schema)

tpl = {"sections": {sid: {"type": sid, "settings": {}} for sid in ORDER}, "order": ORDER}
io.open(TPL, 'w', encoding='utf-8').write(HEADER + json.dumps(tpl, ensure_ascii=False, indent=2) + '\n')

print('%d sections écrites dans sections/' % len(SECTIONS))
print('Template : %s (%d sections, %d octets)' % (TPL, len(ORDER), os.path.getsize(TPL)))
