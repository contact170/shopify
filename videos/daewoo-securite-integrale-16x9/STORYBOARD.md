---
format: 1920x1080
duration: 35s
message: "Une intrusion ? Votre maison réagit en une seconde — alarme, 2 caméras, sirène solaire, sans abonnement."
arc: PAS — Hook (nuit) → Détection → Riposte → Contrôle → Box coupée → Le pack → Garanties → Prix/CTA
audience: "Propriétaires et locataires français qui veulent se protéger sans abonnement"
mode: autonomous
music: "dark pulsing electronic trailer, 124 bpm, tension build then bright confident drop at the pack reveal"
sfx: dense — every reveal, cut and state change carries a sound (whoosh, hit, beep, glass tap, siren sweep, notification, pops, cash slam, riser)
voiceover: none — kinetic typography carries the words
---

## Locked

Croquis v1 validés par le client (« je valide », puis « vas-y pour la vidéo »). La composition, la hiérarchie et les textes de `storyboard.html` font foi.

## Video direction

- **Palette** (frame.md) — nuit : sol `navy-dark` #081430 → `primary` #0c1e4a (radial), texte blanc ; `promo` #e11d48 = alarme / LED / flash / prix ; `success` #037e05 = coches, « 4G », LED verte de la centrale. Jour (F6–F7) : `bg` blanc / `bg-alt` #f5f5f7, encre #1d1d1f, gris #6e6e73, navy pour les chiffres. Inter 600–900, tracking -0.02 à -0.04em, `tabular-nums` sur heures et prix.
- **Polices** — Inter uniquement, fichiers locaux `assets/fonts/Inter-400…900.woff2` (@font-face dans chaque frame).
- **Énergie** — vidéo très dynamique : chaque révélation tombe sur un temps fort (124 bpm → 1 temps = 0,484 s ; les cues ci-dessous sont des secondes locales à la frame). Entrées rapides en `expo.out` / `power4.out` (0,25–0,45 s), slams de texte = scale 1.25→1 + blur 12px→0 + léger flash, secousses caméra déterministes (amplitude décroissante, table sinus indexée, jamais Math.random) sur les impacts. Pas de rebond élastique.
- **Motion grammar** — révélation séquentielle sur les cues, jamais tout à t=0 ; un seul mouvement caméra macro par frame ; tenue finale = immobile (jitter subtil au plus). Seams internes = coupes à vitesse égale (cut-catalog).
- **Respiration** — F1 tient 0,4 s de silence lourd avant « 03:12 » ; F7 se pose sur la coche finale ; F8 tient l'URL immobile ~1,2 s à la fin.
- **Composants réels** — toujours les vraies photos détourées `assets/*.png` (formes exactes) ; la centrale Vigilia + est REconstruite en HTML d'après la photo (voir spec ci-dessous) pour pouvoir allumer ses touches et LED.
- **Spec centrale Vigilia (HTML)** — boîtier blanc cassé #f7f7f5, ratio 1,45:1 paysage, coins ~9 % de la largeur, ombre portée douce. À gauche, grille 4 colonnes × 4 rangées de touches rondes à contour gris fin (#c9c9c9, 1,5 px), chiffres gris #8a8a8a Inter 400 : rangée 1 « 1 2 3 [bouclier] », rangée 2 « 4 5 6 [bouclier] », rangée 3 « 7 8 9 [bouclier] », rangée 4 « ✕ 0 ✓ [engrenage] ». Juste à droite de la 4ᵉ colonne, une colonne de 4 petits points rouges (LED d'état). En haut à droite : LED-pilule verte #3ccf4e. À droite au milieu : zone RFID = carré arrondi à contour gris avec pictogramme sans-contact et « RFID » minuscule. En bas à droite : mot-symbole « DAEWOO » gris #9a9a9a, petit, gras. Les touches peuvent s'allumer (contour → navy/rouge) et la LED passer verte → rouge pour l'alarme.
- **Interdits** — slideshow (tout à t=0 puis figé), screensaver (éléments qui flottent indépendamment), respiration en boucle, pan lent en seconde moitié, `repeat`/`yoyo`, Math.random/Date.now, transitions CSS, texte hors des marges de sécurité (16:9 : 96 px côtés, 64 px haut/bas), statistiques inventées, carte SIM présentée comme incluse, phrases longues à l'écran.

## Frame 1 — 03:12

- scene: Nuit. L'horloge 03:12 claque plein écran, une fenêtre de façade vibre, l'écran tremble.
- voiceover: ""
- duration: 4s
- transition_in: cut
- status: animated
- src: compositions/frames/01-hook-0312.html
- type: hook
- persuasion: Pain validation (la peur de la nuit, concrète)
- beat: tension + anxiety
- blueprint: kinetic-type-beats (Adapt)
- asset_candidates: 
- on_screen: "03:12" → "Tout le monde dort." → "Une fenêtre vibre."
- sfx: t=0 drone grave + battement de cœur (0.0, 0.75, 1.5…) · 0.45 impact sourd sur « 03:12 » · 0.45→1.6 tic d'horloge chaque 0.24 s · 1.95 tintement + bourdonnement de vitre (vibration) · 2.9 impact + mini-glitch sur « Une fenêtre vibre. »
- focal: horloge « 03:12 » puis fenêtre
- roles: typographie seule + fenêtre dessinée en HTML/SVG (aucun asset photo)

Adapt : on garde la frappe plein écran du mot clé ; le « mot » est l'heure, puis la fenêtre tremble.
Scene 1 (0.0–0.45s) : sol nuit seul, vignettage fort ; un lent zoom caméra (scale 1.08→1.0 sur toute la frame, `multi-phase-camera`) démarre ; silence visuel.
Scene 2 (0.45–1.6s) : « 03:12 » SLAM au tiers haut (Inter 900, ~27 % de largeur par chiffre, tabular-nums) via `kinetic-beat-slam` + flash blanc 1 image ; eyebrow « MARDI · NUIT » se révèle au-dessus (per-letter, 0.8s) ; les deux-points clignotent en pas discrets (on/off au tempo, onUpdate déterministe, pas de repeat).
Scene 3 (1.6–2.9s) : la fenêtre (double vantail, cadre blanc, vitres bleutées, reflet diagonal) monte du bas en `expo.out` sous l'horloge ; à 1.95 elle VIBRE : tremblement haute fréquence de ±8 px décroissant sur 0.8s + ondes « (( )) » de chaque côté qui pulsent 3 fois ; « Tout le monde dort. » apparaît discrètement au-dessus du titre (fondu + montée 20 px).
Scene 4 (2.9–4.0s) : « Une fenêtre vibre. » SLAM sous la fenêtre avec `chromatic-glitch` bref (0.2s) ; secousse caméra globale sur l'impact ; tenue tendue jusqu'à la fin (lumière rouge très faible qui monte dans le bas du cadre pour annoncer l'alarme).

narrativeRole: accrocher en 1 seconde avec une situation que tout le monde redoute.
keyMessage: ça arrive la nuit, quand vous ne regardez pas.

## Frame 2 — Détecté

- scene: Gros plan sur le contacteur WDV301 posé sur le cadre de la fenêtre : LED rouge, ondes de vibration, le signal file vers la centrale Vigilia + dont le clavier s'allume.
- voiceover: ""
- duration: 3.5s
- transition_in: zoom-through
- status: animated
- src: compositions/frames/02-detecte.html
- type: product_intro
- persuasion: Show-don't-tell proof
- beat: tension → relief
- blueprint: camera-journey (Adapt — action roundtrip sans curseur)
- asset_candidates: assets/wdv301.png — contacteur WDV301 réel détouré (module + aimant)
- on_screen: "Vibration détectée" (étiquette WDV301) → "Moins d'1 seconde." → "Centrale Vigilia +"
- sfx: 0.25 bip aigu LED · 0.55 zap radio (le signal part) · 1.45 bip de clavier ×2 · 1.6 whoosh · 2.2 impact sur « Moins d'1 seconde. »
- focal: assets/wdv301.png (contacteur WDV301 réel)
- roles: wdv301 = cutout héros · centrale Vigilia + = composant HTML (spec Video direction) · cadre de fenêtre = trait sombre en arrière-plan

Adapt : on garde le voyage caméra cause → conséquence (contacteur → centrale), sans curseur.
Scene 1 (0.0–0.55s) : caméra serrée sur le WDV301 (photo réelle, ~45 % de la hauteur, haut-gauche, posé contre un montant de fenêtre sombre) ; à 0.25 une LED rouge s'allume sur sa fente centrale (point rouge + halo `ambient-glow-bloom`) ; anneaux de vibration concentriques partent du capteur ; pastille « ● Vibration détectée » (rouge translucide) glisse depuis la droite.
Scene 2 (0.55–1.45s) : le signal part — une ligne pointillée lumineuse se dessine (`svg-path-draw`) du capteur vers le bas-droite ; la caméra suit en dézoom/pan (`viewport-change`) jusqu'à révéler la centrale Vigilia + (HTML) en bas-droite.
Scene 3 (1.45–2.2s) : la centrale s'allume : rétro-éclairage des touches en cascade rapide (stagger 0.03), sa LED pilule passe verte → rouge, deux touches flashent navy ; étiquette « Centrale Vigilia + » apparaît sous elle.
Scene 4 (2.2–3.5s) : « Moins d'1 seconde. » SLAM à gauche en gros (Inter 800, 2 lignes) ; tenue.

narrativeRole: le système réagit avant que l'intrus n'entre.
keyMessage: le contacteur 2-en-1 détecte ouverture ET vibration de la vitre.

## Frame 3 — Riposte

- scene: Façade de nuit, la sirène extérieure solaire WOS305S flashe rouge, ondes sonores concentriques, l'écran pulse rouge/marine en stroboscope.
- voiceover: ""
- duration: 4s
- transition_in: cut
- status: animated
- src: compositions/frames/03-riposte.html
- type: feature_showcase
- persuasion: Negative contrast (l'intrus devient la cible)
- beat: power
- blueprint: kinetic-type-beats (Adapt)
- asset_candidates: assets/wos305s.png — sirène extérieure solaire WOS305S réelle détourée (avec panneau solaire)
- on_screen: "Visible depuis la rue." → "Entendue par tout le quartier." · pastille "☀️ Sirène solaire · sans câble"
- sfx: 0.0 montée de sirène (sweep) qui ondule toute la frame · flashs-impacts à 0.3, 0.78, 1.26, 1.74, 2.22, 2.7, 3.18 · 1.3 hit sur « Visible depuis la rue. » · 2.3 hit + sub-boom sur « Entendue par tout le quartier. »
- focal: assets/wos305s.png (sirène extérieure solaire réelle)
- roles: wos305s = cutout héros centré haut · texte = typographie

Adapt : on garde l'empilement de phrases qui claquent ; la sirène réelle est le moteur visuel.
Scene 1 (0.0–1.3s) : la sirène WOS305S (photo réelle avec son panneau solaire, ~55 % de largeur, centrée dans le tiers haut) entre en zoom-through (scale 1.4→1, blur→0) ; son bloc rouge inférieur « s'allume » : flash rouge (overlay rouge en `mix-blend-mode: screen` masqué sur la zone rouge + halo) à chaque temps (0.3, 0.78, …) avec un stroboscope plein écran (fond qui pulse rouge/marine) et des anneaux d'ondes sonores qui partent de la sirène à chaque flash ; mini-secousse caméra à chaque flash.
Scene 2 (1.3–2.3s) : pastille « ☀️ Solaire · sans câble » pop sous la sirène ; « Visible depuis la rue. » SLAM (blanc, Inter 800).
Scene 3 (2.3–4.0s) : « Entendue par tout le quartier. » SLAM en dessous (rose clair #ffd0da) avec secousse plus forte ; les flashs continuent jusqu'à la fin, amplitude des ondes décroissante.

narrativeRole: dissuasion immédiate, sonore et lumineuse.
keyMessage: la maison se défend toute seule.

## Frame 4 — Dans votre poche

- scene: Un téléphone glisse dans le cadre : notification « Daewoo Home Connect — Intrusion détectée · Fenêtre salon ». Tap → vue en direct de la caméra extérieure W512MW (vision nocturne couleur, horodatage 03:12), puis vignette caméra intérieure IP506P.
- voiceover: ""
- duration: 4.5s
- transition_in: push-slide UP
- status: animated
- src: compositions/frames/04-telephone.html
- type: feature_showcase
- persuasion: Feature-to-benefit translation (vérifier avant de réagir)
- beat: control
- blueprint: device-surface-showcase (Adapt — cursorless stepwise-flow)
- asset_candidates: assets/w512mw-nuit.jpg — vue caméra W512MW jour/nuit (moitié droite = nuit); assets/ip506p.png — caméra intérieure IP506P détourée; assets/w512mw.png — caméra extérieure W512MW détourée
- on_screen: notif → "Vous vérifiez en direct." → "2 caméras. Dedans et dehors."
- sfx: 0.25 whoosh montant (téléphone) · 0.7 ding notification · 1.5 tap · 1.6 swoosh ouverture · 1.9 bip REC · 2.9 pop vignette IP506P · 3.4 hit sur « Vous vérifiez en direct. »
- focal: téléphone construit en HTML (écran sombre) contenant assets/w512mw-nuit.jpg
- roles: w512mw-nuit.jpg = flux caméra (moitié droite de l'image = vision nocturne : recadrer sur la moitié droite) · ip506p.png = vignette caméra intérieure (cutout dans une carte) · w512mw.png = petite icône caméra sur l'en-tête du live

Adapt : on garde le parcours d'un flux réel dans l'appareil, étape par étape, sans curseur (un rond de tap blanc suffit).
Scene 1 (0.0–0.7s) : un iPhone générique (coins arrondis, cadre #2a3350, encoche-pilule) monte du bas en `expo.out` et se cale dans les 70 % hauts, légère inclinaison 3D qui se redresse.
Scene 2 (0.7–1.5s) : la notification tombe du haut de l'écran (carte blanche) : « DAEWOO HOME CONNECT · maintenant » / « Intrusion détectée » (rouge) / « Fenêtre salon · WDV301 » ; le téléphone vibre (3 petites secousses).
Scene 3 (1.5–2.9s) : tap (cercle blanc qui pulse sur la notif, `cursor-click-ripple` sans curseur) → la notif s'étend en plein écran (`card-morph-anchor`) et révèle le live caméra W512MW (vision nocturne), badge « ● REC 03:12 » rouge clignotant par pas, coins de cadrage type viseur, label « Caméra extérieure W512MW ».
Scene 4 (2.9–4.5s) : vignette « Caméra intérieure IP506P » (carte arrondie avec la photo de la caméra) glisse en bas de l'écran ; sous le téléphone : « Vous vérifiez en direct. » SLAM puis « 2 caméras. Dedans et dehors. » en gris clair ; tenue.

narrativeRole: le propriétaire reprend le contrôle, où qu'il soit.
keyMessage: alerte + preuve vidéo, instantanément sur le téléphone.

## Frame 5 — Box coupée ?

- scene: Icône Wi-Fi qui grésille et se barre (glitch), tout s'assombrit… puis la centrale bascule en 4G : badge « 4G » qui pop, bulles SMS + appel entrant.
- voiceover: ""
- duration: 3.5s
- transition_in: cut
- status: animated
- src: compositions/frames/05-box-coupee.html
- type: feature_showcase
- persuasion: Risk reversal (l'objection « et si on coupe internet ? »)
- beat: skepticism → confidence
- blueprint: kinetic-type-beats (Adapt)
- asset_candidates: 
- on_screen: "Box coupée ?" → "L'alerte passe quand même." · "SMS + appel en 4G" · mention discrète "carte SIM non fournie"
- sfx: 0.0 grésillement électrique · 0.5 coupure de courant (power-down) · 0.55→0.9 glitch · 1.2 ping 4G montant · 1.7 vibreur + son SMS · 2.15 sonnerie courte (appel) · 2.5 hit sur « L'alerte passe quand même. »
- focal: icône Wi-Fi puis badge « 4G »
- roles: typographie + icônes SVG + bulles HTML (aucun asset photo)

Scene 1 (0.0–0.55s) : l'icône Wi-Fi (3 arcs + point, blanc) grésille (`chromatic-glitch`, arcs qui s'éteignent un par un) ; « Box coupée ? » frappe dessous.
Scene 2 (0.55–1.2s) : une barre rouge barre l'icône en se dessinant (`svg-path-draw`) ; tout l'écran baisse de luminosité (coupure) avec scanlines/bruit bref.
Scene 3 (1.2–2.5s) : le badge vert « 4G » SPRING-POP au centre, une onde verte en part ; bulle SMS « Alarme : intrusion fenêtre salon » entre par la gauche, puis carte blanche « 📞 Appel entrant · Alarme » par la droite, avec vibration.
Scene 4 (2.5–3.5s) : « L'alerte passe quand même. » SLAM ; sous-ligne discrète « Wi-Fi + 4G · carte SIM non fournie » apparaît ; tenue.

narrativeRole: répondre à l'objection n°1 des alarmes connectées.
keyMessage: Wi-Fi + 4G : rien ne coupe l'alerte.

## Frame 6 — Tout dans une boîte

- scene: Bascule jour (fond blanc/gris Apple du site). Titre « Pack Sécurité Intégrale », puis chaque composant pop dans une grille avec sa quantité : centrale Vigilia +, 4× WDV301, 1× WPS305, 1× WRC305, 2× WRF301, 1× IP506P, 1× W512MW, 1× WOS305S, 2× autocollants.
- voiceover: ""
- duration: 6.5s
- transition_in: zoom-through
- status: animated
- src: compositions/frames/06-le-pack.html
- type: feature_showcase
- persuasion: Value stacking
- beat: awe + excitement
- blueprint: grid-card-assemble (Reproduce)
- asset_candidates: assets/wdv301.png — WDV301; assets/wps305-card.jpg — détecteur WPS305 sur fond studio gris; assets/wrc305.png — télécommande WRC305; assets/wrf301.png — 2 badges RFID WRF301; assets/ip506p.png — caméra IP506P; assets/w512mw.png — caméra solaire W512MW; assets/wos305s.png — sirène WOS305S; assets/stickers.png — 2 autocollants
- on_screen: "Tout ce qu'il faut, dans une seule boîte." · étiquettes courtes : "Contacteurs 2-en-1", "Mouvement · animaux ≤ 10 kg", "Télécommande", "Badges RFID", "Caméra int. Full HD", "Caméra ext. solaire 1440p", "Sirène solaire"
- sfx: 0.0 DROP musical (boom + crash) · 0.35 whoosh titre · 1.0 impact doux centrale · puis un pop/click par carte à 1.55, 1.85, 2.15, 2.45, 2.75, 3.05, 3.35, 3.65 · 4.2 hit « 13 éléments » · 5.0 shimmer
- focal: centrale Vigilia + (composant HTML) au centre-haut
- roles: wdv301.png, wps305-card.jpg (photo dans sa carte, fond studio gris conservé), wrc305.png, wrf301.png, ip506p.png, w512mw.png, wos305s.png, stickers.png = cutouts dans des cartes blanches arrondies avec pastille de quantité navy

Scene 1 (0.0–1.0s) : bascule jour : fond `bg-alt` ; eyebrow « ● PACK SÉCURITÉ INTÉGRALE » (point vert) puis titre « Tout ce qu'il faut, dans une seule boîte. » en `waterfall-entry` (mots qui montent en vague).
Scene 2 (1.0–1.55s) : la centrale Vigilia + (HTML, spec Video direction) arrive au centre en zoom-through inverse (scale 1.6→1, blur→0), sa LED verte s'allume.
Scene 3 (1.55–4.2s) : grille 3×3 sous la centrale : 8 cartes blanches (radius 14px, bordure navy 20 %) arrivent une par une sur chaque temps (`spring-pop-entrance` sans rebond : scale 0.6→1 + y 40→0, expo.out), chacune avec sa photo réelle, sa pastille quantité (4×, 1×, 1×, 2×, 1×, 1×, 1×, 2×) et un libellé court : « Contacteurs 2-en-1 », « Mouvement · animaux ≤ 10 kg », « Télécommande », « Badges RFID », « Caméra int. Full HD », « Caméra ext. solaire 1440p », « Sirène solaire », « Autocollants ».
Scene 4 (4.2–6.5s) : 9ᵉ case pleine navy « 13 éléments » pop ; un reflet lumineux balaie toute la grille une fois (`ambient-glow-bloom`, sheen) ; tenue immobile.

narrativeRole: montrer l'abondance — c'est un système complet, pas un gadget.
keyMessage: intérieur, extérieur, jour et nuit — tout est inclus.

## Frame 7 — Sans abonnement

- scene: Compteur « €/mois » qui s'emballe puis s'écrase sur « 0 € », puis rafale de garanties qui claquent une à une avec la coche verte du site.
- voiceover: ""
- duration: 4s
- transition_in: push-slide LEFT
- status: animated
- src: compositions/frames/07-sans-abonnement.html
- type: benefit_highlight
- persuasion: Rule of three + risk reversal
- beat: relief + trust
- blueprint: dataviz-countup (Adapt)
- asset_candidates: 
- on_screen: "0 € d'abonnement. À vie." → ✓ Installation sans technicien · ✓ Expédié sous 24 h · ✓ Garantie 2 ans
- sfx: 0.0→0.9 tic-tic de compteur qui accélère · 0.95 SLAM (impact + cymbale inversée coupée) · 1.45 hit « À vie. » · 2.2, 2.7, 3.2 trois dings avec coche
- focal: le « 0 € » géant
- roles: typographie seule

Adapt : le compteur ne monte pas, il S'ÉCRASE — un rouleau de chiffres flous défile puis s'arrête net sur 0.
Scene 1 (0.0–0.95s) : « Abonnement mensuel » en gris ; dessous, un rouleau vertical de chiffres « €/mois » flous qui défile de plus en plus vite (`vertical-spring-ticker`, motion-blur), aucun montant lisible.
Scene 2 (0.95–1.45s) : le rouleau s'arrête : « 0 € » géant navy SLAM (Inter 900) avec secousse ; la ligne « –– € / mois · –– € / mois » se raye en rouge dessous.
Scene 3 (1.45–2.2s) : « À vie. » SLAM sous le 0 €.
Scene 4 (2.2–4.0s) : trois lignes à coche verte qui claquent une par une sur les temps : « ✓ Installation sans technicien », « ✓ Expédié sous 24 h », « ✓ Garantie 2 ans » (la coche se dessine `svg-path-draw`, le texte glisse depuis la gauche) ; tenue.

narrativeRole: lever les freins du prix récurrent et de l'installation.
keyMessage: vous payez une fois, le système vous appartient.

## Frame 8 — L'offre

- scene: Le pack se recompose en hero, prix barré 475,58 € rayé en rouge, 349,90 € slam, pastille « -26 % », compte à rebours « Jusqu'au 31 octobre », bouton « daewoo-security.fr ».
- voiceover: ""
- duration: 5.5s
- transition_in: zoom-through
- status: animated
- src: compositions/frames/08-offre.html
- type: cta
- persuasion: Scarcity/urgency + value anchoring
- beat: urgency-to-act
- blueprint: logo-assemble-lockup (Adapt)
- asset_candidates: assets/pack.jpg — photo officielle du pack Vigilia + complet (fond blanc); assets/logo-white.png — logo DAEWOO blanc transparent
- on_screen: "Pack Sécurité Intégrale · Vigilia +" · ~~475,58 €~~ · "349,90 €" · "-26 %" · "Offre jusqu'au 31 octobre" · "daewoo-security.fr"
- sfx: 0.0 riser (monte jusqu'à 1.9) · 0.3 whoosh carte · 1.3 rayure (strike) sur le prix barré · 1.9 CASH SLAM + boom sur 349,90 € · 2.6 pop « -26 % » · 3.2 tick « Jusqu'au 31 octobre » · 3.8 click bouton URL · 4.2→5.5 queue de réverbe / outro
- focal: assets/pack.jpg (photo officielle du pack Vigilia + complet, fond blanc, dans une carte blanche arrondie)
- roles: pack.jpg = hero dans carte blanche (pas de détourage) · logo-white.png = logo DAEWOO en haut · typographie prix

Adapt : on garde la construction finale en lockup, terminée sur l'URL ; la marque est le logo DAEWOO réel.
Scene 1 (0.0–0.3s) : retour nuit (radial navy) ; logo DAEWOO blanc (logo-white.png, ~40 % de largeur) se dessine en haut par un wipe gauche→droite.
Scene 2 (0.3–1.3s) : la carte blanche du pack (photo pack.jpg, ~72 % de largeur) arrive en zoom-through inverse et se pose dans le tiers haut ; « Pack Sécurité Intégrale · Vigilia + » apparaît dessous (per-word).
Scene 3 (1.3–2.6s) : « 475,58 € » apparaît en gris puis se fait rayer par un trait rouge qui se dessine ; à 1.9 « 349,90 € » SLAM géant (Inter 900, blanc) avec flash, secousse et `particle-burst` discret (étincelles navy/rouges déterministes) ; pastille rouge « Offre spéciale · -26 % » pop au-dessus de la carte à 2.6.
Scene 4 (2.6–4.2s) : « Jusqu'au 31 octobre · Sans abonnement » se révèle ; bouton-pilule blanc « daewoo-security.fr » pop (press-release-spring) à 3.8.
Scene 5 (4.2–5.5s) : tenue immobile (frame finale) ; dernière 0.4 s : léger fondu au noir global autorisé (c'est la dernière frame).

narrativeRole: convertir — prix ancré, urgence datée, destination claire.
keyMessage: 349,90 € au lieu de 475,58 €, jusqu'au 31 octobre.
