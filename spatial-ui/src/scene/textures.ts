import * as THREE from 'three';

/** Soft radial-gradient alpha disc, used for the ground shadow and the hover halo. */
export function createGlowTexture(hex = '#6f9bff'): THREE.CanvasTexture {
  const size = 256;
  const canvas = document.createElement('canvas');
  canvas.width = size;
  canvas.height = size;
  const ctx = canvas.getContext('2d')!;
  const gradient = ctx.createRadialGradient(size / 2, size / 2, 0, size / 2, size / 2, size / 2);
  gradient.addColorStop(0, `${hex}aa`);
  gradient.addColorStop(0.4, `${hex}55`);
  gradient.addColorStop(1, `${hex}00`);
  ctx.fillStyle = gradient;
  ctx.fillRect(0, 0, size, size);
  const texture = new THREE.CanvasTexture(canvas);
  texture.needsUpdate = true;
  return texture;
}

/** Ground contact-shadow disc, darker and tighter than the glow halo. */
export function createShadowTexture(): THREE.CanvasTexture {
  const size = 256;
  const canvas = document.createElement('canvas');
  canvas.width = size;
  canvas.height = size;
  const ctx = canvas.getContext('2d')!;
  const gradient = ctx.createRadialGradient(size / 2, size / 2, 0, size / 2, size / 2, size / 2);
  gradient.addColorStop(0, 'rgba(2,4,12,0.55)');
  gradient.addColorStop(0.55, 'rgba(2,4,12,0.22)');
  gradient.addColorStop(1, 'rgba(2,4,12,0)');
  ctx.fillStyle = gradient;
  ctx.fillRect(0, 0, size, size);
  const texture = new THREE.CanvasTexture(canvas);
  texture.needsUpdate = true;
  return texture;
}

/** Draws a simple door + two windows onto the house's front facade. */
export function createFacadeTexture(): THREE.CanvasTexture {
  const w = 640;
  const h = 300;
  const canvas = document.createElement('canvas');
  canvas.width = w;
  canvas.height = h;
  const ctx = canvas.getContext('2d')!;
  ctx.clearRect(0, 0, w, h);

  // door
  ctx.fillStyle = 'rgba(255,255,255,0.16)';
  const doorW = 70;
  const doorH = 150;
  ctx.fillRect(w / 2 - doorW / 2, h - doorH, doorW, doorH);

  // windows either side
  const winW = 90;
  const winH = 70;
  const winY = 70;
  ctx.fillStyle = 'rgba(111,155,255,0.22)';
  ctx.fillRect(w / 2 - 210 - winW / 2, winY, winW, winH);
  ctx.fillRect(w / 2 + 210 - winW / 2, winY, winW, winH);

  // faint mullions for the windows
  ctx.strokeStyle = 'rgba(255,255,255,0.35)';
  ctx.lineWidth = 2;
  [w / 2 - 210, w / 2 + 210].forEach((cx) => {
    ctx.beginPath();
    ctx.moveTo(cx - winW / 2, winY + winH / 2);
    ctx.lineTo(cx + winW / 2, winY + winH / 2);
    ctx.moveTo(cx, winY);
    ctx.lineTo(cx, winY + winH);
    ctx.stroke();
  });

  const texture = new THREE.CanvasTexture(canvas);
  texture.colorSpace = THREE.SRGBColorSpace;
  texture.needsUpdate = true;
  return texture;
}
