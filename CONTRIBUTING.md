# Contributing to test-planning

## Introduction

`test-planning` is a markdown-based planning system that tracks issues, epics, sprints, milestones, and AI coding tasks. Contributors edit markdown files, not code — every entity lives as a plain-text file with a structured `## Meta` table so both humans and agents can read and modify project state directly. See [README.md](README.md) for navigation and the common quest patterns, and treat [CLAUDE.md](CLAUDE.md) as the authoritative source for conventions; this document is its human-readable companion.

## Getting Started

1. Clone the repository.
2. Create a feature branch off `main`.
3. Edit the relevant markdown file(s) for your change.
4. Open a pull request describing what you changed and why.

Entity directories you will typically touch:

- `epics/` — large features spanning multiple sprints (`e-XXX.md`)
- `issues/` — individual work items (`i-XXX.md`)
- `sprints/` — time-boxed work periods (`s-XXX.md`); `current.md` points to the active sprint
- `milestones/` — long-term release targets (`m-XXX.md`)
- `tasks/` — AI coding tasks (`t-XXX.md`)

The `skills/` directory contains agent instructions (including coding conventions and testing guidance), and `scripts/` contains utility scripts for querying the planning data.

## Repository Conventions

- **Meta tables:** every entity file has a `## Meta` section using the `| Field | Value |` schema.
- **Sequential IDs:** read `_index.md` in the entity directory for `NEXT_ID` before creating a new entity, then increment it after creation.
- **Bidirectional links:** if an issue links to an epic, the epic must list the issue (and vice versa).
- **Timestamps:** always update the `Updated` timestamp on every change.
- **No deletion:** never delete files — mark them as archived or cancelled instead.
- **No ID edits:** never modify an existing ID; IDs are permanent.
- **Destructive actions:** confirm before making bulk changes.
- **Target repo:** for issues, respect the `Target Repo` field — code changes land in the target repository via coding tasks, not in this repo.

See [CLAUDE.md](CLAUDE.md) for the authoritative version.

## Status Vocabularies

| Entity    | Valid Statuses                                          |
|-----------|---------------------------------------------------------|
| Issue     | backlog, todo, in_progress, in_review, done, blocked    |
| Task      | pending, queued, running, completed, failed, cancelled  |
| Sprint    | planning, active, completed                             |
| Epic      | draft, active, completed                                |
| Milestone | planned, in_progress, completed, missed                 |

If these diverge from CLAUDE.md, CLAUDE.md wins — open a PR to reconcile.

## Working with Entities

### Issues

Issues live in `issues/` as `i-XXX.md`. They move through the statuses above as work progresses. Link each issue to its parent epic (the link must be bidirectional — the epic should list the issue too), and set the `Target Repo` field whenever code work is involved so downstream coding tasks know where to land the change.

### Sprints

Sprints live in `sprints/` as `s-XXX.md`, and `sprints/current.md` points to the active sprint. When activating a new sprint, update `current.md` to reference it as part of the same change. Valid statuses are `planning`, `active`, and `completed`.

### Epics

Epics live in `epics/` as `e-XXX.md` and group related issues under a larger feature. Keep the list of child issues on the epic in sync with the issues that link to it. Valid statuses are `draft`, `active`, and `completed`.

### Milestones

Milestones live in `milestones/` as `m-XXX.md` and represent long-term release targets that span multiple sprints and epics. Link their child epics and sprints bidirectionally. Valid statuses are `planned`, `in_progress`, `completed`, and `missed`.

## Joining the Team (Adding Yourself as a Contributor)

The team roster is tracked in two places that must stay in sync: [team.md](team.md) (source of truth, section heading `## Members`) and [AUTHOR.md](AUTHOR.md) (mirror for discoverability, section heading `## Contributors`). To keep them aligned, open a **single PR** that updates **both** files in the same change. Do not split this across separate pull requests.

- **Joiner:** add yourself as a new row under `## Members` in [team.md](team.md) and mirror the row under `## Contributors` in [AUTHOR.md](AUTHOR.md), in one PR.
- **Role or handle change:** update the row in `team.md` first (source of truth), then mirror the change in `AUTHOR.md`, in one PR.
- **Leaver:** remove or archive the row in `team.md`, then remove the matching row in `AUTHOR.md`, in one PR.

## Commit Format

Follow the conventional-commits style from CLAUDE.md: `type(scope): message`. Examples:

- `feat(auth): add Google OAuth login`
- `fix(api): handle null response body`
- `docs(contributing): add CONTRIBUTING.md`

## Code Changes

Code-level work does not happen here. This repository only tracks planning artifacts (markdown); actual code changes land in the target repositories referenced by the `Target Repo` field on each issue, dispatched through AI coding tasks. For the standards those tasks follow, see [skills/coding/conventions.md](skills/coding/conventions.md) and [skills/coding/testing.md](skills/coding/testing.md).

## References

- [CLAUDE.md](CLAUDE.md)
- [README.md](README.md)
- [ARCHITECTURE.md](ARCHITECTURE.md)
- [STRUCTURE.md](STRUCTURE.md)
- [team.md](team.md)
- [AUTHOR.md](AUTHOR.md)
- [skills/coding/conventions.md](skills/coding/conventions.md)
- [skills/coding/testing.md](skills/coding/testing.md)
