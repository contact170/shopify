# Fiches cartes SIM M2M Afone — refonte

Date : 01/09/2026
Thème de travail : id **202622009684**, renommé depuis « Site definitif 31082026 »

## Les trois fiches

| Produit | SKU | Prix | Suffixe actuel | Nouveau suffixe |
|---|---|---|---|---|
| Carte SIM M2M Afone 1 MOIS OFFERT | SIM1MOIS | 14,90 € | `carte-sim` | `sim-1mois` |
| Carte SIM M2M Afone 1 An Prépayé (Touch/Vigilia) | DASIM1AN | 72,00 € | `carte-sim-1-an` | `sim-1an` |
| Carte SIM M2M Afone 1 An Prépayé — Élite (PA501Z) | SIM1ANPA | 85,00 € | `carte-sim-1-an-elite` | `sim-1an-elite` |

### Pourquoi des suffixes dédiés

Les trois suffixes actuels sont **partagés** avec les produits Configurateur
(vérifié par balayage complet du catalogue — le filtre `template_suffix:` de
l'API Admin ne fonctionne pas, il renvoie tout sans filtrer) :

- `carte-sim` → SIM 1 mois **+** « Configurateur | SIM 1 mois Vigilia / Touch »
- `carte-sim-1-an` → SIM 1 an **+** « Configurateur | SIM 1 an Vigilia/Touch » **+** 2 brouillons
- `carte-sim-1-an-elite` → SIM 1 an Élite **+** « Configurateur | SIM 1 an Elite »

Les nouveaux templates sont donc créés à part ; les pages Configurateur restent
sur les templates actuels, inchangées.

## Données de l'opérateur (source : fiches Afone fournies le 01/09/2026)

Communes aux trois offres : réseau **SFR**, code APN **sl2sfr**, sans engagement,
activation sur `m2minstallateur.afonemobile.fr`, espace client `m2m.afonemobile.fr`,
service client 09 70 80 65 12 / serviceclients@afonemobile.fr.

| | 1 mois | 1 an Touch/Vigilia | 1 an Élite |
|---|---|---|---|
| Offre | mensuelle | prépayée 12 mois | prépayée 12 mois « Plus » |
| Enveloppe | 40 min **ou** 100 SMS **ou** 40 Mo | 30 min **ou** 150 SMS **ou** 50 Mo | 60 min **ou** 300 SMS **ou** 200 Mo |
| Tarif ensuite | 4,75 € TTC/mois | 6 € TTC/mois | 7,80 € TTC/mois |
| Recharge | 1 € TTC → 20 min / 50 SMS / 20 Mo | 1 € TTC → 15 min / 75 SMS / 25 Mo | 2 € TTC → 30 min / 150 SMS / 100 Mo |

Corrections apportées au contenu existant :

- La page Élite présentait « 60 minutes d'appels • 300 SMS • 200 Mo » comme trois
  enveloppes cumulables. La fiche Afone dit **ou** : c'est une réserve unique
  exprimée de trois façons. Corrigé sur les trois fiches.
- La page 1 mois annonçait « 40 min ou 100 SMS » en omettant les 40 Mo.
- La page 1 an Touch/Vigilia n'annonçait aucun contenu de forfait.

## Nouvelles sections de thème

| Fichier | Rôle |
|---|---|
| `sections/acc-couts.liquid` | Bloc « le coût, en clair » : paliers de dépense dans le temps (aujourd'hui / ensuite / recharge), encart foncé sur l'enveloppe incluse, mention légale. Blocs configurables, la section disparaît si aucun palier. |
| `sections/acc-documents.liquid` | Documents à télécharger : cartes cliquables avec titre, description, format et poids. La section disparaît si aucun document. |

Les deux réutilisent `acc-premium.css` et ses variables — même typographie,
mêmes rayons, mêmes ombres que les fiches accessoires.

## Structure des trois pages

`hero · à quoi ça sert · coûts · compatibilité · fiche technique · livraison ·
documents · en détail · avis · widget avis · FAQ · compléter · barre d'achat fixe`

Moast est volontairement absent (aucune vidéo UGC sur ces références).

## Contenu créé

9 métaobjets (3 par fiche) :

| Type | Handles |
|---|---|
| `a_quoi_ca_sert` | `sim-1-mois`, `sim-1-an-touch-vigilia`, `sim-1-an-elite` |
| `bandeau_caracteristiques` | idem |
| `faq_produit` | idem (8 questions chacune) |

Métachamps renseignés sur les trois produits : `titre_page`, `accroche`,
`a_quoi_ca_sert`, `bandeau_caracteristiques`, `faq`, `securite_detection`
(« Ce que la carte SIM apporte »), `connectivite` (« Ce qu'elle ne fait pas »),
`alimentation_autonomie` (« Activer et gérer l'abonnement »), `contenu_du_pack`,
`note_compatibilite`.

Descriptions produit et balises SEO réécrites sur les trois (la fiche 1 an
Touch/Vigilia n'avait aucune balise SEO).

## Documents

Les trois fiches PDF Afone ont été déposées dans la bibliothèque Shopify :

| Fichier | Poids | Fiche |
|---|---|---|
| `Afone_Mobile_Mensuelle.pdf` | 58 ko | 1 mois |
| `Afone_Mobile_12_mois.pdf` | 58 ko | 1 an Touch/Vigilia |
| `Afone_Mobile_12_mois_Plus.pdf` | 58 ko | 1 an Élite |

Les anciens `afone.pdf` et `afone_1mois.pdf` (octobre 2020) restent dans la
bibliothèque mais ne sont plus référencés : impossible de les ouvrir depuis
l'environnement de travail (le proxy bloque le CDN Shopify), donc impossible de
vérifier qu'ils disent la même chose que les fiches de 2026.

## Mise en ligne — faite le 01/09/2026

1. Thème **« Site definitif 31082026 »** (202622009684) publié. ✔
2. Les trois produits basculés sur `sim-1mois`, `sim-1an`, `sim-1an-elite`. ✔

Vérifié après bascule : les quatre produits Configurateur restent sur les
suffixes `carte-sim`, `carte-sim-1-an` et `carte-sim-1-an-elite`, inchangés.

Vérifié le 01/09/2026 : le thème en ligne « Copie de Site definitif 31082026 »
(202625057108) est une duplication de 202622009684 faite le 31/08 à 16 h 00 et
n'a pas été modifiée depuis (`updatedAt` = instant de création). Les 15 fichiers
de référence comparés — `settings_data.json`, `settings_schema.json`,
`layout/theme.liquid`, les trois groupes de sections, `index`, `product`,
`collection`, `cart`, `theme.css`, `acc-premium.js`, `acc-hero`, `acc-barre`,
`product.acc-premium.json` — sont identiques dans les deux thèmes. Publier
202622009684 ne fait donc qu'ajouter les fiches SIM.

Les correctifs galeries caméras (W512MW, W503, W503SP, IP506P, EP506) sont
**déjà en ligne** : le thème publié les contient.

`themeFilesCopy` ne permet pas de copier entre deux thèmes (pas de `srcThemeId`),
d'où le choix de publier le thème de travail plutôt que de reporter les fichiers.
Le thème « Fiches cartes SIM 01092026 » (202692755796), créé par précaution avant
cette vérification, est inutile et peut être supprimé.

L'ordre compte : `templateSuffix` est une propriété du produit, partagée par tous
les thèmes. Basculer avant publication pointerait les pages en ligne vers des
templates absents du thème publié.

## Arbitrages tranchés le 01/09/2026

1. **La carte 1 mois couvre aussi la centrale Key (SA501).** Métaobjet de
   compatibilité créé (`vigilia-touch-key` → « Vigilia, Touch & Key ») et
   rattaché au produit ; note de compatibilité, description et balise SEO
   mises à jour.
2. **L'enveloppe est mensuelle sur les trois offres**, y compris sur les cartes
   prépayées 12 mois : ce qui est prépayé, c'est l'abonnement, pas l'enveloppe.
   Les trois bandeaux affichent « Enveloppe mensuelle » et le texte précise
   « chaque mois ».
3. **Un RIB est demandé à l'activation, y compris pour les cartes prépayées
   1 an.** Rien n'est prélevé pendant les douze mois, mais c'est ce qui permet
   à la ligne de se poursuivre sans coupure au terme de l'année. Précisé à
   quatre endroits sur chaque fiche annuelle : bandeau (ligne « Activation »),
   accordéon « Activer et gérer l'abonnement », FAQ (question dédiée) et
   mention légale du bloc coûts.
4. **Brouillon « Carte SIM 1 An Prépayé — Pour centrale Vigilia »**
   (12260207067476, SKU SIM1VIG) : supprimé. Aucune commande rattachée.
5. **Titre de la fiche 1 mois** corrigé : « (40 min ou 100 SMS ou 40 Mo) ».
   Le handle d'URL est inchangé, aucune redirection nécessaire.

## Reste ouvert

- **Images** : 800 × 800 JPG pour les deux premières fiches, 1500 × 1500 PNG pour
  l'Élite. Non uniformisées.
- **Anciens PDF** `afone.pdf` et `afone_1mois.pdf` (2020) : toujours dans la
  bibliothèque, non référencés, contenu non vérifiable depuis l'environnement
  de travail.
- **Descriptions des produits Configurateur** : elles portent encore l'ancien
  texte. Celle du « Configurateur | SIM 1 an Elite » présente toujours le
  forfait sous forme de liste à puces — 60 minutes d'appels / 300 SMS /
  200 Mo de data — c'est-à-dire comme trois enveloppes cumulables, alors que
  la fiche Afone dit **ou**. Même inexactitude que celle corrigée sur la fiche
  principale. Non modifiée : les produits Configurateur ont été laissés
  intacts par principe.

## Retouches du 01/09/2026 (après première mise en ligne)

Thème de travail : **« Retouches fiches SIM 01092026 »** (id 202693738836),
duplication du thème en ligne.

### 1. Titre de page — le SKU remplacé par une référence lisible

`acc-hero` composait le titre `marque + product.type + variant.sku`, ce qui
donnait « Daewoo Carte SIM DASIM1AN ». Convenable pour un accessoire dont le
SKU est la référence commerciale (WVD301, WKE301), illisible pour une carte SIM
dont le SKU est un code interne.

Nouveau réglage de section `reference` : quand il est rempli, il remplace le
SKU dans le titre ; laissé vide, le comportement reste identique. Aucun autre
gabarit n'est affecté.

| Fiche | `reference` | Titre obtenu |
|---|---|---|
| 1 mois | `1 Mois Offert` | Daewoo Carte SIM 1 Mois Offert |
| 1 an | `1 An Prépayé` | Daewoo Carte SIM 1 An Prépayé |
| 1 an Élite | `1 An Prépayé Élite` | Daewoo Carte SIM 1 An Prépayé Élite |

### 2. Ligne sous le montant, dans le bloc coûts

La mention (« une seule fois, pour 12 mois ») était un `<span>` à l'intérieur du
`<p class="accp-cout__montant">` : elle héritait de `font-weight:600` et surtout
de `letter-spacing:-.035em`, d'où un texte gras et compressé. Elle est désormais
un paragraphe distinct, avec `font-weight:400` et `letter-spacing:normal`.

### 3. Élite — la bascule sur les données mobiles

Point métier ajouté : l'Élite PA501Z est **la seule centrale de la gamme** à
basculer sur les données mobiles en cas de coupure du Wi-Fi. L'application
Daewoo Home Connect reste utilisable — armer, désarmer, consulter l'historique —
là où les autres centrales se limitent aux SMS et à l'appel automatique. Les
caméras, elles, restent inaccessibles.

C'est ce qui justifie l'enveloppe de 200 Mo contre 50 Mo sur l'offre standard.
Ajouté dans : encart du bloc coûts, accordéon « Ce que la carte SIM apporte »,
accordéon « Ce qu'elle ne fait pas » (nuancé), FAQ (questions 1 et 3),
description produit (section dédiée), balise SEO, et 3e atout du hero
(« Application active hors Wi-Fi »).

### 4. Compatibilité de la carte 1 mois

Elle couvre les centrales **Vigilia, Touch (AM301, AM302) et Key (SA501)**.
Métaobjet `vigilia-touch-key`. La centrale **Élite PA501Z n'est pas
concernée** : cette carte ne lui est pas proposée, elle a sa propre offre.

La note de compatibilité et une section de la description l'expliquent au
client plutôt que de le laisser deviner : l'Élite dispose d'une offre dédiée
à l'enveloppe deux fois plus large, parce qu'elle bascule sur les données
mobiles en cas de coupure du Wi-Fi.

Le métaobjet `vigilia-touch-key-elite`, créé sur une lecture erronée puis
devenu inutile, a été supprimé.

### Mise en ligne

Publier **« Retouches fiches SIM 01092026 »**. Les suffixes produit sont déjà
en place, aucune bascule à refaire.
