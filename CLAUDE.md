# CLAUDE.md — AI/LLM Guide

This guide helps AI assistants understand this test-planning repository.

## Project Purpose

This is a **markdown-based project management system** for planning and tracking software development work. All project data lives in markdown files—there's no database. The system tracks milestones, epics, sprints, issues, and coding tasks.

## Repository Structure

```
/workspace/repo/
├── README.md           # Detailed navigation guide (always read first)
├── project.md          # Project overview, linked code repositories
├── team.md             # Team members for @mentions
│
├── milestones/         # Long-term release targets (v1.0, v2.0)
│   ├── _index.md       # NEXT_ID counter
│   └── m-XXX.md        # Individual milestone files
│
├── epics/              # Large features spanning multiple sprints
│   ├── _index.md       # NEXT_ID counter
│   └── e-XXX.md        # Individual epic files
│
├── sprints/            # Time-boxed work periods
│   ├── _index.md       # NEXT_ID counter
│   ├── current.md      # Points to active sprint
│   └── s-XXX.md        # Individual sprint files
│
├── issues/             # Individual work items
│   ├── _index.md       # NEXT_ID counter
│   └── i-XXX.md        # One file per issue
│
├── tasks/              # AI coding tasks
│   ├── _index.md       # NEXT_ID counter
│   └── t-XXX.md        # One file per task
│
└── skills/             # Instructions for AI assistants
    └── coding/         # Coding conventions and patterns
```

## Key Workflows

### Creating Issues
1. Read `issues/_index.md` to get `NEXT_ID`
2. Create `issues/i-{NEXT_ID}.md` using the issue template
3. Update `issues/_index.md` to increment NEXT_ID
4. Link to sprint/epic if specified

### Updating Status
1. Read the entity file (issue, task, etc.)
2. Update the Status field in the Meta table
3. Update the `Updated` timestamp
4. Update parent relationships (sprint lists, epic lists)

### Running Coding Tasks
1. Read `issues/i-X.md` to understand requirements
2. Note the `Target Repo` field—this is where code goes
3. Read `skills/coding/conventions.md` for project patterns
4. Create `tasks/t-{NEXT_ID}.md` with full context
5. Submit to coding queue and track results

## Important Files and Conventions

### Meta Tables
Every entity file has a Meta table at the top:
```markdown
## Meta
| Field | Value |
|-------|-------|
| ID | i-002 |
| Status | in_progress |
| Created | 2026-01-30 |
| Updated | 2026-03-13 |
```

### ID Format
- Milestones: `m-XXX` (e.g., m-001, m-002)
- Epics: `e-XXX`
- Sprints: `s-XXX`
- Issues: `i-XXX`
- Tasks: `t-XXX`

Always read `_index.md` files to get the current NEXT_ID before creating new entities.

### _index.md Files
Each directory has an `_index.md` containing:
- NEXT_ID counter (always increment after creating)
- List of all entities in that directory

### Status Values
| Entity | Valid Statuses |
|--------|---------------|
| Issue | backlog, todo, in_progress, in_review, done, blocked |
| Task | pending, queued, running, completed, failed, cancelled |
| Sprint | planning, active, completed |
| Epic | draft, active, completed |
| Milestone | planned, in_progress, completed, missed |

## Constraints

1. **Never delete files** — Mark as archived/cancelled instead
2. **Never modify IDs** — IDs are permanent identifiers
3. **Always update timestamps** — Update `Updated` field on every change
4. **Maintain bidirectional links** — If A links to B, B should link back
5. **Check target repo** — Issues specify which repository receives code changes

## Additional Resources

For more detailed information, see:
- [README.md](README.md) — Comprehensive navigation guide with quest patterns
- [project.md](project.md) — Project overview and linked repositories
- [skills/coding/conventions.md](skills/coding/conventions.md) — Coding standards