#!/usr/bin/env python3
"""Assemble templates/collection.collection-touch.json from theme-src/collection-touch/*.liquid.

Source of truth for the AM301 / AM302 (Touch / Touch XL) collection page.
Run:  python3 theme-src/build-collection-touch.py
"""
import json, os, sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SRC = os.path.join(ROOT, 'theme-src', 'collection-touch')
BASE = os.path.join(ROOT, 'theme-src', 'collection-touch.base.json')
OUT = os.path.join(ROOT, 'templates', 'collection.collection-touch.json')

CL_DEFAULTS = {
    "color_text": "", "color_background": "", "gradient_background": "",
    "color_button_text": "", "color_button_background": "", "color_button_gradient": "",
    "padding_top": 0, "padding_bottom": 0, "divider": False, "narrow": False, "rounded": False,
}

def read(name):
    with open(os.path.join(SRC, name), encoding='utf-8') as f:
        return f.read().rstrip('\n')

def custom_liquid(name):
    return {
        "type": "custom-liquid",
        "name": "t:sections.custom-liquid.name",
        "settings": dict(liquid=read(name), **CL_DEFAULTS),
    }

# id -> source file. Existing ids are reused so the section keeps its place
# in the theme editor; tc_* ids are new sections introduced by the redesign.
MAPPING = [
    ("custom_liquid_LmmcWi", "01-hero.liquid"),
    ("tc_duel",              "02-duel.liquid"),
    ("tc_verdict",           "03-verdict.liquid"),
    ("custom_liquid_ztNiqY", "12-packs.liquid"),
    ("tc_anatomie",          "04-anatomie.liquid"),
    ("tc_pilotage",          "05-pilotage.liquid"),
    ("tc_journee",           "06-journee.liquid"),
    ("custom_liquid_UHgzRF", "07-pourquoi.liquid"),
    ("custom_liquid_ThwXGh", "08-installation.liquid"),
    ("tc_evolutivite",       "09-evolutivite.liquid"),
    ("faq_h7K6fC",           "10-specs.liquid"),
    ("faq_8TYcdM",           "11-faq.liquid"),
    ("tc_cta",               "13-cta.liquid"),
]

# Visible page order, then the legacy sections left disabled in the theme editor.
ORDER = [
    "custom_liquid_LmmcWi",
    "tc_duel",
    "tc_verdict",
    "custom_liquid_ztNiqY",
    "1778166532d7ba2ea9",        # carrousel UGC Moast
    "tc_anatomie",
    "tc_pilotage",
    "tc_journee",
    "custom_liquid_UHgzRF",
    "custom_liquid_ThwXGh",
    "tc_evolutivite",
    "custom_liquid_cWkFzx",      # bandeau configurateur
    "image_with_text_Fhj8Um",    # Ils ont choisi Daewoo Security
    "17537033312cec849b",        # avis Judge.me
    "faq_h7K6fC",
    "faq_8TYcdM",
    "tc_cta",
    # --- sections héritées, laissées désactivées ---
    "portfolio_T7znjL", "main-collection-banner", "reveal_video_with_text_overlay_q7KxVw",
    "image_with_text_ccMRUa", "featured_product_zBDEMt", "image_with_text_7JB7zG",
    "collage_DxcbGU", "video_with_text_3RUzYJ", "multicolumn_63eiUh", "rich_text_baMk8h",
    "scrolling_banner_kpB7UQ", "multicolumn_wrKDcG", "main-collection",
    "video_with_text_mMWCBm", "1767695119ebd7d2c9",
]

def main():
    with open(BASE, encoding='utf-8') as f:
        tpl = json.load(f)

    for sid, filename in MAPPING:
        tpl['sections'][sid] = custom_liquid(filename)

    missing = [s for s in ORDER if s not in tpl['sections']]
    if missing:
        sys.exit('Sections absentes du template : %s' % ', '.join(missing))
    extra = [s for s in tpl['sections'] if s not in ORDER]
    if extra:
        sys.exit("Sections présentes mais absentes de l'ordre : %s" % ', '.join(extra))

    tpl['order'] = ORDER
    tpl['sections'] = {sid: tpl['sections'][sid] for sid in ORDER}

    os.makedirs(os.path.dirname(OUT), exist_ok=True)
    with open(OUT, 'w', encoding='utf-8') as f:
        json.dump(tpl, f, ensure_ascii=False, indent=2)
        f.write('\n')
    print('Écrit : %s (%d sections, %d octets)' % (OUT, len(ORDER), os.path.getsize(OUT)))

if __name__ == '__main__':
    main()
