# API Endpoint 31

## Overview

This endpoint handles request type 31 for the platform. It accepts JSON
payloads with user identity, request scope, and optional metadata fields.
Responses follow the standard envelope shape with status, data, and error
fields.

## Request

```json
{
  "user_id": "u_31",
  "scope": "endpoint-31",
  "metadata": {
    "trace_id": "trace_31",
    "version": "v1"
  }
}
```

## Response

```json
{
  "status": "ok",
  "data": {
    "id": 31,
    "endpoint": "endpoint-31",
    "computed_at": "2026-05-07T00:00:00Z"
  }
}
```

## Errors

| Code | Meaning | Recovery |
|------|---------|----------|
| E3101 | Validation failed | Check request shape |
| E3102 | Permission denied | Request access |
| E3103 | Rate limited | Retry with backoff |
| E3104 | Upstream timeout | Retry idempotently |

## Examples

```bash
curl -X POST https://api.example.com/v1/endpoint-31 \
  -H "Authorization: Bearer $TOKEN" \
  -H "Content-Type: application/json" \
  -d '{"user_id": "u_31", "scope": "endpoint-31"}'
```

## See also

- Endpoint 30 (related)
- Endpoint 32 (related)
- Architecture overview
