---
description: A persistent, iterative coding capability. "I'm a brick!" - but I get the job done. Use when the user wants you to "brute force" a solution, "keep trying until it works", or "Ralph Wiggum it".
---

# Ralph Wiggum Mode

> "I'm helping!" - Ralph Wiggum

This skill implements the **Ralph Wiggum Pattern**: a persistent, iterative approach to problem-solving. Instead of giving up or asking for help when a task fails, you will enter a loop of execution, verification, and self-correction.

## When to Use

- When a task is well-defined but might require multiple attempts to get right (e.g., fixing a flaky test, satisfying a linter, debugging a cryptic error).
- When the user explicitly says "Ralph Wiggum it", "keep trying", or "brute force this".
- When you are stuck in a loop of failing similar errors and need to break out by trying radically different approaches.

## The Loop

You will execute the following loop until **Success** or **Max Iterations** (default: 5) is reached.

1. **EXECUTE**: Attempt the task using your best current hypothesis.
2. **VERIFY**: Run a command to verify the result (e.g., `npm test`, `lint`, check file existence). **Crucial**: You must have a programmatic way to verify success.
3. **CHECK**:
    - **If Success**: Celebrate! ("I accepted the promise!") and Exit.
    - **If Failure**:
        - **Analyze**: Why did it fail? Read the error output *carefully*.
        - **Hypothesize**: Formulate a *new* hypothesis. Do not simply repeat the same action.
        - **Iterate**: Go back to Step 1.

## Rules of Ralph

1. **Persistence**: Do not stop after one failure. Try again.
2. **Variety**: Do not try the *exact same thing* twice. If `rm -rf` failed, try `del`. If that fails, try PowerShell.
3. **Verification**: You *must* run a verification command after every attempt.
4. **Logging**: Keep a brief "log" of your attempts in the conversation so the user knows you are iterating.

## Example Workflow

User: "Fix the build. Ralph Wiggum style."

**Iteration 1:**

- Action: Fix `tsconfig.json`.
- Verification: `npm run build`
- Result: **Fail** (Error: "Duplicate identifier").

**Iteration 2:**

- Analysis: "I introduced a duplicate identifier."
- Action: Remove the duplicate from `tsconfig.json`.
- Verification: `npm run build`
- Result: **Fail** (Error: "Missing type definition").

**Iteration 3:**

- Analysis: "Need to install types."
- Action: `npm install @types/node --save-dev`
- Verification: `npm run build`
- Result: **Success**.

**Exit:** "I did it!"
