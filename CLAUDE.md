# CLAUDE.md - AI Assistant Guide

This is a **test-planning** repository that manages all project data as markdown files. You can read, write, and search this repository to manage issues, sprints, epics, and milestones.

## Repository Purpose

This repository serves as a planning/management workspace where:
- All project management data lives in markdown files
- Issues, tasks, sprints, epics, and milestones are tracked as individual files
- Code changes are implemented via tasks that target external repositories

## Directory Structure

```
/                           # Repository root
├── CLAUDE.md               # This file
├── README.md               # Human-readable navigation guide
├── project.md              # Project overview, linked repos
├── team.md                 # Team members
│
├── milestones/             # Long-term release targets
│   ├── _index.md           # NEXT_ID counter
│   └── m-XXX.md            # Individual milestones
│
├── epics/                  # Large features spanning sprints
│   ├── _index.md           # NEXT_ID counter
│   └── e-XXX.md            # Individual epics
│
├── sprints/                # Time-boxed work periods
│   ├── _index.md           # NEXT_ID counter
│   ├── current.md          # Points to active sprint
│   └── s-XXX.md            # Individual sprints
│
├── issues/                 # Individual work items
│   ├── _index.md           # NEXT_ID counter
│   └── i-XXX.md            # One file per issue
│
├── tasks/                  # AI coding tasks
│   ├── _index.md           # NEXT_ID counter
│   └── t-XXX.md            # One file per task
│
└── skills/                 # Instructions for AI assistants
    ├── coding/             # Code conventions and patterns
    └── views/              # View styling preferences
```

## Common Workflows

### View Current Sprint
1. Read `sprints/current.md` to get active sprint ID
2. Read `sprints/s-{id}.md` for full sprint details

### Create a New Issue
1. Read `issues/_index.md` to get NEXT_ID
2. Create `issues/i-{NEXT_ID}.md` using the issue template
3. Update `issues/_index.md` to increment NEXT_ID
4. Link to relevant epic/sprint if specified

### Move Issue to Done
1. Read issue file `issues/i-X.md`
2. Update Status field to `done`
3. Update `Updated` timestamp
4. Update sprint file: move issue to `done` list

### Implement Issue (Coding Task)
1. Read issue file thoroughly
2. Note the `Target Repo` field
3. Read `skills/coding/` for project conventions
4. Create `tasks/t-{NEXT_ID}.md` with full context
5. Update `tasks/_index.md` to increment NEXT_ID
6. Submit task to coding queue

## File Format Rules

### Meta Table (Required on Every File)
```markdown
## Meta
| Field | Value |
|-------|-------|
| ID | x-001 |
| Status | active |
| Created | 2026-01-29 |
| Updated | 2026-01-29 |
```

### ID Conventions
- Milestones: `m-XXX` (e.g., m-001)
- Epics: `e-XXX` (e.g., e-001)
- Sprints: `s-XXX` (e.g., s-001)
- Issues: `i-XXX` (e.g., i-001)
- Tasks: `t-XXX` (e.g., t-001)

### Bidirectional Linking
- Issue → Task: Task must link back to issue
- Issue → Sprint: Sprint must list the issue
- Always maintain both directions of links

### Status Values

| Entity | Valid Statuses |
|--------|---------------|
| Issue | backlog, todo, in_progress, in_review, done, blocked |
| Task | pending, queued, running, completed, failed, cancelled |
| Sprint | planning, active, completed |
| Epic | draft, active, completed |
| Milestone | planned, in_progress, completed, missed |

## Critical Rules

1. **Never delete files** - Mark as archived/cancelled instead
2. **Never modify IDs** - IDs are permanent once assigned
3. **Always update timestamps** - Update `Updated` field on every change
4. **Check target repo** - Issues specify which repository receives code
5. **Read skills first** - Before coding tasks, read `skills/coding/`
6. **Confirm destructive actions** - Ask before bulk changes
7. **Use git commits** - All changes should be committed with clear messages

## Quick Reference

- **Current sprint**: Read `sprints/current.md`
- **Next issue ID**: Read `issues/_index.md`
- **Next task ID**: Read `tasks/_index.md`
- **Coding conventions**: Read `skills/coding/conventions.md`
- **Testing guidelines**: Read `skills/coding/testing.md`