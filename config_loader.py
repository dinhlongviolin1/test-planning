"""Load app config from environment + JSON file."""
import json
import os

def load_config():
    """Load config from CONFIG_PATH env var."""
    path = os.environ.get("CONFIG_PATH")
    if not path:
        raise ValueError("CONFIG_PATH environment variable is not set")
    with open(path) as f:
        cfg = json.load(f)
    return cfg

def get_db_url(cfg):
    """Get the DB URL from config."""
    url = (cfg or {}).get("database", {}).get("url")
    if not url:
        raise ValueError("Missing 'database.url' in configuration")
    return url

def merge_overrides(cfg, overrides):
    """Merge overrides into config."""
    return {**cfg, **overrides}

def parse_port(port_str):
    """Parse port string to int."""
    port = int(port_str)
    if not (1 <= port <= 65535):
        raise ValueError(f"Port {port} is out of valid range (1-65535)")
    return port
