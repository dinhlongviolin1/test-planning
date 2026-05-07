# API Endpoint 34

## Overview

This endpoint handles request type 34 for the platform. It accepts JSON
payloads with user identity, request scope, and optional metadata fields.
Responses follow the standard envelope shape with status, data, and error
fields.

## Request

```json
{
  "user_id": "u_34",
  "scope": "endpoint-34",
  "metadata": {
    "trace_id": "trace_34",
    "version": "v1"
  }
}
```

## Response

```json
{
  "status": "ok",
  "data": {
    "id": 34,
    "endpoint": "endpoint-34",
    "computed_at": "2026-05-07T00:00:00Z"
  }
}
```

## Errors

| Code | Meaning | Recovery |
|------|---------|----------|
| E3401 | Validation failed | Check request shape |
| E3402 | Permission denied | Request access |
| E3403 | Rate limited | Retry with backoff |
| E3404 | Upstream timeout | Retry idempotently |

## Examples

```bash
curl -X POST https://api.example.com/v1/endpoint-34 \
  -H "Authorization: Bearer $TOKEN" \
  -H "Content-Type: application/json" \
  -d '{"user_id": "u_34", "scope": "endpoint-34"}'
```

## See also

- Endpoint 33 (related)
- Endpoint 35 (related)
- Architecture overview
