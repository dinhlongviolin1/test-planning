# CLAUDE.md — AI Assistant Guidelines

Welcome, AI Agent! This file provides guidelines for working on this markdown-based project management system.

## Tech Stack

- **Backend**: Go 1.25 · Gin · GORM · Wire DI · PostgreSQL 18 · pgvector
- **Frontend**: React 19 · TanStack Router · Zustand v5 · Tailwind CSS 4
- **AI**: MCP tools over JSON-RPC 2.0 · Vercel AI SDK v5
- **GitHub**: GitHub App installation tokens (org-level)

## Project Structure

```
/                           ← Project root
├── README.md               ← Agent navigation guide
├── CLAUDE.md              ← You are here
├── SOUL.md                ← Project principles and values
├── project.md             ← Project overview
├── team.md                ← Team members
│
├── milestones/            ← Long-term release targets (m-XXX.md)
├── epics/                 ← Large features spanning sprints (e-XXX.md)
├── sprints/               ← Time-boxed work periods (s-XXX.md)
├── issues/                ← Individual work items (i-XXX.md)
├── tasks/                 ← AI coding tasks (t-XXX.md)
├── skills/                ← Instructions for AI assistants
├── docs/                  ← Documentation
└── uploads/               ← File uploads for OCR processing
```

## File Conventions

### Meta Tables

Every file uses a Meta table at the top:

```markdown
## Meta
| Field | Value |
|-------|-------|
| ID | x-001 |
| Status | active |
| Created | 2026-01-29 |
| Updated | 2026-04-13 |
```

### ID Formats

| Entity | Prefix | Example |
|--------|--------|---------|
| Milestone | m- | m-001 |
| Epic | e- | e-002 |
| Sprint | s- | s-001 |
| Issue | i- | i-002 |
| Task | t- | t-001 |

### Status Values

| Entity | Valid Statuses |
|--------|---------------|
| Issue | backlog, todo, in_progress, in_review, done, blocked |
| Task | pending, queued, running, completed, failed, cancelled |
| Sprint | planning, active, completed |
| Epic | draft, active, completed |
| Milestone | planned, in_progress, completed, missed |

## Working with the Project

### Creating New Entities

1. Read `_index.md` in the entity folder to get the NEXT_ID
2. Create the new file with the appropriate template
3. Update `_index.md` to increment NEXT_ID

### Bidirectional Linking

Always maintain bidirectional links:
- If an issue links to a task → the task must link back to the issue
- If an issue is in a sprint → the sprint must list the issue
- If an epic contains issues → each issue should reference the epic

### Timestamps

Always update the `Updated` timestamp when modifying any file. Use ISO format: `YYYY-MM-DD`

### Data Integrity

- **Never delete files** — Mark as archived/cancelled instead
- **Never modify IDs** — IDs are permanent
- **Always update timestamps** — The `Updated` field on every change

## Common Operations

### Show Current Sprint
1. Read `sprints/current.md` to get the active sprint ID
2. Read `sprints/s-{id}.md` for full sprint details

### Move Issue to Done
1. Read the issue file
2. Update Status to `done`
3. Update the `updated` timestamp
4. Update the sprint file to move the issue to done list

### Create a Coding Task
1. Read issue file thoroughly
2. Note the `Target Repo` field
3. Read `skills/coding/conventions.md` for coding standards
4. Create `tasks/t-{NEXT_ID}.md`
5. Update `tasks/_index.md` to increment NEXT_ID

## View Generation

When users request views (kanban, lists, etc.), you generate JSON data:
1. Read the relevant files
2. Parse the data into structured JSON
3. The frontend handles rendering — you provide data only

## Reference

- Full navigation guide: [README.md](README.md)
- Project overview: [project.md](project.md)
- Team structure: [team.md](team.md)
- Coding conventions: [skills/coding/conventions.md](skills/coding/conventions.md)
- Architecture details: [docs/architecture.md](docs/architecture.md)