---
format: 1080x1920
duration: 35s
message: "Une intrusion ? Votre maison réagit en une seconde — alarme, 2 caméras, sirène solaire, sans abonnement."
arc: PAS — Hook (nuit) → Détection → Riposte → Contrôle → Box coupée → Le pack → Garanties → Prix/CTA
audience: "Propriétaires et locataires français qui veulent se protéger sans abonnement"
mode: collaborative
music: "dark pulsing electronic trailer, 124 bpm, tension build then bright confident drop at the pack reveal"
sfx: dense — every reveal, cut and state change carries a sound (whoosh, hit, beep, glass tap, siren sweep, notification, pops, cash slam, riser)
voiceover: none — kinetic typography carries the words
---

## Frame 1 — 03:12

- scene: Nuit. L'horloge 03:12 claque plein écran, une fenêtre de façade vibre, l'écran tremble.
- voiceover: ""
- duration: 4s
- transition_in: cut
- status: outline
- src: compositions/frames/01-hook-0312.html
- type: hook
- persuasion: Pain validation (la peur de la nuit, concrète)
- beat: tension + anxiety
- blueprint: kinetic-type-beats
- asset_candidates:
- on_screen: "03:12" → "Tout le monde dort." → "Une fenêtre vibre."
- sfx: drone grave, battement de cœur, tic d'horloge, impact sourd, vibration de vitre

narrativeRole: accrocher en 1 seconde avec une situation que tout le monde redoute.
keyMessage: ça arrive la nuit, quand vous ne regardez pas.

## Frame 2 — Détecté

- scene: Gros plan sur le contacteur WDV301 posé sur le cadre de la fenêtre : LED rouge, ondes de vibration, le signal file vers la centrale Vigilia + dont le clavier s'allume.
- voiceover: ""
- duration: 3.5s
- transition_in: zoom-through
- status: outline
- src: compositions/frames/02-detecte.html
- type: product_intro
- persuasion: Show-don't-tell proof
- beat: tension → relief
- blueprint: camera-journey
- asset_candidates: assets/wdv301.webp — contacteur WDV301 (module + aimant); assets/vigilia.webp — centrale Vigilia +
- on_screen: "Vibration détectée" (étiquette WDV301) → "Moins d'1 seconde." → "Centrale Vigilia +"
- sfx: bip LED, onde radio (zap), bip de clavier, whoosh

narrativeRole: le système réagit avant que l'intrus n'entre.
keyMessage: le contacteur 2-en-1 détecte ouverture ET vibration de la vitre.

## Frame 3 — Riposte

- scene: Façade de nuit, la sirène extérieure solaire WOS305S flashe rouge, ondes sonores concentriques, l'écran pulse rouge/marine en stroboscope.
- voiceover: ""
- duration: 4s
- transition_in: cut
- status: outline
- src: compositions/frames/03-riposte.html
- type: feature_showcase
- persuasion: Negative contrast (l'intrus devient la cible)
- beat: power
- blueprint: kinetic-type-beats
- asset_candidates: assets/wos305s.webp — sirène extérieure solaire WOS305S
- on_screen: "Visible depuis la rue." → "Entendue par tout le quartier." · pastille "☀️ Sirène solaire · sans câble"
- sfx: montée de sirène (sweep), impacts synchronisés au flash, sub-boom

narrativeRole: dissuasion immédiate, sonore et lumineuse.
keyMessage: la maison se défend toute seule.

## Frame 4 — Dans votre poche

- scene: Un téléphone glisse dans le cadre : notification « Daewoo Home Connect — Intrusion détectée · Fenêtre salon ». Tap → vue en direct de la caméra extérieure W512MW (vision nocturne couleur, horodatage 03:12), puis vignette caméra intérieure IP506P.
- voiceover: ""
- duration: 4.5s
- transition_in: push-slide UP
- status: outline
- src: compositions/frames/04-telephone.html
- type: feature_showcase
- persuasion: Feature-to-benefit translation (vérifier avant de réagir)
- beat: control
- blueprint: device-surface-showcase
- asset_candidates: assets/w512mw.webp — caméra extérieure solaire W512MW; assets/ip506p.webp — caméra intérieure IP506P
- on_screen: notif → "Vous vérifiez en direct." → "2 caméras. Dedans et dehors."
- sfx: ding de notification, tap, swoosh d'ouverture, bip REC

narrativeRole: le propriétaire reprend le contrôle, où qu'il soit.
keyMessage: alerte + preuve vidéo, instantanément sur le téléphone.

## Frame 5 — Box coupée ?

- scene: Icône Wi-Fi qui grésille et se barre (glitch), tout s'assombrit… puis la centrale bascule en 4G : badge « 4G » qui pop, bulles SMS + appel entrant.
- voiceover: ""
- duration: 3.5s
- transition_in: cut
- status: outline
- src: compositions/frames/05-box-coupee.html
- type: feature_showcase
- persuasion: Risk reversal (l'objection « et si on coupe internet ? »)
- beat: skepticism → confidence
- blueprint: kinetic-type-beats
- asset_candidates:
- on_screen: "Box coupée ?" → "L'alerte passe quand même." · "SMS + appel en 4G" · mention discrète "carte SIM non fournie"
- sfx: power-down, glitch, ping 4G, vibreur

narrativeRole: répondre à l'objection n°1 des alarmes connectées.
keyMessage: Wi-Fi + 4G : rien ne coupe l'alerte.

## Frame 6 — Tout dans une boîte

- scene: Bascule jour (fond blanc/gris Apple du site). Titre « Pack Sécurité Intégrale », puis chaque composant pop dans une grille avec sa quantité : centrale Vigilia +, 4× WDV301, 1× WPS305, 1× WRC305, 2× WRF301, 1× IP506P, 1× W512MW, 1× WOS305S, 2× autocollants.
- voiceover: ""
- duration: 6.5s
- transition_in: zoom-through
- status: outline
- src: compositions/frames/06-le-pack.html
- type: feature_showcase
- persuasion: Value stacking
- beat: awe + excitement
- blueprint: grid-card-assemble
- asset_candidates: assets/vigilia.webp; assets/wdv301.webp; assets/wps305.webp; assets/wrc305.webp; assets/wrf301.webp; assets/ip506p.webp; assets/w512mw.webp; assets/wos305s.webp; assets/stickers.webp
- on_screen: "Tout ce qu'il faut, dans une seule boîte." · étiquettes courtes : "Contacteurs 2-en-1", "Mouvement · animaux ≤ 10 kg", "Télécommande", "Badges RFID", "Caméra int. Full HD", "Caméra ext. solaire 1440p", "Sirène solaire"
- sfx: drop musical, un pop/click par composant (cascade rapide), whoosh final

narrativeRole: montrer l'abondance — c'est un système complet, pas un gadget.
keyMessage: intérieur, extérieur, jour et nuit — tout est inclus.

## Frame 7 — Sans abonnement

- scene: Compteur « €/mois » qui s'emballe puis s'écrase sur « 0 € », puis rafale de garanties qui claquent une à une avec la coche verte du site.
- voiceover: ""
- duration: 4s
- transition_in: push-slide LEFT
- status: outline
- src: compositions/frames/07-sans-abonnement.html
- type: benefit_highlight
- persuasion: Rule of three + risk reversal
- beat: relief + trust
- blueprint: dataviz-countup
- asset_candidates:
- on_screen: "0 € d'abonnement. À vie." → ✓ Installation sans technicien · ✓ Expédié sous 24 h · ✓ Garantie 2 ans
- sfx: tic-tic de compteur accéléré, slam, 3 hits avec ding

narrativeRole: lever les freins du prix récurrent et de l'installation.
keyMessage: vous payez une fois, le système vous appartient.

## Frame 8 — L'offre

- scene: Le pack se recompose en hero, prix barré 475,58 € rayé en rouge, 349,90 € slam, pastille « -26 % », compte à rebours « Jusqu'au 31 octobre », bouton « daewoo-security.fr ».
- voiceover: ""
- duration: 5.5s
- transition_in: zoom-through
- status: outline
- src: compositions/frames/08-offre.html
- type: cta
- persuasion: Scarcity/urgency + value anchoring
- beat: urgency-to-act
- blueprint: logo-assemble-lockup
- asset_candidates: assets/vigilia.webp — centrale hero; assets/logo.svg — logo Daewoo Security
- on_screen: "Pack Sécurité Intégrale · Vigilia +" · ~~475,58 €~~ · "349,90 €" · "-26 %" · "Offre jusqu'au 31 octobre" · "daewoo-security.fr"
- sfx: riser, cash slam, strike (rayure), boom final + queue de réverbe

narrativeRole: convertir — prix ancré, urgence datée, destination claire.
keyMessage: 349,90 € au lieu de 475,58 €, jusqu'au 31 octobre.
