# API Endpoint 33

## Overview

This endpoint handles request type 33 for the platform. It accepts JSON
payloads with user identity, request scope, and optional metadata fields.
Responses follow the standard envelope shape with status, data, and error
fields.

## Request

```json
{
  "user_id": "u_33",
  "scope": "endpoint-33",
  "metadata": {
    "trace_id": "trace_33",
    "version": "v1"
  }
}
```

## Response

```json
{
  "status": "ok",
  "data": {
    "id": 33,
    "endpoint": "endpoint-33",
    "computed_at": "2026-05-07T00:00:00Z"
  }
}
```

## Errors

| Code | Meaning | Recovery |
|------|---------|----------|
| E3301 | Validation failed | Check request shape |
| E3302 | Permission denied | Request access |
| E3303 | Rate limited | Retry with backoff |
| E3304 | Upstream timeout | Retry idempotently |

## Examples

```bash
curl -X POST https://api.example.com/v1/endpoint-33 \
  -H "Authorization: Bearer $TOKEN" \
  -H "Content-Type: application/json" \
  -d '{"user_id": "u_33", "scope": "endpoint-33"}'
```

## See also

- Endpoint 32 (related)
- Endpoint 34 (related)
- Architecture overview
