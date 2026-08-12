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
| `templates/collection.accessories-hub.json` | **Nouveau** | Template dédié à `tous-les-accessoires` : 3 blocs (`card_elite`, `card_key`, `card_vigilia_touch`) avec les vrais liens de collection et les 3 images déjà renseignés. |
| `snippets/product-badges.liquid` | **Modifié** | Ajout de 4 lignes en fin de fichier pour le badge de compatibilité produit (voir section « Badges »). Indépendant du reste de ce livrable. |

Aucun JavaScript : navigation par vraies URLs de collection,
`prefers-reduced-motion` respecté en CSS.

## Vos 3 visuels

Vous les avez déposés dans votre bibliothèque de fichiers Shopify et
partagé les 3 URL — ils sont déjà reliés dans le template :

| Bloc | Visuel | Lien |
|---|---|---|
| 1 | `Collection_Accessoires_Elite_PA501Z.png` | `/collections/gamme-elite-accessoires` |
| 2 | `Collection_Accessoires_SA501_Key.png` | `/collections/accessoires` |
| 3 | `Collection_Accessoires_Touch_Vigilia.png` | `/collections/compatible-gamme-vigilia-touch` |

## Déjà déployé — thème brouillon

Ces fichiers sont en ligne dans un thème **brouillon** dédié :
**« Sélecteur accessoires v2 (Claude) »** (id `201278226772`) — un thème
non publié, donc zéro impact sur le site en ligne tant qu'il n'est pas
publié.

**Historique des deux pièges rencontrés (12/08) :**

1. La collection `tous-les-accessoires` a un modèle réellement assigné,
   `accessories-hub` (en anglais) — probablement choisi par inadvertance
   dans le sélecteur de modèle de l'éditeur. Notre fichier s'appelait
   `collection.accessoires-hub.json` (en français) : les deux noms ne
   correspondaient jamais. Corrigé en renommant le fichier en
   `templates/collection.accessories-hub.json`.
2. Le premier thème brouillon (id `200542421332`, maintenant abandonné)
   avait été dupliqué il y a plusieurs semaines depuis un thème qui n'est
   plus celui en ligne aujourd'hui — l'aperçu affichait une page
   entièrement blanche, signe d'un problème global au brouillon
   lui-même, indépendant de cette page. Corrigé en dupliquant un nouveau
   brouillon depuis le thème **réellement publié aujourd'hui**
   (« Brouillon - Pages dédiées VIG501 à VIG507 (Claude) ») et en y
   redéployant les mêmes fichiers.

Aperçu direct :
```
https://daewoo-security.myshopify.com/admin/themes/201278226772/editor?previewPath=%2Fcollections%2Ftous-les-accessoires
```

## Installation manuelle (si besoin de la refaire ailleurs)

1. **Boutique en ligne → Thèmes → Modifier le code** : créez les fichiers
   ci-dessus dans les bons dossiers, en collant le contenu correspondant.
2. Vérifiez que la collection `tous-les-accessoires` a bien pour modèle
   `accessories-hub` (**Réglages de la collection → Modèle de thème**) —
   c'est déjà le cas actuellement, pas d'action nécessaire.
3. Pour changer un lien ou une image : ouvrez le bloc concerné dans
   l'éditeur de thème, champs **Image** et **Lien vers la collection**.
   Rien n'est codé en dur.

## Passer ce thème brouillon en ligne

Deux actions restent à faire **avec votre accord explicite**, vu leur
impact sur le site en ligne :

1. Publier le thème brouillon (**Thèmes → ⋯ → Publier**) — remplace le
   thème actuellement actif (à ce jour : « Brouillon - Pages dédiées
   VIG501 à VIG507 (Claude) »).
2. Rien d'autre à faire côté modèle : la collection pointe déjà vers
   `accessories-hub`, qui existera automatiquement dès la publication.

Dites-le-moi quand vous voulez que je vous guide sur cette étape, ou
que je la fasse pour vous.

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

Aucune des deux n'est plus utilisée par `collection.accessories-hub.json`,
qui pointe maintenant vers la version à 3 visuels ci-dessus.
