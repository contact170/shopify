#!/usr/bin/env python3
# Annotate Daewoo scenario screenshots (arrow + tap halo) and build a ~30s screencast video.
import os, math, numpy as np
from PIL import Image, ImageDraw, ImageFont, ImageFilter

S   = "/tmp/claude-0/-home-user-shopify/95706305-7fda-52f3-b4c4-6cba2e324986/scratchpad"
SRC = f"{S}/src"
ANN = f"{S}/annot"; os.makedirs(ANN, exist_ok=True)
OUT_MP4 = f"{S}/scenario_prise_on_si_armee.mp4"

W, H = 720, 1560
NAVY   = (12, 30, 74)
NAVY2  = (7, 16, 46)
BLUE   = (11, 97, 205)
BLUEL  = (90, 157, 255)
WHITE  = (255, 255, 255)
GREEN  = (22, 163, 74)
AMBER  = (245, 158, 11)

FB = "/usr/share/fonts/truetype/liberation/LiberationSans-Bold.ttf"
FR = "/usr/share/fonts/truetype/liberation/LiberationSans-Regular.ttf"
def font(sz, bold=True): return ImageFont.truetype(FB if bold else FR, sz)

# ---- steps: tip fraction (x,y), arrow angle deg (dir from tip to arrow start), caption ----
STEPS = [
 dict(t=(0.925,0.082), a=125, cap="Sur l'accueil, appuyez sur  +"),
 dict(t=(0.330,0.193), a=25,  cap="Choisissez « Créer une scène »"),
 dict(t=(0.900,0.315), a=140, cap="« Lorsque le statut de l'appareil change »"),
 dict(t=(0.500,0.832), a=-42, cap="Puis « Sélectionner un seul appareil »"),
 dict(t=(0.420,0.484), a=15,  cap="Choisissez votre alarme Vigilia"),
 dict(t=(0.900,0.162), a=135, cap="Ouvrez « Mode » → Armer → Confirmer"),
 dict(t=(0.890,0.444), a=150, cap="Partie ALORS : appuyez sur  +"),
 dict(t=(0.280,0.476), a=-25, cap="Sélectionnez « Appareil »"),
 dict(t=(0.500,0.832), a=-42, cap="Puis « Sélectionner un seul appareil »"),
 dict(t=(0.500,0.406), a=20,  cap="Choisissez la prise SP502F"),
 dict(t=(0.160,0.243), a=-25, cap="Réglez « ON » puis Confirmer"),
 dict(t=(0.868,0.082), a=125, cap="Périmètre de validité → Terminé"),
 dict(t=(0.697,0.432), a=150, cap="Nommez la scène → Confirmer"),
 dict(t=(0.500,0.274), a=None, ring=150, cap="Test : armez votre Vigilia"),
 dict(t=(0.867,0.576), a=None, ring=64,  cap="La prise s'allume automatiquement"),
]

def load(i):
    im = Image.open(f"{SRC}/{i:02d}.jpg").convert("RGB").resize((W, H), Image.LANCZOS)
    return im

def rounded(draw, box, r, fill):
    draw.rounded_rectangle(box, radius=r, fill=fill)

def draw_arrow(ov, tip, ang, length=230):
    """Arrow pointing at tip, coming from direction 'ang' (deg)."""
    rad = math.radians(ang)
    sx, sy = tip[0] + length*math.cos(rad), tip[1] + length*math.sin(rad)
    d = ImageDraw.Draw(ov)
    # white halo underlay then blue on top
    for col, wdt in ((WHITE+(255,), 20), (BLUE+(255,), 11)):
        d.line([(sx, sy), (tip[0], tip[1])], fill=col, width=wdt)
    # arrowhead
    hl = 46
    back = math.radians(ang)
    bx, by = tip[0] + hl*math.cos(back), tip[1] + hl*math.sin(back)
    perp = back + math.pi/2
    for col, gg in ((WHITE+(255,), 10), (BLUE+(255,), 0)):
        p1 = (tip[0], tip[1])
        p2 = (bx + (hl*0.55+gg)*math.cos(perp), by + (hl*0.55+gg)*math.sin(perp))
        p3 = (bx - (hl*0.55+gg)*math.cos(perp), by - (hl*0.55+gg)*math.sin(perp))
        d.polygon([p1, p2, p3], fill=col)

def draw_target(ov, tip, phase, ring=None, color=BLUE):
    """Static crosshair + pulsing halo at tip. phase in [0,1]."""
    d = ImageDraw.Draw(ov)
    cx, cy = tip
    base = ring if ring else 30
    # pulsing expanding ring
    pr = base + phase*(base*0.9)
    a = int(180*(1-phase))
    d.ellipse([cx-pr, cy-pr, cx+pr, cy+pr], outline=color+(a,), width=8)
    pr2 = base + ((phase+0.5) % 1)*(base*0.9)
    a2 = int(150*(1-((phase+0.5) % 1)))
    d.ellipse([cx-pr2, cy-pr2, cx+pr2, cy+pr2], outline=BLUEL+(a2,), width=6)
    # static ring
    d.ellipse([cx-base, cy-base, cx+base, cy+base], outline=WHITE+(255,), width=7)
    d.ellipse([cx-base+7, cy-base+7, cx+base-7, cy+base-7], outline=color+(255,), width=6)
    if not ring:
        d.ellipse([cx-9, cy-9, cx+9, cy+9], fill=color+(255,))

def caption_bar(img, idx, cap):
    ov = Image.new("RGBA", img.size, (0,0,0,0))
    d = ImageDraw.Draw(ov)
    bh = 196
    d.rectangle([0, H-bh, W, H], fill=NAVY+(238,))
    d.rectangle([0, H-bh, W, H-bh+5], fill=BLUE+(255,))
    # progress
    pw = int(W * idx/len(STEPS))
    d.rectangle([0, H-6, pw, H], fill=BLUEL+(255,))
    # step counter chip
    chip = f"ÉTAPE {idx} / {len(STEPS)}"
    fchip = font(30); fcap = font(40)
    d.text((40, H-bh+30), chip, font=fchip, fill=BLUEL+(255,))
    # wrap caption to <=2 lines
    words = cap.split(); lines=[]; cur=""
    for w in words:
        test=(cur+" "+w).strip()
        if d.textlength(test, font=fcap) > W-80: lines.append(cur); cur=w
        else: cur=test
    lines.append(cur); lines=lines[:2]
    y=H-bh+74
    for ln in lines:
        d.text((40, y), ln, font=fcap, fill=WHITE+(255,)); y+=48
    return Image.alpha_composite(img.convert("RGBA"), ov)

def annotate(i, phase=0.35, with_caption=True):
    st = STEPS[i-1]
    img = load(i).convert("RGBA")
    tip = (st["t"][0]*W, st["t"][1]*H)
    ov = Image.new("RGBA", img.size, (0,0,0,0))
    if st.get("a") is not None:
        draw_arrow(ov, tip, st["a"])
    ring = st.get("ring")
    draw_target(ov, tip, phase, ring=ring)
    # soft shadow of overlay
    shadow = ov.filter(ImageFilter.GaussianBlur(6))
    img = Image.alpha_composite(img, shadow)
    img = Image.alpha_composite(img, ov)
    if with_caption:
        img = caption_bar(img, i, st["cap"])
    return img.convert("RGB")

_D0 = ImageDraw.Draw(Image.new("RGB", (1, 1)))
MAXW = W - 96
def fitfont(text, size, bold, maxw=MAXW):
    f = font(size, bold)
    while _D0.textlength(text, font=f) > maxw and size > 12:
        size -= 2; f = font(size, bold)
    return f

def gradient_card(lines, top_pad=None):
    """lines = list of (text, size, bold, color, gap_after) — each line auto-fits width."""
    top = np.array(NAVY, float); bot = np.array(NAVY2, float)
    arr = np.zeros((H, W, 3), np.uint8)
    for y in range(H):
        arr[y, :] = (top + (bot-top)*(y/H)).astype(np.uint8)
    img = Image.fromarray(arr, "RGB")
    d = ImageDraw.Draw(img)
    fitted = [(t, fitfont(t, s, b), c, g) for (t, s, b, c, g) in lines]
    def lh(f): bb = f.getbbox("Ag"); return bb[3]-bb[1]
    total = sum(lh(f) + g for t, f, c, g in fitted)
    y = top_pad if top_pad is not None else (H - total)//2
    for t, f, c, g in fitted:
        w = d.textlength(t, font=f)
        d.text(((W-w)//2, y), t, font=f, fill=c)
        y += lh(f) + g
    return img

def title_card():
    return gradient_card([
        ("SCÉNARIO", 34, True, BLUEL, 30),
        ("Allumer une prise connectée", 50, True, WHITE, 4),
        ("quand l'alarme est armée", 50, True, WHITE, 44),
        ("Vigilia  +  Prise connectée SP502F", 32, False, (200,214,246), 44),
        ("SI armée   →   ALORS prise ON", 34, True, BLUEL, 0),
    ])

def end_card():
    img = gradient_card([
        ("C'EST PRÊT", 34, True, BLUEL, 30),
        ("La prise s'allume toute seule", 48, True, WHITE, 4),
        ("dès que vous armez Vigilia", 48, True, WHITE, 44),
        ("15 étapes · Daewoo Security", 32, False, (200,214,246), 0),
    ], top_pad=H//2-40)
    d = ImageDraw.Draw(img); cx, cy, r = W//2, H//2-210, 66
    d.ellipse([cx-r,cy-r,cx+r,cy+r], fill=GREEN)
    d.line([(cx-30,cy),(cx-6,cy+24),(cx+32,cy-26)], fill=WHITE, width=12, joint="curve")
    return img

def tip_card():
    img = gradient_card([
        ("ASTUCE", 34, True, AMBER, 30),
        ("Créez aussi le scénario inverse", 46, True, WHITE, 44),
        ("SI désarmée", 40, True, BLUEL, 4),
        ("→ ALORS prise OFF", 40, True, BLUEL, 44),
        ("pour éteindre la lampe en rentrant", 30, False, (200,214,246), 0),
    ])
    return img

# ---------- export annotated stills for the web page ----------
WEB = f"{S}/web"; os.makedirs(WEB, exist_ok=True)
for i in range(1, len(STEPS)+1):
    still = annotate(i, phase=0.30, with_caption=False)
    still.save(f"{ANN}/{i:02d}.png")
    annotate(i, phase=0.30, with_caption=True).save(f"{ANN}/{i:02d}_cap.jpg", quality=90)
    # light web JPG (no caption) for embedding in the page gallery
    still.convert("RGB").resize((384, int(384*H/W)), Image.LANCZOS).save(f"{WEB}/{i:02d}.jpg", quality=82)
title_card().convert("RGB").resize((384, int(384*H/W)), Image.LANCZOS).save(f"{WEB}/poster.jpg", quality=84)
print("stills done")

# ---------- build video ----------
import imageio.v2 as imageio
FPS=25; NHOLD=38; NCF=8; NTITLE=46; NEND=64
writer = imageio.get_writer(OUT_MP4, format="FFMPEG", mode="I", fps=FPS,
        codec="libx264", quality=8, macro_block_size=1,
        ffmpeg_params=["-pix_fmt","yuv420p","-movflags","+faststart"])
prev_last = {"f": None}
def emit(frame):
    writer.append_data(np.asarray(frame))
def emit_scene(frames):
    for k, fr in enumerate(frames):
        arr = np.asarray(fr).astype(np.float32)
        if prev_last["f"] is not None and k < NCF:
            a = (k+1)/(NCF+1)
            arr = (1-a)*prev_last["f"] + a*arr
        emit(arr.astype(np.uint8))
        last = arr
    prev_last["f"] = last.astype(np.float32)

# title
tc = title_card(); emit_scene([tc]*NTITLE)
# steps (pre-render base annotated w/o pulse, then add pulsing overlay per frame is heavy;
# we re-annotate per frame with varying phase — 38 frames x 15 is fine)
for i in range(1, len(STEPS)+1):
    frames = [annotate(i, phase=(k/NHOLD*2) % 1.0, with_caption=True) for k in range(NHOLD)]
    emit_scene(frames)
# end + tip (inverse scenario)
ec = end_card(); emit_scene([ec]*54)
tc2 = tip_card(); emit_scene([tc2]*72)
writer.close()
print("video done:", OUT_MP4)
