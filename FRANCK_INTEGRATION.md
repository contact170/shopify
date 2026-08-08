# Intégration de Franck (barre flottante Chatbase)

Ajoute une **barre flottante « Franck »** en bas de page, façon Dialog AI : une barre
discrète (avatar + phrase d'accroche + champ de saisie) qui, au clic, ouvre un panneau
de conversation contenant l'agent **Franck** via l'iframe officielle Chatbase.

## Fichiers ajoutés / modifiés
- `theme_extracted/snippets/franck-bar.liquid` — **nouveau** : toute la barre (HTML/CSS/JS).
- `theme_extracted/config/settings_schema.json` — groupe de réglages **« Franck – Assistant IA »**.
- `theme_extracted/layout/theme.liquid` — une ligne `{%- render 'franck-bar' -%}` avant `</body>`.

Le thème complet, avec l'intégration, est reconstruit dans :
`theme_export__daewoo-security-fr-concept__franck-integration.zip`

## Installation (recommandé : sur un thème de test)
1. Shopify Admin → **Boutique en ligne → Thèmes**.
2. **Ajouter un thème → Importer** le fichier
   `theme_export__daewoo-security-fr-concept__franck-integration.zip`.
   > Importe-le comme thème **non publié** pour tester sans toucher au site en ligne.
3. Sur ce thème → **Personnaliser** → **Paramètres du thème** (icône engrenage en bas)
   → section **« Franck – Assistant IA »**.
4. Colle l'**ID de ton chatbot Chatbase** dans *ID du chatbot Chatbase*.
   > Où le trouver : Chatbase → ton agent → **Connect / Embed** → dans l'iframe,
   > l'ID est la fin de l'URL `.../chatbot-iframe/**VOTRE_ID**`.
5. **Enregistrer**.

### Réglages déjà préparés pour le test
- **Activer la barre Franck** : ✅ activé
- **Où afficher** : *Pages produits uniquement*
- **Limiter à des produits précis** : `offre-exclusive-pack-touch-compatible-animaux-sans-abonnement`
  → la barre n'apparaît **que** sur cette fiche :
  https://daewoo-security.fr/collections/offres-du-mois-1/products/offre-exclusive-pack-touch-compatible-animaux-sans-abonnement

## Côté Chatbase (important)
Dans Chatbase → ton agent → **Security / Domaines autorisés**, ajoute ton domaine
(`daewoo-security.fr` et `*.myshopify.com`) pour autoriser l'affichage de l'iframe.
Si l'« Identity verification » est activée dans Chatbase, désactive-la pour un simple
embed public, sinon le chat restera bloqué.

## Déploiement plus large (après validation)
Dans les réglages du thème :
- **Ajouter d'autres fiches** : ajoute leurs handles, séparés par des virgules.
- **Toutes les pages produits** : vide le champ *Limiter à des produits précis*.
- **Tout le site** : passe *Où afficher* sur *Tout le site*.

Pour désactiver : décoche *Activer la barre Franck*.
