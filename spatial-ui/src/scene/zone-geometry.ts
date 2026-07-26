import * as THREE from 'three';
import type { ZoneId } from '../data/zones';

export type WallKey = 'shell' | 'garage' | null;

export interface ZoneGeo {
  id: ZoneId;
  /** Marker/halo position, local to the house group. */
  anchor: THREE.Vector3;
  /** Where the camera dollies to when this zone is opened. */
  cameraTarget: THREE.Vector3;
  /** Point the camera looks at while dollied in. */
  lookAt: THREE.Vector3;
  /** Which shell material should fade to reveal this zone. */
  wall: WallKey;
  /** True for zones only visible through the glass roof at rest. */
  interior: boolean;
}

// Structural layout of the house — fixed, since the procedural geometry in
// house.ts is built around these exact anchors. Content (title, price,
// photo…) is editable per zone from the section schema; these coordinates
// are not.
export const ZONE_GEOMETRY: Record<ZoneId, ZoneGeo> = {
  entree: {
    id: 'entree',
    anchor: new THREE.Vector3(0, -0.05, 1.32),
    cameraTarget: new THREE.Vector3(0, 0.35, 3.3),
    lookAt: new THREE.Vector3(0, -0.05, 1.2),
    wall: 'shell',
    interior: false
  },
  fenetres: {
    id: 'fenetres',
    anchor: new THREE.Vector3(-1.05, 0.4, 1.32),
    cameraTarget: new THREE.Vector3(-1.5, 0.75, 3.1),
    lookAt: new THREE.Vector3(-1.05, 0.4, 1.2),
    wall: 'shell',
    interior: false
  },
  couloir: {
    id: 'couloir',
    anchor: new THREE.Vector3(0.1, 0.55, 0.0),
    cameraTarget: new THREE.Vector3(0.4, 1.7, 2.7),
    lookAt: new THREE.Vector3(0.1, 0.4, 0.0),
    wall: 'shell',
    interior: true
  },
  salon: {
    id: 'salon',
    anchor: new THREE.Vector3(-0.95, 0.5, 0.35),
    cameraTarget: new THREE.Vector3(-1.7, 1.5, 2.9),
    lookAt: new THREE.Vector3(-0.95, 0.4, 0.35),
    wall: 'shell',
    interior: true
  },
  garage: {
    id: 'garage',
    anchor: new THREE.Vector3(2.2, -0.05, 0.45),
    cameraTarget: new THREE.Vector3(3.7, 0.65, 2.5),
    lookAt: new THREE.Vector3(2.2, -0.05, 0.45),
    wall: 'garage',
    interior: false
  },
  jardin: {
    id: 'jardin',
    anchor: new THREE.Vector3(-2.15, -0.28, -1.4),
    cameraTarget: new THREE.Vector3(-3.7, 1.05, -0.4),
    lookAt: new THREE.Vector3(-2.15, -0.1, -1.4),
    wall: null,
    interior: false
  }
};

export const DEFAULT_CAMERA_POSITION = new THREE.Vector3(4.6, 3.0, 5.6);
export const DEFAULT_CAMERA_TARGET = new THREE.Vector3(0, 0.15, 0);
