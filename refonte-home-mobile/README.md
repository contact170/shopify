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

## Version installée : « premium » (26/09/2026)

**Déjà installée** sur le thème non publié **« Copie de Version finale 26092026 »**. Le thème en ligne n'a pas été touché.

- **Aperçu sur téléphone :** https://daewoo-security.fr/?preview_theme_id=204490637652
- **Éditeur :** Shopify › Boutique en ligne › Thèmes › « Copie de Version finale 26092026 » › Personnaliser
- La home d'origine de la copie est sauvegardée dans `sauvegarde-copie-26092026/index.json.original`

### Direction artistique
- **Signature :** un écran de téléphone verrouillé, avec les notifications de l'alarme (mouvement détecté, alarme activée, « Votre abonnement ce mois-ci : 0,00 € »). En 3 secondes, le client comprend : il est prévenu sur son téléphone, sans abonnement.
- **Typographie :** Instrument Sans (titres serrés, plus premium), police système du téléphone pour les notifications.
- **Couleurs :** nuit #0B1530, encre #0C1E4A, porcelaine #F4F6FB, bleu action #1552D6, vert « protégé » #16A765 réservé au 0 €.
- **Mouvement utile uniquement :** arrivée des notifications, curseur du sélecteur de logement, barres du calcul d'économies. Tout est désactivé si le téléphone demande moins d'animations.

### Parcours (mobile)
1. **Accroche :** « L'alarme maison sans abonnement. Vous l'installez, elle vous prévient. » + prix d'appel en direct + bouton « Trouver mon alarme en 3 clics » + lien « Déjà décidé ? Voir tous les packs »
2. **Réassurance :** expédié sous 24 h, garantie 2 ans, retour sous 14 jours, support en France
3. **Quiz « Quelle alarme est faite pour vous ? »** (section `dw-home-packs`, styles `dw-home-quiz.css`) : une réponse par tap, bouton retour et barre de progression
   - Q1 : une alarme complète ou une caméra seule (la caméra mène directement à la W512MW)
   - Q2 : piloter au clavier ou au badge (Vigilia), sur un écran tactile (Touch), performance maximale (Élite), ou « je ne sais pas encore »
   - « Je ne sais pas encore » ajoute deux questions de conseil : contrainte particulière (grand terrain, dépendances, Internet instable → Élite), puis qui utilisera l'alarme (toute la famille → Vigilia, surtout des adultes → Touch). Le résultat affiche alors un encadré « Pourquoi on vous la conseille » qui reprend les réponses du client. Le lien entre réponses et centrale se règle par le champ « Profil » de chaque bloc « Centrale ».
   - Q3 : un pack prêt à poser (collection de la gamme) ou « je compose moi-même » (configurateur)
   - Résultat : photo, pourquoi elle correspond, 3 points forts, prix « dès » en direct, 0 €/mois, un bouton principal et l'autre formule en lien secondaire
   - Mesure : un événement `dwh_quiz_resultat` est envoyé dans le `dataLayer` (GTM/GA4) avec les réponses
4. **Sans abonnement :** deux cartes claires, « Alarme avec télésurveillance 35 €/mois » contre « Alarme Daewoo 0 €/mois (matériel dès 139,90 €, une seule fois) », puis le bilan honnête : « Sur 3 ans, vous gardez jusqu'à 1 120 € » (abonnements moins le prix du pack, calculé automatiquement)
5. **Avis Judge.me** (réglages actuels conservés)
6. **Pourquoi Daewoo :** marque depuis 1971, sirène 110 dB, batterie de secours, animaux jusqu'à 10 kg, déménagement
7. **FAQ :** vos 10 questions actuelles, avec les données structurées pour le SEO
8. **Appel à l'action final** + barre de boutons collante en bas d'écran sur mobile

Tous les textes, produits et liens se modifient dans l'éditeur, sans toucher au code.

## À vérifier avant la mise en ligne

- [ ] Le **tarif de 35 €/mois** de la télésurveillance (section « Sans abonnement »), modifiable dans l'éditeur
- [ ] La note « 4,6/5 · 1 356 avis » (reprise de votre hero actuel) est-elle à jour ?
- [ ] Les liens `/pages/configurateur_2`, `/pages/pack-alarmes`, `/pages/comparateur-am301-sa501-pa501z`, `/pages/contact`
- [ ] La barre collante ne doit pas chevaucher le widget de chat (en bas à droite) : à tester sur la copie
- [ ] Le configurateur (« Je compose moi-même ») ne présélectionne pas la gamme choisie dans le quiz : un lien sur mesure par gamme peut être renseigné dans chaque bloc « Centrale »
- [ ] Nettoyage avant mise en ligne : les anciens styles du sélecteur (onglets, cartes de gamme) restent dans `dw-home.css` sans être utilisés

## Comment décider (test)

Shopify ne propose pas d'A/B test natif sur la home. Deux options :
- **Simple** : publier la V2 pendant 2 à 3 semaines, puis comparer avec la période précédente sur les mêmes indicateurs (tableau ci-dessus : home mobile, ajout panier et conversion, **en isolant le trafic Google Search** pour ne pas être trompé par le trafic « direct »). Retour arrière en 1 clic en republiant l'ancien thème.
- **Rigoureux** : utiliser une app d'A/B test de thème (Shoplift, Intelligems…) pour partager le trafic 50/50.

Critère de réussite suggéré : un taux d'ajout au panier sur la home mobile qui passe de 0,65 % à plus de 1,5 %.
