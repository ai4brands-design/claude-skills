---
name: threejs-loaders
description: Efficiently load 3D models (GLTF/GLB), textures, and assets into Three.js.
---

# Three.js Loaders

Manage the loading of models, textures, and external assets.

## Basic Loaders

```javascript
import { GLTFLoader } from "three/addons/loaders/GLTFLoader.js";

// Load GLTF model
const loader = new GLTFLoader();
loader.load("model.glb", (gltf) => {
  scene.add(gltf.scene);
});

// Load texture
const textureLoader = new THREE.TextureLoader();
const texture = textureLoader.load("texture.jpg");
```

## Loading Manager

```javascript
const manager = new THREE.LoadingManager();
manager.onProgress = (url, loaded, total) => {
  const progress = (loaded / total) * 100;
  console.log(`Loading: ${progress.toFixed(1)}%`);
};

const textureLoader = new THREE.TextureLoader(manager);
const gltfLoader = new GLTFLoader(manager);
```

## Pro Tips

- Always use `GLTFLoader` with `.glb` files for the most efficient asset delivery.
- Use `LoadingManager` to synchronize multiple assets and display a unified loading screen.
- Set `texture.colorSpace = THREE.SRGBColorSpace` for color/diffuse maps to ensure color accuracy.

## When to Use This Skill

- Importing custom 3D models into your web application.
- Managing complex asset loading pipelines for games or configurators.
- Implementing progress bars and loading screens for heavy 3D scenes.
