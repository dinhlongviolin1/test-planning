# CLAUDE.md — AI Guidance for test-planning Repo

This file is for AI agents (Claude Code). For human-oriented documentation, see [README.md](README.md).

## 1. Project Overview

This is a **markdown-based project management repository**, not an application codebase. It manages sprints, issues, epics, milestones, tasks, and team members via structured markdown files. Work items here represent tasks on a separate linked code repository (see `project.md` for linked repos). There is no build system, no test suite, and no deployable app in this repo.

## 2. Directory Structure

```
/
├── project.md          — Project metadata and linked code repositories
├── team.md             — Team roster with roles
├── epics/              — Large features (e-NNN.md), spanning multiple issues/sprints
├── issues/             — Individual work items (i-NNN.md), linked to epics and sprints
├── sprints/            — Time-boxed work periods (s-NNN.md)
│   └── current.md      — Always points to the active sprint
├── tasks/              — AI coding tasks (t-NNN.md) derived from issues
│   └── _index.md       — Tracks NEXT_ID and lists all tasks
├── milestones/         — Release targets (m-NNN.md)
├── skills/             — Project conventions Claude Code must follow
│   └── coding/
│       ├── conventions.md  — Code style and architecture patterns
│       └── testing.md      — Testing guidelines
└── scripts/            — Utility scripts
```

Each directory has an `_index.md` with an overview and the NEXT_ID counter.

## 3. File Format Conventions

Every entity file starts with a `# Meta` section containing a markdown table:

```markdown
## Meta
| Field | Value |
|-------|-------|
| ID    | i-001 |
| Status | in_progress |
| Created | 2026-01-30 |
| Updated | 2026-01-30 |
```

**ID naming:** `e-NNN` (epics), `i-NNN` (issues), `s-NNN` (sprints), `t-NNN` (tasks), `m-NNN` (milestones). IDs are zero-padded to three digits.

**NEXT_ID tracking:** Each directory's `_index.md` has a `## Next ID` section. Read it before creating a new entity, then increment it after creation.

**Valid statuses:** `pending`, `in_progress`, `done`, `blocked`, `todo`, `cancelled`

## 4. Entity Relationships

```
Milestone (m-NNN)
    └── Epic (e-NNN)
            └── Issue (i-NNN)  ←── also belongs to Sprint (s-NNN)
                    └── Task (t-NNN) ──→ PR (in linked code repo)
```

- **Milestones** group epics into release targets
- **Epics** group related issues into large features
- **Sprints** contain issues (orthogonal to the epic hierarchy — an issue has both an epic and a sprint)
- **Tasks** are AI coding tasks derived from issues; they produce PRs in the linked code repository

**Bidirectional linking is required.** If issue `i-001` references epic `e-001`, then `e-001` must also list `i-001`. Always update both sides when creating or modifying links.

## 5. Common Workflows

### Reading an issue
1. Read `issues/i-NNN.md`
2. Parse the meta table for status, assignee, points
3. Follow links to read the epic (`epics/e-NNN.md`) and sprint (`sprints/s-NNN.md`)

### Navigating to the current sprint
1. Read `sprints/current.md` to get the active sprint ID
2. Read `sprints/s-NNN.md` for full sprint details

### Updating status
- Edit the `Status` field in the meta table of the relevant file
- Update the `Updated` timestamp
- Valid statuses: `pending`, `in_progress`, `done`, `blocked`, `cancelled`

### Creating a new task
1. Read `tasks/_index.md` to get `NEXT_ID` (e.g., `2`)
2. Create `tasks/t-NNN.md` following the format of `tasks/t-001.md`
3. Increment `NEXT_ID` in `tasks/_index.md`
4. Add the new task to the list table in `tasks/_index.md`
5. Update the linked issue file to reference the new task

### Finding coding conventions
- Read `skills/coding/conventions.md` for code style and architecture patterns
- Read `skills/coding/testing.md` for testing guidelines

## 6. Critical Rules

- **Never delete files** — mark as `cancelled` or `done` instead
- **Never reuse IDs** — always read `NEXT_ID` from `_index.md` and increment it after use
- **Preserve existing IDs and links** — do not change IDs when editing files
- **Always update bidirectional links** — if A references B, B must also reference A
- **Always update timestamps** — set the `Updated` field on every change
- **Commit format:** `type(scope): description` (e.g., `docs(claude): add CLAUDE.md`)

## 7. What NOT To Do

- **Do not run build, test, or deploy commands** — none exist in this repo
- **Do not lint or type-check markdown files** — they are data, not code
- **Do not create new entity types** — only use epics, issues, sprints, tasks, milestones
- **Do not modify README.md** — it is the human-facing guide
- **Do not write application code here** — code changes go to the linked repository via tasks

For detailed coding conventions used in linked repositories, see `skills/coding/conventions.md`.
