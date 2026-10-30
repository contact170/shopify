# Mailing du 30/10/2026 : Sécurité Intégrale, caméras, prises, canon à fumée

Fichier à importer dans Brevo : `mailing-brevo.html`.

## Objet et pré-header

| | Objet | Angle |
|---|---|---|
| **A (recommandé)** | Dernière chance : alarme + 2 caméras dès 299,90 € | Urgence + prix concret |
| B (test A/B) | 8 secondes pour faire fuir un cambrioleur | Curiosité, met en avant le canon à fumée |
| C | Votre Pack Sécurité Intégrale se termine samedi | Urgence pure |

Pré-header : déjà intégré dans le HTML. Le coller aussi dans le champ « Texte d'aperçu »
de la campagne Brevo :

> Et aussi : la 2ème caméra à -50 %, 3 prises à 49,90 € et le canon à fumée qui rend une pièce opaque en 8 secondes.

## Structure

1. **Pack Sécurité Intégrale** : badge « Dernière chance · jusqu'au 31/10 à 23h59 », contenu du pack, argument
   « les 2 caméras et la sirène solaire valent déjà 359,70 € à l'unité », choix des 4 centrales, CTA.
2. **Canon à fumée F502W** (bloc vedette, fond bleu nuit) : prix inchangé 249,90 €, chiffres clés
   (8 s, 150 m³, 30-45 min, 0 € d'abonnement), 3 modes de déclenchement, duo caméras + canon.
3. **Caméras W503 et W512MW, la 2ème à -50 %** : 2 cartes produits avec prix « les 2 ».
4. **Pack de 3 prises SP502F** : simulation de présence, 3 étapes, 49,90 € au lieu de 89,70 €.
5. Réassurance, aide (contact + configurateur), pied de page.

## Sources des chiffres (vérifiés dans Shopify le 30/10/2026)

- Packs Sécurité Intégrale : 299,90 / 349,90 / 399,90 / 449,90 € ; fin de l'offre
  2026-10-31T23:59:59+01:00 (compte à rebours de `/pages/offre-speciale`).
- « 359,70 € à l'unité » = caméra IP506P 69,90 € + caméra W512MW 159,90 € + sirène WOS305S 129,90 €.
- Caméras : réductions automatiques actives « W503 – La 2ème à -50% » et « W512MW – La 2ème à -50% »
  (même modèle uniquement, non cumulables). W503 : 119,90 + 59,95 = 179,85 € ; W512MW : 159,90 + 79,95 = 239,85 €.
- Prises : variante « Pack de 3 prises connectées SP502F » 49,90 € (prix barré 89,70 € = 3 × 29,90 €).
- Canon F502W : 249,90 €, caractéristiques reprises de la fiche produit.

## Liens

Les 4 cartes « Choisissez votre centrale » ouvrent la page d'offre avec la centrale déjà
sélectionnée : `/pages/offre-speciale?centrale=vigilia` (ou `vigilia-plus`, `touch`, `touch-xl`).
Les fiches produits des packs Sécurité Intégrale utilisent le modèle Shopify de base : ne pas y envoyer.

## Avant d'envoyer

- [x] **Stock du pack de 3 prises** : passé de 3 à 100 unités (variante `DASP502FP3`,
      entrepôt 6 rue Léon Morane) le 30/10/2026.
- [ ] Brevo : Campagnes › Créer une campagne › E-mail. Renseigner l'objet et le texte d'aperçu,
      puis à l'étape « Concevoir », choisir « Coder votre propre HTML » et coller tout le fichier.
- [ ] Liens Brevo déjà en place dans le pied de page : `{{ unsubscribe }}` (désinscription,
      obligatoire) et `{{ mirror }}` (version en ligne). Ils ne fonctionnent qu'une fois dans Brevo.
- [ ] Adresse du pied de page écrite en clair : Daewoo Security (Liz Invest SAS),
      6 rue Léon Morane, 33700 Mérignac (adresse de la boutique dans Shopify).
- [ ] Dans les paramètres avancés de la campagne, cocher « Activer le suivi Google Analytics »
      (les liens n'ont pas d'UTM en dur).
- [ ] « Envoyer un test » et vérifier sur mobile et sur Gmail.
