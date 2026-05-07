# API Endpoint 9

## Overview

This endpoint handles request type 9 for the platform. It accepts JSON
payloads with user identity, request scope, and optional metadata fields.
Responses follow the standard envelope shape with status, data, and error
fields.

## Request

```json
{
  "user_id": "u_9",
  "scope": "endpoint-9",
  "metadata": {
    "trace_id": "trace_9",
    "version": "v1"
  }
}
```

## Response

```json
{
  "status": "ok",
  "data": {
    "id": 9,
    "endpoint": "endpoint-9",
    "computed_at": "2026-05-07T00:00:00Z"
  }
}
```

## Errors

| Code | Meaning | Recovery |
|------|---------|----------|
| E901 | Validation failed | Check request shape |
| E902 | Permission denied | Request access |
| E903 | Rate limited | Retry with backoff |
| E904 | Upstream timeout | Retry idempotently |

## Examples

```bash
curl -X POST https://api.example.com/v1/endpoint-9 \
  -H "Authorization: Bearer $TOKEN" \
  -H "Content-Type: application/json" \
  -d '{"user_id": "u_9", "scope": "endpoint-9"}'
```

## See also

- Endpoint 8 (related)
- Endpoint 10 (related)
- Architecture overview
