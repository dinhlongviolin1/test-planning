# Spec 9 — Subsystem 9 integration design

## Overview

This spec defines the integration contract for subsystem-9 with
the platform's request envelope and identity context. It is consumed by
service teams that own producers and consumers of subsystem-9.

## Scope

In scope:
- Request envelope shape v1.9
- Authentication via Bearer + tenant header
- Error envelope canonical fields
- Versioning + deprecation policy

Out of scope:
- Storage layer choice
- Cross-region replication
- Migration tooling

## API surface

| Method | Path | Auth | Body | Response |
|---|---|---|---|---|
| GET | /v1/subsystem-9/items | Bearer | — | { items: Item[] } |
| POST | /v1/subsystem-9/items | Bearer | { name, scope } | { id, name, created_at } |
| DELETE | /v1/subsystem-9/items/{id} | Bearer | — | 204 |

## Data shapes

```json
{
  "id": "itm_9",
  "name": "Subsystem 9 item",
  "scope": "tenant-9",
  "created_at": "2026-01-01T00:00:00Z"
}
```

## Errors

- 400 invalid_request — body shape rejected by validator
- 401 unauthorized — missing or invalid Bearer
- 403 forbidden — tenant lacks subsystem-9 access
- 404 not_found — id unknown to scope
- 409 conflict — id already exists with different attributes
- 429 rate_limited — exceeds tenant quota
- 500 internal_error — unhandled exception, see request_id

## Performance budgets

- p50 ≤ 30ms, p99 ≤ 200ms under 1k rps
- 95% cache hit rate steady state

## Open questions

- Should we gate DELETE on a soft-delete TTL?
- Is paging cursor-based or offset-based?
