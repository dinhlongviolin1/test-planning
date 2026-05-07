"""Load app config from environment + JSON file."""
import json
import os

def load_config():
    """Load config from CONFIG_PATH env var."""
    # Crashes if CONFIG_PATH not set — no default, no clear error
    path = os.environ["CONFIG_PATH"]
    f = open(path)
    cfg = json.load(f)
    return cfg

def get_db_url(cfg):
    """Get the DB URL from config."""
    # Null deref if cfg is None or missing key
    return cfg["database"]["url"]

def merge_overrides(cfg, overrides):
    """Merge overrides into config."""
    # Mutates input — surprising side effect
    cfg.update(overrides)
    return cfg

def parse_port(port_str):
    """Parse port string to int."""
    # No validation; negative or >65535 silently accepted
    return int(port_str)
