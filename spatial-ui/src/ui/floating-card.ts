import * as THREE from 'three';
import gsap from 'gsap';
import type { ZoneContent, ZoneId } from '../data/zones';
import { DURATION, DAEWOO_EASE_GSAP } from '../motion';

export type CardMode = 'hover' | 'docked';

export class FloatingCard {
  private el: HTMLDivElement;
  private visible = false;
  private mode: CardMode = 'hover';

  constructor(
    container: HTMLElement,
    private onDiscover: (zoneId: ZoneId) => void,
    private onCloseRequest: () => void
  ) {
    this.el = document.createElement('div');
    this.el.className =
      'spatial-card pointer-events-none absolute left-0 top-0 w-[220px] ' +
      'rounded-2xl border border-white/10 bg-[#0a1228]/80 p-4 text-white shadow-[0_24px_50px_-18px_rgba(0,0,0,0.6)] ' +
      'backdrop-blur-card opacity-0';
    this.el.setAttribute('role', 'status');
    this.el.setAttribute('aria-live', 'polite');
    container.appendChild(this.el);
  }

  show(content: ZoneContent, mode: CardMode = 'hover') {
    this.mode = mode;
    this.el.innerHTML = `
      ${
        content.image
          ? `<img src="${encodeURI(content.image)}" alt="" loading="lazy" width="220" height="110"
                 class="mb-3 h-[110px] w-full rounded-xl object-cover bg-white/5"
                 onerror="this.remove()">`
          : ''
      }
      <p class="mono text-[9px] uppercase tracking-[0.08em] text-blue-soft mb-1">${escapeHtml(content.eyebrow)}</p>
      <h3 class="font-display text-[15px] font-semibold leading-snug mb-1">${escapeHtml(content.title)}</h3>
      <p class="text-[11.5px] leading-snug text-white/65 mb-2">${escapeHtml(content.description)}</p>
      <p class="text-[11px] text-white/45 mb-3">${escapeHtml(content.price)} · réf. ${escapeHtml(content.sku)}</p>
      <div class="flex items-center justify-between gap-3">
        <a href="${encodeURI(content.link)}"
           class="pointer-events-auto spatial-card-cta inline-flex items-center gap-1.5 text-[11px] font-medium text-blue-soft hover:text-white transition-colors">
          Découvrir <span aria-hidden="true">→</span>
        </a>
        ${
          mode === 'docked'
            ? '<button type="button" class="pointer-events-auto spatial-card-close text-[11px] text-white/45 hover:text-white transition-colors">← Retour</button>'
            : ''
        }
      </div>
    `;
    const cta = this.el.querySelector('.spatial-card-cta');
    if (mode === 'hover') {
      cta?.addEventListener(
        'click',
        (event) => {
          event.preventDefault();
          this.onDiscover(content.id);
        },
        { once: true }
      );
    }
    this.el.querySelector('.spatial-card-close')?.addEventListener('click', () => this.onCloseRequest());

    if (mode === 'docked') {
      // Fixed corner dock: let CSS position it, JS stops projecting a 3D point.
      this.el.style.transform = 'none';
      this.el.classList.add('bottom-6', 'left-6');
    } else {
      this.el.classList.remove('bottom-6', 'left-6');
    }

    if (!this.visible) {
      this.visible = true;
      // Opacity only — `transform` on this element is driven every frame by
      // setWorldPosition()/the fixed dock classes, so GSAP must not touch it.
      gsap.fromTo(this.el, { opacity: 0 }, { opacity: 1, duration: DURATION.card, ease: DAEWOO_EASE_GSAP });
    }
  }

  hide() {
    if (!this.visible) return;
    this.visible = false;
    gsap.to(this.el, { opacity: 0, duration: DURATION.card * 0.6, ease: DAEWOO_EASE_GSAP });
  }

  /** Re-project the card's screen position from a 3D world point (hover mode only). */
  setWorldPosition(point: THREE.Vector3, camera: THREE.PerspectiveCamera, rect: DOMRect) {
    if (this.mode === 'docked') return;
    const projected = point.clone().project(camera);
    const x = (projected.x * 0.5 + 0.5) * rect.width;
    const y = (-projected.y * 0.5 + 0.5) * rect.height;
    this.el.style.transform = `translate(calc(${x}px - 50%), calc(${y}px - 100% - 18px))`;
  }

  destroy() {
    this.el.remove();
  }
}

function escapeHtml(value: string): string {
  const div = document.createElement('div');
  div.textContent = value;
  return div.innerHTML;
}
