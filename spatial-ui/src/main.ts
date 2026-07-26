import * as THREE from 'three';
import './style.css';
import { DEFAULT_ZONES, ZONE_ORDER, type ZoneContent, type ZoneId } from './data/zones';
import { buildHouse } from './scene/house';
import { buildLighting } from './scene/lighting';
import { HouseInteractions } from './scene/interactions';
import { FloatingCard } from './ui/floating-card';
import { HotspotLayer } from './ui/hotspots';
import { prefersReducedMotion } from './motion';

function supportsWebGL(): boolean {
  try {
    const canvas = document.createElement('canvas');
    return !!(canvas.getContext('webgl2') || canvas.getContext('webgl'));
  } catch {
    return false;
  }
}

function readZoneContent(root: HTMLElement): Record<ZoneId, ZoneContent> {
  const dataEl = root.querySelector<HTMLElement>('#spatial-hero-data');
  const content: Record<ZoneId, ZoneContent> = { ...DEFAULT_ZONES };
  if (!dataEl?.textContent) return content;
  try {
    const parsed = JSON.parse(dataEl.textContent) as Partial<Record<ZoneId, Partial<ZoneContent>>>;
    ZONE_ORDER.forEach((id) => {
      if (parsed[id]) content[id] = { ...content[id], ...parsed[id], id };
    });
  } catch (error) {
    console.warn('[spatial-hero] Contenu de zone illisible, utilisation des valeurs par défaut.', error);
  }
  return content;
}

function initScene(root: HTMLElement) {
  const canvasRoot = root.querySelector<HTMLElement>('#spatial-hero-canvas-root');
  const cardLayer = root.querySelector<HTMLElement>('#spatial-hero-card-layer');
  const hotspotLayer = root.querySelector<HTMLElement>('#spatial-hero-hotspots');
  const fallback = root.querySelector<HTMLElement>('#spatial-hero-fallback');
  if (!canvasRoot || !cardLayer || !hotspotLayer) return;
  // Re-bind to a non-nullable local: closures defined further down (resize,
  // the render loop) can't otherwise inherit the null-check above.
  const canvasEl: HTMLElement = canvasRoot;

  const contents = readZoneContent(root);

  const scene = new THREE.Scene();
  const camera = new THREE.PerspectiveCamera(35, 1, 0.1, 100);
  const renderer = new THREE.WebGLRenderer({ antialias: true, alpha: true });
  renderer.setPixelRatio(Math.min(window.devicePixelRatio, 2));
  renderer.outputColorSpace = THREE.SRGBColorSpace;
  // The canvas-root wrapper is pointer-events:none (so it never blocks the
  // heading/scroll-cue siblings it overlaps); re-enable it on the canvas
  // itself, which is what actually needs to receive pointer/click events.
  renderer.domElement.style.pointerEvents = 'auto';
  canvasRoot.appendChild(renderer.domElement);

  const house = buildHouse();
  scene.add(house.group);
  scene.add(buildLighting());

  const card = new FloatingCard(cardLayer, (zoneId) => interactions.open(zoneId), () => interactions.close());
  const hotspots = new HotspotLayer(hotspotLayer, contents, {
    onFocus: (zoneId) => interactions.hover(zoneId),
    onBlur: (zoneId) => {
      if (interactions.activeZone !== zoneId) interactions.hover(null);
    },
    onActivate: (zoneId) => (interactions.activeZone === zoneId ? interactions.close() : interactions.open(zoneId))
  });

  const interactions = new HouseInteractions(camera, house.group, house, {
    onHoverChange: (zoneId) => {
      if (zoneId) card.show(contents[zoneId], 'hover');
      else card.hide();
    },
    onOpenStart: () => {
      card.hide();
      root.setAttribute('data-active-zone', 'true');
    },
    onOpenComplete: (zoneId) => card.show(contents[zoneId], 'docked'),
    onClose: () => {
      card.hide();
      root.removeAttribute('data-active-zone');
    }
  });

  // --- pointer interaction ---------------------------------------------------
  const raycaster = new THREE.Raycaster();
  const pointer = new THREE.Vector2();
  const markerMeshes = ZONE_ORDER.map((id) => house.markers[id].hitArea);

  function pickZone(event: PointerEvent): ZoneId | null {
    const rect = renderer.domElement.getBoundingClientRect();
    pointer.x = ((event.clientX - rect.left) / rect.width) * 2 - 1;
    pointer.y = -((event.clientY - rect.top) / rect.height) * 2 + 1;
    raycaster.setFromCamera(pointer, camera);
    const hits = raycaster.intersectObjects(markerMeshes, false);
    return hits.length ? ((hits[0].object.userData.zoneId as ZoneId) ?? null) : null;
  }

  renderer.domElement.addEventListener('pointermove', (event) => {
    if (interactions.activeZone) return;
    const zoneId = pickZone(event);
    renderer.domElement.style.cursor = zoneId ? 'pointer' : 'default';
    interactions.hover(zoneId);
  });

  renderer.domElement.addEventListener('pointerleave', () => {
    if (!interactions.activeZone) interactions.hover(null);
  });

  renderer.domElement.addEventListener('click', (event) => {
    const zoneId = pickZone(event);
    if (zoneId) interactions.open(zoneId);
    else if (interactions.activeZone) interactions.close();
  });

  root.addEventListener('keydown', (event) => {
    if (event.key === 'Escape' && interactions.activeZone) interactions.close();
  });

  // --- resize -------------------------------------------------------------
  function resize() {
    const rect = canvasEl.getBoundingClientRect();
    camera.aspect = rect.width / Math.max(rect.height, 1);
    camera.updateProjectionMatrix();
    renderer.setSize(rect.width, rect.height);
  }
  resize();
  new ResizeObserver(resize).observe(canvasEl);

  // --- render loop ----------------------------------------------------------
  const worldPos = new THREE.Vector3();
  function frame() {
    const rect = canvasEl.getBoundingClientRect();

    ZONE_ORDER.forEach((id) => {
      house.markers[id].core.getWorldPosition(worldPos);
      hotspots.updatePosition(id, worldPos, camera, rect);
    });

    // The docked card (active zone) stays put visually; only the hover card
    // needs to keep tracking the marker, since idle drift keeps it moving.
    const trackedZone = interactions.hoveredZone;
    if (trackedZone && !interactions.activeZone) {
      house.markers[trackedZone].core.getWorldPosition(worldPos);
      card.setWorldPosition(worldPos, camera, rect);
    }

    renderer.render(scene, camera);
    requestAnimationFrame(frame);
  }

  requestAnimationFrame(frame);

  if (fallback) fallback.setAttribute('hidden', 'true');
}

function boot() {
  const root = document.getElementById('spatial-hero');
  if (!root) return;

  if (prefersReducedMotion() || !supportsWebGL()) {
    // Static, real product content stays visible and fully navigable — no
    // 3D, no motion, nothing to lazy-load.
    return;
  }

  let started = false;
  const observer = new IntersectionObserver(
    (entries) => {
      if (started) return;
      if (entries.some((entry) => entry.isIntersecting)) {
        started = true;
        observer.disconnect();
        initScene(root);
      }
    },
    { rootMargin: '200px' }
  );
  observer.observe(root);
}

if (document.readyState === 'loading') {
  document.addEventListener('DOMContentLoaded', boot);
} else {
  boot();
}
