# SOUL.md — Core Principles

This file defines the mission, values, and guiding principles for AI agents working on this repository.

## Mission

This repository is a **planning and management system** that organizes software work into a clear hierarchy: **Milestones → Epics → Sprints → Issues → Tasks**. It serves as the single source of truth for project planning, tracking all work items as markdown files that can be rendered into various views (kanban, list, timeline).

## Core Values

### Conservative Changes
- Read before writing — understand existing state before modifying
- Preserve all identifiers — IDs are permanent
- Only modify this repository; code goes to target repos
- Confirm before destructive or bulk operations

### Cross-References
- Everything connects to everything else
- Bidirectional links: issue ↔ task, issue ↔ sprint ↔ epic
- Link richly to help navigation and context

### Human Oversight
- AI agents propose; humans approve
- Never delete — archive instead
- Commit often with clear messages
- Flag uncertainties, don't assume

## How to Approach This Project

### Read-First
Always start by reading relevant files to understand current state. This repository's power is its interconnected structure — jumping in without context breaks that.

### Link Everything
When you touch a file, update its links. When you create something, connect it to its context. Disconnected data loses value.

### Commit Often
Each meaningful change is a commit. Clear messages help everyone understand the project's evolution.

### Follow the Hierarchy
- Milestones contain epics
- Epics contain issues
- Issues are worked on in sprints
- Issues generate tasks (for code implementation)

## Constraints

1. **This repository only** — Can modify markdown files here, but code changes must go to the target repositories specified in issues
2. **Permanent IDs** — Never change or reuse IDs
3. **Timestamps** — Always update the `Updated` field when modifying
4. **Bidirectional links** — If A points to B, B should point back to A

## Success Criteria

- All work items are properly nested in the hierarchy
- Cross-references are complete and accurate
- Timestamps reflect real modification times
- Commit messages clearly describe changes
- No orphaned or disconnected files