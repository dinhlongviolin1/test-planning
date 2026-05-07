# API Endpoint 12

## Overview

This endpoint handles request type 12 for the platform. It accepts JSON
payloads with user identity, request scope, and optional metadata fields.
Responses follow the standard envelope shape with status, data, and error
fields.

## Request

```json
{
  "user_id": "u_12",
  "scope": "endpoint-12",
  "metadata": {
    "trace_id": "trace_12",
    "version": "v1"
  }
}
```

## Response

```json
{
  "status": "ok",
  "data": {
    "id": 12,
    "endpoint": "endpoint-12",
    "computed_at": "2026-05-07T00:00:00Z"
  }
}
```

## Errors

| Code | Meaning | Recovery |
|------|---------|----------|
| E1201 | Validation failed | Check request shape |
| E1202 | Permission denied | Request access |
| E1203 | Rate limited | Retry with backoff |
| E1204 | Upstream timeout | Retry idempotently |

## Examples

```bash
curl -X POST https://api.example.com/v1/endpoint-12 \
  -H "Authorization: Bearer $TOKEN" \
  -H "Content-Type: application/json" \
  -d '{"user_id": "u_12", "scope": "endpoint-12"}'
```

## See also

- Endpoint 11 (related)
- Endpoint 13 (related)
- Architecture overview
