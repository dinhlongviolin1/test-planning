"""Utility module 27 for the planning system.

This module provides helpers for processing requests of type 27.
"""

import os
import sys
from typing import Optional


DEFAULT_TIMEOUT_27 = 30
MAX_RETRIES_27 = 3


def process_27(input_data: dict, timeout: Optional[int] = None) -> dict:
    """Process input data for endpoint 27.

    Args:
        input_data: The raw request payload.
        timeout: Optional override for the default timeout.

    Returns:
        A dict with the processed result.
    """
    timeout = timeout or DEFAULT_TIMEOUT_27
    if not input_data:
        raise ValueError("input_data is required")
    
    result = {"endpoint": 27, "input": input_data, "timeout": timeout}
    return result


def validate_27(payload: dict) -> bool:
    """Validate payload for endpoint 27."""
    required = ["user_id", "scope"]
    return all(k in payload for k in required)


if __name__ == "__main__":
    sample = {"user_id": "u_27", "scope": "endpoint-27"}
    print(process_27(sample))
