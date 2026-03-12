# CLAUDE.md - Claude Code Agent Guide

This file provides an overview of the test-planning project for Claude Code agents.

## Project Name

**test-planning** - A markdown-based project planning repository

## What This Project Is

A documentation-driven project management system that tracks software projects using markdown files. It manages milestones, epics, sprints, issues, and tasks through structured markdown files. The repository also includes Python utility scripts in the `scripts/` directory for team member management.

## Tech Stack Overview

- **Primary**: Markdown files for all project management data
- **Scripts**: Python 3 for utility functions (e.g., `get_team_members.py`)
- **No framework** - This is a documentation/repository structure, not a software application

## Directory Structure

```
/workspace/repo                    # Root directory
├── CLAUDE.md                      # This file
├── README.md                      # Project overview and navigation guide
├── project.md                     # Project details and linked repositories
├── team.md                        # Team member information
│
├── epics/                         # Large features spanning multiple sprints
│   ├── _index.md                  # Overview + NEXT_ID counter
│   └── e-XXX.md                   # Individual epics
│
├── issues/                        # Individual work items
│   ├── _index.md                  # Overview + NEXT_ID counter (READ BEFORE CREATING NEW ISSUES)
│   └── i-XXX.md                   # Individual issues
│
├── milestones/                    # Long-term release targets
│   ├── _index.md                  # Overview + NEXT_ID counter
│   └── m-XXX.md                   # Individual milestones
│
├── sprints/                       # Time-boxed work periods
│   ├── _index.md                  # Overview + NEXT_ID counter
│   ├── current.md                 # Points to active sprint (READ FIRST FOR CURRENT SPRINT)
│   └── s-XXX.md                   # Individual sprints
│
├── tasks/                         # AI coding tasks
│   ├── _index.md                  # Overview + NEXT_ID counter
│   └── t-XXX.md                   # Individual tasks
│
├── skills/                        # Project-specific instructions for agents
│   └── coding/
│       ├── _index.md
│       ├── conventions.md         # Coding conventions for target repositories
│       └── testing.md
│
├── scripts/                       # Python utility scripts
│   ├── README.md
│   ├── get_team_members.py
│   └── list_users.py
│
└── .tokamak/                      # Orchestration and history
    └── history/                   # Session history
```

## Important Conventions

### Meta Tables

Every entity file contains a Meta table with ID, Status, and Updated fields:

```markdown
## Meta
| Field | Value |
|-------|-------|
| ID | x-001 |
| Status | active |
| Updated | 2026-03-12 |
```

- Always preserve existing IDs
- Always update the `Updated` timestamp when modifying any file

### ID Sequential Numbering

IDs are sequential across each entity type. **Before creating a new file, you MUST:**

1. Read the corresponding `_index.md` file to get the current `NEXT_ID`
2. Create the new file with the next sequential ID
3. Update `_index.md` to increment `NEXT_ID`

### Cross-References Are Bidirectional

- If an issue links to a task, the task must link back to the issue
- If an issue is assigned to a sprint, the sprint must list the issue
- Always maintain bidirectional links when creating or modifying relationships

### Status Values

| Entity | Valid Statuses |
|--------|---------------|
| Issue | `backlog`, `todo`, `in_progress`, `in_review`, `done`, `blocked` |
| Task | `pending`, `queued`, `running`, `completed`, `failed`, `cancelled` |
| Sprint | `planning`, `active`, `completed` |
| Epic | `draft`, `active`, `completed` |
| Milestone | `planned`, `in_progress`, `completed`, `missed` |

## How to Validate

1. **Check NEXT_ID counters**: Always read `_index.md` files before creating new entities to ensure correct ID assignment
2. **Verify bidirectional references**: When linking entities, ensure the relationship exists in both directions
3. **Validate Meta tables**: Ensure all files have correct timestamps in the `Updated` field when modified
4. **Check status values**: Use only the valid status values listed above

## Key File Locations

- `/workspace/repo/README.md` - General project overview and navigation guide for agents
- `/workspace/repo/project.md` - Project details, goals, and linked code repositories
- `/workspace/repo/team.md` - Team members list with roles and capacity
- `/workspace/repo/skills/coding/conventions.md` - Coding conventions for target repositories
- `/workspace/repo/sprints/current.md` - Points to the currently active sprint
- `/workspace/repo/.tokamak/history/` - Session history for context on previous work
- `/workspace/repo/issues/_index.md` - **NEXT_ID counter for issues** (read before creating new issues)
- `/workspace/repo/tasks/_index.md` - **NEXT_ID counter for tasks** (read before creating new tasks)

## Common Tasks for Claude Code Agents

1. **Find current sprint**: Read `sprints/current.md` to get the active sprint ID, then read `sprints/s-{id}.md`
2. **Create new issue**: Read `issues/_index.md` for NEXT_ID, create file, update counter
3. **Move issue to done**: Update issue Status field and Updated timestamp, update sprint file
4. **Create coding task**: Read `tasks/_index.md`, create task file with full context from issue