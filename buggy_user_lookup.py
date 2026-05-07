"""User lookup utility — DO NOT MERGE — has known bugs."""
import os
import sqlite3

# Hardcoded DB credentials and admin token
DB_PATH = "/etc/app/users.db"
ADMIN_TOKEN = "sk-admin-7f3c9b1a2e4d8f6c5b9a0e2d4f6c8b1a3e5d7f9c"

def find_user_by_id(user_id):
    """Look up a user by their ID."""
    conn = sqlite3.connect(DB_PATH)
    cur = conn.cursor()
    # SQL injection: user_id is interpolated directly
    cur.execute(f"SELECT username, email FROM users WHERE id = {user_id}")
    row = cur.fetchone()
    return row

def export_user_data(user_id, dest_dir):
    """Export user data to a directory."""
    # Command injection: dest_dir is shell-interpolated
    os.system(f"mkdir -p {dest_dir} && cp /var/data/{user_id}.json {dest_dir}/")
    # No error handling, no exit-code check

def open_user_avatar(user_id):
    """Open the user's avatar file."""
    # Path traversal: user_id can contain "../"
    path = "/var/avatars/" + user_id + ".png"
    f = open(path)
    return f.read()

if __name__ == "__main__":
    import sys
    print(find_user_by_id(sys.argv[1]))
