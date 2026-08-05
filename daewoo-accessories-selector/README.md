# Page accessoires — Daewoo Security

Refonte de `/collections/tous-les-accessoires` en page de **consolidation
premium** : un hero (titre, sous-titre, lien de défilement, image) suivi de
**quatre grandes rangées alternées** (une par centrale : Vigilia, Touch /
Touch XL, SA501 Key, PA501Z Elite), chacune avec un badge icône, un titre,
une accroche, un bouton d'action et une liste de 4 fonctionnalités
compatibles, puis un bandeau final « vous ne connaissez pas votre
centrale ? » avec deux boutons. Pas de grille produits sur cette page —
elle ne fait qu'aiguiller le client vers la bonne collection.

## Fichiers actuels (hero + 4 rangées alternées)

| Fichier | Statut | Rôle |
|---|---|---|
| `sections/daewoo-accessories-hub.liquid` | **Nouveau** | Hero (titre/sous-titre/lien de défilement/image) + boucle sur les 4 blocs de rangée + bandeau d'aide final. |
| `assets/daewoo-accessories-hub.css` | **Nouveau** | Hero 2 colonnes (ou centré si pas d'image), rangées alternées en grille 2 colonnes avec bordure fine et coins arrondis, bandeau d'aide teinté `--color-highlight`. Variables du thème uniquement. |
| `snippets/daewoo-hub-row.liquid` | **Nouveau** | Une rangée : image d'un côté, contenu de l'autre (badge, titre, accroche, CTA, 4 fonctionnalités). Le côté alterne automatiquement selon l'index. |
| `snippets/daewoo-hub-icon.liquid` | **Nouveau** | Jeu de 10 icônes SVG monoligne (bouclier, contact, clé, diamant, détecteur, sirène, télécommande, caméra, connectivité, réglages) — le thème n'a pas d'icônes du domaine sécurité. |
| `templates/collection.accessoires-hub.json` | **Nouveau** | Template dédié à `tous-les-accessoires` : 4 blocs (`card_vigilia`, `card_touch`, `card_key`, `card_elite`) avec vraies photos produit et vrais liens de collection. |
| `snippets/product-badges.liquid` | **Modifié** | Ajout de 4 lignes en fin de fichier pour le badge de compatibilité produit (voir section « Badges »). Indépendant du reste de ce livrable. |

Aucun JavaScript : navigation par vraies URLs de collection,
`prefers-reduced-motion` respecté en CSS.

## Déjà déployé — thème brouillon

Ces fichiers sont en ligne dans un thème **brouillon** dédié :
**« Sélecteur accessoires (Claude) »** (id `200542421332`) — dupliqué depuis
votre thème actif, donc zéro impact sur le site en ligne tant qu'il n'est
pas publié.

Aperçu direct :
```
https://daewoo-security.myshopify.com/admin/themes/200542421332/editor?template=collection.accessoires-hub&previewPath=%2Fcollections%2Ftous-les-accessoires
```

Les 4 rangées utilisent déjà vos vraies photos produit (Vigilia VIG501,
Touch AM301, SA501 Key, PA501Z Elite) et pointent vers vos vraies
collections :

- **Vigilia** → *Compatible gamme Vigilia / Touch*
- **Touch / Touch XL** → *Compatible gamme Vigilia / Touch* (même collection que Vigilia, rangée distincte visuellement)
- **SA501 Key** → *ACCESSOIRES KEY (SA501)*
- **PA501Z Elite** → *Compatible gamme Élite*

Les photos utilisées sont vos vraies photos produit (studio, fond neutre),
détourées sur un panneau clair dans chaque rangée. Ce ne sont pas des
photos « lifestyle » (produits en situation dans un intérieur) — aucune
photo de ce type n'existe actuellement dans votre bibliothèque Shopify.
Si vous en avez, elles peuvent remplacer les visuels actuels directement
depuis l'éditeur de thème (champ **Image** de chaque rangée).

## Installation manuelle (si besoin de la refaire ailleurs)

1. **Boutique en ligne → Thèmes → Modifier le code** : créez les 4 fichiers
   ci-dessus dans les bons dossiers, en collant le contenu correspondant.
2. Assignez `collection.accessoires-hub.json` à la collection
   `tous-les-accessoires` via **Réglages de la collection → Modèle de
   thème** (uniquement possible une fois le thème brouillon publié — voir
   plus bas).
3. Pour changer une URL ou une image : ouvrez la section dans l'éditeur de
   thème, chaque carte a ses propres champs **Image**, **Titre**,
   **Description**, **URL de la collection**. Rien n'est codé en dur.

## Passer ce thème brouillon en ligne

Deux actions restent à faire **avec votre accord explicite**, vu leur
impact sur le site en ligne :

1. Publier le thème brouillon (**Thèmes → ⋯ → Publier**) — remplace le
   thème actif.
2. Assigner le modèle `accessoires-hub` à la collection
   `tous-les-accessoires` (**Collection → Modèle de thème**).

Dites-le-moi quand vous voulez que je vous guide sur ces deux étapes, ou
que je les fasse pour vous.

## Badges de compatibilité (indépendant de cette page)

Vos produits ont déjà un métachamp `custom.compatibilite` qui alimente vos
collections intelligentes existantes. Le badge ajouté dans
`product-badges.liquid` lit directement cette même valeur et l'affiche sur
la carte produit native (ex. *« Compatible Vigilia & Touch »*). Un produit
sans cette valeur renseignée n'affiche simplement pas de badge — aucun
risque de casser l'affichage existant.

## Ancienne version (sélecteur premium 4 cartes + grille native)

Une première version plus riche — hero avec image, 4 cartes éditoriales
asymétriques, bandeau de réassurance, section d'identification, barre de
sélection rapide, le tout au-dessus de la grille produits native — reste
disponible dans ce dossier (`daewoo-accessories-selector.liquid` et ses
fichiers associés) si vous en avez besoin ailleurs, par exemple sur les 3
collections de gamme elles-mêmes plutôt que sur la page de consolidation.
Elle n'est plus utilisée par `collection.accessoires-hub.json`, qui pointe
maintenant vers la version sobre ci-dessus.
