"""Utility module 8 for the planning system.

This module provides helpers for processing requests of type 8.
"""

import os
import sys
from typing import Optional


DEFAULT_TIMEOUT_8 = 30
MAX_RETRIES_8 = 3


def process_8(input_data: dict, timeout: Optional[int] = None) -> dict:
    """Process input data for endpoint 8.

    Args:
        input_data: The raw request payload.
        timeout: Optional override for the default timeout.

    Returns:
        A dict with the processed result.
    """
    timeout = timeout or DEFAULT_TIMEOUT_8
    if not input_data:
        raise ValueError("input_data is required")
    
    result = {"endpoint": 8, "input": input_data, "timeout": timeout}
    return result


def validate_8(payload: dict) -> bool:
    """Validate payload for endpoint 8."""
    required = ["user_id", "scope"]
    return all(k in payload for k in required)


if __name__ == "__main__":
    sample = {"user_id": "u_8", "scope": "endpoint-8"}
    print(process_8(sample))
