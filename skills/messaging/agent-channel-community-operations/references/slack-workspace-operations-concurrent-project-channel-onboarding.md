# Concurrent project-channel onboarding

Use this when one portfolio request is repeated across multiple Slack channels or Hermes sessions.

## Ownership and deduplication

- Assign one owner per project channel. A session triggered inside a project channel should update only that channel unless it is explicitly the portfolio orchestrator.
- Before posting, inspect recent session results or channel history for an existing status card. Update or correct it instead of posting a second independent version.
- The orchestrator owns the consolidated portfolio report; channel workers own their single project report.
- Treat successful message delivery, bot membership, and an agent-generated reply as separate checks.

## Canonical channel → project map

Build a single map before broadcasting:

| Field | Meaning |
|---|---|
| channel | Exact Slack slug and channel ID |
| project | Human project/product name |
| canonical_path | Owning repository or directory |
| context_file | Durable context document, if created |
| evidence_time | When Git/tests/services were checked |
| confidence | confirmed or candidate |

Do not let two workers infer different repositories from similar names. If a match is only a candidate, label it and ask for confirmation in the status card. If a wrong mapping was already posted, publish a short correction naming the canonical path and mark the earlier card superseded.

## Stop semantics

`stop`, `para`, `paraaa`, or an equivalent interruption means immediate cancellation of pending GUI/API side effects. Do not finish the current batch. Resume only after a later explicit instruction authorizes new actions; then rediscover live Slack state rather than continuing from stale UI references.

## Minimal status card

Post one card per channel:

- Purpose
- Verified state and evidence time
- Progress
- Blockers/risks
- Next three actions
- Canonical project path

Avoid duplicate prose, speculative completion claims, and context copied from a similarly named project.
