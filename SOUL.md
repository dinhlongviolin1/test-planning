# SOUL.md — AI Assistant Guidance

## Project Essence

- **Project**: test-planning
- **Type**: Documentation/Project Management System
- **Core Functionality**: Manage software projects through markdown-based file operations. AI assistants act as project managers, creating and updating issues, tasks, sprints, and tracking progress.
- **Active Since**: 2026-01-29

## Architecture

This is a file-based project management system where:
- **Issues** represent individual work items
- **Tasks** are AI coding assignments that produce PRs
- **Epics** group related issues across sprints
- **Sprints** are time-boxed work periods
- **Milestones** are release targets

All data flows through markdown files with standardized Meta tables.

## Data Flow

```
Milestone (v1.0)
    │
    └── Epic (Feature Area)
            │
            ├── Issue (Work Item) ──→ Status transitions
            │       │
            │       └── Task (Coding Assignment) ──→ Target Repo PR
            │
            └── Issue → ...
```

## Working Guidelines

### Before Making Changes
1. Always read the relevant file(s) first
2. Check `_index.md` for ID counters before creating new entities
3. Understand existing file structure from similar files

### When Updating Files
1. Preserve all existing IDs
2. Update the `Updated` timestamp in Meta tables
3. Maintain bidirectional links (if A links to B, B must link to A)
4. Use exact status values from the valid set

### Status Transitions

| Entity | Valid Transitions |
|--------|-------------------|
| Issue | backlog → todo → in_progress → in_review → done |
| Task | pending → queued → running → completed/failed |
| Sprint | planning → active → completed |

## Team Structure

Team capacity is 90 pts/sprint across 9 members. See `team.md` for member details and roles.

## Important Notes

- This is a **planning repository** — actual code goes to linked repos
- View generation: you provide JSON data, frontend renders it
- Commit each meaningful change with a clear message
- When unsure, read more files before proceeding

## Quick Reference

| Need | File |
|------|------|
| Current sprint | `sprints/current.md` |
| Next issue ID | `issues/_index.md` |
| Next task ID | `tasks/_index.md` |
| Coding conventions | `skills/coding/conventions.md` |
| Team info | `team.md` |

## Philosophy

- **Conservative**: Prefer asking over guessing
- **Linkable**: Cross-references help navigation
- **Timestamped**: Every change has an Updated field
- **Permanent IDs**: Never reuse or modify existing IDs