# API Endpoint 30

## Overview

This endpoint handles request type 30 for the platform. It accepts JSON
payloads with user identity, request scope, and optional metadata fields.
Responses follow the standard envelope shape with status, data, and error
fields.

## Request

```json
{
  "user_id": "u_30",
  "scope": "endpoint-30",
  "metadata": {
    "trace_id": "trace_30",
    "version": "v1"
  }
}
```

## Response

```json
{
  "status": "ok",
  "data": {
    "id": 30,
    "endpoint": "endpoint-30",
    "computed_at": "2026-05-07T00:00:00Z"
  }
}
```

## Errors

| Code | Meaning | Recovery |
|------|---------|----------|
| E3001 | Validation failed | Check request shape |
| E3002 | Permission denied | Request access |
| E3003 | Rate limited | Retry with backoff |
| E3004 | Upstream timeout | Retry idempotently |

## Examples

```bash
curl -X POST https://api.example.com/v1/endpoint-30 \
  -H "Authorization: Bearer $TOKEN" \
  -H "Content-Type: application/json" \
  -d '{"user_id": "u_30", "scope": "endpoint-30"}'
```

## See also

- Endpoint 29 (related)
- Endpoint 31 (related)
- Architecture overview
