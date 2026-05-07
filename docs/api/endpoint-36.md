# API Endpoint 36

## Overview

This endpoint handles request type 36 for the platform. It accepts JSON
payloads with user identity, request scope, and optional metadata fields.
Responses follow the standard envelope shape with status, data, and error
fields.

## Request

```json
{
  "user_id": "u_36",
  "scope": "endpoint-36",
  "metadata": {
    "trace_id": "trace_36",
    "version": "v1"
  }
}
```

## Response

```json
{
  "status": "ok",
  "data": {
    "id": 36,
    "endpoint": "endpoint-36",
    "computed_at": "2026-05-07T00:00:00Z"
  }
}
```

## Errors

| Code | Meaning | Recovery |
|------|---------|----------|
| E3601 | Validation failed | Check request shape |
| E3602 | Permission denied | Request access |
| E3603 | Rate limited | Retry with backoff |
| E3604 | Upstream timeout | Retry idempotently |

## Examples

```bash
curl -X POST https://api.example.com/v1/endpoint-36 \
  -H "Authorization: Bearer $TOKEN" \
  -H "Content-Type: application/json" \
  -d '{"user_id": "u_36", "scope": "endpoint-36"}'
```

## See also

- Endpoint 35 (related)
- Endpoint 37 (related)
- Architecture overview
