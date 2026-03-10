# CLAUDE.md - AI Agent Guide

This file provides essential information for AI coding agents working in this repository.

## Project Overview

This is a **markdown-based test-planning project management system**. All project data—issues, tasks, sprints, epics, and milestones—is stored as markdown files. This repository serves as the planning/coordination layer; actual code implementations live in separate target repositories referenced by issues.

## Directory Structure

```
/                          ← Root of planning repository
├── README.md              ← Game-style navigation guide (for humans)
├── project.md             ← Project overview with linked code repositories
├── team.md                ← Team members with roles and capacity
├── CLAUDE.md              ← AI agent guide (this file)
│
├── issues/                ← Individual work items
│   ├── _index.md          ← NEXT_ID counter + issue list
│   └── i-XXX.md           ← One file per issue
│
├── tasks/                 ← AI coding tasks (submitted to target repos)
│   ├── _index.md          ← NEXT_ID counter + task list
│   └── t-XXX.md           ← One file per task
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
├── milestones/            ← Long-term release targets
│   ├── _index.md
│   └── m-XXX.md
│
└── skills/                ← Instructions for AI agents
    ├── coding/
    │   ├── conventions.md ← Coding standards and patterns
    │   └── testing.md     ← Testing requirements
    └── views/             ← View rendering guidelines
```

## How to Work With This Repo

### Before Making Changes
1. **Read existing files first** - Understand current state before modifying
2. **Check _index.md files** - These contain the `NEXT_ID` counter for creating new entities

### Creating New Files
1. Read the appropriate `_index.md` to get `NEXT_ID`
2. Create the new file with format `x-NNN.md` (e.g., `i-013.md`, `t-002.md`)
3. Update `_index.md` to increment `NEXT_ID`
4. Always include the Meta table with ID, Status, Created, Updated fields

### Bidirectional Linking
When you create or modify links:
- If an issue links to a task → the task must link back to the issue
- If an issue is assigned to a sprint → the sprint must list the issue
- Maintain these relationships manually

### For Coding Tasks
Before implementing any coding task:
1. Read `skills/coding/conventions.md` for project coding standards
2. Read `skills/coding/testing.md` for testing requirements
3. Check the issue's `Target Repo` field to know where code should go

## Key Constraints

1. **Never modify or delete existing IDs** - IDs are permanent identifiers
2. **Always update the 'Updated' timestamp** - Modify the `Updated` field in the Meta table whenever you change any file
3. **Maintain bidirectional links** - Related entities must reference each other
4. **Never delete files** - Instead of deleting, archive by changing Status to cancelled/archived
5. **Check target repositories** - Issues specify which repo code should be written to via the `Target Repo` field

## File Format Reference

### Meta Table (every entity file)
```markdown
## Meta
| Field | Value |
|-------|-------|
| ID | i-002 |
| Status | in_progress |
| Created | 2026-01-30 |
| Updated | 2026-02-09 |
```

### Status Values

| Entity | Valid Statuses |
|--------|---------------|
| Issue | backlog, todo, in_progress, in_review, done, blocked |
| Task | pending, queued, running, completed, failed, cancelled |
| Sprint | planning, active, completed |
| Epic | draft, active, completed |
| Milestone | planned, in_progress, completed, missed |

## Quick Reference

- **Find current sprint**: Read `sprints/current.md`
- **Create new issue**: Read `issues/_index.md`, create `issues/i-{NEXT_ID}.md`, update index
- **Move issue to done**: Update issue Status + Updated timestamp, also update sprint file
- **Run a coding task**: Read issue → Read `skills/coding/` → Create task → Submit to queue