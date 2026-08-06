# Bandeau promo « Week-end +8% » — page d'accueil daewoo-security.fr

Bandeau promotionnel pleine largeur, **voyant**, mettant en avant une
**remise supplémentaire de +8 %** sur le configurateur pendant le week-end.
La remise est **cumulable avec les remises paliers** du configurateur (jusqu'à −25 %).

Palette chaude (ambre → orange → corail) avec texte navy `#12224a` (rappel de marque),
Poppins + DM Sans, soleil promo animé et compte à rebours.

## Aperçu
Ouvrez `bandeau-weekend-8.liquid` — ou l'aperçu interactif partagé dans la conversation.

## Ce que contient le bandeau
- Gros **+8 %** en soleil promo animé (point focal)
- Jauge des remises paliers : `−5 %  −15 %  jusqu'à −25 %  +  +8 % week-end`
- **Aucun code** — mention « remise appliquée automatiquement » (gérée par le configurateur / Lovable)
- **Compte à rebours en direct** visant automatiquement le **dimanche 23 h 59** (rien à reprogrammer)
- Bouton CTA vers le configurateur, rayures animées, étincelles (tout se coupe si `prefers-reduced-motion`)

## Installation (2 min)
1. Admin Shopify → **Boutique en ligne → Personnaliser** (thème `daewoo-security-fr-concept`).
2. Sur la page d'accueil, **Ajouter une section → Contenu Liquid** (Custom Liquid). Placez-la sous le slideshow.
3. Collez tout le contenu de [`bandeau-weekend-8.liquid`](./bandeau-weekend-8.liquid) dans le champ Liquid.
4. Réglez la marge intérieure haut/bas de la section sur `0` (le bandeau gère ses propres marges).
5. **Enregistrer**.

## À personnaliser (en haut du fichier)
```liquid
{%- assign cta_url = '/pages/configurateurs' -%}   {# lien du bouton vers le configurateur #}
```
Rien d'autre à toucher : pas de code promo (le configurateur applique la remise),
et le compte à rebours calcule tout seul la fin du week-end.

## Activer / désactiver
Pour retirer l'offre après le week-end : masquez la section depuis le personnalisateur
(icône œil) ou supprimez-la. Le compte à rebours se réinitialise seul au week-end suivant.

## Ajuster les remises affichées
Les paliers `−5 % / −15 % / −25 %` et le `+8 %` sont de simples `<span class="dwp__chip">`
dans le HTML — modifiez le texte si vos paliers réels diffèrent.
