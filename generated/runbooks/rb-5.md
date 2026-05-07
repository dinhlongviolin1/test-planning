# Runbook 5 — Incident response for subsystem-5

## Symptoms

- Pages from synthetic-monitor-5 firing
- Error rate > 1% for /api/route-5 for 5 minutes
- Latency p99 > 500ms

## Triage

1. Check service-5 dashboard at grafana.example/d/5
2. Inspect recent deploys via "kubectl rollout history" within last 30m
3. Look at error sample in Loki: `{service="subsystem-5"} |~ "ERROR"`

## Mitigation

- Roll back the most recent deploy if the timing aligns
- Disable feature flag `subsystem_5_v5` via the flag UI
- Scale up replicas by 50% temporarily

## Validation

- Page resolves
- Error rate < 0.1% for 10 minutes
- No backlog in queue `subsystem_5_dlq`

## Postmortem

File postmortem within 48h using template at runbooks/_postmortem-template.md.
