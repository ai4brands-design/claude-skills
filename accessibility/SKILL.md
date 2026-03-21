---
name: accessibility
description: Implement web accessibility standards (WCAG 2.1 AA) using semantic HTML and ARIA patterns.
---

# Web Accessibility (WCAG 2.1 AA)

Ensure your web applications are inclusive and accessible to all users.

## Semantic HTML

```html
<!-- ❌ WRONG -->
<div onclick="submit()">Submit</div>

<!-- ✅ CORRECT -->
<button type="submit">Submit</button>
<a href="/next">Next page</a>
```

## Focus Management

```css
/* ✅ CORRECT - custom accessible outline */
button:focus-visible {
  outline: 2px solid var(--primary);
  outline-offset: 2px;
}
```

## ARIA Patterns

```html
<!-- ✅ CORRECT - ARIA fills semantic gap -->
<div role="dialog" aria-labelledby="title" aria-modal="true">
  <h2 id="title">Confirm action</h2>
</div>

<!-- ✅ BETTER - Use native HTML when available -->
<dialog aria-labelledby="title">
  <h2 id="title">Confirm action</h2>
</dialog>
```

## Pro Tips

- Always use `:focus-visible` to style focus states without annoying mouse users.
- Provide descriptive `alt` text for informative images; use `alt=""` for decorative ones.
- Test with screen readers (VoiceOver, NVDA) to verify the logical order of content.
