#!/usr/bin/env python3
"""Génère les sections et le template de la page collection ÉLITE (PA501Z).

Sources : theme-src/collection-elite/*.liquid (HTML + CSS autonomes, une section par fichier).
Sorties :
  - sections/el-*.liquid                            (fichiers de section du thème)
  - templates/collection.collection-elite-2.json    (template de la page)

Usage : python3 theme-src/build-collection-elite.py
"""
import json, os

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SRC = os.path.join(ROOT, 'theme-src', 'collection-elite')
BASE = os.path.join(ROOT, 'theme-src', 'collection-elite.base.json')
SECTIONS_DIR = os.path.join(ROOT, 'sections')
OUT = os.path.join(ROOT, 'templates', 'collection.collection-elite-2.json')

# fichier source -> (type de section, nom affiché dans l'éditeur de thème, max 25 car.)
SECTIONS = [
    ('01-hero.liquid',          'el-hero',          'Élite — Hero'),
    ('02-reseaux.liquid',       'el-reseaux',       'Élite — Triple connexion'),
    ('03-zigbee.liquid',        'el-zigbee',        'Élite — Zigbee'),
    ('04-packs.liquid',         'el-packs',         'Élite — Packs'),
    ('05-anatomie.liquid',      'el-anatomie',      'Élite — Anatomie'),
    ('06-app.liquid',           'el-app',           'Élite — Pilotage app'),
    ('07-privacy.liquid',       'el-privacy',       'Élite — Confidentialité'),
    ('08-installation.liquid',  'el-installation',  'Élite — Installation'),
    ('09-accessoires.liquid',   'el-accessoires',   'Élite — Accessoires'),
    ('10-configurateur.liquid', 'el-configurateur', 'Élite — Configurateur'),
    ('11-specs.liquid',         'el-specs',         'Élite — Fiche technique'),
    ('12-faq.liquid',           'el-faq',           'Élite — FAQ'),
    ('13-cta.liquid',           'el-cta',           'Élite — CTA final'),
]

# Ordre d'affichage, puis les sections standard laissées désactivées.
ORDER = [
    'el-hero', 'el-reseaux', 'el-zigbee', 'el-packs',
    'el-anatomie', 'el-app', 'el-privacy', 'el-installation', 'el-accessoires',
    'el-configurateur',
    'tc-temoignage',            # « Ils ont choisi Daewoo Security » (section partagée)
    '17537033312cec849b',       # avis Judge.me
    'el-specs', 'el-faq', 'el-cta',
    # --- sections standard de collection, conservées désactivées ---
    'main-collection-banner', 'main-collection',
]

# Sections d'origine remplacées par la refonte, retirées du template. Elles restent
# consultables dans theme-src/collection-elite.base.json et dans le thème publié.
DROPPED = [
    'custom_liquid_rDimba',   # ancien hero
    'custom_liquid_4JkcDY',   # bandeau désactivé
    'custom_liquid_MFK3nh',   # anciens packs (PA570 / PA574, produits archivés)
    'custom_liquid_t3y4Gq',   # ancienne installation
    'custom_liquid_aYq3gY',   # ancien bandeau configurateur
    'custom_liquid_ETnkHn',   # ancien « Pourquoi choisir »
    'image_with_text_4AH9rC', # temporisation (repris dans la fiche technique)
    'faq_gtMVaJ',             # ancienne FAQ « Détails produit »
    'faq_qNU8cD',             # ancienne FAQ générale
    'image_with_text_Fhj8Um', # remplacé par la section tc-temoignage
]

NEW_TYPES = {typ for _, typ, _ in SECTIONS}


def write_sections():
    os.makedirs(SECTIONS_DIR, exist_ok=True)
    for src, typ, label in SECTIONS:
        body = open(os.path.join(SRC, src), encoding='utf-8').read().rstrip('\n')
        schema = json.dumps({'name': label, 'settings': []}, ensure_ascii=False, indent=2)
        with open(os.path.join(SECTIONS_DIR, typ + '.liquid'), 'w', encoding='utf-8') as f:
            f.write('%s\n\n{%% schema %%}\n%s\n{%% endschema %%}\n' % (body, schema))


def write_template():
    with open(BASE, encoding='utf-8') as f:
        tpl = json.load(f)

    for sid in DROPPED:
        tpl['sections'].pop(sid, None)

    for _, typ, _ in SECTIONS:
        tpl['sections'][typ] = {'type': typ, 'settings': {}}
    tpl['sections']['tc-temoignage'] = {'type': 'tc-temoignage', 'settings': {}}

    for sid in ('main-collection-banner', 'main-collection'):
        if sid in tpl['sections']:
            tpl['sections'][sid]['disabled'] = True

    missing = [s for s in ORDER if s not in tpl['sections']]
    if missing:
        raise SystemExit('sections absentes du template : %s' % missing)
    extra = [s for s in tpl['sections'] if s not in ORDER]
    if extra:
        raise SystemExit('sections orphelines : %s' % extra)

    tpl['sections'] = {sid: tpl['sections'][sid] for sid in ORDER}
    tpl['order'] = list(ORDER)

    with open(OUT, 'w', encoding='utf-8') as f:
        json.dump(tpl, f, ensure_ascii=False, indent=2)
        f.write('\n')
    return len(tpl['order']), os.path.getsize(OUT)


if __name__ == '__main__':
    write_sections()
    n, size = write_template()
    print('%d fichiers de section écrits dans sections/' % len(SECTIONS))
    print('Template : %s (%d sections, %d octets)' % (OUT, n, size))
