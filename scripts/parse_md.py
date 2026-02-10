#!/usr/bin/env python3
"""Parse markdown files to extract GitHub usernames and issue references."""

import re
from pathlib import Path


def find_markdown_files(root_dir: str = ".") -> list[Path]:
    """Recursively find all markdown files in the repository."""
    root = Path(root_dir)
    return list(root.rglob("*.md"))


def extract_usernames(content: str) -> set[str]:
    """Extract GitHub usernames (like @username) from content."""
    pattern = r'@([a-zA-Z0-9_-]+)'
    return set(re.findall(pattern, content))


def extract_issues(content: str) -> set[str]:
    """Extract issue references (like #123 or org/repo#123) from content."""
    # Pattern matches #123 or org/repo#123
    pattern = r'(?:^|[^\w/])(?:[a-zA-Z0-9_-]+/)?#(\d+)'
    matches = re.findall(pattern, content)
    # Reconstruct with prefix for org/repo cases - simplified approach
    result = set()
    for match in matches:
        # Need to get the org/repo prefix - re-scan for context
        org_pattern = r'([a-zA-Z0-9_-]+)/#' + str(match)
        org_match = re.search(org_pattern, content)
        if org_match:
            result.add(f"{org_match.group(1)}#{match}")
        else:
            result.add(f"#{match}")
    return result


def parse_markdown_files(files: list[Path]) -> tuple[dict[str, list[str]], dict[str, list[str]]]:
    """Parse markdown files and extract users and issues with their locations."""
    users = {}  # username -> list of files
    issues = {}  # issue -> list of files

    for filepath in files:
        try:
            content = filepath.read_text()
        except Exception:
            continue

        found_users = extract_usernames(content)
        found_issues = extract_issues(content)

        for user in found_users:
            users.setdefault(user, []).append(str(filepath))

        for issue in found_issues:
            issues.setdefault(issue, []).append(str(filepath))

    return users, issues


def print_report(users: dict[str, list[str]], issues: dict[str, list[str]]) -> None:
    """Print a formatted report of extracted users and issues."""
    print("=" * 60)
    print("GITHUB USERS AND ISSUE REFERENCES REPORT")
    print("=" * 60)

    print("\n## GitHub Users Found:")
    print("-" * 40)
    if users:
        for user in sorted(users.keys()):
            files = users[user]
            print(f"  @{user}")
            for f in files:
                print(f"    - {f}")
    else:
        print("  None found")

    print("\n## Issue References Found:")
    print("-" * 40)
    if issues:
        for issue in sorted(issues.keys(), key=lambda x: (x.split('#')[0] if '#' in x else x, x.split('#')[-1] if '#' in x else x)):
            files = issues[issue]
            print(f"  {issue}")
            for f in files:
                print(f"    - {f}")
    else:
        print("  None found")

    print("\n" + "=" * 60)
    print(f"Total unique users: {len(users)}")
    print(f"Total unique issues: {len(issues)}")
    print("=" * 60)


def main() -> None:
    """Main entry point."""
    root_dir = Path(__file__).parent.parent
    files = find_markdown_files(root_dir)
    users, issues = parse_markdown_files(files)
    print_report(users, issues)


if __name__ == "__main__":
    main()