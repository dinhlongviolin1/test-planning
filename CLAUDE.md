# CLAUDE.md — AI Agent Onboarding Guide

Welcome, AI Agent! This file serves as your main reference for working on this project. Read it thoroughly before making any changes.

## Project Purpose

This is a **markdown-based project management system** where all project data lives in markdown files rather than a database or traditional project management tool.

- **What lives here**: Issues, epics, sprints, milestones, tasks, and team information
- **Code changes**: Go to target repositories via coding tasks (you spawn AI coders)
- **Your role**: Read/write markdown files, spawn coding agents, manage project state

## Directory Structure

```
/                           # Root of planning repo
├── README.md               # Navigation guide for agents
├── project.md              # Project overview and linked repos
├── team.md                 # Team members for @mentions
├── CLAUDE.md               # AI Agent onboarding guide (you are here)
│
├── milestones/             # Long-term release targets
│   ├── _index.md           # Overview + how to use
│   └── m-XXX.md            # Individual milestones
│
├── epics/                  # Large features spanning multiple sprints
│   ├── _index.md
│   └── e-XXX.md
│
├── sprints/                # Time-boxed work periods
│   ├── _index.md
│   ├── current.md          # Points to active sprint
│   └── s-XXX.md
│
├── issues/                 # Individual work items
│   ├── _index.md           # Overview + NEXT_ID COUNTER
│   └── i-XXX.md            # One file per issue (self-contained)
│
├── tasks/                  # AI coding tasks
│   ├── _index.md           # Overview + NEXT_ID COUNTER
│   └── t-XXX.md            # One file per task
│
└── skills/                 # Instructions for AI agents
    ├── _index.md
    ├── coding/             # How to write code for this project
    │   ├── conventions.md  # Code style, naming, structure
    │   └── testing.md      # Testing requirements
    └── views/              # View styling preferences
```

## Key Conventions

### Meta Tables

Every file contains a Meta table at the top:

```markdown
## Meta
| Field | Value |
|-------|-------|
| ID | x-001 |
| Status | active |
| Created | 2026-01-29 |
| Updated | 2026-01-29 |
```

- Always preserve existing IDs — never modify them
- Always update the `Updated` timestamp when modifying any file

### ID System

- IDs are sequential across each entity type (issues: i-XXX, tasks: t-XXX, etc.)
- **Before creating a new file**, read `_index.md` to get the current NEXT_ID
- Increment NEXT_ID after creating a new file
- IDs are permanent — once assigned, they never change

### Status Values

| Entity | Valid Statuses |
|--------|---------------|
| Issue | backlog, todo, in_progress, in_review, done, blocked |
| Task | pending, queued, running, completed, failed, cancelled |
| Sprint | planning, active, completed |
| Epic | draft, active, completed |
| Milestone | planned, in_progress, completed, missed |

### Bidirectional Links

- If an issue links to a task → the task must link back to the issue
- If an issue is assigned to a sprint → the sprint must list that issue
- Always maintain these cross-references when making changes

## Team Reference

Team members are defined in [team.md](team.md). Use @mentions when assigning or discussing:

- @dinhlongviolin1 — Dinh Long, Software Engineer
- @faisal — Faisal, Frontend Engineer/UI Designer
- @louis — Louis, Senior Software Engineer
- @nguyen — Nguyen, Senior Software Engineer
- @vanalite — Van Alite, Senior Software Engineer
- @bach — Bach, Researcher
- @alan — Alan, Researcher
- @alex — Alex, Researcher
- @thinhle — Thinh Le, Researcher

## Useful Patterns

### Creating a New Issue

1. Read `issues/_index.md` to get the current NEXT_ID
2. Create `issues/i-{NEXT_ID}.md` using the issue template
3. Update `issues/_index.md` to increment NEXT_ID
4. If a sprint is specified, update the sprint file's issue list
5. If an epic is specified, update the epic file's issue list

### Updating Issue Status

1. Read the issue file `issues/i-XXX.md`
2. Update the Status field in the Meta table
3. Update the `Updated` timestamp
4. Read `sprints/current.md` to find the active sprint
5. Update the sprint file: move the issue from the old status list to the new one

### Running a Coding Task

1. Read the issue file thoroughly to understand requirements
2. Note the `Target Repo` field — that's where the code goes
3. Read `skills/coding/conventions.md` and `skills/coding/testing.md`
4. Search the web for technical guidance if needed
5. Create `tasks/t-{NEXT_ID}.md` with full context from the issue
6. Update `tasks/_index.md` to increment NEXT_ID
7. Link the task in the issue file
8. Submit the task to the coding queue
9. Wait for results and update the task file with outcomes

### Quick Reference: Common Operations

| Task | How To |
|------|--------|
| Find current sprint | Read `sprints/current.md` |
| Find next available ID | Read `{entity}/_index.md` |
| Move issue to done | Edit Meta table + update sprint |
| Create coding task | Read issue → create task file → link back |
| Check coding standards | Read `skills/coding/conventions.md` |
| Check testing requirements | Read `skills/coding/testing.md` |

## Important Notes

1. **Never delete files** — Mark as `cancelled` or `archived` instead
2. **Never modify IDs** — IDs are permanent identifiers
3. **Always update timestamps** — The `Updated` field must reflect the last change
4. **Check target repo** — Issues specify which repository receives code changes
5. **Read skills before coding** — Always load `skills/coding/` before executing tasks
6. **Confirm destructive actions** — Ask the user before bulk changes

## Additional Resources

- [README.md](README.md) — Detailed navigation patterns and view generation
- [project.md](project.md) — Project overview and linked repositories
- [skills/coding/conventions.md](skills/coding/conventions.md) — Code style, naming, structure
- [skills/coding/testing.md](skills/coding/testing.md) — Testing requirements and patterns
- [skills/_index.md](skills/_index.md) — How to use skills in this project