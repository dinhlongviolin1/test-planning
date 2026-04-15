"""
Tests for get_all_issues_and_epics.py
"""

import json
import os
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path
from unittest.mock import patch

# Ensure the scripts directory is importable
sys.path.insert(0, str(Path(__file__).resolve().parent))

from get_all_issues_and_epics import (
    parse_meta_table,
    parse_sections,
    parse_markdown_file,
    get_all_items,
)


SAMPLE_ISSUE = """\
# Meta
| Field | Value |
|-------|-------|
| ID | i-001 |
| Status | todo |
| Created | 2026-01-30 |
| Updated | 2026-01-30 |
| Points | 5 |
| Assignee | @alice |

## Title
Design database architecture

## Description
Design and document the database architecture.

## Linked Epics
- [e-001](e-001.md) - Create 300b Model

## Linked Sprint
- [s-001](s-001.md) - Sprint 1

## Linked Milestone
- [m-001](m-001.md) - Q1 Release

## Target Repo
owner/test-repo

## Tasks
- [ ] Analyze data patterns
- [x] Design schema
- [ ] Define indexing strategy

## Notes
Critical path item.
"""

SAMPLE_EPIC = """\
# Meta
| Field | Value |
|-------|-------|
| ID | e-001 |
| Status | active |
| Created | 2026-01-30 |
| Updated | 2026-01-30 |
| Owner | @bob |

## Title
Create 300b Model

## Description
Development of a 300 billion parameter model.

## Related Issues
- [i-001](i-001.md) - Design database architecture
"""


class TestParseMetaTable(unittest.TestCase):

    def test_parse_meta_table(self):
        meta = parse_meta_table(SAMPLE_ISSUE)
        self.assertEqual(meta['ID'], 'i-001')
        self.assertEqual(meta['Status'], 'todo')
        self.assertEqual(meta['Created'], '2026-01-30')
        self.assertEqual(meta['Updated'], '2026-01-30')
        self.assertEqual(meta['Points'], '5')
        self.assertEqual(meta['Assignee'], '@alice')

    def test_parse_meta_table_empty(self):
        content = "## Title\nSome title\n\n## Description\nSome description"
        meta = parse_meta_table(content)
        self.assertEqual(meta, {})

    def test_parse_meta_table_double_hash(self):
        content = "## Meta\n| Field | Value |\n|---|---|\n| ID | e-018 |\n| Status | active |\n"
        meta = parse_meta_table(content)
        self.assertEqual(meta['ID'], 'e-018')
        self.assertEqual(meta['Status'], 'active')


class TestParseSections(unittest.TestCase):

    def test_parse_sections_with_tasks(self):
        sections = parse_sections(SAMPLE_ISSUE)
        tasks = sections['tasks']
        self.assertEqual(len(tasks), 3)
        self.assertEqual(tasks[0], {"task": "Analyze data patterns", "done": False})
        self.assertEqual(tasks[1], {"task": "Design schema", "done": True})
        self.assertEqual(tasks[2], {"task": "Define indexing strategy", "done": False})

    def test_parse_sections_with_links(self):
        sections = parse_sections(SAMPLE_ISSUE)
        linked_epics = sections['linked_epics']
        self.assertEqual(len(linked_epics), 1)
        self.assertEqual(linked_epics[0]['id'], 'e-001')
        self.assertEqual(linked_epics[0]['link'], 'e-001.md')
        self.assertEqual(linked_epics[0]['description'], 'Create 300b Model')

        # Related Issues from epic
        sections_epic = parse_sections(SAMPLE_EPIC)
        related = sections_epic['related_issues']
        self.assertEqual(len(related), 1)
        self.assertEqual(related[0]['id'], 'i-001')

    def test_parse_sections_title_and_description(self):
        sections = parse_sections(SAMPLE_ISSUE)
        self.assertEqual(sections['title'], 'Design database architecture')
        self.assertEqual(sections['description'], 'Design and document the database architecture.')

    def test_parse_sections_linked_sprint_none(self):
        content = "## Linked Sprint\n- None\n"
        sections = parse_sections(content)
        self.assertEqual(sections['linked_sprint'], [])

    def test_parse_sections_target_repo(self):
        sections = parse_sections(SAMPLE_ISSUE)
        self.assertEqual(sections['target_repo'], 'owner/test-repo')

    def test_parse_sections_notes(self):
        sections = parse_sections(SAMPLE_ISSUE)
        self.assertEqual(sections['notes'], 'Critical path item.')


class TestParseMarkdownFile(unittest.TestCase):

    def test_parse_markdown_file(self):
        with tempfile.NamedTemporaryFile(mode='w', suffix='.md', delete=False) as f:
            f.write(SAMPLE_ISSUE)
            f.flush()
            tmp_path = Path(f.name)

        try:
            result = parse_markdown_file(tmp_path)
            # Meta fields (lowercased keys)
            self.assertEqual(result['id'], 'i-001')
            self.assertEqual(result['status'], 'todo')
            self.assertEqual(result['points'], '5')
            self.assertEqual(result['assignee'], '@alice')
            # Sections
            self.assertEqual(result['title'], 'Design database architecture')
            self.assertIsInstance(result['tasks'], list)
            self.assertEqual(len(result['tasks']), 3)
            self.assertIsInstance(result['linked_epics'], list)
            self.assertEqual(result['_source_file'], tmp_path.name)
        finally:
            os.unlink(tmp_path)


class TestGetAllItems(unittest.TestCase):

    def _create_md_file(self, tmpdir, name, status):
        content = (
            f"# Meta\n"
            f"| Field | Value |\n"
            f"|-------|-------|\n"
            f"| ID | {name.replace('.md', '')} |\n"
            f"| Status | {status} |\n\n"
            f"## Title\nTest item {name}\n\n"
            f"## Description\nA test item.\n"
        )
        filepath = os.path.join(tmpdir, name)
        with open(filepath, 'w') as f:
            f.write(content)

    def test_get_all_items_with_status_filter(self):
        with tempfile.TemporaryDirectory() as tmpdir:
            self._create_md_file(tmpdir, 'i-001.md', 'todo')
            self._create_md_file(tmpdir, 'i-002.md', 'in_progress')
            self._create_md_file(tmpdir, 'i-003.md', 'todo')

            with patch('get_all_issues_and_epics.get_repo_root', return_value=Path(tmpdir).parent):
                dirname = Path(tmpdir).name
                # Case-insensitive: 'TODO' should match 'todo'
                items = get_all_items(dirname, status_filter='TODO')
                self.assertEqual(len(items), 2)
                for item in items:
                    self.assertEqual(item['status'].lower(), 'todo')

    def test_get_all_items_empty_directory(self):
        with tempfile.TemporaryDirectory() as tmpdir:
            with patch('get_all_issues_and_epics.get_repo_root', return_value=Path(tmpdir).parent):
                dirname = Path(tmpdir).name
                items = get_all_items(dirname)
                self.assertEqual(items, [])

    def test_get_all_items_nonexistent_directory(self):
        with tempfile.TemporaryDirectory() as tmpdir:
            with patch('get_all_issues_and_epics.get_repo_root', return_value=Path(tmpdir)):
                items = get_all_items('nonexistent_dir')
                self.assertEqual(items, [])

    def test_get_all_items_skips_index(self):
        with tempfile.TemporaryDirectory() as tmpdir:
            # Create _index.md and a real data file
            with open(os.path.join(tmpdir, '_index.md'), 'w') as f:
                f.write("# Index\nThis is an index file.\n")
            self._create_md_file(tmpdir, 'i-001.md', 'todo')

            with patch('get_all_issues_and_epics.get_repo_root', return_value=Path(tmpdir).parent):
                dirname = Path(tmpdir).name
                items = get_all_items(dirname)
                self.assertEqual(len(items), 1)
                self.assertEqual(items[0]['id'], 'i-001')

    def test_get_all_items_skips_malformed(self):
        with tempfile.TemporaryDirectory() as tmpdir:
            # Create a valid file
            self._create_md_file(tmpdir, 'i-001.md', 'todo')
            # Create a malformed file that will cause a parse error
            malformed_path = os.path.join(tmpdir, 'i-002.md')
            with open(malformed_path, 'wb') as f:
                f.write(b'\x80\x81\x82')  # Invalid UTF-8

            with patch('get_all_issues_and_epics.get_repo_root', return_value=Path(tmpdir).parent):
                dirname = Path(tmpdir).name
                items = get_all_items(dirname)
                # Should still get the valid file
                self.assertEqual(len(items), 1)
                self.assertEqual(items[0]['id'], 'i-001')


class TestCLI(unittest.TestCase):

    def _run_script(self, *extra_args):
        script = str(Path(__file__).resolve().parent / 'get_all_issues_and_epics.py')
        cmd = [sys.executable, script] + list(extra_args)
        result = subprocess.run(cmd, capture_output=True, text=True, timeout=30)
        return result

    def test_cli_output_structure(self):
        result = self._run_script()
        self.assertEqual(result.returncode, 0)
        data = json.loads(result.stdout)
        self.assertIn('issues', data)
        self.assertIn('epics', data)
        self.assertIsInstance(data['issues'], list)
        self.assertIsInstance(data['epics'], list)
        # Should have 12 issues and 18 epics from real data
        self.assertEqual(len(data['issues']), 12)
        self.assertEqual(len(data['epics']), 18)

    def test_cli_status_filter(self):
        result = self._run_script('--status', 'todo')
        self.assertEqual(result.returncode, 0)
        data = json.loads(result.stdout)
        # All returned issues should have status 'todo'
        for issue in data['issues']:
            self.assertEqual(issue['status'].lower(), 'todo')
        # Epics don't have 'todo' status, so should be empty
        self.assertEqual(len(data['epics']), 0)

    def test_cli_status_filter_active(self):
        result = self._run_script('-s', 'active')
        self.assertEqual(result.returncode, 0)
        data = json.loads(result.stdout)
        # All returned epics should have status 'active'
        for epic in data['epics']:
            self.assertEqual(epic['status'].lower(), 'active')
        # Issues don't have 'active' status, so should be empty
        self.assertEqual(len(data['issues']), 0)


if __name__ == '__main__':
    unittest.main()
