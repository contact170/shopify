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
| 1 | Bandeau des 4 garanties | au-dessus de l'iframe | `01-bandeau-et-choix.liquid` |
| 2 | Le choix : pack complet ou sur-mesure | au-dessus de l'iframe | `01-bandeau-et-choix.liquid` |
| 3 | Rail « Offres exclusives du moment » | sous l'iframe | `02-offres-exclusives.liquid` |

`preview.html` est la maquette complète, à ouvrir dans un navigateur.

## Le parti pris

Le vocabulaire visuel vient du sujet : un panneau de commande d'alarme. Chaque
option est une **face de panneau** avec sa ligne d'état en écriture monospace et
sa LED — le bloc *Pack complet* est plein (navy), le bloc *Configurateur* est
clair et affiche « vous êtes ici », puisque c'est la page où le visiteur se
trouve déjà. C'est le panneau qu'il ne connaît pas qui reçoit le poids visuel.

Palette et typo reprises du thème en place, rien d'inventé :

| Rôle | Valeur | Origine |
|------|--------|---------|
| Navy texte et panneau plein | `#0c1e4a` | `color_text` du thème |
| Lavande de fond | `#f2f3ff` | `color_background` du thème |
| Bleu action et LED | `#0b61cd` | `color_keyboard_focus` du thème |
| Rouge remises | `#e11d48` | `color_sale_price` du thème |
| Titres et textes | Poppins | `type_header_font` du thème |
| Données, prix, états | IBM Plex Mono | ajout — les chiffres alignés d'un clavier d'alarme |

Le rouge ne sert **qu'aux remises**, jamais à autre chose.

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

## Points à trancher

- **Le cadeau.** Le bloc configurateur annonce « un cadeau ajouté à toute
  commande passée par le configurateur ». C'est repris de l'ancien bandeau
  promo du template, aujourd'hui désactivé. À confirmer que l'offre est toujours
  active, sinon remplacer cette ligne.
- **Livraison 48 h et garantie 2 ans** dans le bandeau : à valider, ces mentions
  ne viennent pas des données du store.
- **La ligne d'aide au choix** (moins de cinq ouvertures → pack) est une règle
  plausible, pas une règle vérifiée. À ajuster selon la réalité produit.
