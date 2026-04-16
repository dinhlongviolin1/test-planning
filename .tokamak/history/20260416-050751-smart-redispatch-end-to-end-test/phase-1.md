# Research smart-redispatch feature (phase-1)

**Date**: 2026-04-16

## What is "smart-redispatch"?

**Finding: NOT FOUND in codebase.**

The term "smart-redispatch" appears only in:
- The history directory name itself (`.tokamak/history/20260416-050751-smart-redispatch-end-to-end-test/`)
- The run metadata file (`.tokamak/history/20260416-050751-smart-redispatch-end-to-end-test/run.md`)
- The EPSI-20 history entry referencing a new request for "smart-redispatch end-to-end test"

There is **no feature definition, spec, or documentation** for "smart-redispatch" anywhere in:
- `docs/overview.md` — lists AI agent dispatch as "Planned" only
- `docs/architecture.md` — describes AI agent workflows and task dispatch, but no "smart-redispatch"
- `docs/api-spec.md` — MCP tools for dispatch (task dispatch), no smart-redispatch endpoint
- `agents.md` — describes agent spawning and dispatch, no smart-redispatch concept
- `skills/coding/` — coding conventions, no mention

### Broader "dispatch" context

The repo documents **task dispatch** as a core concept:
- `agents.md`: "The agent commits all changes to git... Code changes are dispatched to target repositories via coding tasks -- never modify code directly in this planning repo."
- `ARCHITECTURE.md`: MCP tools for "task dispatch" (60 registered tools)
- `docs/overview.md`: "AI agent dispatch | Planned"

The "smart-redispatch" task may refer to an advanced/redispatch mode for the task dispatch system — but no such feature exists in the current codebase. This run may be a **placeholder/validation run** to test end-to-end workflows.

## Existing Test Patterns

### Test conventions (`skills/coding/testing.md`)

- **Unit tests**: describe/it structure (Jest-style)
- **Minimum 80% coverage**, 100% for critical paths
- **Mocking**: use mocks for external services, factories for test data, never mock what you don't own
- **Integration tests**: test API endpoints end-to-end with a reset test database
- **Test error scenarios**

### Actual test coverage in repo

**No test files exist.** The repo has:
- Python utility scripts in `scripts/` (not tests)
- No `.test.` or `_test.` files
- No Jest, pytest, or other test framework configuration

### Scripts as patterns

`scripts/get_all_issues_and_epics.py` is a reference implementation showing:
- Markdown meta table parsing (`parse_meta_table`)
- Section parsing (`parse_sections`)
- Data classes for issues/epics/agents (`Issue`, `Epic`, `Agent`)
- JSON serialization (`to_dict`)
- Command-line interface with `argparse`

## Task File Structure (`tasks/t-001.md`)

A task file contains:

```
## Meta
| Field | Value |
|-------|-------|
| ID | t-XXX |
| Status | pending |
| Created | YYYY-MM-DD |
| Updated | YYYY-MM-DD |
| Issue | - |
| Priority | medium |
| Complexity | 1 |

## Context
[Description of what the task entails]

## [Additional sections]
[Requirements, Implementation Notes, Expected Output, etc.]

## Definition of Done
- [ ] Checklist items
```

### Valid task statuses
`pending`, `queued`, `running`, `completed`, `failed`, `cancelled`

## Tasks Directory State

From `tasks/_index.md`:
- **NEXT_ID: 2**
- Only existing task: `t-001` (pending)

## Execution History Context

From `HISTORY.md` (EPSI-20):
- Prior runs focused on license additions (MIT → Apache 2.0)
- The current run (Run 7) was triggered by a new request: "verification: smart-redispatch end-to-end test"
- The run appears to be a **validation test** of the end-to-end workflow, not a feature implementation

## Summary

| Item | Finding |
|------|---------|
| What is smart-redispatch? | Not found in codebase — likely a placeholder/validation run name |
| Test patterns | Described in `skills/coding/testing.md` (Jest-style), no actual test files |
| Task file structure | Documented above from `t-001.md` |
| Existing coverage of smart-redispatch | None — feature does not exist in code |
| NEXT_ID for tasks/ | **2** |
| Scripts pattern | Python utilities with `parse_meta_table`, dataclasses, argparse |
## Task 1.1: Research smart-redispatch feature and document findings
**Status**: in_progress
**Summary**: Researched the smart-redispatch feature and documented findings in phase-1.md. The term "smart-redispatch" does not exist in the codebase — it appears only in the history/run directory names. The broader "dispatch" concept refers to the AI task dispatch system (spawning coding agents to target repos). No actual test files exist in the repo; test conventions are documented in `skills/coding/testing.md` (Jest-style). Task files use a markdown meta table structure with fields like ID, Status, Prior
