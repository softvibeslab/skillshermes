# Hermes ↔ n8n control plane for call-center agents

Use this pattern when a chat-operated Hermes profile coordinates calls through n8n and a managed voice platform.

## Minimal ownership model

```text
Chat → isolated Hermes profile → authenticated n8n webhook → voice platform API → carrier
                                      ↘ event/state store ← platform webhooks
```

- Hermes interprets operator intent, validates required fields, and submits commands.
- n8n owns scheduling, retries, idempotency, provider credentials, call-state updates, and callbacks.
- The voice platform owns media/conversation runtime.
- The carrier owns PSTN/SIP connectivity.

Do not make the Hermes chat process wait for scheduled or long-running calls. n8n should acknowledge immediately, execute asynchronously, and publish status events.

## Profile setup boundary

Creating a profile and sharing credentials are separate security decisions.

1. Create the isolated profile and its identity first.
2. Define the minimum tools and webhook contract without secrets.
3. Ask for explicit approval before cloning or copying authentication from another profile.
4. If reuse is approved, prefer the profile manager's supported clone/setup path over manual file copying.
5. If reuse is not approved, authenticate the new profile independently.
6. Add messaging-platform tokens only when the user explicitly requests that channel.

Never combine credential transfer and multiple configuration edits in one compound command. A denied approval can stop the command mid-flight and leave uncertain partial state. Make the authentication handoff its own auditable step, then verify the profile before continuing.

## Command envelope

Use one versioned webhook and a small action vocabulary:

```json
{
  "version": 1,
  "requestId": "stable-idempotency-key",
  "action": "call.now",
  "requestedAt": "2026-01-01T12:00:00Z",
  "requestedBy": "chat-user-or-agent-id",
  "payload": {}
}
```

Recommended MVP actions:

- `call.now`: destination, assistant/agent, caller identity, campaign/contact IDs.
- `call.schedule`: same fields plus an ISO-8601 time and timezone.
- `call.cancel`: internal job ID or provider call ID.
- `call.status`: internal job ID or provider call ID.
- `contact.upsert`: normalized contact plus consent provenance.
- `knowledge.ingest`: file/source reference, MIME type, scope, and intended assistant.

Return `202 Accepted` with `requestId` and an n8n job ID. Final results arrive through status polling or a separate authenticated event webhook.

## Security

- Put Vapi/carrier credentials only in n8n's credential store or the voice platform.
- Authenticate Hermes → n8n using a header credential or HMAC signature; never put secrets in query strings.
- Use a different secret for n8n → Hermes callbacks.
- Log request IDs and redacted metadata, not phone numbers, document contents, or credentials.
- Reject unknown actions, missing consent evidence, invalid E.164 numbers, and past/ambiguous schedule times.

## Knowledge-base ingestion

Upload binary files to controlled storage first; send n8n a reference rather than embedding large files in chat webhook JSON. n8n then performs extraction/OCR, malware/type checks where needed, normalization, chunking/indexing or provider upload, and records the resulting knowledge-base ID. Do not let a call start against a newly uploaded knowledge base until ingestion reports a terminal success state.

## Verification

1. Profile starts and can use its configured model without exposing credentials.
2. A signed test command reaches n8n and returns `202`.
3. Replaying the same `requestId` does not create a second call.
4. One consented test number completes the full call lifecycle.
5. n8n records provider IDs and sends a redacted final status event.
6. Scheduling and cancellation are tested before batch campaigns.
