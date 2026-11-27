# Offre Ultime (27/11/2026)

Pack Ultime = contenu du Pack Vision Duo + sirène intérieure WIS305, prix net
(sans bon d'achat), jusqu'au mardi 1er décembre 2026 à 9h.

- Produit : `pack-alarme-ultime` (gid://shopify/Product/16027863155028),
  étiquette `pack-ult` (pas de `pack-xxx` de la gamme : pas de bon d'achat),
  modèle `product.pack-ultime`.
- Variantes : PK-ULT-VIG 399,90 € (prix barré 601,60), PK-ULT-VIGP 449,90 €
  (641,60), PK-ULT-AM301 499,90 € (683,20), PK-ULT-AM302 549,90 € (715,50).
  Prix barré = même équipement dans le configurateur avec sa remise
  habituelle (métachamp de variante `custom.prix_reference`).
- Stock : 25 / 20 / 15 / 15 (75 packs, limité par 78 sirènes WIS305).
- Images : `images/ultime-*.jpg` (photo Vision Duo + sirène intérieure +
  pastille « Offre Ultime »), une par centrale.
- Thème « Offre Ultime 27112026 (Claude) » (210124734804), depuis « Rupture
  W512MW v2 » :
  - `sections/pack-gamme.liquid` : étiquette `pack-ult` reconnue, blocs
    `when 'ult'` (textes, contenu, FAQ ; accent noir et jaune, signature
    « Offre Ultime »).
  - `templates/product.pack-ultime.json` : copie de `product.pack-gamme`
    sans la section du bon d'achat, sans vidéos.
  - `sections/bf-collection.liquid` : pas de pastille de carte pour
    `pack-ult` (la pastille est sur le visuel).
  - `templates/index.json` : carrousel Black Friday de l'accueil = Ultime,
    Sécurité Intégrale, Vision Duo Solaire (Touch XL série précédente et
    Vigilia Sécurité Renforcée retirés).
- Collection Black Friday (manuelle, source
  gid://shopify/CollectionConditionsSource/50645827924) : à la publication,
  retirer 12472652693844 (Touch XL série précédente) et 12454111314260
  (Vigilia Sécurité Renforcée), ajouter l'Ultime en position 0.
- Fin de l'offre (mardi 1er décembre 9h) : passer le produit en brouillon
  ou le retirer de la collection et du carrousel.

## Ajouts du 27/11 (suite)

- Phrase « pk_plus » de l'Ultime retirée. À la place : option « panneau
  solaire SPW503, 49,90 € pièce » avec compteur (`snippets/pk-option-solaire.liquid`),
  déplacée par script juste au-dessus du bouton d'achat du haut. Elle pilote
  le compteur SPW503 du bloc « Complétez votre pack » (pv-accessoires), qui
  gère le total et la mise au panier (pack + panneaux en un clic).
- `snippets/pv-accessoires.liquid` : pour l'étiquette `pack-ult`, liste
  dédiée SPW503, WDV301, WPS305, WRC305 (le contacteur de garage est retiré :
  la page dépassait la limite de consultations `all_products` de Shopify et
  affichait un doublon).
- Page Black Friday : encart « Offre Ultime » sous l'en-tête
  (`snippets/bf-ultime-encart.liquid`, rendu dans `bf-collection`), prix et
  prix barré lus sur le produit, compte à rebours, disparaît mardi 1er
  décembre à 9h.
- Collection Black Friday : Touch XL série précédente et Vigilia Sécurité
  Renforcée retirés le 27/11 (fiches toujours en vente). L'Ultime sera ajouté
  en tête à la publication du thème.
- Fiche Franck : option panneaux solaires ajoutée.

## Référencement Lalog (27/11)

- `Referencement_Lalog_Pack_Ultime_2711.csv` : 4 références PK-ULT-*, même
  format que le fichier Lalog des 6 packs (point-virgule, sans en-tête, CRLF).
  Contenu = celui du Vision Duo (PK-VDU-*) + sirène intérieure WIS305
  (3760285866322). Sirène solaire = WOS305 (3760285864328) + SPWOS305
  (3760285864335).
- EAN 3760285864717 (panneau solaire SPW503 de la caméra W503, confirmé par le
  dirigeant) ajouté dans Shopify sur SPW503 et SPW503C.
