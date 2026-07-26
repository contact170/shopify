import * as THREE from 'three';

/** One directional key light, one soft fill — matches the "single light source" design rule. */
export function buildLighting(): THREE.Group {
  const group = new THREE.Group();

  const key = new THREE.DirectionalLight('#eaf0ff', 1.4);
  key.position.set(4, 5, 3);
  group.add(key);

  const fill = new THREE.HemisphereLight('#3d78ef', '#04060d', 0.55);
  group.add(fill);

  const rim = new THREE.DirectionalLight('#6f9bff', 0.4);
  rim.position.set(-5, 2, -4);
  group.add(rim);

  return group;
}
