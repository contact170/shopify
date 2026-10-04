# Pages domotique au design « premium » — 04/10/2026

Refonte des fiches produit et des pages de collection sur le modèle de la fiche
du canon à fumée F502W (gabarit `product.acc-premium`, piloté par métachamps).

## 1. Fiches produit — EN LIGNE (données Shopify)

Gabarit `acc-premium` appliqué. Pour chaque produit, les éléments suivants ont été renseignés :
type de produit (utilisé dans le H1 « Daewoo {type} {référence} »), titre de page, accroche,
conseil d'achat, note de compatibilité, fiche technique (métaobjet `bandeau_caracteristiques`),
FAQ (métaobjet `faq_produit`, balisage FAQPage), bloc « Son rôle » (`a_quoi_ca_sert`),
contenu de la boîte, accordéons techniques, description longue (H2/H3, liste « En bref »),
titre et méta-description SEO, textes alternatifs des images.

| Produit | Handle | Métaobjets créés |
|---|---|---|
| Visiophone DB502W | `visiophone-avec-sonnette-interieure-db502w` | bandeau `db502w`, faq `db502w` |
| Recharge F502R | `recharge-f502r-pour-canon-a-fumee-f502w` | bandeau `f502r`, faq `f502r`, rôle `recharge-f502r`, compatibilité `canon-a-fumee-f502w` |
| Interrupteur 2 zones ILC502W | `interrupteur-connecte-pour-lumiere-2-zones` | bandeau `ilc502w`, faq `ilc502w` |
| Interrupteur 1 zone ILC501W | `interrupteur-connecte-pour-lumiere-1-zone-copie` | bandeau `ilc501w`, faq `ilc501w` |
| Distributeur NutriVision 501C | `distributeur-de-croquettes-connecte-avec-camera-nutrivision-501c` | bandeau `nutrivision-501c`, faq `nutrivision-501c` |
| Montre SW101 | `montre-connectee-sw101` | bandeau `sw101`, faq `sw101` |

Métaobjets « rôle » existants réécrits : `visiophone`, `interrupteur-lumiere` (partagé par les
deux interrupteurs), `distributeur-de-croquette`, `montre-connectee`.

Médias conservés : toutes les images produit restent attachées. La vidéo YouTube du NutriVision
est intégrée dans la description (bloc « En détail »). Le visuel lifestyle du DB502W, qui
n'était référencé que par un métachamp de l'ancien gabarit, est repris dans sa description.

## 2. Thème — copie à prévisualiser puis publier

Thème : **« Version finale 04102026 + pages domotique (Claude) »**
(`gid://shopify/OnlineStoreTheme/205103432020`), copie du thème publié du 04/10/2026.

| Fichier | Changement |
|---|---|
| `templates/collection.eclairage-prises-connectees.json` | Nouveau : hero, vitrine de la gamme (3 cartes), 4 arguments, grille produits, FAQ (FAQPage) |
| `templates/list-collections.json` | Visuels produits actuels par collection (bloc « image »), H1 « Toutes nos collections » |
| `sections/acc-hero.liquid` | Galerie : 10 vignettes au lieu de 6 (DB502W en a 9, NutriVision 7) |

La collection `eclairage-prises-connectees` utilise déjà le modèle `eclairage-prises-connectees` :
tant que la copie n'est pas publiée, Shopify affiche le modèle de collection par défaut.

## 3. SEO des collections — EN LIGNE

- `eclairage-prises-connectees` : titre, méta-description, description.
- `dissuasion` : la méta-description parlait d'autocollants ; elle décrit désormais le canon à fumée et sa recharge.
- `compagnons-connectes` : la méta-description mentionne désormais le distributeur NutriVision.

## À vérifier côté métier

- Contenu des boîtes : interrupteurs (« adhésif de fixation » retiré, car il ne correspond pas à
  un appareillage encastré), NutriVision (« alimentation secteur » ajoutée).
- Montre SW101 : la compatibilité Vigilia est annoncée (l'ancienne fiche ne citait que Key, Touch et Élite).
- Interrupteurs : il est indiqué qu'ils restent utilisables à la main (commande locale), ce qui est le fonctionnement habituel de ce type d'appareil.
