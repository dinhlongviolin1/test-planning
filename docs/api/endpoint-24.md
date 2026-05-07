# API Endpoint 24

## Overview

This endpoint handles request type 24 for the platform. It accepts JSON
payloads with user identity, request scope, and optional metadata fields.
Responses follow the standard envelope shape with status, data, and error
fields.

## Request

```json
{
  "user_id": "u_24",
  "scope": "endpoint-24",
  "metadata": {
    "trace_id": "trace_24",
    "version": "v1"
  }
}
```

## Response

```json
{
  "status": "ok",
  "data": {
    "id": 24,
    "endpoint": "endpoint-24",
    "computed_at": "2026-05-07T00:00:00Z"
  }
}
```

## Errors

| Code | Meaning | Recovery |
|------|---------|----------|
| E2401 | Validation failed | Check request shape |
| E2402 | Permission denied | Request access |
| E2403 | Rate limited | Retry with backoff |
| E2404 | Upstream timeout | Retry idempotently |

## Examples

```bash
curl -X POST https://api.example.com/v1/endpoint-24 \
  -H "Authorization: Bearer $TOKEN" \
  -H "Content-Type: application/json" \
  -d '{"user_id": "u_24", "scope": "endpoint-24"}'
```

## See also

- Endpoint 23 (related)
- Endpoint 25 (related)
- Architecture overview
