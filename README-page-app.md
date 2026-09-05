# Page « Espace client équipé » — trafic application Daewoo Home Connect

Page d'atterrissage mobile pour les clients qui arrivent depuis le bouton de
l'application. Ils possèdent déjà une centrale : la page ne leur revend pas un
système, elle leur fait identifier leur gamme puis leur propose les accessoires
réellement compatibles, les consommables et l'assistance.

## Fichiers

| Fichier | Rôle |
|---|---|
| `sections/app-hub.liquid` | La section complète (HTML, CSS, JS, schéma) |
| `templates/page.app.json` | Le gabarit de page, pré-rempli avec vos collections et produits |

## Installation

1. **Boutique en ligne → Thèmes → … → Modifier le code**
2. `sections` → *Ajouter une section* → nom `app-hub` → coller `sections/app-hub.liquid`
3. `templates` → *Ajouter un modèle* → type `page`, nom `app` → coller `templates/page.app.json`
4. **Boutique en ligne → Pages → Ajouter une page**
   - Titre : `Mon espace Daewoo`
   - Modèle de page : `page.app`
   - Enregistrer → l'URL est `https://daewoo-security.fr/pages/mon-espace-daewoo`
5. Dans l'éditeur de thème, ouvrir la page pour ajouter les photos des centrales
   (facultatif) et vérifier les liens.

## Contenu pré-rempli

Gammes et collections d'accessoires branchées :

| Gamme | Centrale | Collection | Carte SIM |
|---|---|---|---|
| Key | SA501 | `gamme-key-accessoires` | SIM 1 an (72 €) |
| Vigilia / Touch | AM301 · AM302 | `compatible-gamme-vigilia-touch` | SIM 1 an (72 €) |
| Élite | PA501Z | `gamme-elite-accessoires` | SIM 1 an Élite (85 €) |

Liens d'assistance : Manuels, Franck (assistance), WhatsApp technique, SAV.
Parrainage : `/pages/programme-de-parrainage`.

## Lien à mettre dans l'application

```
https://daewoo-security.fr/pages/mon-espace-daewoo?src=app&utm_source=app&utm_medium=bouton&utm_campaign=home-connect
```

Les deux paramètres sont utiles :

- `src=app` déclenche le mode intégré : l'en-tête, le pied de page et le dock
  mobile du site sont masqués pendant toute la session (réglage désactivable
  dans l'éditeur). La navigation du site n'a pas de sens dans une webview.
- `utm_source=app` sort ce trafic de la catégorie « Accès direct » dans les
  statistiques Shopify. C'est indispensable : aujourd'hui les 10 000 clics de
  l'application sont noyés dans les 11 790 sessions « direct », impossible de
  mesurer quoi que ce soit.

## Comportement

- Le client choisit sa centrale une seule fois ; le choix est mémorisé en
  `localStorage` (`daewoo:gamme`) et la visite suivante démarre directement sur
  ses accessoires compatibles.
- Chaque sélection émet un évènement `daewoo:gamme-selected` sur `document`,
  à brancher sur Google Analytics ou Meta pour savoir quelle gamme est la plus
  représentée dans le parc installé.
- Les fiches produit réutilisent le composant `product-card` du thème :
  l'ajout au panier rapide, les badges promo et le panier latéral fonctionnent
  exactement comme sur le reste du site.
