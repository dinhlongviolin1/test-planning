# API Endpoint 28

## Overview

This endpoint handles request type 28 for the platform. It accepts JSON
payloads with user identity, request scope, and optional metadata fields.
Responses follow the standard envelope shape with status, data, and error
fields.

## Request

```json
{
  "user_id": "u_28",
  "scope": "endpoint-28",
  "metadata": {
    "trace_id": "trace_28",
    "version": "v1"
  }
}
```

## Response

```json
{
  "status": "ok",
  "data": {
    "id": 28,
    "endpoint": "endpoint-28",
    "computed_at": "2026-05-07T00:00:00Z"
  }
}
```

## Errors

| Code | Meaning | Recovery |
|------|---------|----------|
| E2801 | Validation failed | Check request shape |
| E2802 | Permission denied | Request access |
| E2803 | Rate limited | Retry with backoff |
| E2804 | Upstream timeout | Retry idempotently |

## Examples

```bash
curl -X POST https://api.example.com/v1/endpoint-28 \
  -H "Authorization: Bearer $TOKEN" \
  -H "Content-Type: application/json" \
  -d '{"user_id": "u_28", "scope": "endpoint-28"}'
```

## See also

- Endpoint 27 (related)
- Endpoint 29 (related)
- Architecture overview
