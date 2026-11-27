# Boîte DAEWOO EF503 — caméra extérieure PoE

Habillage Daewoo posé sur le gabarit du fabricant (boîte TS58, **228 × 149 × 93 mm**, carton 300 g blanc + W9 renforcé, pelliculage mat, quadri).

## Fichiers

| Fichier | Usage |
|---|---|
| `EF503_BAT_avec_gabarit.pdf` | BAT à envoyer à l'usine : visuel + tracé de découpe (magenta), languette de suspension (cyan pointillé), légendes des faces |
| `EF503_impression_RVB.pdf` | Fichier d'impression vectoriel, fond perdu 3 mm, sans tracé de découpe |
| `EF503_impression_CMJN.pdf` | Même fichier converti automatiquement en CMJN (noir riche ≈ C72 M68 Y67 K88) — à faire valider par l'imprimeur |
| `EF503_maquette_3D_avant.jpg` / `_arriere.jpg` | Rendus 3D de la boîte fermée |
| `EF503_a_plat_avec_gabarit.png` | Aperçu à plat |
| `EF503_face_principale.png` | Face principale seule (visuel pour la fiche produit ou les réseaux sociaux) |

## Répartition des faces

- **Couvercle (face principale)** : logo, EF503, visuel produit, arguments PoE / 1080p / Métal, « Sans abonnement », pictos.
- **Face avant** : explication du PoE (un seul câble pour l'image et l'alimentation) avec un schéma.
- **Côté droit** : application Daewoo Home Connect (QR code, badges stores) et engagements de la marque.
- **Dos** : caractéristiques en 4 langues, mentions légales, importateur (nouvelle adresse), EAN 3760285866513, logos réglementaires, encart blanc pour l'étiquette usine.
- **Côté gauche** : fiche technique détaillée FR/EN.
- **Rabat intérieur** (visible à l'ouverture, imprimé tête-bêche) : message de bienvenue et 3 étapes d'installation.

## Points à valider avant impression

1. **PoE et structure métallique** n'apparaissent pas dans la fiche CS58-Y, qui n'indique qu'une alimentation DC 12 V et ne précise pas la matière du boîtier : à confirmer avec le fournisseur.
2. **Résolution** : la fiche donne 2 MP natifs (le 3 MP est interpolé). La boîte indique donc « Full HD 1080p · 2 MP ».
3. **QR code** : c'est le même lien que sur la boîte IP506P (`a.smart321.com/kodaksmartlife`). Vérifier qu'il ouvre bien Daewoo Home Connect, et que l'EF503 est compatible avec cette application.
4. **Adresse** : 15 Allée James Watt, Immeuble 2000 Watt, 33700 Mérignac (adresse tirée de la page retours du site). L'adresse de la boutique dans l'admin Shopify est encore l'ancienne.
5. **Étiquette usine** : le gabarit prévoit des repères d'étiquette sur le côté gauche. Une zone blanche a été prévue au dos, à côté de l'EAN, comme sur l'IP506P.
6. **Sens du couvercle** : il se lit depuis la face avant, alors que le fabricant l'avait imprimé dans l'autre sens. À vérifier sur une maquette blanche à cause de la languette de suspension.
7. Mentions légales reprises de l'IP506P, avec seulement les fautes de frappe corrigées et le © passé à 2026. Le logo Triman et l'Info-tri, obligatoires en France, sont à vérifier avec votre éco-organisme.

## Régénérer les fichiers

Depuis `source/build/` (Python 3 avec Pillow, Node avec Playwright, Ghostscript pour le CMJN) :

```bash
python3 make.py print box_print.html && python3 make.py proof box_proof.html
node render.js box_print.html EF503_print pdf 3
node render.js box_proof.html EF503_proof pdf 1
gs -q -dSAFER -dBATCH -dNOPAUSE -sDEVICE=pdfwrite -sColorConversionStrategy=CMYK -sProcessColorModel=DeviceCMYK -dCompatibilityLevel=1.6 -sOutputFile=EF503_print_CMYK.pdf EF503_print.pdf
```

Tous les textes et toutes les positions (en mm) se trouvent dans `make.py`. Les éclairages de fond sont générés par `bg_raster.py`, qui nécessite numpy.
