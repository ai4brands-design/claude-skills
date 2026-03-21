---
description: Expert guidelines for React and Next.js performance, focused on Vercel's best practices (Jan 2026).
---

# Vercel React Patterns & Best Practices (2026)

This skill encapsulates the latest "Agent Skills" from Vercel for optimizing React and Next.js applications. Use this when writing, refactoring, or reviewing React/Next.js code.

## Core Principles

### 1. React Compiler Readiness

* **Rule**: Write code that is compatible with the React Compiler (React 19+).
* **Do**: Use standard JavaScript semantics. The compiler automatically memoizes components and hooks.
* **Don't**: Overuse `useMemo` or `useCallback` manually unless necessary for specific referential equality checks that the compiler might miss (rare).
* **Check**: Ensure components are pure and idempotent where possible.

### 2. Server Components First

* **Rule**: Default to Server Components. Only use Client Components (`"use client"`) when interactivity is strictly required.
* **Why**: Reduces client-side bundle size, improves Initial Page Load (IPL), and moves data fetching closer to the database.
* **Pattern**:

    ```tsx
    // Server Component (default)
    import { db } from './db';
    import ClientComponent from './ClientComponent';

    export default async function Page() {
      const data = await db.query();
      return (
        <div>
          <h1>{data.title}</h1>
          <ClientComponent interactiveData={data.interactive} />
        </div>
      );
    }
    ```

### 3. Core Web Vitals (CWV) Optimization

* **LCP (Largest Contentful Paint)**:
  * Prioritize the "hero" image.
  * Use `next/image` with `priority={true}` for LCP elements.
  * Avoid lazy loading LCP images.
* **CLS (Cumulative Layout Shift)**:
  * Always define explicit `width` and `height` for images and containers.
  * Use skeleton loaders (UI placeholders) while data is loading to preserve layout.
* **INP (Interaction to Next Paint)**:
  * Does the UI respond quickly?
  * Avoid long-running tasks on the main thread during interactions.
  * Use `useTransition` for non-urgent state updates.

### 4. Vercel Deployment & Edge

* **Edge Functions**: Use for personalized, low-latency tasks (e.g., A/B testing middleware, geo-blocking).
* **ISR (Incremental Static Regeneration)**: Use for content that changes but doesn't need to be live-real-time only on every request.
* **PPR (Partial Prerendering)**: (If available/experimental) Adopt PPR to combine static shell with dynamic holes.

## Code Review Checklist

When reviewing React code, ask:

1. [ ] Could this be a Server Component?
2. [ ] Is `next/image` used for all images?
3. [ ] Are fonts optimized (`next/font`)?
4. [ ] Is metadata statically generated where possible?
5. [ ] Are we fetching data in a waterfall? (Use `Promise.all` or parallel server components).
