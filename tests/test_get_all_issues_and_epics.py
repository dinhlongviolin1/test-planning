"""Tests for scripts/get_all_issues_and_epics.py"""

import json
import logging
import subprocess
import sys
from pathlib import Path

import pytest

# Add scripts/ to path so we can import the module
sys.path.insert(0, str(Path(__file__).resolve().parent.parent / "scripts"))

from get_all_issues_and_epics import (
    get_all_items,
    parse_markdown_file,
    parse_meta_table,
    parse_sections,
)

SAMPLE_ISSUE = """# Meta
| Field | Value |
|-------|-------|
| ID | i-test-001 |
| Status | todo |
| Created | 2026-01-30 |
| Updated | 2026-01-30 |
| Points | 5 |
| Assignee | @testuser |

## Title
Test issue title

## Description
Test description content.

## Linked Epics
- [e-001](e-001.md) - Test Epic

## Linked Sprint
- [s-001](s-001.md) - Sprint 1

## Linked Milestone
- [m-001](m-001.md) - Milestone 1

## Target Repo
user/test-repo

## Tasks
- [ ] Task one
- [ ] Task two

## Notes
Some notes here.
"""

SAMPLE_EPIC = """# Meta
| Field | Value |
|-------|-------|
| ID | e-test-001 |
| Status | active |
| Created | 2026-01-30 |
| Updated | 2026-01-30 |
| Owner | @testowner |

## Title
Test epic title

## Description
Test epic description.

## Related Issues
- [i-001](i-001.md) - Test Issue
"""


def _write_md(directory: Path, filename: str, content: str) -> Path:
    """Helper to write a markdown file into a directory."""
    directory.mkdir(parents=True, exist_ok=True)
    filepath = directory / filename
    filepath.write_text(content, encoding="utf-8")
    return filepath


class TestParseIssueMetaFields:
    def test_parse_issue_meta_fields(self, tmp_path: Path) -> None:
        filepath = _write_md(tmp_path, "i-test-001.md", SAMPLE_ISSUE)
        result = parse_markdown_file(filepath)

        assert result["id"] == "i-test-001"
        assert result["status"] == "todo"
        assert result["points"] == "5"
        assert result["assignee"] == "@testuser"
        assert result["created"] == "2026-01-30"
        assert result["updated"] == "2026-01-30"


class TestParseIssueSections:
    def test_parse_issue_sections(self, tmp_path: Path) -> None:
        filepath = _write_md(tmp_path, "i-test-001.md", SAMPLE_ISSUE)
        result = parse_markdown_file(filepath)

        assert result["title"] == "Test issue title"
        assert "Test description content." in result["description"]
        assert "e-001" in result["linked_epics"]
        assert "s-001" in result["linked_sprint"]
        assert "m-001" in result["linked_milestone"]
        assert result["target_repo"] == "user/test-repo"
        assert "Task one" in result["tasks"]
        assert "Task two" in result["tasks"]
        assert "Some notes here." in result["notes"]


class TestParseEpicMetaFields:
    def test_parse_epic_meta_fields(self, tmp_path: Path) -> None:
        filepath = _write_md(tmp_path, "e-test-001.md", SAMPLE_EPIC)
        result = parse_markdown_file(filepath)

        assert result["id"] == "e-test-001"
        assert result["status"] == "active"
        assert result["owner"] == "@testowner"
        assert result["created"] == "2026-01-30"
        assert result["updated"] == "2026-01-30"


class TestParseEpicSections:
    def test_parse_epic_sections(self, tmp_path: Path) -> None:
        filepath = _write_md(tmp_path, "e-test-001.md", SAMPLE_EPIC)
        result = parse_markdown_file(filepath)

        assert result["title"] == "Test epic title"
        assert "Test epic description." in result["description"]
        assert "i-001" in result["related_issues"]


class TestFilterByStatus:
    def test_filter_by_status(self, tmp_path: Path, monkeypatch: pytest.MonkeyPatch) -> None:
        issues_dir = tmp_path / "issues"
        _write_md(issues_dir, "i-001.md", SAMPLE_ISSUE)  # status=todo
        _write_md(
            issues_dir,
            "i-002.md",
            SAMPLE_ISSUE.replace("| Status | todo |", "| Status | done |"),
        )
        _write_md(
            issues_dir,
            "i-003.md",
            SAMPLE_ISSUE.replace("| Status | todo |", "| Status | todo |"),
        )

        monkeypatch.setattr(
            "get_all_issues_and_epics.get_repo_root", lambda: tmp_path
        )

        from get_all_issues_and_epics import main

        monkeypatch.setattr("sys.argv", ["prog", "--status", "todo"])

        import io

        captured = io.StringIO()
        monkeypatch.setattr("sys.stdout", captured)

        main()

        output = json.loads(captured.getvalue())
        assert len(output["issues"]) == 2
        for item in output["issues"]:
            assert item["status"] == "todo"


class TestFilterByStatusCaseInsensitive:
    def test_filter_by_status_case_insensitive(
        self, tmp_path: Path, monkeypatch: pytest.MonkeyPatch
    ) -> None:
        issues_dir = tmp_path / "issues"
        _write_md(issues_dir, "i-001.md", SAMPLE_ISSUE)  # status=todo

        monkeypatch.setattr(
            "get_all_issues_and_epics.get_repo_root", lambda: tmp_path
        )

        from get_all_issues_and_epics import main

        monkeypatch.setattr("sys.argv", ["prog", "--status", "TODO"])

        import io

        captured = io.StringIO()
        monkeypatch.setattr("sys.stdout", captured)

        main()

        output = json.loads(captured.getvalue())
        assert len(output["issues"]) == 1
        assert output["issues"][0]["status"] == "todo"


class TestEmptyDirectories:
    def test_empty_directories(self, tmp_path: Path, monkeypatch: pytest.MonkeyPatch) -> None:
        (tmp_path / "issues").mkdir()
        (tmp_path / "epics").mkdir()

        monkeypatch.setattr(
            "get_all_issues_and_epics.get_repo_root", lambda: tmp_path
        )

        from get_all_issues_and_epics import main

        monkeypatch.setattr("sys.argv", ["prog"])

        import io

        captured = io.StringIO()
        monkeypatch.setattr("sys.stdout", captured)

        main()

        output = json.loads(captured.getvalue())
        assert output == {"issues": [], "epics": []}


class TestMissingDirectories:
    def test_missing_directories(self, tmp_path: Path, monkeypatch: pytest.MonkeyPatch) -> None:
        monkeypatch.setattr(
            "get_all_issues_and_epics.get_repo_root", lambda: tmp_path
        )

        from get_all_issues_and_epics import main

        monkeypatch.setattr("sys.argv", ["prog"])

        import io

        captured = io.StringIO()
        monkeypatch.setattr("sys.stdout", captured)

        main()

        output = json.loads(captured.getvalue())
        assert output == {"issues": [], "epics": []}


class TestSkipIndexFiles:
    def test_skip_index_files(self, tmp_path: Path) -> None:
        issues_dir = tmp_path / "issues"
        _write_md(issues_dir, "_index.md", "# Index\nSome index content.")
        _write_md(issues_dir, "i-001.md", SAMPLE_ISSUE)

        items = get_all_items(issues_dir)

        assert len(items) == 1
        assert items[0]["id"] == "i-test-001"


class TestMalformedFileSkipped:
    def test_malformed_file_skipped(self, tmp_path: Path, caplog: pytest.LogCaptureFixture) -> None:
        issues_dir = tmp_path / "issues"
        _write_md(issues_dir, "bad.md", "# No Meta Table\nJust some text.")
        _write_md(issues_dir, "i-001.md", SAMPLE_ISSUE)

        with caplog.at_level(logging.WARNING):
            items = get_all_items(issues_dir)

        assert len(items) == 1
        assert items[0]["id"] == "i-test-001"
        assert any("Skipping" in record.message for record in caplog.records)


class TestJsonOutputStructure:
    def test_json_output_structure(self, tmp_path: Path, monkeypatch: pytest.MonkeyPatch) -> None:
        issues_dir = tmp_path / "issues"
        epics_dir = tmp_path / "epics"
        _write_md(issues_dir, "i-001.md", SAMPLE_ISSUE)
        _write_md(epics_dir, "e-001.md", SAMPLE_EPIC)

        monkeypatch.setattr(
            "get_all_issues_and_epics.get_repo_root", lambda: tmp_path
        )

        from get_all_issues_and_epics import main

        monkeypatch.setattr("sys.argv", ["prog"])

        import io

        captured = io.StringIO()
        monkeypatch.setattr("sys.stdout", captured)

        main()

        output = json.loads(captured.getvalue())
        assert "issues" in output
        assert "epics" in output
        assert isinstance(output["issues"], list)
        assert isinstance(output["epics"], list)
        assert len(output["issues"]) == 1
        assert len(output["epics"]) == 1


class TestScriptSubprocessExitCode:
    def test_script_subprocess_exit_code(self) -> None:
        script_path = Path(__file__).resolve().parent.parent / "scripts" / "get_all_issues_and_epics.py"
        result = subprocess.run(
            [sys.executable, str(script_path)],
            capture_output=True,
            text=True,
        )
        assert result.returncode == 0

        output = json.loads(result.stdout)
        assert "issues" in output
        assert "epics" in output
        assert isinstance(output["issues"], list)
        assert isinstance(output["epics"], list)
