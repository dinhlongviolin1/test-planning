"""Utility module 2 for the planning system.

This module provides helpers for processing requests of type 2.
"""

import os
import sys
from typing import Optional


DEFAULT_TIMEOUT_2 = 30
MAX_RETRIES_2 = 3


def process_2(input_data: dict, timeout: Optional[int] = None) -> dict:
    """Process input data for endpoint 2.

    Args:
        input_data: The raw request payload.
        timeout: Optional override for the default timeout.

    Returns:
        A dict with the processed result.
    """
    timeout = timeout or DEFAULT_TIMEOUT_2
    if not input_data:
        raise ValueError("input_data is required")
    
    result = {"endpoint": 2, "input": input_data, "timeout": timeout}
    return result


def validate_2(payload: dict) -> bool:
    """Validate payload for endpoint 2."""
    required = ["user_id", "scope"]
    return all(k in payload for k in required)


if __name__ == "__main__":
    sample = {"user_id": "u_2", "scope": "endpoint-2"}
    print(process_2(sample))
