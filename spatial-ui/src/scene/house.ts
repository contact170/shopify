import * as THREE from 'three';
import { ZONE_GEOMETRY } from './zone-geometry';
import type { ZoneId } from '../data/zones';
import { ZONE_ORDER } from '../data/zones';
import { createFacadeTexture, createGlowTexture, createShadowTexture } from './textures';

export interface ZoneMarker {
  id: ZoneId;
  core: THREE.Mesh;
  halo: THREE.Sprite;
  /** Larger, invisible raycast target — the visible core is too small to hit reliably. */
  hitArea: THREE.Mesh;
}

export interface HouseBuild {
  group: THREE.Group;
  /** Front face of the main shell — fades to reveal entrée/fenêtres/couloir/salon. */
  shellFrontMaterial: THREE.MeshPhysicalMaterial;
  /** Garage volume material — fades to reveal the garage zone. */
  garageMaterial: THREE.MeshPhysicalMaterial;
  markers: Record<ZoneId, ZoneMarker>;
}

const NAVY = '#0c1e4a';
const GLASS_BLUE = '#3d78ef';

export function buildHouse(): HouseBuild {
  const group = new THREE.Group();

  // --- ground contact shadow -------------------------------------------------
  const shadowTex = createShadowTexture();
  const ground = new THREE.Mesh(
    new THREE.CircleGeometry(4.6, 48),
    new THREE.MeshBasicMaterial({ map: shadowTex, transparent: true, depthWrite: false })
  );
  ground.rotation.x = -Math.PI / 2;
  ground.position.y = -0.92;
  group.add(ground);

  // --- foundation slab ---------------------------------------------------
  const slab = new THREE.Mesh(
    new THREE.BoxGeometry(3.6, 0.22, 3.0),
    new THREE.MeshStandardMaterial({ color: NAVY, roughness: 0.8, metalness: 0.05 })
  );
  slab.position.set(0.2, -0.47, 0.0);
  group.add(slab);

  // --- main shell (single box, per-face materials so the front can fade alone) ---
  const shellShared = new THREE.MeshPhysicalMaterial({
    color: NAVY,
    transparent: true,
    opacity: 0.5,
    roughness: 0.3,
    metalness: 0.1,
    side: THREE.DoubleSide,
    depthWrite: false
  });
  const shellFrontMaterial = new THREE.MeshPhysicalMaterial({
    color: NAVY,
    map: createFacadeTexture(),
    transparent: true,
    opacity: 0.5,
    roughness: 0.3,
    metalness: 0.1,
    side: THREE.DoubleSide,
    depthWrite: false
  });
  const shellBox = new THREE.BoxGeometry(3.2, 1.5, 2.7);
  // BoxGeometry face group order: [+x, -x, +y, -y, +z, -z]
  const shell = new THREE.Mesh(shellBox, [
    shellShared,
    shellShared,
    shellShared,
    shellShared,
    shellFrontMaterial,
    shellShared
  ]);
  shell.position.set(0, 0.4, 0);
  group.add(shell);

  // --- pitched glass roof --------------------------------------------------
  const roofMaterial = new THREE.MeshPhysicalMaterial({
    color: GLASS_BLUE,
    transparent: true,
    opacity: 0.16,
    roughness: 0.15,
    metalness: 0.2,
    side: THREE.DoubleSide,
    depthWrite: false
  });
  const roofPlaneGeo = new THREE.PlaneGeometry(3.5, 2.05);
  const roofLeft = new THREE.Mesh(roofPlaneGeo, roofMaterial);
  roofLeft.position.set(0, 1.55, 0.62);
  roofLeft.rotation.x = -Math.PI / 2 + 0.5;
  const roofRight = new THREE.Mesh(roofPlaneGeo, roofMaterial);
  roofRight.position.set(0, 1.55, -0.62);
  roofRight.rotation.x = Math.PI / 2 - 0.5;
  group.add(roofLeft, roofRight);

  // --- garage volume ---------------------------------------------------------
  const garageMaterial = new THREE.MeshPhysicalMaterial({
    color: NAVY,
    transparent: true,
    opacity: 0.5,
    roughness: 0.3,
    metalness: 0.1,
    side: THREE.DoubleSide,
    depthWrite: false
  });
  const garage = new THREE.Mesh(new THREE.BoxGeometry(1.1, 0.95, 1.5), garageMaterial);
  garage.position.set(2.2, 0.02, 0.35);
  group.add(garage);

  // --- garden ground patch (visual cue for the jardin zone) ------------------
  const gardenGlow = createGlowTexture('#3d78ef');
  const garden = new THREE.Mesh(
    new THREE.CircleGeometry(1.3, 32),
    new THREE.MeshBasicMaterial({ map: gardenGlow, transparent: true, depthWrite: false, opacity: 0.5 })
  );
  garden.rotation.x = -Math.PI / 2;
  garden.position.set(-2.15, -0.9, -1.4);
  group.add(garden);

  // --- zone markers (visible dot + halo sprite + a larger invisible raycast target) --
  const haloTexture = createGlowTexture('#6f9bff');
  const markerGeo = new THREE.SphereGeometry(0.055, 20, 20);
  const hitAreaGeo = new THREE.SphereGeometry(0.22, 12, 12);
  const markers = {} as Record<ZoneId, ZoneMarker>;

  ZONE_ORDER.forEach((id) => {
    const zone = ZONE_GEOMETRY[id];
    const material = new THREE.MeshStandardMaterial({
      color: GLASS_BLUE,
      emissive: new THREE.Color(GLASS_BLUE),
      emissiveIntensity: 0.9,
      roughness: 0.3
    });
    const core = new THREE.Mesh(markerGeo, material);
    core.position.copy(zone.anchor);
    core.userData.zoneId = id;
    core.renderOrder = 2;

    const halo = new THREE.Sprite(
      new THREE.SpriteMaterial({
        map: haloTexture,
        transparent: true,
        depthWrite: false,
        blending: THREE.AdditiveBlending,
        opacity: 0.7
      })
    );
    halo.scale.set(0.5, 0.5, 0.5);
    halo.position.copy(zone.anchor);
    halo.renderOrder = 1;

    const hitArea = new THREE.Mesh(
      hitAreaGeo,
      new THREE.MeshBasicMaterial({ transparent: true, opacity: 0, depthWrite: false })
    );
    hitArea.position.copy(zone.anchor);
    hitArea.userData.zoneId = id;

    group.add(core, halo, hitArea);
    markers[id] = { id, core, halo, hitArea };
  });

  return { group, shellFrontMaterial, garageMaterial, markers };
}
