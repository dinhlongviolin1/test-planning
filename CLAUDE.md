# CLAUDE.md — Agent Orientation

This is a **project management/planning repository** that uses markdown files. There is no source code here — code lives in target repositories referenced from issues.

See `README.md` (titled "Agent Navigation Guide") for full operational details.

## Repository Structure

```
/
├── issues/        — Individual work items (i-001, i-002, …)
├── tasks/         — AI coding tasks submitted to the coding queue (t-001, t-002, …)
├── epics/         — Large features spanning multiple sprints (e-001, …)
├── milestones/    — Long-term release targets (m-001, …)
├── sprints/       — Time-boxed work periods (s-001, …); current.md → active sprint
├── skills/        — Project-specific conventions; read before submitting coding tasks
├── project.md     — Project metadata (currently sparse/placeholder)
└── team.md        — Team members for @mentions
```

Each directory (except `skills/`) contains an `_index.md` with a NEXT_ID counter.

## Workflow

**Milestone → Epic → Issue → Task → PR**

Issues specify a Target Repo where code changes go. Tasks are the AI coding work items. When implementing an issue, create a task file in `tasks/`, link it back to the issue, and submit it to the coding queue.

## ID System

All entities have sequential IDs (i-001, t-001, e-001, m-001, s-001). Before creating any new entity:
1. Read the relevant `_index.md` to get NEXT_ID
2. Create the file using that ID
3. Increment NEXT_ID in `_index.md`

## Critical Rules

- **Never delete files** — mark status as `archived` or `cancelled` instead
- **Never modify IDs** — they are permanent
- **Always update `Updated` timestamp** when modifying any file
- **Read `skills/`** before submitting coding tasks
- **Links are bidirectional** — if an issue links a task, the task must link back to the issue
