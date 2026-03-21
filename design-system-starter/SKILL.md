---
name: design-system-starter
description: Build robust, scalable design systems that ensure visual consistency and exceptional user experiences.
---

# Design System Starter

Build robust, scalable design systems that ensure visual consistency and exceptional user experiences.

## Design Tokens

```json
{
  "color": {
    "primitive": {
      "blue": {
        "50": "#eff6ff",
        "100": "#dbeafe",
        "200": "#bfdbfe",
        "300": "#93c5fd",
        "400": "#60a5fa",
        "500": "#3b82f6",
        "600": "#2563eb",
        "700": "#1d4ed8",
        "800": "#1e40af",
        "900": "#1e3a8a",
        "950": "#172554"
      }
    },
    "semantic": {
      "brand": {
        "primary": "{color.primitive.blue.600}",
        "primary-hover": "{color.primitive.blue.700}",
        "primary-active": "{color.primitive.blue.800}"
      },
      "background": {
        "primary": "{color.primitive.white}",
        "secondary": "{color.primitive.gray.50}"
      }
    }
  }
}
```

## Typography

```json
{
  "typography": {
    "fontFamily": {
      "sans": "'Inter', -apple-system, BlinkMacSystemFont, 'Segoe UI', sans-serif",
      "mono": "'Fira Code', 'Courier New', monospace"
    },
    "fontSize": {
      "xs": "0.75rem",
      "sm": "0.875rem",
      "base": "1rem",
      "lg": "1.125rem",
      "xl": "1.25rem",
      "2xl": "1.5rem"
    }
  }
}
```

## Pro Tips

- Use semantic naming (e.g., `color-brand-primary`) instead of primitives (e.g., `color-blue-600`) in components.
- Automate token generation for multiple platforms (web, mobile).
- Establish a clear contribution model for new components.
