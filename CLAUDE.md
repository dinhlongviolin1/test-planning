# CLAUDE.md — AI Assistant Guidelines

## Project Context

This is a test-planning project for validating the Tokamak PM system end-to-end: issue tracking, kanban boards, context docs, GitHub integration, and AI agent workflows.

## Tech Stack

- **Backend**: Go 1.25 · Gin · GORM · Wire DI · PostgreSQL 18 · pgvector
- **Frontend**: React 19 · TanStack Router · Zustand v5 · Tailwind CSS 4
- **AI**: MCP tools over JSON-RPC 2.0 · Vercel AI SDK v5
- **GitHub**: GitHub App installation tokens (org-level)

Reference: `docs/architecture.md`

## Key Services

- **PM Service**: Issues, initiatives (epics), projects, boards, sprints
- **Document Service**: `pm_documents` (markdown), `pm_documents` (OCR-processed uploads)
- **MCP Tools**: 60 registered tools across issues, projects, teams, context docs, repo access, task dispatch

## Naming Conventions

Reference: `skills/coding/conventions.md`

| Type | Convention | Example |
|------|------------|---------|
| Public IDs | prefix + underscore | `iss_abc123`, `proj_xyz` |
| Files | kebab-case | `user-service.ts` |
| Functions | camelCase | `getUserById` |

## Public ID Prefixes

- Issues: `iss_`
- Projects: `proj_`
- Initiatives: `init_`
- Documents: `doc_`
- Document categories: `dcat_`

## GitHub Integration

Installation token resolution pattern:
1. `GetInstallationForUser(owner)` — lookup GitHub App installation by org
2. `GetInstallationToken(installationID)` — returns scoped token
3. Token used for tree/content API calls (no PAT required)

## Database Schema

Main tables in `llm_api` schema:
- `pm_projects` + `pm_project_repos`
- `pm_issues` + `pm_issue_initiatives`
- `pm_initiatives` (epics)
- `pm_documents` + `pm_document_categories`
- `pm_tasks` + `pm_task_executions`

## Reference Files

- `docs/overview.md` — project goals and team
- `docs/architecture.md` — technical architecture
- `skills/coding/conventions.md` — coding standards
- `team.md` — team members