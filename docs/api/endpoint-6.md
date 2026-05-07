# API Endpoint 6

## Overview

This endpoint handles request type 6 for the platform. It accepts JSON
payloads with user identity, request scope, and optional metadata fields.
Responses follow the standard envelope shape with status, data, and error
fields.

## Request

```json
{
  "user_id": "u_6",
  "scope": "endpoint-6",
  "metadata": {
    "trace_id": "trace_6",
    "version": "v1"
  }
}
```

## Response

```json
{
  "status": "ok",
  "data": {
    "id": 6,
    "endpoint": "endpoint-6",
    "computed_at": "2026-05-07T00:00:00Z"
  }
}
```

## Errors

| Code | Meaning | Recovery |
|------|---------|----------|
| E601 | Validation failed | Check request shape |
| E602 | Permission denied | Request access |
| E603 | Rate limited | Retry with backoff |
| E604 | Upstream timeout | Retry idempotently |

## Examples

```bash
curl -X POST https://api.example.com/v1/endpoint-6 \
  -H "Authorization: Bearer $TOKEN" \
  -H "Content-Type: application/json" \
  -d '{"user_id": "u_6", "scope": "endpoint-6"}'
```

## See also

- Endpoint 5 (related)
- Endpoint 7 (related)
- Architecture overview
