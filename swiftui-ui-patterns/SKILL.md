---
name: swiftui-ui-patterns
description: Guideline for building clean, maintainable, and scalable SwiftUI interfaces for iOS.
---

# SwiftUI UI Patterns

Expert guidance on creating performant iOS applications with SwiftUI.

## State Management

- `@State`: Local view-private state.
- `@Binding`: Two-way data flow between parent and child.
- `@Observable`: Modern reactive data models (iOS 17+).
- `@Environment`: Dependencies and system settings.

## Component Patterns

### Sheets with Selection

```swift
@State private var selectedItem: Item?

.sheet(item: $selectedItem) { item in
    EditItemSheet(item: item)
}
```

### Async Tasks

```swift
.task {
    await store.fetch()
}
```

## Pro Tips

- Use `.task` instead of `onAppear` for async data loading to handle cancellation automatically.
- Keep Views lightweight; extract complex logic into observable models.
- Leverage `EnvironmentValues` for dependency injection and theme management.

## When to Use This Skill

- Designing new SwiftUI features or screens with complex state.
- Refactoring legacy SwiftUI code for better performance and maintainability.
- Implementing standard iOS UI patterns like TabView and NavigationStack.
