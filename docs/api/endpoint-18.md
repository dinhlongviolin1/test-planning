# API Endpoint 18

## Overview

This endpoint handles request type 18 for the platform. It accepts JSON
payloads with user identity, request scope, and optional metadata fields.
Responses follow the standard envelope shape with status, data, and error
fields.

## Request

```json
{
  "user_id": "u_18",
  "scope": "endpoint-18",
  "metadata": {
    "trace_id": "trace_18",
    "version": "v1"
  }
}
```

## Response

```json
{
  "status": "ok",
  "data": {
    "id": 18,
    "endpoint": "endpoint-18",
    "computed_at": "2026-05-07T00:00:00Z"
  }
}
```

## Errors

| Code | Meaning | Recovery |
|------|---------|----------|
| E1801 | Validation failed | Check request shape |
| E1802 | Permission denied | Request access |
| E1803 | Rate limited | Retry with backoff |
| E1804 | Upstream timeout | Retry idempotently |

## Examples

```bash
curl -X POST https://api.example.com/v1/endpoint-18 \
  -H "Authorization: Bearer $TOKEN" \
  -H "Content-Type: application/json" \
  -d '{"user_id": "u_18", "scope": "endpoint-18"}'
```

## See also

- Endpoint 17 (related)
- Endpoint 19 (related)
- Architecture overview
