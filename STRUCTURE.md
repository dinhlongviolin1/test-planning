# Structure

This file documents the physical file and folder layout of the repository. See `CLAUDE.md` for conventions and critical rules, and `ARCHITECTURE.md` for the tech stack and system architecture.

## Directory Tree

```
/
├── README.md
├── CLAUDE.md
├── ARCHITECTURE.md
├── STRUCTURE.md          ← this file
├── LICENSE.md
├── agents.md
├── project.md
├── team.md
├── team_members.py
├── .gitignore
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
├── docs/
│   ├── overview.md
│   ├── architecture.md
│   ├── api-spec.md
│   ├── meeting-notes.md
│   ├── design/
│   │   └── ux-guidelines.md
│   └── engineering/
│       ├── setup.md
│       └── backend/
│           └── api-routes.md
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
└── uploads/
    ├── architecture-summary.pdf
    ├── project-notes-screenshot.png
    └── sprint-notes.txt
```

## Root Files

| File | Purpose |
|------|---------|
| `README.md` | Agent navigation guide and quest patterns |
| `CLAUDE.md` | AI agent instructions, conventions, and critical rules |
| `ARCHITECTURE.md` | System architecture, tech stack, and data flow |
| `STRUCTURE.md` | This file -- repository layout reference |
| `LICENSE.md` | Apache 2.0 license |
| `agents.md` | Agent configuration and capabilities |
| `project.md` | Project overview and linked code repositories |
| `team.md` | Team members for @mentions |
| `team_members.py` | Script to list team members programmatically |
| `.gitignore` | Git ignore rules |

## Entity Directories

The five entity directories (`epics/`, `issues/`, `sprints/`, `milestones/`, `tasks/`) share a common structure:

- Each directory contains an `_index.md` that tracks a `NEXT_ID` counter used for sequential ID assignment when creating new entities.
- Entity files follow a zero-padded three-digit naming pattern: `e-XXX.md`, `i-XXX.md`, `s-XXX.md`, `m-XXX.md`, `t-XXX.md`.
- Every entity file has a `## Meta` section with a structured markdown table. See `CLAUDE.md` for the meta table format and valid status values per entity type.

### Special file: `sprints/current.md`

`sprints/current.md` is a pointer file that identifies the currently active sprint. It is not a sprint entity itself -- it references the active `s-XXX.md` file.

### Entity Hierarchy

Entities relate to each other in a top-down hierarchy. All cross-references between entities are bidirectional (see `CLAUDE.md`).

```
Milestone → Epic → Issue → Task → PR
```

## Documentation (`docs/`)

Project documentation and reference materials.

- `overview.md` -- high-level project overview
- `architecture.md` -- detailed architecture notes (supplements root `ARCHITECTURE.md`)
- `api-spec.md` -- API endpoint specification
- `meeting-notes.md` -- meeting notes and decisions
- `design/` -- UX and design documentation (`ux-guidelines.md`)
- `engineering/` -- engineering setup and guides (`setup.md`)
- `engineering/backend/` -- backend-specific documentation (`api-routes.md`)

The `docs/` directory also contains non-markdown assets (PDF, PNG, TXT) that are copies of files stored in `uploads/`.

## Skills (`skills/`)

Agent instruction files that define how AI agents should approach coding tasks.

- `_index.md` -- skill registry, categories, and loading priority
- `coding/conventions.md` -- code style, naming patterns, and architectural patterns
- `coding/testing.md` -- testing guidelines, frameworks, and coverage expectations

### Loading Priority

When executing a coding task, agents must always load `coding/conventions.md` and `coding/testing.md` before starting work. Additional skills are loaded based on task type.

## Scripts (`scripts/`)

Python utility scripts for querying project data. See `scripts/README.md` for usage details.

| Script | Purpose |
|--------|---------|
| `get_all_issues_and_epics.py` | Parse and list all issues and epics from their markdown files |
| `get_team_members.py` | Parse team member information from `team.md` |
| `list_users.py` | List all team members (CLI wrapper around `team_members.py`) |

## Uploads (`uploads/`)

Asset storage for binary and non-markdown files such as PDFs, images, and text files. These files are referenced by docs and other markdown files throughout the repository.

## Conventions

This section provides a brief summary -- see `CLAUDE.md` for full details.

- **Meta tables:** Every entity file has a `## Meta` section with a structured markdown table containing fields like ID, Status, and Updated.
- **Sequential IDs:** Each entity directory's `_index.md` tracks a `NEXT_ID` counter. Read it before creating a new entity, then increment it after creation.
- **Bidirectional links:** All cross-references between entities are maintained in both directions. If an issue links to an epic, the epic must also list the issue.
- **Status values:** Each entity type has its own set of valid statuses, defined in `CLAUDE.md`.
