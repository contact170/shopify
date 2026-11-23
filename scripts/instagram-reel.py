#!/usr/bin/env python3
"""Monte un reel Instagram vertical (1080 x 1920) à partir de visuels produits.

Usage :
    python3 scripts/instagram-reel.py plan.json sortie.mp4
    python3 scripts/instagram-reel.py plan.json apercu.jpg --apercu

plan.json :
    {"plans": [
      {"type": "accroche", "image": "<url ou chemin>", "titre": "Pas de prise\\nélectrique dehors ?", "sous_titre": "Cette caméra s'en passe.", "ancrage_x": 0.3},
      {"type": "carte",    "image": "<url ou chemin>", "titre": "100 % solaire", "sous_titre": "Panneau 3 W inclus"},
      {"type": "fin",      "image": "<url ou chemin>", "titre": "Caméra solaire\\nW512MW", "sous_titre": "Sans abonnement"}
    ]}

Deux règles tirées du premier reel publié (23/11/2026) :

1. Zone sûre. Instagram superpose son interface à la vidéo : nom du compte et
   ligne audio en haut, légende et boutons en bas et à droite. Tout texte
   reste donc entre SAFE_TOP et SAFE_BOTTOM, et rien d'important ne touche
   les 120 px de droite dans le bas de l'image.
2. Piste son. Instagram a refusé une vidéo dont la piste audio était un
   silence quasi vide (2 kbit/s). La sortie porte une piste AAC standard
   (48 kHz, 128 kbit/s) avec un souffle inaudible.

Dépendances : Pillow, ffmpeg, police Inter (ExtraBold et Medium).
"""
import io
import json
import subprocess
import sys
import urllib.request

from PIL import Image, ImageDraw, ImageFilter, ImageFont

W, H, FPS = 1080, 1920, 30
SAFE_TOP, SAFE_BOTTOM = 270, 1500
NAVY, JAUNE = (11, 31, 74), (255, 204, 0)
F_GRAS = "/usr/share/fonts/opentype/inter/Inter-ExtraBold.otf"
F_NORMAL = "/usr/share/fonts/opentype/inter/Inter-Medium.otf"
DUREE = {"accroche": 3.0, "carte": 2.6, "fin": 3.6}
FONDU = 0.35


def police(chemin, taille):
    return ImageFont.truetype(chemin, taille)


def charger(source):
    if source.startswith("https://cdn.shopify.com/"):
        with urllib.request.urlopen(source, timeout=30) as r:
            return Image.open(io.BytesIO(r.read())).convert("RGB")
    if source.startswith("http"):
        raise SystemExit(f"Image refusée (CDN Shopify uniquement) : {source}")
    return Image.open(source).convert("RGB")


def adoucir(t):
    t = max(0.0, min(1.0, t))
    return 1 - (1 - t) ** 3


def couvrir(im, w, h, zoom=1.0, ancrage_x=0.5):
    r = max(w / im.width, h / im.height) * zoom
    im2 = im.resize((int(im.width * r) + 1, int(im.height * r) + 1), Image.LANCZOS)
    x = int((im2.width - w) * ancrage_x)
    y = (im2.height - h) // 2
    return im2.crop((x, y, x + w, y + h))


def texte_centre(d, y, texte, f, couleur):
    for i, ligne in enumerate(texte.split("\n")):
        w = d.textlength(ligne, font=f)
        d.text(((W - w) / 2, y + i * int(f.size * 1.15)), ligne, font=f, fill=couleur)


def pastille(d, y, texte, f, alpha):
    w = d.textlength(texte, font=f)
    h = int(f.size * 1.9)
    d.rounded_rectangle(((W - w) / 2 - 44, y, (W + w) / 2 + 44, y + h), 30, fill=JAUNE + (alpha,))
    d.text(((W - w) / 2, y + int(f.size * 0.36)), texte, font=f, fill=NAVY + (alpha,))


def masque_arrondi(im, r):
    m = Image.new("L", im.size, 0)
    ImageDraw.Draw(m).rounded_rectangle((0, 0, im.width - 1, im.height - 1), r, fill=255)
    return m


class Plan:
    def __init__(self, spec):
        self.type = spec["type"]
        self.titre = spec.get("titre", "")
        self.sous_titre = spec.get("sous_titre", "")
        self.ancrage_x = spec.get("ancrage_x", 0.5)
        self.duree = spec.get("duree", DUREE[self.type])
        self.image = charger(spec["image"])
        self.fond = None
        if self.type == "carte":
            flou = couvrir(self.image, W, H, 1.15).filter(ImageFilter.GaussianBlur(40))
            self.fond = Image.blend(flou, Image.new("RGB", (W, H), NAVY), 0.72)

    def rendre(self, t, index, total):
        p = t / self.duree
        calque = Image.new("RGBA", (W, H), (0, 0, 0, 0))
        d = ImageDraw.Draw(calque)
        if self.type == "accroche":
            img = couvrir(self.image, W, H, 1.0 + 0.08 * p, self.ancrage_x).convert("RGBA")
            voile = Image.new("RGBA", (W, H), (0, 0, 0, 0))
            dv = ImageDraw.Draw(voile)
            for y in range(H):
                a = int(200 * max(0, 1 - abs(y - 480) / 600))
                dv.line((0, y, W, y), fill=NAVY + (min(215, a + 40),))
            img = Image.alpha_composite(img, voile)
            a1 = adoucir(t / 0.5)
            texte_centre(d, SAFE_TOP + 40 + int(40 * (1 - a1)), self.titre, police(F_GRAS, 104), (255, 255, 255, int(255 * a1)))
            a2 = adoucir((t - 0.9) / 0.5)
            if a2 > 0 and self.sous_titre:
                lignes = self.titre.count("\n") + 1
                pastille(d, SAFE_TOP + 40 + lignes * 120 + 60, self.sous_titre, police(F_GRAS, 64), int(255 * a2))
        elif self.type == "carte":
            img = self.fond.copy().convert("RGBA")
            a = adoucir(t / 0.45)
            cote = 960
            c2 = int(cote * (0.955 + 0.045 * p))
            carte = self.image.resize((c2, c2), Image.LANCZOS)
            x0 = (W - c2) // 2
            y0 = 530 + (cote - c2) // 2 + int(60 * (1 - a))
            ombre = Image.new("RGBA", (W, H), (0, 0, 0, 0))
            ImageDraw.Draw(ombre).rounded_rectangle((x0, y0 + 20, x0 + c2, y0 + c2 + 20), 48, fill=(0, 0, 0, 110))
            img = Image.alpha_composite(img, ombre.filter(ImageFilter.GaussianBlur(25)))
            img.paste(carte, (x0, y0), masque_arrondi(carte, 48))
            texte_centre(d, SAFE_TOP + 10, self.titre, police(F_GRAS, 92), (255, 255, 255, int(255 * a)))
            a2 = adoucir((t - 0.3) / 0.4)
            texte_centre(d, SAFE_TOP + 140, self.sous_titre, police(F_NORMAL, 44), (255, 255, 255, int(230 * a2)))
        else:  # fin
            img = Image.new("RGBA", (W, H), (255, 255, 255, 255))
            ImageDraw.Draw(img).rectangle((0, 1000, W, H), fill=NAVY)
            a = adoucir(t / 0.5)
            c2 = int(700 * (0.92 + 0.08 * a))
            produit = self.image.resize((c2, c2), Image.LANCZOS)
            img.paste(produit, ((W - c2) // 2, SAFE_TOP + (700 - c2) // 2))
            texte_centre(d, 1050, self.titre, police(F_GRAS, 88), (255, 255, 255, int(255 * a)))
            a2 = adoucir((t - 0.5) / 0.4)
            if a2 > 0 and self.sous_titre:
                pastille(d, 1280, self.sous_titre, police(F_GRAS, 58), int(255 * a2))
            a3 = adoucir((t - 0.9) / 0.4)
            texte_centre(d, 1425, "Lien en bio  ·  daewoo-security.fr", police(F_NORMAL, 42), (255, 255, 255, int(235 * a3)))
        if self.type == "carte":
            larg = (W - 200 - (total - 1) * 12) / total
            for i in range(total):
                x = 100 + i * (larg + 12)
                d.rounded_rectangle((x, SAFE_BOTTOM + 10, x + larg, SAFE_BOTTOM + 18), 4, fill=(255, 255, 255, 90))
                if i < index:
                    d.rounded_rectangle((x, SAFE_BOTTOM + 10, x + larg, SAFE_BOTTOM + 18), 4, fill=(255, 255, 255, 255))
                elif i == index and larg * p > 8:
                    d.rounded_rectangle((x, SAFE_BOTTOM + 10, x + larg * p, SAFE_BOTTOM + 18), 4, fill=(255, 255, 255, 255))
        return Image.alpha_composite(img, calque).convert("RGB")


def main():
    if len(sys.argv) < 3:
        raise SystemExit(__doc__)
    plans = [Plan(s) for s in json.load(open(sys.argv[1], encoding="utf-8"))["plans"]]
    n = len(plans)
    sortie = sys.argv[2]
    if "--apercu" in sys.argv:
        planche = Image.new("RGB", (270 * n, 480))
        for i, pl in enumerate(plans):
            vue = pl.rendre(pl.duree * 0.7, i, n)
            ImageDraw.Draw(vue).line((0, SAFE_TOP, W, SAFE_TOP), fill=(255, 0, 0), width=4)
            ImageDraw.Draw(vue).line((0, SAFE_BOTTOM, W, SAFE_BOTTOM), fill=(255, 0, 0), width=4)
            planche.paste(vue.resize((270, 480)), (i * 270, 0))
        planche.save(sortie, quality=85)
        return
    debuts = [0.0]
    for pl in plans[:-1]:
        debuts.append(debuts[-1] + pl.duree - FONDU)
    total = debuts[-1] + plans[-1].duree
    ff = subprocess.Popen(
        ["ffmpeg", "-y", "-loglevel", "error",
         "-f", "rawvideo", "-pix_fmt", "rgb24", "-s", f"{W}x{H}", "-r", str(FPS), "-i", "-",
         "-f", "lavfi", "-i", "anoisesrc=color=pink:amplitude=0.002:sample_rate=48000",
         "-map", "0:v", "-map", "1:a", "-shortest",
         "-c:v", "libx264", "-profile:v", "high", "-level", "4.0", "-pix_fmt", "yuv420p",
         "-g", "30", "-keyint_min", "30", "-sc_threshold", "0", "-bf", "2",
         "-b:v", "5M", "-maxrate", "6M", "-bufsize", "10M",
         "-color_primaries", "bt709", "-color_trc", "bt709", "-colorspace", "bt709",
         "-c:a", "aac", "-ar", "48000", "-ac", "2", "-b:a", "128k",
         "-movflags", "+faststart", sortie],
        stdin=subprocess.PIPE)
    for k in range(int(total * FPS)):
        t = k / FPS
        i = max(j for j in range(n) if debuts[j] <= t)
        vue = plans[i].rendre(t - debuts[i], i, n)
        if i > 0 and t - debuts[i] < FONDU:
            avant = plans[i - 1].rendre(t - debuts[i - 1], i - 1, n)
            vue = Image.blend(avant, vue, adoucir((t - debuts[i]) / FONDU))
        ff.stdin.write(vue.tobytes())
    ff.stdin.close()
    if ff.wait() != 0:
        raise SystemExit("ffmpeg a échoué")
    print(f"{sortie} : {total:.1f} s")


if __name__ == "__main__":
    main()
