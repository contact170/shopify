# Page configurateur — proposition de design

Concerne la page **« Trouver mon alarme »** du menu → `/pages/configurateur_2`
(page Shopify *Configurez votre alarme*, template `page.configurateur-lovable`).

## Ce que fait la proposition

Aujourd'hui la page ne contient que l'iframe du configurateur Lovable : toutes
les autres sections du template sont désactivées. Le visiteur qui arrive du menu
n'a donc qu'une seule porte d'entrée, et il ne sait pas qu'un pack déjà assemblé
existe.

La proposition ajoute trois choses, **sans toucher au configurateur lui-même** :

| # | Bloc | Position | Fichier |
|---|------|----------|---------|
| 1 | Bandeau des garanties, pleine largeur | au-dessus de l'iframe | `01-bandeau-et-choix.liquid` |
| 2 | Le choix : pack complet ou sur-mesure | au-dessus de l'iframe | `01-bandeau-et-choix.liquid` |
| 3 | Rail « Offres exclusives du moment » | sous l'iframe | `02-offres-exclusives.liquid` |

`preview.html` est la maquette complète, à ouvrir dans un navigateur.

## Le design vient du site, pas d'ailleurs

Tout est repris du design déjà en place sur la page d'accueil (hero, section
« Nos 3 gammes », section À propos) et des réglages du thème :

| Rôle | Valeur | Origine |
|------|--------|---------|
| Navy | `#0b1e4a` | dégradé du hero et fond de la section À propos |
| Bleu primaire | `#1a4fab` | bouton et bord des cartes « gammes » — aussi `color_price` du thème |
| Cyan d'accent | `#48cae4` | pastille des badges du site |
| Lavande de fond | `#f2f3ff` | `color_background` du thème |
| Rouge remises | `#e11d48` | `color_sale_price` du thème |
| Texte secondaire | `#5b6485` | sous-titres du hero |
| Titres | Poppins 600/700 | typo d'affichage du site |
| Textes | DM Sans 300–600 | typo de lecture du site |

Composants réutilisés tels quels : le **badge pilule à pastille**, la **carte
blanche** (coins 18 px, bord 1,5 px, survol qui soulève), le **dégradé navy →
bleu avec halo cyan**, le **bandeau pleine largeur** en `100vw` que le site
emploie déjà dans la section À propos.

Le parti pris : le panneau **Pack complet** est le panneau plein, celui qui
attire l'œil, alors que le panneau **Configurateur** est clair et porte la
mention « vous êtes ici ». C'est volontaire — le visiteur est déjà sur le
configurateur, l'information qu'il n'a pas, c'est le pack.

Le rouge ne sert **qu'aux remises**, jamais à autre chose.

## Les images

Aucune image nouvelle à produire : la proposition utilise des visuels qui
existent déjà dans vos fichiers Shopify.

| Emplacement | Fichier Shopify |
|-------------|-----------------|
| Panneau *Pack complet* | `Image_Acceuil_Pack_Pret_a_poser_Daewoo.png` |
| Panneau *Configurateur* | `Image_Acceuil_Configurateur_Daewoo.png` |
| Cartes du rail | photo principale de chaque produit, tirée automatiquement |

Pour changer l'un des deux visuels de panneau, il suffit de remplacer l'URL dans
les variables `img_pack` / `img_config` en haut de `01-bandeau-et-choix.liquid`.

## Pose dans Shopify

Pour chacun des deux fichiers `.liquid` :

1. Boutique en ligne → Thèmes → **Personnaliser**
2. Ouvrir la page `Configurez votre alarme` (`/pages/configurateur_2`)
3. **Ajouter une section** → *Liquid personnalisé*
4. Coller le contenu du fichier dans le champ *Liquid*
5. Régler **marge haute = 0** et **marge basse = 0**
6. Glisser la section : `01-…` **au-dessus** de la section « Page », `02-…` **en dessous**

Aucune modification du corps de la page ni de l'iframe. Les classes sont toutes
préfixées `.cfg-` pour ne rien percuter dans le thème.

## Ce qui est dynamique

Rien à maintenir à la main :

- **Prix mini et nombre de packs** du bloc *Pack complet* → collection `starters-packs`
- **Produits, photos, prix, remises et compteur** du rail → collection `offres-exclusives-copie`
  (*Offres exclusives (Alarmes uniquement)*)
- Le pourcentage de remise et le montant économisé sont **calculés** depuis
  `compare_at_price`, jamais saisis
- Les produits en rupture sont sautés automatiquement
- Les titres sont nettoyés à l'affichage : le préfixe `OFFRE EXCLUSIVE |` est
  retiré pour laisser lire le produit

Pour pointer vers d'autres collections, changer la ligne `assign` en haut de
chaque fichier.

## Le seul point à vérifier

La collection `starters-packs` (4 produits, à partir de 139,90 €) doit être
**publiée sur la boutique en ligne**, sinon le bouton « Voir les packs
complets » mènera à une page introuvable. Je n'ai pas pu le vérifier depuis ici :
l'API refuse la lecture des publications sans le droit `read_product_listings`.

Si ce n'est pas la bonne collection de destination, remplacer `starters-packs`
en haut de `01-bandeau-et-choix.liquid`.
