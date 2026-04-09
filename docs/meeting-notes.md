# Meeting Notes

## 2026-04-09 — Context Sync Review

**Attendees:** Long, Han, Ashley

### Discussed

- Project context page revamp shipped (PR #347 by Han)
- AI MCP tools for context now include: `pm_context_read_index`, `pm_context_init`, `pm_context_restructure`, folder CRUD, repo browsing
- Tiptap JSON → Markdown migration added as goose migration `000123`
- Background polling (5s) added to context page for live AI updates

### Decisions

1. Keep OCR uploads as `project_files` (separate from PM docs) — use "Add to Context" button to convert
2. Repo import only supports text files for now; PDFs in repo require separate upload flow
3. `pm_docs_*` tools renamed to `pm_context_*` for clarity

### Action Items

- [ ] Long: test full import flow with `test-planning` repo
- [ ] Han: review placeholder text in empty doc state
- [ ] Ashley: verify Slack `pm_context_*` tool classification

## 2026-04-07 — Kickoff

**Attendees:** Long, Han

### Goals set

- Ship multi-repo project support before end of sprint
- Context sync to be AI-readable by next week
- Sidebar to show repos under active project when on issue view
