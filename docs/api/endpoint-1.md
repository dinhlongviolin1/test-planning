# API Endpoint 1

## Overview

This endpoint handles request type 1 for the platform. It accepts JSON
payloads with user identity, request scope, and optional metadata fields.
Responses follow the standard envelope shape with status, data, and error
fields.

## Request

```json
{
  "user_id": "u_1",
  "scope": "endpoint-1",
  "metadata": {
    "trace_id": "trace_1",
    "version": "v1"
  }
}
```

## Response

```json
{
  "status": "ok",
  "data": {
    "id": 1,
    "endpoint": "endpoint-1",
    "computed_at": "2026-05-07T00:00:00Z"
  }
}
```

## Errors

| Code | Meaning | Recovery |
|------|---------|----------|
| E101 | Validation failed | Check request shape |
| E102 | Permission denied | Request access |
| E103 | Rate limited | Retry with backoff |
| E104 | Upstream timeout | Retry idempotently |

## Examples

```bash
curl -X POST https://api.example.com/v1/endpoint-1 \
  -H "Authorization: Bearer $TOKEN" \
  -H "Content-Type: application/json" \
  -d '{"user_id": "u_1", "scope": "endpoint-1"}'
```

## See also

- Endpoint 0 (related)
- Endpoint 2 (related)
- Architecture overview
