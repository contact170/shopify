# Page 3 du dossier fournisseur : rendus 3D de référence (même format que la planche)
import sys, os
d = sys.argv[1]
font = "@font-face{font-family:'Poppins';font-weight:600;src:url('" + os.path.abspath('../assets/poppins-latin-600-normal.woff2') + "') format('woff2');}" \
       "@font-face{font-family:'Poppins';font-weight:400;src:url('" + os.path.abspath('../assets/poppins-latin-400-normal.woff2') + "') format('woff2');}" + \
       open('../assets/notosc/notosc.css', encoding='utf-8').read().replace("url('../assets/", "url('" + os.path.abspath('../assets') + "/")
html = f'''<!doctype html><html><head><meta charset="utf-8"><style>{font}
@page {{ size: 802mm 397mm; margin: 0 }}
html,body {{ margin:0; background:#fff; font-family:Poppins,'Noto Sans SC',sans-serif; -webkit-print-color-adjust:exact; print-color-adjust:exact }}
.sheet {{ position:relative; width:802mm; height:397mm; overflow:hidden }}
h1 {{ position:absolute; left:20mm; top:14mm; margin:0; font-size:7mm; font-weight:600; color:#111 }}
.note {{ position:absolute; left:20mm; top:26mm; font-size:3.6mm; color:#444; line-height:1.55 }}
.img {{ position:absolute; top:46mm; width:374mm; height:300mm; object-fit:cover; object-position:center; border-radius:3mm }}
.cap {{ position:absolute; top:352mm; font-size:4mm; font-weight:600; color:#111 }}
</style></head><body><div class="sheet">
<h1>DAEWOO EF503 — 3D REFERENCE · 效果图</h1>
<div class="note">For reference only: shows how each panel is oriented once the box is folded. · 仅供参考：展示折盒后各面方向。<br>
Lid artwork reads from the FRONT panel. Inner flap is printed upside down so it reads correctly when the box is opened. · 盖面文字朝正面方向；内折页倒印，开盒时正向阅读。</div>
<img class="img" style="left:20mm" src="mockup_front.png">
<img class="img" style="left:408mm" src="mockup_back.png">
<div class="cap" style="left:20mm">FRONT VIEW · 正面效果</div>
<div class="cap" style="left:408mm">BACK VIEW · 背面效果</div>
</div></body></html>'''
open(os.path.join(d, 'ref.html'), 'w', encoding='utf-8').write(html)
