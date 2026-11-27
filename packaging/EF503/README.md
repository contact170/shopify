# Boîte DAEWOO EF503 — caméra extérieure PoE

Habillage Daewoo sur le gabarit du fabricant : boîte TS58 de **228 × 149 × 93 mm**, carton 300 g blanc renforcé W9, pelliculage mat, impression en quadrichromie. Version actuelle : **v2 (27/11/2026)**.

## Fichiers

| Fichier | Usage |
|---|---|
| **`EF503_DAEWOO_dossier_fournisseur.pdf`** | **Fichier à envoyer au fournisseur.** 3 pages en CMJN, textes vectorisés, annotations en anglais et en chinois. Page 1 : contrôle de calage sur le tracé de découpe. Page 2 : fichier d'impression avec fond perdu de 3 mm. Page 3 : rendus 3D de référence. |
| `EF503_impression_CMJN.pdf` | Page 2 seule : fichier d'impression en CMJN, textes vectorisés |
| `EF503_impression_RVB.pdf` | Même fichier d'impression en RVB, polices intégrées |
| `EF503_maquette_3D_avant.jpg` / `_arriere.jpg` | Rendus 3D de la boîte fermée |
| `EF503_a_plat_avec_gabarit.png` | Aperçu à plat avec le tracé de découpe |
| `EF503_face_principale.png` | Face principale seule, pour la fiche produit ou les réseaux sociaux |

## Répartition des faces

- **Couvercle (face principale)** : logo, EF503, visuel produit, arguments PoE (avec adaptateur secteur inclus), 1080p et Métal, « Sans abonnement », pictos.
- **Face avant** : explication du PoE (un seul câble pour l'image et l'alimentation), alternative avec l'adaptateur secteur fourni (câble de 3 m), schéma de raccordement.
- **Côté droit** : application Daewoo Home Connect (QR code, badges des stores) et engagements de la marque.
- **Dos** : caractéristiques en 4 langues, mentions légales, importateur, EAN 3760285866513, logos réglementaires, encart blanc pour l'étiquette usine.
- **Côté gauche** : fiche technique FR/EN.
- **Rabat intérieur** (imprimé tête-bêche, visible à l'ouverture) : message de bienvenue et 3 étapes d'installation.

## Modifications v2

- Adaptateur secteur inclus, avec un câble d'alimentation de 3 m : mentionné sur le couvercle, la face avant, le dos (4 langues), la fiche technique et le rabat intérieur.
- Carte microSD : jusqu'à 128 Go (au lieu de 256 Go).
- Vision nocturne : « infrarouge ou couleur », sans distance.
- Fiche technique : « Zones » retiré de la ligne Détection. Le poids est regroupé avec les dimensions pour libérer une ligne au câble d'alimentation.

## Points restant à vérifier

1. **QR code** : c'est le même lien que sur l'IP506P (`a.smart321.com/kodaksmartlife`). Vérifier qu'il ouvre bien Daewoo Home Connect.
2. **Adresse de l'importateur** : 15 Allée James Watt, Immeuble 2000 Watt, 33700 Mérignac. L'adresse de la boutique dans l'admin Shopify est encore l'ancienne.
3. **Sens du couvercle** : il se lit depuis la face avant. À vérifier sur une maquette blanche à cause de la languette de suspension.
4. **Logo Triman et Info-tri** : obligatoires en France, ils ne figuraient pas sur l'IP506P. À vérifier avec votre éco-organisme.

## Régénérer les fichiers

La boîte est décrite par `produit.json`, `gabarit.json` et `images/EF503.png`. Elle se reconstruit avec le moteur commun `packaging/_moteur/` (c'est aussi l'exemple de référence de l'agent `/boite-produit`) :

```bash
python3 packaging/_moteur/construire.py packaging/EF503 --brouillon   # contrôle rapide
python3 packaging/_moteur/construire.py packaging/EF503               # tous les livrables
```

Le build complet réécrit les fichiers de ce dossier. Les fichiers v2 livrés le 27/11/2026 ont été produits par le premier script, propre à l'EF503 (historique git, commit a83b7e5). Le moteur reproduit le même design ; seuls quelques blocs (badges des stores, note PoE) sont décalés de 1 à 3 mm.
