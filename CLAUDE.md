# CLAUDE.md — Claude Code Guide for test-planning

## Project Purpose

This is the **test-planning** repository — a planning and project-management repository where AI agents read and write markdown files to manage sprints, issues, tasks, epics, and milestones.

**Important:** This repo contains only planning data. Code changes go to *target* repositories, which are referenced in the `Target Repo` field of each issue file. Do not write code directly into this repository.

## Directory Structure

```
/
├── README.md          — Agent navigation guide (game tutorial style); read this first
├── project.md         — Project overview and linked code repositories
├── team.md            — Team members (for @mentions)
│
├── milestones/        — Long-term release targets
│   └── m-XXX.md       — Individual milestone files
│
├── epics/             — Large features spanning multiple sprints
│   └── e-XXX.md       — Individual epic files
│
├── sprints/           — Time-boxed work periods
│   ├── current.md     — Symlink pointing to the active sprint
│   └── s-XXX.md       — Individual sprint files
│
├── issues/            — Individual work items
│   ├── _index.md      — NEXT_ID counter; read before creating a new issue
│   └── i-XXX.md       — One file per issue (self-contained)
│
├── tasks/             — AI coding tasks
│   ├── _index.md      — NEXT_ID counter; read before creating a new task
│   └── t-XXX.md       — One file per task
│
└── skills/            — Instructions for AI agents
    ├── coding/        — Coding conventions for target repositories
    └── views/         — How to style and generate views
```

## Key Conventions

- **Meta table**: Every file has a `## Meta` section with a markdown table containing at minimum `ID`, `Status`, `Created`, and `Updated` fields.
- **IDs are permanent**: IDs are sequential and must never be modified. They are assigned at creation time.
- **Read `_index.md` first**: Before creating any new issue or task, read the relevant `_index.md` to get the correct `NEXT_ID`. After creating the file, increment `NEXT_ID` in `_index.md`.
- **Bidirectional links**: If an issue links to a task, the task must link back to the issue. If an issue belongs to a sprint, the sprint must list the issue.
- **Always update timestamps**: When modifying any file, update its `Updated` field to today's date (`YYYY-MM-DD`).
- **Never delete files**: Mark files as `done`, `cancelled`, or `archived` instead of deleting them.
- **Target Repo**: Each issue has a `Target Repo` field specifying which repository receives the code changes. Always read this before spawning a coding task.

## Status Values

| Entity    | Valid Statuses                                          |
|-----------|---------------------------------------------------------|
| Issue     | `backlog`, `todo`, `in_progress`, `in_review`, `done`, `blocked` |
| Task      | `pending`, `queued`, `running`, `completed`, `failed`, `cancelled` |
| Sprint    | `planning`, `active`, `completed`                       |
| Epic      | `draft`, `active`, `completed`                          |
| Milestone | `planned`, `in_progress`, `completed`, `missed`         |

## Workflow Tips

- **Read `README.md` first** — it is the primary navigation guide with common quest patterns (creating issues, moving issues to done, implementing coding tasks, etc.).
- **Read `skills/coding/`** before starting any coding task to understand project conventions for the target repository.
- **Find the current sprint**: read `sprints/current.md` to get the active sprint ID, then read the corresponding `sprints/s-XXX.md`.
- **Before creating any entity**: read the relevant `_index.md` to get the correct `NEXT_ID`, create the file, then increment `NEXT_ID`.
- **Commit every change** — each meaningful change is a git commit with a clear conventional commit message.
