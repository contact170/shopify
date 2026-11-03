# Brezello : fiche produit Shopify

Page produit de l'inhaler nasal Brezello, prête à installer sur une boutique
Shopify avec un thème récent (Online Store 2.0 : Dawn, Concept, etc.).
Elle ne touche pas au thème existant : tout est préfixé `brezello-` ou `bz-`.

Aperçu en ligne : https://claude.ai/artifact/Wds6iHqaQMZ7DWwidTuVTx
(l'en-tête et le pied de page de l'aperçu sont ceux d'une démo : sur la
boutique, ce sont ceux du thème).

## Contenu

| Fichier | Rôle |
|---|---|
| `shopify/sections/brezello-produit.liquid` | Galerie, choix parfum/format, abonnement, panier, bandeau défilant, grille des parfums, composition |
| `shopify/sections/brezello-rituel.liquid` | Mode d'emploi en étapes |
| `shopify/sections/brezello-objet.liquid` | L'objet sur fond sombre, schéma annoté |
| `shopify/sections/brezello-faq.liquid` | Questions fréquentes |
| `shopify/sections/brezello-coffret.liquid` | Mise en avant du coffret |
| `shopify/snippets/brezello-inhaler.liquid` | Illustration de l'inhaler (affichée tant qu'il n'y a pas de photo) |
| `shopify/assets/brezello.css`, `brezello.js` | Styles et interactions |
| `shopify/assets/bz-*.woff2` | Polices Bricolage Grotesque et DM Mono (licence SIL OFL), hébergées dans le thème : rien n'est chargé depuis Google, ce qui évite le transfert d'adresses IP vers Google (RGPD) |
| `shopify/templates/product.brezello.json` | Modèle de fiche produit qui assemble les sections, 4 parfums préremplis |
| `outils/` | Générateur de l'aperçu (liquidjs + données fictives) |

## Installation

1. **Dupliquer le thème** (Boutique en ligne › Thèmes › … › Dupliquer) et
   travailler sur la copie.
2. **Créer le produit** avec deux options :
   - `Parfum` : Glaciale, Agrumi, Dolce, Calma
   - `Format` : Solo, Duo, Pack de 4 (ou vos propres formats)

   Le nom des valeurs de `Parfum` doit être identique au nom des blocs
   « Parfum » de la section (c'est ce qui relie couleurs et textes à la variante).
3. **Ajouter les fichiers au thème** (… › Modifier le code) en respectant les
   dossiers `sections/`, `snippets/`, `assets/`, `templates/`. Les polices
   `.woff2` s'importent dans `assets/` avec « Importer un fichier ».
   Avec Shopify CLI : `shopify theme push --only` suivi des chemins.
4. **Attribuer le modèle** : fiche du produit dans l'admin › Modèle de thème ›
   `brezello`.
5. **Personnaliser dans l'éditeur de thème** : textes, couleurs, produit du
   coffret, ordre des sections.

## Comportement

- **Photos** : tant que le produit n'a pas de photo, l'illustration vectorielle
  s'affiche aux couleurs du parfum. Dès qu'il y en a, elles la remplacent ;
  une photo rattachée à une variante s'affiche quand on la choisit.
- **Abonnement** : le bloc « Mode d'achat » n'apparaît que si le produit a un
  plan d'abonnement (application Shopify Subscriptions, par exemple).
- **Ajout au panier** : envoi standard Shopify vers la page panier, compatible
  avec tous les thèmes. Les boutons de paiement express se désactivent dans les
  réglages de la section.
- **Adresse de la page** : le choix d'une variante met à jour `?variant=`.

## À compléter avant la mise en ligne

Tout ce qui est entre crochets : prix et seuil de livraison (`[XX]`), délai
d'expédition, durée d'utilisation, âge minimum, hauteur de l'objet, liste
INCI de chaque parfum. Vérifier aussi l'adresse `bonjour@brezello.com`.

## Points réglementaires à valider

- Textes volontairement limités aux sensations (fraîcheur, bien-être) : aucune
  allégation de soin. Un produit aux huiles essentielles vendu en France ne
  peut pas revendiquer d'effet thérapeutique.
- Statut du produit, étiquetage et précautions (enfants, grossesse, épilepsie,
  asthme) à confirmer avec le fournisseur et son évaluateur de sécurité.
- Éviter les variantes à la caféine proposées par certains fabricants.
- Droit de rétractation de 14 jours : les produits d'hygiène descellés peuvent
  en être exclus, d'où la mention « produit non ouvert ».

## Régénérer l'aperçu

```bash
cd brezello/outils && npm install
node render-preview.js ../shopify apercu.html
```
