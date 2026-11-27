# Black Friday 2026 : note de reprise

Opération Black Friday de daewoo-security.fr, du vendredi 13 novembre à 16h au
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
| Pack Alarme Vigilia Sécurité Renforcée | VIG2601-002 / VIG+2601-002 | 389,90 € / 439,90 € (baissé de 10 € le 13/11, contre 399,90 / 449,90 au lancement) | 520,40 € / 525,80 € (métachamp `prix_reference`) | Brouillon, modèle `pack-vigilia-bf`, visuels refaits (textes alternatifs et noms de fichiers optimisés) |

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

Un bon pour la prochaine commande, selon le pack acheté entre le 13 et le
30 novembre 2026 :

| Bon | Packs | Étiquette du pack |
|---|---|---|
| 30 € | Essentiel | `pack-ess` |
| 50 € | Sécurité Intégrale, Vision Duo, Panorama | `pack-psi`, `pack-vdu`, `pack-pan` |
| 70 € | Vision Duo Solaire, Panorama Duo | `pack-vds`, `pack-pdu` |

Le Touch XL Série précédente et le Vigilia Sécurité Renforcée ne donnent pas
droit au bon (prix déjà remisés). Les commandes passées via le configurateur
non plus (décision du 16/11 : elles ont déjà la remise du configurateur et les
7 % Black Friday).

Liste des commandes éligibles : `docs/bons-black-friday-2026-liste.md`
(15 bons, 730 € au 20/11 14h ; étiquettes posées dans Shopify).

Règles décidées le 13/11 :
- **un bon par pack acheté** (2 packs = 2 bons, montants cumulés selon les
  packs) ;
- **un seul code par commande** : le bon ne se cumule ni avec un autre code
  ni avec un deuxième bon ;
- **commandes par téléphone ou sur devis éligibles** dès qu'elles contiennent
  un pack éligible (la liste quotidienne couvre donc tous les canaux de vente,
  y compris les commandes créées depuis l'admin).

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
propre offre : caméra W503 offerte dès 600 € net, du vendredi 13 novembre 16h
au lundi 16 novembre 9h30. Elle repose sur 5 codes Shopify : `W503OFFERTE`,
`W503OFFERTE10`, `W503OFFERTE15`, `W503OFFERTE20`, `W503OFFERTE25`.

Point d'attention relevé le 11/11 : ces codes retirent 89,93 à 119,90 € sur
toute commande d'au moins 600 €, que la W503 soit dans le panier ou non, et se
cumulent avec les autres réductions. Un client qui connaît le code peut donc
l'utiliser sur un pack Black Friday de 600 € ou plus (Panorama Touch XL,
Vision Duo Solaire, Panorama Duo) sans prendre la caméra, et recevoir en plus
son bon de 70 €. Limites : une utilisation par client, 4 jours.

Décision du 12/11 : l'offre W503 est **réservée au configurateur**. Le site
Black Friday n'en parle pas et n'ajoute pas de caméra au panier. Dans le
configurateur, la caméra est ajoutée automatiquement dès 600 € net, avec le
code du palier (`W503OFFERTE` ou `W503OFFERTE` + 10/15/20/25). Correction des
codes demandée à Lovable : n'avoir d'effet que si la W503 est dans le panier,
sans changer le palier de remise. Contrôle quotidien : signaler toute commande
avec un code W503 sans caméra W503.

Annonce sur l'accueil (13/11) : section à part « Black Friday · W503 »
(`sections/bf-w503.liquid`), placée juste au-dessus du configurateur
(« Aucun pack ne vous correspond ? »), et non plus dans le bloc Black Friday.
Visible du vendredi 13 novembre 16h au lundi 16 novembre 9h30, puis disparaît
seule. Avant 16h, ajouter `&bf_test=1` à l'adresse de l'aperçu pour la voir.
Sur mobile, version compacte (sans le paragraphe d'explication).

Bloc Black Friday de l'accueil sur mobile (13/11) : titre « BLACK FRIDAY » sur
une ligne, et texte court dans le ticket (réglage « Conditions, version courte
sur mobile »). Le texte complet reste affiché sur ordinateur.

Le thème Black Friday garde le même code d'intégration du configurateur que le
thème en ligne (fichiers `layout/theme.liquid`, `snippets/custom.liquid`
identiques) : la publication du thème ne coupe rien.

## Offre « −7 % en plus » du configurateur (16 au 20 novembre)

Lancée par le dirigeant le lundi 16 novembre à 17h, jusqu'au vendredi
20 novembre 2026 à 14h. Dans le configurateur, 7 % de remise s'ajoutent à la
remise palier : code `BLACKFRIDAY7` (remise de commande de 7 %, une fois par
client, cumulable), envoyé automatiquement par le configurateur avec les
remises automatiques `CONFIGURATEUR10/15/20/25` (remises produit cumulables
avec les remises de commande, vérifié le 16/11). Les 7 % s'appliquent donc sur
le prix après remise palier. Le code n'est affiché nulle part.

| Montant d'achat | Remise configurateur | Remise totale |
|---|---|---|
| dès 300 € | 10 % | 16,3 % |
| dès 450 € | 15 % | 21 % |
| dès 700 € | 20 % | 25,6 % |
| dès 900 € | 25 % | 30,3 % |

Mise en avant sur le site, dans la copie « Configurateur -7% 16112026
(Claude) » (`gid://shopify/OnlineStoreTheme/209106534740`), faite à partir du
thème en ligne « Corrections audit S46 14112026 (Claude) » :

- **Bandeau défilant** (`sections/psi-bandeau.liquid`) : nouveau « second
  message » en alternance avec le message Black Friday, avec sa pastille, son
  lien (`/pages/configurateur_2`) et ses dates. Il passe en premier et
  disparaît seul le 20/11 à 14h ; le message Black Friday reste jusqu'au 30/11.
  Les valeurs du second message sont les valeurs par défaut de la section
  (pas de modification de `sections/header-group.json`).
- **Encart de l'accueil** (`sections/bf-w503.liquid`, au-dessus du
  configurateur « Aucun pack ne vous correspond ? ») : l'encart W503, terminé,
  devient l'encart « Black Friday · Config » (sceau −7 %, 4 paliers calculés,
  échéance, temps restant, bouton « Composer mon alarme »). Le nom du fichier
  est gardé pour ne pas toucher à `templates/index.json`. Disparaît seul le
  20/11 à 14h. Sur mobile, les 4 paliers tiennent sur une ligne.
- `sections/bf-config.liquid` : fichier intermédiaire inutilisé, resté dans la
  copie (suppression bloquée pour Claude) ; à effacer dans « Modifier le code ».

Aperçus : `docs/apercus/bf-configurateur-7-*.png`,
`docs/apercus/bf-bandeau-defilant-7-ordi.png`.

Le thème à republier après le 30/11 reste « Avis Google accueil 09112026
(Claude) ».

Publié par le dirigeant le 16/11 vers 17h30 ; contrôle en ligne fait (accueil,
page Black Friday, fiche Sécurité Intégrale, configurateur, panier, sur
ordinateur et mobile) : bandeau à 2 messages, encart visible, pas d'erreur.

Point d'attention relevé le 16/11 (simulation de panier dans Shopify, sans
commande) :
- panier du configurateur à 469,60 € : remise palier 15 % (70,42 €) puis 7 %
  (27,94 €), total 371,24 €, soit −21 % : conforme ;
- Pack Panorama (529,90 €) avec le code `BLACKFRIDAY7` : 492,81 €. Le code
  marche donc hors configurateur (remise de commande sur tous les articles),
  et ce pack donne en plus le bon de 50 €. Aucune commande avec ce code au
  16/11 au soir.
- La remise `BLACKFRIDAY7` date de juillet (13 utilisations passées) et n'est
  utilisable qu'une fois par client : les clients de l'offre de juillet ne
  peuvent pas l'utiliser de nouveau.
- La collection `accessoires-configurateurs` ne contient que les produits
  « Configurateur | … » (références en C) : c'est la cible possible pour
  réserver les 7 % au configurateur.

Correction décidée le 16/11 (accord du dirigeant) :
- Le forfait Shopify ne permet pas de cumuler deux remises produit sur une même
  ligne (`productDiscountsWithTagsOnSameCartLine` refusé) : un code « 7 % sur
  les produits du configurateur » ne s'ajouterait pas au palier.
- Solution retenue : **un code par palier**, qui contient déjà la remise
  totale, limité à la collection `accessoires-configurateurs`, avec le même
  seuil que le palier, une fois par client, du 16/11 17h40 au 20/11 14h. Sur
  chaque ligne, Shopify garde la meilleure remise produit : le code remplace la
  remise automatique du palier.

| Palier | Code | Taux | Seuil | Remise Shopify |
|---|---|---|---|---|
| 10 % | `CFG16-ZCR5D3` | 16,3 % | 300 € | `DiscountCodeNode/2370678391124` |
| 15 % | `CFG21-FPSTYR` | 20,95 % | 450 € | `DiscountCodeNode/2370678292820` |
| 20 % | `CFG26-LTMSSF` | 25,6 % | 700 € | `DiscountCodeNode/2370678423892` |
| 25 % | `CFG30-E7SH8D` | 30,25 % | 900 € | `DiscountCodeNode/2370678456660` |

- Simulations (sans commande) : 339,70 € → 284,34 € ; 469,60 € → 371,25 € ;
  749,50 € → 557,65 € ; 909,40 € → 634,36 €. Code à 30 % sur un panier de
  469,60 € : refusé (le palier automatique de 15 % reste). Code sur le Pack
  Panorama, seul ou avec un article du configurateur : refusé.
- Shopify arrondit la remise au centime inférieur, article par article. Le
  configurateur doit faire le même calcul pour afficher le même total.
- Fait le 16/11 vers 18h : Lovable envoie le code du palier (commit
  `522c70f`, publication relancée par Claude), puis `BLACKFRIDAY7` a été
  désactivé (`DiscountCodeNode/2345005154644`, fin 17h01 UTC). Contrôle :
  `BLACKFRIDAY7` ne donne plus rien, ni sur un pack ni dans le configurateur ;
  `CFG21-FPSTYR` donne 371,25 € sur le panier de contrôle.
- Reste dans Lovable : le prix du bouton « Commander mon alarme » en haut de
  la recommandation (`RecoCompactHero.tsx`) et l'avantage estimé pendant le
  questionnaire (`LiveValuePanel.tsx`) calculent encore 7 % sur tout le panier,
  cartes SIM comprises. Message de correction : `docs/lovable-codes-paliers-black-friday.md`.
- Canon à fumée et recharge (F502WC, F502RC) : ils étaient dans la
  collection remisée (étiquette `Configurateur`, et sélection manuelle pour le
  canon) alors que le configurateur les exclut de la remise. Le 16/11, à la
  demande du dirigeant, ils ont été ajoutés aux exclusions de la collection
  `accessoires-configurateurs` (73 → 71 produits ; étiquettes inchangées).
  Contrôle : panier Vigilia + W512MW + WOS305S + canon + recharge avec
  `CFG16-ZCR5D3` → remise de 70,03 € sur les 3 articles du configurateur,
  canon et recharge au prix plein. Ni les paliers ni les codes CFG ne les
  remisent plus. Les cartes SIM et les prises connectées envoyées par le
  configurateur (références sans C) n'étaient déjà pas remisées.
- Le configurateur continue de proposer le canon à fumée et sa recharge
  (suggestions et recherche), à la demande du dirigeant, avec une pastille
  « Hors remise » (texte d'aide : non concerné par la remise du configurateur
  ni par les −7 %, non compté pour les paliers) sur tous les articles hors
  remise, dans les suggestions, la recherche et les lignes du devis. Texte du
  canon et de la recharge complété par « Prix fixe, hors remise du
  configurateur. » (Lovable, commit `b90889e`, 2,6 crédits).
- Lovable, commit `876a4de` : le prix du bouton « Commander mon alarme » et
  l'avantage estimé du questionnaire sont calculés comme les codes CFG
  (articles remisés uniquement).
- Les deux commits relus par Claude (affichage seulement, aucun calcul de
  prix modifié hors ces deux affichages), puis publication lancée le 16/11
  vers 18h15.

## Lancement : fait le vendredi 13 novembre vers 12h45

Thème « Black Friday 12112026 (Claude) » publié par le dirigeant. Ensuite :
AM3022601-002 et VIG2601-002 passés en « Actif » (publiés sur les 6 canaux,
Lovable compris) ; « Offres du moment » renommé « Black Friday » vers
`/collections/black-friday` dans `menu-pc-2` et `menu-mobile` (sous-menus
conservés). Vérifié en ligne : accueil (mobile et ordinateur), page Black Friday
(8 packs), fiches des 2 packs Black Friday et du Panorama Duo, sans erreur.
Thème à republier après l'opération : « Avis Google accueil 09112026 (Claude) »
(ancien thème en ligne). Codes W503 actifs depuis 12h15, encart W503 aligné.

## Liste de lancement (pour mémoire)

1. Le dirigeant publie le thème « Black Friday 12112026 (Claude) ».
2. Passer AM3022601-002 et VIG2601-002 en « Actif ». Ils sont déjà publiés
   sur la boutique en ligne depuis le 10/11 et rangés dans la collection Black
   Friday, mais restent invisibles partout (même dans l'aperçu du thème) tant
   qu'ils sont en brouillon.
3. Renommer « Offres du moment » en « Black Friday » et le faire pointer vers
   `/collections/black-friday`, dans les menus `menu-pc-2` et `menu-mobile`
   (les menus ne dépendent pas du thème : changement immédiat).
4. Vérifier l'accueil, la collection, les fiches et le panier sur mobile.
5. À partir du 14/11 : liste quotidienne des commandes éligibles au bon.

Après le 30/11 : republier le thème habituel, remettre le menu « Offres du
moment », dépublier la collection et repasser les deux packs en brouillon si
besoin. Le 15/12 : créer les codes et envoyer les e-mails.

## Point du 17/11 (décisions du dirigeant)

- Le bon de 30/50/70 € continue pour le moment (fin prévue le 30/11) ; décision
  vendredi 20/11 selon les ventes : il pourrait être remplacé par une réduction.
- Les 7 % du configurateur s'arrêtent le vendredi 20/11 à 14h ; une autre
  opération les remplacera (à définir).
- Fiche Notion de Franck corrigée le 17/11 (elle annonçait par erreur la fin
  du bon le 16/11 au soir et la fin des 7 % à midi).

## Prolongation des 7 % (20/11)

- Décision du dirigeant le 20/11 vers 11h30 : les 7 % du configurateur sont
  prolongés jusqu'au mardi 24/11 10h (« Prolongation exceptionnelle » affichée
  à partir de 14h). Lovable fait le bandeau du configurateur.
- Les 4 codes CFG prolongés par Claude jusqu'au 2026-11-24T09:00:00Z (10h
  Paris), vérifiés actifs. Lovable ne voit pas ces codes dans son accès Shopify.
- Fiche Notion de Franck passée à mardi 10h. Persona : dans le bloc Black
  Friday, « jusqu'au 20/11 14h » devient « jusqu'au 24/11 10h » (même longueur).
- Accueil (bandeau déroulant et encart) : copie « Prolongation -7% 20112026
  (Claude) » (`gid://shopify/OnlineStoreTheme/209515446612`), faite à partir du
  thème en ligne « Bon produit dans les vidéos 19112026 (Claude) » après
  suppression d'anciens thèmes par le dirigeant (limite de 20 thèmes). Seules
  les valeurs par défaut de `sections/bf-w503.liquid` et
  `sections/psi-bandeau.liquid` changent : fin mardi 24/11 10h, pastille
  « Prolongation exceptionnelle », échéance « Jusqu'à mardi 10h », conditions
  mises à jour (hors remise, pas de bon pour le configurateur). Aperçu vérifié
  sur ordinateur et mobile. À publier par le dirigeant à 14h.
- Le thème non publié « Franck fiche produit 19112026 (Claude) » garde
  l'ancienne fin (vendredi 14h) : y reporter ces 2 fichiers avant de le publier.
- 20/11 vers 14h15 : le dirigeant a déplacé l'encart « Black Friday · Config »
  dans l'éditeur du thème en ligne, juste après les avis Google (ordre :
  bf_home, dwh_hero, gamme_offre, avis_google, bf_w503, dwh_packs…). Vérifié en
  ligne. La copie de `templates/index.json` du dépôt n'a pas cet ordre.

## Équipements à prix Black Friday et encart configurateur sur la page BF (20/11)

Demande du dirigeant le 20/11 vers 14h20 : DB502W à −35 %, W503 à −30 % (offre
« 2e à −50 % » retirée provisoirement), NutriVision à −30 %, et un encart
configurateur sur la page Black Friday.

- **Prix (Shopify, en ligne dès le 20/11 vers 15h)**, prix barré = ancien prix,
  inchangé sur les 30 derniers jours (contrôlé sur les commandes web et Amazon
  du 21/10 au 20/11 ; pas de vente NutriVision sur la période) :

  | Produit | Variante | Prix | Barré | Remise |
  | --- | --- | --- | --- | --- |
  | Visiophone DB502W | 46917546967380 | 83,90 € | 129,90 € | −35,4 % |
  | Caméra W503 | 52524198396244 | 83,90 € | 119,90 € | −30,0 % |
  | NutriVision 501C | 40464497016985 | 111,90 € | 159,90 € | −30,0 % |

  Les produits « Configurateur | … » (W503C, DB502WC) ne changent pas.
  **À remettre après le 30/11** : 129,90 / 119,90 / 159,90 € et prix barré vide.
- **Collection `black-friday`** : les 3 produits ajoutés (11 offres) ;
  description mise à jour.
- **Thème** : copie « Promos produits BF 20112026 (Claude) »
  (`gid://shopify/OnlineStoreTheme/209531732308`), faite depuis le thème en
  ligne « Prolongation -7% 20112026 (Claude) ».
  - `sections/bf-collection.liquid` : encart configurateur (−7 % en plus,
    paliers, compte à rebours, bouton) entre l'en-tête et la liste, classes
    `bfc__cfg-…`, disparaît seul après le 24/11 10h ; badge « −X % » (arrondi à
    l'inférieur) pour la liste « Produits remisés ».
  - `templates/collection.black-friday.json` : les 3 produits remisés, texte
    d'en-tête (« jusqu'à −35 % ») et mention légale (prix barré = prix le plus
    bas des 30 jours précédents, du 20 au 30/11).
  - `sections/product-w503-landing.liquid` : réglage « Afficher l'offre -50 %
    sur la 2e caméra » (décoché par défaut) qui masque le bloc Pack Duo et les
    sélecteurs 1/2 caméras. À recocher dans l'éditeur quand l'offre reprend.
  - Aperçu vérifié sur ordinateur et mobile.
- **Thème publié** par le dirigeant le 20/11 vers 16h30 (Paris).
- **Remise automatique « W503 – La 2ème à -50% »** (2340706910548) :
  désactivée par Claude juste après la publication (fin 2026-11-20T15:30:43Z).
  La réactiver après le Black Friday si l'offre reprend (et recocher la case
  dans la fiche W503).
- **Contrôle en ligne (20/11)** : page BF avec encart et 11 offres (badges
  −35/−30 %), fiche W503 sans Pack Duo, prix barrés DB502W et NutriVision,
  accueil (encart et bandeau −7 %) ; panier simulé 2 × W503 + DB502W +
  NutriVision = 363,60 €, aucune remise « 2e à −50 % ».
- **Vidéos Moast (contrôle du 20/11)** : visibles et lisibles (lecteur avec le
  nouveau prix) sur W503, W503SP, W512MW, IP506P, EP506, DB502W, sirène WOS305S,
  SPW503, centrale Touch, packs gamme 2026, packs Touch (dont Touch XL BF),
  starters Touch et Élite, packs Élite, collections Touch et Vigilia.
  Bloc présent mais aucune vidéo associée dans Moast : NutriVision, canon
  F502W, centrale Touch XL, sonnette SB501, panneau SPW502.
  Aucune vidéo (déjà le cas avant le Black Friday, bloc dans la section
  « main-product » désactivée) : packs Vigilia (vig501 à vig507, offres
  Vigilia, Vigilia BF), starter Vigilia, prise SP502F.
- **Franck** : fiche Notion mise à jour (partie 4 bis : prix, liens, offre
  « 2e W503 à −50 % » suspendue, W512MW inchangée).
- **Reporté à la semaine du 23/11 (décision du dirigeant)** : ajouter les
  vidéos Moast sur les pages Vigilia (vig501 à vig507, offres Vigilia, Vigilia
  BF, starter Vigilia) et sur la prise SP502F, sous le bouton d'achat comme
  sur les packs Élite, dans une copie du thème. Vérifier en même temps les
  vidéos associées à ces produits dans Moast, et en associer à NutriVision,
  canon F502W, centrale Touch XL, sonnette SB501 et panneau SPW502.

## Questions Franck sur les fiches packs (20/11)

Décision du dirigeant le 20/11 : deux questions sous le bouton d'achat des
8 packs de l'offre, adaptées à chaque pack (différence entre packs,
installation des caméras, intérêt de la carte SIM). Un clic ouvre Franck dans un
panneau latéral avec la question déjà envoyée (reprise de la maquette du 19/11,
thème « Franck fiche produit 19112026 (Claude) », qui ne doit plus être publié
tel quel).

- **Métachamps produit** créés : « Franck – question 1 » et « Franck – question 2 »
  (`custom.franck_question_1` et `_2`, texte d'une ligne). Le bloc ne
  s'affiche que sur les produits qui ont une question 1.

  | Pack | Question 1 | Question 2 |
  | --- | --- | --- |
  | Essentiel | Quelle différence avec le Pack Sécurité Intégrale ? | À quoi sert la carte SIM avec ce pack ? |
  | Sécurité Intégrale | Quelle différence avec le Pack Panorama ? | Comment installer la caméra extérieure solaire ? |
  | Vision Duo | Quelle différence avec le Pack Vision Duo Solaire ? | Comment installer les 2 caméras extérieures ? |
  | Panorama | Quelle différence avec le Pack Sécurité Intégrale ? | Où et comment installer la caméra rotative ? |
  | Vision Duo Solaire | Quelle différence avec le Pack Vision Duo ? | Comment installer les caméras et leurs panneaux solaires ? |
  | Panorama Duo | Quelle différence avec le Pack Panorama ? | À quoi sert la carte SIM avec ce pack ? |
  | Vigilia Sécurité Renforcée (BF) | Quelle différence avec le Pack Sécurité Intégrale ? | Wi-Fi ou Wi-Fi + 4G : à quoi sert la carte SIM ? |
  | Touch XL série précédente (BF) | Quelle différence avec les nouveaux packs ? | Comment installer les caméras de ce pack ? |

  Le message envoyé à Franck est précédé de « À propos du produit « nom du
  pack » : ».
- **Thème** : copie « Franck packs BF 20112026 (Claude) »
  (`gid://shopify/OnlineStoreTheme/209544773972`), faite depuis le thème en
  ligne « Promos produits BF 20112026 (Claude) ».
  - `snippets/dw-franck-panneau.liquid` : identique à la maquette du 19/11.
  - `snippets/dw-franck-questions.liquid` : questions lues dans les métachamps,
    bloc masqué sans question 1 (plus de questions par défaut par gamme).
  - `snippets/dw-dock-offset.liquid` : une ligne ajoutée à la fin qui rend le
    bloc (à retirer pour annuler).
  - `sections/product-touch-landing.liquid` : `data-dwf-ancre` sur le bouton
    d'achat du haut (ligne 332), pour placer les questions sur le Touch XL.
  Copies des 3 snippets dans `theme/franck-packs-2026/snippets/`.
- À surveiller : crédits Chatbase consommés par les clics.

## Contrôle complet avant le week-end (20/11, vers 17h)

- Thème en ligne : « Franck packs BF 20112026 (Claude) ». Le dirigeant a
  supprimé « Franck fiche produit 19112026 (Claude) » et confirmé que le
  configurateur fonctionne.
- 12 pages principales sans erreur Liquid, traduction manquante ni erreur
  JavaScript ; 126 liens internes en 200.
- Panier réel avec les 6 packs, les 2 packs BF, W503, DB502W et NutriVision
  (11 articles, 3 818,90 €) puis page « Paiement - Daewoo Security » ouverte
  (articles et Alma présents) ; panier vidé ensuite.
- Clic sur « Ajouter au panier » validé sur les 8 packs (ordinateur). Le
  navigateur de test a ensuite été bloqué par la protection anti-robots de
  Shopify (429 « Just a moment… »), pas les visiteurs : W503, DB502W et
  NutriVision vérifiés sans navigateur (formulaire d'achat et prix présents),
  clic à faire par le dirigeant.
- Stocks : packs 80 à 100 par centrale ; configurateur bas sur SIM 1 mois (21),
  SIM 1 an Vigilia/Touch (34), WIS305 (49), EXT301 (50) ; DB502W 61.
- Livraison France : Colissimo et point relais gratuits dès 50 €, Chronopost 9,90 €.
- Codes CFG actifs jusqu'au 24/11 10h (25 utilisations) ; panier configurateur
  469,60 € → 371,25 € avec CFG21. Lovable : fin 24/11 10h, mêmes codes.
- Questions Franck présentes en ligne sur les 8 packs, absentes ailleurs.

## Finale Black Friday du configurateur (24 au 30 novembre)

Offre du dirigeant, mise en ligne par Lovable le 24/11 à 11h30 : à chaque
palier, une remise en plus ou, dès 450 €, un cadeau au choix. Les codes ne
sont pas recopiés ici (voir Shopify, Réductions, titres « BF finale … »).

| Palier | Remise en plus | Ou cadeau (minimum du code après remise) |
| --- | --- | --- |
| dès 300 € | +5 %, total 14,5 % (code créé le 24/11) | — |
| dès 450 € | +6 %, total 20,1 % (code créé le 24/11) | 2 WDV301, ou 2 WDS502Z pour Élite (440 €) |
| dès 700 € | +7 %, total 25,6 % (code du palier 700 € prolongé) | W503 (650 €) |
| dès 900 € | +8 %, total 31 % (code créé le 24/11) | W512MW (790 €) |

- 11 codes actifs du 24/11 11h30 au 30/11 23h59. Codes de palier limités à
  la collection `accessoires-configurateurs`, minimum sur le montant avant
  remise. Codes cadeaux : remise de commande égale au prix du cadeau après la
  remise du palier.
- **Minimum des codes cadeaux** : Shopify le vérifie **après** la remise
  automatique du configurateur (testé : refusé sur 709,20 € soit 567,36 € après
  −20 %, accepté sur 789 € soit 631,20 €). Les 450/700/900 € demandés par
  Lovable auraient bloqué des paniers légitimes ; réglés à 440/650/790 €, soit
  les plus petits paniers réels (441,83 / 655,92 / 794,93 € après remise,
  cadeau compris).
- « 1 utilisation par client » retirée sur les 11 codes (des clients du
  week-end avaient déjà utilisé les codes repris).
- Les 2 codes cadeaux du palier 25 % rendus cumulables avec les remises
  automatiques (ils ne l'étaient pas : le client aurait perdu le palier ou le
  cadeau).
- 9 paniers simulés : chaque palier, remise et cadeau, au centime près
  (ex. 469,60 € + 2 WDV301 → 399,18 € ; 909,10 € + W512MW → 681,87 €).
- Fiche Notion de Franck mise à jour (résumé, partie 5, bon, ancienne offre
  W503). Resynchroniser la source dans Chatbase.

### Bandeaux « dernière ligne droite » (24/11)

Copie « Finale BF 24112026 (Claude) » (`gid://shopify/OnlineStoreTheme/209848402260`),
faite depuis le thème en ligne « Franck packs BF 20112026 (Claude) ». À publier
par le dirigeant.

- Accueil : encart « Black Friday · Config » (`sections/bf-w503.liquid`) repris pour
  la Finale : pastille ronde « jusqu'à −8 % ou cadeau », titre « Jusqu'à −8 % en
  plus ou un cadeau sur votre alarme sur mesure », 4 paliers avec remise totale
  et cadeau (−14,5 % / −20,1 % ou 2 contacteurs / −25,6 % ou W503 / −31 % ou
  W512MW), compte à rebours, du 24/11 11h30 au 30/11 23h59. Paliers au format
  « seuil|remise|remise en plus|cadeau », 2 colonnes sur mobile.
- Page Black Friday : même encart (`sections/bf-collection.liquid`, réglages
  `cfg_*` par défaut).
- Bandeau défilant : second message « Dernière ligne droite · Finale Black
  Friday : jusqu'à −8 % en plus ou un cadeau offert » vers le configurateur,
  du 24/11 11h30 au 30/11 23h59, en premier ; pastille du premier message
  « Derniers jours ».
- Pastille rouge de l'accueil et de la page Black Friday : « Dernière ligne
  droite · fin le 30/11 » ; titre du compte à rebours : « Plus que ».
- Aperçu vérifié sur ordinateur et mobile, sans erreur.

### Page Black Friday plus claire et bon thème de départ (24/11)

- **Ne pas publier « Finale BF 24112026 (Claude) »** (`209848402260`) : elle
  vient de « Franck packs BF 20112026 », alors que le thème en ligne depuis le
  22/11 est « Fiche Vigilia mobile 22112026 (Claude) » (`209676763476`, fait
  dans une autre session). La publier retirerait les changements de la fiche
  Vigilia.
- Nouvelle copie faite depuis le thème en ligne : « Finale BF clair 24112026
  (Claude) » (`gid://shopify/OnlineStoreTheme/209851777364`), avec la Finale
  (encarts, bandeau défilant, pastilles) et la page Black Friday éclaircie.
- Page Black Friday : seul l'en-tête reste noir. L'encart du configurateur
  devient une carte crème bordée d'or (texte foncé, paliers sur fond blanc,
  bouton noir, échéance en pastille jaune, surtitre en rouge). Grille sur fond
  gris très clair `#f5f6fa` avec cartes blanches ombrées, liens « Voir l'offre »
  bleu marine, mention du bon en pastille jaune pâle. Étapes du bon et
  réassurance sur fond blanc, coches bleu marine.
- 24/11 vers 15h : « Finale BF clair 24112026 (Claude) » publiée par le
  dirigeant. Contrôle en ligne : 7 pages clés sans erreur Liquid (accueil, page
  BF, 2 packs, W503, configurateur, panier), encarts Finale visibles sur
  l'accueil et la page BF (paliers −14,5 / −20,1 / −25,6 / −31 %, « Fin dans
  6 j 8 h »), bandeau défilant « Dernière ligne droite » puis « Derniers
  jours », questions Franck toujours présentes sur les packs, aucune erreur
  JavaScript, pas de débordement mobile. Paniers simulés inchangés (palier 450 €
  avec contacteurs : 399,18 € ; palier 900 € à −31 % : 627,36 €).

### Accueil plus compact sur mobile (24/11)

- Copie « Accueil mobile compact 24112026 (Claude) »
  (`gid://shopify/OnlineStoreTheme/209883136340`), faite depuis le thème en
  ligne « Finale BF clair 24112026 (Claude) ». À publier par le dirigeant.
- Nouveau snippet `dw-accueil-mobile` (copie dans
  `theme/accueil-mobile-2026/snippets/`), rendu juste avant `</body>` dans
  `layout/theme.liquid`, sur la page d'accueil seulement :
  `{%- if template.name == 'index' -%}{%- render 'dw-accueil-mobile' -%}{%- endif -%}`.
  Tout est sous `@media (max-width:749px)` : rien ne change sur ordinateur.
- Réductions : marges des blocs (64 → 40 px), titres (33 → 28 px), en-tête
  Black Friday (titre, compte à rebours, ticket, cartes du carrousel plus
  étroites), téléphone du bloc d'accueil réduit à 78 %, image de la gamme en
  16/10, images des 2 packs « prêts à poser » ramenées à 190 px (elles étaient
  forcées à 348 px), quiz, configurateur, comparatif d'abonnement, atouts,
  FAQ. Mentions légales en 10,5–11 px.
- Masqués sur mobile : le paragraphe d'introduction de la gamme 2026 (les 4
  puces restent) et la section vide du carrousel d'avis Judge.me (84 px blancs,
  le widget est masqué par Judge.me ; elle réapparaît si le widget s'affiche).
- Mesure (390 px) : page de 14 369 px (17 écrans) → 11 664 px (13,8 écrans),
  encart Finale du configurateur du 5,9e au 4,8e écran. Ordinateur identique
  (10 983 px avant et après). Aucune erreur Liquid, pas de débordement.
- Pour annuler : retirer la ligne de rendu de `layout/theme.liquid`.
- 24/11 en fin d'après-midi : « Accueil mobile compact 24112026 (Claude) »
  publiée par le dirigeant. Contrôle en ligne : accueil mobile 11 681 px
  (13,8 écrans), ordinateur 10 984 px (inchangé), aucune erreur Liquid, pas de
  débordement. Compte à rebours, encart Finale (paliers −14,5 / −20,1 / −25,6 /
  −31 %), bandeau « Dernière ligne droite », quiz (question 1 → 2), barre
  collante et carrousel Black Friday fonctionnent. Page BF, pack Sécurité
  Intégrale (questions Franck présentes), pack Vigilia, W503 (83,90 € au lieu
  de 119,90 €), configurateur et panier : sans erreur, sans le CSS de
  l'accueil. Codes de la Finale actifs jusqu'au 30/11 23h59.

### Rupture de la caméra W512MW (25/11)

- La W512MW est en rupture ; réapprovisionnement entre le 5 et le 10 décembre.
  Tout reste commandable (stock Shopify inchangé, 673 unités affichées) : les
  packs partent tout de suite, les caméras W512MW suivent séparément.
- Thème en ligne le 25/11 au matin : « Panier et fiches BF 25112026 (Claude) »
  (`209894015316`, fait dans une autre session). Copie à publier : « Rupture
  W512MW v2 25112026 (Claude) » (`gid://shopify/OnlineStoreTheme/209947361620`).
  Une première copie faite par erreur depuis l'ancien thème a été renommée
  « NE PAS PUBLIER - Rupture W512MW ancienne base » (`209945067860`).
- Nouveaux métachamps produit : « Disponibilité – titre » (`custom.dispo_titre`)
  et « Disponibilité – message » (`custom.dispo_texte`), renseignés sur 13
  produits : Sécurité Intégrale, Panorama, Panorama Duo (2 caméras), Vigilia
  Sécurité Renforcée, offre Élite double W512MW (2), PA573 Harmonie+, PA574
  Tranquillité+ (2), VIG506, VIG507, AM343, AM353, la caméra W512MW et sa
  version configurateur (W512MWC). Pour retirer le message : vider ces champs.
- Thème : snippet `dw-dispo-message` (encadré jaune placé par script juste
  au-dessus du premier bouton d'achat, rendu avant `</body>` sur les fiches) ;
  snippet `dw-dispo-panier` (ligne sous l'article dans `main-cart` et
  `cart-drawer`) ; pastille sur les cartes de l'accueil (`bf-home`) et de la
  page Black Friday (`bf-collection`) ; phrase ajoutée à la légende des paliers
  de l'encart Finale (accueil et page BF). Copies des snippets dans
  `theme/rupture-w512mw-2026/snippets/`.
- Fiche Notion de Franck : partie « 1 bis » ajoutée (packs concernés,
  expédition séparée, configurateur, packs non concernés). À resynchroniser
  dans Chatbase.
- Aperçu vérifié : message sur les fiches (mobile et ordinateur), absent des
  packs non concernés, pastilles (2 sur l'accueil, 4 sur la page BF), légende,
  panier et tiroir (ligne sous le pack et sous la caméra), aucune erreur Liquid.
- À faire au réapprovisionnement : vider les métachamps des 13 produits.
- 25/11 : « Rupture W512MW v2 25112026 (Claude) » publiée par le dirigeant
  (avertissement côté configurateur Lovable fait par lui). Contrôle en ligne :
  message visible au-dessus du bouton d'achat sur les 11 packs et la caméra
  (texte « 2 caméras » sur Panorama Duo, Élite double et PA574), absent des
  packs non concernés ; pastilles (2 accueil, 4 page BF) ; légende des paliers
  sur l'accueil et la page BF ; panier et tiroir : ligne sous le pack, la
  caméra et la caméra du configurateur ; accueil compact conservé (11 800 px) ;
  aucune erreur Liquid, pas de débordement mobile.

### Offre Ultime (27/11)

- Pack Ultime créé (Vision Duo + sirène intérieure WIS305), prix net
  399,90 / 449,90 / 499,90 / 549,90 € jusqu'au mardi 1er décembre 9h, sans
  bon d'achat. Détails : `theme/offre-ultime-2026/README.md`.
- Copie à publier : « Offre Ultime 27112026 (Claude) » (210124734804).
- Fiche Notion de Franck : partie 4 « L'Offre Ultime », anciens packs
  marqués « retirés de la sélection Black Friday ». À resynchroniser.
