"""User lookup utility."""
import os
import re
import shutil
import sqlite3
from pathlib import Path

DB_PATH = os.environ["DB_PATH"]
ADMIN_TOKEN = os.environ["ADMIN_TOKEN"]

def find_user_by_id(user_id):
    """Look up a user by their ID."""
    conn = sqlite3.connect(DB_PATH)
    try:
        cur = conn.cursor()
        cur.execute("SELECT username, email FROM users WHERE id = ?", (user_id,))
        return cur.fetchone()
    finally:
        conn.close()

def export_user_data(user_id, dest_dir):
    """Export user data to a directory."""
    if not re.fullmatch(r'[A-Za-z0-9_-]+', user_id):
        raise ValueError("Invalid user ID")
    source = Path("/var/data") / f"{user_id}.json"
    if not source.resolve().is_relative_to(Path("/var/data").resolve()):
        raise ValueError("Invalid source path")
    export_base = Path(os.environ.get("EXPORT_DIR", "/var/exports"))
    dest = Path(dest_dir).resolve()
    if not dest.is_relative_to(export_base.resolve()):
        raise ValueError("Invalid destination path")
    os.makedirs(dest, exist_ok=True)
    shutil.copy(source, dest)

def open_user_avatar(user_id):
    """Open the user's avatar file."""
    if not re.fullmatch(r'[A-Za-z0-9_-]+', user_id):
        raise ValueError("Invalid user ID")
    path = Path("/var/avatars") / f"{user_id}.png"
    if not path.resolve().is_relative_to(Path("/var/avatars").resolve()):
        raise ValueError("Invalid avatar path")
    with open(path, "rb") as f:
        return f.read()

if __name__ == "__main__":
    import sys
    print(find_user_by_id(sys.argv[1]))
