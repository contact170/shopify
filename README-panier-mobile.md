# Panier mobile — bandeau de réassurance

Optimisation du panier sur mobile uniquement. La version desktop n'est pas
modifiée : tout le nouveau code vit dans un `@media screen and (max-width: 767px)`,
et le bandeau d'origine reste affiché au-dessus de 768 px.

## Pourquoi

Sur 90 jours :

| | Sessions | Ajouts panier | Checkout atteint | Commandes | Conversion |
|---|---|---|---|---|---|
| Mobile | 31 504 | 847 | 538 | 218 | **0,69 %** |
| Desktop | 8 456 | 629 | 514 | 263 | **3,11 %** |

Le mobile fait 79 % du trafic et produit moins de commandes que le desktop.
La fuite se voit à l'étape panier → checkout : **63,5 % sur mobile contre
81,7 % sur desktop**. C'est cette étape que ce composant vise.

Sur les 100 dernières commandes payées, **10 sont sous 50 €** — soit exactement
les 90 % annoncés. Mais ces 10 commandes valent 32,80 € à 47,80 € : toutes à
moins de 18 € du seuil, alors que les accessoires démarrent à 34,90 €.
Supprimer la barre de progression ferait perdre ce levier.

D'où les deux états plutôt qu'un message fixe.

## Fichiers

| Fichier | Rôle |
|---|---|
| `snippets/cart-reassurance-mobile.liquid` | Le composant complet (markup + CSS) |

## Installation

**1.** Créer `snippets/cart-reassurance-mobile.liquid` et y coller le fichier.

**2.** Dans `sections/cart-drawer.liquid` (vers la ligne 110), remplacer :

```liquid
                  if show_free_shipping_bar
                    render 'free-shipping-bar', minimum_amount: minimum_amount
                  endif
```

par :

```liquid
                  if show_free_shipping_bar
                    echo '<div class="cart-legacy-bar">'
                    render 'free-shipping-bar', minimum_amount: minimum_amount
                    echo '</div>'
                    render 'cart-reassurance-mobile', minimum_amount: minimum_amount
                  endif
```

**3.** Refaire exactement la même substitution dans `sections/main-cart.liquid`
(vers la ligne 707), pour la page `/cart`. L'indentation y est différente,
gardez celle du fichier.

Aucun autre fichier n'est touché. Le seuil reste celui déjà réglé dans
l'éditeur de thème (`50`), le composant le reçoit en paramètre.

## Ce que ça change

**Sous 50 € (10 % des paniers)** — la barre est conservée, mais devient
actionnable : montant restant, progression, et un lien vers les accessoires
triés du moins cher au plus cher.

**À partir de 50 € (90 % des paniers)** — la barre pleine à 100 % laisse place
à « Livraison gratuite · France et Belgique », suivi de quatre repères :
paiement sécurisé, Colissimo 48 h, sans abonnement, SAV à Bordeaux.

**Pied du tiroir** — « Commander » passe pleine largeur et le cadenas
réapparaît (le thème le masque sous 640 px) ; « Voir le panier » devient un
lien discret. Les deux boutons se partageaient l'écran à 50/50, ce qui donnait
à une sortie de tunnel le même poids visuel qu'à la commande.

## Exactitude des promesses affichées

Textes vérifiés contre vos zones de livraison Shopify réelles :

| Zone | ≥ 50 € | < 50 € | Transporteur |
|---|---|---|---|
| France | 0 € | 7,90 € | Colissimo 48 H |
| Belgique | 0 € | 14,90 € | DPD 3–5 jours |
| Reste UE | 14,90 € | 14,90 € | DPD |

La gratuité vaut bien pour la France **et** la Belgique, et pour elles seules —
d'où la mention explicite des deux pays plutôt que « Europe ».

Tous les textes sont regroupés en haut du snippet, dans un bloc `assign`.
Si vous changez vos tarifs de livraison, changez-les aussi. Ils sont écrits
en français en dur : les versions `/en/` et `/es-com/` du site afficheront
donc du français dans ce bandeau.
