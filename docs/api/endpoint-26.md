# API Endpoint 26

## Overview

This endpoint handles request type 26 for the platform. It accepts JSON
payloads with user identity, request scope, and optional metadata fields.
Responses follow the standard envelope shape with status, data, and error
fields.

## Request

```json
{
  "user_id": "u_26",
  "scope": "endpoint-26",
  "metadata": {
    "trace_id": "trace_26",
    "version": "v1"
  }
}
```

## Response

```json
{
  "status": "ok",
  "data": {
    "id": 26,
    "endpoint": "endpoint-26",
    "computed_at": "2026-05-07T00:00:00Z"
  }
}
```

## Errors

| Code | Meaning | Recovery |
|------|---------|----------|
| E2601 | Validation failed | Check request shape |
| E2602 | Permission denied | Request access |
| E2603 | Rate limited | Retry with backoff |
| E2604 | Upstream timeout | Retry idempotently |

## Examples

```bash
curl -X POST https://api.example.com/v1/endpoint-26 \
  -H "Authorization: Bearer $TOKEN" \
  -H "Content-Type: application/json" \
  -d '{"user_id": "u_26", "scope": "endpoint-26"}'
```

## See also

- Endpoint 25 (related)
- Endpoint 27 (related)
- Architecture overview
