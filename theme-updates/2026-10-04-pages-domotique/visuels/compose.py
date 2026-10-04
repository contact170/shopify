from PIL import Image, ImageDraw, ImageFilter, ImageFont, ImageOps
src = Image.open('tmp-ivr501-a.jpg').convert('RGB')
# boite englobante de l'interrupteur : tout ce qui n'est pas blanc pur
mask = src.convert('L').point(lambda p: 255 if p < 246 else 0)
bbox = mask.getbbox()
sw = src.crop(bbox)
print('bbox', bbox, sw.size)

W = 1600
canvas = Image.new('RGB', (W, W), (255, 255, 255))

def poser(img, size, cx, cy, ombre=0.28):
    s = img.resize((size, int(size * img.height / img.width)), Image.LANCZOS)
    x, y = int(cx - s.width / 2), int(cy - s.height / 2)
    # ombre portee douce
    sh = Image.new('L', (s.width + 160, s.height + 160), 0)
    ImageDraw.Draw(sh).rectangle([80, 80, 80 + s.width, 80 + s.height], fill=int(255 * ombre))
    sh = sh.filter(ImageFilter.GaussianBlur(34))
    noir = Image.new('RGB', sh.size, (12, 30, 74))
    canvas.paste(noir, (x - 80 + 10, y - 80 + 28), sh)
    canvas.paste(s, (x, y))
    # filet pour detacher le verre blanc du fond blanc
    ImageDraw.Draw(canvas).rectangle([x, y, x + s.width - 1, y + s.height - 1], outline=(214, 218, 226), width=2)

poser(sw, 560, 450, 760, 0.22)
poser(sw, 560, 1150, 760, 0.22)
poser(sw, 680, 800, 860, 0.32)

d = ImageDraw.Draw(canvas)
bold = '/usr/share/fonts/truetype/liberation/LiberationSans-Bold.ttf'
reg = '/usr/share/fonts/truetype/liberation/LiberationSans-Regular.ttf'
navy = (12, 30, 74)
# titre
f1 = ImageFont.truetype(bold, 78); f2 = ImageFont.truetype(reg, 44)
t1 = 'Pack de 3 interrupteurs'; t2 = 'Volet roulant connecté IVR501W'
d.text((W / 2, 150), t1, font=f1, fill=navy, anchor='mm')
d.text((W / 2, 240), t2, font=f2, fill=(91, 100, 128), anchor='mm')
# pastille x3
r = 120; cx, cy = 1330, 1280
d.ellipse([cx - r, cy - r, cx + r, cy + r], fill=navy)
d.text((cx, cy + 4), '×3', font=ImageFont.truetype(bold, 118), fill=(255, 255, 255), anchor='mm')
# bandeau bas
f3 = ImageFont.truetype(bold, 42)
d.text((W / 2, 1470), 'Wi-Fi · Application Daewoo Home Connect · Sans abonnement', font=f3, fill=navy, anchor='mm')
canvas.save('ivr501w-pack-3-interrupteurs.jpg', quality=90, optimize=True, progressive=True)
canvas.resize((800, 800), Image.LANCZOS).save('apercu.jpg', quality=85)
