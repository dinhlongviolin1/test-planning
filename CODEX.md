# CODEX.md

Agent instruction file for AI agents working with the `test-planning` markdown-based planning system.

## Project Overview

The `test-planning` repository is a markdown-based planning system that tracks:
- Issues — individual work items
- Epics — large features spanning multiple sprints
- Sprints — time-boxed work periods
- Milestones — long-term release targets
- Tasks — AI coding tasks

All data is stored as markdown files with structured meta tables, enabling AI agents to read, create, and update planning artifacts programmatically.

## Repository Structure

| Directory | Purpose | File Pattern |
|-----------|---------|--------------|
| `epics/` | Large features spanning multiple sprints | `e-XXX.md` |
| `issues/` | Individual work items | `i-XXX.md` |
| `sprints/` | Time-boxed work periods | `s-XXX.md` |
| `milestones/` | Long-term release targets | `m-XXX.md` |
| `tasks/` | AI coding tasks | `t-XXX.md` |
| `skills/` | Agent instructions | `*.md` |
| `scripts/` | Utility scripts | `*.py` |
| `docs/` | Project documentation | `*.md` |

The `sprints/` directory contains a `current.md` symlink/file pointing to the active sprint.

## Key Conventions

### Meta Tables

Every entity file contains a `## Meta` section with a markdown table:

```markdown
## Meta
| Field | Value |
|-------|-------|
| ID | x-001 |
| Status | active |
| Created | 2026-01-15 |
| Updated | 2026-05-06 |
```

### Sequential IDs

Before creating a new entity:
1. Read `_index.md` in the entity's directory to find `NEXT_ID`
2. Use that ID for the new file
3. Increment `NEXT_ID` in `_index.md`

### Bidirectional Links

Links between entities are always bidirectional:
- If an issue links to an epic, the epic must list that issue
- If a task links to an issue, the issue must list that task

## Status Values

### Issue Statuses

| Status | Meaning |
|--------|---------|
| `backlog` | Not yet prioritized |
| `todo` | Prioritized but not started |
| `in_progress` | Currently being worked on |
| `in_review` | Under review |
| `done` | Completed |
| `blocked` | Blocked by dependency |

### Task Statuses

| Status | Meaning |
|--------|---------|
| `pending` | Not yet queued |
| `queued` | Ready to run |
| `running` | Currently executing |
| `completed` | Successfully finished |
| `failed` | Failed to complete |
| `cancelled` | Cancelled before completion |

### Sprint Statuses

| Status | Meaning |
|--------|---------|
| `planning` | Sprint is being planned |
| `active` | Sprint is in progress |
| `completed` | Sprint has ended |

### Epic Statuses

| Status | Meaning |
|--------|---------|
| `draft` | Not yet finalized |
| `active` | In progress |
| `completed` | All work finished |

### Milestone Statuses

| Status | Meaning |
|--------|---------|
| `planned` | Scheduled for future |
| `in_progress` | Work ongoing |
| `completed` | Goals achieved |
| `missed` | Deadline not met |

## Critical Rules

1. **Never delete files** — mark entities as `cancelled` or `archived` instead
2. **Never modify IDs** — IDs are permanent and must not change
3. **Always update the `Updated` timestamp** — update on every modification
4. **Check the `Target Repo` field on issues** — code changes go to target repositories via coding tasks, not directly in this repo
5. **Read `skills/coding/`** before starting any coding task
6. **Confirm destructive actions** — ask before bulk operations

## Reference Files

| File | Purpose |
|------|---------|
| `CLAUDE.md` | Human-facing project instructions |
| `ARCHITECTURE.md` | High-level architecture overview (Go 1.25, React 19, PostgreSQL 18) |
| `README.md` | Full navigation guide with quest patterns |
| `skills/_index.md` | Agent navigation and skill loading priority |
| `skills/coding/conventions.md` | Code style and patterns |
| `skills/coding/testing.md` | Testing guidelines |

## Commit Format

Use conventional commits:

```
type(scope): message
```

### Types

| Type | When to Use |
|------|-------------|
| `feat` | New feature |
| `fix` | Bug fix |
| `docs` | Documentation changes |
| `style` | Formatting, no code change |
| `refactor` | Code restructuring |
| `test` | Adding/updating tests |
| `chore` | Maintenance tasks |

### Examples

- `feat(auth): add Google OAuth login`
- `fix(api): handle null response body`
- `docs(planning): update sprint template`