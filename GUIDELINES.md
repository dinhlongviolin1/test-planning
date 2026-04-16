# Guidelines

This document is the human-readable rulebook for using the `test-planning` system. It summarizes the conventions, status vocabularies, and critical rules that keep the planning data consistent. For contributor onboarding, see [CONTRIBUTING.md](CONTRIBUTING.md); for agent-specific instructions, see [CLAUDE.md](CLAUDE.md).

## Purpose of the planning system

The `test-planning` repository is a markdown-based tracker for issues, epics, sprints, milestones, and AI coding tasks. All data is stored as plain markdown files with structured `## Meta` tables so the project history is reviewable, diffable, and editable without specialized tooling. Entities cross-reference one another so you can navigate the project from any file.

## Entity directory layout

| Directory | File pattern | Purpose |
|-----------|--------------|---------|
| `epics/` | `e-XXX.md` | Large features spanning multiple sprints |
| `issues/` | `i-XXX.md` | Individual work items |
| `sprints/` | `s-XXX.md` | Time-boxed work periods; `current.md` points to the active sprint |
| `milestones/` | `m-XXX.md` | Long-term release targets |
| `tasks/` | `t-XXX.md` | AI coding tasks executed against target repositories |

## Meta table convention

Every entity file has a `## Meta` section with a markdown table holding its identifying and state fields. At minimum, include an `ID`, a `Status`, and an `Updated` timestamp; additional fields vary by entity type.

```markdown
## Meta
| Field | Value |
|-------|-------|
| ID    | i-001 |
| Status | backlog |
| Updated | 2026-04-16 |
```

## Sequential IDs

Entity IDs are allocated sequentially and are permanent:

- Before creating a new entity, read `_index.md` in that entity directory and use its `NEXT_ID` value.
- After creating the entity, increment `NEXT_ID` in `_index.md` so the next contributor picks up the following number.
- Never modify an ID once it has been assigned — other files may already link to it.

## Bidirectional links

Every cross-entity link must be mirrored on both sides of the relationship. Examples:

- If an issue links to an epic, the epic's file must list that issue.
- If an issue is assigned to a sprint, the sprint's file must list that issue.
- If a task relates to an issue, the issue must link back to that task.

Mirroring prevents orphaned references and ensures navigating from any file gives a complete picture of its relationships.

## Status values

Each entity type has a fixed vocabulary of allowed status values. Use exactly these strings — no synonyms, no new values without updating CLAUDE.md first.

**Issue**

| Status | Description |
|--------|-------------|
| backlog | Not yet prioritized |
| todo | Ready to work on |
| in_progress | Currently being worked on |
| in_review | Under review |
| done | Completed |
| blocked | Waiting on external dependency |

**Task**

| Status | Description |
|--------|-------------|
| pending | Not yet queued |
| queued | Waiting to be executed |
| running | Currently being executed |
| completed | Task finished successfully |
| failed | Task encountered an error |
| cancelled | Task was cancelled |

**Sprint**

| Status | Description |
|--------|-------------|
| planning | Sprint is being planned |
| active | Sprint is in progress |
| completed | Sprint has ended |

**Epic**

| Status | Description |
|--------|-------------|
| draft | Epic is being defined |
| active | Epic is being worked on |
| completed | Epic is finished |

**Milestone**

| Status | Description |
|--------|-------------|
| planned | Scheduled but not yet started |
| in_progress | Actively being worked on |
| completed | Delivered on or before the target date |
| missed | Target date passed without delivery |

## Critical rules

1. Never delete files — mark them as archived or cancelled instead.
2. Never modify IDs — IDs are permanent once assigned.
3. Always update the `Updated` timestamp field on every change to an entity file.
4. Check the `Target Repo` field on issues — code changes go to target repositories via coding tasks, not directly in this repo.
5. Read `skills/coding/conventions.md` and `skills/coding/testing.md` before starting any coding task.
6. Confirm destructive actions — ask before performing bulk changes.

## Commit format

All commits follow the `type(scope): message` pattern.

```text
docs(guidelines): add GUIDELINES.md
```

See [CONTRIBUTING.md](CONTRIBUTING.md#commit-format) for the full list of allowed types and more examples.

## Related documents

- [CLAUDE.md](CLAUDE.md) — agent-facing instructions and critical rules
- [CONTRIBUTING.md](CONTRIBUTING.md) — how to contribute, full commit-type reference
- [ARCHITECTURE.md](ARCHITECTURE.md) — high-level architecture overview
- [STRUCTURE.md](STRUCTURE.md) — planning system structure
- [README.md](README.md) — navigation guide
- [skills/coding/conventions.md](skills/coding/conventions.md) and [skills/coding/testing.md](skills/coding/testing.md) — coding conventions and testing guidelines
