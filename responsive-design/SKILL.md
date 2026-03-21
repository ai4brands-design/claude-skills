---
name: responsive-design
description: Master modern responsive design techniques to create interfaces that adapt seamlessly across all screen sizes.
---

# Responsive Design

Master viewport breakpoints, container queries, and fluid typography.

## Viewport Breakpoints (Tailwind)

- `sm`: 640px
- `md`: 768px
- `lg`: 1024px
- `xl`: 1280px

## Container Queries

```css
/* Define a containment context */
.card-container {
  container-type: inline-size;
  container-name: card;
}

/* Query the container */
@container card (min-width: 400px) {
  .card {
    display: grid;
    grid-template-columns: 200px 1fr;
    gap: 1rem;
  }
}
```

## Fluid Typography

```css
:root {
  --text-base: clamp(1rem, 0.9rem + 0.5vw, 1.125rem);
  --text-2xl: clamp(1.5rem, 1.25rem + 1.25vw, 2rem);
}
```

## Pro Tips

- Prioritize container queries over media queries for modular components.
- Use `clamp()` for spacing and typography to reduce the number of breakpoints needed.
- Always test for "intermediate" sizes where layouts might break between standard breakpoints.
