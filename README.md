# First Signal synthetic source repository

This public repository contains **demonstration code only**. It has no production source, telemetry, credentials, customer data, or real on-call contacts.

First Signal uses its immutable Git commits to demonstrate an important incident-investigation rule:

```text
affected service + environment + instance + timestamp
  -> runtime artifact digest
  -> build provenance
  -> repository + exact full commit SHA
  -> exact source and deployed-revision diff
```

The `shipping` example deliberately contains two deployed revisions. Version 1.4.0 allows a two-second carrier deadline and retries; version 1.5.0 reduces the deadline to 0.2 seconds and removes retries. Synthetic telemetry in the First Signal application compares the new and old rollout cohorts.

The repository's current `HEAD` may be newer than the simulated deployed commit. The investigator must use the full SHA proven by the runtime artifact record, never the latest branch or tag.
