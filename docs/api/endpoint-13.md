# API Endpoint 13

## Overview

This endpoint handles request type 13 for the platform. It accepts JSON
payloads with user identity, request scope, and optional metadata fields.
Responses follow the standard envelope shape with status, data, and error
fields.

## Request

```json
{
  "user_id": "u_13",
  "scope": "endpoint-13",
  "metadata": {
    "trace_id": "trace_13",
    "version": "v1"
  }
}
```

## Response

```json
{
  "status": "ok",
  "data": {
    "id": 13,
    "endpoint": "endpoint-13",
    "computed_at": "2026-05-07T00:00:00Z"
  }
}
```

## Errors

| Code | Meaning | Recovery |
|------|---------|----------|
| E1301 | Validation failed | Check request shape |
| E1302 | Permission denied | Request access |
| E1303 | Rate limited | Retry with backoff |
| E1304 | Upstream timeout | Retry idempotently |

## Examples

```bash
curl -X POST https://api.example.com/v1/endpoint-13 \
  -H "Authorization: Bearer $TOKEN" \
  -H "Content-Type: application/json" \
  -d '{"user_id": "u_13", "scope": "endpoint-13"}'
```

## See also

- Endpoint 12 (related)
- Endpoint 14 (related)
- Architecture overview
