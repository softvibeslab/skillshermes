# Approval-result attribution and recovery

## Observed lesson

During repository-specialist setup, the assistant attributed a blocked command to the user. The user disputed having rejected it. The visible follow-up found older log entries describing an approval request on a thread without a callback while prompt_toolkit was active, denied to avoid stdin deadlock. Those entries were from a different date/task; they were evidence of a possible failure mode, not the cause of the current block.

The assistant suggested exiting and continuing the CLI session. The visible record did not verify that this restored approval handling. Do not preserve that suggestion as a guaranteed fix or hardcode its command syntax without checking the installed CLI.

## Diagnostic checklist

1. Record the blocked operation and whether any preceding independent operations completed. A blocked batch does not prove its intended artifacts exist.
2. State only the known outcome: execution was blocked / approval did not complete.
3. Check the installed approval-result mapping and the actual caller. Separate explicit rejection from policy denial, callback exceptions, unavailable input, and expiry.
4. Correlate log timestamp, profile, command, and session. Report old matches explicitly as historical and redact secrets from command excerpts.
5. Keep security enabled. Diagnose read-only where authorized; do not route the blocked mutation through a different tool.
6. If an interactive restart is appropriate, verify the installed resume syntax and preserve a concise checkpoint: target profile, authorized scope, verified artifacts, blocked operation, next check.
7. On continuation, verify current state and restored approval handling before resuming the authorized mutation. Report recovery only after it is observed.

## User-facing wording

“Te creo: ese mensaje no demuestra que tú hayas pulsado Rechazar. La aprobación no se completó; todavía no confirmo si fue una política, un fallo de entrada o un timeout.”

Use the wording only as appropriate to the evidence; do not assert a specific runtime defect without current corroboration.
