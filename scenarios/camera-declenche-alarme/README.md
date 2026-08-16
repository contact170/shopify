# Scénario — Si la caméra détecte un mouvement, ALORS déclencher l'alarme

Scénario **prioritaire** (Touch / Vigilia / Key). Ici la logique est **inversée** par rapport aux autres :
la **caméra IP506P** devient la **condition**, et l'**alarme** devient l'**action**.

- **SI** la caméra **IP506P** détecte un **mouvement**
- **ALORS** on **déclenche / arme l'alarme**.

## Vous n'avez que 7 images à envoyer

Les **5 premiers écrans sont identiques** aux autres scénarios (accueil → +, *Créer une scène*,
*Lorsque le statut de l'appareil change*, *Sélectionner un seul appareil*, liste des appareils).
**Je les réutilise automatiquement** — inutile de les renvoyer.

## Où déposer les 7 captures

Glissez vos fichiers PNG **dans ce dossier** (`scenarios/camera-declenche-alarme/`).
Nommez-les si possible `06 … 12` selon l'ordre ci-dessous (adaptez si l'app diffère) :

| Fichier | Étape | Écran / clic (à confirmer) |
|---------|-------|----------------------------|
| `06-choix-camera.png`     | 6  | Dans la liste, choisir la **caméra IP506P** (comme déclencheur) |
| `07-fonction-detection.png` | 7 | Fonctions IP506P → **Détection de mouvement** |
| `08-etat-detection.png`   | 8  | État déclencheur de la détection (ex. **Détecté / On**) → Confirmer |
| `09-alors.png`            | 9  | Partie **ALORS** → le **+** à droite |
| `10-action-alarme.png`    | 10 | Choisir l'action côté **alarme** (Appareil → Vigilia, ou *Sélectionnez une action*) |
| `11-mode-armer.png`       | 11 | Régler l'action : **Armer / déclencher l'alarme** → Confirmer |
| `12-nom-enregistrer.png`  | 12 | **Enregistrer & nommer** (ex. « Alarme si caméra détecte ») + test |

*(Si votre parcours compte une capture de plus ou de moins, envoyez ce que vous avez et
précisez l'ordre — je m'adapte.)*

## Détails utiles pour la mise en forme
- Précisez pour chaque image **où vous avez appuyé** (un mot suffit) si ce n'est pas évident.
- Comme d'habitude : une fois poussées, je grave les **flèches** et je monte la **vidéo compacte**.
- Pensez au **sens inverse / à la temporisation** si pertinent — dites-moi si vous voulez une note
  spécifique sur cette page (ex. délai avant déclenchement, mode nuit, etc.).
