# SOUL.md — Project Principles, Values, and Mission

## Mission

Enable AI agents to manage software projects using markdown-based workflows. We build a project planning system where all data lives in version-controlled markdown files, allowing AI assistants to orchestrate software development through structured planning documents.

## Core Values

### Transparency

All project data exists in plain-text markdown files that are version-controlled with Git. Anyone can inspect the state of the project by reading files. There are no hidden databases or opaque state — the planning repo is the single source of truth.

### Automation

We design for AI-first workflows. Every process that can be automated should be — from issue creation to sprint tracking to code task generation. The system exists to amplify AI capability in project management.

### Collaboration

We believe in human-AI partnership. AI handles coordination, tracking, and routine tasks while humans focus on creative decisions and domain expertise. The system facilitates this partnership rather than replacing human judgment.

## Principles

### 1. Never Delete Data

Data is never removed — only archived or marked as cancelled. This preserves history, enables audit trails, and allows recovery from mistakes. Use the `Status` field to mark items as cancelled rather than deleting files.

### 2. Maintain Bidirectional Links

Every relationship between entities flows both directions. Issues reference their epics; epics list their issues. Tasks link to their parent issues; issues track their tasks. This creates a navigable web of context.

### 3. Keep Timestamps Updated

The `Updated` field in every Meta table reflects the last modification. This enables sorting by recency, detecting stale items, and understanding project velocity. Always update timestamps when making changes.

### 4. Use Clear Identifiers

Every entity has a unique, stable ID (m-XXX, e-XXX, s-XXX, i-XXX, t-XXX). These IDs are never reused or modified. This enables precise referencing across the entire project ecosystem.

### 5. Prefer Explicit Over Implicit

State is expressed explicitly in markdown files rather than inferred or stored in external systems. This makes the project self-documenting and enables offline analysis.

## Team Structure

The project is maintained by a distributed team:

| Role | Members |
|------|---------|
| Senior Software Engineers | @louis, @nguyen, @vanalite |
| Software Engineer | @dinhlongviolin1 |
| Frontend Engineer/UI Designer | @faisal |
| Researchers | @bach, @alan, @alex, @thinhle |

## Relationship to Code

This planning repository coordinates work across code repositories. Issues specify a `Target Repo` where implementation occurs. Tasks represent AI coding jobs that generate pull requests in target repositories.

## Guiding Philosophy

The system treats project planning as a structured conversation between humans and AI. Each markdown file is a record of intent, progress, and outcome. The AI's role is to maintain this record accurately, surface relevant information, and guide work toward completed objectives.

When making decisions, prioritize:
1. **Clarity** — Can someone understand this by reading the files?
2. **Traceability** — Can we trace any item back to its origin?
3. **Automation** — Can this manual process be systematized?
4. **History** — Will future maintainers have the context they need?

## Reference

- Project overview: [project.md](project.md)
- Navigation guide: [README.md](README.md)
- AI assistant guidelines: [CLAUDE.md](CLAUDE.md)