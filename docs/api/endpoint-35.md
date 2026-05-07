# API Endpoint 35

## Overview

This endpoint handles request type 35 for the platform. It accepts JSON
payloads with user identity, request scope, and optional metadata fields.
Responses follow the standard envelope shape with status, data, and error
fields.

## Request

```json
{
  "user_id": "u_35",
  "scope": "endpoint-35",
  "metadata": {
    "trace_id": "trace_35",
    "version": "v1"
  }
}
```

## Response

```json
{
  "status": "ok",
  "data": {
    "id": 35,
    "endpoint": "endpoint-35",
    "computed_at": "2026-05-07T00:00:00Z"
  }
}
```

## Errors

| Code | Meaning | Recovery |
|------|---------|----------|
| E3501 | Validation failed | Check request shape |
| E3502 | Permission denied | Request access |
| E3503 | Rate limited | Retry with backoff |
| E3504 | Upstream timeout | Retry idempotently |

## Examples

```bash
curl -X POST https://api.example.com/v1/endpoint-35 \
  -H "Authorization: Bearer $TOKEN" \
  -H "Content-Type: application/json" \
  -d '{"user_id": "u_35", "scope": "endpoint-35"}'
```

## See also

- Endpoint 34 (related)
- Endpoint 36 (related)
- Architecture overview
