# API Specification

## Base URL

`http://localhost:8080/v1`

## Authentication

All endpoints require `Authorization: Bearer <jwt>` header.

## PM Endpoints

### Projects

| Method | Path | Description |
|--------|------|-------------|
| GET | `/pm/projects` | List all projects |
| GET | `/pm/projects/:id` | Get project by public ID |
| POST | `/pm/projects` | Create project |
| PUT | `/pm/projects/:id` | Update project |

### Issues

| Method | Path | Description |
|--------|------|-------------|
| GET | `/pm/issues` | List issues (filter: project_id, team_id, status) |
| GET | `/pm/issues/:id` | Get issue |
| POST | `/pm/issues` | Create issue |
| PUT | `/pm/issues/:id` | Update issue |
| DELETE | `/pm/issues/:id` | Delete issue |

### Context Docs

| Method | Path | Description |
|--------|------|-------------|
| GET | `/pm/projects/:id/context-index` | Full folder + doc tree |
| POST | `/pm/projects/:id/context-init` | Bootstrap default folders |
| POST | `/pm/projects/:id/context-restructure` | Batch move docs |
| POST | `/pm/projects/:id/context/import-project-file` | OCR file → PM doc |
| POST | `/pm/projects/:id/context/import-repo-folder` | Repo folder → PM docs |

### Repo Access

| Method | Path | Description |
|--------|------|-------------|
| GET | `/pm/projects/:id/repo/tree` | List repo files |
| GET | `/pm/projects/:id/repo/content` | Read file content |

## MCP Endpoint

`POST /v1/mcp` — JSON-RPC 2.0 over HTTP  
`GET /v1/mcp` — List available tools

### Example tool call

```json
{
  "jsonrpc": "2.0",
  "id": 1,
  "method": "tools/call",
  "params": {
    "name": "pm_context_read_index",
    "arguments": { "project_id": "proj_abc123" }
  }
}
```
