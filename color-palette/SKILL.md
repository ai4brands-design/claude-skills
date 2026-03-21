---
name: color-palette
description: Design, validate, and optimize color palettes for accessibility and standard themes.
---

# Color Palette Generation

Generate 11-shade scales and semantic tokens for web and mobile projects.

## Tailwind v4 @theme Syntax

```css
@theme {
  /* Shade scale */
  --color-primary-50: #F0FDFA;
  --color-primary-100: #CCFBF1;
  --color-primary-500: #14B8A6;
  --color-primary-950: #042F2E;

  /* Light mode semantics */
  --color-background: #FFFFFF;
  --color-foreground: var(--color-primary-950);
  --color-primary: var(--color-primary-600);
}

.dark {
  /* Dark mode overrides */
  --color-background: var(--color-primary-950);
  --color-foreground: var(--color-primary-50);
  --color-primary: var(--color-primary-500);
}
```

## Accessibility (Contrast)

Check contrast ratio using the WCAG formula:
`contrastRatio = (L1 + 0.05) / (L2 + 0.05)`

## Pro Tips

- Aim for a contrast ratio of at least 4.5:1 for normal text and 3:1 for large text.
- Use `hsl()` values in CSS variables if you need to generate shades programmatically.
- Ensure your primary color has enough variance across its scale to support all UI states (hover, active, disabled).
