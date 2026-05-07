# API Endpoint 4

## Overview

This endpoint handles request type 4 for the platform. It accepts JSON
payloads with user identity, request scope, and optional metadata fields.
Responses follow the standard envelope shape with status, data, and error
fields.

## Request

```json
{
  "user_id": "u_4",
  "scope": "endpoint-4",
  "metadata": {
    "trace_id": "trace_4",
    "version": "v1"
  }
}
```

## Response

```json
{
  "status": "ok",
  "data": {
    "id": 4,
    "endpoint": "endpoint-4",
    "computed_at": "2026-05-07T00:00:00Z"
  }
}
```

## Errors

| Code | Meaning | Recovery |
|------|---------|----------|
| E401 | Validation failed | Check request shape |
| E402 | Permission denied | Request access |
| E403 | Rate limited | Retry with backoff |
| E404 | Upstream timeout | Retry idempotently |

## Examples

```bash
curl -X POST https://api.example.com/v1/endpoint-4 \
  -H "Authorization: Bearer $TOKEN" \
  -H "Content-Type: application/json" \
  -d '{"user_id": "u_4", "scope": "endpoint-4"}'
```

## See also

- Endpoint 3 (related)
- Endpoint 5 (related)
- Architecture overview
