# Black Friday 2026 : note de reprise

Opération Black Friday de daewoo-security.fr, du jeudi 12 novembre au matin au
lundi 30 novembre 2026 à 23h59. Cette note décrit ce qui est prêt, ce qui reste
à décider et la liste du lancement. État au 10/11/2026 au soir.

## Thème

- Copie non publiée du thème en ligne : « Black Friday 12112026 (Claude) »,
  `gid://shopify/OnlineStoreTheme/208484335956`.
  Aperçu : https://daewoo-security.fr/?preview_theme_id=208484335956
- La publication d'un thème est bloquée pour Claude : le dirigeant clique sur
  « Publier » dans l'admin.
- Copie des fichiers créés ou modifiés : dossier `theme/black-friday-2026/`.

| Fichier | Rôle |
|---|---|
| `sections/bf-home.liquid` (nouveau) | Bloc Black Friday en tête de l'accueil : titre, compte à rebours, ticket du bon de 50 €, cartes d'offres (blocs « Offre »). Disparaît seul après la date de fin. |
| `sections/gamme-home.liquid` (modifié) | Options « Habillage Black Friday », « Avantage sous le prix », « Pastille sur chaque pack » et ancre `#packs-2026`. Vides ou décochées : rendu habituel. |
| `sections/header-group.json` | Bandeau `psi_bandeau` réglé en Black Friday, lien `/collections/black-friday`, fin le 30/11. |
| `templates/index.json` | Section `bf_home` ajoutée en premier, gamme en habillage Black Friday. |
| `sections/bf-collection.liquid` + `templates/collection.black-friday.json` (nouveaux) | Page de la collection Black Friday : en-tête noir et jaune, grille des packs, étapes du bon, réassurance. |
| `sections/pack-gamme.liquid` (modifié, voir `pack-gamme-vbf.diff`) | Code de pack `vbf` (étiquette `pack-vbf`) pour le Pack Vigilia Sécurité Renforcée, FAQ adaptée (2 centrales, prix barré estimé). |
| `templates/product.pack-vigilia-bf.json` (nouveau) | Fiche du Vigilia : 2 centrales (option « WiFi uniquement » / « WiFi & GSM »). |
| `templates/product.pg-vbf.json` | Modèle de test uniquement (aperçu du code `vbf` sur un pack en ligne avec `?view=pg-vbf`). Suppression bloquée pour Claude : à effacer dans « Modifier le code ». |
| `assets/bf-tmp-index.json`, `assets/bf-tmp-header-group.json` | Fichiers temporaires sans effet, à effacer dans « Modifier le code ». |

Les fichiers JSON du thème ne passent pas par `themeFilesUpsert` en mode URL
(le travail se termine sans rien écrire). Méthode qui marche : envoyer le JSON
comme fichier `assets/…`, puis `themeFilesCopy` vers sa place, ou l'envoyer en
`TEXT` s'il est petit.

## Produits et collection

| Produit | Réf. | Prix TTC | Prix barré | État |
|---|---|---|---|---|
| Pack Alarme Touch XL – Série précédente | AM3022601-002 | 369,90 € | 619,60 € (valeur achat séparé : kit AM302 299,90 + IP506P 69,90 + W503 119,90 + WOS305S 129,90) | Brouillon, fiche refaite (modèle `pack-touch-2`, métachamps) |
| Pack Alarme Vigilia Sécurité Renforcée | VIG2601-002 / VIG+2601-002 | 399,90 € / 449,90 € | 520,40 € / 525,80 € (métachamp `prix_reference`) | Brouillon, modèle `pack-vigilia-bf`, visuels refaits |

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

## À décider

- Bon de 50 € pour l'achat d'un des 6 nouveaux packs. Proposition : réservé aux
  acheteurs de ces packs (segment client), une utilisation par client, dès 150 €
  d'achat, valable du 1er décembre au 31 janvier, envoyé par un bloc
  conditionnel dans l'e-mail de confirmation de commande. Les textes du thème
  (ticket, étapes, bandeau) l'annoncent déjà ; à ajuster une fois décidé.

## Lancement, jeudi 12 novembre au matin

1. Le dirigeant publie le thème « Black Friday 12112026 (Claude) ».
2. Passer AM3022601-002 et VIG2601-002 en « Actif ». Ils sont déjà publiés
   sur la boutique en ligne depuis le 10/11 (invisibles tant qu'ils sont en
   brouillon).
3. Renommer « Offres du moment » en « Black Friday » et le faire pointer vers
   `/collections/black-friday`, dans les menus `menu-pc-2` et `menu-mobile`
   (les menus ne dépendent pas du thème : changement immédiat).
4. Créer le code du bon de 50 € et le bloc de l'e-mail de confirmation.
5. Vérifier l'accueil, la collection, les deux fiches et le panier sur mobile.

Après le 30/11 : republier le thème habituel, remettre le menu « Offres du
moment », dépublier la collection et repasser les deux packs en brouillon si
besoin.
