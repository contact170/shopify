import * as THREE from 'three';
import type { ZoneContent, ZoneId } from '../data/zones';
import { ZONE_ORDER } from '../data/zones';

export interface HotspotHandlers {
  onFocus: (zoneId: ZoneId) => void;
  onBlur: (zoneId: ZoneId) => void;
  onActivate: (zoneId: ZoneId) => void;
}

/**
 * Invisible, keyboard-focusable buttons layered over the canvas so every
 * zone is reachable without a pointer — the canvas itself has no DOM focus
 * semantics, so this is the only way tab/enter can drive the scene.
 */
export class HotspotLayer {
  private buttons = new Map<ZoneId, HTMLButtonElement>();

  constructor(container: HTMLElement, contents: Record<ZoneId, ZoneContent>, handlers: HotspotHandlers) {
    ZONE_ORDER.forEach((id) => {
      const btn = document.createElement('button');
      btn.type = 'button';
      btn.className =
        'spatial-hotspot absolute h-9 w-9 -translate-x-1/2 -translate-y-1/2 rounded-full ' +
        'focus-visible:outline focus-visible:outline-2 focus-visible:outline-blue-soft focus-visible:outline-offset-4';
      btn.style.left = '-999px';
      btn.style.top = '-999px';
      btn.setAttribute('aria-label', `${contents[id].eyebrow} — ${contents[id].title}`);
      btn.addEventListener('focus', () => handlers.onFocus(id));
      btn.addEventListener('blur', () => handlers.onBlur(id));
      btn.addEventListener('click', () => handlers.onActivate(id));
      container.appendChild(btn);
      this.buttons.set(id, btn);
    });
  }

  updatePosition(id: ZoneId, point: THREE.Vector3, camera: THREE.PerspectiveCamera, rect: DOMRect) {
    const btn = this.buttons.get(id);
    if (!btn) return;
    const projected = point.clone().project(camera);
    if (projected.z > 1) {
      btn.style.left = '-999px';
      return;
    }
    const x = (projected.x * 0.5 + 0.5) * rect.width;
    const y = (-projected.y * 0.5 + 0.5) * rect.height;
    btn.style.left = `${x}px`;
    btn.style.top = `${y}px`;
  }

  destroy() {
    this.buttons.forEach((btn) => btn.remove());
  }
}
