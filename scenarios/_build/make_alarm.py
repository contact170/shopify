#!/usr/bin/env python3
# "Si la caméra détecte un mouvement -> ALORS déclencher l'alarme (SOS)" — annotate + video.
import os, math, numpy as np
from PIL import Image, ImageDraw, ImageFont, ImageFilter
S="/tmp/claude-0/-home-user-shopify/95706305-7fda-52f3-b4c4-6cba2e324986/scratchpad"
SRC=f"{S}/cam3"; ANN=f"{S}/annot_alarm"; WEB=f"{S}/webalarm"
os.makedirs(ANN,exist_ok=True); os.makedirs(WEB,exist_ok=True)
OUT=f"{S}/scenario_camera_alarme.mp4"
W,H=720,1560
NAVY=(12,30,74);NAVY2=(7,16,46);BLUE=(11,97,205);BLUEL=(90,157,255)
WHITE=(255,255,255);GREEN=(22,163,74);AMBER=(245,158,11);RED=(225,29,72)
FB="/usr/share/fonts/truetype/liberation/LiberationSans-Bold.ttf"
FR="/usr/share/fonts/truetype/liberation/LiberationSans-Regular.ttf"
def font(s,b=True): return ImageFont.truetype(FB if b else FR,s)
_D0=ImageDraw.Draw(Image.new("RGB",(1,1)));MAXW=W-96
def fitfont(t,s,b,mw=MAXW):
    f=font(s,b)
    while _D0.textlength(t,font=f)>mw and s>12: s-=2;f=font(s,b)
    return f
STEPS=[
 dict(t=(0.925,0.082),a=125,cap="Sur l'accueil, appuyez sur  +"),
 dict(t=(0.330,0.193),a=25, cap="Choisissez « Créer une scène »"),
 dict(t=(0.900,0.315),a=140,cap="« Lorsque le statut de l'appareil change »"),
 dict(t=(0.500,0.832),a=-42,cap="Puis « Sélectionner un seul appareil »"),
 dict(t=(0.500,0.799),a=-150,cap="Choisissez la caméra IP506P (le déclencheur)"),
 dict(t=(0.885,0.715),a=150,cap="Choisissez « Mouvement détecté »"),
 dict(t=(0.860,0.081),a=140,cap="Validez « Mouvement détecté » → Confirmer"),
 dict(t=(0.890,0.460),a=150,cap="Partie ALORS : appuyez sur  +"),
 dict(t=(0.280,0.476),a=-25,cap="Sélectionnez « Appareil »"),
 dict(t=(0.420,0.327),a=15, cap="Choisissez l'alarme Vigilia"),
 dict(t=(0.150,0.396),a=-25,cap="Choisissez « SOS » puis Confirmer"),
 dict(t=(0.500,0.852),a=-90,cap="Enregistrez, puis nommez la scène"),
]
def load(p): return Image.open(p).convert("RGB").resize((W,H),Image.LANCZOS)
def draw_arrow(ov,tip,ang,length=230):
    r=math.radians(ang);sx,sy=tip[0]+length*math.cos(r),tip[1]+length*math.sin(r);d=ImageDraw.Draw(ov)
    for c,w in ((WHITE+(255,),20),(BLUE+(255,),11)): d.line([(sx,sy),tip],fill=c,width=w)
    hl=46;bx,by=tip[0]+hl*math.cos(r),tip[1]+hl*math.sin(r);pp=r+math.pi/2
    for c,g in ((WHITE+(255,),10),(BLUE+(255,),0)):
        d.polygon([tip,(bx+(hl*0.55+g)*math.cos(pp),by+(hl*0.55+g)*math.sin(pp)),
                   (bx-(hl*0.55+g)*math.cos(pp),by-(hl*0.55+g)*math.sin(pp))],fill=c)
def draw_target(ov,tip,ph,ring=None,color=BLUE):
    d=ImageDraw.Draw(ov);cx,cy=tip;base=ring if ring else 30
    pr=base+ph*(base*0.9);a=int(180*(1-ph));d.ellipse([cx-pr,cy-pr,cx+pr,cy+pr],outline=color+(a,),width=8)
    p2=(ph+0.5)%1;pr2=base+p2*(base*0.9);a2=int(150*(1-p2));d.ellipse([cx-pr2,cy-pr2,cx+pr2,cy+pr2],outline=BLUEL+(a2,),width=6)
    d.ellipse([cx-base,cy-base,cx+base,cy+base],outline=WHITE+(255,),width=7)
    d.ellipse([cx-base+7,cy-base+7,cx+base-7,cy+base-7],outline=color+(255,),width=6)
    if not ring: d.ellipse([cx-9,cy-9,cx+9,cy+9],fill=color+(255,))
def caption_bar(img,idx,cap,total):
    ov=Image.new("RGBA",img.size,(0,0,0,0));d=ImageDraw.Draw(ov);bh=196
    d.rectangle([0,H-bh,W,H],fill=NAVY+(238,));d.rectangle([0,H-bh,W,H-bh+5],fill=BLUE+(255,))
    d.rectangle([0,H-6,int(W*idx/total),H],fill=BLUEL+(255,))
    d.text((40,H-bh+30),f"ÉTAPE {idx} / {total}",font=font(30),fill=BLUEL+(255,))
    fc=font(40);ws=cap.split();lines=[];cur=""
    for w in ws:
        t=(cur+" "+w).strip()
        if d.textlength(t,font=fc)>W-80: lines.append(cur);cur=w
        else: cur=t
    lines.append(cur);lines=lines[:2];y=H-bh+74
    for ln in lines: d.text((40,y),ln,font=fc,fill=WHITE+(255,));y+=48
    return Image.alpha_composite(img.convert("RGBA"),ov)
def annotate(i,ph=0.35,cap=True):
    st=STEPS[i-1];img=load(f"{SRC}/{i:02d}.jpg").convert("RGBA");tip=(st["t"][0]*W,st["t"][1]*H)
    ov=Image.new("RGBA",img.size,(0,0,0,0))
    if st.get("a") is not None: draw_arrow(ov,tip,st["a"])
    draw_target(ov,tip,ph,ring=st.get("ring"))
    img=Image.alpha_composite(img,ov.filter(ImageFilter.GaussianBlur(6)));img=Image.alpha_composite(img,ov)
    if cap: img=caption_bar(img,i,st["cap"],len(STEPS))
    return img.convert("RGB")
def gcard(lines,top_pad=None):
    top=np.array(NAVY,float);bot=np.array(NAVY2,float);arr=np.zeros((H,W,3),np.uint8)
    for y in range(H): arr[y,:]=(top+(bot-top)*(y/H)).astype(np.uint8)
    img=Image.fromarray(arr,"RGB");d=ImageDraw.Draw(img)
    ft=[(t,fitfont(t,s,b),c,g) for (t,s,b,c,g) in lines];lh=lambda f:(f.getbbox("Ag")[3]-f.getbbox("Ag")[1])
    total=sum(lh(f)+g for t,f,c,g in ft);y=top_pad if top_pad is not None else (H-total)//2
    for t,f,c,g in ft:
        w=d.textlength(t,font=f);d.text(((W-w)//2,y),t,font=f,fill=c);y+=lh(f)+g
    return img
def title_card():
    return gcard([("SCÉNARIO",34,True,BLUEL,30),
        ("Déclencher l'alarme",48,True,WHITE,4),
        ("si la caméra détecte un mouvement",42,True,WHITE,44),
        ("Caméra IP506P  +  Alarme Vigilia",32,False,(200,214,246),44),
        ("SI mouvement  →  ALORS SOS",34,True,BLUEL,0)])
def end_card():
    img=gcard([("C'EST PRÊT",34,True,BLUEL,30),
        ("L'alarme se déclenche",48,True,WHITE,4),
        ("si la caméra voit un mouvement",44,True,WHITE,44),
        ("12 étapes · Daewoo Security",32,False,(200,214,246),0)],top_pad=H//2-40)
    d=ImageDraw.Draw(img);cx,cy,r=W//2,H//2-210,66
    d.ellipse([cx-r,cy-r,cx+r,cy+r],fill=GREEN);d.line([(cx-30,cy),(cx-6,cy+24),(cx+32,cy-26)],fill=WHITE,width=12,joint="curve")
    return img
def tip_card():
    return gcard([("ASTUCE",34,True,AMBER,30),
        ("À combiner avec",44,True,WHITE,4),
        ("« Détection ON si armée »",40,True,BLUEL,44),
        ("pour ne déclencher que",30,False,(200,214,246),4),
        ("lorsque l'alarme est armée",30,False,(200,214,246),0)])
# stills + web
for i in range(1,len(STEPS)+1):
    s=annotate(i,ph=0.30,cap=False);s.save(f"{ANN}/{i:02d}.png")
    s.convert("RGB").resize((384,int(384*H/W)),Image.LANCZOS).save(f"{WEB}/{i:02d}.jpg",quality=82)
title_card().convert("RGB").resize((384,int(384*H/W)),Image.LANCZOS).save(f"{WEB}/poster.jpg",quality=84)
print("alarm stills done")
import imageio.v2 as imageio
FPS=25;NHOLD=36;NCF=8
wr=imageio.get_writer(OUT,format="FFMPEG",mode="I",fps=FPS,codec="libx264",quality=8,
    macro_block_size=1,ffmpeg_params=["-pix_fmt","yuv420p","-movflags","+faststart"])
prev={"f":None}
def emit(frames):
    last=None
    for k,fr in enumerate(frames):
        arr=np.asarray(fr).astype(np.float32)
        if prev["f"] is not None and k<NCF: a=(k+1)/(NCF+1);arr=(1-a)*prev["f"]+a*arr
        wr.append_data(arr.astype(np.uint8));last=arr
    prev["f"]=last
emit([title_card()]*46)
for i in range(1,len(STEPS)+1): emit([annotate(i,ph=(k/NHOLD*2)%1.0,cap=True) for k in range(NHOLD)])
emit([end_card()]*54); emit([tip_card()]*70)
wr.close();print("alarm video done:",OUT)
