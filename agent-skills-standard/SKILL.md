---
description: Standardization guide for creating new AI Agent Skills. Use this when the user asks to "create a skill" or "standardize skills".
---

# Agent Skills Standard

Follow this template when creating new `SKILL.md` files to ensure compatibility with the Antigravity system and modern AI agent standards.

## File Location

Skills live in: `.gemini/antigravity/skills/<skill-name>/SKILL.md`

## SKILL.md Template

```markdown
---
description: [Short, action-oriented description. Triggers for the AI.]
---

# [Skill Name]

[Brief introduction to the skill and its purpose.]

## When to Use
- [Scenario 1]
- [Scenario 2]

## Core Capabilities / Rules
[Detailed instructions, "Do's and Don'ts", and best practices.]

## Tools & Commands
[If this skill relies on specific CLI tools, list them here with examples.]

## Example Workflow
[A brief scenario showing the skill in action.]
```

## Best Practices

1. **YAML Frontmatter**: The `description` in the frontmatter is CRITICAL. It is the primary signal for the AI to select the skill. Keep it concise but descriptive.
2. **Instructional, Not Descriptive**: Don't just describe *what* something is. Tell the agent *how* to do it. Use imperative verbs ("Do this", "Check that").
3. **Checklists**: AI agents love checklists. Use them for audits or verification steps.
4. **Context**: Provide context on *why* a rule exists (e.g., "for performance", "for accessibility").
5. **Examples**: Provide good/bad code examples if the skill involves coding patterns.
