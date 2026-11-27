# Découpe chaque face depuis le rendu à plat : python3 crop_faces.py <rendu.png> <dossier_sortie>
import sys, os
from PIL import Image
Image.MAX_IMAGE_PIXELS = None
im = Image.open(sys.argv[1]); out = sys.argv[2]; os.makedirs(out, exist_ok=True)
s = im.width / 802
P = {'LID': (124.53, 274.38, 227.9, 148.93), 'P1': (124.53, 423.31, 227.9, 92.96), 'P2': (352.43, 423.31, 148.94, 92.96),
     'P3': (501.37, 423.31, 227.89, 92.96), 'P4': (729.26, 423.31, 148.94, 92.96), 'INNER': (501.37, 281.56, 227.89, 141.75)}
for k, (x, y, w, h) in P.items():
    im.crop(tuple(int(round(v * s)) for v in (x - 91, y - 239, x - 91 + w, y - 239 + h))).save(os.path.join(out, f'{k}.png'))
