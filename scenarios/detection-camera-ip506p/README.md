# Scénario — Détection de la caméra IP506P selon l'état de l'alarme

Scénario **prioritaire**. Objectif : lier la **détection de mouvement de la caméra Daewoo IP506P Full HD**
à l'état de la centrale **Vigilia**, dans les deux sens.

- **Scénario principal :** SI l'alarme est **Armée** → ALORS **activer la détection de mouvement** de la IP506P.
- **Scénario inverse :** SI l'alarme est **Désarmée** → ALORS **désactiver la détection de mouvement** de la IP506P.

## Variante à expliquer sur la page — Mode Vie privée

Pour la **IP506P**, on peut aussi créer le scénario suivant :

- SI l'alarme est **Désarmée** → ALORS **activer le Mode Vie privée** (la caméra se **referme** physiquement / masque l'objectif).

> **Important à préciser sur la page :**
> Le **Mode Vie privée ne coupe PAS la détection de mouvement**.
> La caméra continue de détecter les mouvements même objectif fermé ; le Mode Vie privée
> ne fait que masquer l'image (confidentialité), il ne désactive pas la détection.
>
> → Si vous voulez réellement **couper la détection** quand vous êtes chez vous, utilisez le
> **scénario inverse** ci-dessus (Désarmée → détection OFF), et non le Mode Vie privée.

## Où déposer les captures d'écran

Glissez vos fichiers PNG **dans ce dossier** (`scenarios/detection-camera-ip506p/`).
Renommez-les si possible selon l'ordre ci-dessous.

### A. Scénario principal — Armée → détection caméra ON

| Fichier | Étape | Écran / clic |
|---------|-------|--------------|
| `01-accueil.png`        | 1  | Accueil → **+** en haut à droite → *Créer une scène* |
| `02-condition.png`      | 2  | *Lorsque le statut de l'appareil change* → *Sélectionner un seul appareil* |
| `03-choix-alarme.png`   | 3  | Choisir l'alarme **Vigilia** dans la liste |
| `04-armer.png`          | 4  | **Mode → Armer → Confirmer** |
| `05-alors.png`          | 5  | Partie **ALORS** → le **+** à droite |
| `06-choix-camera.png`   | 6  | *Appareil* → **Daewoo IP506P Full HD** |
| `07-action-detection.png` | 7 | Choisir l'action **Détection de mouvement** → **ON / Activer** |
| `08-validite.png`       | 8  | **Périmètre de validité** → *Terminé* |
| `09-nom.png`            | 9  | **Enregistrer & nommer** (ex. « Détection caméra si armée ») |
| `10-test.png`           | 10 | Test (détection active quand l'alarme est armée) |

### B. Scénario inverse — Désarmée → détection caméra OFF

| Fichier | Étape | Écran / clic |
|---------|-------|--------------|
| `inv-04-desarmer.png`   | condition | **Mode → Désarmer → Confirmer** |
| `inv-07-detection-off.png` | action | **Détection de mouvement → OFF / Désactiver** |
| `inv-09-nom.png`        | nom | ex. « Détection caméra OFF si désarmée » |

*(Les étapes 1-3, 5-6, 8 sont identiques au scénario principal — inutile de refaire ces captures.)*

### C. Variante Mode Vie privée — Désarmée → Vie privée ON

| Fichier | Étape | Écran / clic |
|---------|-------|--------------|
| `vp-07-action-vie-privee.png` | action | Choisir l'action **Mode Vie privée** → **ON / Activer** |
| `vp-nom.png`            | nom | ex. « Vie privée si désarmée » |

## Rappel du format
- Captures d'écran de l'app (format mobile vertical), une par étape.
- Une fois poussées, je grave les **flèches** sur chaque capture et je monte une **vidéo compacte**,
  comme pour le scénario « Prise ON si armée ».
