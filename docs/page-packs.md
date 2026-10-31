# Page « Packs alarme » (remplace l'iframe Lovable)

Nouvelle page de présentation des 6 packs de la gamme 2026 (choix de la
centrale) et des 5 packs Élite, rendue par le thème Shopify au lieu de
l'application Lovable affichée dans une iframe sur `/pages/pack-alarmes`.

## Fichiers

| Fichier | Rôle |
|---|---|
| `theme/sections/dw-page-packs.liquid` | Section complète : en-tête, conseiller en 3 questions, choix de la centrale, 6 cartes, comparatif, packs Élite, réassurance, FAQ, données structurées (FAQPage, ItemList) |
| `theme/templates/page.packs-alarme.json` | Modèle de page avec tous les blocs remplis (4 centrales, 6 packs, 5 packs Élite, 8 questions) |

Les deux fichiers sont installés dans le thème non publié
« Gamme packs 6x4 - dev (Claude) » (`gid://shopify/OnlineStoreTheme/207470788948`),
celui du lancement de la gamme. Aucun fichier existant n'y a été modifié.

## D'où viennent les données

Rien n'est recopié à la main dans la section :

- **6 packs** (produits étiquetés `gamme-packs-2026`) : prix et disponibilité
  de chaque variante (option « Centrale »), photo de la variante, prix barré
  = métachamp de variante `custom.prix_reference` (même règle que la fiche
  `pack-gamme`), contenu = `custom.contenu_pack`, « idéal pour » =
  `custom.ideal_pour`, caméras extérieures = `custom.cameras_exterieures`.
  Les chiffres du comparatif sont comptés à partir de `custom.contenu_pack`.
- **Packs Élite** (PA570 à PA574) : prix, photo, référence et
  `custom.nb_accessoires` lus sur le produit. Leur contenu est saisi dans le
  bloc « Pack Élite » (une ligne `quantité|libellé`), car ces produits n'ont
  pas de métachamp `custom.contenu_pack` ; s'il est rempli un jour, il est
  utilisé à la place.
- **Note des avis** : `snippets/pv-avis-vigilia.liquid` en mode `stats`
  (mêmes avis que les fiches packs), arrondie vers le bas.
- **Mises en avant** (données de ventes sur 90 jours au 31/10/2026) :
  l'ancienne offre Sécurité Intégrale est le pack le plus vendu de cette
  gamme (38 commandes), d'où la pastille « Recommandé » ; Tranquillité+
  (PA574) est le pack Élite le plus vendu (25 commandes).

## Fonctionnement

- Choix de la centrale (Vigilia, Vigilia +, Touch, Touch XL) : change d'un
  coup prix, prix barrés, photos, liens, variante ajoutée au panier, ligne
  « badges RFID » (Vigilia et Vigilia + seulement) et prix du comparatif.
  `?centrale=vigilia-plus` dans l'adresse présélectionne une centrale ; les
  liens vers les fiches passent la centrale choisie (`?centrale=…`).
- Conseiller : logement (3, 5 ou 8 ouvertures), caméras extérieures (0, 1
  ou 2), centrale ou gamme Élite. Score = écart de contacteurs × 10 +
  caméra manquante × 40 + caméra en trop × 20 + prix / 50 €. Affiche le
  pack retenu avec la bonne variante, et une autre option.
- « Ajouter au panier » : `/cart/add.js` puis ouverture du tiroir panier
  (même code que la fiche `pack-gamme`).
- Un produit en brouillon est ignoré sur la boutique. Les 6 packs étant en
  brouillon au 31/10/2026, l'aperçu du thème n'affiche pour l'instant que
  l'en-tête, le conseiller limité à l'Élite et les packs Élite.

## Mise en ligne

1. Publier les 6 produits de la gamme (statut Actif, canal Boutique en ligne).
2. Vérifier l'aperçu :
   `https://daewoo-security.fr/pages/pack-alarmes?view=packs-alarme&preview_theme_id=207470788948`
3. Publier le thème « Gamme packs 6x4 - dev (Claude) » (ou copier les deux
   fichiers dans le thème publié).
4. Dans Shopify › Boutique en ligne › Pages › « pack alarmes », choisir le
   modèle `packs-alarme` (à faire seulement après l'étape 3, sinon la page
   retombe sur le modèle par défaut). Le contenu de la page (l'iframe
   Lovable) n'est plus affiché par ce modèle ; il peut être vidé.

## Vérifié avant livraison

Rendu local de la section (liquidjs) avec les vraies données des 11
produits, injecté dans la page réelle du site (en-tête, pied de page et CSS
du thème), captures ordinateur et mobile, aucun débordement horizontal,
aucune erreur JavaScript. Tests automatiques : choix de centrale (prix,
prix barrés, variantes, liens, badges RFID, comparatif) et 5 parcours du
conseiller.
