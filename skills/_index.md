# Project Skills

This folder contains instructions and conventions for AI agents working on this project.

## Skill Categories

| Category | Purpose | When Used |
|----------|---------|-----------|
| `coding/` | Code style, testing, patterns | Before any coding task |
| `views/` | View styling preferences | When generating custom views |

## Loading Priority

When executing a coding task:
1. ALWAYS load `coding/conventions.md`
2. ALWAYS load `coding/testing.md`
3. Load specific skills based on task type

## Adding New Skills

To add a new skill:
1. Create a markdown file in the appropriate category
2. Update the category's `_index.md`
3. The AI will automatically discover and use it
