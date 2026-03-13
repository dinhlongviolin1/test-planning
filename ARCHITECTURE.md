# Architecture Guide

This document explains how this markdown-based project management system works.

## What Is This Repository?

This is a **test-planning repository** for managing software development projects. Instead of using a database or project management tool like Jira, all data is stored as markdown files. Each entity (issue, task, sprint, etc.) is a separate file with a consistent structure.

The system is designed to be:
- **Human-readable** — Plain markdown that anyone can edit
- **AI-friendly** — Structured data that AI assistants can parse and manipulate
- **Version-controlled** — All changes tracked in git with history

## Directory Structure

| Directory | Purpose |
|-----------|---------|
| `milestones/` | Long-term release targets (e.g., v1.0, v2.0) |
| `epics/` | Large features spanning multiple sprints |
| `sprints/` | Time-boxed work periods (typically 2 weeks) |
| `issues/` | Individual work items and user stories |
| `tasks/` | AI coding tasks for automated implementation |
| `skills/` | Instructions and conventions for AI assistants |

## Entity Relationships

```
Milestone (v1.0)
    │
    └── Epic (Authentication)
            │
            ├── Issue (Implement OAuth)
            │       │
            │       └── Task (coding task) → PR in target repo
            │
            └── Issue (Add MFA)
```

- **Milestones** contain multiple **epics**
- **Epics** contain multiple **issues**
- **Issues** may spawn **tasks** (coding work)
- **Sprints** group **issues** for a specific time period

## ID Conventions

Each entity type uses a specific ID prefix and sequential numbering:

| Type | Prefix | Example |
|------|--------|---------|
| Milestone | m- | m-001, m-002 |
| Epic | e- | e-001, e-002 |
| Sprint | s- | s-001, s-002 |
| Issue | i- | i-001, i-002 |
| Task | t- | t-001, t-002 |

Before creating a new entity, always check the `_index.md` file in that directory to get the current NEXT_ID, then increment it after creation.

## File Naming

- Index files: `_index.md` — contains directory overview and next ID
- Entity files: `{id}.md` — one file per entity (e.g., `i-001.md`)

## Status Values

| Entity Type | Valid Statuses |
|-------------|----------------|
| Milestone | planned, in_progress, completed, missed |
| Epic | draft, active, completed |
| Sprint | planning, active, completed |
| Issue | backlog, todo, in_progress, in_review, done, blocked |
| Task | pending, queued, running, completed, failed, cancelled |

## Common Workflows

### Creating a New Issue
1. Read `issues/_index.md` to get the next ID
2. Create `issues/i-{id}.md` following the Meta table format
3. Update `issues/_index.md` to increment NEXT_ID
4. Optionally link to a sprint and/or epic

### Moving an Issue to Done
1. Open the issue file and change Status to `done`
2. Update the `Updated` timestamp
3. Update the parent sprint file to move the issue to the done list

### Running a Coding Task
1. Identify the issue to implement
2. Note the Target Repo from the issue
3. Create a task file with full context
4. Submit to the coding queue

## Key Files

- `README.md` — Detailed navigation guide with step-by-step quests
- `project.md` — Project overview and linked code repositories
- `team.md` — Team member directory

For more details, see [README.md](README.md).