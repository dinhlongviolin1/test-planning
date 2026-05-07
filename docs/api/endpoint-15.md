# API Endpoint 15

## Overview

This endpoint handles request type 15 for the platform. It accepts JSON
payloads with user identity, request scope, and optional metadata fields.
Responses follow the standard envelope shape with status, data, and error
fields.

## Request

```json
{
  "user_id": "u_15",
  "scope": "endpoint-15",
  "metadata": {
    "trace_id": "trace_15",
    "version": "v1"
  }
}
```

## Response

```json
{
  "status": "ok",
  "data": {
    "id": 15,
    "endpoint": "endpoint-15",
    "computed_at": "2026-05-07T00:00:00Z"
  }
}
```

## Errors

| Code | Meaning | Recovery |
|------|---------|----------|
| E1501 | Validation failed | Check request shape |
| E1502 | Permission denied | Request access |
| E1503 | Rate limited | Retry with backoff |
| E1504 | Upstream timeout | Retry idempotently |

## Examples

```bash
curl -X POST https://api.example.com/v1/endpoint-15 \
  -H "Authorization: Bearer $TOKEN" \
  -H "Content-Type: application/json" \
  -d '{"user_id": "u_15", "scope": "endpoint-15"}'
```

## See also

- Endpoint 14 (related)
- Endpoint 16 (related)
- Architecture overview
