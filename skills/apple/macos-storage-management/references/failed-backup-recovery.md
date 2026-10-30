# Recovering space from a failed recursive backup

Use when an interrupted backup expanded beyond its intended source or exhausted disk space. This is recovery of a disposable partial copy, not permission to remove backups generally.

## Establish scope

1. Read the execution log and identify the exact destination created by the failed attempt. Preserve the source, historical backups, and staged installations.
2. Inspect symlinks before retrying a recursive copy. A profile's `home` link can point to the real user home; a copy that follows it can include unrelated data or even reach its own destination. Preserve links without dereferencing and test that behavior on a small fixture first.
3. Confirm the copy writer and its descendants have stopped. A killed parent or negative signal exit code is not proof that all children stopped, nor proof of backup success.
4. Interpret process matches, not just match counts: `pgrep -fl 'rsync'` can match macOS `colorsyncd` and `colorsync.useragent`. Inspect executable names and arguments; never terminate those system services based on the substring.
5. Measure only the named partial destination without following links, e.g. `du -shP /absolute/partial-backup`, and record `df -h` for its volume. Do not equate folder size to guaranteed recoverable APFS space.

## Authorized removal

- Ask for explicit approval naming the exact partial-backup directory. A request to update software is not blanket deletion permission.
- Before deletion, reject an empty path, filesystem root, user home, source directory, backup parent directory, or a destination that is itself a symlink. Verify the path against the execution log. Avoid wildcards and trailing slashes.
- Delete only that confirmed destination using the normal approval-controlled tool. Do not bypass a denied execution with a different tool, command spelling, or user-run deletion workaround.
- Verify destination absence, protected source/staging paths still present, and current free space. Presence checks establish existence, not complete content integrity or application health.
- Report measured free space after removal, not a causal recovery figure inferred from an earlier measurement; unrelated writes/deletions and APFS accounting can change it.

## Resume safely

Do not rerun the failed backup unchanged. Correct link handling, exclude sockets as non-restorable runtime objects, preserve private permissions, monitor free space, and make consistent database copies (for SQLite, its backup API). Validate integrity and a restoration into an isolated destination before calling the replacement backup restorable or proceeding with a production upgrade.
