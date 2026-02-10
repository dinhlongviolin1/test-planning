# 🎮 Agent Navigation Guide

Welcome, AI Agent! This document is your guide to understanding and navigating this project repository. Think of it like a game tutorial - read this first before making any moves.

## 🌍 World Overview

You are an AI assistant managing the **test-planning** software project. This repository is your "game world" where all project management data lives as markdown files.

**Your Powers:**
- 📖 Read any file to understand project state
- ✏️ Write to files to make changes
- 🔍 Search the web for technical guidance
- 🤖 Spawn coding agents to write code

**Your Constraints:**
- You can only modify files in THIS repository (the planning repo)
- Code changes go to TARGET repositories via coding tasks
- All changes are committed to git (version controlled)
- You use the human's GitHub credentials (respect their permissions)

## 🗺️ Map of the World

```
/                      ← Root of planning repo
├── README.md          ← YOU ARE HERE
├── project.md         ← Project overview, linked code repos
├── team.md            ← Team members (for @mentions)
├── requirements.txt   ← Python dependencies
├── .gitignore         ← Git ignore rules
│
├── src/               ← Python source code
│   └── team_members/  ← Team member utilities package
│       ├── __init__.py
│       └── ...
│
├── scripts/           ← Executable scripts
│   ├── list_users.py
│   ├── get_team_members.py
│   └── README.md
│
├── tests/             ← Unit tests
│   ├── __init__.py
│   └── test_team_members.py
│
├── milestones/        ← Long-term release targets
│   ├── _index.md      ← Overview + how to use
│   └── m-XXX.md       ← Individual milestones
│
├── epics/             ← Large features (span multiple sprints)
│   ├── _index.md
│   └── e-XXX.md
│
├── sprints/           ← Time-boxed work periods
│   ├── _index.md
│   ├── current.md     ← IMPORTANT: Points to active sprint
│   └── s-XXX.md
│
├── issues/            ← Individual work items
│   ├── _index.md      ← Overview + NEXT ID COUNTER
│   └── i-XXX.md       ← One file per issue (self-contained)
│
├── tasks/             ← 🤖 AI coding tasks
│   ├── _index.md      ← Overview + NEXT ID COUNTER
│   └── t-XXX.md       ← One file per task
│
└── skills/            ← Instructions for you!
    ├── coding/        ← How to write code for this project
    └── views/         ← How to style views
```

## 🎯 Common Quests

### Quest: "Show me the current sprint"
1. Read `sprints/current.md` to get the active sprint ID
2. Read `sprints/s-{id}.md` for full sprint details
3. Generate JSON matching the requested view schema

### Quest: "Create a new issue"
1. Read `issues/_index.md` to get the NEXT_ID
2. Create `issues/i-{NEXT_ID}.md` using the issue template
3. Update `issues/_index.md` to increment NEXT_ID
4. If sprint specified, update the sprint file's issue list
5. If epic specified, update the epic file's issue list

### Quest: "Move issue X to Done"
1. Read the issue file `issues/i-X.md`
2. Update the Status field to `done`
3. Update the `updated` timestamp
4. Read `sprints/current.md` to get current sprint
5. Update sprint file: move issue from old status list to `done` list

### Quest: "Implement issue X" (coding task)
1. Read `issues/i-X.md` thoroughly
2. Note the `Target Repo` field - that's where code goes
3. Read `skills/coding/` for project conventions
4. Search web if needed for technical guidance
5. Create `tasks/t-{NEXT_ID}.md` with full context
6. Update `tasks/_index.md` to increment NEXT_ID
7. Update issue file to link the task
8. Submit task to the coding queue
9. Wait for results and update task file

### Quest: "Quick coding task" (orphan, no issue)
1. Read `skills/coding/` for conventions
2. Create `tasks/t-{NEXT_ID}.md` with Issue field as `-`
3. Proceed with coding task as above

## 📜 File Format Rules

### Every file has a Meta table
```markdown
## Meta
| Field | Value |
|-------|-------|
| ID | x-001 |
| Status | active |
...
```
- Always preserve existing IDs
- Always update `Updated` timestamp when modifying

### IDs are sequential
- Read `_index.md` for NEXT_ID before creating
- Increment NEXT_ID after creating

### Links are bidirectional
- If issue links to task → task links back to issue
- If issue is in sprint → sprint lists the issue

### Status values
| Entity | Valid Statuses |
|--------|---------------|
| Issue | backlog, todo, in_progress, in_review, done, blocked |
| Task | pending, queued, running, completed, failed, cancelled |
| Sprint | planning, active, completed |
| Epic | draft, active, completed |
| Milestone | planned, in_progress, completed, missed |

## ⚠️ Critical Rules

1. **Never delete files** - Mark as archived/cancelled instead
2. **Never modify IDs** - IDs are permanent
3. **Always update timestamps** - `Updated` field on every change
4. **Check target repo** - Issues specify which repo code goes to
5. **Read skills first** - Before coding tasks, read `skills/coding/`
6. **Confirm destructive actions** - Ask before bulk changes

## 🔗 Relationship Diagram

```
Milestone (v1.0)
    │
    └── Epic (Authentication)
            │
            ├── Issue (Implement OAuth)
            │       │
            │       └── Task (AI coding task) ──→ PR (in code repo)
            │
            └── Issue (Add MFA)
                    │
                    └── Task ──→ PR
```

## 🎮 View Generation

When user asks to see something, you generate JSON data:

1. User: "Show kanban board"
2. You: Read sprint file, parse issues
3. You: Generate JSON matching kanban schema
4. Frontend: Renders the view

**You don't render views** - you provide structured data. The frontend handles display.

## 💡 Tips for Success

- **Start by reading** - Always read relevant files before changing anything
- **Be conservative** - When unsure, ask the user
- **Link everything** - Cross-references help everyone navigate
- **Use the skills** - Project-specific instructions are in `skills/`
- **Commit often** - Each change is a git commit with a clear message
