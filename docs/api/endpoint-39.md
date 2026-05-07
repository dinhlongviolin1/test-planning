# API Endpoint 39

## Overview

This endpoint handles request type 39 for the platform. It accepts JSON
payloads with user identity, request scope, and optional metadata fields.
Responses follow the standard envelope shape with status, data, and error
fields.

## Request

```json
{
  "user_id": "u_39",
  "scope": "endpoint-39",
  "metadata": {
    "trace_id": "trace_39",
    "version": "v1"
  }
}
```

## Response

```json
{
  "status": "ok",
  "data": {
    "id": 39,
    "endpoint": "endpoint-39",
    "computed_at": "2026-05-07T00:00:00Z"
  }
}
```

## Errors

| Code | Meaning | Recovery |
|------|---------|----------|
| E3901 | Validation failed | Check request shape |
| E3902 | Permission denied | Request access |
| E3903 | Rate limited | Retry with backoff |
| E3904 | Upstream timeout | Retry idempotently |

## Examples

```bash
curl -X POST https://api.example.com/v1/endpoint-39 \
  -H "Authorization: Bearer $TOKEN" \
  -H "Content-Type: application/json" \
  -d '{"user_id": "u_39", "scope": "endpoint-39"}'
```

## See also

- Endpoint 38 (related)
- Endpoint 40 (related)
- Architecture overview
