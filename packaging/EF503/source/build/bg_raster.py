# Fonds "éclairés" rastérisés (opaques, tramés) pour éviter toute transparence à l'impression
import numpy as np
from PIL import Image
PXMM = 10  # 254 dpi
BLACK = (0x0B, 0x0B, 0x0D)
def hexc(h): h = h.lstrip('#'); return np.array([int(h[i:i+2], 16) for i in (0, 2, 4)], float)
SPOT = [(0, '#30333A', 1), (0.45, '#1B1C20', 0.85), (1, '#0B0B0D', 0)]
SOFT = [(0, '#24262B', 1), (1, '#0B0B0D', 0)]
FLOOR = [(0, '#FFFFFF', 0.10), (1, '#FFFFFF', 0)]
P = {'LID': (124.53, 274.38, 227.90, 148.93), 'P1': (124.53, 423.31, 227.90, 92.96),
     'P2': (352.43, 423.31, 148.94, 92.96), 'INNER': (501.37, 281.56, 227.89, 141.75)}
# rect (l, t, r, b bleed) et halos (cx, cy, rx, ry, stops, opacité) en coordonnées locales du panneau
JOBS = {
 'LID': ((3, 3, 3, 0), [(166, 84, 88, 78, SPOT, 1), (160, 141, 52, 5, FLOOR, 1), (40, 20, 70, 45, SOFT, 0.55)]),
 'P1': ((0, 0, 0, 0), [(156, 62, 80, 40, SOFT, 0.9)]),
 'P2': ((0, 0, 0, 0), [(118, 30, 60, 40, SOFT, 0.8)]),
 'INNER': ((3, 3, 3, 0), [(114, 80, 100, 60, SOFT, 0.8)]),
}
def grad(stops, d):
    offs = np.array([s[0] for s in stops]); cols = np.array([hexc(s[1]) for s in stops]); al = np.array([s[2] for s in stops])
    d = np.clip(d, 0, 1)
    c = np.stack([np.interp(d, offs, cols[:, k]) for k in range(3)], -1)
    a = np.interp(d, offs, al)
    return c, a
rng = np.random.default_rng(503)
for name, ((bl, bt, br, bb), halos) in JOBS.items():
    x0, y0, w, h = P[name]
    W, H = w + bl + br, h + bt + bb
    nx, ny = int(round(W * PXMM)), int(round(H * PXMM))
    xs = (np.arange(nx) + 0.5) / PXMM - bl
    ys = (np.arange(ny) + 0.5) / PXMM - bt
    X, Y = np.meshgrid(xs, ys)
    img = np.zeros((ny, nx, 3)) + np.array(BLACK, float)
    for cx, cy, rx, ry, stops, op in halos:
        d = np.sqrt(((X - cx) / rx) ** 2 + ((Y - cy) / ry) ** 2)
        c, a = grad(stops, d)
        a = (a * op)[..., None]
        img = c * a + img * (1 - a)
    img += rng.uniform(-0.9, 0.9, img.shape)
    out = Image.fromarray(np.clip(np.round(img), 0, 255).astype(np.uint8), 'RGB')
    out.save(f'../assets/bg_{name}.jpg', quality=95, subsampling=0)
    print(name, out.size, 'bleed', (bl, bt, br, bb))
