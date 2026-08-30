# Fiches accessoires — modèle premium

Thème d'aperçu (non publié) : **« Fiche accessoire uniformisee v1 (Claude) »**
`gid://shopify/OnlineStoreTheme/202527113556`

Le thème publié n'est pas modifié.

## Principe

La fiche accessoire est entièrement reconstruite : mise en page aérée, grande
typographie, photographie produit isolée, tableaux en filets fins. Chaque
section est pilotée par les données du produit et **disparaît si le métachamp
correspondant est vide** — une fiche non renseignée n'affiche jamais de bloc vide.

## Sections de la page (dans l'ordre)

| Section | Fichier | Source des données |
|---|---|---|
| En-tête, galerie, achat | `sections/acc-hero.liquid` | `custom.titre_page`, `custom.accroche`, `product.type`, SKU, `custom.compatibilite`, `custom.conseil_quantite`, images produit, note Judge.me |
| Son rôle (bande sombre animée) | `sections/acc-chrono.liquid` | `custom.a_quoi_ca_sert` |
| Installation + manuel | `sections/acc-installation.liquid` | `custom.video_installation`, `custom.manuel_produit` |
| Compatibilité | `sections/acc-compat.liquid` | `custom.compatibilite`, `custom.note_compatibilite` |
| Fiche technique | `sections/acc-fiche-technique.liquid` | `custom.bandeau_caracteristiques` |
| Dans la boîte | `sections/acc-boite.liquid` | `custom.contenu_du_pack` |
| Note clients | `sections/acc-avis.liquid` | `reviews.rating`, `reviews.rating_count` |
| Avis Judge.me | section `apps` | widget Judge.me |
| FAQ produit + JSON-LD FAQPage | `sections/acc-faq-produit.liquid` | `custom.faq` (métaobjet `faq_produit`) |

Styles et scripts communs : `assets/acc-premium.css`, `assets/acc-premium.js`.

## Zone d'achat

- Sélecteur de quantité, total calculé dès 2 pièces.
- Conseil de quantité issu de `custom.conseil_quantite` (ex. baie vitrée à deux
  vantaux = deux détecteurs).
- L'en-tête accepte des blocs d'application : y déposer le widget **Alma** ou le
  badge **Judge.me** depuis l'éditeur de thème.
- Le balisage `Product` (prix, stock, note) est réémis par `acc-hero`.

## Métachamps créés pour ce modèle

`custom.titre_page`, `custom.accroche`, `custom.conseil_quantite`,
`custom.note_compatibilite`, `custom.securite_detection` (définition),
plus le métaobjet `bandeau_caracteristiques` du WDV301.

## Limites connues

- L'ajout au panier passe par un envoi de formulaire classique : il ouvre la
  page panier au lieu du tiroir latéral du thème. À rebrancher sur le composant
  du thème si vous gardez ce modèle.
- Le rendu n'a pas pu être vérifié depuis l'environnement de développement
  (accès sortant vers la boutique bloqué) : à contrôler dans l'aperçu.

## Reste à faire pour généraliser

Renseigner par accessoire : `titre_page`, `accroche`, `conseil_quantite`,
`note_compatibilite`, `bandeau_caracteristiques`, `faq`, `contenu_du_pack`,
`video_installation`, `manuel_produit`, le type de produit et le SKU.
Puis appliquer le même modèle aux templates `product.accessoires.json` et
`product.accesoires-sans-videos.json`.
