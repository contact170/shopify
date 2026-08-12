# Page accessoires — Daewoo Security

Refonte de `/collections/tous-les-accessoires` en page de **consolidation** :
un court texte d'explication en haut, puis **trois visuels de compatibilité
fournis par vous** (un par groupe de centrale), chacun entièrement cliquable
vers la vraie collection correspondante. Les visuels portent déjà leur
propre titre, leurs photos produit et leurs pictogrammes — cette page ne
fait qu'un cadre, un lien et un ordre autour d'eux, rien d'autre. Pas de
grille produits ici — elle ne fait qu'aiguiller le client vers la bonne
collection.

## Fichiers actuels (3 visuels cliquables)

| Fichier | Statut | Rôle |
|---|---|---|
| `sections/daewoo-accessories-hub.liquid` | **Nouveau** | Titre + texte d'explication, puis boucle sur les blocs `card` (un par visuel). |
| `assets/daewoo-accessories-hub.css` | **Nouveau** | Grille de 3 colonnes (1 colonne sous 900px), coins arrondis, ombre douce, léger effet de survol. Aucun texte ajouté sur les images. |
| `snippets/daewoo-hub-image-link.liquid` | **Nouveau** | Un visuel = un seul `<a>` cliquable contenant l'image en entier. |
| `templates/collection.accessoires-hub.json` | **Nouveau** | Template dédié à `tous-les-accessoires` : 3 blocs (`card_elite`, `card_key`, `card_vigilia_touch`) avec les vrais liens de collection déjà renseignés. |
| `snippets/product-badges.liquid` | **Modifié** | Ajout de 4 lignes en fin de fichier pour le badge de compatibilité produit (voir section « Badges »). Indépendant du reste de ce livrable. |

Aucun JavaScript : navigation par vraies URLs de collection,
`prefers-reduced-motion` respecté en CSS.

## Vos 3 visuels — à déposer vous-même

Je n'ai pas pu récupérer les 3 images que vous avez partagées dans la
conversation (elles n'existent pas comme fichiers accessibles de mon
côté). Le champ **Image** de chaque bloc est prêt à les recevoir — il
suffit de :

1. Ouvrir l'éditeur de thème sur le thème brouillon (lien ci-dessous).
2. Cliquer sur la section **Daewoo — Hub accessoires**, puis sur chacun
   des 3 blocs **Visuel compatibilité**.
3. Cliquer sur **Sélectionner une image** et déposer le fichier
   correspondant.

Les 3 blocs sont déjà dans le bon ordre, avec les bons liens et un texte
alternatif d'accessibilité pré-rempli :

| Bloc | Visuel attendu | Lien |
|---|---|---|
| 1 | Infographie **PA501Z Elite** | `/collections/gamme-elite-accessoires` |
| 2 | Infographie **SA501 Key** | `/collections/accessoires` |
| 3 | Infographie **Vigilia · Touch · Touch XL** | `/collections/compatible-gamme-vigilia-touch` |

## Déjà déployé — thème brouillon

Ces fichiers sont en ligne dans un thème **brouillon** dédié :
**« Sélecteur accessoires (Claude) »** (id `200542421332`) — dupliqué depuis
votre thème actif, donc zéro impact sur le site en ligne tant qu'il n'est
pas publié.

Aperçu direct :
```
https://daewoo-security.myshopify.com/admin/themes/200542421332/editor?template=collection.accessoires-hub&previewPath=%2Fcollections%2Ftous-les-accessoires
```

## Installation manuelle (si besoin de la refaire ailleurs)

1. **Boutique en ligne → Thèmes → Modifier le code** : créez les fichiers
   ci-dessus dans les bons dossiers, en collant le contenu correspondant.
2. Assignez `collection.accessoires-hub.json` à la collection
   `tous-les-accessoires` via **Réglages de la collection → Modèle de
   thème** (uniquement possible une fois le thème brouillon publié — voir
   plus bas).
3. Déposez vos 3 images comme décrit ci-dessus. Pour changer un lien :
   champ **Lien vers la collection** du bloc concerné. Rien n'est codé en
   dur.

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

## Anciennes versions (conservées au cas où)

Deux itérations précédentes restent dans ce dossier au cas où vous en
auriez besoin ailleurs sur le site :

- `daewoo-accessories-selector.liquid` et fichiers associés — hero avec
  image, 4 cartes éditoriales, bandeau de réassurance, section
  d'identification, barre de sélection rapide, au-dessus de la grille
  produits native.
- `snippets/daewoo-identify-card.liquid`, `snippets/daewoo-range-card.liquid`
  — blocs de la version ci-dessus.

Aucune des deux n'est plus utilisée par `collection.accessoires-hub.json`,
qui pointe maintenant vers la version à 3 visuels ci-dessus.
