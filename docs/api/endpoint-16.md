# API Endpoint 16

## Overview

This endpoint handles request type 16 for the platform. It accepts JSON
payloads with user identity, request scope, and optional metadata fields.
Responses follow the standard envelope shape with status, data, and error
fields.

## Request

```json
{
  "user_id": "u_16",
  "scope": "endpoint-16",
  "metadata": {
    "trace_id": "trace_16",
    "version": "v1"
  }
}
```

## Response

```json
{
  "status": "ok",
  "data": {
    "id": 16,
    "endpoint": "endpoint-16",
    "computed_at": "2026-05-07T00:00:00Z"
  }
}
```

## Errors

| Code | Meaning | Recovery |
|------|---------|----------|
| E1601 | Validation failed | Check request shape |
| E1602 | Permission denied | Request access |
| E1603 | Rate limited | Retry with backoff |
| E1604 | Upstream timeout | Retry idempotently |

## Examples

```bash
curl -X POST https://api.example.com/v1/endpoint-16 \
  -H "Authorization: Bearer $TOKEN" \
  -H "Content-Type: application/json" \
  -d '{"user_id": "u_16", "scope": "endpoint-16"}'
```

## See also

- Endpoint 15 (related)
- Endpoint 17 (related)
- Architecture overview
