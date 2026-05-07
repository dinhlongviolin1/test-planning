# API Endpoint 5

## Overview

This endpoint handles request type 5 for the platform. It accepts JSON
payloads with user identity, request scope, and optional metadata fields.
Responses follow the standard envelope shape with status, data, and error
fields.

## Request

```json
{
  "user_id": "u_5",
  "scope": "endpoint-5",
  "metadata": {
    "trace_id": "trace_5",
    "version": "v1"
  }
}
```

## Response

```json
{
  "status": "ok",
  "data": {
    "id": 5,
    "endpoint": "endpoint-5",
    "computed_at": "2026-05-07T00:00:00Z"
  }
}
```

## Errors

| Code | Meaning | Recovery |
|------|---------|----------|
| E501 | Validation failed | Check request shape |
| E502 | Permission denied | Request access |
| E503 | Rate limited | Retry with backoff |
| E504 | Upstream timeout | Retry idempotently |

## Examples

```bash
curl -X POST https://api.example.com/v1/endpoint-5 \
  -H "Authorization: Bearer $TOKEN" \
  -H "Content-Type: application/json" \
  -d '{"user_id": "u_5", "scope": "endpoint-5"}'
```

## See also

- Endpoint 4 (related)
- Endpoint 6 (related)
- Architecture overview
