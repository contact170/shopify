import sys
view = sys.argv[1]  # front | back
k = 3.7  # px par mm
L, W, Hh = 227.9*k, 148.93*k, 92.96*k
if view == 'front':
    rot = 'rotateX(-27deg) rotateY(-29deg)'
    tx, ty = 0, 40
else:
    rot = 'rotateX(-27deg) rotateY(151deg)'
    tx, ty = 0, 40
def face(cls, img, w, h, tf, shade):
    return (f'<div class="f {cls}" style="width:{w}px;height:{h}px;margin-left:{-w/2}px;margin-top:{-h/2}px;transform:{tf};'
            f'background-image:url(faces/{img}.png)"><div class="sh" style="background:{shade}"></div></div>')
faces = [
  face('front', 'P1', L, Hh, f'translateZ({W/2}px)', 'linear-gradient(180deg,rgba(255,255,255,.05),rgba(0,0,0,.10))'),
  face('right', 'P2', W, Hh, f'rotateY(90deg) translateZ({L/2}px)', 'linear-gradient(90deg,rgba(0,0,0,.30),rgba(0,0,0,.42))'),
  face('back', 'P3', L, Hh, f'rotateY(180deg) translateZ({W/2}px)', 'linear-gradient(180deg,rgba(255,255,255,.04),rgba(0,0,0,.12))'),
  face('left', 'P4', W, Hh, f'rotateY(-90deg) translateZ({L/2}px)', 'linear-gradient(90deg,rgba(0,0,0,.38),rgba(0,0,0,.28))'),
  face('top', 'LID', L, W, f'rotateX(90deg) translateZ({Hh/2}px)', 'linear-gradient(160deg,rgba(255,255,255,.10),rgba(255,255,255,0) 55%)'),
]
html = f'''<!doctype html><html><head><meta charset="utf-8"><style>
html,body{{margin:0;height:100%}}
body{{width:1600px;height:1100px;overflow:hidden;background:radial-gradient(ellipse 70% 60% at 50% 42%,#f4f5f6 0%,#e2e4e7 55%,#cfd2d6 100%);font-family:sans-serif}}
.stage{{position:absolute;left:50%;top:50%;perspective:3600px;perspective-origin:50% 30%}}
.box{{position:absolute;transform-style:preserve-3d;transform:translate({tx}px,{ty}px) {rot}}}
.f{{position:absolute;left:0;top:0;background-size:100% 100%;backface-visibility:hidden;outline:1px solid rgba(255,255,255,.05);outline-offset:-1px}}
.sh{{position:absolute;inset:0}}
.shadow{{position:absolute;left:50%;top:50%;width:1300px;height:340px;margin-left:-650px;margin-top:170px;
  background:radial-gradient(ellipse 50% 50% at 50% 50%,rgba(0,0,0,.34),rgba(0,0,0,.14) 45%,rgba(0,0,0,0) 72%);filter:blur(8px)}}
</style></head><body>
<div class="shadow"></div>
<div class="stage"><div class="box">{"".join(faces)}</div></div>
</body></html>'''
open(f'mockup_{view}.html','w').write(html)
