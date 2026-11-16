# Message pour Lovable : codes par palier (Black Friday −7 %)

À coller tel quel dans le projet Lovable « Configurateur Site Daewoo Security ».

```text
Black Friday −7 % : remplacer le code unique BLACKFRIDAY7 par un code par palier.

Pourquoi : BLACKFRIDAY7 retire 7 % sur toute la commande, y compris hors configurateur (un client qui connaît le code peut l'utiliser sur un pack du site). Il est remplacé par 4 codes Shopify déjà créés, un par palier. Chaque code contient la remise totale (palier + 7 %), ne s'applique qu'aux produits « Configurateur | … » et seulement à partir du seuil du palier. Shopify garde la meilleure remise sur chaque article : le code remplace donc la remise automatique du palier au paiement.

1. Dans src/lib/weekendPromo.ts, remplacer WEEKEND_BONUS_CODE = "BLACKFRIDAY7" par une table palier → code et taux total :
   - palier 10 % (dès 300 €) → "CFG16-ZCR5D3", taux total 0.163
   - palier 15 % (dès 450 €) → "CFG21-FPSTYR", taux total 0.2095
   - palier 20 % (dès 700 €) → "CFG26-LTMSSF", taux total 0.256
   - palier 25 % (dès 900 €) → "CFG30-E7SH8D", taux total 0.3025

2. Dans src/routes/recommandation.tsx, au moment du paiement : quand isWeekendPromoActive() est vrai et qu'un palier s'applique, mettre dans discountCodes le code du palier à la place de BLACKFRIDAY7. Le palier se choisit exactement comme aujourd'hui (getDiscountTier). Ne plus jamais envoyer BLACKFRIDAY7. Hors période (après le vendredi 20 novembre 14h), rien ne change par rapport à avant l'opération.

3. Montant affiché, pour qu'il soit identique au paiement Shopify : calculer la remise totale comme Shopify avec ces codes. Pour chaque article remisé : remise unitaire = prix unitaire × taux total, arrondie au centime inférieur ; remise de la ligne = remise unitaire × quantité ; remise totale = somme des lignes. La part « −7 % Black Friday » affichée = remise totale − remise du palier. Les pourcentages affichés dans les bandeaux (−16,3 / −21 / −25,6 / −30,3 %) ne changent pas.
   Contrôle : Vigilia Wi-Fi 139,90 + W512MW 159,90 + WOS305S 129,90 + WDV301 39,90 = 469,60 € → remise totale 98,35 € → total 371,25 €.

4. Tests à faire après publication : un panier par palier ; sur la page de paiement Shopify, le code CFGxx doit apparaître et le total doit être le même que dans le configurateur. Panier sous 300 € : aucun code.

Ne rien changer d'autre (bandeau Black Friday, compte à rebours, textes, autres offres).
```

Une fois en ligne : prévenir Claude, qui contrôle le code dans Lovable puis
désactive `BLACKFRIDAY7` dans Shopify.

## Correction n° 2 : aligner les deux autres affichages de prix (16/11)

```text
Black Friday −7 % : aligner les deux autres affichages de prix sur le calcul des codes CFG.

Problème : dans src/components/v2b/RecoCompactHero.tsx, le prix du bouton « Commander mon alarme — … € » utilise encore computeWeekendBonus(summary.subtotal, summary.discountAmount), donc 7 % sur tout le panier, y compris les articles exclus de la remise (cartes SIM, prises connectées, canon à fumée). Or les codes CFG ne s'appliquent qu'aux articles remisés. Exemple : avec une carte SIM 1 an (72 €) dans le panier, ce bouton affiche environ 5 € de moins que le récapitulatif et que le paiement Shopify.

1. RecoCompactHero.tsx : quand isWeekendPromoActive() est vrai et qu'un palier s'applique, calculer la remise −7 % exactement comme dans src/routes/recommandation.tsx : computeWeekendTierTotalDiscount(lignes remisées, palier) − remise du palier, avec les lignes remisées (discountableLines) et getEffectivePrice. Hors période : 0.
2. LiveValuePanel.tsx : l'avantage « +X € d'avantage à la fin » utilise computeWeekendBonus(estimate.total, 0). Le calculer avec la même méthode, sur les articles remisés de la recommandation.
3. Vérifier que le prix du bouton du haut, le total du récapitulatif et le total de la page de paiement Shopify sont identiques, avec et sans carte SIM dans le panier.

Ne rien changer d'autre.
```
