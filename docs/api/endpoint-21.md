# API Endpoint 21

## Overview

This endpoint handles request type 21 for the platform. It accepts JSON
payloads with user identity, request scope, and optional metadata fields.
Responses follow the standard envelope shape with status, data, and error
fields.

## Request

```json
{
  "user_id": "u_21",
  "scope": "endpoint-21",
  "metadata": {
    "trace_id": "trace_21",
    "version": "v1"
  }
}
```

## Response

```json
{
  "status": "ok",
  "data": {
    "id": 21,
    "endpoint": "endpoint-21",
    "computed_at": "2026-05-07T00:00:00Z"
  }
}
```

## Errors

| Code | Meaning | Recovery |
|------|---------|----------|
| E2101 | Validation failed | Check request shape |
| E2102 | Permission denied | Request access |
| E2103 | Rate limited | Retry with backoff |
| E2104 | Upstream timeout | Retry idempotently |

## Examples

```bash
curl -X POST https://api.example.com/v1/endpoint-21 \
  -H "Authorization: Bearer $TOKEN" \
  -H "Content-Type: application/json" \
  -d '{"user_id": "u_21", "scope": "endpoint-21"}'
```

## See also

- Endpoint 20 (related)
- Endpoint 22 (related)
- Architecture overview
