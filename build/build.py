# -*- coding: utf-8 -*-
"""Emit one bespoke landing section + template per Élite pack.

The six Élite pages are near-identical: only the hero, the box contents,
the three feature blocks and the spec grid change from one pack to the
next. Everything else — the centrale anatomy, the continuity matrix, the
SIM module, the Zigbee module, the accessory picker, the FAQ — is shared
copy that the merchant has revised three times already in review.

So the pages are generated rather than hand-copied: the shared wording
lives once, in tpl-*.liquid, and a change to it is re-emitted to all six
files. The theme still receives six self-contained sections, matching the
convention the Vigilia range already uses (product-vig50x-landing.liquid).

Usage: python3 build.py   →  writes out/product-<key>-landing.liquid
                             and out/product.<suffix>.json
"""
import json, os, re, sys

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
from packs import PACKS  # noqa: E402

OUT = os.path.join(os.path.dirname(HERE), 'out')
VIG = os.path.join(os.path.dirname(HERE), 'vig503-landing.liquid')
VIG_TPL = os.path.join(os.path.dirname(HERE), 'vig503.json')

CHECK = ('<svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" '
         'stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M20 6 9 17l-5-5">'
         '</path></svg>')


def contents_html(rows):
    out = []
    for row in rows:
        qty, name, desc = row[0], row[1], row[2]
        zig = len(row) > 3 and row[3] == 'zig'
        out.append('        <div class="pv-contents__item">\n'
                   '          <span class="pv-contents__qty">%s</span>\n'
                   '          <div>\n'
                   '            <div class="pv-contents__name">%s</div>\n'
                   '            <div class="pv-contents__desc">%s</div>\n' % (qty, name, desc))
        if zig:
            out.append('            <span class="pe-zigtag">Zigbee 3.0</span>\n')
        out.append('          </div>\n        </div>\n')
    return ''.join(out)


def features_html(feats):
    out = []
    for i, f in enumerate(feats):
        alt = 'pv-section--alt' if i % 2 == 0 else ''
        rev = ' pv-feature--reverse' if i % 2 == 1 else ''
        bullets = ''.join(
            '            <li>%s%s</li>\n' % (CHECK, b) for b in f['bullets'])
        # A feature can point at a Shopify Files asset (the app screenshot has
        # no product to hang off) instead of a Liquid image object.
        if f.get('src'):
            # height:auto because the theme's `.pv img` sets max-width but not
            # height — with both attributes present the image would squash.
            media = ('          <img src="%s" alt="%s" loading="lazy" '
                     'width="%d" height="%d" style="height:auto;">\n'
                     % (f['src'], f['alt'], f.get('w', 1000), f.get('h', 1000)))
        else:
            media = ('          {{ %s | image_url: width: 1000 | image_tag: loading: \'lazy\', '
                     'widths: \'500,750,1000\', alt: \'%s\' }}\n' % (f['img'], f['alt']))
        out.append(
            '  {%%- comment -%%} Feature %d {%%- endcomment -%%}\n'
            '  <section class="pv-section %s">\n'
            '    <div class="pv-wrap">\n'
            '      <div class="pv-feature%s pv-reveal">\n'
            '        <div class="pv-feature__media">\n'
            '%s'
            '        </div>\n'
            '        <div class="pv-feature__body">\n'
            '          <span class="pv-feature__num">%s</span>\n'
            '          <h2>%s</h2>\n'
            '          <p class="pv-feature__text">\n            %s\n          </p>\n'
            '          <ul>\n%s          </ul>\n'
            '        </div>\n      </div>\n    </div>\n  </section>\n\n'
            % (i + 1, alt, rev, media, f['eyebrow'], f['h2'], f['text'], bullets))
    return ''.join(out)


def specs_html(p):
    rows = [
        ('Connectivité', 'Ethernet RJ45 (prioritaire), Wi-Fi 2,4 GHz&#10;4G+ en secours avec carte SIM M2M en option'),
        ('Réseau capteurs', 'Passerelle Zigbee 3.0 intégrée&#10;Radio bidirectionnelle chiffrée, anti-brouillage'),
        ('Alimentation &amp; autonomie', 'Centrale : secteur + batterie de secours 10 h&#10;Sirène extérieure solaire, autonome'),
        ('Caméras incluses', p['specs_cams']),
        ('Capteurs inclus', p['specs_sensors']),
        ('Évolutivité', "Jusqu'à 200 accessoires&#10;Compatible gamme SA501, hors WDS501, WVD501 et WKE501"),
        ('Compatibilité tierce', 'Équipements Zigbee 3.0 et Tuya&#10;Non compatible Alexa et Google Home'),
        ('Installation', 'Sans technicien ni câblage pour les capteurs&#10;Appairage guidé par Daewoo Home Connect'),
    ]
    out = ''.join(
        '        <div class="pv-specs__item">\n          <dt>%s</dt>\n          <dd>%s</dd>\n        </div>\n'
        % (k, v) for k, v in rows)
    out += ('        <div class="pv-specs__item">\n          <dt>Référence</dt>\n'
            '          <dd class="pv-ref">{{ variant.sku | default: \'%s\' }}</dd>\n        </div>\n' % p['sku'])
    return out


def chips_html(chips):
    out = ['\n']
    for kind, label in chips:
        cls = 'pe-chip pe-chip--%s' % kind if kind else 'pe-chip'
        out.append('        <span class="%s">%s</span>\n' % (cls, label))
    out.append('      ')
    return ''.join(out)


def zig2_html(pair):
    return ('          <h3>%s</h3>\n          <p>%s</p>' % pair)


def build():
    src = open(VIG).read().split('\n')
    css_core = '\n'.join(src[143:534])
    alma = '\n'.join(src[1200:1235]).replace('PVAlmaModal-', 'PEAlmaModal-')

    head_t = open(os.path.join(HERE, 'tpl-head.liquid')).read()
    body_t = open(os.path.join(HERE, 'tpl-body.liquid')).read()
    # Two hero variants: v1 is the original order (texte, puis visuel,
    # puis CTA), v2 remonte le visuel et le CTA sous la tagline. En test
    # sur un seul pack le temps que le marchand compare — quand la v2
    # sera validée, il suffit de la passer en défaut et de supprimer v1.
    heroes = {'v1': open(os.path.join(HERE, 'tpl-hero.liquid')).read(),
              'v2': open(os.path.join(HERE, 'tpl-hero2.liquid')).read()}
    tail_t = open(os.path.join(HERE, 'tpl-tail.liquid')).read()
    css_extra = open(os.path.join(HERE, 'css-extra.liquid')).read()

    raw = re.sub(r'/\*.*?\*/', '', open(VIG_TPL).read(), flags=re.S)
    help_drawer = json.loads(raw)['sections']['help-drawer']

    os.makedirs(OUT, exist_ok=True)
    for p in PACKS:
        subs = {
            '%%DOC_PRODUCT%%': p['doc'],
            '%%CAM_EXT%%': p['cam_ext'],
            '%%IMG1%%': p['img1'],
            '%%SKU%%': p['sku'],
            '%%STICKY%%': p['sticky'],
            '%%H1%%': p['h1'],
            '%%TAGLINE%%': p['tagline'],
            '%%SUB%%': p['sub'],
            '%%SUMMARY%%': p['summary'],
            '%%CHIPS%%': chips_html(p['chips']),
            '%%CONTENTS_LEAD%%': p['contents_lead'],
            '%%CONTENTS%%': contents_html(p['contents']),
            '%%ZIG2%%': zig2_html(p['zig2']),
            '%%BAND_TITLE%%': p['band'],
            '%%TOTAL_BASE%%': p['total_base'],
            '%%FEATURES%%': features_html(p['features']),
            '%%SPECS_LEAD%%': p['specs_lead'],
            '%%SPECS%%': specs_html(p),
            '%%FINAL_TITLE%%': p['final'],
            '%%LD_DESC%%': p['ld'],
            '%%JS_PACKNAME%%': p['js_name'],
            '%%SCHEMA_NAME%%': p['schema'],
        }
        body = body_t.replace('%%HERO%%', heroes[p.get('hero', 'v1')])
        head, tail = head_t, tail_t
        for k, v in subs.items():
            head, body, tail = head.replace(k, v), body.replace(k, v), tail.replace(k, v)
        # Keep the figure and its unit on one line. Body only: the same string
        # inside the JSON-LD of the tail would render as a literal "&nbsp;".
        body = body.replace('10 h', '10&nbsp;h')

        section = (head + '\n<div id="shopify-section-{{ section.id }}" class="pv">\n'
                   + '  <style>\n' + css_core + '\n' + css_extra + '  </style>\n'
                   + body + '\n' + alma + '\n' + tail)

        left = re.findall(r'%%[A-Z0-9_]+%%', section)
        assert not left, (p['key'], set(left))
        # Shopify caps a section schema name at 25 characters. Over that,
        # themeFilesUpsert drops the file and reports no error at all.
        assert len(p['schema']) <= 25, (p['key'], p['schema'], len(p['schema']))

        name = 'product-%s-landing' % p['key']
        open(os.path.join(OUT, name + '.liquid'), 'w').write(section)
        tpl = {'sections': {'main': {'type': name, 'settings': {}},
                            'help-drawer': help_drawer},
               'order': ['main', 'help-drawer']}
        open(os.path.join(OUT, 'product.%s.json' % p['suffix']), 'w').write(
            json.dumps(tpl, ensure_ascii=False, indent=2))
        print('%-12s %7d bytes  ->  sections/%s.liquid + templates/product.%s.json'
              % (p['sku'], len(section), name, p['suffix']))


if __name__ == '__main__':
    build()
