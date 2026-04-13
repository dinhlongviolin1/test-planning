# CLAUDE.md — AI Assistant Guide

This file provides instructions for AI agents working on this planning repository.

## Overview

This is a **test-planning** repository — a project management system that organizes work as markdown files. The hierarchy flows: **Milestones → Epics → Sprints → Issues → Tasks**. All data lives in this repository; code changes go to target repositories.

## Project Structure

```
/                   # Root
├── milestones/     # Long-term release targets (m-XXX.md)
├── epics/          # Large features spanning sprints (e-XXX.md)
├── sprints/        # Time-boxed work periods (s-XXX.md)
├── issues/         # Individual work items (i-XXX.md)
├── tasks/          # AI coding tasks (t-XXX.md)
├── skills/         # Instructions for AI agents
│   ├── coding/conventions.md   # Required before coding
│   └── coding/testing.md       # Testing requirements
├── project.md      # Project overview + linked repos
└── team.md         # Team members
```

## Key Conventions

### File IDs
- IDs are sequential and permanent: `m-001`, `e-001`, `s-001`, `i-001`, `t-001`
- Always read `_index.md` to get the NEXT_ID before creating files
- Never modify existing IDs

### Timestamps
- Update the `Updated` field on every file modification
- Format: `YYYY-MM-DD`

### Status Values
| Entity   | Valid Statuses                                      |
|----------|-----------------------------------------------------|
| Issue    | backlog, todo, in_progress, in_review, done, blocked |
| Task     | pending, queued, running, completed, failed, cancelled |
| Sprint   | planning, active, completed                        |
| Epic     | draft, active, completed                           |
| Milestone| planned, in_progress, completed, missed            |

### Links
- Cross-references are bidirectional: issue → task, task → issue
- If an issue is in a sprint, the sprint file lists it

## Critical Rules

1. **Never delete files** — Mark as archived/cancelled instead
2. **Preserve IDs** — IDs are permanent identifiers
3. **Always update timestamps** — `Updated` field on every change
4. **Read skills before coding** — Load `skills/coding/conventions.md` and `skills/coding/testing.md` before implementing
5. **Confirm destructive actions** — Ask before bulk changes

## Workflow Patterns

### Create New Issue
1. Read `issues/_index.md` to get NEXT_ID
2. Create `issues/i-{NEXT_ID}.md` using existing issue as template
3. Update `issues/_index.md` to increment NEXT_ID
4. Link to epic/sprint if specified
5. Update timestamp

### Move Issue to Done
1. Read issue file, update Status to `done`
2. Update `Updated` timestamp
3. Update sprint file: move issue to `done` list

### Create Coding Task
1. Read issue to understand requirements and target repo
2. Read `skills/coding/conventions.md` and `skills/coding/testing.md`
3. Read `tasks/_index.md` to get NEXT_ID
4. Create `tasks/t-{NEXT_ID}.md` with full context
5. Update `tasks/_index.md` to increment NEXT_ID
6. Link task in issue file
7. Commit changes

## Commit Format

Use: `feat(docs): <description>`

Examples:
- `feat(docs): add CLAUDE.md with AI assistant instructions`
- `feat(docs): create SOUL.md with core principles`

Stage files explicitly — never use `git add -A` or `git add .`

## Reading Order

When working on a task:
1. Read `README.md` for project overview
2. Read relevant section files (`_index.md`) for current state
3. Read specific files (issue, epic, sprint) for context
4. Read skills in `skills/coding/` before implementing code tasks