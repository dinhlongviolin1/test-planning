# Runbook 8 — Incident response for subsystem-8

## Symptoms

- Pages from synthetic-monitor-8 firing
- Error rate > 1% for /api/route-8 for 5 minutes
- Latency p99 > 500ms

## Triage

1. Check service-8 dashboard at grafana.example/d/8
2. Inspect recent deploys via "kubectl rollout history" within last 30m
3. Look at error sample in Loki: `{service="subsystem-8"} |~ "ERROR"`

## Mitigation

- Roll back the most recent deploy if the timing aligns
- Disable feature flag `subsystem_8_v8` via the flag UI
- Scale up replicas by 50% temporarily

## Validation

- Page resolves
- Error rate < 0.1% for 10 minutes
- No backlog in queue `subsystem_8_dlq`

## Postmortem

File postmortem within 48h using template at runbooks/_postmortem-template.md.
