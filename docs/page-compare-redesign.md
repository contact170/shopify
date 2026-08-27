# Refonte de la page comparatif — /pages/product-compare

Thème d'aperçu : **« Page comparatif alarmes (Claude) »** — `202266378580`
Aperçu : https://daewoo-security.fr/pages/product-compare?preview_theme_id=202266378580

Ce thème est une **duplication du thème Élite `202210017620`**. Il contient donc
les trois refontes : Touch/Touch XL, Élite et le comparatif. Si vous publiez
plusieurs thèmes, **celui-ci doit être publié en dernier**.

## Ce qui remplace l'existant

L'ancienne page utilisait la section native `product-comparison` du thème,
alimentée par trois blocs produit. Elle présentait plusieurs défauts :

- des en-têtes de groupe restés en anglais et non traduits — « #### Battery »,
  « #### Sound », « #### Customizable Sound EQ », et une valeur « TRUE » ;
- des lignes **désalignées** entre les trois colonnes : la ligne 14 portait un
  libellé sur la Touch et rien sur la Vigilia, la ligne 19 répétait « Type de
  logement conseillé » comme libellé *et* comme valeur sur l'Élite ;
- des données fausses ou périmées : télécommandes « WRC301 » au lieu de WRC501
  dans le kit Élite, sirène Élite à « 95-100 dB », « radio Daewoo » ;
- aucune hiérarchie : 23 lignes de même poids, sans indication de ce qui
  différencie réellement les gammes.

La nouvelle page est composée de six sections Liquid maison, sur le modèle des
pages Touch et Élite.

## Structure

1. **Intro** (`cp-intro`) — fond sombre, les trois gammes et leur prix d'entrée.
2. **Le choix en 30 secondes** (`cp-orienteur`) — trois situations formulées à la
   première personne, chacune renvoyant vers une gamme. Le raccourci pour le
   client qui ne veut pas lire le tableau.
3. **Les trois gammes** (`cp-gammes`) — cartes produit de hauteur égale : visuel,
   positionnement, 3 points forts + 1 limite assumée, prix, deux CTA.
4. **Le tableau** (`cp-tableau`) — 21 lignes réparties en 5 groupes, en-tête
   collante au défilement. **6 lignes sont marquées « sur les trois gammes »** et
   occupent toute la largeur : on ne compare que ce qui diffère. Les avantages
   exclusifs à une gamme portent un badge « Seule à le faire ».
5. **Trois différences** (`cp-differences`) — l'écran, le comportement en coupure
   Internet, et l'arbitrage assistant vocal / passerelle Zigbee. Chaque bloc se
   termine par une recommandation.
6. **CTA** (`cp-cta`) — configurateur et contact.

## Code couleur

Chaque gamme garde la même couleur sur toute la page, reprise de sa page de
destination :

| Gamme | Accent | Texte accentué |
|---|---|---|
| Vigilia | `#e0912b` | `#a35a00` |
| Touch & Touch XL | `#2f6fe0` | `#1f5fd0` |
| Élite | `#12a0ad` | `#0a6068` |

La couleur n'est jamais le seul porteur d'information : chaque colonne est aussi
nommée, et en mobile chaque valeur porte l'étiquette de sa gamme.

## Mobile

En dessous de 900 px l'en-tête du tableau disparaît et chaque ligne devient un
bloc : le libellé, puis les trois valeurs, chacune précédée du nom de sa gamme et
de sa pastille de couleur. Aucun défilement horizontal.

## Sources des données

- **Vigilia** — sections de la page `/collections/systeme-dalarme-vigilia`
  (packs, FAQ détails produit, FAQ générale) et fiche du starter pack.
- **Touch / Touch XL** — fiche technique de la refonte Touch (`tc-specs`).
- **Élite** — fiche technique de la refonte Élite (`el-specs`), après les
  corrections validées par le client.
- **Prix** — API Shopify, prix minimum des trois kits de départ au 27/08/2026 :
  139,90 € / 199,90 € / 299,90 €.

## Points de vigilance factuels

- **Nombre d'accessoires Vigilia : 60 ou 90 ?** La FAQ « Détails produit » de la
  page Vigilia annonce **60**, le bloc « Pourquoi choisir la gamme Vigilia »
  annonce **90**, et l'ancien comparatif annonçait **60**. Le tableau retient
  **60** — à trancher, sachant que 90 est aussi la valeur de la Touch et
  ressemble à un copier-coller.
- **Durée de retour : 14 ou 30 jours ?** Les pages Touch et Élite annoncent
  14 jours, la page Vigilia 30 jours. Le comparatif écrit donc « retour gratuit »
  **sans durée**, pour ne pas afficher une contradiction. À harmoniser.
- **Sirène Touch : 90 dB.** La fiche AM353 annonce 90 dB là où la refonte Touch
  retient 95 dB pour la Touch XL. Le tableau reprend 90 dB / 95 dB XL.
- **Batterie Vigilia ≈ 4 h**, d'après la FAQ de la page Vigilia.
- **Comportement en coupure Internet** : seule l'Élite garde l'application active
  en 4G+. La Touch, avec une carte SIM, envoie des SMS et se pilote par SMS. La
  Vigilia n'a de module GSM que sur la version correspondante. Ne pas simplifier
  ces trois cas en un seul.
- **Les caméras ne sont jamais consultables** pendant une coupure Internet, quelle
  que soit la gamme, **même avec une carte SIM** dans la centrale.
- **Zigbee** : seules trois références Daewoo (WDS502Z, WVD502Z, WKE502Z) passent
  en Zigbee, et la compatibilité avec les accessoires Zigbee 3.0 / Tuya tiers
  n'est pas garantie.

## Modifier la page

```bash
# éditer les sections
$EDITOR theme-src/page-compare/*.liquid

# régénérer sections/cp-*.liquid et templates/page.compare.json
python3 theme-src/build-page-compare.py
```

Puis déployer les fichiers modifiés sur le thème d'aperçu via `themeFilesUpsert`
et vérifier le `checksumMd5` renvoyé contre le `md5sum` local.
