# API Endpoint 40

## Overview

This endpoint handles request type 40 for the platform. It accepts JSON
payloads with user identity, request scope, and optional metadata fields.
Responses follow the standard envelope shape with status, data, and error
fields.

## Request

```json
{
  "user_id": "u_40",
  "scope": "endpoint-40",
  "metadata": {
    "trace_id": "trace_40",
    "version": "v1"
  }
}
```

## Response

```json
{
  "status": "ok",
  "data": {
    "id": 40,
    "endpoint": "endpoint-40",
    "computed_at": "2026-05-07T00:00:00Z"
  }
}
```

## Errors

| Code | Meaning | Recovery |
|------|---------|----------|
| E4001 | Validation failed | Check request shape |
| E4002 | Permission denied | Request access |
| E4003 | Rate limited | Retry with backoff |
| E4004 | Upstream timeout | Retry idempotently |

## Examples

```bash
curl -X POST https://api.example.com/v1/endpoint-40 \
  -H "Authorization: Bearer $TOKEN" \
  -H "Content-Type: application/json" \
  -d '{"user_id": "u_40", "scope": "endpoint-40"}'
```

## See also

- Endpoint 39 (related)
- Endpoint 41 (related)
- Architecture overview
