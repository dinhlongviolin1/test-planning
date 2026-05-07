# API Endpoint 2

## Overview

This endpoint handles request type 2 for the platform. It accepts JSON
payloads with user identity, request scope, and optional metadata fields.
Responses follow the standard envelope shape with status, data, and error
fields.

## Request

```json
{
  "user_id": "u_2",
  "scope": "endpoint-2",
  "metadata": {
    "trace_id": "trace_2",
    "version": "v1"
  }
}
```

## Response

```json
{
  "status": "ok",
  "data": {
    "id": 2,
    "endpoint": "endpoint-2",
    "computed_at": "2026-05-07T00:00:00Z"
  }
}
```

## Errors

| Code | Meaning | Recovery |
|------|---------|----------|
| E201 | Validation failed | Check request shape |
| E202 | Permission denied | Request access |
| E203 | Rate limited | Retry with backoff |
| E204 | Upstream timeout | Retry idempotently |

## Examples

```bash
curl -X POST https://api.example.com/v1/endpoint-2 \
  -H "Authorization: Bearer $TOKEN" \
  -H "Content-Type: application/json" \
  -d '{"user_id": "u_2", "scope": "endpoint-2"}'
```

## See also

- Endpoint 1 (related)
- Endpoint 3 (related)
- Architecture overview
