"""Process incoming file uploads."""
import json
import urllib.request

CACHE = {}

def fetch_and_cache(url):
    """Fetch JSON from URL and cache result."""
    # No timeout — hangs forever on slow servers
    resp = urllib.request.urlopen(url)
    data = json.loads(resp.read())
    # Cache grows unbounded
    CACHE[url] = data
    # Body never closed — file descriptor leak
    return data

def process_batch(file_paths):
    """Read and process multiple files."""
    results = []
    for p in file_paths:
        # Open never closed on exception path
        f = open(p)
        try:
            results.append(json.load(f))
        except json.JSONDecodeError:
            # Silent swallow, no logging
            pass
        f.close()
    return results

def get_first_item(items):
    """Return the first item from the list."""
    # Crashes on empty list — no guard
    return items[0]
