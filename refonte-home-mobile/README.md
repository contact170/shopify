# Refonte home page — version mobile first (V2)

**Statut : proposition, rien n'est en ligne.** À installer uniquement sur une **copie** du thème publié.

## Pourquoi cette refonte (chiffres Shopify, 30 derniers jours)

| | Sessions | Ajout panier | Conversion |
|---|---|---|---|
| Mobile (toutes pages) | 18 125 (83 %) | 2,1 % | **0,35 %** |
| Desktop (toutes pages) | 3 411 | 6,4 % | **2,05 %** |
| **Home en mobile** | **11 220** | 0,65 % | **0,09 %** |
| Page comparateur en mobile | 1 021 | 8,3 % | 1,27 % |

La home concentre 62 % des entrées mobiles et presque aucune vente.
⚠️ Sur ces 11 220 sessions, **10 050 sont en « direct »** (0,06 % de conversion). Le trafic Google Search qui arrive sur la même home convertit à 1,09 %. Une partie du problème vient donc de la **qualité ou du suivi du trafic** (publicités sans UTM, navigateurs intégrés à Facebook ou Instagram, bots), pas seulement de la page. À analyser en parallèle.

## Structure de la nouvelle home (environ 7 écrans mobiles au lieu de ~18 sections)

1. **Hero** : promesse en une phrase, 3 bénéfices, 2 boutons (packs / configurateur), note clients, prix d'appel
2. **Barre de réassurance** : 0 € d'abonnement, livraison offerte, garantie 2 ans, SAV en France
3. **Comment ça marche** : 3 étapes
4. **Packs guidés par logement** : onglets Appartement / Maison / Grande maison (un seul pack affiché à la fois sur mobile), puis les 3 portes de sortie : configurateur, quiz, caméra seule (best-seller W512MW), plus le lien vers le comparatif
5. **Sans abonnement** : comparaison chiffrée avec la télésurveillance
6. **Avis clients** : le carrousel Judge.me actuel, conservé
7. **Pourquoi nous** : chiffres clés, SAV Mérignac, Wi-Fi coupé, animaux, application gratuite
8. **FAQ** : 6 objections fréquentes, avec les données structurées FAQ pour le SEO
9. **Appel à l'action final**
10. **Barre d'action collante sur mobile** : elle apparaît après le hero et se masque sur les packs, le CTA final et le footer

Les prix sont **lus en direct** dans Shopify (produits choisis dans l'éditeur), avec le paiement en 4× calculé automatiquement.
Aucune police externe n'est chargée (Poppins du thème) : la page est plus légère que l'actuelle.

## Installation sur une copie du thème (sans risque)

1. Shopify › Boutique en ligne › Thèmes › thème publié › **⋯ › Dupliquer**. Renommez la copie, par exemple « Home V2 – TEST ».
2. Sur la **copie** : ⋯ › **Modifier le code**, puis ajoutez :
   - `assets/dw-home.css`
   - `snippets/dw-home-icon.liquid`
   - les 7 fichiers `sections/dw-home-*.liquid`
3. Dans la copie, ouvrez `templates/index.json`, **sauvegardez son contenu** (copier-coller dans un fichier), puis remplacez-le par `templates/index.json` de ce dossier.
   Le bloc d'avis Judge.me y est déjà repris.
4. Ouvrez l'éditeur de la copie :
   - vérifiez les 3 produits des packs (et changez-les si besoin, par exemple pour des packs plus complets)
   - ajoutez une **photo en situation** dans le hero (pour l'instant c'est l'image produit qui s'affiche) : c'est le levier visuel le plus fort
   - remplissez le bandeau promo si une offre est en cours
5. Utilisez **Aperçu › Partager l'aperçu** pour tester sur votre téléphone.

## À vérifier avant la mise en ligne

- [ ] Le **tarif de 35 €/mois** de la télésurveillance (section « Sans abonnement »), modifiable dans l'éditeur
- [ ] La note « 4,6/5 · 900+ avis » et le chiffre « 60 000 foyers » : sont-ils toujours d'actualité ?
- [ ] Les liens `/pages/configurateur_2`, `/pages/trouver-mon-alarme-quiz`, `/pages/comparateur-am301-sa501-pa501z`, `/pages/contact`
- [ ] La barre collante ne doit pas chevaucher le widget de chat (en bas à droite) : à tester sur la copie
- [ ] Les montants Alma (4× sans frais) doivent correspondre à votre contrat

## Comment décider (test)

Shopify ne propose pas d'A/B test natif sur la home. Deux options :
- **Simple** : publier la V2 pendant 2 à 3 semaines, puis comparer avec la période précédente sur les mêmes indicateurs (tableau ci-dessus : home mobile, ajout panier et conversion, **en isolant le trafic Google Search** pour ne pas être trompé par le trafic « direct »). Retour arrière en 1 clic en republiant l'ancien thème.
- **Rigoureux** : utiliser une app d'A/B test de thème (Shoplift, Intelligems…) pour partager le trafic 50/50.

Critère de réussite suggéré : un taux d'ajout au panier sur la home mobile qui passe de 0,65 % à plus de 1,5 %.
