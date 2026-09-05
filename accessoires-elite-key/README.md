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

## 7. Suites du 02/09

### Collection « Compatible gamme Key (SA501) »

`gid://shopify/Collection/726036578644` · handle `gamme-key-accessoires` ·
15 produits · publiee sur la boutique en ligne.

Motif : `acc-complements` cherche, parmi les collections du produit, la
premiere dont le titre contient « compatible ». La gamme Key n'en avait
aucune — « ACCESSOIRES KEY (SA501) » est une collection manuelle dont le
titre ne contient pas le mot — donc le bloc « Completez votre systeme »
restait masque sur les fiches Key.

Regle : **TAG egale `gamme_key`**, sans la condition
`categorie_de_produit = Accessoires` retenue pour les deux autres gammes.
La centrale SA501 4G et l'adaptateur secteur n'ont pas ce metachamp
(volontairement, pour ne pas faire entrer une centrale dans « Tous les
accessoires ») et seraient sinon exclus, alors que ce sont justement deux
des fiches concernees.

Produits tagues : WDS501, WPS501, WVD501, WOS501S, WMO501, WSD501, WRC501,
WRF501, WWF501, WKE501, WDG501, les cartes SIM 1 mois et 1 an, la centrale
Key 4G et l'adaptateur secteur. Le canon a fumee et les autocollants n'ont
pas ete tagues : ils ont deja leur collection « Compatible toutes gammes ».

Les produits compatibles Key **et** Elite appartiennent desormais a deux
collections « Compatible … ». `acc-complements` prend la premiere trouvee ;
les deux propositions sont valables, la famille 501 etant commune.

Constate au passage : **WIS502 et WOS501 sont ARCHIVES**, ce qui explique
et clot le point sur leurs anciennes images et sur l'absence d'avis du
WIS502.

### Fiches Configurateur des cartes SIM

Les quatre produits Configurateur (1 mois, 1 an Vigilia, 1 an
Vigilia/Touch, 1 an Elite) ont ete reecrits sur le meme fond que les fiches
publiques : enveloppe presentee comme une reserve unique exprimee de trois
facons et renouvelee chaque mois, tarifs, recharge, RIB demande a
l'activation meme en prepaye, APN `sl2sfr`, France uniquement,
non-remboursable une fois activee.

L'erreur principale corrigee : la fiche Elite listait
« 60 minutes / 300 SMS / 200 Mo » comme trois postes qui s'additionnent,
et ne disait rien du basculement sur les donnees mobiles qui justifie
justement son enveloppe plus large.

### Visuels EP506

Le metaobjet `ep-506-1` (`245413380436`) utilisait trois visuels de la W503
sur quatre. Les quatre pointent desormais sur des visuels EP506 en WebP
2048 px :

| Bloc | Visuel |
|---|---|
| Resistante | `camera-exterieure-daewoo-ep506-etanche-intemperies` |
| Audio bidirectionnel | `camera-daewoo-ep506-surveillance-smartphone` |
| Vision nocturne couleur | `camera-daewoo-ep506-vision-nocturne-couleur` |
| Detection de mouvement | `camera-daewoo-ep506-detection-suivi-mouvements` |

Le troisieme bloc portait « Notifications instantanees avec apercu
rapide » ; aucun visuel EP506 ne correspondait a ce propos, et le seul
disponible qui s'en approchait servait deja au bloc audio. Le bloc a donc
ete reecrit sur la vision nocturne couleur, qui est une vraie
caracteristique de la camera et dispose de son visuel. Les six images
EP506 ont recu leur texte alternatif.

### Menage

Fait : rien de destructif. Deux points ont ete volontairement laisses en
l'etat plutot que supprimes a l'aveugle.

- **Anciens PDF Afone** (`afone.pdf` et `afone_1mois.pdf`, 2021, 900 Ko a
  eux deux) : conserves. Impossible de prouver qu'ils ne sont references
  nulle part — les pages « Manuels » et « Notices » ont un corps vide et
  sont construites en sections ou via PageFly, donc leurs liens ne sont pas
  interrogeables simplement. Le gain de place est negligeable ; le risque
  d'un lien mort sur une page vivante ne l'est pas. Ils contiennent en
  revanche des tarifs de 2020 : a supprimer depuis l'admin apres
  verification visuelle des pages qui pourraient y renvoyer.
- **Doublon suppose sur la W503** : `camera-autonome-daewoo-w503-panneau-solaire.webp`
  et `camera-w503-daewoo-panneau-solaire-fixation-murale.webp` font le meme
  poids exact (77 716 o) mais portent deux descriptions differentes et
  servent sur deux fiches differentes. Les images ne sont pas affichables
  depuis cet environnement : a trancher a l'oeil dans la bibliotheque.

A faire depuis l'admin Shopify, l'API bloquant ces suppressions :

- `templates/product.zz-probe.json`, present dans le theme publie
  « Version definitive 02092026 » et dans le precedent. Fichier de test,
  utilise par aucun produit.
- Les brouillons de theme devenus inutiles : « RESTAURATION URGENTE -
  Fusion complete », « Avis clients v1 - bandeau temps reel », « Retouches
  fiches SIM 01092026 - Avant Pagefly », « Home conversion 02092026 »,
  « Accessoires Elite Key 02092026 ». Garder le theme publie et
  « Espacements et correctif SA501 02092026 » comme retour arriere, ainsi
  que les deux themes marques « NE PAS SUPPRIMER ».

### Centrale Élite PA501Z seule dans la collection Élite

`DAPA501Z` (`7843976184021`, 199,90 €) portait deja le tag `gamme_elite`
mais restait hors de « Compatible gamme Élite » : la regle de cette
collection est `categorie_de_produit = Accessoires` **ET** tag
`gamme_elite`, et le metachamp manquait.

Solution retenue : ajouter `categorie_de_produit = Accessoires` a la
centrale, plutot que de retirer cette condition de la regle. La collection
Élite ne peut pas passer en tag seul comme la gamme Key : `gamme_elite`
est un tag ancien, porte aussi par les packs (Starter pack Élite, offres
exclusives, configurateurs), qui se retrouveraient alors dans la
collection d'accessoires. La gamme Key, elle, utilise un tag `gamme_key`
cree pour l'occasion, donc sans contamination.

Ce choix suit la convention deja en place : les centrales Touch AM301 et
Touch XL AM302 vendues seules portent elles aussi
`categorie_de_produit = Accessoires`. Effet de bord assume et coherent :
la centrale entre aussi dans « Tous les accessoires » (51 -> 52).

**Point technique utile** : ecrire un metachamp avec `metafieldsSet` ne
declenche pas le recalcul des collections automatisees. Il faut un
`productUpdate` sur le produit, meme sans changement de valeur, pour que
Shopify le reindexe. Sans cela, la collection reste inchangee, ce qui peut
faire croire a une regle qui ne marche pas.

Asymetrie restante, non traitee faute de demande : la centrale Key SA501
4G est dans « Compatible gamme Key (SA501) » via le tag, mais pas dans
« Tous les accessoires », faute du metachamp categorie. Et sa fiche, comme
celles des centrales Touch, est au gabarit premium, alors que la fiche
PA501Z est encore sur `pack-par-defaut`.

## 8. Fiche centrale Élite PA501Z (03/09)

`DAPA501Z` (`7843976184021`, 199,90 €) passe de `pack-par-defaut` a
`acc-premium`. Quatrieme et derniere « centrale seule » au gabarit premium,
apres Touch AM301, Touch XL AM302 et Key SA501 4G. En ligne, sans
publication de theme.

Tout le contenu vient de la fiche existante, qui etait deja riche : rien
n'a ete invente, seulement redistribue dans les blocs du gabarit.

- **Titre** : `productType` passe de « Alarme » a « Centrale Élite » et le
  nom de produit du bandeau vaut `PA501Z`, ce qui donne
  « Daewoo Centrale Élite PA501Z ».
- **Sous-titre** « Trois reseaux, aucune coupure. » et accroche sur la
  bascule Wi-Fi / Ethernet / 4G, la passerelle Zigbee et la batterie.
- **Bandeau caracteristiques**, 8 lignes : reference, type, connexions,
  bascule reseau automatique, capacite 200 accessoires, batterie 10 h,
  liaison radio bidirectionnelle cryptee, emplacement carte SIM 4G.
- **Son role** : le cœur du systeme, la continuite reseau, l'evolutivite.
- **Compatibilite** : accessoires de la gamme Key compatibles, avec les
  trois exceptions documentees (WDS501, WVD501, WKE501 → versions Zigbee),
  passerelle Zigbee ouverte au marche, et l'incompatibilite assumee avec
  Alexa et Google Home.
- **FAQ** : 7 questions, dont le remplacement d'une SA501 en gardant ses
  accessoires, le comportement en coupure Internet et en coupure de
  courant, et l'absence d'abonnement.
- **Option associee** : la carte SIM 1 an Élite, puisque la 4G en a besoin.
- **Dans la boite** : centrale, adaptateur secteur et cable Ethernet
  RJ45, avec le titre surcharge en « La centrale et son branchement. » via
  `custom.titre_boite`. Le cable RJ45 est aussi signale dans le bloc
  alimentation, la liaison filaire etant un argument de la fiche.
- Les cinq visuels PA501Z ont recu leur texte alternatif.

Le bloc « Completez votre systeme » fonctionne desormais sur cette fiche,
la centrale ayant rejoint « Compatible gamme Élite » la veille.

## 9. Bouton « Ajouter au panier » — degrade navy (03/09)

Harmonisation du bouton d'achat sur tout le site : un bleu navy avec un
degrade leger vers la droite.

Etat constate avant modification, dans l'export du theme :

- `settings.color_button_background` = `#0c1e4a` (navy, deja en place sur
  tout le theme Home) et `settings.color_button_gradient` **vide**. Le
  theme expose donc nativement un reglage de degrade, non utilise.
- `snippets/css-variables.liquid` retombe sur la couleur pleine quand le
  degrade est vide, ce qui explique l'aspect uniforme actuel.
- Les fiches premium, elles, utilisaient `--accp-bleu` (`#1a4fab`), un
  bleu roi plus clair : c'etait la vraie incoherence.
- Aucune section ni aucun asset ne code une couleur de bouton en dur.

Degrade retenu (« Equilibre », valide sur maquette) :

```
linear-gradient(90deg,#0c1e4a 0%,#1a3f7a 100%)
```

Contraste du texte blanc : 16,15:1 au depart, 10,31:1 a l'arrivee — les
deux extremites restent tres au-dessus du seuil AAA.

Deux endroits a modifier :

1. `config/settings_data.json` — renseigner `color_button_gradient` avec
   la valeur ci-dessus. `color_button_background` reste a `#0c1e4a` : il
   sert de repli si le degrade n'est pas supporte. Meme valeur a poser sur
   `color_drawer_button_gradient` pour le tiroir panier.
2. `assets/acc-premium.css` — `.accp-bouton` passe de
   `background:var(--accp-bleu)` a `background:var(--accp-panier)`, un
   nouveau token qui porte le degrade. `--accp-bleu` **reste inchange** :
   il sert aussi aux surtitres `.accp-ref`, aux liens `.accp-lien`, a
   l'anneau de focus et aux chevrons de la FAQ, qui doivent garder le
   bleu roi. `--accp-navy` est ajoute pour disposer du navy plein.
   `.accp-bouton[disabled]` recoit `background-image:none` pour que le
   gris desactive ne laisse pas passer le degrade.

La barre collante (`sections/acc-barre.liquid`) reutilise `.accp-bouton`
et suit donc automatiquement.

## 10. Lien « Je veux comparer » sur l'accueil (04/09)

La carte « Je veux comparer » du bloc « Vous hésitez encore ? » pointait
vers `/pages/comparateur-am301-sa501-pa501z`. Elle pointe desormais vers
`/pages/product-compare` (page « Product Compare », publiee).

Le lien est defini dans `snippets/dw-chemins.liquid`, rendu par la section
`custom_liquid_kCUJGw` de `templates/index.json` :

```liquid
{% assign compare_url = "https://daewoo-security.fr/pages/product-compare" %}
```

Le fichier ne change que sur cette ligne : 9 070 octets contre 9 085, soit
exactement les 15 octets d'ecart entre les deux identifiants de page.

À noter : le bloc `image_JhEhKY` du diaporama `slideshow_BKBykn` porte
encore l'ancienne URL, mais ce diaporama est **desactive** sur l'accueil,
il n'a donc pas ete touche.

### Bouton panier : ce qui est fait, ce qui reste

`assets/acc-premium.css` porte le degrade (section 9) : les fiches
accessoires premium et leur barre collante sont a jour.

`config/settings_data.json` n'a **pas** ete modifie. Deux tentatives de
reecriture par l'API ont perdu du contenu en cours de retranscription (la
premiere a supprime les blocs d'application `powerful-form-builder` et
`pagefly-page-builder` — depuis desinstalles, donc sans consequence, mais
le controle de taille laissait encore un ecart inexplique). Le champ
`size` renvoye par l'API est la taille **compactee** du JSON, pas celle du
fichier lisible, ce qui rend la verification par octets impossible sur ce
fichier — contrairement aux `.liquid` et `.css`, stockes tels quels.

Les deux reglages restants se posent donc dans l'editeur de theme,
Parametres du theme → Couleurs :

- **Boutons → Degrade arriere-plan**
- **Menu et Tiroirs → Degrade de l'arriere-plan du bouton**

Dans les deux cas : degrade lineaire, 90° (vers la droite), `#0C1E4A` a
0 % et `#1A3F7A` a 100 %. Le champ « Arriere-plan » reste a `#0C1E4A`.

## 11. Page /collections/all (05/09)

### Ce que la page affichait

`/collections/all` est la collection automatique de Shopify : elle liste
tout ce qui est publie sur la boutique en ligne. N'etant pas une vraie
collection, elle n'a ni titre, ni description, ni image.

Le gabarit `templates/collection.json` lui appliquait quand meme
`main-collection-banner`, regle sur **550 px de haut** avec superposition
`#0c1e4a` : un grand bloc vide, suivi de la grille.

Mesure faite sur l'API :

| | |
|---|---|
| Produits actifs et publies | 156 |
| dont tag `Configurateur` | **59** (38 %) |
| Produits reels | 97 |
| Pages de pagination (50/page) | 4 |

Les 59 produits « Configurateur \| … » sont les variantes internes du
configurateur. Ils portent le tag `hidden-from-store`, mais **le theme ne
l'utilise nulle part** : `grep hidden-from-store sections/main-collection.liquid`
ne renvoie rien. Ils s'affichent donc en clair, avec le meme visuel et
presque le meme titre que le produit reel.

Le tag `Configurateur` est le sur-ensemble propre : 59 produits, dont les
57 marques `hidden-from-store`. Aucun produit ne porte `hidden-from-store`
sans `Configurateur`.

### Ce qui a ete construit

`sections/coll-catalogue.liquid` (9 564 o), section autonome :

1. **En-tete d'orientation** — surtitre, H1, chapo, sur le fond `#eef2fd`
   des fiches premium.
2. **Six cartes de destination**, en blocs editables : les trois gammes
   d'alarme, les cameras, tous les accessoires, la maison connectee.
   Chaque carte prend l'image de la collection, avec repli sur le premier
   produit, et affiche son nombre de produits.
3. **Grille**, qui saute les produits portant le tag exclu. Elle appelle
   le snippet `product-card` du theme avec les memes reglages globaux que
   `main-collection` : les cartes sont identiques a celles des autres
   collections.

`templates/collection.all.json` (2 412 o) monte cette section, puis
« Vous avez consulte ».

Le tag exclu est un reglage (`tag_exclu`, defaut `Configurateur`) : le
vider reaffiche tout.

### Reserve a lever

**Je n'ai pas pu verifier que Shopify route bien `/collections/all` vers
`templates/collection.all.json`.** La documentation ne decrit les gabarits
alternatifs que via le `template_suffix` d'une collection, et la collection
« all » etant virtuelle, elle n'en a pas. Le proxy de l'environnement
bloque le domaine, donc aucun rendu n'est possible d'ici.

Si le routage ne fonctionne pas, la solution de repli est une vraie
collection automatique (regle `TAG NOT_EQUALS Configurateur`, soit les
97 produits reels), avec titre, description et image, vers laquelle
`/collections/all` est redirigee.

### Pagination

La grille saute les produits exclus a l'interieur d'une page deja
paginee : avec 48 produits par page, une page peut donc en afficher
moins. C'est un compromis assume — filtrer avant de paginer n'est pas
possible en Liquid sur une collection automatique.
