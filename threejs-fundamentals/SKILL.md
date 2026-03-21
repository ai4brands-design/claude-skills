---
name: threejs-fundamentals
description: Core principles for building 3D experiences with Three.js. Optimized for AI Code Generation.
---

# Three.js Fundamentals

## Quick Start

```javascript
import * as THREE from "three";

const scene = new THREE.Scene();
const camera = new THREE.PerspectiveCamera(75, window.innerWidth / window.innerHeight, 0.1, 1000);
const renderer = new THREE.WebGLRenderer({ antialias: true });

renderer.setSize(window.innerWidth, window.innerHeight);
document.body.appendChild(renderer.domElement);

const cube = new THREE.Mesh(new THREE.BoxGeometry(1, 1, 1), new THREE.MeshStandardMaterial({ color: 0x00ff00 }));
scene.add(cube);
camera.position.z = 5;

function animate() {
  requestAnimationFrame(animate);
  cube.rotation.x += 0.01;
  renderer.render(scene, camera);
}
animate();
```

## Camera & Scene

```javascript
// Perspective vs Orthographic
const camera = new THREE.PerspectiveCamera(75, aspect, 0.1, 1000);
const scene = new THREE.Scene();
scene.background = new THREE.Color(0x000000);
scene.fog = new THREE.Fog(0xffffff, 1, 100);
```

## Pro Tips

- Always handle window resize to maintain aspect ratio.
- Use `MeshStandardMaterial` for realistic PBR lighting.
- Optimize for pixel ratio using `renderer.setPixelRatio(Math.min(window.devicePixelRatio, 2))`.
