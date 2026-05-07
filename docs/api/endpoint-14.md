# API Endpoint 14

## Overview

This endpoint handles request type 14 for the platform. It accepts JSON
payloads with user identity, request scope, and optional metadata fields.
Responses follow the standard envelope shape with status, data, and error
fields.

## Request

```json
{
  "user_id": "u_14",
  "scope": "endpoint-14",
  "metadata": {
    "trace_id": "trace_14",
    "version": "v1"
  }
}
```

## Response

```json
{
  "status": "ok",
  "data": {
    "id": 14,
    "endpoint": "endpoint-14",
    "computed_at": "2026-05-07T00:00:00Z"
  }
}
```

## Errors

| Code | Meaning | Recovery |
|------|---------|----------|
| E1401 | Validation failed | Check request shape |
| E1402 | Permission denied | Request access |
| E1403 | Rate limited | Retry with backoff |
| E1404 | Upstream timeout | Retry idempotently |

## Examples

```bash
curl -X POST https://api.example.com/v1/endpoint-14 \
  -H "Authorization: Bearer $TOKEN" \
  -H "Content-Type: application/json" \
  -d '{"user_id": "u_14", "scope": "endpoint-14"}'
```

## See also

- Endpoint 13 (related)
- Endpoint 15 (related)
- Architecture overview
