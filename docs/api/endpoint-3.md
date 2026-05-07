# API Endpoint 3

## Overview

This endpoint handles request type 3 for the platform. It accepts JSON
payloads with user identity, request scope, and optional metadata fields.
Responses follow the standard envelope shape with status, data, and error
fields.

## Request

```json
{
  "user_id": "u_3",
  "scope": "endpoint-3",
  "metadata": {
    "trace_id": "trace_3",
    "version": "v1"
  }
}
```

## Response

```json
{
  "status": "ok",
  "data": {
    "id": 3,
    "endpoint": "endpoint-3",
    "computed_at": "2026-05-07T00:00:00Z"
  }
}
```

## Errors

| Code | Meaning | Recovery |
|------|---------|----------|
| E301 | Validation failed | Check request shape |
| E302 | Permission denied | Request access |
| E303 | Rate limited | Retry with backoff |
| E304 | Upstream timeout | Retry idempotently |

## Examples

```bash
curl -X POST https://api.example.com/v1/endpoint-3 \
  -H "Authorization: Bearer $TOKEN" \
  -H "Content-Type: application/json" \
  -d '{"user_id": "u_3", "scope": "endpoint-3"}'
```

## See also

- Endpoint 2 (related)
- Endpoint 4 (related)
- Architecture overview
