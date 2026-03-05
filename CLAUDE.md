# CLAUDE.md - AI Agent Project Overview

This file provides a comprehensive overview of the project for AI agents. It complements README.md by being specifically tailored for AI agents.

## Project Purpose and Description

This is a **file-based project management system** using markdown files to track:
- **Issues** - Individual work items and user stories
- **Tasks** - AI coding tasks for automated implementation
- **Epics** - Large features that span multiple sprints
- **Sprints** - Time-boxed work periods (usually 1-2 weeks)
- **Milestones** - Long-term release targets and version planning
- **Team Members** - Project team information

All data is stored in markdown files with a consistent format using Meta tables.

## Directory Structure

```
/workspace/repo/
├── README.md              # Project overview (don't modify)
├── project.md             # Detailed agent navigation guide
├── team.md                # Team members (for @mentions)
├── CLAUDE.md              # AI Agent overview (this file)
│
├── milestones/            # Long-term release targets
│   ├── _index.md          # Overview + NEXT_ID counter
│   └── m-XXX.md           # Individual milestone files
│
├── epics/                 # Large features (span multiple sprints)
│   ├── _index.md          # Overview + NEXT_ID counter
│   └── e-XXX.md           # Individual epic files
│
├── sprints/               # Time-boxed work periods
│   ├── _index.md          # Overview + NEXT_ID counter
│   ├── current.md         # Points to active sprint (important!)
│   └── s-XXX.md           # Individual sprint files
│
├── issues/                # Individual work items
│   ├── _index.md          # Overview + NEXT_ID counter
│   └── i-XXX.md           # One file per issue (self-contained)
│
├── tasks/                 # AI coding tasks
│   ├── _index.md          # Overview + NEXT_ID counter
│   └── t-XXX.md           # One file per task
│
├── skills/                # Instructions for AI agents
│   ├── coding/            # Coding conventions and guidelines
│   │   ├── conventions.md # File structure, naming, code style
│   │   └── testing.md     # Testing requirements
│   └── _index.md          # Skills overview
│
└── scripts/               # Utility scripts
    └── README.md          # Scripts documentation
```

## Key Files

| File | Purpose |
|------|---------|
| `project.md` | **Detailed agent navigation guide** - READ THIS FIRST for navigation instructions |
| `team.md` | Team members with usernames, roles, and capacity |
| `README.md` | Project overview (human-readable) |
| `issues/_index.md` | Issue list + NEXT_ID counter (currently 13) |
| `tasks/_index.md` | Task list + NEXT_ID counter (currently 2) |
| `sprints/current.md` | Points to active sprint |
| `skills/coding/conventions.md` | Coding standards and conventions |
| `skills/coding/testing.md` | Testing requirements |

## Conventions

### Meta Tables
Every entity file contains a Meta table at the top:
```markdown
## Meta
| Field | Value |
|-------|-------|
| ID | x-001 |
| Status | active |
| Created | 2026-01-29 |
| Updated | 2026-01-29 |
```

### ID Naming Conventions
| Entity | Prefix | Example |
|--------|--------|---------|
| Issues | i- | i-001, i-002 |
| Epics | e- | e-001, e-002 |
| Sprints | s- | s-001, s-002 |
| Milestones | m- | m-001, m-002 |
| Tasks | t- | t-001, t-002 |

### Status Values
| Entity | Valid Statuses |
|--------|---------------|
| Issue | backlog, todo, in_progress, in_review, done, blocked |
| Task | pending, queued, running, completed, failed, cancelled |
| Sprint | planning, active, completed |
| Epic | draft, active, completed |
| Milestone | planned, in_progress, completed, missed |

### Bidirectional Linking
- If an issue links to a task → the task links back to the issue
- If an issue is in a sprint → the sprint lists the issue
- Always maintain cross-references when updating

### Creating New Entities
1. Read `_index.md` in the relevant directory to get NEXT_ID
2. Create the new file using the entity template
3. Update `_index.md` to increment NEXT_ID
4. Update timestamps (Updated field) on all modified files

## Guidelines for AI Agents

### Navigation
1. **Start with project.md** - It contains the detailed navigation guide
2. **Check current sprint** - Read `sprints/current.md` first to find active sprint
3. **Find NEXT_ID** - Always read `_index.md` before creating new entities

### Common Operations

**Show current sprint:**
1. Read `sprints/current.md` to get active sprint ID
2. Read `sprints/s-{id}.md` for full sprint details

**Create a new issue:**
1. Read `issues/_index.md` to get NEXT_ID
2. Create `issues/i-{NEXT_ID}.md` using the issue template
3. Update `issues/_index.md` to increment NEXT_ID

**Move issue to Done:**
1. Read issue file `issues/i-X.md`
2. Update Status to `done`
3. Update `updated` timestamp

**Create coding task:**
1. Read `issues/i-X.md` thoroughly
2. Note the `Target Repo` field
3. Read `skills/coding/` for conventions
4. Create `tasks/t-{NEXT_ID}.md` with full context
5. Update `tasks/_index.md` to increment NEXT_ID

### Critical Rules
1. **Never delete files** - Mark as archived/cancelled instead
2. **Never modify IDs** - IDs are permanent
3. **Always update timestamps** - `Updated` field on every change
4. **Check target repo** - Issues specify which repo code goes to
5. **Read skills first** - Before coding tasks, read `skills/coding/`
6. **Confirm destructive actions** - Ask before bulk changes

## Important Notes

- **Detailed Navigation Guide**: See `project.md` for comprehensive agent navigation instructions
- **Coding Conventions**: See `skills/coding/conventions.md` for file structure, naming, and code style
- **Testing Guidelines**: See `skills/coding/testing.md` for coverage requirements and test structure

## Entity Relationships

```
Milestone (v1.0)
    │
    └── Epic (Authentication)
            │
            ├── Issue (Implement OAuth)
            │       │
            │       └── Task (AI coding task) ──→ PR (in code repo)
            │
            └── Issue (Add MFA)
                    │
                    └── Task ──→ PR
```

## Tips for Success

- **Start by reading** - Always read relevant files before changing anything
- **Be conservative** - When unsure, ask the user
- **Link everything** - Cross-references help everyone navigate
- **Use the skills** - Project-specific instructions are in `skills/`
- **Commit often** - Each change is a git commit with a clear message