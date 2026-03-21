---
name: threejs-materials
description: Master the creation and application of materials in Three.js for realistic rendering.
---

# Three.js Materials

Master PBR (Physically Based Rendering) and basic materials in Three.js.

## PBR Material (Standard)

```javascript
import * as THREE from "three";

const material = new THREE.MeshStandardMaterial({
  color: 0xffffff,
  roughness: 0.5,
  metalness: 0.0,
  map: colorTexture,
  normalMap: normalTexture,
  aoMap: aoTexture,
  displacementMap: dispTexture,
  emissive: 0x000000
});

// aoMap requires second UV channel
geometry.setAttribute("uv2", geometry.attributes.uv);
```

## Basic & Performance Materials

- `MeshBasicMaterial`: Not affected by lights. Best for performance or emissive layers.
- `MeshLambertMaterial`: Gouraud shading. Fast, good for matte surfaces.
- `MeshPhongMaterial`: Blinn-Phong shading. Good for shiny/plastic surfaces.

## Pro Tips

- Use `MeshStandardMaterial` as your default for realistic scenes.
- Enable `transparent: true` only when necessary, as transparency is computationally expensive.
- Use `side: THREE.DoubleSide` for planes or thin objects that need to be visible from both sides.

## When to Use This Skill

- Styling 3D objects with colors, textures, and physical properties.
- Optimizing render performance by choosing appropriate material types.
- Creating advanced visual effects like self-illumination (emissive) or transparency.
