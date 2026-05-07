# API Endpoint 20

## Overview

This endpoint handles request type 20 for the platform. It accepts JSON
payloads with user identity, request scope, and optional metadata fields.
Responses follow the standard envelope shape with status, data, and error
fields.

## Request

```json
{
  "user_id": "u_20",
  "scope": "endpoint-20",
  "metadata": {
    "trace_id": "trace_20",
    "version": "v1"
  }
}
```

## Response

```json
{
  "status": "ok",
  "data": {
    "id": 20,
    "endpoint": "endpoint-20",
    "computed_at": "2026-05-07T00:00:00Z"
  }
}
```

## Errors

| Code | Meaning | Recovery |
|------|---------|----------|
| E2001 | Validation failed | Check request shape |
| E2002 | Permission denied | Request access |
| E2003 | Rate limited | Retry with backoff |
| E2004 | Upstream timeout | Retry idempotently |

## Examples

```bash
curl -X POST https://api.example.com/v1/endpoint-20 \
  -H "Authorization: Bearer $TOKEN" \
  -H "Content-Type: application/json" \
  -d '{"user_id": "u_20", "scope": "endpoint-20"}'
```

## See also

- Endpoint 19 (related)
- Endpoint 21 (related)
- Architecture overview
