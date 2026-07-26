// Single shared easing curve and timing scale for the whole experience —
// per the design direction, one signature ease reused everywhere (hover,
// card entrance, camera dolly, wall fade) rather than a different curve
// per animation.
export const DAEWOO_EASE = 'cubic-bezier(0.16, 1, 0.3, 1)';
export const DAEWOO_EASE_GSAP = 'power3.out';

export const DURATION = {
  hover: 0.5,
  card: 0.6,
  dolly: 1.1,
  wallFade: 0.9,
  signal: 1.4,
  ret: 0.9
} as const;

export const prefersReducedMotion = (): boolean =>
  window.matchMedia('(prefers-reduced-motion: reduce)').matches;
