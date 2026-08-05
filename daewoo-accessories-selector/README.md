# Page accessoires — Daewoo Security

Refonte de `/collections/tous-les-accessoires` en page de **consolidation** :
un titre court et trois cartes sobres qui renvoient chacune vers la vraie
collection d'accessoires correspondante. Pas de grille produits sur cette
page — elle ne fait qu'aiguiller le client vers la bonne page en un coup
d'œil.

## Fichiers actuels (page de consolidation)

| Fichier | Statut | Rôle |
|---|---|---|
| `sections/daewoo-accessories-hub.liquid` | **Nouveau** | Titre + sous-titre courts, puis 3 cartes égales. |
| `assets/daewoo-accessories-hub.css` | **Nouveau** | Style sobre : bordures fines, une seule couleur d'accent (`--color-highlight`, au survol uniquement), pas d'ombre ni de dégradé lourd. Variables du thème uniquement. |
| `snippets/daewoo-hub-card.liquid` | **Nouveau** | Une carte : image entière sur fond neutre (jamais recadrée), titre, description courte, lien. Toute la carte est un seul `<a>`. |
| `templates/collection.accessoires-hub.json` | **Nouveau** | Template dédié à `tous-les-accessoires` — uniquement cette section, rien d'autre. |
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

Les 3 cartes utilisent déjà vos vraies photos produit (Touch AM301, SA501
Key, PA501Z Elite) et pointent vers vos 3 vraies collections :

- **Vigilia & Touch / Touch XL** → *Compatible gamme Vigilia / Touch*
- **SA501 Key** → *ACCESSOIRES KEY (SA501)*
- **PA501Z Elite** → *Compatible gamme Élite*

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
