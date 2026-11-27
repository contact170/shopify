#!/usr/bin/env bash
# Régénère tous les livrables de la boîte EF503.
# Usage : ./build_all.sh [dossier_livrables] [dossier_temporaire]
set -euo pipefail
cd "$(dirname "$0")"
OUT=$(realpath "${1:-../..}"); TMP=$(realpath -m "${2:-/tmp/ef503_build}")
mkdir -p "$TMP/faces"
GS="gs -q -dSAFER -dBATCH -dNOPAUSE -sDEVICE=pdfwrite -sColorConversionStrategy=CMYK -sProcessColorModel=DeviceCMYK -dCompatibilityLevel=1.6 -dAutoRotatePages=/None -dNoOutputFonts"

python3 make.py print box_print.html
python3 make.py proof box_proof.html
node render.js box_print.html "$TMP/print" pdf 3
node render.js box_proof.html "$TMP/proof" pdf 2
rm -f box_print.html box_proof.html

python3 crop_faces.py "$TMP/print.png" "$TMP/faces"
for v in front back; do
  python3 mockup.py $v "$TMP"
  node shot.js "$TMP/mockup_$v.html" "$TMP/mockup_$v.png" 1600 1100 2
done
python3 make_ref.py "$TMP"
node render.js "$TMP/ref.html" "$TMP/ref" pdf 1

# Dossier fournisseur (3 pages, CMJN, textes vectorisés) + fichier d'impression seul
$GS -sOutputFile="$OUT/EF503_DAEWOO_dossier_fournisseur.pdf" "$TMP/proof.pdf" "$TMP/print.pdf" "$TMP/ref.pdf"
$GS -sOutputFile="$OUT/EF503_impression_CMJN.pdf" "$TMP/print.pdf"
cp "$TMP/print.pdf" "$OUT/EF503_impression_RVB.pdf"

python3 - "$TMP" "$OUT" <<'PY'
import sys
from PIL import Image
Image.MAX_IMAGE_PIXELS = None
tmp, out = sys.argv[1], sys.argv[2]
for v, n in (('front', 'avant'), ('back', 'arriere')):
    Image.open(f'{tmp}/mockup_{v}.png').convert('RGB').save(f'{out}/EF503_maquette_3D_{n}.jpg', quality=92, subsampling=0)
im = Image.open(f'{tmp}/proof.png').convert('RGB'); im.thumbnail((4000, 4000)); im.save(f'{out}/EF503_a_plat_avec_gabarit.png', optimize=True)
Image.open(f'{tmp}/faces/LID.png').convert('RGB').save(f'{out}/EF503_face_principale.png', optimize=True)
PY
echo "Livrables écrits dans $OUT"
