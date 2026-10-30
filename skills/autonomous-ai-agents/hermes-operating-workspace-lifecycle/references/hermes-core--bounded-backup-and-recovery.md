# Bounded runtime backups and recoverability

## Failure pattern

A maintenance backup followed a symlink into unrelated personal files, producing an oversized partial copy. The durable lesson is scope enforcement, not a particular path, version, or tool failure.

## Before copying

- Identify exact source roots and a new, private destination outside all source trees. Account for symlinked ancestors when checking containment.
- Inventory entries with lstat. Do not resolve every entry and recursively copy its target. Preserve symbolic links as links; inventory external targets as excluded dependencies, not as automatically authorized sources.
- Exclude sockets, devices, FIFOs, and recursive backup directories. Explain exclusions and required external dependencies in a private manifest.
- Verify the chosen backup/export implementation's link behavior, including root links. A supported command is not proof that traversal is bounded.
- Estimate logical bytes, file count, free space, and extraction headroom. Use private directory/file permissions from creation, not only after completion.
- Test the exact copying mechanism on a disposable fixture containing an external-directory symlink and a cycle. Assert external contents are not copied and traversal terminates. Never claim this check ran without executing it.

## While copying

Use tracked background execution with completion notification for long bounded work. Record the process handle and generated destination before starting. Monitor progress against inventory; stop on unexpected scope or growth. Do not activate a candidate while the backup remains partial or unverified.

## Recovery gate

Archive existence, size, checksum, and integrity test are not sufficient proof of restoration. Inspect member paths and link behavior before extracting; reject traversal outside the test destination. Extract to an isolated private directory, validate required configuration/state and database integrity, and account for mutable SQLite state using a consistent snapshot or quiescence. Do not launch cloned bots or scheduled jobs from restored state.

Preserve the old source revision and runtime environment as well as state: switching a Git branch alone does not undo changed dependencies. A backup commit also has a different SHA from its base; record and verify both distinctly.

## Failure handling

Stop only the identified backup process, then inspect its exact output boundary. Label partial artifacts explicitly. Delete them only within authorized scope, without following links, and preserve prior verified backups. Report measured facts rather than claiming recoverability based on a prior assistant message. Resume safe preparation only within current permissions; never route around a denied operation.

Do candidate preparation and reversible checks before the downtime window where possible. Quiesce for the consistent final snapshot and activation; record previously active gateways and define their restoration path before stopping them.
