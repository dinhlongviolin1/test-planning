# API Endpoint 19

## Overview

This endpoint handles request type 19 for the platform. It accepts JSON
payloads with user identity, request scope, and optional metadata fields.
Responses follow the standard envelope shape with status, data, and error
fields.

## Request

```json
{
  "user_id": "u_19",
  "scope": "endpoint-19",
  "metadata": {
    "trace_id": "trace_19",
    "version": "v1"
  }
}
```

## Response

```json
{
  "status": "ok",
  "data": {
    "id": 19,
    "endpoint": "endpoint-19",
    "computed_at": "2026-05-07T00:00:00Z"
  }
}
```

## Errors

| Code | Meaning | Recovery |
|------|---------|----------|
| E1901 | Validation failed | Check request shape |
| E1902 | Permission denied | Request access |
| E1903 | Rate limited | Retry with backoff |
| E1904 | Upstream timeout | Retry idempotently |

## Examples

```bash
curl -X POST https://api.example.com/v1/endpoint-19 \
  -H "Authorization: Bearer $TOKEN" \
  -H "Content-Type: application/json" \
  -d '{"user_id": "u_19", "scope": "endpoint-19"}'
```

## See also

- Endpoint 18 (related)
- Endpoint 20 (related)
- Architecture overview
