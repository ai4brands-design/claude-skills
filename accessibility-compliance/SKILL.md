---
name: accessibility-compliance
description: Master accessibility implementation to create inclusive experiences that work for everyone, including users with disabilities.
---

# Accessibility Compliance

Master the implementation of accessible UI components following WCAG 2.2 standards.

## Accessible Components (React)

```tsx
interface ButtonProps extends React.ButtonHTMLAttributes<HTMLButtonElement> {
  variant?: "primary" | "secondary";
  isLoading?: boolean;
}

function AccessibleButton({ children, variant = "primary", isLoading = false, disabled, ...props}: ButtonProps) {
  return (
    <button
      disabled={disabled || isLoading}
      aria-busy={isLoading}
      aria-disabled={disabled || isLoading}
      className={cn(
        "focus-visible:outline-none focus-visible:ring-2 focus-visible:ring-offset-2",
        "min-h-[44px] min-w-[44px]",
        variant === "primary" && "bg-primary text-primary-foreground",
        (disabled || isLoading) && "opacity-50 cursor-not-allowed",
      )}
      {...props}
    >
      {isLoading ? (
        <>
          <span className="sr-only">Loading</span>
          <Spinner aria-hidden="true" />
        </>
      ) : (
        children
      )}
    </button>
  );
}
```

## Dialogs & Modals

- Use `FocusTrap` to keep navigation within active modals.
- Implement `Escape` key listeners to close overlays.
- Ensure proper `role="dialog"` and `aria-modal="true"` attributes.

## Pro Tips

- Always test with actual assistive technologies (NVDA, VoiceOver) as automation only catches ~30% of issues.
- Prioritize semantic HTML before resorting to ARIA roles.
- Integrate accessibility checks into your CI/CD pipeline to catch regressions early.

## When to Use This Skill

- Auditing web applications to identify and remediate WCAG Level AA violations.
- Developing UI component libraries with built-in accessibility.
- Creating complex interactive patterns (grids, tabs, trees) that require ARIA.
