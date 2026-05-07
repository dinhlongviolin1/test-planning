# API Endpoint 8

## Overview

This endpoint handles request type 8 for the platform. It accepts JSON
payloads with user identity, request scope, and optional metadata fields.
Responses follow the standard envelope shape with status, data, and error
fields.

## Request

```json
{
  "user_id": "u_8",
  "scope": "endpoint-8",
  "metadata": {
    "trace_id": "trace_8",
    "version": "v1"
  }
}
```

## Response

```json
{
  "status": "ok",
  "data": {
    "id": 8,
    "endpoint": "endpoint-8",
    "computed_at": "2026-05-07T00:00:00Z"
  }
}
```

## Errors

| Code | Meaning | Recovery |
|------|---------|----------|
| E801 | Validation failed | Check request shape |
| E802 | Permission denied | Request access |
| E803 | Rate limited | Retry with backoff |
| E804 | Upstream timeout | Retry idempotently |

## Examples

```bash
curl -X POST https://api.example.com/v1/endpoint-8 \
  -H "Authorization: Bearer $TOKEN" \
  -H "Content-Type: application/json" \
  -d '{"user_id": "u_8", "scope": "endpoint-8"}'
```

## See also

- Endpoint 7 (related)
- Endpoint 9 (related)
- Architecture overview
