# Accessoires Élite / Key — passage au design premium

Date : 02/09/2026 · Boutique daewoo-security.fr

Suite de l'uniformisation faite sur la gamme Vigilia / Touch. Aucune
section ni aucun template n'a été créé : `product.acc-premium.json` et les
sections `acc-*` étaient déjà présents dans le thème publié
**Home conversion 02092026 (Claude)** (`202778476884`). Le travail est donc
essentiellement de la donnée produit, qui est **déjà en ligne**.

## 1. Correctif thème (à publier)

Thème dupliqué : **Accessoires Elite Key 02092026 (Claude)** —
`gid://shopify/OnlineStoreTheme/202807476564`.

Un seul fichier modifié : `sections/acc-hero.liquid` (8 317 o, contre 8 010).

Motif : le titre de l'en-tête est construit comme
`marque + type de produit + référence`, et la référence venait du SKU.
Les SKU Vigilia / Touch sont propres (`WVD301`), ceux des gammes Élite et
Key sont préfixés (`DAWVD501`, `DAWDS501`, `DASTIC10`) et s'affichaient tels
quels dans le H1.

Nouvel ordre de priorité pour la référence :

1. le réglage `reference` de la section (déjà utilisé par les fiches SIM) ;
2. `product.metafields.custom.bandeau_caracteristiques.value.titre_1` ;
3. le SKU.

Le champ `titre_1` du bandeau n'est pas affiché par `acc-fiche-technique`
(vérifié) : il sert uniquement de nom de produit. Sur les fiches Vigilia /
Touch déjà en place, `titre_1` vaut exactement le SKU (`WVD301` = `WVD301`),
donc **aucune de ces pages ne change**.

Tant que le thème n'est pas publié, les fiches Élite / Key affichent
« Daewoo Détecteur de vibration DAWVD501 » au lieu de
« Daewoo Détecteur de vibration WVD501 ». Rien n'est cassé, seul le libellé
est moins propre.

## 2. Produits passés en `acc-premium`

17 accessoires + le canon à fumée + les autocollants. Pour chacun :
`titre_page`, `accroche`, `note_compatibilite`, `conseil_quantite`, un
métaobjet `bandeau_caracteristiques`, un `productType` propre, les `alt`
d'images manquants, et `templateSuffix = acc-premium`.

| Produit | ID | Ancien suffixe | Ajouts spécifiques |
|---|---|---|---|
| Contacteur de porte WDS501 | 4665250349195 | accessoires | FAQ, categorie_de_produit |
| Détecteur mouvement animaux WPS501 | 4665329483915 | accessoires | — |
| Télécommande WRC501 | 4665429393547 | accessoires-sans-details | — |
| Sirène int/ext WOS501 | 4665442041995 | accessoires | FAQ |
| Sirène ext solaire WOS501S | 4670908465291 | accessoires | — |
| Détecteur de fumée WSD501 | 5600764625049 | accessoires | — |
| Détecteur de vibration WVD501 | 5600837861529 | accessoires | FAQ, categorie_de_produit |
| Badge RFID WRF501 | 5600843563161 | accessoires-sans-details | — |
| Mouvement extérieur WMO501 | 6044640149657 | accessoires | — |
| Fuite d'eau WWF501 | 6659267395737 | accessoires | — |
| Clavier WKE501 | 6729245196441 | accessoires | FAQ, categorie_de_produit |
| Contacteur garage WDG501 | 7479262511317 | accessoires | — |
| Contacteur Zigbee WDS502Z | 7937744011477 | accessoires-sans-details | — |
| Vibration Zigbee WVD502Z | 7937745125589 | accessoires | securite_detection, connectivite |
| Clavier Zigbee WKE502Z | 7937746927829 | accessoires | securite_detection, connectivite |
| Sirène intérieure WIS502 | 7975041433813 | accessoires | FAQ |
| Amplificateur Zigbee EXT501 | 11974636667220 | ext501zig | a_quoi_ca_sert, contenu_du_pack, connectivite, alimentation |
| Canon à fumée F502W | 8521990766932 | accesoires-sans-videos | option_associee → recharge F502R |
| Autocollants x10 | 6001578311833 | autocollants-x10 | a_quoi_ca_sert, FAQ, contenu_du_pack |

`acc-premium` et `acc-premium-sd` sont **strictement identiques** (même
octet près) : un seul suffixe suffit, `acc-premium` a donc été utilisé
partout.

## 3. Autocollants dans toutes les gammes

Problème : « Compatible gamme Vigilia / Touch » et « Compatible gamme
Élite » sont des collections **automatisées** dont la règle était
`categorie_de_produit = Accessoires` **ET** `compatibilite = <gamme>`.
Le métachamp `compatibilite` est une référence unique : un produit
« Toutes les gammes » ne peut donc appartenir à aucune des deux, et un
produit ne peut pas être ajouté manuellement à une collection automatisée.

Solution retenue : remplacer la seconde règle par un tag.

| Collection | Nouvelle règle (ET) | Effectif avant → après |
|---|---|---|
| Compatible gamme Vigilia / Touch (685200703828) | categorie = Accessoires + tag `gamme_vigilia_touch` | 28 → 29 |
| Compatible gamme Élite (685200802132) | categorie = Accessoires + tag `gamme_elite` | 16 → 17 |

Les 28 et 16 membres d'origine ont été tagués un par un avant le
changement de règle ; la composition a été revérifiée après recalcul :
**identique, plus les autocollants**.

**À retenir pour la suite** : un nouvel accessoire n'entre plus dans ces
collections par son métachamp `compatibilite` mais par son tag
`gamme_vigilia_touch` / `gamme_elite`. Le métachamp reste utilisé pour le
badge « Compatible … » de l'en-tête.

« Compatible toutes gammes » n'a pas été touchée (les autocollants y
étaient déjà).

Placements validés le 02/09 :

| Produit | Vigilia / Touch | Élite | Key (collection manuelle) |
|---|---|---|---|
| Autocollants x10 | oui | oui | oui |
| Carte SIM 1 mois | oui | non | oui |
| Carte SIM 1 an Vigilia/Touch | oui | non | oui |
| Carte SIM 1 an Élite | non | oui | non |

Le canon à fumée reste dans ses collections actuelles (Accessoires Key,
Maison connectée, Tous les accessoires, Compatible toutes gammes, Spécial
SA501 4G, Dissuasion) : il n'a pas été ajouté aux deux collections de
gamme.

## 4. Points restants

- **Images non retravaillées** : WOS501 (4665442041995) et WIS502
  (7975041433813) sont encore en `.jpg` / `.png`. Produits arrêtés, laissés
  en l'état sur décision du 02/09.
- **Volume du canon à fumée** : tranché le 02/09, l'appareil est donné pour
  **100 à 150 m³**. Corrigé dans le bandeau caractéristiques, le conseil de
  quantité, la description produit et le métaobjet
  `caracteristiques_principales`.
- **Adaptateur secteur Key** (7978957701333) laissé sur son gabarit
  `sa501` : pièce détachée sans contenu, hors périmètre accessoires.
- Le WKE501 et le WKE502Z partagent deux visuels ; leurs `alt` ont été
  écrits sans référence produit pour rester justes sur les deux fiches.
  Idem pour les visuels WWF301 / WDG301 réutilisés sur les fiches 501.
