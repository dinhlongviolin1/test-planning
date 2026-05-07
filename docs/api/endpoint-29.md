# API Endpoint 29

## Overview

This endpoint handles request type 29 for the platform. It accepts JSON
payloads with user identity, request scope, and optional metadata fields.
Responses follow the standard envelope shape with status, data, and error
fields.

## Request

```json
{
  "user_id": "u_29",
  "scope": "endpoint-29",
  "metadata": {
    "trace_id": "trace_29",
    "version": "v1"
  }
}
```

## Response

```json
{
  "status": "ok",
  "data": {
    "id": 29,
    "endpoint": "endpoint-29",
    "computed_at": "2026-05-07T00:00:00Z"
  }
}
```

## Errors

| Code | Meaning | Recovery |
|------|---------|----------|
| E2901 | Validation failed | Check request shape |
| E2902 | Permission denied | Request access |
| E2903 | Rate limited | Retry with backoff |
| E2904 | Upstream timeout | Retry idempotently |

## Examples

```bash
curl -X POST https://api.example.com/v1/endpoint-29 \
  -H "Authorization: Bearer $TOKEN" \
  -H "Content-Type: application/json" \
  -d '{"user_id": "u_29", "scope": "endpoint-29"}'
```

## See also

- Endpoint 28 (related)
- Endpoint 30 (related)
- Architecture overview
