# Contributing

Thank you for your interest in contributing to the `test-planning` project! This document provides guidelines and instructions for contributors.

## Getting Started

The `test-planning` repository is a **markdown-based planning system** that tracks issues, epics, sprints, milestones, and AI coding tasks. All data is stored as markdown files with structured meta tables. Contributions can range from adding team members, creating and managing issues, to writing code for target repositories.

## Becoming a Contributor

To get added as a contributor to this project, you need to open two pull requests that update both `team.md` and `AUTHOR.md` together. This bidirectional approach ensures contributor information is consistent across both files.

### Step 1: Update `team.md`

Add yourself to the Contributors table in `team.md` with the following columns:

| Username | Name | Role | Capacity/Sprint |
|----------|------|------|-----------------|
| @yourusername | Your Name | Your Role | 10 pts |

### Step 2: Update `AUTHOR.md`

Add yourself to the Contributors table in `AUTHOR.md` with the following columns:

| Username | Name | Role |
|----------|------|------|
| @yourusername | Your Name | Your Role |

### Notes

- Both PRs should be opened together (you can link them)
- See the existing entries in both files for the format to follow
- If you're unsure which role to assign yourself, consult with the team

## Working with Issues

Issues are individual work items stored in `issues/` as `i-XXX.md` files.

### Meta Table

Every issue file has a `## Meta` section:

```markdown
## Meta
| Field | Value |
|-------|-------|
| ID    | i-001 |
| Status | backlog |
| Updated | 2026-04-16 |
```

### Valid Issue Statuses

| Status | Description |
|--------|-------------|
| backlog | Not yet prioritized |
| todo | Ready to work on |
| in_progress | Currently being worked on |
| in_review | Under review |
| done | Completed |
| blocked | Waiting on external dependency |

### Critical Rules

- **Never delete issues** -- mark as archived/cancelled instead
- **Never modify IDs** -- IDs are permanent
- **Always update the `Updated` timestamp** when modifying files
- **Check the `Target Repo` field** -- code changes go to target repositories via coding tasks, not directly in this repo

## Working with Sprints and Epics

### Sprints

Sprints are time-boxed work periods stored in `sprints/` as `s-XXX.md` files.

| Status | Description |
|--------|-------------|
| planning | Sprint is being planned |
| active | Sprint is in progress |
| completed | Sprint has ended |

### Epics

Epics are large features spanning multiple sprints, stored in `epics/` as `e-XXX.md` files.

| Status | Description |
|--------|-------------|
| draft | Epic is being defined |
| active | Epic is being worked on |
| completed | Epic is finished |

## Coding Tasks

AI coding tasks are stored in `tasks/` as `t-XXX.md` files. Each task represents work to be done in a target repository.

### Valid Task Statuses

| Status | Description |
|--------|-------------|
| pending | Not yet queued |
| queued | Waiting to be executed |
| running | Currently being executed |
| completed | Task finished successfully |
| failed | Task encountered an error |
| cancelled | Task was cancelled |

### Before Working on Code Tasks

Read the following files before working on any coding task:

- `skills/coding/conventions.md` -- coding conventions and style guidelines
- `skills/coding/testing.md` -- testing requirements and best practices

## Bidirectional Links

Links between entities in this project are always **bidirectional**. This ensures consistency across the planning system.

### Examples

- If an issue links to an epic, the epic must also list that issue
- If an issue is assigned to a sprint, the sprint file must list that issue
- If a task relates to an issue, the issue must link to the task

### Why This Matters

Bidirectional linking prevents orphaned references and ensures that navigating from any file gives a complete picture of its relationships. When you update one side of a relationship, always update the other.

## Commit Format

All commits must follow this format:

```
type(scope): message
```

### Types

| Type | Description |
|------|-------------|
| feat | New feature |
| fix | Bug fix |
| docs | Documentation changes |
| style | Formatting, whitespace (no code change) |
| refactor | Code refactoring (no feature/fix change) |
| test | Adding or updating tests |
| chore | Maintenance tasks, dependencies |

### Examples

```
feat(auth): add Google OAuth login
fix(api): handle null response body
docs(contributing): add CONTRIBUTING.md
refactor(issues): extract status validation
test(auth): add unit tests for login flow
chore(deps): upgrade dependencies
```

## Questions?

If you have questions about contributing, reach out to a team member via the GitHub repository's issues or discussions.