# CLAUDE.md - LLM Agent Guide

This file provides LLM-specific context for working with this markdown-based test-planning project management system. For a general overview, see README.md.

## Project Description

This is a markdown-based test-planning project management system. It uses markdown files to track issues, epics, sprints, tasks, and milestones. All project data is stored as self-contained markdown files with consistent formatting.

## Repository Structure Overview

```
/workspace/repo/
├── README.md           ← Main guide for agents - read this first
├── CLAUDE.md           ← LLM-specific context (this file)
├── project.md          ← Project overview and linked code repos
├── team.md             ← Team members for @mentions
│
├── issues/             ← Individual work items (i-XXX.md files)
│   ├── _index.md       ← NEXT_ID counter for new issues
│   └── i-XXX.md        ← Individual issue files
│
├── epics/              ← Large features spanning multiple sprints
│   ├── _index.md
│   └── e-XXX.md
│
├── sprints/            ← Time-boxed work periods
│   ├── _index.md
│   ├── current.md      ← Points to active sprint
│   └── s-XXX.md
│
├── tasks/              ← AI coding tasks
│   ├── _index.md       ← NEXT_ID counter for new tasks
│   └── t-XXX.md
│
├── skills/             ← Instructions for AI agents
│   ├── coding/         ← Coding conventions
│   │   ├── _index.md
│   │   ├── conventions.md
│   │   └── testing.md
│   └── views/          ← View styling conventions
│
├── scripts/            ← Python utility scripts
│   ├── get_team_members.py
│   ├── list_users.py
│   └── README.md
│
├── milestones/         ← Long-term release targets
│   ├── _index.md
│   └── m-XXX.md
│
├── .tokamak/           ← Orchestration metadata
└── .claude/            ← Claude session memory
```

## Main Technologies

- **Documentation-driven**: All project data stored as markdown files
- **Python**: Utility scripts for team member retrieval (get_team_members.py, list_users.py)
- **Git**: Version control for all changes
- **No complex setup needed**: Just read/write markdown files with any text editor

## Development Setup

1. Clone the repository
2. No dependencies required - this is a documentation-driven system
3. Use any text editor for markdown editing
4. Python 3 for running utility scripts in the scripts/ directory

## How to Work with the Project

### Reading and Writing Markdown Files
- All project data lives in markdown files
- Each file type has a specific format with a Meta table at the top

### Updating Issue Status
1. Read the issue file (e.g., `issues/i-002.md`)
2. Update the Status field in the Meta table
3. Update the Updated timestamp

### Creating New Items
1. Read the corresponding `_index.md` file to get the NEXT_ID
2. Create the new file using the appropriate template
3. Update `_index.md` to increment NEXT_ID

### Maintaining Bidirectional Links
- If an issue links to a task, the task must link back to the issue
- If an issue is assigned to a sprint, the sprint must list the issue

### Managing Sprints
- Read `sprints/current.md` to find the active sprint
- Sprints contain lists of issues by status (todo, in_progress, done)

## Coding Conventions

Follow these conventions from `skills/coding/conventions.md`:

### Naming Conventions
| Type | Convention | Example |
|------|------------|---------|
| Files | kebab-case | user-service.ts |
| Classes | PascalCase | UserService |
| Functions | camelCase | getUserById |
| Constants | SCREAMING_SNAKE | MAX_RETRIES |

### Git Commits
Format: `type(scope): message`

Types: `feat`, `fix`, `docs`, `style`, `refactor`, `test`, `chore`

Examples:
- `feat(auth): add Google OAuth login`
- `fix(api): handle null user in profile endpoint`
- `docs: update issue i-002 status to in_progress`

### Code Style
- Group imports: external first, then internal
- Sort alphabetically within groups
- Use custom error classes with error codes and messages
- Use structured logging with relevant context

## Important Notes for LLMs

### README.md is the Main Guide
- README.md contains the primary documentation for agents
- CLAUDE.md supplements README.md with LLM-specific context
- Always read README.md first when starting work

### File Format Rules

Every file has a Meta table:
```markdown
## Meta
| Field | Value |
|-------|-------|
| ID | i-002 |
| Status | in_progress |
| Created | 2026-03-18 |
| Updated | 2026-03-18 |
```

**Critical rules:**
- Always preserve existing IDs
- Always update the `Updated` timestamp when modifying files
- IDs are sequential - read `_index.md` for NEXT_ID before creating new files
- Never delete files - mark as archived/cancelled instead

### Status Values

| Entity | Valid Statuses |
|--------|---------------|
| Issue | backlog, todo, in_progress, in_review, done, blocked |
| Task | pending, queued, running, completed, failed, cancelled |
| Sprint | planning, active, completed |
| Epic | draft, active, completed |
| Milestone | planned, in_progress, completed, missed |

### Bidirectional Linking
- Links must be maintained both ways
- If issue links to task → task links back to issue
- If issue is in sprint → sprint lists the issue
- If issue belongs to epic → epic lists the issue

### Skills Directory
- Check `skills/coding/` for project-specific coding conventions before coding tasks
- Use `skills/coding/testing.md` for testing guidelines

### Commit Convention
- Always use conventional commits: `type(scope): message`
- Include `.tokamak/` and `.claude/` files in commits - these are first-class project files
- Stage files explicitly - never use `git add -A` or `git add .`