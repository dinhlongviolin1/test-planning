# API Endpoint 25

## Overview

This endpoint handles request type 25 for the platform. It accepts JSON
payloads with user identity, request scope, and optional metadata fields.
Responses follow the standard envelope shape with status, data, and error
fields.

## Request

```json
{
  "user_id": "u_25",
  "scope": "endpoint-25",
  "metadata": {
    "trace_id": "trace_25",
    "version": "v1"
  }
}
```

## Response

```json
{
  "status": "ok",
  "data": {
    "id": 25,
    "endpoint": "endpoint-25",
    "computed_at": "2026-05-07T00:00:00Z"
  }
}
```

## Errors

| Code | Meaning | Recovery |
|------|---------|----------|
| E2501 | Validation failed | Check request shape |
| E2502 | Permission denied | Request access |
| E2503 | Rate limited | Retry with backoff |
| E2504 | Upstream timeout | Retry idempotently |

## Examples

```bash
curl -X POST https://api.example.com/v1/endpoint-25 \
  -H "Authorization: Bearer $TOKEN" \
  -H "Content-Type: application/json" \
  -d '{"user_id": "u_25", "scope": "endpoint-25"}'
```

## See also

- Endpoint 24 (related)
- Endpoint 26 (related)
- Architecture overview
