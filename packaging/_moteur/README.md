# Moteur de boîtes Daewoo

Ce moteur sert à l'agent `/boite-produit` (`.claude/skills/boite-produit/SKILL.md`). Il produit la boîte d'un produit dans la charte Daewoo à partir de trois éléments :
- le gabarit PDF du fabricant ;
- une fiche `produit.json` ;
- le visuel produit détouré.

## Commandes

```bash
# 1. Lire le gabarit du fabricant → gabarit.json + gabarit_apercu.png (faces repérées automatiquement)
python3 packaging/_moteur/gabarit.py <gabarit.pdf> packaging/<MODELE>

# 2. Rendu rapide avec contrôles automatiques (débordements, chevauchements, zones réservées)
python3 packaging/_moteur/construire.py packaging/<MODELE> --brouillon

# 3. Tous les livrables : dossier fournisseur, PDF CMJN/RVB, rendus 3D, aperçus
python3 packaging/_moteur/construire.py packaging/<MODELE>
```

Prérequis :
- Python 3 avec `pillow`, `numpy` et `segno` ;
- Node avec Playwright (Chromium) ;
- Ghostscript ;
- poppler-utils.

## Contenu

| Fichier | Rôle |
|---|---|
| `gabarit.py` | Lit les traits du PDF fabricant (découpe, cotes, languette, repères) et détecte la bande de 4 côtés, le couvercle, le rabat intérieur, la patte de collage et les zones réservées. Propose une attribution des faces. |
| `construire.py` | Modèles de faces (`hero`, `argument`, `application`, `dos`, `fiche`, `rabat`, `identite`) qui s'adaptent aux dimensions (paysage ou portrait), éclairages opaques, EAN-13 et QR code vectoriels, contrôles automatiques, BAT annoté en anglais et en chinois, rendus 3D, conversion CMJN avec textes vectorisés. |
| `marque.json` | Constantes de marque : couleurs, importateur, mentions légales, garantie, application, rabat. Un `produit.json` peut en surcharger n'importe quelle clé. |
| `ean.py` | Encodage EAN-13 et clé de contrôle. |
| `outils.js` | Rendu Playwright (PDF, PNG, contrôles) et captures. |
| `assets/` | Logo DAEWOO et logos réglementaires vectorisés, badges des stores, icône de l'application, polices Poppins et Noto Sans SC (sous-ensemble, complété automatiquement par npm si un caractère manque), icônes Lucide (licence ISC). |

## Tests de référence

- **EF503** (`packaging/EF503/`) : boîte 228 × 149 × 93 mm, couvercle principal. Le moteur reproduit la boîte v2 validée le 27/11/2026, sans aucune alerte.
- **Boîte haute fictive** (110 × 70 × 190 mm, testée le 27/11/2026) :
  - face principale en portrait ;
  - schéma vertical ;
  - dos empilé ;
  - fiche sur une colonne ;
  - application sur le couvercle ;
  - rabat compact.

Après toute modification du moteur, relancer EF503 en `--brouillon` et comparer ses faces avec `packaging/EF503/EF503_face_principale.png`.
