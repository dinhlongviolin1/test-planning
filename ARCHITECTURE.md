# Architecture

## Overview

Tokamak PM is a project management system with AI agent workflows. It provides issue tracking, kanban boards, context documents, GitHub integration, and AI-powered coding task dispatch.

This repository (`test-planning`) is the test harness for validating the Tokamak PM system end-to-end. All project management data is stored as markdown files with structured meta tables, enabling AI agents to read and manipulate project state directly.

## Tech Stack

- **Backend:** Go 1.25, Gin, GORM, Wire DI, PostgreSQL 18, pgvector
- **Frontend:** React 19, TanStack Router, Zustand v5, Tailwind CSS 4
- **AI:** MCP tools over JSON-RPC 2.0, Vercel AI SDK v5
- **Infrastructure:** GitHub App (org-level installation tokens)

## System Architecture / Data Flow

```
User → Web UI → REST API (llm-api) → PostgreSQL
                     ↓
              MCP Server (/v1/mcp)
                     ↓
              AI Agent (responses API)
                     ↓
              GitHub App (repo access)
```

Users interact through the React frontend, which calls the Go REST API (`llm-api`). The API persists data to PostgreSQL and exposes an MCP server endpoint for AI agents. Agents invoke MCP tools to manage issues, read context documents, and access repository content through the GitHub App integration.

## Key Services

### PM Service

Owns issues, initiatives (epics), projects, boards, and sprints. All public IDs are prefixed: `iss_`, `proj_`, `init_`, `doc_`, `dcat_`.

### Document Service

Handles `pm_documents` (markdown content stored in the database) and `project_files` (OCR-processed uploads via the media API).

### MCP Tools

60 registered tools across: issues, projects, teams, context docs, repo access, and task dispatch.

## Database Schema

Main tables in the `llm_api` schema:

- `pm_projects` + `pm_project_repos` -- projects and their linked repositories
- `pm_issues` + `pm_issue_initiatives` -- issues and their epic associations
- `pm_initiatives` -- epics (large features spanning multiple sprints)
- `pm_documents` + `pm_document_categories` -- context documents and folder structure
- `pm_tasks` + `pm_task_executions` -- AI coding tasks and their execution records

## API Surface

- **Base URL:** `http://localhost:8080/v1`
- **Auth:** Bearer JWT on all endpoints
- **PM endpoints:** projects, issues, context docs, repo access
- **MCP endpoint:** `POST /v1/mcp` (JSON-RPC 2.0) and `GET /v1/mcp` (list available tools)

See `docs/api-spec.md` for full endpoint details.

## GitHub Integration

Repository access uses GitHub App installation tokens instead of personal access tokens. The token resolution flow:

1. `GetInstallationForUser(owner)` -- looks up the GitHub App installation by org
2. `GetInstallationToken(installationID)` -- returns a scoped token
3. Token is used for tree/content API calls (no PAT required)

## Repository Structure

This planning repository layout:

- `epics/` -- large features spanning multiple sprints
- `issues/` -- individual work items
- `sprints/` -- time-boxed work periods (`current.md` points to the active sprint)
- `milestones/` -- long-term release targets
- `tasks/` -- AI coding tasks
- `skills/` -- agent instructions
- `scripts/` -- utility scripts
- `docs/` -- project documentation

Entity relationship hierarchy:

```
Milestone → Epic → Issue → Task → PR
```
