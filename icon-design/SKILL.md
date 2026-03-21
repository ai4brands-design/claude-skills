---
name: icon-design
description: Select the right icon for the job. Maps concepts to icons, provides templates, prevents common mistakes.
---

# Icon Design

Select the right icon for the job and implement it efficiently.

## Library Comparison

- **Lucide**: Clean, modern, highly customizable (Recommended).
- **Heroicons**: Optimized for Tailwind CSS.
- **Phosphor**: Extensive set with multiple weights.

## Semantic Mapping

- **Recognition**: `Trophy`, `Star`, `Award`
- **Finance**: `Tag`, `DollarSign`, `CreditCard`
- **Location**: `MapPin`, `Globe`, `Map`
- **Communication**: `MessageCircle`, `Phone`, `Mail`
- **Safety**: `Shield`, `Lock`, `ShieldCheck`

## Implementation (React)

```tsx
import { Home, Users, Settings, type LucideIcon } from 'lucide-react'

const ICON_MAP: Record<string, LucideIcon> = { Home, Users, Settings }

export function Icon({ name, className }: { name: string, className?: string }) {
  const LucideIcon = ICON_MAP[name]
  return LucideIcon ? <LucideIcon className={className} /> : null
}
```

## Pro Tips

- Use `stroke="currentColor"` to ensure icons inherit text color.
- Standardize sizes: `w-4 h-4` (small), `w-5 h-5` (default), `w-6 h-6` (large).
- Avoid bundling all icons; use explicit maps or tree-shaking friendly imports.
