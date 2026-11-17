# Refonte de la page d'accueil — note de reprise

Mission : refonte premium, mobile d'abord, de la page d'accueil de
daewoo-security.fr (thème Impact, sections sur mesure `dw-home-*`).
Cette note permet à une nouvelle session de reprendre sans contexte.

## État au 17/11/2026

| Phase | État |
|---|---|
| 1. Audit | Fait (ci-dessous) |
| 2. Architecture | Proposée, accord de principe du dirigeant (« ok vas y ») |
| 3. Maquette | Première version : `maquette-accueil.html` (à faire valider) |
| 4. Développement sur copie du thème | **Bloqué** : voir « Blocage » |
| 5. Contrôles, 6. Présentation | À faire |

## Règles fixées par le dirigeant

- Ne jamais modifier le thème publié ; travailler sur une copie nommée
  « … (Claude) » ; ne rien publier sans autorisation explicite.
- Uniquement les vraies photos produits ; aucun prix, promotion ou
  caractéristique supposé : tout est relevé sur le site.
- Pas de prix barré ni d'économie sans justification réelle.
- Textes, prix, images et offres modifiables dans l'éditeur Shopify
  (sections OS 2.0), prix lus sur les fiches produits.
- Conserver Alma, le configurateur, les avis, le suivi analytique.
- Recommandation : ne pas publier avant la fin du Black Friday (30/11).

## Blocage

Le connecteur Shopify lit le catalogue et les statistiques mais refuse
`theme_bash`, `theme_screenshot` et `theme_commit` (« permissions
supplémentaires requises »). Le dirigeant doit le déconnecter puis le
reconnecter sur https://claude.ai/customize/connectors en acceptant les
permissions sur les thèmes, puis ouvrir une nouvelle session.

En attendant, les fichiers du thème se lisent par GraphQL
(`theme(id:) { files(filenames:) { nodes { body { ... on
OnlineStoreThemeFileBodyText { content } } } } }`) et le site en ligne
se capture avec Playwright sur `https://daewoo-security.fr/` (sans
`www`, seul domaine autorisé par l'environnement). Les sections sous le
premier écran n'apparaissent qu'au défilement : capturer écran par
écran, pas en pleine page.

Thème publié le 17/11/2026 : `gid://shopify/OnlineStoreTheme/209106534740`
« Configurateur -7% 16112026 (Claude) ».

## Audit : constats mesurés

Sources : ShopifyQL (90 jours), GA4 et Chrome UX Report via GSC Wizard
(28 jours), captures Playwright du 17/11/2026.

| Constat | Mesure |
|---|---|
| Part du mobile | 46 610 sessions sur 60 212 (77 %) |
| Conversion mobile / ordinateur | 0,64 % / 2,25 % |
| Ajout au panier mobile / ordinateur | 3,5 % / 7,5 % |
| Accueil comme page d'entrée | 22 093 sessions, 1,9 % d'ajout au panier, 0,41 % de conversion |
| Comparateur comme page d'entrée | 3 910 sessions, 11,4 % d'ajout au panier, 3,17 % |
| Page « offre spéciale » | 1 682 sessions, 2,32 % |
| Hauteur de l'accueil mobile | 14 136 px (environ 21 écrans de 664 px) |
| Position du H1 sur mobile | 1 654 px, sous 1 520 px de bloc Black Friday |
| Utilisateurs atteignant 50 % de la page | 622 sur 3 038 (20 %) |
| LCP mobile réel (p75) | 1,34 s (0,83 s en septembre) |
| INP mobile réel (p75) | 189 ms, 78 % de visites « bonnes » |
| CLS mobile réel (p75) | 0 |
| Scripts chargés sur l'accueil | 114 requêtes |

Autres constats :
- Deux barres fixes en bas sur mobile (boutons flottants + navigation),
  plus bandeau et en-tête : environ 60 % de l'écran reste au contenu.
- Trois mécaniques promotionnelles simultanées (prix Black Friday, bons
  d'achat 30/50/70 €, −7 % configurateur) et long texte légal en milieu
  de page.
- Trois prix « dès » en trois écrans (139,90 €, 249,90 €, 369,90 €).
- Deux sections de packs redondantes (`gamme_offre`, `dwh_best`).
- Deux notes d'avis sans explication (4,6/5 sur 1 091 ; 4,9/5 sur 77 Google).
- Aucun événement `dwh_*` (quiz, offres) dans GA4 pour l'accueil, alors
  que le thème les pousse dans le `dataLayer` (suivi par Addingwell/GTM).

Hypothèse (non démontrée) : l'écart avec le comparateur vient en partie
d'un trafic plus décidé.

Forces à conserver : quiz en 3 questions, configurateur, calcul « sans
abonnement », FAQ avec `FAQPage`, avis réels, sections éditables.

## Architecture retenue (ordre mobile)

1. Premier écran : note, H1, photo produit, prix « dès » unique, trois
   preuves, bouton principal, ruban saisonnier fin (activable par dates).
2. Aiguillage des 4 parcours (pack, composer, aide au choix, caméras et
   accessoires).
3. Offres du moment : 3 cartes au plus, conditions repliées ; section
   masquée hors période.
4. Packs : une seule section, choix du pack puis de la centrale, prix et
   paiement Alma mis à jour.
5. Aide au choix : 3 centrales + quiz.
6. Configurateur et ses paliers (−10 % dès 300 €, −15 % dès 450 €,
   −20 % dès 700 €, −25 % dès 900 €).
7. Avis (boutique et Google réunis, sources indiquées).
8. Sans abonnement (calcul sur 3 ans) et application Daewoo Home Connect.
9. Accompagnement : téléphone, rappel, livraison, garantie, retour.
10. FAQ (10 questions conservées), puis appel final.

Barre mobile unique : menu, bouton « Trouver mon alarme », panier. Le
bouton s'efface quand un bouton équivalent est déjà à l'écran.

Résultat de la maquette : 7 570 px sur mobile (−46 %), H1 et photo
produit dans le premier écran.

## Maquette

- `maquette-accueil.html` : autonome (photos et police intégrées),
  sélecteur de packs fonctionnel avec les prix relevés le 17/11/2026.
- `avant-apres-premier-ecran-mobile.png`,
  `maquette-ordinateur-premier-ecran.png`.

Limites connues de la maquette :
- Le contenu détaillé des packs n'affiche que ce qui est confirmé par
  la page actuelle ; la liste complète viendra des fiches produits.
- Le bloc application n'a pas de capture d'écran : il en faut une vraie
  de Daewoo Home Connect, à fournir par le dirigeant.
- Le seuil minimal d'éligibilité Alma n'a pas été vérifié.
- Le canon à fumée (section « dissuasion ») n'y figure plus : à placer
  dans le parcours accessoires ou à réintégrer si le dirigeant y tient.

## Mesure prévue

Environ 245 sessions d'accueil par jour : un test A/B sur le taux de
conversion demanderait près de 10 mois. Critère principal proposé :
taux d'ajout au panier et clics vers offres, packs, quiz et
configurateur ; chiffre d'affaires par session suivi en parallèle.
Préalable : faire remonter les événements d'accueil dans GA4, sans
doublon avec ceux d'Addingwell.

## Prochaines étapes

1. Validation de la maquette par le dirigeant.
2. Reconnexion du connecteur Shopify, duplication du thème publié.
3. Développement en sections OS 2.0 isolées, réutilisant `dw-socle`.
4. Contrôles (parcours, variantes, performances mesurées, SEO), puis
   lien de prévisualisation et présentation avant/après.
