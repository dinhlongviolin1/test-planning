# API Endpoint 27

## Overview

This endpoint handles request type 27 for the platform. It accepts JSON
payloads with user identity, request scope, and optional metadata fields.
Responses follow the standard envelope shape with status, data, and error
fields.

## Request

```json
{
  "user_id": "u_27",
  "scope": "endpoint-27",
  "metadata": {
    "trace_id": "trace_27",
    "version": "v1"
  }
}
```

## Response

```json
{
  "status": "ok",
  "data": {
    "id": 27,
    "endpoint": "endpoint-27",
    "computed_at": "2026-05-07T00:00:00Z"
  }
}
```

## Errors

| Code | Meaning | Recovery |
|------|---------|----------|
| E2701 | Validation failed | Check request shape |
| E2702 | Permission denied | Request access |
| E2703 | Rate limited | Retry with backoff |
| E2704 | Upstream timeout | Retry idempotently |

## Examples

```bash
curl -X POST https://api.example.com/v1/endpoint-27 \
  -H "Authorization: Bearer $TOKEN" \
  -H "Content-Type: application/json" \
  -d '{"user_id": "u_27", "scope": "endpoint-27"}'
```

## See also

- Endpoint 26 (related)
- Endpoint 28 (related)
- Architecture overview
