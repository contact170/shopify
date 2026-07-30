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
| `templates/collection.accessoires-hub.json` | **Nouveau** | Template alternatif dédié : ma section + la section `main-collection` native, réglée avec vos filtres/tri/pagination actuels. Ne remplace pas votre `collection.json` par défaut. |

Aucun fichier JavaScript n'a été nécessaire : navigation par vraies URLs de
collection, défilement doux en CSS (`scroll-behavior: smooth`), état actif de
la barre de sélection calculé côté serveur (Liquid), `prefers-reduced-motion`
respecté en CSS.

## Déjà déployé — thème brouillon

Ces 6 fichiers sont déjà en ligne dans un thème **brouillon** dédié :
**« Sélecteur accessoires (Claude) »** (id `200542421332`) — dupliqué depuis
votre thème actif, donc zéro impact sur le site en ligne tant qu'il n'est pas
publié.

Aperçu direct :
```
https://daewoo-security.myshopify.com/admin/themes/200542421332/editor?template=collection.accessoires-hub&previewPath=%2Fcollections%2Ftous-les-accessoires
```

Les sections ci-dessous restent utiles si vous voulez recréer ça vous-même
dans un autre thème, ou comprendre ce qui a été fait.

## 1. Installation dans le thème

1. Dans l'admin Shopify : **Boutique en ligne → Thèmes → (votre thème) → Modifier le code**.
2. Créez les fichiers ci-dessus dans les bons dossiers (`Add a new section/asset/snippet/template`), en collant le contenu correspondant.
3. Ouvrez `snippets/product-badges.liquid` existant et collez le bloc ajouté en fin de fichier (juste avant le `</div>` final) — ne remplacez pas le reste du fichier.

> Note technique : les réglages de type URL (`button_link`, `quick_nav_all_link`,
> `identify_contact_link`) n'ont pas de valeur par défaut dans le schéma —
> Shopify rejette les chemins relatifs comme défaut de schéma. Dans le template
> `collection.accessoires-hub.json` fourni, les 4 cartes sont déjà pré-remplies
> avec vos vraies URLs de collection (via `shopify://collections/...`) ; si vous
> ajoutez la section manuellement ailleurs, il faudra renseigner ces URLs une
> fois dans l'éditeur (voir section 3 ci-dessous).

## 2. Ajouter la section au template de collection

Deux options :

- **Option rapide (déjà faite dans le brouillon) :** utiliser
  `templates/collection.accessoires-hub.json` tel quel comme template
  alternatif, puis l'assigner à la collection `tous-les-accessoires` via
  **Réglages de la collection → Modèle de theme** dans l'admin (uniquement
  une fois le thème publié — voir plus bas).
- **Option manuelle :** dans **Éditeur de thème → template de collection de
  votre choix → Ajouter une section**, choisissez *Daewoo — Accessoires*.
  Placez-la **au-dessus** de la section *Collection principale* (grille
  produits native). Elle arrive pré-remplie (voir `presets`) : hero, 4
  cartes, 4 avantages de réassurance — il ne manque que les images et les
  4 URLs (voir section 3).

Répétez l'étape sur les templates des collections dédiées (`accessoires` pour
Key, `gamme-elite-accessoires` pour Elite, `compatible-gamme-vigilia-touch`)
si vous voulez le même bandeau de navigation en haut de chacune — la barre de
sélection rapide détectera automatiquement la page active.

## 3. Configurer les URLs des 4 cartes

Chaque carte (`Carte — Vigilia`, `Carte — Touch / Touch XL`, `Carte — SA501 Key`,
`Carte — PA501Z Elite`) a son propre champ **URL de la collection d'accessoires**,
sans valeur par défaut dans le schéma (Shopify l'exige ainsi). Dans le
template fourni elles sont déjà renseignées ; si vous ajoutez la section à la
main ailleurs, remplissez-les vous-même via le sélecteur de collection de
l'éditeur :

- Vigilia **et** Touch / Touch XL → collection *Compatible gamme Vigilia / Touch*
  (les deux cartes peuvent partager cette même collection tout en gardant
  chacune leur propre image, titre et badge — c'est intentionnel, pas un bug).
- SA501 Key → collection *ACCESSOIRES KEY (SA501)*
- PA501Z Elite → collection *Compatible gamme Élite*

Rien n'est codé en dur dans le Liquid — tout passe par ces champs.

## 4. Ajouter les visuels

Chaque carte a un réglage **Style de l'image** :

- **Lifestyle** (par défaut) : photo pleine largeur, texte en surimpression.
  Fait pour de vraies photos d'intérieur, format large ~16:10 à 21:9, avec
  une variante **Image mobile** plus verticale.
- **Produit** : la photo reste entière (non recadrée) sur un fond neutre,
  le texte passe en dessous plutôt qu'en surimpression. Pensé pour vos
  photos studio existantes (fond blanc), en attendant vos prises de vue
  lifestyle.

Dans le thème brouillon, les 4 cartes utilisent déjà vos vraies photos
produit existantes (celles de vos fiches produit centrales) en style
**Produit** — nettement plus premium qu'un aperçu vide, mais toujours en
attente de vos photos lifestyle pour le rendu final visé par le brief.
Sans image du tout, un placeholder Shopify propre s'affiche.

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
