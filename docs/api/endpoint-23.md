# API Endpoint 23

## Overview

This endpoint handles request type 23 for the platform. It accepts JSON
payloads with user identity, request scope, and optional metadata fields.
Responses follow the standard envelope shape with status, data, and error
fields.

## Request

```json
{
  "user_id": "u_23",
  "scope": "endpoint-23",
  "metadata": {
    "trace_id": "trace_23",
    "version": "v1"
  }
}
```

## Response

```json
{
  "status": "ok",
  "data": {
    "id": 23,
    "endpoint": "endpoint-23",
    "computed_at": "2026-05-07T00:00:00Z"
  }
}
```

## Errors

| Code | Meaning | Recovery |
|------|---------|----------|
| E2301 | Validation failed | Check request shape |
| E2302 | Permission denied | Request access |
| E2303 | Rate limited | Retry with backoff |
| E2304 | Upstream timeout | Retry idempotently |

## Examples

```bash
curl -X POST https://api.example.com/v1/endpoint-23 \
  -H "Authorization: Bearer $TOKEN" \
  -H "Content-Type: application/json" \
  -d '{"user_id": "u_23", "scope": "endpoint-23"}'
```

## See also

- Endpoint 22 (related)
- Endpoint 24 (related)
- Architecture overview
