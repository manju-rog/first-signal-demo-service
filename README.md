# First Signal demo service

This public repository is a **fully synthetic source-history fixture** for the First Signal production-support investigation MVP. It contains no production code, telemetry, credentials, customer data, or real escalation contacts.

## Demonstrated incident

A partial rollout places synthetic release 1.5.0 on one shipping instance. Quote requests begin timing out even though the carrier remains healthy and an older-build peer succeeds under comparable traffic.

First Signal resolves the affected instance to an immutable artifact, maps that artifact to an exact full commit SHA, reads this file at that revision, and compares it with the previous relevant deployed revision.

## Deliberate source history

- **Previous deployed build:** `3e59b332d84fe9d0ae2d4dd14ae3f0c12ed8b690` — 2.0-second timeout and two retries.
- **Affected deployed build:** `05f3d7cf6dacbd45fa0e52a0ed336cb8c5dc1552` — 0.2-second timeout and no retries.
- **Newer repository HEAD:** documentation and ownership commits intentionally come later. This proves that the investigator must not silently substitute the latest branch or tag for the code actually deployed.

The application combines this real GitHub history with visibly labeled synthetic deployment, telemetry, change, runbook, and ownership fixtures. The report should treat the release as likely associated because the exact deployed diff matches the failure timing and the old/new cohorts differ under comparable workload.

## Safety boundary

The demonstration is read-only from the investigator. It does not restart services, roll back releases, change configuration, operate queues, publish tickets, or execute text retrieved from logs or documentation.
