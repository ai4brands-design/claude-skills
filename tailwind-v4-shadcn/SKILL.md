---
name: tailwind-v4-shadcn
description: Production-tested stack for Tailwind v4 and shadcn/ui. Optimized for AI Code Generation.
---

# Tailwind v4 + shadcn/ui Production Stack

## Fast Setup

```bash
pnpm add tailwindcss @tailwindcss/vite
pnpm add -D @types/node tw-animate-css
pnpm dlx shadcn@latest init
```

## CSS Configuration (v4)

```css
@import "tailwindcss";
@import "tw-animate-css";

@theme inline {
  --color-background: var(--background);
  --color-foreground: var(--foreground);
  --color-primary: var(--primary);
}

@layer base {
  body {
    background-color: var(--background);
    color: var(--foreground);
  }
}
```

## Component Usage

```tsx
<div className="bg-background text-foreground">
  {/* Theme switches automatically */}
</div>
```

## Pro Tips

- Delete `tailwind.config.ts` - v4 uses CSS imports and vite plugins.
- Use `hsl()` wrappers in `:root` and `.dark` variables for shadcn compatibility.
- Prefer `@layer base` for global styles.
