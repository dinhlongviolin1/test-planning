# API Endpoint 7

## Overview

This endpoint handles request type 7 for the platform. It accepts JSON
payloads with user identity, request scope, and optional metadata fields.
Responses follow the standard envelope shape with status, data, and error
fields.

## Request

```json
{
  "user_id": "u_7",
  "scope": "endpoint-7",
  "metadata": {
    "trace_id": "trace_7",
    "version": "v1"
  }
}
```

## Response

```json
{
  "status": "ok",
  "data": {
    "id": 7,
    "endpoint": "endpoint-7",
    "computed_at": "2026-05-07T00:00:00Z"
  }
}
```

## Errors

| Code | Meaning | Recovery |
|------|---------|----------|
| E701 | Validation failed | Check request shape |
| E702 | Permission denied | Request access |
| E703 | Rate limited | Retry with backoff |
| E704 | Upstream timeout | Retry idempotently |

## Examples

```bash
curl -X POST https://api.example.com/v1/endpoint-7 \
  -H "Authorization: Bearer $TOKEN" \
  -H "Content-Type: application/json" \
  -d '{"user_id": "u_7", "scope": "endpoint-7"}'
```

## See also

- Endpoint 6 (related)
- Endpoint 8 (related)
- Architecture overview
