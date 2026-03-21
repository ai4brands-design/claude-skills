---
name: threejs-textures
description: Load and configure textures for 3D models in Three.js.
---

# Three.js Textures

Master texture loading, color spaces, and filtering for optimal 3D visuals.

## Texture Loading

```javascript
const loader = new THREE.TextureLoader();
const texture = loader.load("texture.jpg");

// Handle multiple textures
const [color, normal, rough] = await Promise.all([
  loadTexture("color.jpg"),
  loadTexture("normal.jpg"),
  loadTexture("rough.jpg")
]);
```

## Configuration

- **Color Space**: `colorTexture.colorSpace = THREE.SRGBColorSpace` (for albedo/color).
- **Wrapping**: `texture.wrapS = THREE.RepeatWrapping` (for tiling).
- **Filtering**: `texture.minFilter = THREE.LinearMipmapLinearFilter` (for smoothness).
- **Anisotropy**: `texture.anisotropy = renderer.capabilities.getMaxAnisotropy()` (sharper at angles).

## Pro Tips

- Always set `colorSpace` correctly to avoid washed-out or too-dark colors.
- Use Anisotropic filtering to keep textures sharp when viewed at shallow angles.
- Use non-power-of-two (NPOT) textures sparingly as they can impact performance on older GPUs.

## When to Use This Skill

- Applying surface detail and imagery to 3D meshes.
- Correcting color issues or blurriness in loaded textures.
- Implementing tiling patterns or rotating textures programmatically.
