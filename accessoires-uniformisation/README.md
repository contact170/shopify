# Uniformisation des fiches accessoires

Premier jalon : fiche **WDV301** (contacteur d'ouverture / vibration 2-en-1),
prise comme modèle pour l'ensemble des pages accessoires.

Thème d'aperçu (non publié) : **« Fiche accessoire uniformisee v1 (Claude) »**
`gid://shopify/OnlineStoreTheme/202527113556`

Le thème publié n'est pas modifié : tout est visible en prévisualisation avant
publication.

## Structure cible d'une fiche accessoire

1. **Bloc identité** en haut de la buy box : type d'accessoire, référence (SKU),
   compatibilité. Piloté par les données produit, donc identique sur toutes les fiches.
2. Badges « à quoi ça sert » (métaobjet `a_quoi_ca_sert`).
3. Lien « Télécharger le manuel d'utilisation (PDF) » (métachamp `manuel_produit`).
4. Section **Son rôle dans votre sécurité** (3 visuels + métaobjet `a_quoi_ca_sert`).
5. Section **Installation simple** (vidéo du métachamp `video_installation`).
6. **Détails produit** — onglets branchés sur des métachamps réels :
   Sécurité & détection · Connectivité & compatibilité · Alimentation & autonomie ·
   Caractéristiques générales · Contenu de la boîte · icônes « Inclus dans la boîte ».
7. **Fiche technique** — tableau clé/valeur (métaobjet `bandeau_caracteristiques`).
8. **FAQ produit** — questions propres au produit (métaobjet `faq_produit`) + balisage
   `FAQPage` (JSON-LD).
9. FAQ générique accessoires, avis Judge.me, produits récemment consultés.

Toutes les nouvelles sections sont conditionnées à la présence du métachamp :
une fiche non encore renseignée n'affiche simplement pas la section.

## Fichiers

| Fichier | Rôle |
|---|---|
| `templates/product.accessoires-sans-details.json` | Template accessoire uniformisé |
| `sections/acc-fiche-technique.liquid` | Tableau « Fiche technique » |
| `sections/acc-faq-produit.liquid` | FAQ propre au produit + JSON-LD FAQPage |
| `snippets/acc-faq-item.liquid` | Rendu d'une question/réponse |

## Corrections apportées au template

- Les onglets « Image & vidéo » et « Dimensions » pointaient vers des métachamps
  vides : ils s'affichaient vides sur toutes les fiches. Remplacés par des onglets
  utiles, et le contenu n'est plus enveloppé dans `<p></p>` afin qu'un onglet sans
  donnée disparaisse au lieu de s'afficher vide.
- Le métachamp `custom.securite_detection` était renseigné mais affiché nulle part :
  une définition de métachamp a été créée et l'onglet correspondant ajouté.
- Suppression, dans ce template uniquement, des sections **désactivées** (invisibles)
  héritées des pages caméras / abonnement cloud. Le thème publié les conserve.

## Reste à faire pour généraliser

- Renseigner par accessoire : `bandeau_caracteristiques`, `faq` (métaobjet `faq_produit`),
  `securite_detection`, `caracteristiques_generales`, `contenu_du_pack`, `manuel_produit`,
  `video_installation`, ainsi que le type de produit Shopify et le SKU.
- Reporter la même structure sur les templates `product.accessoires.json` et
  `product.accesoires-sans-videos.json`.
