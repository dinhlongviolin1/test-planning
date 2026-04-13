# SOUL.md — Project Purpose & Principles

## Purpose

This project serves as a **test harness** for validating the Tokamak PM system end-to-end. It verifies that the core PM functionalities work correctly before deploying to production.

## Goals

From `docs/overview.md`:
- Verify issue creation, assignment, and status transitions across multiple repos
- Test project context doc syncing (AI reads, writes, restructures)
- Validate GitHub App installation token resolution for repo browsing
- Confirm sidebar repo navigation filters issues correctly

## Scope

| Area | Status |
|------|--------|
| Issue tracking | In progress |
| Kanban board | Active |
| Context docs | Testing |
| AI agent dispatch | Planned |
| GitHub import | Testing |

## Team

From `team.md`:
- **Long** — project lead, full-stack
- **Han** — UX / frontend
- **Ashley** — AI tooling / backend

## Guiding Principles

1. **Test-first validation** — verify functionality before assuming it works
2. **End-to-end coverage** — test full user flows, not just unit logic
3. **Clear test artifacts** — each test should be self-documenting
4. **Reproducible results** — tests must pass consistently

## Architecture

Reference: `docs/architecture.md`

The test harness validates:
- REST API layer (llm-api)
- MCP Server (`/v1/mcp`)
- AI Agent integration (responses API)
- GitHub App integration (installation tokens)

## Timeline

- Week 1: Core PM flows
- Week 2: Context sync + AI integration
- Week 3: Repo import + OCR pipeline