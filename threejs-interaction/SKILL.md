---
name: threejs-interaction
description: Implement raycasting, mouse picking, and interactive controls in Three.js.
---

# Three.js Interaction

Enable user interaction with 3D scenes using raycasting and controls.

## Orbit Controls

```javascript
import { OrbitControls } from "three/addons/controls/OrbitControls.js";

const controls = new OrbitControls(camera, renderer.domElement);
controls.enableDamping = true;
```

## Raycasting (Mouse Picking)

```javascript
const raycaster = new THREE.Raycaster();
const mouse = new THREE.Vector2();

function onClick(event) {
  mouse.x = (event.clientX / window.innerWidth) * 2 - 1;
  mouse.y = -(event.clientY / window.innerHeight) * 2 + 1;

  raycaster.setFromCamera(mouse, camera);
  const intersects = raycaster.intersectObjects(scene.children);
  if (intersects.length > 0) {
    console.log("Clicked:", intersects[0].object);
  }
}
window.addEventListener("click", onClick);
```

## Pro Tips

- Use `enableDamping` in `OrbitControls` for a smoother, high-end feel.
- When raycasting, pass a restricted list of `clickableObjects` instead of `scene.children` for better performance.
- Handle touch events similarly to mouse events using `event.touches[0]`.

## When to Use This Skill

- Adding camera navigation (zoom, pans, rotate) to a 3D scene.
- Implementing click/hover events to select or highlight 3D objects.
- Building interactive product configurators or data visualizations.
