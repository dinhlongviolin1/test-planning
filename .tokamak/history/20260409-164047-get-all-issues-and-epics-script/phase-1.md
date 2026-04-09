# Implement Get All Issues and Epics Script (phase-1)

**Date**: 2026-04-09

## Task 1.1: Create the Python script scripts/get_all_issues_and_epics.py that reads markdown files from issues/ and epics/ directories, parses the Meta table format, extracts ALL fields (ID, Status, Title, Description, Points, Assignee, Linked Epics, Linked Sprint, Linked Milestone, Target Repo, Tasks, Notes, Created, Updated, etc.), supports --status/-s CLI argument for case-insensitive status filtering, outputs JSON to stdout with structure {"issues": [...], "epics": [...]}, handles empty directories gracefully, skips files with malformed metadata and logs warnings, and uses exit code 0 on success, non-zero on errors. Follow the coding patterns from scripts/get_team_members.py: use dataclasses for data representation, Path for file handling, argparse for CLI, and standard libraries (os, re, json, argparse). See issues/i-001.md and i-002.md for the exact markdown table format with fields: ID, Status, Created, Updated, Points, Assignee. See epics/e-001.md for epics format with fields: ID, Status, Created, Updated. For both, also parse sections like Title, Description, Linked Epics, Linked Sprint, Linked Milestone, Target Repo, Tasks, Notes, Related Issues as key-value lists or strings.
**Status**: in_progress
**Summary**: Task completed.

## Task 1.qa.1: Fix QA issues in phase Implement Get All Issues and Epics Script
**Status**: in_progress
**Summary**: Task completed.
