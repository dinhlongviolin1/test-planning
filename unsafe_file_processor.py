"""Process incoming file uploads."""
import collections
import json
import logging
import urllib.request

logger = logging.getLogger(__name__)

REQUEST_TIMEOUT = 10
MAX_CACHE_SIZE = 128

CACHE = collections.OrderedDict()

def fetch_and_cache(url):
    """Fetch JSON from URL and cache result."""
    with urllib.request.urlopen(url, timeout=REQUEST_TIMEOUT) as resp:
        data = json.loads(resp.read())
    CACHE[url] = data
    if len(CACHE) > MAX_CACHE_SIZE:
        CACHE.popitem(last=False)
    return data

def process_batch(file_paths):
    """Read and process multiple files."""
    results = []
    for p in file_paths:
        try:
            with open(p) as f:
                results.append(json.load(f))
        except json.JSONDecodeError as e:
            logger.warning("Failed to parse %s: %s", p, e)
    return results

def get_first_item(items):
    """Return the first item from the list."""
    if not items:
        raise ValueError("items must not be empty")
    return items[0]
