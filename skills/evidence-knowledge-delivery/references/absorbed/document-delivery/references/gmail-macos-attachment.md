# Gmail attachment delivery on macOS

Use this fallback when the user is already authenticated in Gmail in a Chromium browser and API/CLI attachment support is unavailable.

## Preconditions

- The user explicitly authorized the recipient and document.
- The PDF has already passed `pdfinfo` and `pdftotext` checks.
- The correct Gmail account is visible in the browser title or account UI.
- No login, permission, or password prompt is present.

## Reliable sequence

1. Open Gmail in the existing browser profile without replacing the user’s current tab when possible.
2. Verify the account identity from the Gmail title/account UI.
3. Open a new composer.
4. Fill recipient, subject, and a short body.
5. Put the PDF file object on the macOS clipboard:

   ```bash
   osascript -e 'set the clipboard to (POSIX file "/absolute/path/file.pdf")'
   ```

6. Focus the Gmail message body and press `cmd+v`.
7. Wait for an attachment chip showing:
   - expected filename;
   - plausible size;
   - no upload spinner or error.
8. Send with the visible Send control or `cmd+return`.
9. Wait for the composer to close and any “Sending…” indicator to clear.
10. Verify with a Sent search:

    ```text
    in:sent subject:"Exact subject"
    ```

11. Confirm exactly one result and a paperclip indicator. Open it if recipient or attachment identity is ambiguous.

## Why clipboard paste works

The AppleScript command places a file object (`public.file-url`) on the pasteboard. Gmail interprets the paste as an uploaded attachment. Copying the pathname as plain text does not.

## Duplicate prevention

If the UI disappears but confirmation is unclear, search Sent before retrying. A transport may have succeeded even if a later UI or save-state action failed.

## UI automation notes

- Prefer accessibility-element clicks over coordinates.
- When Gmail exposes unlabeled toolbar buttons, clipboard-paste avoids the native file picker entirely.
- After every state-changing action, recapture and verify the new state.
- Background automation may target an unexpected frontmost app for generic keystrokes; explicitly focus/click the Gmail text area before pasting or sending.
- Do not click authentication, permission, password, or recovery dialogs.

## Minimal verification receipt

Record only:

- recipient;
- subject;
- attachment filename and observed size;
- Sent search result count;
- send timestamp if visibly available.
