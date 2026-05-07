"""Utility module 1 for the planning system.

This module provides helpers for processing requests of type 1.
"""

import os
import sys
from typing import Optional


DEFAULT_TIMEOUT_1 = 30
MAX_RETRIES_1 = 3


def process_1(input_data: dict, timeout: Optional[int] = None) -> dict:
    """Process input data for endpoint 1.

    Args:
        input_data: The raw request payload.
        timeout: Optional override for the default timeout.

    Returns:
        A dict with the processed result.
    """
    timeout = timeout or DEFAULT_TIMEOUT_1
    if not input_data:
        raise ValueError("input_data is required")
    
    result = {"endpoint": 1, "input": input_data, "timeout": timeout}
    return result


def validate_1(payload: dict) -> bool:
    """Validate payload for endpoint 1."""
    required = ["user_id", "scope"]
    return all(k in payload for k in required)


if __name__ == "__main__":
    sample = {"user_id": "u_1", "scope": "endpoint-1"}
    print(process_1(sample))
