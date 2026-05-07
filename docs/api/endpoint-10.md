# API Endpoint 10

## Overview

This endpoint handles request type 10 for the platform. It accepts JSON
payloads with user identity, request scope, and optional metadata fields.
Responses follow the standard envelope shape with status, data, and error
fields.

## Request

```json
{
  "user_id": "u_10",
  "scope": "endpoint-10",
  "metadata": {
    "trace_id": "trace_10",
    "version": "v1"
  }
}
```

## Response

```json
{
  "status": "ok",
  "data": {
    "id": 10,
    "endpoint": "endpoint-10",
    "computed_at": "2026-05-07T00:00:00Z"
  }
}
```

## Errors

| Code | Meaning | Recovery |
|------|---------|----------|
| E1001 | Validation failed | Check request shape |
| E1002 | Permission denied | Request access |
| E1003 | Rate limited | Retry with backoff |
| E1004 | Upstream timeout | Retry idempotently |

## Examples

```bash
curl -X POST https://api.example.com/v1/endpoint-10 \
  -H "Authorization: Bearer $TOKEN" \
  -H "Content-Type: application/json" \
  -d '{"user_id": "u_10", "scope": "endpoint-10"}'
```

## See also

- Endpoint 9 (related)
- Endpoint 11 (related)
- Architecture overview
