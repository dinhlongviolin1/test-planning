# API Endpoint 17

## Overview

This endpoint handles request type 17 for the platform. It accepts JSON
payloads with user identity, request scope, and optional metadata fields.
Responses follow the standard envelope shape with status, data, and error
fields.

## Request

```json
{
  "user_id": "u_17",
  "scope": "endpoint-17",
  "metadata": {
    "trace_id": "trace_17",
    "version": "v1"
  }
}
```

## Response

```json
{
  "status": "ok",
  "data": {
    "id": 17,
    "endpoint": "endpoint-17",
    "computed_at": "2026-05-07T00:00:00Z"
  }
}
```

## Errors

| Code | Meaning | Recovery |
|------|---------|----------|
| E1701 | Validation failed | Check request shape |
| E1702 | Permission denied | Request access |
| E1703 | Rate limited | Retry with backoff |
| E1704 | Upstream timeout | Retry idempotently |

## Examples

```bash
curl -X POST https://api.example.com/v1/endpoint-17 \
  -H "Authorization: Bearer $TOKEN" \
  -H "Content-Type: application/json" \
  -d '{"user_id": "u_17", "scope": "endpoint-17"}'
```

## See also

- Endpoint 16 (related)
- Endpoint 18 (related)
- Architecture overview
