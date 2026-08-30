# Fiches accessoires passées au modèle premium

Thème d'aperçu : « Fiche accessoire uniformisee v1 (Claude) » — `202527113556`

| Réf. | Produit | Template | Titre de page |
|---|---|---|---|
| WDV301 | Contacteur d'ouverture / vibration 2-en-1 | `accessoires-sans-details` | Deux détections. Un seul capteur. |
| WVD301 | Détecteur de vibration | `accessoires` | Le choc suffit. |
| WDG301 | Contacteur de porte de garage | `accessoires` | Le garage aussi est une porte d'entrée. |
| WPS305 | Détecteur de mouvement animaux | `accessoires` | Il voit l'intrus, pas le chat. |
| WMO301 | Détecteur de mouvement extérieur | `accessoires` | La détection commence avant la porte. |
| WSD301 | Détecteur de fumée connecté | `accessoires` | 85 dB dans la maison. Une alerte dans votre poche. |
| BIR301 | Barrières infrarouge | `accessoires-sans-details` | Franchir le faisceau suffit. |
| WWF301 | Détecteur de fuite d'eau | `accessoires` | Les premières gouttes suffisent. |

Pour chaque fiche : type de produit Shopify, `titre_page`, `accroche`,
`conseil_quantite`, `note_compatibilite`, métaobjet `bandeau_caracteristiques`,
textes alternatifs des visuels, balises SEO et description longue.

## Points de vigilance relevés

- Les descriptions annonçaient souvent « Compatible TOUCH / TOUCH XL » sans
  mentionner Vigilia, alors que ces accessoires le sont. Corrigé au fil des fiches.
- Pile du WDG301 : CR2032 (le métachamp indiquait CR2450).
- `contenu_du_pack` valait « Accessoire / Adhésive de fixation / Manuel » sur
  toute la gamme. Remplacé par le contenu réel, fiche par fiche.

## WMO301 — avertissement d'exposition au soleil

Le capteur ne doit jamais être orienté face aux rayons du soleil : la variation
brutale de chaleur sur la lentille est interprétée comme un mouvement et provoque
de fausses détections. L'avertissement figure à trois endroits de la fiche —
description (« Où l'installer »), volet « Sécurité et détection », et ligne
« Pose » de la fiche technique.

La consigne ne concerne que les détecteurs d'extérieur : le WPS305 est un
modèle d'intérieur. Reste à vérifier sur le WMO501.

## WSD301 — données complétées

Le métachamp « Alimentation / Autonomie » contenait un argument commercial
(« Sécurité permanente… ») au lieu des données attendues. Complété depuis :

- alimentation : 1 pile CR123A longue autonomie (durée volontairement non chiffrée) ;
- certification : EN 14604 ;
- pose : visserie et kit de fixation inclus.

La pile CR123A est fournie avec le produit. Restent à confirmer : les dimensions.

## BIR301 — balise titre absente

Le produit n'avait aucune balise titre SEO (`seo.title` vide) : Google reprenait
le titre brut du produit. Une balise a été rédigée.

Ses caractéristiques (portée de 10 m, IP66, dimensions 33 x 3,5 cm, 4 piles
ER15505H 3,6 V incluses, autonomie de 2 ans, anti-démontage) étaient présentes
dans les métachamps mais peu visibles sur la page ; elles remontent dans la
fiche technique.

Piles fournies, comme celle du WSD301 : indiqué dans le contenu de la boîte.

## Bandeau « Complétez votre système »

Les recommandations automatiques de Shopify piochaient dans tout le catalogue et
remontaient des centrales d'alarme. Elles sont remplacées par
`sections/acc-complements.liquid`, qui affiche les autres produits de la
collection **« Compatible … »** à laquelle appartient le produit courant — donc
toujours la même gamme. Sans collection de ce type, la section reste masquée
plutôt que d'afficher une gamme étrangère.

La section écarte aussi les doublons « Configurateur | … » et accepte une liste
de handles à exclure.

### Donnée à corriger

Les centrales **Touch AM301** (`centrale-touch-am301-avec-ecran-tactile-4-3`) et
**Touch XL AM302** (`centrale-am302`) portent le métachamp
`custom.categorie_de_produit` = « Accessoires ». Elles entrent donc dans la
collection « Compatible gamme Vigilia / Touch », qui sert de source au bandeau.
Elles sont écartées par la liste d'exclusions, mais la vraie correction est de
changer leur catégorie — à valider, car cela les retirerait aussi de la page de
cette collection.

## WWF301 — éléments manquants

Deux sections de la fiche resteront masquées tant que les données n'existent pas :

- **FAQ produit** : le métachamp `custom.faq` n'est pas renseigné (aucun métaobjet
  `faq_produit` pour cette référence). C'est le seul des huit produits traités
  dans ce cas.
- **Lien vers le manuel** : `custom.manuel_produit` est vide.

Le titre du produit annonçait « Compatible Touch (AM301/AM302) » sans Vigilia,
alors que la description et le métachamp de compatibilité l'incluent. Aligné sur
la convention de la gamme : « | Compatible Touch/Vigilia (AM30x) ». L'URL du
produit est inchangée.
