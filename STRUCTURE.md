# Repository Structure

This document describes the directory layout, file naming conventions, and organization of the `test-planning` repository. It complements [CLAUDE.md](CLAUDE.md) (conventions and agent rules), [ARCHITECTURE.md](ARCHITECTURE.md) (system architecture and tech stack), and [README.md](README.md) (agent navigation guide).

## Directory Tree

```
/
├── ARCHITECTURE.md
├── CLAUDE.md
├── LICENSE.md
├── README.md
├── agents.md
├── project.md
├── team.md
├── team_members.py
│
├── epics/
│   ├── _index.md
│   └── e-XXX.md
│
├── issues/
│   ├── _index.md
│   └── i-XXX.md
│
├── sprints/
│   ├── _index.md
│   ├── current.md
│   └── s-XXX.md
│
├── milestones/
│   ├── _index.md
│   └── m-XXX.md
│
├── tasks/
│   ├── _index.md
│   └── t-XXX.md
│
├── skills/
│   ├── _index.md
│   └── coding/
│       ├── _index.md
│       ├── conventions.md
│       └── testing.md
│
├── scripts/
│   ├── README.md
│   ├── get_all_issues_and_epics.py
│   ├── get_team_members.py
│   └── list_users.py
│
├── docs/
│   ├── api-spec.md
│   ├── architecture.md
│   ├── meeting-notes.md
│   ├── overview.md
│   ├── design/
│   │   └── ux-guidelines.md
│   └── engineering/
│       ├── setup.md
│       └── backend/
│           └── api-routes.md
│
└── uploads/
    ├── architecture-summary.pdf
    ├── project-notes-screenshot.png
    └── sprint-notes.txt
```

## Entity Directories

Entity directories store the core project management data. Each directory contains markdown files following a consistent naming pattern and structure.

- **epics/** — Large features spanning multiple sprints. Files use the `e-XXX.md` naming pattern (e.g., `e-001.md`, `e-002.md`).
- **issues/** — Individual work items. Files use the `i-XXX.md` pattern (e.g., `i-001.md`, `i-042.md`).
- **sprints/** — Time-boxed work periods. Files use the `s-XXX.md` pattern (e.g., `s-001.md`, `s-003.md`). Also contains `current.md`, which points to the active sprint.
- **milestones/** — Long-term release targets. Files use the `m-XXX.md` pattern (e.g., `m-001.md`).
- **tasks/** — AI coding tasks dispatched to coding agents. Files use the `t-XXX.md` pattern (e.g., `t-001.md`, `t-015.md`).

Every entity file contains a `## Meta` section with a structured markdown table. See [CLAUDE.md](CLAUDE.md) for valid status values and critical rules for working with entities.

## Index Files

Every entity directory contains a `_index.md` file that serves two purposes:

1. **ID counter** — Tracks a `NEXT_ID` value used for sequential ID assignment. When creating a new entity, read `_index.md` to get the next available ID, then increment `NEXT_ID` after creation.
2. **Entity listing** — Contains a table or list of all entities in that directory for quick reference.

This convention ensures IDs are unique and sequential across all entities of a given type.

## Supporting Directories

- **skills/** — Agent instructions and conventions loaded by AI agents before coding tasks. Contains its own `_index.md` and a `coding/` subdirectory with `conventions.md` (code style and project conventions) and `testing.md` (testing guidelines).
- **scripts/** — Utility scripts for working with the repository. Includes `get_all_issues_and_epics.py`, `get_team_members.py`, and `list_users.py`. Has its own `README.md` with usage instructions.
- **docs/** — Project documentation. Root-level files include `api-spec.md`, `architecture.md`, `meeting-notes.md`, and `overview.md`. Subdirectories: `design/` (contains `ux-guidelines.md`) and `engineering/` (contains `setup.md` and `backend/api-routes.md`). See [ARCHITECTURE.md](ARCHITECTURE.md) for tech stack details.
- **uploads/** — Uploaded reference files including PDFs, screenshots, and notes used for project context.

## Root-Level Files

- `ARCHITECTURE.md` — High-level system architecture, tech stack, and data flow (see that file for details)
- `CLAUDE.md` — AI agent conventions, rules, and guidelines for working in this repository
- `README.md` — Navigation guide for AI agents with quest patterns and file format rules
- `LICENSE.md` — Project license (Apache 2.0)
- `agents.md` — Agent configuration and capabilities
- `project.md` — Project overview and linked code repositories
- `team.md` — Team members and roles
- `team_members.py` — Script for team member data

## Naming Patterns

| Entity | Pattern | Example |
|--------|---------|---------|
| Epic | `e-XXX.md` | `e-001.md` |
| Issue | `i-XXX.md` | `i-042.md` |
| Sprint | `s-XXX.md` | `s-003.md` |
| Milestone | `m-XXX.md` | `m-001.md` |
| Task | `t-XXX.md` | `t-015.md` |
