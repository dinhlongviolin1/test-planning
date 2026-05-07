# API Endpoint 32

## Overview

This endpoint handles request type 32 for the platform. It accepts JSON
payloads with user identity, request scope, and optional metadata fields.
Responses follow the standard envelope shape with status, data, and error
fields.

## Request

```json
{
  "user_id": "u_32",
  "scope": "endpoint-32",
  "metadata": {
    "trace_id": "trace_32",
    "version": "v1"
  }
}
```

## Response

```json
{
  "status": "ok",
  "data": {
    "id": 32,
    "endpoint": "endpoint-32",
    "computed_at": "2026-05-07T00:00:00Z"
  }
}
```

## Errors

| Code | Meaning | Recovery |
|------|---------|----------|
| E3201 | Validation failed | Check request shape |
| E3202 | Permission denied | Request access |
| E3203 | Rate limited | Retry with backoff |
| E3204 | Upstream timeout | Retry idempotently |

## Examples

```bash
curl -X POST https://api.example.com/v1/endpoint-32 \
  -H "Authorization: Bearer $TOKEN" \
  -H "Content-Type: application/json" \
  -d '{"user_id": "u_32", "scope": "endpoint-32"}'
```

## See also

- Endpoint 31 (related)
- Endpoint 33 (related)
- Architecture overview
