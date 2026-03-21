---
name: interaction-design
description: Create engaging, intuitive interactions through motion, feedback, and thoughtful state transitions that enhance usability and delight.
---

# Interaction Design

Create engaging, intuitive interactions through motion, feedback, and thoughtful state transitions.

## Motion Principles

```css
/* Common easings */
--ease-out: cubic-bezier(0.16, 1, 0.3, 1); /* Decelerate - entering */
--ease-in: cubic-bezier(0.55, 0, 1, 0.45); /* Accelerate - exiting */
--ease-in-out: cubic-bezier(0.65, 0, 0.35, 1); /* Both - moving between */
--spring: cubic-bezier(0.34, 1.56, 0.64, 1); /* Overshoot - playful */
```

## Interactive Components (React + Framer Motion)

```tsx
import { motion } from "framer-motion";

export function InteractiveButton({ children, onClick }) {
  return (
    <motion.button
      whileHover={{ scale: 1.02 }}
      whileTap={{ scale: 0.98 }}
      transition={{ type: "spring", stiffness: 400, damping: 17 }}
      className="px-4 py-2 bg-blue-600 text-white rounded-lg"
      onClick={onClick}
    >
      {children}
    </motion.button>
  );
}
```

## Feedback & State

- **Loading**: Use skeleton screens (`animate-pulse`) to manage perceived performance.
- **Progress**: Animate progress bars with `ease-out` for a "snappy" start.
- **Transitions**: Use `AnimatePresence` for smooth mounting/unmounting of elements.

## Pro Tips

- Prioritize Purposeful Motion: Ensure animations serve a function (feedback, orientation, focus).
- Iterate on Timings: Small changes in duration (e.g., 200ms vs 300ms) significantly impact feel.
- Integrate Accessibility: Respect `prefers-reduced-motion` settings.

## When to Use This Skill

- Adding microinteractions to buttons, forms, and other UI elements.
- Implementing smooth and contextual page or component transitions.
- Designing effective loading states and notification systems.
