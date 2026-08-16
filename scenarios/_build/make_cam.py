#!/usr/bin/env python3
# Annotate IP506P camera-detection scenario + build screencast video.
import os, math, numpy as np
from PIL import Image, ImageDraw, ImageFont, ImageFilter

S   = "/tmp/claude-0/-home-user-shopify/95706305-7fda-52f3-b4c4-6cba2e324986/scratchpad"
SRC = f"{S}/cam"
ANN = f"{S}/annot_cam"; os.makedirs(ANN, exist_ok=True)
WEB = f"{S}/webcam";   os.makedirs(WEB, exist_ok=True)
OUT_MP4 = f"{S}/scenario_camera_ip506p.mp4"

W, H = 720, 1560
NAVY=(12,30,74); NAVY2=(7,16,46); BLUE=(11,97,205); BLUEL=(90,157,255)
WHITE=(255,255,255); GREEN=(22,163,74); AMBER=(245,158,11)
FB="/usr/share/fonts/truetype/liberation/LiberationSans-Bold.ttf"
FR="/usr/share/fonts/truetype/liberation/LiberationSans-Regular.ttf"
def font(sz,bold=True): return ImageFont.truetype(FB if bold else FR, sz)
_D0=ImageDraw.Draw(Image.new("RGB",(1,1))); MAXW=W-96
def fitfont(t,size,bold,maxw=MAXW):
    f=font(size,bold)
    while _D0.textlength(t,font=f)>maxw and size>12: size-=2; f=font(size,bold)
    return f

STEPS=[
 dict(t=(0.925,0.082), a=125, cap="Sur l'accueil, appuyez sur  +"),
 dict(t=(0.330,0.193), a=25,  cap="Choisissez « Créer une scène »"),
 dict(t=(0.900,0.315), a=140, cap="« Lorsque le statut de l'appareil change »"),
 dict(t=(0.500,0.832), a=-42, cap="Puis « Sélectionner un seul appareil »"),
 dict(t=(0.420,0.484), a=15,  cap="Choisissez votre alarme Vigilia"),
 dict(t=(0.900,0.162), a=135, cap="Ouvrez « Mode » → Armer → Confirmer"),
 dict(t=(0.890,0.444), a=150, cap="Partie ALORS : appuyez sur  +"),
 dict(t=(0.280,0.476), a=-25, cap="Sélectionnez « Appareil »"),
 dict(t=(0.500,0.832), a=-42, cap="Puis « Sélectionner un seul appareil »"),
 dict(t=(0.500,0.799), a=-150,cap="Choisissez la caméra IP506P Full HD"),
 dict(t=(0.885,0.345), a=150, cap="Choisissez « Détection de mouvement »"),
 dict(t=(0.160,0.423), a=-25, cap="Activez la détection : « On » puis Confirmer"),
 dict(t=(0.500,0.852), a=-90, cap="Vérifiez le récapitulatif, puis Enregistrer"),
 dict(t=(0.697,0.432), a=150, cap="Nommez la scène → Confirmer"),
 dict(t=(0.500,0.274), a=None, ring=150, cap="Test : armez votre Vigilia"),
 dict(t=(0.854,0.194), a=None, ring=60,  cap="La détection de mouvement est bien active"),
]

def load(path):
    return Image.open(path).convert("RGB").resize((W,H), Image.LANCZOS)

def draw_arrow(ov, tip, ang, length=230):
    rad=math.radians(ang); sx,sy=tip[0]+length*math.cos(rad),tip[1]+length*math.sin(rad)
    d=ImageDraw.Draw(ov)
    for col,wdt in ((WHITE+(255,),20),(BLUE+(255,),11)): d.line([(sx,sy),tip],fill=col,width=wdt)
    hl=46; back=math.radians(ang); bx,by=tip[0]+hl*math.cos(back),tip[1]+hl*math.sin(back); perp=back+math.pi/2
    for col,gg in ((WHITE+(255,),10),(BLUE+(255,),0)):
        d.polygon([tip,(bx+(hl*0.55+gg)*math.cos(perp),by+(hl*0.55+gg)*math.sin(perp)),
                   (bx-(hl*0.55+gg)*math.cos(perp),by-(hl*0.55+gg)*math.sin(perp))],fill=col)

def draw_target(ov,tip,phase,ring=None,color=BLUE):
    d=ImageDraw.Draw(ov); cx,cy=tip; base=ring if ring else 30
    pr=base+phase*(base*0.9); a=int(180*(1-phase)); d.ellipse([cx-pr,cy-pr,cx+pr,cy+pr],outline=color+(a,),width=8)
    p2=(phase+0.5)%1; pr2=base+p2*(base*0.9); a2=int(150*(1-p2)); d.ellipse([cx-pr2,cy-pr2,cx+pr2,cy+pr2],outline=BLUEL+(a2,),width=6)
    d.ellipse([cx-base,cy-base,cx+base,cy+base],outline=WHITE+(255,),width=7)
    d.ellipse([cx-base+7,cy-base+7,cx+base-7,cy+base-7],outline=color+(255,),width=6)
    if not ring: d.ellipse([cx-9,cy-9,cx+9,cy+9],fill=color+(255,))

def caption_bar(img,idx,cap,total):
    ov=Image.new("RGBA",img.size,(0,0,0,0)); d=ImageDraw.Draw(ov); bh=196
    d.rectangle([0,H-bh,W,H],fill=NAVY+(238,)); d.rectangle([0,H-bh,W,H-bh+5],fill=BLUE+(255,))
    d.rectangle([0,H-6,int(W*idx/total),H],fill=BLUEL+(255,))
    d.text((40,H-bh+30),f"ÉTAPE {idx} / {total}",font=font(30),fill=BLUEL+(255,))
    fcap=font(40); words=cap.split(); lines=[]; cur=""
    for w in words:
        test=(cur+" "+w).strip()
        if d.textlength(test,font=fcap)>W-80: lines.append(cur); cur=w
        else: cur=test
    lines.append(cur); lines=lines[:2]; y=H-bh+74
    for ln in lines: d.text((40,y),ln,font=fcap,fill=WHITE+(255,)); y+=48
    return Image.alpha_composite(img.convert("RGBA"),ov)

def annotate_img(img, st, phase=0.35, idx=None, total=None, with_caption=True):
    img=img.convert("RGBA"); tip=(st["t"][0]*W, st["t"][1]*H)
    ov=Image.new("RGBA",img.size,(0,0,0,0))
    if st.get("a") is not None: draw_arrow(ov,tip,st["a"])
    draw_target(ov,tip,phase,ring=st.get("ring"))
    img=Image.alpha_composite(img, ov.filter(ImageFilter.GaussianBlur(6)))
    img=Image.alpha_composite(img, ov)
    if with_caption and idx is not None: img=caption_bar(img,idx,st["cap"],total)
    return img.convert("RGB")

def annotate(i, phase=0.35, with_caption=True):
    return annotate_img(load(f"{SRC}/{i:02d}.jpg"), STEPS[i-1], phase, i, len(STEPS), with_caption)

def gradient_card(lines, top_pad=None):
    top=np.array(NAVY,float); bot=np.array(NAVY2,float); arr=np.zeros((H,W,3),np.uint8)
    for y in range(H): arr[y,:]=(top+(bot-top)*(y/H)).astype(np.uint8)
    img=Image.fromarray(arr,"RGB"); d=ImageDraw.Draw(img)
    fitted=[(t,fitfont(t,s,b),c,g) for (t,s,b,c,g) in lines]
    lh=lambda f:(f.getbbox("Ag")[3]-f.getbbox("Ag")[1])
    total=sum(lh(f)+g for t,f,c,g in fitted); y=top_pad if top_pad is not None else (H-total)//2
    for t,f,c,g in fitted:
        w=d.textlength(t,font=f); d.text(((W-w)//2,y),t,font=f,fill=c); y+=lh(f)+g
    return img

def title_card():
    return gradient_card([
        ("SCÉNARIO",34,True,BLUEL,30),
        ("Détection de la caméra IP506P",46,True,WHITE,4),
        ("quand l'alarme est armée",48,True,WHITE,44),
        ("Vigilia  +  Caméra IP506P Full HD",32,False,(200,214,246),44),
        ("SI armée   →   ALORS détection ON",34,True,BLUEL,0),
    ])

def end_card():
    img=gradient_card([
        ("C'EST PRÊT",34,True,BLUEL,30),
        ("La caméra surveille",48,True,WHITE,4),
        ("dès que vous armez Vigilia",48,True,WHITE,44),
        ("16 étapes · Daewoo Security",32,False,(200,214,246),0),
    ], top_pad=H//2-40)
    d=ImageDraw.Draw(img); cx,cy,r=W//2,H//2-210,66
    d.ellipse([cx-r,cy-r,cx+r,cy+r],fill=GREEN); d.line([(cx-30,cy),(cx-6,cy+24),(cx+32,cy-26)],fill=WHITE,width=12,joint="curve")
    return img

def tip_inverse_card():
    return gradient_card([
        ("ASTUCE",34,True,AMBER,30),
        ("Créez aussi le scénario inverse",46,True,WHITE,44),
        ("SI désarmée",40,True,BLUEL,4),
        ("→ ALORS détection OFF",40,True,BLUEL,44),
        ("pour couper la détection chez vous",30,False,(200,214,246),0),
    ])

def tip_privacy_card():
    return gradient_card([
        ("MODE VIE PRIVÉE",34,True,AMBER,26),
        ("SI désarmée → Vie privée ON",40,True,WHITE,4),
        ("(la caméra se referme)",30,False,(200,214,246),38),
        ("Ne coupe PAS la détection !",38,True,BLUEL,4),
        ("Pensez à créer les 2 sens à chaque fois",30,False,(200,214,246),0),
    ])

# ---- stills + web assets ----
for i in range(1,len(STEPS)+1):
    still=annotate(i,phase=0.30,with_caption=False)
    still.save(f"{ANN}/{i:02d}.png")
    still.convert("RGB").resize((384,int(384*H/W)),Image.LANCZOS).save(f"{WEB}/{i:02d}.jpg",quality=82)
# Mode Vie Privée annotated still (for the page note)
vp=annotate_img(load(f"{SRC}/vieprivee.jpg"),
                dict(t=(0.130,0.238),a=-25,cap="Mode Vie privée → On"),
                phase=0.30, with_caption=False)
vp.save(f"{ANN}/vieprivee.png")
vp.convert("RGB").resize((384,int(384*H/W)),Image.LANCZOS).save(f"{WEB}/vieprivee.jpg",quality=82)
title_card().convert("RGB").resize((384,int(384*H/W)),Image.LANCZOS).save(f"{WEB}/poster.jpg",quality=84)
print("cam stills done")

# ---- video ----
import imageio.v2 as imageio
FPS=25; NHOLD=34; NCF=8
writer=imageio.get_writer(OUT_MP4,format="FFMPEG",mode="I",fps=FPS,codec="libx264",quality=8,
        macro_block_size=1,ffmpeg_params=["-pix_fmt","yuv420p","-movflags","+faststart"])
prev={"f":None}
def emit_scene(frames):
    last=None
    for k,fr in enumerate(frames):
        arr=np.asarray(fr).astype(np.float32)
        if prev["f"] is not None and k<NCF:
            a=(k+1)/(NCF+1); arr=(1-a)*prev["f"]+a*arr
        writer.append_data(arr.astype(np.uint8)); last=arr
    prev["f"]=last
emit_scene([title_card()]*46)
for i in range(1,len(STEPS)+1):
    emit_scene([annotate(i,phase=(k/NHOLD*2)%1.0,with_caption=True) for k in range(NHOLD)])
emit_scene([end_card()]*52)
emit_scene([tip_inverse_card()]*66)
emit_scene([tip_privacy_card()]*74)
writer.close()
print("cam video done:",OUT_MP4)
