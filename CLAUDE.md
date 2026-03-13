# CLAUDE.md - Quick Reference for Claude Code

A markdown-based project management repo where issues, tasks, sprints, epics, and milestones are stored as individual .md files.

See `README.md` for complete details.

---

## Key Files & Directories

| Path | Purpose |
|------|---------|
| `project.md` | Project overview |
| `team.md` | Team members |
| `README.md` | Full reference guide |
| `issues/` | Individual work items (i-001.md, i-002.md, ...) |
| `tasks/` | AI coding tasks (t-001.md, ...) |
| `sprints/` | Time-boxed work periods (s-001.md, ...) + `current.md` pointer |
| `epics/` | Large features (e-001.md, ...) |
| `milestones/` | Release targets (m-001.md, ...) |
| `skills/` | Project conventions |

Each directory has `_index.md` with a NEXT_ID counter and entity list.

---

## ID Conventions

- Format: `i-001`, `t-001`, `s-001`, `e-001`, `m-001`
- Always read `_index.md` to get NEXT_ID before creating a new entity
- Increment NEXT_ID in `_index.md` after creating
- Never modify existing IDs

---

## Status Values

| Type | Valid Statuses |
|------|---------------|
| Issue | `backlog`, `todo`, `in_progress`, `in_review`, `done`, `blocked` |
| Task | `pending`, `queued`, `running`, `completed`, `failed`, `cancelled` |
| Sprint | `planning`, `active`, `completed` |
| Epic | `draft`, `active`, `completed` |
| Milestone | `planned`, `in_progress`, `completed`, `missed` |

---

## Key Rules

- Never delete files — mark as `archived` or `cancelled` instead
- Always update the `Updated` timestamp on every change
- Links are bidirectional: if an issue links to a task, the task must link back
- Read `skills/coding/` before implementing coding tasks

---

## Common Actions

**Read issues:** Read files in `issues/`

**Create issue:**
1. Read `issues/_index.md` for NEXT_ID
2. Create `issues/i-{ID}.md`
3. Increment NEXT_ID in `issues/_index.md`

**Update issue status:**
1. Edit `Status` field in the issue file
2. Update `Updated` timestamp
3. If the issue is in a sprint, update the sprint file too

**Find active sprint:**
1. Read `sprints/current.md` for the sprint ID
2. Read `sprints/s-{id}.md`
