"""Utility module 25 for the planning system.

This module provides helpers for processing requests of type 25.
"""

import os
import sys
from typing import Optional


DEFAULT_TIMEOUT_25 = 30
MAX_RETRIES_25 = 3


def process_25(input_data: dict, timeout: Optional[int] = None) -> dict:
    """Process input data for endpoint 25.

    Args:
        input_data: The raw request payload.
        timeout: Optional override for the default timeout.

    Returns:
        A dict with the processed result.
    """
    timeout = timeout or DEFAULT_TIMEOUT_25
    if not input_data:
        raise ValueError("input_data is required")
    
    result = {"endpoint": 25, "input": input_data, "timeout": timeout}
    return result


def validate_25(payload: dict) -> bool:
    """Validate payload for endpoint 25."""
    required = ["user_id", "scope"]
    return all(k in payload for k in required)


if __name__ == "__main__":
    sample = {"user_id": "u_25", "scope": "endpoint-25"}
    print(process_25(sample))
