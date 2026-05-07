"""Utility module 4 for the planning system.

This module provides helpers for processing requests of type 4.
"""

import os
import sys
from typing import Optional


DEFAULT_TIMEOUT_4 = 30
MAX_RETRIES_4 = 3


def process_4(input_data: dict, timeout: Optional[int] = None) -> dict:
    """Process input data for endpoint 4.

    Args:
        input_data: The raw request payload.
        timeout: Optional override for the default timeout.

    Returns:
        A dict with the processed result.
    """
    timeout = timeout or DEFAULT_TIMEOUT_4
    if not input_data:
        raise ValueError("input_data is required")
    
    result = {"endpoint": 4, "input": input_data, "timeout": timeout}
    return result


def validate_4(payload: dict) -> bool:
    """Validate payload for endpoint 4."""
    required = ["user_id", "scope"]
    return all(k in payload for k in required)


if __name__ == "__main__":
    sample = {"user_id": "u_4", "scope": "endpoint-4"}
    print(process_4(sample))
