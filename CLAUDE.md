# CLAUDE.md

This is the `test-planning` repository -- a markdown-based planning system that tracks issues, epics, sprints, milestones, and AI coding tasks. All data is stored as markdown files with structured meta tables.

## Repository Structure

- `epics/` -- Large features spanning multiple sprints (`e-XXX.md` files)
- `issues/` -- Individual work items (`i-XXX.md` files)
- `sprints/` -- Time-boxed work periods (`s-XXX.md` files), with `current.md` pointing to the active sprint
- `milestones/` -- Long-term release targets (`m-XXX.md` files)
- `tasks/` -- AI coding tasks (`t-XXX.md` files)
- `skills/` -- Agent instructions, including `coding/conventions.md` and `coding/testing.md`
- `scripts/` -- Utility scripts (`get_all_issues_and_epics.py`, `get_team_members.py`, `list_users.py`)
- `docs/` -- Project documentation including `architecture.md` (Go 1.25, React 19, PostgreSQL 18 stack)

## Key Conventions

### Meta Tables

Every entity file has a `## Meta` section with a markdown table:

```
## Meta
| Field | Value |
|-------|-------|
| ID    | x-001 |
| Status | active |
```

### Sequential IDs

Read `_index.md` in the entity directory for `NEXT_ID` before creating a new entity, then increment it after creation.

### Bidirectional Links

Links between entities are always bidirectional. If an issue links to an epic, the epic must list the issue, and vice versa.

### Status Values

| Entity    | Valid Statuses                                          |
|-----------|---------------------------------------------------------|
| Issue     | backlog, todo, in_progress, in_review, done, blocked    |
| Task      | pending, queued, running, completed, failed, cancelled  |
| Sprint    | planning, active, completed                             |
| Epic      | draft, active, completed                                |
| Milestone | planned, in_progress, completed, missed                 |

## Critical Rules

1. **Never delete files** -- mark as archived/cancelled instead.
2. **Never modify IDs** -- IDs are permanent.
3. **Always update the `Updated` timestamp** field on every change.
4. **Check the `Target Repo` field on issues** -- code changes go to target repositories via coding tasks, not directly in this repo.
5. **Read `skills/coding/`** before starting any coding task.
6. **Confirm destructive actions** -- ask before bulk changes.

## References

- `skills/coding/conventions.md` -- coding conventions
- `skills/coding/testing.md` -- testing guidelines
- `docs/architecture.md` -- tech stack details (Go 1.25, React 19, PostgreSQL 18)
- `README.md` -- full navigation guide with quest patterns

## Commit Format

```
type(scope): message
```

Examples: `feat(auth): add Google OAuth login`, `fix(api): handle null response body`
