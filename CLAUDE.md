# CLAUDE.md — LLM Onboarding Guide

Welcome! This document provides everything you need to understand and navigate this repository as an AI assistant.

## Repository Purpose

This is a **test-planning management system** that stores all project management data as markdown files. The repository serves as the central planning hub for organizing work across milestones, epics, sprints, issues, and tasks.

## Directory Structure

```
/                           ← Repository root
├── CLAUDE.md              ← You are here
├── ARCHITECTURE.md        ← Architecture documentation
├── README.md              ← Human-facing navigation guide
├── project.md             ← Project overview and linked repos
├── team.md                ← Team members for @mentions
│
├── milestones/            ← Long-term release targets
│   ├── _index.md          ← Overview + NEXT_ID counter
│   └── m-XXX.md           ← Individual milestones
│
├── epics/                 ← Large features spanning multiple sprints
│   ├── _index.md
│   └── e-XXX.md
│
├── sprints/               ← Time-boxed work periods
│   ├── _index.md
│   ├── current.md         ← Points to active sprint
│   └── s-XXX.md
│
├── issues/                ← Individual work items
│   ├── _index.md          ← Overview + NEXT_ID counter
│   └── i-XXX.md           ← One file per issue (self-contained)
│
├── tasks/                 ← AI coding tasks
│   ├── _index.md          ← Overview + NEXT_ID counter
│   └── t-XXX.md           ← One file per task
│
└── skills/                ← Instructions for AI assistants
    ├── coding/            ← Code conventions and patterns
    │   ├── _index.md
    │   ├── conventions.md
    │   └── testing.md
    └── views/             ← View generation guidelines
```

## ID Conventions

All IDs follow sequential numbering with prefix:

| Entity | Prefix | Example |
|--------|--------|---------|
| Milestone | m- | m-001, m-002 |
| Epic | e- | e-001, e-002 |
| Sprint | s- | s-001, s-002 |
| Issue | i- | i-001, i-002 |
| Task | t- | t-001, t-002 |

**IMPORTANT**: Never modify existing IDs. They are permanent identifiers.

## File Format Rules

### Every Entity File Has a Meta Table

```markdown
# Meta
| Field | Value |
|-------|-------|
| ID | x-001 |
| Status | active |
| Created | 2026-01-30 |
| Updated | 2026-01-30 |
```

- Always preserve existing IDs
- Always update `Updated` timestamp when modifying any field
- Use the date format `YYYY-MM-DD`

### ID Allocation

1. Read `_index.md` for the entity type to get `NEXT_ID`
2. Create the new file with the next available ID
3. Update `_index.md` to increment `NEXT_ID`

### Bidirectional Links

When creating or modifying links:
- If an issue links to a task → task must link back to issue
- If an issue is assigned to a sprint → sprint must list the issue
- If an issue belongs to an epic → epic must list the issue

### Status Values by Entity

| Entity | Valid Statuses |
|--------|---------------|
| Issue | backlog, todo, in_progress, in_review, done, blocked |
| Task | pending, queued, running, completed, failed, cancelled |
| Sprint | planning, active, completed |
| Epic | draft, active, completed |
| Milestone | planned, in_progress, completed, missed |

## Common Workflows

### Show Current Sprint
1. Read `sprints/current.md` to get active sprint ID
2. Read `sprints/s-{id}.md` for full sprint details

### Create a New Issue
1. Read `issues/_index.md` to get NEXT_ID
2. Create `issues/i-{NEXT_ID}.md` using issue format
3. Update `issues/_index.md` to increment NEXT_ID
4. If sprint specified, add issue to sprint file
5. If epic specified, add issue to epic file

### Move Issue to Done
1. Read `issues/i-X.md`
2. Update Status field to `done`
3. Update `updated` timestamp
4. Read `sprints/current.md` or relevant sprint file
5. Move issue from status list to `Done` list

### Implement Issue (Coding Task)
1. Read `issues/i-X.md` thoroughly
2. Note the `Target Repo` field - that's where code goes
3. Read `skills/coding/conventions.md` for project conventions
4. Search web for technical guidance if needed
5. Create `tasks/t-{NEXT_ID}.md` with full context
6. Update `tasks/_index.md` to increment NEXT_ID
7. Update issue file to link the task
8. Submit task to coding queue

## Critical Rules

1. **Never delete files** - Mark as archived/cancelled instead
2. **Never modify IDs** - IDs are permanent once created
3. **Always update timestamps** - `Updated` field on every change
4. **Check target repo** - Issues specify which repo code goes to
5. **Read skills first** - Before coding tasks, read `skills/coding/`
6. **Confirm destructive actions** - Ask before bulk changes
7. **Commit often** - Each change should be a git commit

## Reading Order

When starting work on this repository:

1. Read `CLAUDE.md` (this file) — you are here
2. Read `ARCHITECTURE.md` for system design overview
3. Read relevant `_index.md` files for entity overview
4. Read specific entity files as needed
5. Check `skills/` for AI assistant instructions