#!/usr/bin/env python3
"""Génère les sections et le template de la page collection Touch / Touch XL.

Sources : theme-src/collection-touch/*.liquid (HTML + CSS autonomes, une section par fichier).
Sorties :
  - sections/tc-*.liquid                          (fichiers de section du thème)
  - templates/collection.collection-touch.json    (template de la page)

Usage : python3 theme-src/build-collection-touch.py
"""
import json, os, sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SRC = os.path.join(ROOT, 'theme-src', 'collection-touch')
BASE = os.path.join(ROOT, 'theme-src', 'collection-touch.base.json')
SECTIONS_DIR = os.path.join(ROOT, 'sections')
OUT = os.path.join(ROOT, 'templates', 'collection.collection-touch.json')

# fichier source -> (type de section, nom affiché dans l'éditeur de thème)
SECTIONS = [
    ('01-hero.liquid',         'tc-hero',         'Touch — Hero'),
    ('02-duel.liquid',         'tc-duel',         'Touch — Duel Touch/XL'),
    ('03-verdict.liquid',      'tc-verdict',      'Touch — Quel modèle ?'),
    ('12-packs.liquid',        'tc-packs',        'Touch — Packs'),
    ('04-anatomie.liquid',     'tc-anatomie',     'Touch — Anatomie'),
    ('05-pilotage.liquid',     'tc-pilotage',     'Touch — Pilotage'),
    ('06-journee.liquid',      'tc-journee',      'Touch — Journée type'),
    ('07-pourquoi.liquid',     'tc-pourquoi',     'Touch — Pourquoi'),
    ('08-installation.liquid', 'tc-installation', 'Touch — Installation'),
    ('09-evolutivite.liquid',  'tc-evolutivite',  'Touch — Évolutivité'),
    ('10-specs.liquid',        'tc-specs',        'Touch — Fiche technique'),
    ('11-faq.liquid',          'tc-faq',          'Touch — FAQ'),
    ('13-cta.liquid',          'tc-cta',          'Touch — CTA final'),
    ('14-configurateur.liquid', 'tc-configurateur','Touch — Configurateur'),
]

# Ordre d'affichage de la page, puis les sections héritées laissées désactivées.
ORDER = [
    'tc-hero', 'tc-duel', 'tc-verdict', 'tc-packs',
    '1778166532d7ba2ea9',        # carrousel UGC Moast
    'tc-anatomie', 'tc-pilotage', 'tc-journee', 'tc-pourquoi', 'tc-installation', 'tc-evolutivite',
    'tc-configurateur',          # bandeau configurateur
    'image_with_text_Fhj8Um',    # Ils ont choisi Daewoo Security
    '17537033312cec849b',        # avis Judge.me
    'tc-specs', 'tc-faq', 'tc-cta',
    # --- sections standard de collection, conservées désactivées ---
    'main-collection-banner', 'main-collection', '1767695119ebd7d2c9',
]

# Sections d'origine devenues inutilisées, retirées du template. Elles restent
# consultables dans theme-src/collection-touch.base.json et dans le thème publié.
DROPPED = [
    'custom_liquid_cWkFzx',
    'custom_liquid_LmmcWi', 'custom_liquid_ztNiqY', 'custom_liquid_ThwXGh', 'custom_liquid_UHgzRF',
    'faq_h7K6fC', 'faq_8TYcdM',
    'portfolio_T7znjL', 'reveal_video_with_text_overlay_q7KxVw',
    'image_with_text_ccMRUa', 'featured_product_zBDEMt', 'image_with_text_7JB7zG',
    'collage_DxcbGU', 'video_with_text_3RUzYJ', 'multicolumn_63eiUh', 'rich_text_baMk8h',
    'scrolling_banner_kpB7UQ', 'multicolumn_wrKDcG', 'video_with_text_mMWCBm',
]

NEW_TYPES = {typ for _, typ, _ in SECTIONS}


def write_sections():
    os.makedirs(SECTIONS_DIR, exist_ok=True)
    for src, typ, label in SECTIONS:
        body = open(os.path.join(SRC, src), encoding='utf-8').read().rstrip('\n')
        schema = json.dumps({'name': label, 'settings': []}, ensure_ascii=False, indent=2)
        path = os.path.join(SECTIONS_DIR, typ + '.liquid')
        with open(path, 'w', encoding='utf-8') as f:
            f.write('%s\n\n{%% schema %%}\n%s\n{%% endschema %%}\n' % (body, schema))


def write_template():
    with open(BASE, encoding='utf-8') as f:
        tpl = json.load(f)

    for sid in DROPPED:
        tpl['sections'].pop(sid, None)

    for _, typ, _ in SECTIONS:
        tpl['sections'][typ] = {'type': typ, 'settings': {}}

    missing = [s for s in ORDER if s not in tpl['sections']]
    if missing:
        sys.exit('Sections absentes du template : %s' % ', '.join(missing))
    extra = [s for s in tpl['sections'] if s not in ORDER]
    if extra:
        sys.exit("Sections hors de l'ordre défini : %s" % ', '.join(extra))

    tpl['order'] = ORDER
    tpl['sections'] = {sid: tpl['sections'][sid] for sid in ORDER}

    os.makedirs(os.path.dirname(OUT), exist_ok=True)
    with open(OUT, 'w', encoding='utf-8') as f:
        json.dump(tpl, f, ensure_ascii=False, indent=2)
        f.write('\n')
    return len(ORDER), os.path.getsize(OUT)


if __name__ == '__main__':
    write_sections()
    n, size = write_template()
    print('%d fichiers de section écrits dans sections/' % len(SECTIONS))
    print('Template : %s (%d sections, %d octets)' % (OUT, n, size))
