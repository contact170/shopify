import * as THREE from 'three';
import gsap from 'gsap';
import type { ZoneId } from '../data/zones';
import { ZONE_GEOMETRY, DEFAULT_CAMERA_POSITION, DEFAULT_CAMERA_TARGET } from './zone-geometry';
import type { HouseBuild } from './house';
import { DURATION, DAEWOO_EASE_GSAP, prefersReducedMotion } from '../motion';

const SIREN_ZONE: ZoneId = 'jardin';
const SIGNAL_COLOR = '#ff7a45';

export interface InteractionCallbacks {
  onHoverChange: (zoneId: ZoneId | null) => void;
  onOpenStart: (zoneId: ZoneId) => void;
  onOpenComplete: (zoneId: ZoneId) => void;
  onClose: () => void;
}

export class HouseInteractions {
  private camera: THREE.PerspectiveCamera;
  private houseGroup: THREE.Group;
  private house: HouseBuild;
  private callbacks: InteractionCallbacks;
  private lookAt = DEFAULT_CAMERA_TARGET.clone();
  private hovered: ZoneId | null = null;
  private active: ZoneId | null = null;
  private idleTl: gsap.core.Timeline | null = null;
  private reducedMotion = prefersReducedMotion();

  constructor(
    camera: THREE.PerspectiveCamera,
    houseGroup: THREE.Group,
    house: HouseBuild,
    callbacks: InteractionCallbacks
  ) {
    this.camera = camera;
    this.houseGroup = houseGroup;
    this.house = house;
    this.callbacks = callbacks;
    this.camera.position.copy(DEFAULT_CAMERA_POSITION);
    this.camera.lookAt(this.lookAt);
    this.startIdle();
  }

  private startIdle() {
    if (this.reducedMotion || this.active) return;
    this.idleTl?.kill();
    this.idleTl = gsap.timeline({ repeat: -1, yoyo: true }).to(this.houseGroup.rotation, {
      y: 0.055,
      duration: 6,
      ease: 'sine.inOut'
    });
  }

  private stopIdle() {
    this.idleTl?.kill();
    this.idleTl = null;
  }

  get activeZone() {
    return this.active;
  }

  get hoveredZone() {
    return this.hovered;
  }

  hover(zoneId: ZoneId | null) {
    if (this.active || zoneId === this.hovered) return;
    const prev = this.hovered;
    this.hovered = zoneId;

    if (prev) this.setMarkerHovered(prev, false);
    if (zoneId) this.setMarkerHovered(zoneId, true);

    this.callbacks.onHoverChange(zoneId);
  }

  private setMarkerHovered(zoneId: ZoneId, hovered: boolean) {
    const marker = this.house.markers[zoneId];
    gsap.to(marker.halo.scale, {
      x: hovered ? 0.85 : 0.5,
      y: hovered ? 0.85 : 0.5,
      duration: DURATION.hover,
      ease: DAEWOO_EASE_GSAP
    });
    gsap.to(marker.core.position, {
      y: ZONE_GEOMETRY[zoneId].anchor.y + (hovered ? 0.06 : 0),
      duration: DURATION.hover,
      ease: DAEWOO_EASE_GSAP
    });
  }

  open(zoneId: ZoneId) {
    if (this.active === zoneId) return;
    if (this.active) this.resetWall(this.active);
    this.active = zoneId;
    this.hovered = null;
    this.stopIdle();
    this.callbacks.onOpenStart(zoneId);

    const geo = ZONE_GEOMETRY[zoneId];
    const dur = this.reducedMotion ? 0.01 : DURATION.dolly;
    const tl = gsap.timeline({
      onComplete: () => {
        this.playFunctionalDemo(zoneId);
        this.callbacks.onOpenComplete(zoneId);
      }
    });

    tl.to(
      this.camera.position,
      { x: geo.cameraTarget.x, y: geo.cameraTarget.y, z: geo.cameraTarget.z, duration: dur, ease: DAEWOO_EASE_GSAP },
      0
    );
    tl.to(
      this.lookAt,
      {
        x: geo.lookAt.x,
        y: geo.lookAt.y,
        z: geo.lookAt.z,
        duration: dur,
        ease: DAEWOO_EASE_GSAP,
        onUpdate: () => this.camera.lookAt(this.lookAt)
      },
      0
    );

    const wallMaterial = this.wallMaterialFor(zoneId);
    if (wallMaterial) {
      tl.to(wallMaterial, { opacity: 0.06, duration: this.reducedMotion ? 0.01 : DURATION.wallFade, ease: DAEWOO_EASE_GSAP }, 0.1);
    }
  }

  private wallMaterialFor(zoneId: ZoneId): THREE.MeshPhysicalMaterial | null {
    const wall = ZONE_GEOMETRY[zoneId].wall;
    if (wall === 'shell') return this.house.shellFrontMaterial;
    if (wall === 'garage') return this.house.garageMaterial;
    return null;
  }

  /** Instantly restores a zone's wall opacity — used when jumping straight to another zone. */
  private resetWall(zoneId: ZoneId) {
    const material = this.wallMaterialFor(zoneId);
    if (material) gsap.to(material, { opacity: 0.5, duration: 0.3, ease: DAEWOO_EASE_GSAP });
  }

  close() {
    if (!this.active) return;
    const closingZone = this.active;
    this.active = null;
    const wallMaterial = this.wallMaterialFor(closingZone);
    const dur = this.reducedMotion ? 0.01 : DURATION.ret;

    const tl = gsap.timeline({
      onComplete: () => {
        this.callbacks.onClose();
        this.startIdle();
      }
    });
    tl.to(
      this.camera.position,
      { x: DEFAULT_CAMERA_POSITION.x, y: DEFAULT_CAMERA_POSITION.y, z: DEFAULT_CAMERA_POSITION.z, duration: dur, ease: DAEWOO_EASE_GSAP },
      0
    );
    tl.to(
      this.lookAt,
      {
        x: DEFAULT_CAMERA_TARGET.x,
        y: DEFAULT_CAMERA_TARGET.y,
        z: DEFAULT_CAMERA_TARGET.z,
        duration: dur,
        ease: DAEWOO_EASE_GSAP,
        onUpdate: () => this.camera.lookAt(this.lookAt)
      },
      0
    );
    if (wallMaterial) {
      tl.to(wallMaterial, { opacity: 0.5, duration: dur, ease: DAEWOO_EASE_GSAP }, 0);
    }
  }

  /** The "why this product is here" beat: a short local action, then a signal travelling to the siren. */
  private playFunctionalDemo(zoneId: ZoneId) {
    const marker = this.house.markers[zoneId];

    if (zoneId === SIREN_ZONE) {
      this.flashSiren();
      return;
    }

    const local = gsap.timeline();
    switch (zoneId) {
      case 'entree':
      case 'garage':
        local.to(marker.core.position, { y: '+=0.05', duration: 0.35, yoyo: true, repeat: 1, ease: 'sine.inOut' });
        break;
      case 'fenetres':
        local.to(marker.core.rotation, { z: 0.3, duration: 0.18, yoyo: true, repeat: 3, ease: 'sine.inOut' });
        break;
      case 'couloir':
      case 'salon':
        local.to(marker.halo.scale, { x: 1.1, y: 1.1, duration: 0.4, yoyo: true, repeat: 1, ease: 'sine.inOut' });
        break;
    }

    local.call(() => this.sendSignal(zoneId));
  }

  private sendSignal(from: ZoneId) {
    if (this.reducedMotion) {
      this.flashSiren();
      return;
    }
    const start = ZONE_GEOMETRY[from].anchor;
    const end = ZONE_GEOMETRY[SIREN_ZONE].anchor;
    const geometry = new THREE.SphereGeometry(0.045, 12, 12);
    const material = new THREE.MeshBasicMaterial({ color: SIGNAL_COLOR, transparent: true });
    const pulse = new THREE.Mesh(geometry, material);
    pulse.position.copy(start);
    this.houseGroup.add(pulse);

    gsap.to(pulse.position, {
      x: end.x,
      y: end.y + 0.4,
      z: end.z,
      duration: DURATION.signal,
      ease: 'power1.inOut',
      onComplete: () => {
        this.houseGroup.remove(pulse);
        geometry.dispose();
        material.dispose();
        this.flashSiren();
      }
    });
  }

  private flashSiren() {
    const siren = this.house.markers[SIREN_ZONE];
    const mat = siren.core.material as THREE.MeshStandardMaterial;
    gsap
      .timeline()
      .to(mat, { emissiveIntensity: 2.6, duration: 0.12, ease: 'power2.out' })
      .to(mat, { emissiveIntensity: 0.9, duration: 0.5, ease: 'power2.in' })
      .to(siren.halo.scale, { x: 1.3, y: 1.3, duration: 0.5, ease: 'power2.out' }, 0)
      .to(siren.halo.scale, { x: 0.5, y: 0.5, duration: 0.6, ease: 'power2.in' }, 0.5);
  }
}
