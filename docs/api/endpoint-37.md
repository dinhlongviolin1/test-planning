# API Endpoint 37

## Overview

This endpoint handles request type 37 for the platform. It accepts JSON
payloads with user identity, request scope, and optional metadata fields.
Responses follow the standard envelope shape with status, data, and error
fields.

## Request

```json
{
  "user_id": "u_37",
  "scope": "endpoint-37",
  "metadata": {
    "trace_id": "trace_37",
    "version": "v1"
  }
}
```

## Response

```json
{
  "status": "ok",
  "data": {
    "id": 37,
    "endpoint": "endpoint-37",
    "computed_at": "2026-05-07T00:00:00Z"
  }
}
```

## Errors

| Code | Meaning | Recovery |
|------|---------|----------|
| E3701 | Validation failed | Check request shape |
| E3702 | Permission denied | Request access |
| E3703 | Rate limited | Retry with backoff |
| E3704 | Upstream timeout | Retry idempotently |

## Examples

```bash
curl -X POST https://api.example.com/v1/endpoint-37 \
  -H "Authorization: Bearer $TOKEN" \
  -H "Content-Type: application/json" \
  -d '{"user_id": "u_37", "scope": "endpoint-37"}'
```

## See also

- Endpoint 36 (related)
- Endpoint 38 (related)
- Architecture overview
