---
description: UI/UX auditing and design guidelines based on Vercel's web-design-guidelines and modern standards.
---

# Web Design Guidelines & Audit

Use this skill to audit user interfaces, CSS, and HTML for quality, accessibility, and visual polish.

## Accessibility (a11y) - First Priority

* **Semantic HTML**: Use `<button>`, `<nav>`, `<main>`, `<article>`, not `<div>` soup.
* **Alt Text**: All `<img>` tags must have meaningful `alt` text. Decorative images should have `alt=""`.
* **Color Contrast**: Text must meet WCAG AA standards (4.5:1 ratio).
* **Keyboard Navigation**: All interactive elements (links, buttons, inputs) must be focusable and usable via keyboard (Tab/Enter/Space).
* **Focus States**: Never remove default focus outlines (`outline: none`) without replacing them with a custom visual indicator.
* **ARIA**: Use ARIA attributes only when semantic HTML is insufficient. "No ARIA is better than bad ARIA."

## Visual Design & Polish

* **Whitespace**: "When in doubt, add more whitespace." Give elements room to breathe. Use consistent spacing scales (e.g., Tailwind's `p-4`, `m-8`).
* **Typography**:
  * Limit to 2-3 font families max.
  * Use a consistent type scale.
  * Ensure line-height (leading) is comfortable (typically 1.5 for body text, tighter for headings).
* **Visual Hierarchy**:
  * The most important element should be the most prominent.
  * Use size, weight, color, and position to establish order.
* **Consistency**:
  * Buttons, inputs, and cards should reuse the same classes/components.
  * Don't invent new styles for solved problems.

## Responsive Design

* **Mobile First**: Design constraints for mobile first, then expand for desktop.
* **Touch Targets**: Buttons and links on mobile must be at least 44x44px.
* **No Horizontal Scroll**: Ensure no element forces the viewport to scroll horizontally on mobile (use `max-w-full`, `overflow-hidden` where appropriate).

## Audit Checklist

1. [ ] Run Lighthouse/Axe audit.
2. [ ] Tab through the entire page. Can you see where you are? Can you operate everything?
3. [ ] Zoom to 200%. Does the layout break?
4. [ ] Check standard resolutions: Mobile (375px), Tablet (768px), Desktop (1024px+).
