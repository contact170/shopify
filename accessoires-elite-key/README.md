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
| Canon à fumée F502W | 8521990766932 | accesoires-sans-videos | option_associee → recharge F502R, cartouche fournie |
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
- **Cartouche du canon à fumée** : l'appareil est livré avec une cartouche.
  Précisé dans le contenu du pack, le conseil de quantité, la description
  produit et une question de FAQ supplémentaire, pour que la recharge
  F502R proposée en option ne soit pas prise pour un complément
  indispensable à l'achat.
- **Adaptateur secteur Key** (7978957701333) laissé sur son gabarit
  `sa501` : pièce détachée sans contenu, hors périmètre accessoires.
- Le WKE501 et le WKE502Z partagent deux visuels ; leurs `alt` ont été
  écrits sans référence produit pour rester justes sur les deux fiches.
  Idem pour les visuels WWF301 / WDG301 réutilisés sur les fiches 501.

## 5. Centrale Key (SA501) 4G — migration 2G

Produit : **Centrale Key (SA501) 4G — vendue sans adaptateur secteur**
(`15051542659412`, handle `starter-pack-key-sa501-4g`, SKU `SA5014GS`,
99,90 €). Passée de `pack-par-defaut` à `acc-premium`.

Cette fiche n'a qu'un seul cas de vente : un client qui possède déjà une
SA501 de première génération et qui utilise, ou veut utiliser, une carte
SIM. Toute la page est écrite autour de ça.

- **Sous-titre** « Pour remplacer une SA501 2G. » et accroche qui pose
  d'emblée la condition : sans carte SIM, rien à changer.
- **Conseil sous le prix** : le test « suis-je concerné ? » avant l'achat.
- **Son rôle (acc-chrono)** : les trois étapes de la migration — vérifier,
  remplacer la centrale seule, réassocier les accessoires.
- **Compatibilité (acc-compat)** : tous les accessoires Key restent
  compatibles ; réassociation un par un à réception ; les caméras, en
  Wi-Fi, ne sont pas concernées et ne doivent pas être supprimées de
  l'application ; vendue sans adaptateur secteur.
- **FAQ** : 7 questions reprenant le message envoyé aux clients (qui est
  concerné, compatibilité des accessoires, manipulations à réception,
  caméras, absence d'adaptateur, carte SIM et abonnement, garantie).
- **Fiche technique** : bandeau 8 lignes + les trois accordéons
  (sécurité, connectivité, alimentation).
- **Option associée** : l'adaptateur secteur SA501, puisque la centrale
  est livrée sans.

**Correction importante** : `contenu_du_pack` listait le contenu du
*Starter Pack* (centrale + 2 contacteurs + détecteur + 2 télécommandes +
2 badges) alors que le produit est la centrale seule à 99,90 €. Remplacé
par le contenu réel.

L'**adaptateur secteur Key** (`7978957701333`) a été converti dans la
foulée, puisqu'il est désormais l'option affichée sous le bouton d'achat :
`acc-premium`, titre de page, accroche, note de compatibilité, bandeau et
contenu du pack.

### À traiter

- Les 5 visuels issus de la gamme AM302 sont des infographies génériques
  (Alexa / Google Home, carte SIM, sans abonnement) : conservés sur
  décision du 02/09. Leurs `alt` ont été neutralisés, puisque les mêmes
  fichiers servent sur les fiches Touch XL.
- **Bloc « Complétez votre système »** : `acc-complements` cherche une
  collection dont le titre contient « Compatible », et la gamme Key n'en a
  pas — « ACCESSOIRES KEY (SA501) » est une collection manuelle. La section
  se masque donc proprement sur les fiches Key seules (WDS501, WVD501,
  WKE501, centrale SA501 4G, adaptateur secteur). Pour l'afficher, il
  faudrait renommer cette collection ou en créer une « Compatible gamme
  Key » sur le tag `gamme_sa501`.
- La centrale n'a pas reçu `categorie_de_produit` : elle resterait sinon
  dans « Tous les accessoires ». La centrale Touch AM301 seule, elle, l'a.


## 6. Retouches du 02/09 (après publication)

Thème publié entre-temps : **Accessoires Elite Key 02092026 (Claude)**
(`202807476564`), qui est devenu le thème principal. Les corrections
ci-dessous vivent dans un nouveau brouillon,
**Espacements et correctif SA501 02092026 (Claude)** (`202819666260`),
à publier.

### Erreur Liquid en bas de page

`Liquid error (sections/acc-complements line 34): comparison of String
with 1 failed`, visible sur les fiches de la gamme Key seule. La section
cherche la collection « Compatible … » du produit ; la gamme Key n'en a
pas, `source_handle` restait vide et `collections['']` ne renvoyait pas de
collection, si bien que `source.products_count` n'était plus un nombre.
Le compteur est désormais calculé de façon sûre et la section se masque
sans rien afficher.

### Titre du bloc « Dans la boîte »

Nouveau métachamp **`custom.titre_boite`** (texte court) lu par
`acc-boite` avant le réglage de section. Il permet de remplacer
« Tout est fourni. » fiche par fiche sans toucher au gabarit partagé.
Réglé sur « La centrale, et rien d'autre. » pour la SA501 4G, dont le
contenu du pack est désormais une seule ligne.

### Espacements

Rythme vertical resserré d'environ un tiers dans `acc-premium.css`, ce qui
profite à toutes les fiches premium :

| Variable / règle | Avant | Après |
|---|---|---|
| `--accp-bande` | clamp(64px, 10vw, 132px) | clamp(42px, 6.4vw, 84px) |
| `.accp-bande--serree` | clamp(44px, 6vw, 80px) | clamp(30px, 4.2vw, 54px) |
| `.accp-hero` (bas) | clamp(48px, 7vw, 76px) | clamp(32px, 4.6vw, 52px) |
| `.accp-galerie` | clamp(24px, 4vw, 36px) | clamp(18px, 2.8vw, 28px) |
| `.accp-achat` | clamp(28px, 4vw, 40px) | clamp(20px, 2.8vw, 30px) |
| `.accp-chrono` | clamp(36px, 5vw, 64px) | clamp(24px, 3.4vw, 42px) |
| `.accp-specs` | clamp(28px, 4vw, 48px) | clamp(20px, 3vw, 34px) |
| `.accp-boite` | clamp(24px, 4vw, 40px) | clamp(18px, 2.8vw, 28px) |
| `.accp-faq` | clamp(26px, 4vw, 42px) | clamp(18px, 2.8vw, 30px) |

Reste un levier non actionné : les marges des sections d'application dans
`product.acc-premium.json` (Moast 40 px en bas, Judge.me 12/32, Vus
récemment 24/36). À réduire si la page paraît encore aérée.

### Titre de la fiche SA501

`productType` passé de « Centrale Key » à « Centrale SA501 » et le nom de
produit du bandeau de « SA501 4G » à « Key 4G », ce qui donne le H1
demandé : **Daewoo Centrale SA501 Key 4G**. Le sous-titre, qui répétait
l'accroche, devient « La centrale seule, en version 4G. »

### Avis clients : carrousel Judge.me sur les avis du produit

Deux essais avant de trouver. Le `cards_carousel` de la page d'accueil
etait bien plus leger que le `review_widget`, mais affichait les avis mis
en avant de la boutique et non ceux du produit. Le reglage
`reviews_selection` n'etant pas valide contre une liste de valeurs cote
Shopify (verifie en envoyant une valeur bidon, acceptee sans erreur), il
n'y avait aucun moyen sur de deviner l'option correspondante.

Deux valeurs ont ete lues dans le theme apres reglage manuel depuis
l'editeur. La premiere, `product_reviews`, ne correspondait a aucune option
du bloc : Judge.me la ignorait et retombait sur « tous les avis ». La bonne
est **`current_product`**, verifiee en ligne sur la fiche SA501.

D'apres la documentation du bloc, « Current product » affiche les avis du
produit consulte **et exclut** ceux des autres produits de son Product
Group Judge.me. Il n'existe pas d'option « collection » : les seuls choix
sont tous les avis, les avis mis en avant, le produit courant, et une
selection manuelle d'au plus 10 produits.

Configuration retenue, reprise sur les 7 gabarits :

| Reglage | Valeur |
|---|---|
| `reviews_selection` | `current_product` |
| `show_sample_reviews` | false (pas de faux avis de demonstration) |
| `star_rating` | `all` |
| `display_order` | `media_first` |
| `no_image_fallback` | `review_text_only` |
| `max_reviews` / `reviews_shown` | 20 / 4 |
| `image_ratio` | 1 |
| `header_text` | Les avis de nos clients |
| `show_average_rating` | true |

Gabarits concernes : `acc-premium`, `acc-premium-sd`,
`centrale-seule-touch`, `centrale-seule-touchxl`, `sim-1mois`, `sim-1an`,
`sim-1an-elite`.

Deux ajustements qui accompagnent ce choix :

- `acc-avis` ne s'affiche plus du tout quand le produit n'a aucun avis.
  Auparavant la section laissait un surtitre orphelin au-dessus d'un
  carrousel vide.
- Les regles CSS qui masquaient le titre et l'histogramme du
  `review_widget` ont ete retirees d'`acc-premium.css` : ce bloc n'est plus
  utilise, et les selecteurs risquaient de masquer par ricochet l'en-tete
  du carrousel.

**Etat des avis par produit** (metachamp `reviews.rating_count`) : quinze
accessoires affichent exactement 152 avis, ce qui indique un regroupement
de produits cote Judge.me plutot que des comptes propres. Les valeurs
distinctes sont WOS501 (6), autocollants (6), canon a fumee (3),
adaptateur secteur Key (2) et centrale SA501 4G (16).

**Seul produit sans aucun avis : la sirene interieure WIS502**
(`7975041433813`), qui n'a pas de metachamp `rating_count`. Son carrousel
restera vide. Le carrousel n'offre pas de repli automatique vers la
collection ; la facon propre de traiter ce cas est de rattacher le WIS502
au groupe de produits Judge.me qui donne leurs 152 avis aux autres
accessoires, ce qui se fait dans l'application Judge.me.

Note : le fichier `templates/product.zz-probe.json`, cree pour tester les
valeurs du reglage, est reste dans le theme — la suppression de fichiers de
theme est bloquee depuis l'API. Il n'est utilise par aucun produit ; a
supprimer depuis l'admin Shopify.
