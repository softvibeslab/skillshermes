# Apple Mail fallback on macOS

Use this when API/CLI and authenticated webmail routes are unavailable but Apple Mail already has a configured sending account.

## Reliable sequence

1. Create a **new outgoing message** with an exact subject, authorized recipient, short body, and absolute attachment paths.
2. Select the intended configured sending account explicitly when more than one account exists.
3. Send the new outgoing message.
4. Wait briefly for Mail sync.
5. Search by the exact subject across **Sent**, **Inbox/All Mail** (useful for self-addressed delivery), and **Drafts**.
6. Verify recipient and attachment count/names on the delivered or sent copy.
7. If a residual draft with the same subject remains after verified delivery, delete only that draft to prevent a later duplicate.

## Verification rule

AppleScript returning success from `send` is not delivery proof. Completion requires a matching message in Sent or a received copy in Inbox/All Mail with the expected recipient and attachments.

For self-addressed mail, Inbox receipt is strong end-to-end evidence that SMTP delivery completed. Keep the exact subject unique enough to distinguish the run.

## Duplicate prevention

If the first attempt appears to have become a draft:

- check Sent/Inbox before retrying;
- do not repeatedly call `send` on a mailbox-retrieved draft object;
- prefer composing one fresh outgoing message from the intended account;
- after delivery is verified, remove the stale draft.

## Attachment caveat

Mail’s scripting interface can report attachment metadata inconsistently while syncing. Verify the source files before send, attachment count on the message, and—when names look duplicated or stale—inspect the received message rather than trusting a single transient metadata read.

## Completion evidence

Record only:

- exact recipient;
- exact subject;
- sending route/account;
- delivered/sent mailbox where verified;
- attachment count and expected names;
- whether any duplicate draft was removed.
