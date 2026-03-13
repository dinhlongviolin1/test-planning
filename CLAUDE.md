# CLAUDE.md - Agent Guidance for test-planning

## Repository Purpose

This is a **markdown-based project management repository**. All project data (issues, tasks, epics, milestones, sprints) is stored as markdown files with Meta tables. Agents read/write these files to manage the project.

## Key Files

| File | Purpose |
|------|---------|
| `README.md` | Agent navigation guide (game-style tutorial with world map, quests, file format rules) |
| `project.md` | Project overview with status, goals, linked code repositories |
| `team.md` | Team members list with usernames, names, roles, capacity per sprint |
| `skills/coding/conventions.md` | Coding conventions and practices for implementation tasks |
| `scripts/get_team_members.py` | Python utility to retrieve team member data |
| `scripts/list_users.py` | Python utility to list users |

## Directory Structure

```
/                      ← Root
├── README.md          ← Navigation guide (start here)
├── project.md         ← Project overview
├── team.md            ← Team members
├── milestones/        ← Long-term release targets (m-XXX.md)
├── epics/             ← Large features (e-XXX.md)
├── sprints/           ← Time-boxed work periods (s-XXX.md, current.md)
├── issues/            ← Individual work items (i-XXX.md)
├── tasks/             ← AI coding tasks (t-XXX.md)
├── scripts/           ← Python utilities
└── skills/            ← Agent instructions (coding/, views/)
```

## Naming Conventions

| Entity | Pattern | Example |
|--------|---------|---------|
| Issues | `i-XXX` | `i-001`, `i-002` |
| Tasks | `t-XXX` | `t-001` |
| Epics | `e-XXX` | `e-001` |
| Milestones | `m-XXX` | `m-001` |
| Sprints | `s-XXX` | `s-001` |

## File Format Rules

- **Meta tables**: Every file has a `## Meta` section with ID, Status, Updated fields
- **IDs are sequential**: Check `_index.md` for the next available ID before creating new files
- **Timestamps**: Always update the `Updated` field when modifying any file
- **Bidirectional links**: If an issue links to a task, the task should link back to the issue

## Status Values

| Entity | Valid Statuses |
|--------|---------------|
| Issue | `backlog`, `todo`, `in_progress`, `in_review`, `done`, `blocked` |
| Task | `pending`, `queued`, `running`, `completed`, `failed`, `cancelled` |
| Sprint | `planning`, `active`, `completed` |
| Epic | `draft`, `active`, `completed` |
| Milestone | `planned`, `in_progress`, `completed`, `missed` |

## Common Workflows

- **View current sprint**: Read `sprints/current.md` → read the referenced sprint file
- **Create issue**: Read `issues/_index.md` for next ID → create file → update `_index.md`
- **Create task**: Read `tasks/_index.md` for next ID → create file → link to issue

## Important Notes

- Read `README.md` for detailed navigation guide with quest examples
- Check `skills/coding/conventions.md` before implementing coding tasks
- Team members are defined in `team.md` for @mentions
- Never delete files — mark as archived/cancelled instead