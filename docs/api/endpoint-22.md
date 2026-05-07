# API Endpoint 22

## Overview

This endpoint handles request type 22 for the platform. It accepts JSON
payloads with user identity, request scope, and optional metadata fields.
Responses follow the standard envelope shape with status, data, and error
fields.

## Request

```json
{
  "user_id": "u_22",
  "scope": "endpoint-22",
  "metadata": {
    "trace_id": "trace_22",
    "version": "v1"
  }
}
```

## Response

```json
{
  "status": "ok",
  "data": {
    "id": 22,
    "endpoint": "endpoint-22",
    "computed_at": "2026-05-07T00:00:00Z"
  }
}
```

## Errors

| Code | Meaning | Recovery |
|------|---------|----------|
| E2201 | Validation failed | Check request shape |
| E2202 | Permission denied | Request access |
| E2203 | Rate limited | Retry with backoff |
| E2204 | Upstream timeout | Retry idempotently |

## Examples

```bash
curl -X POST https://api.example.com/v1/endpoint-22 \
  -H "Authorization: Bearer $TOKEN" \
  -H "Content-Type: application/json" \
  -d '{"user_id": "u_22", "scope": "endpoint-22"}'
```

## See also

- Endpoint 21 (related)
- Endpoint 23 (related)
- Architecture overview
