# ARCHITECTURE.md — System Architecture

This document explains the architecture of the test-planning management system.

## What Is This Repository?

This is a **markdown-based project management system** where all planning data lives as human-readable markdown files. It serves as the central hub for organizing and tracking work across a software project.

### Key Characteristics

- **File-based storage**: All data stored in markdown files with structured metadata
- **Hierarchical organization**: Milestones → Epics → Sprints → Issues → Tasks
- **Bidirectional references**: All relationships are tracked in both directions
- **ID-based referencing**: Entities use stable IDs for cross-referencing

## Directory Structure

```
/                   ← Root
├── project.md      ← Project metadata and linked repositories
├── team.md         ← Team member directory
│
├── milestones/     ← Long-term release targets (quarters, versions)
│   └── m-XXX.md    ← Individual milestone
│
├── epics/          ← Large features spanning multiple sprints
│   └── e-XXX.md    ← Individual epic
│
├── sprints/        ← Time-boxed work periods (typically 2 weeks)
│   ├── current.md  ← Pointer to active sprint
│   └── s-XXX.md    ← Individual sprint
│
├── issues/         ← Individual work items (user stories, bugs)
│   └── i-XXX.md    ← Individual issue
│
├── tasks/          ← AI coding tasks for implementation
│   └── t-XXX.md    ← Individual task
│
└── skills/         ← AI assistant instructions
    └── coding/     ← Code conventions
```

## Entity Relationships

The system follows a hierarchical containment model:

```
Milestone (v1.0)
    │
    ├── Epic (Authentication)
    │       │
    │       ├── Issue (Implement OAuth)
    │       │       │
    │       │       └── Task (AI coding task) ──→ PR (in target repo)
    │       │
    │       └── Issue (Add MFA)
    │               │
    │               └── Task ──→ PR
    │
    └── Epic (API Redesign)
            │
            └── Issue (Rate limiting)
                    │
                    └── Task ──→ PR
```

### Relationship Rules

| From | To | Relationship |
|------|-----|--------------|
| Milestone | Epic | Contains multiple epics |
| Epic | Issue | Contains multiple issues |
| Sprint | Issue | Assigns multiple issues |
| Issue | Task | Can spawn one task |
| Issue | Epic | Belongs to one epic |
| Issue | Sprint | Assigned to one sprint |
| Issue | Milestone | Contributes to one milestone |

## Workflow: How Work Flows Through the System

### 1. Planning Phase

1. **Create Milestone** - Define a release target (e.g., "Q1 2026 Foundation")
2. **Create Epic** - Break milestone into large feature areas
3. **Create Issues** - Further break epics into actionable items

### 2. Execution Phase

1. **Assign to Sprint** - Move issues into a sprint's backlog
2. **Track Progress** - Sprint tracks issues by status (Todo → In Progress → In Review → Done)
3. **Implement** - Create tasks for AI coding agents

### 3. Completion Phase

1. **Mark Done** - Issue status changes to `done`
2. **Sprint Complete** - Sprint status changes to `completed`
3. **Epic Complete** - When all issues done, epic status changes
4. **Milestone Complete** - When all sprints done, milestone status changes

## File Structure Details

### Issue File (`issues/i-XXX.md`)

```markdown
# Meta
| Field | Value |
|-------|-------|
| ID | i-002 |
| Status | in_progress |
| Created | 2026-01-30 |
| Updated | 2026-02-09 |
| Points | 5 |
| Assignee | @username |

## Title
[Issue title]

## Description
[Detailed description]

## Linked Epics
- [e-002](e-002.md)

## Linked Sprint
- [s-001](s-001.md)

## Target Repo
[GitHub repo where code should be written]

## Tasks
- [ ] Subtask 1
- [ ] Subtask 2
```

### Sprint File (`sprints/s-XXX.md`)

Contains status-based issue lists:
- Issues (Todo)
- Issues (In Progress)
- Issues (In Review)
- Issues (Done)

### Task File (`tasks/t-XXX.md`)

Contains implementation context for AI coding agents.

## State Transitions

### Issue States
```
backlog → todo → in_progress → in_review → done
    ↓
  blocked
```

### Sprint States
```
planning → active → completed
```

### Epic States
```
draft → active → completed
```

### Milestone States
```
planned → in_progress → completed | missed
```

## Design Principles

1. **Single Source of Truth** - Each entity exists in exactly one file
2. **Bidirectional Links** - References go both ways for navigation
3. **Immutable IDs** - Once created, IDs never change
4. **Timestamp Tracking** - Every change updates the `Updated` field
5. **Self-Contained Files** - Issue files have all relevant context

## Usage Notes

- This repository is the **planning repo** - not the code repo
- Code changes go to **target repositories** specified in issues
- View generation: AI provides JSON data, frontend renders the UI
- Skills in `skills/` provide AI-specific instructions