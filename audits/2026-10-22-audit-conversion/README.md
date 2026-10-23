# Audit conversion daewoo-security.fr (22 octobre 2026)

Rapport complet : ouvrir `index.html` dans un navigateur (graphiques et captures inclus).

Version auditée : thème en ligne « Vidéo Shopify 22102026 (Claude) » (id 206712471892), publié le 22/10/2026 à 18 h 47. Constats revérifiés sur le site en ligne le 23/10/2026. L'export de thème du 18/05/2026 présent dans ce dépôt n'a pas servi de base à l'audit.

Périmètre : SEO technique, GEO (visibilité dans les IA), UX/UI mobile et ordinateur, configurateur, panier et paiement, performance, catalogue et Google Shopping, conformité des prix. Données Shopify des 90 derniers jours (24/07 → 22/10/2026), exploration des 232 URL du sitemap, tests iPhone 13 / Pixel 7 / 360 px, Lighthouse 12.8, 11 requêtes de recherche.

## Chiffres clés (90 jours)

| Indicateur | Valeur |
|---|---|
| Sessions | 51 472, dont 78 % sur mobile |
| Conversion mobile / ordinateur | 0,62 % / 2,48 % |
| Accueil (42 % des entrées) | 0,35 % (0,21 % sur mobile) |
| Comparateur | 3,0 % (meilleure page) |
| Commandes canal Lovable (hors tunnel boutique) | 154 cmd, 69,5 k€, panier moyen 466 € |
| Conversion réelle estimée (boutique + Lovable) | ≈ 1,8 % au lieu de 1,0 % affiché |

## Les 20 actions prioritaires

| # | Action | Impact | Effort | Qui |
|---|---|---|---|---|
| 1 | Réunir boutique et canal Lovable dans un seul indicateur ; faire passer configurateur et page packs par le panier Shopify natif | Critique | Moyen | Développeur |
| 2 | Fiches packs mobile : photo, note, prix, variante dans le 1er écran | Critique | Moyen | Développeur |
| 3 | Checkout : case newsletter décochée, téléphone facultatif | Élevé | Faible | Vous |
| 4 | Ligne de réassurance sous chaque bouton d'achat (livraison, 14 j, Alma) | Élevé | Faible | Développeur |
| 5 | Accueil : 3 packs avec prix sous le hero ; quiz qui affiche des packs | Élevé | Moyen | Développeur |
| 6 | Remplacer l'iframe de /pages/pack-alarmes par une grille native | Élevé | Moyen | Développeur |
| 7 | Harmoniser avis, retours, téléphone, durées, contenu des packs | Élevé | Faible | Vous |
| 8 | Prix barrés : prix de référence ou « prix des éléments séparés » | Élevé | Faible | Vous |
| 9 | Clarifier la gamme d'offres Vigilia (359,90 € vs PSI 299,90 €) | Élevé | Faible | Vous |
| 10 | Fournisseur = Daewoo, EAN des packs, notes Judge.me en données structurées | Élevé | Faible | Vous + dév. |
| 11 | Nettoyer la mesure : robots, UTM Meta, double comptage Google Ads | Élevé | Faible | Vous / agence |
| 12 | Brancher www.daewoo-security.fr | Moyen | Faible | Vous |
| 13 | Panier : paiement express, accessoires suggérés, date de livraison | Moyen | Moyen | Développeur |
| 14 | Accueil : barre collante sur le dock, titre final illisible | Moyen | Faible | Développeur |
| 15 | Performance mobile : pixels, Judge.me, lazysizes, polices, images | Moyen | Moyen | Développeur |
| 16 | Relance des 372 paniers abandonnés | Moyen | Faible | Vous |
| 17 | SEO : doublons de collections, H1, produits Configurateur, URL « -copie » | Moyen | Faible | Vous |
| 18 | Réputation : Trustpilot / Avis Google, fiche Google Business, marketplaces | Moyen | Moyen | Vous |
| 19 | Mise à jour des comparatifs tiers et tests presse de la gamme actuelle | Moyen | Moyen | Vous / RP |
| 20 | Blog : auteurs réels, comparatifs factuels, fusion des doublons | Faible à moyen | Élevé | Contenu |

## Limites

Le proxy de test sortait par une IP américaine et bloquait plusieurs domaines tiers (applications Lovable, Shop Pay, PayPal, Judge.me, Consentmo, Trustpilot). Les éléments correspondants sont à revérifier sur un vrai téléphone depuis la France. Search Console, GA4 et Merchant Center n'étaient pas accessibles. Les points juridiques (RGPD, prix de référence) sont des risques à valider avec un conseil.
