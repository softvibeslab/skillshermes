---
name: document-delivery
description: Create, validate, and deliver user-requested documents as PDF by email or messaging, with reliable attachment handling and sent-state verification. Use when a source Markdown/HTML/document must be rendered, attached, sent, and verified end to end.
version: 1.0.0
---

# Document Delivery

Turn an existing source document into a verified deliverable and send it through the user-authorized channel.

## Outcome

Complete the whole chain:

1. locate the canonical source;
2. render the requested format;
3. validate the artifact;
4. compose a concise message;
5. attach the correct file;
6. send only to the authorized recipient;
7. verify the sent record and attachment.

Do not report success after merely creating a draft or clicking Send.

## Workflow

### 1. Confirm scope from the request

Extract:

- source document;
- requested format;
- recipient and channel;
- subject or a sensible default;
- whether the user explicitly authorized sending.

A direct request such as “send this PDF to X” authorizes that exact recipient, attachment, and ordinary covering message. Do not broaden recipients, add CC/BCC, or include unrelated files.

### 2. Use the smallest rendering path

Prefer, in order:

1. an existing requested-format artifact that matches the current source;
2. an installed native converter;
3. Markdown/HTML conversion plus the browser’s native print-to-PDF;
4. GUI export only when no deterministic converter exists.

For Markdown on macOS, a minimal dependable path is:

```bash
pandoc input.md --standalone --css=print.css -o output.html
"/Applications/Google Chrome.app/Contents/MacOS/Google Chrome" \
  --headless --disable-gpu --no-pdf-header-footer \
  --print-to-pdf=output.pdf "file:///absolute/path/output.html"
```

Use a short print stylesheet; do not build a document-generation framework for one file.

### 3. Validate before delivery

Run the smallest checks that catch real failure:

```bash
pdfinfo output.pdf
pdftotext output.pdf - | sed -n '1,12p'
```

Confirm:

- file exists and is non-empty;
- page count is plausible;
- expected title/body text is present;
- page size is appropriate;
- no obvious clipping or blank output.

For high-stakes or visual documents, inspect at least the first page visually.

### 4. Select the delivery route

Prefer the first configured route that supports attachments:

1. email API/CLI with attachment support;
2. authenticated webmail UI;
3. configured desktop mail client;
4. send the file through the current messaging platform if the user accepts that channel.

A route that can send text but not attachments does not satisfy a PDF-delivery request.

### 5. Compose minimally

Default covering message:

```text
Subject: [Document title]

Hola [name],

Te envío adjunto [document description] en formato PDF.

Saludos,
[Sender]
```

Keep the body shorter than the document. Avoid exposing local paths, internal project notes, or tool details.

### 6. Attach reliably

Before sending, verify the visible attachment name and size.

For authenticated Gmail in a Chromium browser on macOS, if the native file picker is unreliable under background automation, place the file object—not its text path—on the clipboard and paste it into the focused composer:

```bash
osascript -e 'set the clipboard to (POSIX file "/absolute/path/document.pdf")'
```

Then focus the Gmail body and press `cmd+v`. Wait for the attachment chip to show the filename and completed size before sending.

See `references/gmail-macos-attachment.md` for the detailed fallback and verification sequence.

### 7. Send and verify

After sending:

- wait until “Sending…” clears;
- search Sent using a specific subject query;
- verify exactly one matching message;
- confirm the paperclip/attachment indicator;
- when possible, open the sent message and verify recipient, subject, and attachment name.

For Apple Mail on macOS, `send` returning success is not proof of delivery: verify the exact subject in Sent or, for self-addressed mail, the received copy in Inbox/All Mail. Check Drafts before retrying and remove a stale duplicate draft only after delivery is proven. See `references/apple-mail-macos-delivery.md`.

Only then report delivery.

## Safety boundaries

- Never type passwords, API keys, or recovery codes into automation.
- Stop on permission dialogs or authentication prompts that require secrets.
- Never infer a recipient from unrelated inbox content.
- Do not send a draft merely because the composer is complete.
- Do not retry a send blindly after an ambiguous error; check Sent first to prevent duplicates.
- Do not attach source files containing secrets or unrelated personal data.

## Pitfalls

- Treating PDF creation as completion when the user asked for delivery.
- Reporting success while Gmail still shows “Sending…”.
- Retrying after a save-to-Sent error without checking whether SMTP already delivered.
- Pasting a pathname as text instead of a file object.
- Clicking raw coordinates without recapturing and confirming the attachment chip.
- Sending from the wrong browser profile or email account.
- Using a polished interactive HTML renderer when a basic print stylesheet is sufficient.

## Completion report

State only verified facts:

- recipient;
- subject;
- format and page count when checked;
- sent-state verification.

Example:

> Sent to `person@example.com` with subject “Project Brief.” The attached PDF is 6 A4 pages; the message appears once in Sent with the attachment indicator.
