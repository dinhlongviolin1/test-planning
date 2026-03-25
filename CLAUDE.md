# CLAUDE.md — AI Assistant Reference

This file provides essential context for AI assistants working in this repository.

## Project Overview

This is a **markdown-based project planning repository** that manages software projects through markdown files. It tracks:
- **Milestones** — Long-term release targets
- **Epics** — Large features spanning multiple sprints
- **Sprints** — Time-boxed work periods
- **Issues** — Individual work items
- **Tasks** — AI coding tasks for target repositories

The repository acts as a "game world" where AI assistants manage project state by reading and writing markdown files. Code changes are pushed to target repositories via coding tasks, not directly in this planning repo.

## Tech Stack

This is a **planning/markdown-based project**, not a code project.

- **Storage**: Markdown files (`.md`)
- **Scripts**: Python scripts in `/scripts` directory
  - `list_users.py` — Lists all users
  - `get_team_members.py` — Retrieves team members from team.md

## File Structure

```
/                           # Root of planning repo
├── README.md               # Main entry point with navigation guide
├── project.md              # Project overview, linked code repos
├── team.md                 # Team members (for @mentions)
├── CLAUDE.md               # AI assistant reference (this file)
│
├── milestones/             # Long-term release targets
│   ├── _index.md           # Overview + how to use
│   └── m-XXX.md            # Individual milestones
│
├── epics/                  # Large features (span multiple sprints)
│   ├── _index.md
│   └── e-XXX.md
│
├── sprints/                # Time-boxed work periods
│   ├── _index.md
│   ├── current.md          # Points to active sprint
│   └── s-XXX.md
│
├── issues/                 # Individual work items
│   ├── _index.md           # Overview + NEXT ID COUNTER
│   └── i-XXX.md            # One file per issue
│
├── tasks/                  # AI coding tasks
│   ├── _index.md           # Overview + NEXT ID COUNTER
│   └── t-XXX.md            # One file per task
│
├── skills/                 # Instructions for AI assistants
│   ├── coding/             # How to write code for this project
│   │   ├── _index.md
│   │   ├── conventions.md  # Coding standards
│   │   └── testing.md      # Testing requirements
│   └── views/              # How to style views
│
└── scripts/                # Python utility scripts
    ├── README.md
    ├── list_users.py
    └── get_team_members.py
```

## Coding Standards

When writing code for target repositories, follow the conventions in:
- `skills/coding/conventions.md` — File structure, naming conventions, code style
- `skills/coding/testing.md` — Coverage requirements, test structure, mocking rules

Key conventions:
- **Commits**: Use conventional format `type(scope): message` (feat, fix, docs, style, refactor, test, chore)
- **File naming**: kebab-case for files, PascalCase for classes, camelCase for functions, SCREAMING_SNAKE for constants

## Testing Requirements

Follow `skills/coding/testing.md` for all test-related work:
- Minimum 80% code coverage, 100% for critical paths
- Use Arrange-Act-Assert pattern
- Mock external services, not owned code

## Common Workflows

### Creating a New Issue
1. Read `issues/_index.md` to get the NEXT_ID
2. Create `issues/i-{NEXT_ID}.md` using the issue template
3. Update `issues/_index.md` to increment NEXT_ID
4. If sprint specified, update the sprint file's issue list
5. If epic specified, update the epic file's issue list

### Moving Issues Between Statuses
1. Read the issue file `issues/i-X.md`
2. Update the Status field (backlog, todo, in_progress, in_review, done, blocked)
3. Update the `updated` timestamp
4. Read `sprints/current.md` to get current sprint
5. Update sprint file: move issue from old status list to new status list

### Creating a Coding Task
1. Read `issues/i-X.md` thoroughly
2. Note the `Target Repo` field - that's where code goes
3. Read `skills/coding/` for project conventions
4. Create `tasks/t-{NEXT_ID}.md` with full context
5. Update `tasks/_index.md` to increment NEXT_ID
6. Update issue file to link the task

### Viewing Current Sprint
1. Read `sprints/current.md` to get the active sprint ID
2. Read `sprints/s-{id}.md` for full sprint details

## Important Files

| File | Purpose |
|------|---------|
| `README.md` | Main entry point with navigation guide |
| `project.md` | Project overview and linked repositories |
| `team.md` | Team member details |
| `skills/coding/conventions.md` | Coding standards |
| `skills/coding/testing.md` | Testing requirements |
| `issues/_index.md` | Issue counter (NEXT_ID) |
| `tasks/_index.md` | Task counter (NEXT_ID) |

## File Format Rules

Every entity file has a Meta table:
```markdown
## Meta
| Field | Value |
|-------|-------|
| ID | x-001 |
| Status | active |
| Updated | 2026-03-25 |
```

**Status values:**
- Issues: backlog, todo, in_progress, in_review, done, blocked
- Tasks: pending, queued, running, completed, failed, cancelled
- Sprints: planning, active, completed
- Epics: draft, active, completed
- Milestones: planned, in_progress, completed, missed

## Critical Rules

1. **Never delete files** — Mark as archived/cancelled instead
2. **Never modify IDs** — IDs are permanent
3. **Always update timestamps** — `Updated` field on every change
4. **Check target repo** — Issues specify which repo code goes to
5. **Read skills first** — Before coding tasks, read `skills/coding/`
6. **Bidirectional links** — If issue links to task, task links back to issue