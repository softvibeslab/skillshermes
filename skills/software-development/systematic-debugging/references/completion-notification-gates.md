# Deferred completion notifications for stateful jobs

Use when a user asks for an email after a long-running job completes. Scheduling a check is not sending mail, and launching a worker is not completion.

## Reuse before scheduling
1. List existing scheduled jobs before creating anything. Reuse/update a matching completion watcher rather than adding a second sender.
2. Verify the configured mail CLI version and account availability without displaying credentials. Configuration presence is not proof of SMTP delivery.
3. Give the watcher a self-contained prompt: absolute project path, current run directory, expected status/checkpoint files, target for every branch, recipient, authorization, completion criteria, and duplicate-send policy. Do not rely on chat context.
4. When recovery creates a successor clone, update the existing watcher to follow the documented successor. Never infer which result is authoritative solely from directory modification times.

## Completion gate
Require successful final run state, every platform at the requested committed target, no unresolved pending work, and appropriate read-only integrity checks. A stale running state, one platform finishing, or an older report is insufficient. Preserve qualifications about approximate memory and accepted partial rounds in the notification.

The watcher is read-only with respect to the workload: it must not restart simulations, replay partial work, or silently repair results. A failed run must not trigger a success email. Only send failure notices if separately authorized.

## Prevent duplicate mail
- Check both a durable notification receipt and Sent mail before sending; reuse existing receipts even if they predate the watcher revision.
- Record a send attempt before submission, then record the confirmed result/message identifier afterward. Use a stable subject/run identifier for reconciliation.
- A crash after SMTP acceptance but before writing the receipt leaves an ambiguous attempt. Inspect Sent/provider evidence; do not blindly retry on a nonzero CLI exit. Delivery may succeed while saving the Sent copy fails.
- Once delivery is confirmed, subsequent ticks must not send again. Disable/remove the watcher when the scheduler permits it, or leave it inert behind the receipt.
- A repeat limit is a monitoring deadline, not evidence that the workload finished. Surface exhausted monitoring rather than letting the user's expected notification silently disappear.

## Communication
Say 'completion notice scheduled' only after the scheduler confirms the active watcher. Say 'email sent' only with delivery evidence. Include the recipient and check interval; do not imply real-time notification. Background-process completion notifications and periodic watcher checks are distinct mechanisms, and neither is guaranteed to run while the host/scheduler is stopped.

## Observed application
An interrupted multi-platform simulation had an existing email watcher. Reusing it and replacing its stale run path with the current recovery clone avoided duplicate schedulers and checking obsolete results. The mail account was configured, but no success email was due until both platforms passed the completion gate.
