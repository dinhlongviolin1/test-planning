# Contributing

Thanks for your interest in contributing to test-planning. This document
captures the small set of conventions we follow.

## Workflow

1. Create a feature branch off `main`. Use a short, descriptive name —
   `docs/<topic>` for documentation, `feat/<topic>` for new content,
   `fix/<topic>` for corrections.
2. Make your change. Keep commits small and atomic; one logical change
   per commit.
3. Open a pull request against `main`. Fill in the description with
   what changed and why.
4. Address review feedback before merging.

## Style

- Markdown files use ATX-style headings (`#`, `##`, `###`).
- Wrap prose at 80 columns when possible; tables and code blocks may
  exceed that limit.
- Python files (in `scripts/` and `team_members.py`) follow PEP 8 and
  use type hints.

## Reporting issues

Open an issue under `issues/` describing the problem, expected behaviour,
and reproduction steps if applicable.
