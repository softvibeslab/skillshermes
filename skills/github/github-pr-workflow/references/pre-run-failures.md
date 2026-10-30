# Diagnosing GitHub Actions failures before a runner starts

Use this when a workflow concludes `failure` almost immediately, `gh run view --log-failed` has no logs, or old logs return HTTP 410.

## Signal

A job that never reached a runner commonly has:

- `steps: []`
- `runner_id: 0`
- empty `runner_name`
- duration of only a few seconds

This usually means GitHub rejected the job before checkout or test execution. Do not patch application code based only on the red CI badge.

## Deterministic probe

```bash
REPO=owner/repo
RUN_ID=123

# Find failed job IDs even when logs are gone.
gh run view "$RUN_ID" -R "$REPO" --json jobs,conclusion,url

JOB_ID=456
gh api "repos/$REPO/actions/jobs/$JOB_ID"
gh api "repos/$REPO/check-runs/$JOB_ID/annotations"
```

The check-run annotations endpoint often preserves the actual platform-level reason after downloadable logs have expired. Examples include account billing locks, policy restrictions, and malformed workflow configuration.

## Interpretation

1. If annotations identify a platform/account issue, report that as the root cause and stop changing code.
2. Reproduce tests locally to distinguish repository health from runner availability.
3. Account or payment UI requires the account owner; do not attempt payment actions automatically.
4. After the account-level issue is resolved, rerun the workflow and verify a runner is assigned and steps execute.
