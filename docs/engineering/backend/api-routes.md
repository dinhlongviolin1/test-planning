# API Routes Reference

## PM Routes (v1)

All routes require `Authorization: Bearer <jwt>`.

### Projects
- `GET /v1/pm/projects` — list all projects
- `POST /v1/pm/projects` — create project
- `GET /v1/pm/projects/:id` — get project

### Context Docs
- `GET /v1/pm/projects/:id/context-index` — full folder + doc tree
- `POST /v1/pm/projects/:id/context-init` — bootstrap default folders
- `POST /v1/pm/projects/:id/context/import-repo-folder` — recursive repo import
- `POST /v1/pm/projects/:id/context/import-project-file` — OCR upload → PM doc

### Repo Access
- `GET /v1/pm/projects/:id/repo/tree` — list repo files
- `GET /v1/pm/projects/:id/repo/content` — read file content
