# CLAUDE.md - LLM Context File

This file provides essential context for AI assistants working with this repository.

## Project Overview

This is the **test-planning** repository - a project management system where all data (issues, sprints, epics, milestones, tasks) is stored as markdown files. The AI assistant manages software projects by reading/writing these markdown files and creating coding tasks for implementation in linked repositories.

## Repository Structure

```
/                           # Root of planning repo
├── CLAUDE.md              # This file - LLM context
├── README.md              # Detailed agent guide (read this first for workflows)
├── project.md             # Project overview, linked code repositories
├── team.md                # Team members (for @mentions)
├── issues/                # Individual work items (i-XXX.md)
├── tasks/                 # AI coding tasks (t-XXX.md)
├── epics/                 # Large features (e-XXX.md)
├── sprints/               # Time-boxed work periods (s-XXX.md)
├── milestones/            # Release targets (m-XXX.md)
└── skills/                # Project-specific instructions for AI
    └── coding/            # Coding conventions and testing guidelines
```

## Key Files

| File | Purpose |
|------|---------|
| `issues/_index.md` | Issue list with NEXT_ID counter |
| `tasks/_index.md` | Task list with NEXT_ID counter |
| `sprints/current.md` | Points to active sprint |
| `skills/coding/conventions.md` | Tech stack and code style |
| `skills/coding/testing.md` | Testing guidelines |

## ID Conventions

- Issues: `i-XXX` (e.g., i-001, i-002)
- Tasks: `t-XXX` (e.g., t-001, t-002)
- Epics: `e-XXX`
- Sprints: `s-XXX`
- Milestones: `m-XXX`

Always read `_index.md` before creating new files to get the NEXT_ID, then increment it.

## Common Operations

### Create New Issue
1. Read `issues/_index.md` to get NEXT_ID
2. Create `issues/i-{NEXT_ID}.md` using issue template
3. Update `issues/_index.md` to increment NEXT_ID

### Update Issue Status
1. Read the issue file
2. Update Status field (valid values: backlog, todo, in_progress, in_review, done, blocked)
3. Update the `Updated` timestamp

### Create Coding Task
1. Read `issues/i-X.md` to understand requirements
2. Check `Target Repo` field for where code goes
3. Read `skills/coding/` for project conventions
4. Create `tasks/t-{NEXT_ID}.md` with full context
5. Update `tasks/_index.md` to increment NEXT_ID

## Critical Rules

1. **Never delete files** - Mark as archived/cancelled instead
2. **Never modify IDs** - IDs are permanent once created
3. **Always update timestamps** - Update `Updated` field on every change
4. **Check target repo** - Issues specify which repository receives code changes
5. **Use skills** - Read `skills/coding/` before any coding task
6. **Maintain bidirectional links** - If issue links to task, task must link back

## File Format

All entity files use a Meta table at the top:

```markdown
## Meta
| Field | Value |
|-------|-------|
| ID | i-001 |
| Status | todo |
| Created | 2026-01-30 |
| Updated | 2026-01-30 |
```

## Status Values

| Entity | Valid Statuses |
|--------|---------------|
| Issue | backlog, todo, in_progress, in_review, done, blocked |
| Task | pending, queued, running, completed, failed, cancelled |
| Sprint | planning, active, completed |
| Epic | draft, active, completed |
| Milestone | planned, in_progress, completed, missed |

## View Generation

This repository uses a view system where the AI provides JSON data and the frontend renders it. When asked to show kanban boards, lists, or other views:
1. Read relevant files (sprint, issue lists)
2. Parse and structure the data
3. Generate JSON matching the view schema

The AI does not render views directly - it provides structured data.

## For More Details

See [README.md](README.md) for comprehensive workflow examples and detailed navigation instructions.