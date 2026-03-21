---
name: favicon-gen
description: Generate professional favicons from logos or initials. Optimized for cross-platform compatibility.
---

# Favicon Generator

Generate production-ready favicons for web applications.

## Generation Methods

### Method 1: Logo Extraction

1. Extract the icon element from your logo SVG.
2. Center in a 32x32 viewBox and simplify for small sizes.

### Method 2: Monogram Favicon

```svg
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 32 32">
  <circle cx="16" cy="16" r="16" fill="#0066cc"/>
  <text x="16" y="21" font-size="16" font-weight="bold" text-anchor="middle" fill="#ffffff" font-family="sans-serif">AC</text>
</svg>
```

## Implementation

```html
<link rel="icon" href="/favicon.ico" sizes="any">
<link rel="icon" href="/favicon.svg" type="image/svg+xml">
<link rel="apple-touch-icon" href="/apple-touch-icon.png">
<link rel="manifest" href="/site.webmanifest">
```

## Pro Tips

- Use SVG for favicons whenever possible for perfect scaling.
- Include a 180x180 PNG for `apple-touch-icon`.
- Simplify the design as much as possible; fine details vanish at 16x16px.
