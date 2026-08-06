# Bandeau promo « Week-end −10% » — page d'accueil daewoo-security.fr

Bandeau promotionnel pleine largeur mettant en avant **−10 % sur le configurateur pendant le week-end**.
Conçu pour s'intégrer à la charte du thème (navy `#0b1e4a`, bleu `#1a4fab`, accent cyan `#48cae4`, Poppins + DM Sans).

## Aperçu
Ouvrez `bandeau-weekend-10.liquid` — ou l'aperçu interactif partagé dans la conversation.

## Ce que contient le bandeau
- Message principal + gros **−10 %** en cyan
- Un **coupon perforé** style ticket avec le code promo et un bouton **Copier**
- Un **compte à rebours en direct** qui vise automatiquement le **dimanche 23 h 59** (aucune date à changer chaque semaine)
- Bouton CTA vers le configurateur, halos animés, effet de brillance (désactivés si `prefers-reduced-motion`)

## Installation (2 min)
1. Admin Shopify → **Boutique en ligne → Personnaliser** (thème `daewoo-security-fr-concept`).
2. Sur la page d'accueil, **Ajouter une section → Contenu Liquid** (Custom Liquid). Placez-la sous le slideshow.
3. Collez tout le contenu de [`bandeau-weekend-10.liquid`](./bandeau-weekend-10.liquid) dans le champ Liquid.
4. Réglez le champ « Marge intérieure haut/bas » de la section sur `0` (le bandeau gère ses propres marges).
5. **Enregistrer**.

## À personnaliser (en haut du fichier)
```liquid
{%- assign cta_url = '/pages/configurateurs' -%}   {# lien du bouton #}
{%- assign promo   = 'WEEKEND10' -%}               {# code affiché sur le coupon #}
```

## Créer le code promo dans Shopify
Admin → **Réductions → Créer un code de réduction → Montant en pourcentage** →
`-10 %`, code **WEEKEND10**. Vous pouvez le limiter à la collection du configurateur
et programmer sa validité du samedi 00 h 00 au dimanche 23 h 59.

## Activer / désactiver
Pour retirer l'offre après le week-end : masquez la section depuis le personnalisateur
(icône œil) ou supprimez-la. Le compte à rebours se réinitialise seul au week-end suivant.
