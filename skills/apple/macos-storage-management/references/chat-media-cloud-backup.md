# Verified chat-media backup before cleanup

Use this pattern when a chat app owns hundreds of GB of media and the user wants a cloud backup before reclaiming disk space.

## Scope and safety

- Preserve chat databases, contacts, credentials, sessions, and settings by default. Back up/delete only the media tree unless the user explicitly requests a full application-state archive.
- Quit the app before inventorying. macOS service extensions may relaunch independently; pause or terminate them during the snapshot and guarantee they resume when the job exits.
- Never delete an app container wholesale. If in-app deletion is practical, prefer it. If direct media deletion is explicitly authorized, delete only files recorded in the verified snapshot and only when size and `mtime_ns` still match.

## Preflight

1. Measure source bytes and file count.
2. Confirm remote quota exceeds source size plus reasonable overhead.
3. Fetch target-folder metadata and verify `canAddChildren`/write access with a disposable create-and-trash probe.
4. Confirm enough local free space for one archive chunk.
5. Keep the Mac awake for the bounded job (`caffeinate -w PID`).

## Large trees: archive, do not upload file-by-file

Hundreds of thousands of small files can take days of API metadata calls. Build independently restorable uncompressed TAR chunks (typically 4–8 GB; media is already compressed) and upload tens of archives instead.

Maintain a durable SQLite manifest containing:

- relative path
- byte size
- nanosecond mtime
- chunk number
- per-chunk file count/source bytes
- remote file ID, archive size, and checksum
- completion/deletion markers

Build chunks deterministically. For each chunk:

1. Revalidate every source file against manifest size and mtime.
2. Create one TAR with relative paths.
3. Reopen it and verify member count.
4. Compute local MD5.
5. Upload resumably.
6. Compare remote `size` and `md5Checksum` with the local archive.
7. Persist the remote ID/checksum, then remove only the temporary TAR.

Do not remove source media until every chunk and the restore manifest are remotely verified. After full verification, unlink only unchanged snapshot files; skip new or modified files. Remove empty directories afterward.

## Resumption and idempotency

- Persist state after every verified chunk.
- On restart, skip completed chunks.
- Before re-uploading a named archive, search the destination. Reuse it only when name, size, and checksum all match; otherwise trash the conflicting remote object and upload again.
- A failed or interrupted job must leave source media untouched unless the global verification marker was already committed.

## Google Drive specifics

- Reading folder metadata does not prove write access. Perform a disposable write probe first.
- Uploading to an arbitrary existing folder generally requires the full Drive OAuth scope (`https://www.googleapis.com/auth/drive`), not `drive.readonly`; changing scopes requires fresh consent.
- Use resumable uploads and retry transient HTTP/network errors with bounded exponential backoff.
- Drive reports `md5Checksum` for ordinary uploaded files; use it together with byte size as the deletion gate.

## Restore contract

Upload a human-readable restore index plus the SQLite manifest. Each TAR should be independently extractable:

```sh
tar -xf whatsapp-media-NNN-of-NNN.tar
```

Record clearly that media archives are not a native chat-app backup and that local chat databases were intentionally preserved.