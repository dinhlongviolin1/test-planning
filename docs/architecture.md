# Architecture

## Stack

**Backend:** Go 1.25 · Gin · GORM · Wire DI · PostgreSQL 18 · pgvector  
**Frontend:** React 19 · TanStack Router · Zustand v5 · Tailwind CSS 4  
**AI:** MCP tools over JSON-RPC 2.0 · Vercel AI SDK v5  
**GitHub:** GitHub App installation tokens (org-level)

## Data Flow

```
User → Web UI → REST API (llm-api) → PostgreSQL
                     ↓
              MCP Server (/v1/mcp)
                     ↓
              AI Agent (responses API)
                     ↓
              GitHub App (repo access)
```

## Key Services

### PM Service
Owns issues, initiatives (epics), projects, boards, sprints.  
All public IDs are prefixed: `iss_`, `proj_`, `init_`, `doc_`, `dcat_`.

### Document Service
Handles pm_documents (markdown, stored in DB) and project_files (OCR-processed uploads via media API).

### MCP Tools
60 registered tools across: issues, projects, teams, context docs, repo access, task dispatch.

## Database Schema

Main tables in `llm_api` schema:
- `pm_projects` + `pm_project_repos`
- `pm_issues` + `pm_issue_initiatives`
- `pm_initiatives` (epics)
- `pm_documents` + `pm_document_categories`
- `pm_tasks` + `pm_task_executions`

## GitHub Integration

Installation tokens resolved via:
1. `GetInstallationForUser(owner)` — looks up GitHub App installation by org
2. `GetInstallationToken(installationID)` — returns a scoped token
3. Token used for tree/content API calls (no PAT required)
