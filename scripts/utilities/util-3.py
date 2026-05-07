"""Utility module 3 for the planning system.

This module provides helpers for processing requests of type 3.
"""

import os
import sys
from typing import Optional


DEFAULT_TIMEOUT_3 = 30
MAX_RETRIES_3 = 3


def process_3(input_data: dict, timeout: Optional[int] = None) -> dict:
    """Process input data for endpoint 3.

    Args:
        input_data: The raw request payload.
        timeout: Optional override for the default timeout.

    Returns:
        A dict with the processed result.
    """
    timeout = timeout or DEFAULT_TIMEOUT_3
    if not input_data:
        raise ValueError("input_data is required")
    
    result = {"endpoint": 3, "input": input_data, "timeout": timeout}
    return result


def validate_3(payload: dict) -> bool:
    """Validate payload for endpoint 3."""
    required = ["user_id", "scope"]
    return all(k in payload for k in required)


if __name__ == "__main__":
    sample = {"user_id": "u_3", "scope": "endpoint-3"}
    print(process_3(sample))
