"""
Integration tests for the get_all_data.py script.
"""

import json
import subprocess
from pathlib import Path
import sys

# Add repo root to path
sys.path.insert(0, str(Path(__file__).parent.parent))

from scripts.get_all_data import print_json, print_users, print_issues


class TestGetAllDataIntegration:
    """Integration tests for get_all_data script."""

    def test_print_users(self):
        """Test printing users."""
        # Should not raise an exception
        print_users()

    def test_print_issues(self):
        """Test printing issues."""
        # Should not raise an exception
        print_issues()

    def test_print_json(self):
        """Test JSON output."""
        # Capture the output
        import io
        import sys as sys_module

        # Redirect stdout to capture output
        old_stdout = sys_module.stdout
        sys_module.stdout = io.StringIO()
        print_json()
        output = sys_module.stdout.getvalue()
        sys_module.stdout = old_stdout

        # Should be valid JSON
        data = json.loads(output)
        assert "users" in data
        assert "issues" in data

    def test_cli_users_only(self):
        """Test CLI with --users flag."""
        result = subprocess.run(
            ["python3", "scripts/get_all_data.py", "--users"],
            capture_output=True,
            text=True,
            cwd=Path(__file__).parent.parent,
        )

        assert result.returncode == 0
        assert "TEAM MEMBERS" in result.stdout

    def test_cli_issues_only(self):
        """Test CLI with --issues flag."""
        result = subprocess.run(
            ["python3", "scripts/get_all_data.py", "--issues"],
            capture_output=True,
            text=True,
            cwd=Path(__file__).parent.parent,
        )

        assert result.returncode == 0
        assert "ISSUES" in result.stdout

    def test_cli_json_output(self):
        """Test CLI with --json flag."""
        result = subprocess.run(
            ["python3", "scripts/get_all_data.py", "--json"],
            capture_output=True,
            text=True,
            cwd=Path(__file__).parent.parent,
        )

        assert result.returncode == 0
        data = json.loads(result.stdout)
        assert "users" in data
        assert "issues" in data
        assert len(data["users"]) > 0
        assert len(data["issues"]) > 0
