# Scénario — « Prise ON si armée »

Allumer la prise connectée **SP502F** automatiquement quand la centrale **Vigilia** est armée
(fonction *Scène / Intelligent* de l'application Daewoo).

## Où déposer les captures d'écran

Glissez vos fichiers PNG **dans ce dossier** (`scenarios/prise-on-si-armee/`).

## Liste de tournage (10 étapes)

| Fichier | Étape | Écran / clic |
|---------|-------|--------------|
| `01-accueil.png`       | 1  | Accueil → **+** en haut à droite → *Créer une scène* |
| `02-condition.png`     | 2  | *Lorsque le statut de l'appareil change* → *Sélectionner un seul appareil* |
| `03-choix-alarme.png`  | 3  | Choisir l'alarme **Vigilia** dans la liste |
| `04-armer.png`         | 4  | **Mode → Armer → Confirmer** |
| `05-alors.png`         | 5  | Partie **ALORS** → le **+** à droite |
| `06-choix-prise.png`   | 6  | *Appareil* → prise **SP502F** |
| `07-prise-on.png`      | 7  | **Ma prise → ON → Confirmer** |
| `08-validite.png`      | 8  | **Périmètre de validité** (périodes / répétition) |
| `09-nom.png`           | 9  | **Enregistrer & nommer** (« Prise on si armée ») |
| `10-test-accueil.png`  | 10 | Test : accueil avec la prise **verte (ON)** |
| `10-test-centrale.png` | 10 | Test : centrale **armée** (preuve) |

**Déjà reçues :** étapes 1, 4, 7, 8, 9 + preuve.
**Manquantes :** étapes **2, 3, 5, 6**.
