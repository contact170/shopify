# -*- coding: utf-8 -*-
"""Per-pack content for the Élite PA501Z landing pages.

Everything in here comes from each product's own descriptionHtml in the
Shopify catalogue, normalised against two facts the merchant confirmed
and that several of those descriptions still contradict:

  - the centrale is the PA501Z (PA573's description says "PA500Z", a typo,
    and PA571's calls it "Centrale PA571");
  - its backup battery lasts 10 h (several descriptions claim 12 h).

PA571's description lists its contacteurs and détecteurs de vibration
generically, without references. The merchant has since confirmed they are
the Zigbee ones, so the page names them WDS502Z and WVD502Z like the rest
of the range.
"""

CENTRALE = ('Centrale Élite PA501Z',
            'Ethernet RJ45, Wi-Fi 2,4 GHz, 4G+ (carte SIM en option), passerelle Zigbee 3.0. Batterie de secours 10 h.')
SIRENE = ('Sirène extérieure solaire WOS501S',
          'Flash lumineux et sirène en façade, rechargée par la lumière du jour. Aucune prise nécessaire.')
IP506P = ('Caméra intérieure motorisée IP506P',
          'Rotation 360°, auto-tracking, vision nocturne. Objectif qui se rétracte physiquement en mode Vie Privée. Alimentation secteur.')
FIXATIONS = ('Fixations, notices et autocollants dissuasifs',
             "Tout le nécessaire d'installation est fourni dans la boîte.")

# Reusable feature blocks, keyed by the camera a pack actually ships.
FEAT_W503 = dict(img='feat_image_1', alt='Caméra extérieure autonome W503',
    eyebrow='VIDÉOSURVEILLANCE EXTÉRIEURE', h2="Un œil sur l'allée, sans tirer un seul câble.",
    text="La caméra W503 fonctionne sur batterie longue durée. Elle se fixe où vous voulez, même sans prise à proximité, et bascule en vision nocturne couleur grâce à son projecteur intégré.",
    bullets=['Full HD, vision nocturne couleur', '100 % sans fil, aucun raccordement électrique'])
FEAT_W503_SOLAR = dict(img='feat_image_1', alt='Caméras extérieures W503 et panneaux solaires SPW503',
    eyebrow='VIDÉOSURVEILLANCE EXTÉRIEURE', h2='Deux caméras que vous ne rechargerez jamais.',
    text="Chaque caméra W503 est livrée avec son panneau solaire SPW503 : l'alimentation est continue, sans câble à tirer ni batterie à descendre. Full HD, vision nocturne couleur, audio bidirectionnel, IP65.",
    bullets=['Panneau solaire SPW503 fourni pour chaque caméra', 'Audio bidirectionnel : vous parlez au visiteur depuis le téléphone'])
FEAT_W512 = dict(img='feat_image_1', alt='Caméra extérieure motorisée solaire W512MW',
    eyebrow='VIDÉOSURVEILLANCE EXTÉRIEURE', h2='Une caméra qui balaie, au lieu de fixer un angle.',
    text="La W512MW est motorisée : elle pivote pour couvrir toute une façade, une cour ou une allée depuis un seul point de fixation. Son panneau solaire la recharge en continu, donc aucun câble électrique. Full HD, vision nocturne, audio bidirectionnel.",
    bullets=['Motorisée : balayage panoramique depuis le téléphone',
             'Panneau solaire fourni : aucune recharge à prévoir',
             'Vision nocturne et audio bidirectionnel'])
FEAT_W512_SOLAR = dict(img='feat_image_1', alt='Caméras extérieures motorisées W512MW et panneaux solaires',
    eyebrow='VIDÉOSURVEILLANCE EXTÉRIEURE', h2='Deux caméras motorisées, alimentées par le soleil.',
    text="Les deux W512MW sont motorisées et livrées avec leur panneau solaire : elles balaient toute une façade et se rechargent seules. 3 MP, PTZ, vision nocturne couleur, audio bidirectionnel.",
    bullets=['3 MP, PTZ : balayage panoramique et zoom depuis le téléphone', 'Panneau solaire fourni : aucune recharge à prévoir'])
FEAT_W512_SOLAR_1 = dict(img='feat_image_1', alt='Caméras extérieures solaires W512MW',
    eyebrow='VIDÉOSURVEILLANCE EXTÉRIEURE', h2='Deux caméras motorisées, totalement autonomes.',
    text="Les deux W512MW sont motorisées et solaires : elles balaient toute une façade, une cour ou une allée, et se rechargent seules. Aucun câble, aucune prise à proximité.",
    bullets=['Motorisées : balayage panoramique depuis le téléphone', '100 % autonomes, rechargées par la lumière du jour'])

FEAT_INT = dict(img='feat_image_2', alt='Caméra intérieure motorisée IP506P en mode Vie Privée',
    eyebrow='VIDÉOSURVEILLANCE INTÉRIEURE', h2="Chez vous, l'objectif se referme physiquement.",
    text="La IP506P suit les mouvements sur 360° avec auto-tracking. Quand vous désarmez l'alarme en rentrant, l'objectif se rétracte mécaniquement — pas un simple voyant logiciel, un mouvement que vous voyez.",
    bullets=['Rotation 360° et auto-tracking', 'Mode Vie Privée mécanique'])

# Shopify Files asset, 1254x1254, alt "Application mobile Daewoo Home Connect".
APP_SHOT = ('https://cdn.shopify.com/s/files/1/0326/3132/4811/files/'
            'Application_Daewoo.webp?v=1787742289&amp;width=1000')

def feat_app(cams):
    return dict(img='feat_image_3', src=APP_SHOT, w=1254, h=1254,
        alt='Application mobile Daewoo Home Connect',
        eyebrow='UNE SEULE APPLICATION', h2='Un système, pas juste des accessoires.',
        text="Daewoo Home Connect pilote l'ensemble : armement et désarmement à distance, alertes, visualisation en direct des %s. Gratuite, sans abonnement, sur iOS et Android." % cams,
        bullets=['Mode Maison : ouvertures et vibrations actives, mouvement désactivé',
                 "Temporisation d'entrée et de sortie réglable",
                 "Alerte immédiate en cas d'arrachement d'un périphérique"])

CHIPS_BASE = [('zig', 'Zigbee 3.0'), ('eth', 'Port RJ45'), ('4g', '4G+ données'), ('', 'Batterie 10&nbsp;h')]

PACKS = [
  dict(
    key='pa570', sku='PA570', suffix='pa570',
    handle='daewoo-pack-alarme-maison-sans-fil-elite-zenguard-centrale-pa501z-kit-comprenant-13-accessoires-1-camera-autonome-exterieure-1-interieure',
    doc='Pack Alarme Maison sans Fil\n  Elite (Zenguard) PA570" (499,90 €, SKU PA570, templateSuffix "pa570")',
    sticky='Pack Élite PA570', schema='Pack Élite PA570', js_name='Pack Élite PA570',
    h1='Pack alarme Élite PA570 ZenGuard, centrale PA501Z',
    tagline='La seule centrale de la gamme qui reste pilotable quand la box tombe en panne.',
    sub="Centrale PA501Z multiprotocole — Ethernet, Wi-Fi, 4G+ et passerelle Zigbee 3.0 — accompagnée\n        de 13 accessoires dont 9 capteurs Zigbee, deux caméras et une sirène extérieure solaire.\n        Installation sans technicien, sans travaux, sans abonnement obligatoire.",
    summary='Le PA570 comprend une centrale Élite, deux caméras et treize accessoires, soit seize éléments au total.',
    chips=CHIPS_BASE + [('', "Jusqu'à 200 accessoires")],
    contents_lead="13 accessoires et deux caméras, pensés pour une maison avec beaucoup d'ouvertures vitrées.",
    contents=[
      ('1×',) + CENTRALE, ('1×',) + IP506P,
      ('1×', 'Caméra extérieure autonome W503', '100 % sans fil, batterie longue durée, Full HD, vision nocturne couleur avec projecteur intégré.'),
      ('1×',) + SIRENE,
      ('5×', "Contacteurs d'ouverture WDS502Z", 'Portes et fenêtres. Remontée instantanée, confirmée par la centrale.', 'zig'),
      ('4×', 'Détecteurs de vibration WVD502Z', "Baies vitrées et fenêtres : l'alarme part au premier choc, avant l'entrée.", 'zig'),
      ('1×', 'Détecteur de mouvement WPS501', 'Double faisceau infrarouge Pet Immune : ignore les animaux de moins de 12 kg.'),
      ('2×', 'Télécommandes 4 boutons WRC501', 'Armement, désarmement, mode nuit, et SOS par appui long de 3 secondes.'),
      ('—',) + FIXATIONS,
    ],
    zig2=('Neuf capteurs Zigbee dans la boîte',
          "5 contacteurs d'ouverture WDS502Z et 4 détecteurs de vibration WVD502Z, appairés à la centrale depuis l'application."),
    cam_ext='camera-daewoo-w503-autonome-haute-resolution-wifi-1080p', img1='w503-sans-fil',
    features=[FEAT_W503, FEAT_INT, feat_app('deux caméras')],
    band='Équipez votre maison avec le pack Élite PA570',
    total_base='Pack Élite PA570 seul. Ajoutez des accessoires ci-dessus pour compléter votre installation.',
    specs_lead="Tout ce qu'il faut savoir sur le Pack Élite PA570.",
    specs_cams='1 caméra intérieure motorisée IP506P (360°, auto-tracking, mode Vie Privée)&#10;1 caméra extérieure autonome W503 (Full HD, vision nocturne couleur)',
    specs_sensors="5 contacteurs d'ouverture WDS502Z&#10;4 détecteurs de vibration WVD502Z",
    final='Pack Élite PA570 ZenGuard — Zigbee 3.0 et triple connexion',
    ld="Pack alarme maison sans fil Élite PA570 ZenGuard : centrale PA501Z multiprotocole (Ethernet RJ45, Wi-Fi, 4G+, passerelle Zigbee 3.0), 13 accessoires dont 9 capteurs Zigbee, 2 caméras et une sirène extérieure solaire. Sans abonnement obligatoire.",
  ),
  dict(
    key='pa571', sku='PA571', suffix='pa571',
    handle='daewoo-pack-alarme-maison-sans-fil-elite-defense-centrale-pa501z-kit-comprenant-15-accessoires-2-cameras-autonomes-exterieure-1-interieur',
    doc='Pack Alarme Defense+ PA571"\n  (629,90 €, SKU PA571, templateSuffix "pa571")',
    sticky='Pack Élite PA571', schema='Pack Élite PA571', js_name='Pack Élite PA571',
    h1='Pack alarme Élite PA571 Defense+, centrale PA501Z',
    tagline='Trois caméras et onze capteurs Zigbee, pour couvrir le tour de la maison.',
    sub="Centrale PA501Z multiprotocole — Ethernet, Wi-Fi, 4G+ et passerelle Zigbee 3.0 — avec\n        deux caméras extérieures autonomes, une caméra intérieure motorisée, onze capteurs Zigbee\n        et une sirène extérieure solaire. Sans travaux, sans abonnement obligatoire.",
    summary='Le PA571 comprend une centrale Élite, trois caméras, onze capteurs Zigbee et une sirène extérieure solaire.',
    chips=CHIPS_BASE + [('', '3 caméras incluses')],
    contents_lead='Trois caméras et onze capteurs Zigbee, pour une maison avec plusieurs façades à couvrir.',
    contents=[
      ('1×',) + CENTRALE,
      ('2×', 'Caméras extérieures autonomes W503', '100 % sans fil, batterie longue durée, Full HD, vision nocturne couleur, audio bidirectionnel.'),
      ('1×',) + IP506P,
      ('1×',) + SIRENE,
      ('6×', "Contacteurs d'ouverture WDS502Z", 'Entrée, baies vitrées, fenêtres, accès secondaires et garage.', 'zig'),
      ('5×', 'Détecteurs de vibration WVD502Z', 'Baies vitrées et fenêtres : détection préventive, avant effraction.', 'zig'),
      ('1×', 'Détecteur de mouvement', 'Double faisceau infrarouge Pet Immune : ignore les animaux de moins de 12 kg.'),
      ('—',) + FIXATIONS,
    ],
    zig2=('Onze capteurs Zigbee dans la boîte',
          "6 contacteurs d'ouverture WDS502Z et 5 détecteurs de vibration WVD502Z, appairés à la centrale depuis l'application."),
    cam_ext='camera-daewoo-w503-autonome-haute-resolution-wifi-1080p', img1='w503-sans-fil',
    features=[FEAT_W503, FEAT_INT, feat_app('trois caméras')],
    band='Équipez votre maison avec le pack Élite PA571',
    total_base='Pack Élite PA571 seul. Ajoutez des accessoires ci-dessus pour compléter votre installation.',
    specs_lead="Tout ce qu'il faut savoir sur le Pack Élite PA571.",
    specs_cams='2 caméras extérieures autonomes W503 (Full HD, vision nocturne couleur, audio bidirectionnel)&#10;1 caméra intérieure motorisée IP506P (360°, auto-tracking, mode Vie Privée)',
    specs_sensors="6 contacteurs d'ouverture WDS502Z&#10;5 détecteurs de vibration WVD502Z&#10;1 détecteur de mouvement Pet Immune",
    final='Pack Élite PA571 Defense+ — trois caméras et triple connexion',
    ld="Pack alarme maison sans fil Élite PA571 Defense+ : centrale PA501Z multiprotocole (Ethernet RJ45, Wi-Fi, 4G+, passerelle Zigbee 3.0), 2 caméras extérieures autonomes W503, 1 caméra intérieure motorisée IP506P, 11 capteurs Zigbee et une sirène extérieure solaire. Sans abonnement obligatoire.",
  ),
  dict(
    key='pa572', sku='PA572', suffix='pa572',
    handle='daewoo-pack-alarme-maison-sans-fil-elite-horizon-centrale-pa501z-kit-xxl-18-accessoires-2-cameras-solaires-exterieures-1-interieure',
    doc='Pack Alarme Horizon+ PA572"\n  (699,90 €, SKU PA572, templateSuffix "pa572")',
    sticky='Pack Élite PA572', schema='Pack Élite PA572', js_name='Pack Élite PA572',
    h1='Pack alarme Élite PA572 Horizon+, centrale PA501Z',
    tagline='Kit XXL : treize capteurs Zigbee et deux caméras extérieures solaires.',
    sub="Centrale PA501Z multiprotocole — Ethernet, Wi-Fi, 4G+ et passerelle Zigbee 3.0 — avec\n        deux caméras extérieures et leurs panneaux solaires, une caméra intérieure motorisée,\n        treize capteurs Zigbee, un clavier déporté et une sirène extérieure solaire.",
    summary='Le PA572 comprend une centrale Élite, trois caméras, treize capteurs Zigbee, un clavier et deux télécommandes.',
    chips=CHIPS_BASE + [('', '2 caméras solaires'), ('', '13 capteurs Zigbee')],
    contents_lead='Un kit XXL, pensé pour les grandes maisons et les terrains avec plusieurs accès.',
    contents=[
      ('1×',) + CENTRALE,
      ('2×', 'Caméras extérieures autonomes W503', 'Full HD, vision nocturne couleur, audio bidirectionnel, IP65.'),
      ('2×', 'Panneaux solaires SPW503', 'Alimentation continue des caméras W503, sans câble à tirer.'),
      ('1×',) + IP506P,
      ('1×',) + SIRENE,
      ('7×', "Contacteurs d'ouverture WDS502Z", 'Portes et fenêtres. Remontée instantanée, confirmée par la centrale.', 'zig'),
      ('6×', 'Détecteurs de vibration WVD502Z', "Baies vitrées et fenêtres : l'alarme part au premier choc, avant l'entrée.", 'zig'),
      ('1×', 'Détecteur de mouvement WPS501', 'Double faisceau infrarouge Pet Immune : ignore les animaux de moins de 12 kg.'),
      ('1×', 'Clavier déporté sans fil WKE502Z', 'Armement et désarmement par code ou badge, sans passer par le téléphone.', 'zig'),
      ('2×', 'Télécommandes 4 boutons WRC501', 'Armement, désarmement, mode nuit, et SOS par appui long de 3 secondes.'),
      ('—',) + FIXATIONS,
    ],
    zig2=('Quatorze équipements Zigbee dans la boîte',
          "7 contacteurs WDS502Z, 6 détecteurs de vibration WVD502Z et le clavier WKE502Z, appairés à la centrale depuis l'application."),
    cam_ext='camera-daewoo-w503-autonome-haute-resolution-wifi-1080p', img1='w503-sans-fil',
    features=[FEAT_W503_SOLAR, FEAT_INT, feat_app('trois caméras')],
    band='Équipez votre maison avec le pack Élite PA572',
    total_base='Pack Élite PA572 seul. Ajoutez des accessoires ci-dessus pour compléter votre installation.',
    specs_lead="Tout ce qu'il faut savoir sur le Pack Élite PA572.",
    specs_cams='2 caméras extérieures autonomes W503 avec panneaux solaires SPW503 (Full HD, IP65)&#10;1 caméra intérieure motorisée IP506P (360°, auto-tracking, mode Vie Privée)',
    specs_sensors="7 contacteurs d'ouverture WDS502Z&#10;6 détecteurs de vibration WVD502Z&#10;1 clavier déporté WKE502Z",
    final='Pack Élite PA572 Horizon+ — kit XXL et caméras solaires',
    ld="Pack alarme maison sans fil Élite PA572 Horizon+ : centrale PA501Z multiprotocole (Ethernet RJ45, Wi-Fi, 4G+, passerelle Zigbee 3.0), 2 caméras extérieures W503 avec panneaux solaires, 1 caméra intérieure IP506P, 13 capteurs Zigbee, un clavier déporté et une sirène extérieure solaire. Sans abonnement obligatoire.",
  ),
  dict(
    key='pa573', sku='PA573', suffix='pa573',
    handle='daewoo-pack-alarme-maison-sans-fil-elite-harmonie-centrale-pa501z-kit-xxl-19-accessoires-1-camera-solaire-motorisee-1-interieure',
    doc='Pack Alarme Harmonie+ PA573"\n  (659,90 €, SKU PA573, templateSuffix "pa573")',
    sticky='Pack Élite PA573', schema='Pack Élite PA573', js_name='Pack Élite PA573',
    h1='Pack alarme Élite PA573 Harmonie+, centrale PA501Z',
    tagline='Une caméra extérieure motorisée solaire et treize capteurs Zigbee pour les grands volumes.',
    sub="Centrale PA501Z multiprotocole — Ethernet, Wi-Fi, 4G+ et passerelle Zigbee 3.0 — avec\n        une caméra extérieure motorisée solaire, une caméra intérieure motorisée, treize capteurs\n        Zigbee, deux détecteurs de mouvement et un clavier déporté.",
    summary='Le PA573 comprend une centrale Élite, une caméra extérieure solaire, une caméra intérieure, treize capteurs Zigbee et deux détecteurs de mouvement.',
    chips=CHIPS_BASE + [('', 'Caméra solaire'), ('', '2 caméras motorisées'), ('', '13 capteurs Zigbee')],
    contents_lead='Une caméra extérieure solaire, une caméra intérieure et une couverture renforcée, pour les grands volumes.',
    contents=[
      ('1×',) + CENTRALE,
      ('1×', 'Caméra extérieure motorisée W512MW', 'Panoramique, Full HD, vision nocturne, audio bidirectionnel.'),
      ('1×', 'Panneau solaire', 'Recharge la W512MW en continu : aucun câble électrique à tirer.'),
      ('1×',) + IP506P,
      ('1×',) + SIRENE,
      ('7×', "Contacteurs d'ouverture Zigbee", "Portes d'entrée, portes de service et garage.", 'zig'),
      ('6×', 'Détecteurs de vibration Zigbee', 'Baies vitrées et fenêtres : détection avant effraction.', 'zig'),
      ('2×', 'Détecteurs de mouvement Pet Immune', 'Grands volumes. Ignorent les animaux de moins de 12 kg.'),
      ('1×', 'Clavier déporté sans fil WKE502Z', 'Armement et désarmement par code confidentiel.', 'zig'),
      ('2×', 'Télécommandes 4 fonctions', 'Armement, désarmement, mode nuit, et SOS par appui long de 3 secondes.'),
      ('—',) + FIXATIONS,
    ],
    zig2=('Quatorze équipements Zigbee dans la boîte',
          "7 contacteurs d'ouverture, 6 détecteurs de vibration et le clavier WKE502Z, tous en Zigbee 3.0, appairés depuis l'application."),
    cam_ext='camera-w512mw-exterieure-rotative-1440p-avec-panneau-solaire', img1='w512mw-installation-maison',
    features=[FEAT_W512, FEAT_INT, feat_app('deux caméras motorisées')],
    band='Équipez votre maison avec le pack Élite PA573',
    total_base='Pack Élite PA573 seul. Ajoutez des accessoires ci-dessus pour compléter votre installation.',
    specs_lead="Tout ce qu'il faut savoir sur le Pack Élite PA573.",
    specs_cams='1 caméra extérieure motorisée solaire W512MW (panoramique, Full HD, vision nocturne)&#10;1 caméra intérieure motorisée IP506P (360°, auto-tracking, mode Vie Privée)',
    specs_sensors="7 contacteurs d'ouverture Zigbee&#10;6 détecteurs de vibration Zigbee&#10;1 clavier déporté WKE502Z&#10;2 détecteurs de mouvement Pet Immune",
    final='Pack Élite PA573 Harmonie+ — caméras motorisées et capteurs Zigbee',
    ld="Pack alarme maison sans fil Élite PA573 Harmonie+ : centrale PA501Z multiprotocole (Ethernet RJ45, Wi-Fi, 4G+, passerelle Zigbee 3.0), 1 caméra extérieure motorisée solaire W512MW, 1 caméra intérieure IP506P, 13 capteurs Zigbee, 2 détecteurs de mouvement et une sirène extérieure solaire. Sans abonnement obligatoire.",
  ),
  dict(
    key='pa574', sku='PA574', suffix='pa574',
    handle='daewoo-pack-alarme-maison-sans-fil-elite-tranquillite-centrale-pa501z-kit-xxl-20-accessoires-2-cameras-solaires-motorisees',
    doc='Pack Alarme Tranquillité+ PA574"\n  (789,90 €, SKU PA574, templateSuffix "pa574")',
    sticky='Pack Élite PA574', schema='Pack Élite PA574', js_name='Pack Élite PA574',
    h1='Pack alarme Élite PA574 Tranquillité+, centrale PA501Z',
    tagline='Le kit le plus complet : deux caméras motorisées solaires et quatorze capteurs Zigbee.',
    sub="Centrale PA501Z multiprotocole — Ethernet, Wi-Fi, 4G+ et passerelle Zigbee 3.0 — avec\n        deux caméras extérieures motorisées et leurs panneaux solaires, une caméra intérieure,\n        quatorze capteurs Zigbee, un clavier mural et une sirène extérieure solaire.",
    summary='Le PA574 comprend une centrale Élite, trois caméras dont deux motorisées solaires, et quatorze capteurs Zigbee.',
    chips=CHIPS_BASE + [('', '3 caméras motorisées'), ('', '14 capteurs Zigbee')],
    contents_lead='Le kit le plus complet de la gamme Élite, pour les grandes propriétés.',
    contents=[
      ('1×',) + CENTRALE,
      ('2×', 'Caméras extérieures motorisées W512MW', '3 MP, PTZ, vision nocturne couleur, audio bidirectionnel.'),
      ('2×', 'Panneaux solaires', 'Alimentation continue des caméras W512MW, sans câble à tirer.'),
      ('1×',) + IP506P,
      ('1×',) + SIRENE,
      ('8×', "Détecteurs d'ouverture WDS502Z", 'Portes, fenêtres et baies vitrées.', 'zig'),
      ('6×', 'Détecteurs de vibration WVD502Z', 'Baies vitrées et fenêtres : détection avant effraction.', 'zig'),
      ('2×', 'Détecteurs de mouvement WPS501', 'Double faisceau infrarouge Pet Immune : ignorent les animaux de moins de 12 kg.'),
      ('1×', 'Clavier mural sans fil WKE502Z', 'Armement et désarmement par code ou badge RFID.', 'zig'),
      ('2×', 'Télécommandes 4 boutons WRC501', 'Armement, désarmement, mode nuit, et SOS par appui long de 3 secondes.'),
      ('—',) + FIXATIONS,
    ],
    zig2=('Quinze équipements Zigbee dans la boîte',
          "8 détecteurs d'ouverture WDS502Z, 6 détecteurs de vibration WVD502Z et le clavier WKE502Z, appairés depuis l'application."),
    cam_ext='camera-w512mw-exterieure-rotative-1440p-avec-panneau-solaire', img1='w512mw-installation-maison',
    features=[FEAT_W512_SOLAR, FEAT_INT, feat_app('trois caméras')],
    band='Équipez votre maison avec le pack Élite PA574',
    total_base='Pack Élite PA574 seul. Ajoutez des accessoires ci-dessus pour compléter votre installation.',
    specs_lead="Tout ce qu'il faut savoir sur le Pack Élite PA574.",
    specs_cams='2 caméras extérieures motorisées W512MW avec panneaux solaires (3 MP, PTZ)&#10;1 caméra intérieure motorisée IP506P (360°, auto-tracking, mode Vie Privée)',
    specs_sensors="8 détecteurs d'ouverture WDS502Z&#10;6 détecteurs de vibration WVD502Z&#10;1 clavier mural WKE502Z&#10;2 détecteurs de mouvement WPS501",
    final='Pack Élite PA574 Tranquillité+ — le kit le plus complet',
    ld="Pack alarme maison sans fil Élite PA574 Tranquillité+ : centrale PA501Z multiprotocole (Ethernet RJ45, Wi-Fi, 4G+, passerelle Zigbee 3.0), 2 caméras extérieures motorisées W512MW avec panneaux solaires, 1 caméra intérieure IP506P, 14 capteurs Zigbee, un clavier mural et une sirène extérieure solaire. Sans abonnement obligatoire.",
  ),
  dict(
    key='eliteoffre1', sku='PA5012601-001', suffix='eliteoffre1',
    handle='offre-exclusive-pack-elite-compatible-animaux-sans-abonnement-copie',
    doc='OFFRE EXCLUSIVE | Pack ÉLITE PA501Z |\n  Double Caméra Solaire W512MW" (699,90 € au lieu de 1 068,90 €,\n  SKU PA5012601-001, templateSuffix "eliteoffre1")',
    sticky='Offre exclusive · Pack Élite', schema='Offre exclusive Élite', js_name='Pack Élite',
    h1='Offre exclusive — Pack Élite PA501Z, double caméra solaire W512MW',
    tagline='Deux caméras motorisées 100 % solaires, au prix de l\'offre limitée.',
    sub="Centrale PA501Z multiprotocole — Ethernet, Wi-Fi, 4G+ et passerelle Zigbee 3.0 — avec\n        deux caméras extérieures motorisées totalement autonomes, une caméra intérieure,\n        huit capteurs Zigbee, un détecteur de mouvement et une sirène extérieure solaire.",
    summary="Le pack comprend une centrale Élite, deux caméras solaires motorisées, une caméra intérieure, neuf capteurs et une sirène extérieure solaire.",
    chips=CHIPS_BASE + [('', '3 caméras'), ('', 'Offre limitée')],
    contents_lead='Trois caméras et une protection périmétrique complète, en offre limitée.',
    contents=[
      ('1×',) + CENTRALE,
      ('2×', 'Caméras extérieures solaires W512MW', 'Motorisées et totalement autonomes : aucun câble, aucune prise à proximité.'),
      ('1×', 'Caméra intérieure motorisée IP506P', "Rotation 360° avec auto-tracking et mode Vie Privée : l'objectif se referme mécaniquement."),
      ('1×',) + SIRENE,
      ('4×', "Contacteurs d'ouverture WDS502Z", 'Portes et fenêtres. Remontée instantanée, confirmée par la centrale.', 'zig'),
      ('4×', 'Détecteurs de vibration WVD502Z', "Baies vitrées et fenêtres : l'alarme part au premier choc, avant l'entrée.", 'zig'),
      ('1×', 'Détecteur de mouvement WPS501', 'Double faisceau infrarouge Pet Immune : ignore les animaux de moins de 12 kg.'),
      ('2×', 'Télécommandes 4 boutons WRC501', 'Armement et désarmement sans sortir le téléphone.'),
      ('—',) + FIXATIONS,
    ],
    zig2=('Huit capteurs Zigbee dans la boîte',
          "4 contacteurs WDS502Z et 4 détecteurs de vibration WVD502Z, appairés à la centrale depuis l'application."),
    cam_ext='camera-w512mw-exterieure-rotative-1440p-avec-panneau-solaire', img1='w512mw-installation-maison',
    features=[FEAT_W512_SOLAR_1, feat_app('caméras'), FEAT_INT],
    band='Profitez de l\'offre exclusive sur le pack Élite',
    total_base="Pack Élite en offre exclusive. Ajoutez des accessoires ci-dessus pour compléter votre installation.",
    specs_lead="Tout ce qu'il faut savoir sur cette offre exclusive.",
    specs_cams='2 caméras extérieures motorisées solaires W512MW (vision nocturne couleur, audio bidirectionnel)&#10;1 caméra intérieure motorisée IP506P (360°, auto-tracking, mode Vie Privée)',
    specs_sensors='4 contacteurs WDS502Z&#10;4 détecteurs de vibration WVD502Z&#10;1 détecteur de mouvement WPS501',
    final='Offre exclusive — Pack Élite PA501Z et double caméra solaire',
    ld="Offre exclusive sur le pack alarme maison sans fil Élite PA501Z : centrale multiprotocole (Ethernet RJ45, Wi-Fi, 4G+, passerelle Zigbee 3.0), 2 caméras extérieures motorisées solaires W512MW, 1 caméra intérieure IP506P, 8 capteurs Zigbee, un détecteur de mouvement et une sirène extérieure solaire. Sans abonnement obligatoire.",
  ),
  dict(
    key='starter', sku='PA501ZSTARTER', suffix='starterelite',
    handle='starter-pack-elite-daewoo',
    doc='Starter pack Élite PA501Z Wifi / GSM 4G+ Livrée avec\n  5 Accessoires" (299,90 €, SKU PA501ZSTARTER, templateSuffix "starterelite").\n\n  Seul pack de la gamme sans caméra ni sirène : la ligne "flux vidéo" de la\n  matrice, les deux blocs caméra et la question 2 de la FAQ sont remplacés,\n  et le renvoi latéral pointe vers le PA570 au lieu du Starter lui-même.',
    sticky='Starter Pack Élite', schema='Starter Pack Élite', js_name='Starter Pack Élite',
    h1='Starter Pack Élite PA501Z, la centrale et de quoi commencer',
    tagline='La même centrale que les packs complets, avec cinq accessoires pour démarrer.',
    sub="Centrale PA501Z multiprotocole — Ethernet, Wi-Fi, 4G+ et passerelle Zigbee 3.0 — avec\n        deux contacteurs d'ouverture Zigbee, un détecteur de mouvement compatible animaux\n        et deux télécommandes. Tout le reste s'ajoute quand vous le décidez.",
    summary='Le Starter Pack comprend la centrale Élite et cinq accessoires, soit six éléments au total.',
    chips=CHIPS_BASE + [('', '5 accessoires'), ("", "Jusqu'à 200 accessoires")],
    contents_lead="L'essentiel pour protéger une entrée et une pièce de passage, sur la centrale la plus complète de la gamme.",
    contents=[
      ('1×',) + CENTRALE,
      ('2×', "Contacteurs d'ouverture WDS502Z", 'Porte d\'entrée et fenêtre. Remontée instantanée, confirmée par la centrale.', 'zig'),
      ('1×', 'Détecteur de mouvement WPS501', 'Double faisceau infrarouge Pet Immune : ignore les animaux de moins de 12 kg.'),
      ('2×', 'Télécommandes 4 boutons WRC501', 'Armement, désarmement, mode nuit, et SOS par appui long de 3 secondes.'),
      ('—',) + FIXATIONS,
    ],
    zig2=('Deux capteurs Zigbee dans la boîte',
          "Les 2 contacteurs WDS502Z sont appairés depuis l'application. Le reste de la gamme Zigbee s'ajoute ensuite, sans rien remplacer."),
    cam_ext='', img1='',
    feat_images="""  # Ce pack n'embarque aucune caméra : les visuels des blocs viennent de la
  # centrale elle-même, prise sur sa propre fiche pour disposer des vues de
  # détail que la galerie du pack ne porte pas toujours.
  assign pa501 = all_products['strong-centrale-dalarme-strong-elite']
  assign feat_image_1 = pa501.featured_image | default: hero_image
  for img in pa501.images
    if img.src contains 'elite-lifestyle'
      assign feat_image_1 = img
    endif
  endfor

  assign feat_image_2 = pa501.featured_image | default: hero_image
  for img in pa501.images
    if img.src contains 'elite-vue-arriere'
      assign feat_image_2 = img
    endif
  endfor
""",
    matrix_cam_row='',
    matrix_lead='Trois situations, quatre fonctions. Sans rien enjoliver.',
    matrix_foot_cam="<strong>Et les caméras, si vous en ajoutez ?</strong> Elles passent uniquement par le Wi-Fi. Aucune carte SIM ne rend leur flux vidéo accessible pendant une coupure : c'est vrai sur l'Élite comme sur le reste de la gamme.",
    faq2=('Puis-je ajouter des caméras à ce pack ?',
          "Oui. La centrale PA501Z pilote la caméra intérieure IP506P et les caméras extérieures W503 et W512MW, qui s'ajoutent quand vous le souhaitez. À savoir avant d'acheter : les caméras passent uniquement par le Wi-Fi. Si votre box est coupée, leur flux vidéo n'est plus accessible, même avec une carte SIM installée — c'est vrai sur toute la gamme."),
    xsell=dict(
      handle='daewoo-pack-alarme-maison-sans-fil-elite-zenguard-centrale-pa501z-kit-comprenant-13-accessoires-1-camera-autonome-exterieure-1-interieure',
      lead='Comparez les packs Élite, ou passez directement à un pack avec caméras.',
      alt='Le Pack Élite PA570 ZenGuard',
      title='Besoin de caméras ? Le Pack PA570',
      text='La même centrale, avec 13 accessoires, une caméra extérieure autonome et une caméra intérieure.',
      btn='Voir le Pack PA570'),
    features=[
      dict(img='feat_image_1', alt="Centrale d'alarme Élite PA501Z installée dans une maison",
        eyebrow='LA CENTRALE', h2="C'est la pièce qu'on n'achète qu'une fois.",
        text="Le Starter Pack embarque exactement la même centrale que les packs à 500 ou 800 €. Les capteurs, les caméras et les sirènes s'ajoutent ensuite, un par un, sans jamais racheter le cerveau du système.",
        bullets=['Identique à celle des packs PA570 à PA574',
                 "Jusqu'à 200 accessoires ajoutables",
                 'Compatible gamme SA501, hors WDS501, WVD501 et WKE501']),
      dict(img='feat_image_2', alt='Vue arrière de la centrale PA501Z, port Ethernet et emplacement carte SIM',
        eyebrow='CONNECTIQUE', h2='Une prise réseau, et un emplacement pour la SIM.',
        text="Au dos du boîtier : un port Ethernet RJ45 pour une liaison câblée insensible au Wi-Fi saturé du voisinage, et un emplacement de carte SIM pour la 4G+ en secours. La carte reste optionnelle.",
        bullets=['Port RJ45 prioritaire, Wi-Fi 2,4 GHz en relais',
                 'Emplacement SIM pour la 4G+ de secours',
                 'Batterie de secours 10 h intégrée']),
      dict(img='feat_image_3', src=APP_SHOT, w=1254, h=1254,
        alt='Application mobile Daewoo Home Connect',
        eyebrow='UNE SEULE APPLICATION', h2='Un système, pas juste des accessoires.',
        text="Daewoo Home Connect pilote l'ensemble : armement et désarmement à distance, alertes, et la vidéo des caméras que vous ajouterez. Gratuite, sans abonnement, sur iOS et Android.",
        bullets=['Mode Maison : ouvertures actives, mouvement désactivé',
                 "Temporisation d'entrée et de sortie réglable",
                 "Alerte immédiate en cas d'arrachement d'un périphérique"]),
    ],
    band='Commencez avec le Starter Pack Élite',
    total_base='Starter Pack Élite seul. Ajoutez des accessoires ci-dessus pour couvrir plus de pièces.',
    specs_lead="Tout ce qu'il faut savoir sur le Starter Pack Élite.",
    specs_power='Centrale : secteur + batterie de secours 10 h&#10;Sirène intégrée à la centrale',
    specs_cams="Aucune caméra dans ce pack&#10;Compatibles en option : IP506P (intérieure), W503 et W512MW (extérieures)",
    specs_sensors="2 contacteurs d'ouverture WDS502Z&#10;1 détecteur de mouvement WPS501&#10;2 télécommandes 4 boutons WRC501",
    final='Starter Pack Élite PA501Z — la centrale et cinq accessoires',
    ld="Starter Pack alarme maison sans fil Élite PA501Z : centrale multiprotocole (Ethernet RJ45, Wi-Fi, 4G+, passerelle Zigbee 3.0), 2 contacteurs d'ouverture Zigbee WDS502Z, 1 détecteur de mouvement WPS501 compatible animaux et 2 télécommandes WRC501. Évolutif jusqu'à 200 accessoires, sans abonnement obligatoire.",
  ),
]
