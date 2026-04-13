# CLAUDE.md — AI Assistant Guidance

## Project Overview

- **Name**: test-planning
- **Type**: Documentation/Project Management
- **Description**: A project management repository where all planning data lives as markdown files. AI assistants manage issues, tasks, epics, sprints, and milestones through file operations.
- **Status**: Active
- **Created**: 2026-01-29

## Directory Structure

```
/workspace/repo/
├── README.md              # Agent navigation guide (READ THIS FIRST)
├── project.md             # Project overview, linked code repos
├── team.md                # Team members for @mentions
├── CLAUDE.md              # This file — AI assistant guidance
├── SOUL.md                # Complementary AI guidance
├── issues/                # Individual work items (i-XXX.md)
├── tasks/                 # AI coding tasks (t-XXX.md)
├── epics/                 # Large features (e-XXX.md)
├── sprints/               # Time-boxed work periods (s-XXX.md)
├── milestones/            # Release targets (m-XXX.md)
├── skills/                # Project-specific instructions
│   └── coding/            # How to write code for linked repos
├── docs/                  # Project documentation
├── scripts/               # Utility scripts
└── uploads/               # Sample files for testing OCR features
```

## Key Files

| File | Purpose |
|------|---------|
| `issues/_index.md` | Issue index with NEXT_ID counter |
| `tasks/_index.md` | Task index with NEXT_ID counter |
| `sprints/current.md` | Points to active sprint |
| `skills/coding/conventions.md` | Code conventions for target repos |

## Development Patterns

### File ID System
- Always read `_index.md` before creating new files to get the next ID
- IDs are sequential and permanent — never modify existing IDs
- Update `_index.md` to increment NEXT_ID after creating new files

### Meta Tables
Every entity file has a Meta table at the top:
```markdown
## Meta
| Field | Value |
|-------|-------|
| ID | i-001 |
| Status | todo |
| Updated | 2026-04-13 |
```
- Always update `Updated` timestamp when modifying files
- Use valid status values: issues (backlog/todo/in_progress/in_review/done/blocked), tasks (pending/queued/running/completed/failed/cancelled), sprints (planning/active/completed)

### Bidirectional Linking
- Issues link to tasks → tasks link back to issues
- Issues in sprints → sprints list the issues
- Update both sides when creating/modifying relationships

## How to Work With This Project

### Common Tasks

**Show current sprint:**
1. Read `sprints/current.md` → get sprint ID
2. Read `sprints/s-{id}.md` → get full details

**Create new issue:**
1. Read `issues/_index.md` → get NEXT_ID
2. Create `issues/i-{NEXT_ID}.md` using existing issue as template
3. Update `issues/_index.md` → increment NEXT_ID
4. If sprint specified, update sprint file's issue list

**Move issue to done:**
1. Read `issues/i-X.md` → update Status to `done`
2. Update `Updated` timestamp
3. Read `sprints/current.md` → update sprint file (move issue to done list)

**Create coding task:**
1. Read `issues/i-X.md` → note Target Repo
2. Read `skills/coding/` for conventions
3. Read `tasks/_index.md` → get NEXT_ID
4. Create `tasks/t-{NEXT_ID}.md` with full context
5. Update `tasks/_index.md` → increment NEXT_ID

## Constraints

- Never delete files — mark as archived/cancelled instead
- Never modify IDs — they are permanent
- Always update timestamps on changes
- Read `skills/coding/` before coding tasks
- Confirm destructive actions with user

## Related Repositories

Code changes go to target repositories specified in issues, not this planning repo.