# Page accessoires — Daewoo Security

Refonte de `/collections/tous-les-accessoires` en page de **consolidation** :
un court texte d'explication en haut, puis **trois visuels de compatibilité
fournis par vous** (un par groupe de centrale), empilés verticalement,
chacun entièrement cliquable vers la vraie collection correspondante. Les
visuels portent déjà leur propre titre, leurs photos produit et leurs
pictogrammes — cette page ne fait qu'un cadre, un lien et un ordre autour
d'eux, rien d'autre. Pas de grille produits ici — elle ne fait qu'aiguiller
le client vers la bonne collection.

## Fichiers actuels

| Fichier | Rôle |
|---|---|
| `sections/daewoo-accessories-hub.liquid` | Titre + texte d'explication, puis boucle sur les blocs `card` (un par visuel). CSS entièrement en ligne (`<style>` dans le fichier — voir « Pièges » ci-dessous pour pourquoi). |
| `snippets/daewoo-hub-image-link.liquid` | Un visuel = un seul `<a>` cliquable contenant l'image en entier, en haute résolution. |
| `templates/collection.accessories-hub.json` | Template dédié à `tous-les-accessoires` : 3 blocs (`card_elite`, `card_vigilia_touch`, `card_key`) avec les vraies images et les vrais liens de collection déjà renseignés. |
| `snippets/product-badges.liquid` *(modifié)* | Ajout de 4 lignes en fin de fichier pour le badge de compatibilité produit (voir section « Badges »). Indépendant du reste de ce livrable. |

Aucun JavaScript : navigation par vraies URLs de collection,
`prefers-reduced-motion` respecté en CSS.

## Vos 3 visuels

Déposés dans votre bibliothèque de fichiers Shopify, reliés dans le
template, dans cet ordre (haut → bas) :

| Ordre | Visuel | Lien |
|---|---|---|
| 1 | `Collection_Accessoires_Elite_PA501Z.png` | `/collections/gamme-elite-accessoires` |
| 2 | `Collection_Accessoires_Touch_Vigilia.png` | `/collections/compatible-gamme-vigilia-touch` |
| 3 | `Collection_Accessoires_SA501_Key.png` | `/collections/accessoires` |

## Déjà déployé — thème brouillon

**« Sélecteur accessoires v3 - correctif (Claude) »** (id `201280913748`) —
thème non publié, zéro impact sur le site en ligne tant qu'il n'est pas
publié.

Aperçu direct (thème brouillon + vraie collection) :
```
https://daewoo-security.myshopify.com/admin/themes/201280913748/editor?previewPath=%2Fcollections%2Ftous-les-accessoires
```
ou sur le vrai domaine (nécessite d'être connecté à l'admin dans le même
navigateur) :
```
https://daewoo-security.fr/collections/tous-les-accessoires?preview_theme_id=201280913748
```

## Pièges rencontrés (12/08) — à garder en tête pour la suite

Cette page a eu une mise au point inhabituellement longue. Plusieurs
causes réelles et distinctes se sont superposées :

1. **Nom de modèle** — la collection avait pour modèle assigné
   `accessories-hub` (anglais), notre fichier s'appelait
   `collection.accessoires-hub.json` (français). Ils ne correspondaient
   jamais → page par défaut silencieusement. Corrigé en renommant le
   fichier.
2. **`{% doc %}` non supporté** — la balise Liquid `{% doc %}...{% enddoc %}`
   (documentation de section, relativement récente) faisait échouer le
   rendu de **toute la section, silencieusement, sans la moindre erreur**
   sur cette boutique. Remplacée partout par `{% comment %}`.
3. **Collision de noms de classes CSS** — la cause la plus sournoise :
   réutiliser les noms de classes du thème (`section`, `section--padding`,
   `page-width`) sur nos propres éléments faisait échouer le rendu de la
   section, encore une fois silencieusement. Nos classes utilisent
   maintenant des noms qui ne collisionnent avec rien du thème
   (`daewoo-hub-wrap`, `daewoo-hub-container`, etc.), et le fichier CSS a
   été rapatrié **en ligne dans la section** (plus de fichier `.css`
   séparé) pour éliminer tout risque de timing de chargement.
4. **Flou du texte dans les images** — une fois le rendu débloqué, le
   texte à l'intérieur des visuels restait flou quelle que soit la taille
   du cadre CSS : l'attribut `sizes` de l'image demandait au navigateur
   une version basse résolution (pensée pour un affichage à 380px), donc
   il chargeait un fichier trop petit et l'étirait. Corrigé en mettant
   `sizes: '100vw'`.

Si un futur ajout à cette boutique (section personnalisée, snippet) se
retrouve à rendre une page blanche sans erreur, revérifier ces 3 pistes
en premier : balises Liquid récentes (`{% doc %}` et assimilées), noms de
classes CSS qui collisionnent avec le thème, et l'attribut `sizes` des
images qui ne matche pas leur taille d'affichage réelle.

## Installation manuelle (si besoin de la refaire ailleurs)

1. **Boutique en ligne → Thèmes → Modifier le code** : créez les fichiers
   ci-dessus dans les bons dossiers, en collant le contenu correspondant.
2. Vérifiez que la collection cible a bien pour modèle `accessories-hub`
   (**Réglages de la collection → Modèle de thème**).
3. Pour changer un lien ou une image : ouvrez le bloc concerné dans
   l'éditeur de thème, champs **Image** et **Lien vers la collection**.
   Rien n'est codé en dur.
4. Pour ajuster la taille des visuels : dans
   `sections/daewoo-accessories-hub.liquid`, la règle `.daewoo-hub__grid`
   contrôle la largeur maximale (actuellement `1020px`).

## Passer ce thème brouillon en ligne

Je ne peux pas publier le thème moi-même (action bloquée par sécurité).
Pour publier :

1. **Boutique en ligne → Thèmes** → trouvez « Sélecteur accessoires v3 -
   correctif (Claude) » dans la liste des brouillons → **⋯ → Publier**.
2. Rien d'autre à faire côté modèle : la collection pointe déjà vers
   `accessories-hub`, qui existera automatiquement dès la publication.

⚠️ Ce brouillon a été dupliqué depuis le thème alors en ligne
(« Brouillon - Pages dédiées VIG501 à VIG507 (Claude) »). Si ce thème a
été modifié depuis la duplication, ces modifications ne seraient pas
présentes dans ce brouillon et publier les écraserait.

## Badges de compatibilité (indépendant de cette page)

Vos produits ont déjà un métachamp `custom.compatibilite` qui alimente vos
collections intelligentes existantes. Le badge ajouté dans
`product-badges.liquid` lit directement cette même valeur et l'affiche sur
la carte produit native (ex. *« Compatible Vigilia & Touch »*). Un produit
sans cette valeur renseignée n'affiche simplement pas de badge — aucun
risque de casser l'affichage existant.

## Anciennes versions (conservées au cas où)

Une itération précédente reste dans ce dossier au cas où vous en auriez
besoin ailleurs sur le site : `daewoo-accessories-selector.liquid` et ses
fichiers associés (`daewoo-identify-card.liquid`,
`daewoo-range-card.liquid`, `daewoo-accessories-selector.css`) — hero avec
image, 4 cartes éditoriales, bandeau de réassurance, section
d'identification, barre de sélection rapide, au-dessus de la grille
produits native. Elle n'est plus utilisée par
`collection.accessories-hub.json`, qui pointe maintenant vers la version
à 3 visuels ci-dessus.
