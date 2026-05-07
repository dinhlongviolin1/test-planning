# API Endpoint 11

## Overview

This endpoint handles request type 11 for the platform. It accepts JSON
payloads with user identity, request scope, and optional metadata fields.
Responses follow the standard envelope shape with status, data, and error
fields.

## Request

```json
{
  "user_id": "u_11",
  "scope": "endpoint-11",
  "metadata": {
    "trace_id": "trace_11",
    "version": "v1"
  }
}
```

## Response

```json
{
  "status": "ok",
  "data": {
    "id": 11,
    "endpoint": "endpoint-11",
    "computed_at": "2026-05-07T00:00:00Z"
  }
}
```

## Errors

| Code | Meaning | Recovery |
|------|---------|----------|
| E1101 | Validation failed | Check request shape |
| E1102 | Permission denied | Request access |
| E1103 | Rate limited | Retry with backoff |
| E1104 | Upstream timeout | Retry idempotently |

## Examples

```bash
curl -X POST https://api.example.com/v1/endpoint-11 \
  -H "Authorization: Bearer $TOKEN" \
  -H "Content-Type: application/json" \
  -d '{"user_id": "u_11", "scope": "endpoint-11"}'
```

## See also

- Endpoint 10 (related)
- Endpoint 12 (related)
- Architecture overview
