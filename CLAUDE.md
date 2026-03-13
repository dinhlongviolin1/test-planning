# CLAUDE.md — AI Assistant Onboarding Guide

Welcome! This document is your primary reference for working in this test-planning repository.

## Repository Purpose

This is a **test-planning management** repository where all project data is stored as markdown files. Each file represents an entity in the project hierarchy:

- **Milestones** — Long-term release targets (quarterly goals)
- **Epics** — Large features spanning multiple sprints
- **Sprints** — Time-boxed work periods (typically 2 weeks)
- **Issues** — Individual work items and user stories
- **Tasks** — AI coding tasks that generate code in target repositories

You can read any file to understand project state and write to files to make changes. Code changes go to target repositories via coding tasks.

---

## Directory Structure

```
/                      ← Repository root
├── README.md          ← Project overview and navigation guide
├── project.md         ← Project metadata, linked code repos
├── team.md            ← Team members for @mentions
├── CLAUDE.md          ← You are here (AI onboarding)
│
├── milestones/        ← Long-term release targets
│   ├── _index.md      ← Overview + list of all milestones
│   └── m-XXX.md       ← Individual milestone files
│
├── epics/             ← Large features (span multiple sprints)
│   ├── _index.md      ← Overview + list of all epics
│   └── e-XXX.md       ← Individual epic files
│
├── sprints/           ← Time-boxed work periods
│   ├── _index.md      ← Overview + list of all sprints
│   ├── current.md     ← Pointer to active sprint
│   └── s-XXX.md       ← Individual sprint files
│
├── issues/            ← Individual work items
│   ├── _index.md      ← Overview + NEXT_ID counter (important!)
│   └── i-XXX.md       ← Individual issue files (self-contained)
│
├── tasks/             ← AI coding tasks
│   ├── _index.md      ← Overview + NEXT_ID counter (important!)
│   └── t-XXX.md       ← Individual task files
│
└── skills/            ← Instructions for AI agents
    ├── coding/        ← Code style, testing conventions
    │   ├── _index.md
    │   ├── conventions.md
    │   └── testing.md
    └── views/         ← View styling preferences
```

---

## Common Workflows

### Viewing Current Sprint

1. Read `sprints/current.md` to get the active sprint ID
2. Read `sprints/s-{id}.md` for full sprint details
3. The sprint file lists issues by status: Todo, In Progress, In Review, Done

### Creating a New Issue

1. Read `issues/_index.md` to get the current `NEXT_ID`
2. Create `issues/i-{NEXT_ID}.md` using the issue template below
3. Update `issues/_index.md` to increment `NEXT_ID`
4. If assigning to a sprint, update the sprint file's issue list
5. If linking to an epic, update the epic file's issue list

**Issue Template:**
```markdown
# Meta
| Field | Value |
|-------|-------|
| ID | i-XXX |
| Status | backlog |
| Created | YYYY-MM-DD |
| Updated | YYYY-MM-DD |

## Title
[Issue title]

## Description
[Description of the work item]

## Linked Epics
- [e-XXX](e-XXX.md) - Epic title

## Linked Sprint
- [s-XXX](s-XXX.md) - Sprint title

## Target Repo
[owner/repo-name]

## Tasks
- [ ] Task 1
- [ ] Task 2

## Notes
[Any additional notes]
```

### Moving an Issue to Done

1. Read the issue file `issues/i-{id}.md`
2. Update the Status field to `done`
3. Update the `updated` timestamp to today's date (YYYY-MM-DD)
4. Read the sprint file and move the issue from its current status list to the "Done" list

### Implementing a Coding Task (from an Issue)

1. Read `issues/i-{id}.md` thoroughly
2. Note the `Target Repo` field — that's where the code goes
3. Read `skills/coding/conventions.md` and `skills/coding/testing.md` for project rules
4. Create `tasks/t-{NEXT_ID}.md` with full context from the issue
5. Update `tasks/_index.md` to increment NEXT_ID
6. Update the issue file to link the task
7. Execute the coding task (spawn coding agent or similar)
8. Wait for results and update task file with outcome

### Quick Coding Task (no issue)

1. Read `skills/coding/` for conventions
2. Create `tasks/t-{NEXT_ID}.md` with `Issue` field as `-`
3. Proceed with coding task execution

---

## File Format Rules

### Meta Tables

Every entity file (issues, tasks, sprints, epics, milestones) has a Meta table at the top:

```markdown
## Meta
| Field | Value |
|-------|-------|
| ID | x-001 |
| Status | active |
| Created | 2026-01-30 |
| Updated | 2026-01-30 |
```

**Always:**
- Preserve existing IDs — never change them
- Update the `Updated` timestamp whenever you modify a file

### ID Conventions

- IDs are **sequential** and **permanent**
- Before creating a new entity, read the `_index.md` file to get the current `NEXT_ID`
- After creating, increment `NEXT_ID` in `_index.md`
- ID format: `{type}-{number}` (e.g., `i-001`, `s-002`, `t-003`)

### Bidirectional Links

Always maintain reciprocal links:
- If an issue links to a task → the task must link back to the issue
- If an issue is in a sprint → the sprint must list the issue
- If an issue belongs to an epic → the epic must list the issue

### Status Values

| Entity | Valid Statuses |
|--------|---------------|
| Issue | `backlog`, `todo`, `in_progress`, `in_review`, `done`, `blocked` |
| Task | `pending`, `queued`, `running`, `completed`, `failed`, `cancelled` |
| Sprint | `planning`, `active`, `completed` |
| Epic | `draft`, `active`, `completed` |
| Milestone | `planned`, `in_progress`, `completed`, `missed` |

---

## Critical Rules and Constraints

1. **Never delete files** — Mark as `cancelled` or `archived` instead of deleting
2. **Never modify IDs** — IDs are permanent identifiers; changing them breaks references
3. **Always update timestamps** — Set `Updated` to today's date (YYYY-MM-DD) on every change
4. **Check target repo field** — Issues specify which repository code should be written to
5. **Read skills first** — Before any coding task, load `skills/coding/conventions.md` and `skills/coding/testing.md`
6. **Confirm destructive actions** — Ask the user before bulk changes or file modifications
7. **Commit all changes** — Each change should be a git commit with a clear message

---

## Entity Hierarchy

```
Milestone (e.g., Q1 2026 Release)
    │
    └── Epic (e.g., Core Platform Enhancements)
            │
            ├── Issue (e.g., Implement authentication API)
            │       │
            │       └── Task (AI coding task) ──→ PR (in target repo)
            │
            └── Issue (e.g., Add MFA support)
                    │
                    └── Task ──→ PR
```

---

## Tips for Success

- **Start by reading** — Always read relevant files before making changes
- **Be conservative** — When unsure, ask the user for clarification
- **Link everything** — Cross-references help navigate the project
- **Use the skills** — Project-specific instructions are in `skills/coding/`
- **Generate structured data** — When users ask for views (kanban, list, etc.), read the relevant files and generate JSON data; the frontend handles rendering