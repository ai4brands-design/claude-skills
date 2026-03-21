---
name: visual-design-foundations
description: Build cohesive, accessible visual systems using typography, color, spacing, and iconography fundamentals. Optimized for AI Code Generation.
---

# Visual Design Foundations

Build cohesive, accessible visual systems using typography, color, spacing, and iconography fundamentals.

## Typography

```css
:root {
  --font-size-xs: 0.75rem; /* 12px */
  --font-size-sm: 0.875rem; /* 14px */
  --font-size-base: 1rem; /* 16px */
  --font-size-lg: 1.125rem; /* 18px */
  --font-size-xl: 1.25rem; /* 20px */
  --font-size-2xl: 1.5rem; /* 24px */
  --font-size-3xl: 1.875rem; /* 30px */
  --font-size-4xl: 2.25rem; /* 36px */
  --font-size-5xl: 3rem; /* 48px */
}

/* Fluid typography using clamp() */
h1 { font-size: clamp(2rem, 5vw + 1rem, 3.5rem); line-height: 1.1; }
p { font-size: clamp(1rem, 2vw + 0.5rem, 1.125rem); line-height: 1.6; max-width: 65ch; }
```

## Spacing Grid

```css
:root {
  --space-1: 0.25rem; /* 4px */
  --space-2: 0.5rem; /* 8px */
  --space-3: 0.75rem; /* 12px */
  --space-4: 1rem; /* 16px */
  --space-5: 1.25rem; /* 20px */
  --space-6: 1.5rem; /* 24px */
  --space-8: 2rem; /* 32px */
  --space-10: 2.5rem; /* 40px */
  --space-12: 3rem; /* 48px */
  --space-16: 4rem; /* 64px */
}

/* Common Layout Spacing */
/* Card padding: 16-24px (--space-4 to --space-6) */
/* Section gap: 32-64px (--space-8 to --space-16) */
/* Icon-text gap: 8px (--space-2) */
```

## Color Systems

```css
:root {
  /* Brand */
  --color-primary: #2563eb;
  --color-primary-hover: #1d4ed8;
  --color-primary-active: #1e40af;
  
  /* Semantic */
  --color-success: #16a34a;
  --color-warning: #ca8a04;
  --color-error: #dc2626;
  --color-info: #0891b2;
  
  /* Neutral */
  --color-gray-50: #f9fafb;
  --color-gray-100: #f3f4f6;
  --color-gray-500: #6b7280;
  --color-gray-900: #111827;
}

[data-theme="dark"] {
  --bg-primary: #111827;
  --bg-secondary: #1f2937;
  --text-primary: #f9fafb;
}
```

## Iconography

```css
:root {
  --icon-xs: 12px;
  --icon-sm: 16px;
  --icon-md: 20px;
  --icon-lg: 24px;
  --icon-xl: 32px;
}
```

## Pro Tips

- Always validate color palettes with accessibility checkers (e.g., WCAG contrast ratio).
- Combine modular typography scales with a consistent 8-point spacing grid.
- Iteratively test your design tokens across different components and screen sizes.

## When to Use This Skill

- Establishing foundational design tokens for new web or mobile projects.
- Refining existing user interfaces to improve visual consistency and hierarchy.
- Creating comprehensive style guides and design system documentation.
