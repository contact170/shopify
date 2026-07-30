# Sélecteur d'accessoires — Daewoo Security

Refonte de `/collections/tous-les-accessoires` : un sélecteur de centrale premium
(Vigilia / Touch & Touch XL / SA501 Key / PA501Z Elite) au-dessus de la grille
produits **native** du thème Impact (Maestrooo), inchangée.

## Fichiers

| Fichier | Statut | Rôle |
|---|---|---|
| `sections/daewoo-accessories-selector.liquid` | **Nouveau** | Hero, sélecteur 4 cartes, réassurance, identification, transition + barre de sélection rapide. |
| `assets/daewoo-accessories-selector.css` | **Nouveau** | Tout le style. Utilise les variables CSS existantes du thème (`--color-foreground`, `--sp-*`, `--animation-primary`, `--rounded-full`…) — aucune couleur ni espacement codé en dur. |
| `snippets/daewoo-range-card.liquid` | **Nouveau** | Une des 4 grandes cartes lifestyle (image + texte + CTA), toute la carte est un seul `<a>` sémantique. |
| `snippets/daewoo-identify-card.liquid` | **Nouveau** | Carte compacte de la section « Vous ne connaissez pas votre centrale ? », réutilise les réglages de la carte correspondante. |
| `snippets/product-badges.liquid` | **Modifié** | Ajout de 4 lignes en fin de fichier pour afficher le badge de compatibilité. Le reste du fichier est inchangé — copiez uniquement le bloc marqué `Daewoo —` si vous avez modifié ce fichier depuis. |

Aucun fichier JavaScript n'a été nécessaire : navigation par vraies URLs de
collection, défilement doux en CSS (`scroll-behavior: smooth`), état actif de
la barre de sélection calculé côté serveur (Liquid), `prefers-reduced-motion`
respecté en CSS.

## 1. Installation dans le thème

1. Dans l'admin Shopify : **Boutique en ligne → Thèmes → Impact → Modifier le code**.
2. Créez les 4 nouveaux fichiers ci-dessus dans les bons dossiers (`Add a new section/asset/snippet`), en collant le contenu correspondant.
3. Ouvrez `snippets/product-badges.liquid` existant et collez le bloc ajouté en fin de fichier (juste avant le `</div>` final) — ne remplacez pas le reste du fichier.

## 2. Ajouter la section au template de collection

1. **Éditeur de thème → Collection par défaut** (ou le template spécifique utilisé par `tous-les-accessoires` si vous en avez un dédié).
2. **Ajouter une section** → choisissez *Daewoo — Sélecteur accessoires*. Placez-la **au-dessus** de la section *Collection principale* (grille produits native).
3. Elle arrive pré-remplie (voir `presets`) : hero, 4 cartes, 4 avantages de réassurance — vous n'avez qu'à ajouter les images.

Répétez l'étape sur les templates des collections dédiées (`accessoires` pour
Key, `gamme-elite-accessoires` pour Elite, `compatible-gamme-vigilia-touch`)
si vous voulez le même bandeau de navigation en haut de chacune — la barre de
sélection rapide détectera automatiquement la page active.

## 3. Configurer les URLs des 4 cartes

Chaque carte (`Carte — Vigilia`, `Carte — Touch / Touch XL`, `Carte — SA501 Key`,
`Carte — PA501Z Elite`) a son propre champ **URL de la collection d'accessoires**.
Les valeurs par défaut pointent déjà vers vos collections réelles :

- Vigilia **et** Touch / Touch XL → `/collections/compatible-gamme-vigilia-touch`
  (les deux cartes peuvent partager cette même URL tout en gardant chacune
  leur propre image, titre et badge — c'est intentionnel, pas un bug).
- SA501 Key → `/collections/accessoires`
- PA501Z Elite → `/collections/gamme-elite-accessoires`

Changez-les librement dans l'éditeur si vos handles de collection évoluent —
rien n'est codé en dur dans le Liquid.

## 4. Ajouter les visuels lifestyle

Pour chaque carte : **Image desktop** (pleine largeur, format large ~16:10 à
21:9) et **Image mobile** (format plus vertical) dans les réglages du bloc.
Sans image, un placeholder Shopify propre s'affiche — la page reste
utilisable en attendant vos photos.

Utilisez uniquement de vraies photos de vos centrales (Vigilia, Touch AM301,
Touch XL AM302, SA501 Key, PA501Z Elite) : rien dans le code ne modifie ou
ne remplace leur design réel, c'est uniquement l'image que vous fournissez qui
s'affiche.

## 5. Badges de compatibilité — comment ça marche

Vos produits ont déjà un métachamp `custom.compatibilite` (référence à un
metaobject `compatibilite`) qui alimente vos collections intelligentes
existantes. Le badge ajouté dans `product-badges.liquid` lit directement
cette même valeur et l'affiche telle quelle sur la carte produit native
(ex. *« Compatible Vigilia & Touch »*, *« Compatible Key »*, *« Compatible
Toutes les gammes »*). Rien n'est déduit du titre produit en JavaScript, et
un produit sans cette valeur renseignée n'affiche simplement pas de badge —
aucun risque de casser l'affichage existant.

## Ce qui n'a volontairement pas changé

- La grille produits, les filtres, le tri, la pagination/scroll infini, le
  quick add, les avis, le panier latéral, le SEO et les données structurées :
  100 % natifs du thème Impact, non touchés.
- Aucune bibliothèque JS externe, aucun filtrage JS maison : la navigation
  entre gammes se fait par de vraies URLs de collection Shopify.
