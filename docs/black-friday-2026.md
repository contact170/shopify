# Black Friday 2026 : note de reprise

Opération Black Friday de daewoo-security.fr, du jeudi 12 novembre à 18h au
lundi 30 novembre 2026 à 23h59. Cette note décrit ce qui est prêt, le
fonctionnement des bons d'achat et la liste du lancement. État au 11/11/2026.

## Thème

- Copie non publiée du thème en ligne : « Black Friday 12112026 (Claude) »,
  `gid://shopify/OnlineStoreTheme/208484335956`.
  Aperçu : https://daewoo-security.fr/?preview_theme_id=208484335956
- La publication d'un thème est bloquée pour Claude : le dirigeant clique sur
  « Publier » dans l'admin.
- Copie des fichiers créés ou modifiés : dossier `theme/black-friday-2026/`
  (identique au thème au 11/11, sommes MD5 vérifiées).

| Fichier | Rôle |
|---|---|
| `sections/bf-home.liquid` (nouveau) | Bloc Black Friday en tête de l'accueil : titre, compte à rebours, ticket « Jusqu'à 70 € », cartes d'offres (blocs « Offre »). Disparaît seul après la date de fin. |
| `sections/gamme-home.liquid` (modifié) | Options « Habillage Black Friday », « Avantage sous le prix » et « Pastille sur chaque pack », réglage « Bon » par pack (le texte `[bon]` est remplacé par le montant du pack choisi), ancre `#packs-2026`. Vides ou décochées : rendu habituel. |
| `sections/header-group.json` | Bandeau `psi_bandeau` réglé en Black Friday (« jusqu'à 70 € offerts »), lien `/collections/black-friday`, fin le 30/11. |
| `templates/index.json` | Section `bf_home` ajoutée en premier, gamme en habillage Black Friday avec le montant du bon sur chaque pack. |
| `sections/bf-collection.liquid` + `templates/collection.black-friday.json` (nouveaux) | Page de la collection Black Friday : en-tête noir et jaune, grille des packs avec le montant du bon de chacun (listes `bon1_products` à `bon3_products`), étapes du bon, réassurance, conditions. |
| `sections/bf-pack-bon.liquid` (nouveau) | Bandeau noir en haut des fiches des 6 nouveaux packs : « Bon de X € offert pour votre prochaine commande, envoyé par e-mail le 15 décembre ». Montant lu dans l'étiquette du pack. Disparaît seul après le 30/11 à 23h59. |
| `templates/product.pack-gamme.json` | Section `bf_bon` (bandeau ci-dessus) ajoutée avant la fiche. Les 4 blocs de centrales ne changent pas. |
| `sections/pack-gamme.liquid` (modifié, voir `pack-gamme-vbf.diff`) | Code de pack `vbf` (étiquette `pack-vbf`) pour le Pack Vigilia Sécurité Renforcée, FAQ adaptée (2 centrales, prix barré estimé). |
| `templates/product.pack-vigilia-bf.json` (nouveau) | Fiche du Vigilia : 2 centrales (option « WiFi uniquement » / « WiFi & GSM »). Pas de bandeau de bon : ce pack n'y donne pas droit. |
| `templates/product.pg-vbf.json` | Modèle de test uniquement. Suppression bloquée pour Claude : à effacer dans « Modifier le code ». |
| `assets/bf-tmp-index.json`, `assets/bf-tmp-header-group.json` | Fichiers temporaires sans effet, à effacer dans « Modifier le code ». |

Les fichiers JSON du thème ne passent pas par `themeFilesUpsert` en mode URL
(le travail se termine sans rien écrire). Méthode qui marche : les envoyer en
`TEXT`, ou comme fichier `assets/…` puis `themeFilesCopy` vers leur place.
Shopify ajoute ensuite un en-tête de commentaire et remet en forme le JSON :
la somme MD5 change, pas le contenu.

## Produits et collection

| Produit | Réf. | Prix TTC | Prix barré | État |
|---|---|---|---|---|
| Pack Alarme Touch XL – Série précédente | AM3022601-002 | 369,90 € | 619,60 € (valeur achat séparé : kit AM302 299,90 + IP506P 69,90 + W503 119,90 + WOS305S 129,90) | Brouillon, fiche refaite (modèle `pack-touch-2`, métachamps) |
| Pack Alarme Vigilia Sécurité Renforcée | VIG2601-002 / VIG+2601-002 | 399,90 € / 449,90 € | 520,40 € / 525,80 € (métachamp `prix_reference`) | Brouillon, modèle `pack-vigilia-bf`, visuels refaits (textes alternatifs et noms de fichiers optimisés) |

- Prix barré du Vigilia : estimation prudente du prix configurateur, égale au
  prix de référence du Panorama Vigilia (588,20 / 593,60) moins le prix public
  d'un contacteur WDV301 et d'une télécommande WRC305 (67,80 €). Le vrai prix
  configurateur est au moins égal. L'ancien prix barré Shopify (624,20 / 674,20)
  a été retiré : il dépassait celui du Panorama, pack plus complet.
- Collection « Black Friday » `/collections/black-friday`
  (`gid://shopify/Collection/735299436884`), modèle `black-friday`, publiée
  sur la boutique en ligne le 10/11. Elle contient les 6 nouveaux packs et les
  2 packs ci-dessus.
- Une ancienne redirection `/collections/black-friday` → configurateur existe
  toujours. Elle ne s'applique que si la collection est dépubliée : on la garde
  comme repli après l'opération.

## Bons d'achat (décidé le 11/11)

Un bon pour la prochaine commande, selon le pack acheté entre le 12 et le
30 novembre 2026 :

| Bon | Packs | Étiquette du pack |
|---|---|---|
| 30 € | Essentiel | `pack-ess` |
| 50 € | Sécurité Intégrale, Vision Duo, Panorama | `pack-psi`, `pack-vdu`, `pack-pan` |
| 70 € | Vision Duo Solaire, Panorama Duo | `pack-vds`, `pack-pdu` |

Le Touch XL Série précédente et le Vigilia Sécurité Renforcée ne donnent pas
droit au bon (prix déjà remisés).

Fonctionnement :

- Le site annonce un envoi par e-mail **le 15 décembre**, après le délai de
  rétractation. Les commandes annulées ou retournées sont exclues.
- Gestion **manuelle** : chaque jour, Claude prépare la liste des commandes
  éligibles de la veille. Le 15 décembre, un code unique par commande est créé
  et l'e-mail est envoyé par le dirigeant.
- La liste reste dans Shopify : étiquettes de commande `bon-bf-30`,
  `bon-bf-50`, `bon-bf-70` (ajout par Claude sur accord du dirigeant). Les
  récapitulatifs ne contiennent que des numéros de commande, des packs et des
  montants, jamais de nom, d'e-mail ni d'adresse.
- Le 15 décembre, avant l'envoi : écarter les commandes remboursées, annulées
  ou en cours de retour, et celles livrées depuis moins de 14 jours (délai de
  rétractation pas encore écoulé).

Conditions du bon (décidées le 11/11) : valable jusqu'au **31 mars 2027
inclus**, **sans minimum d'achat**, utilisable en une seule fois. Elles
figurent dans le ticket de l'accueil, l'étape 3 de la page Black Friday et les
mentions en bas de ces deux pages.

Choix du dirigeant : la communication Black Friday ne parle jamais du délai de
rétractation (accueil, page Black Friday, bandeau, fiches). La date du
15 décembre est donnée sans justification. Seule la FAQ habituelle de
l'accueil (question « Livraison, retour et remboursement ») le cite, comme
avant l'opération.

## Offre du configurateur (Lovable), à coordonner

Le configurateur (projet Lovable « Configurateur Site Daewoo Security ») a sa
propre offre : caméra W503 offerte dès 600 € net, du jeudi 12 novembre 18h au
lundi 16 novembre 9h30. Elle repose sur 5 codes Shopify : `W503OFFERTE`,
`W503OFFERTE10`, `W503OFFERTE15`, `W503OFFERTE20`, `W503OFFERTE25`.

Point d'attention relevé le 11/11 : ces codes retirent 89,93 à 119,90 € sur
toute commande d'au moins 600 €, que la W503 soit dans le panier ou non, et se
cumulent avec les autres réductions. Un client qui connaît le code peut donc
l'utiliser sur un pack Black Friday de 600 € ou plus (Panorama Touch XL,
Vision Duo Solaire, Panorama Duo) sans prendre la caméra, et recevoir en plus
son bon de 70 €. Limites : une utilisation par client, 4 jours.

Le thème Black Friday garde le même code d'intégration du configurateur que le
thème en ligne (fichiers `layout/theme.liquid`, `snippets/custom.liquid`
identiques) : la publication du thème ne coupe rien.

## Lancement, jeudi 12 novembre à 18h

1. Le dirigeant publie le thème « Black Friday 12112026 (Claude) ».
2. Passer AM3022601-002 et VIG2601-002 en « Actif ». Ils sont déjà publiés
   sur la boutique en ligne depuis le 10/11 et rangés dans la collection Black
   Friday, mais restent invisibles partout (même dans l'aperçu du thème) tant
   qu'ils sont en brouillon.
3. Renommer « Offres du moment » en « Black Friday » et le faire pointer vers
   `/collections/black-friday`, dans les menus `menu-pc-2` et `menu-mobile`
   (les menus ne dépendent pas du thème : changement immédiat).
4. Vérifier l'accueil, la collection, les fiches et le panier sur mobile.
5. À partir du 13/11 : liste quotidienne des commandes éligibles au bon.

Après le 30/11 : republier le thème habituel, remettre le menu « Offres du
moment », dépublier la collection et repasser les deux packs en brouillon si
besoin. Le 15/12 : créer les codes et envoyer les e-mails.
