# Chat-Controlled Call-Center Control Plane

Use this reference when Hermes or another chat agent controls calls through n8n and a managed voice platform.

## Default architecture

```text
Chat → isolated Hermes profile → authenticated n8n webhook → voice platform → SIP/PSTN provider
Voice-platform event → n8n normalization → signed Hermes webhook → agent/log/chat
```

Do not add a softphone, custom SIP SDK, PBX, or MCP server unless the requirement specifically needs a human SIP endpoint, proprietary media handling, owned extensions, or interactive tool access.

## Prerequisites

Confirm:

- n8n production webhook URL and whether n8n is local or remote;
- voice-platform private credential, assistant/agent ID, and outbound phone-number ID;
- carrier support for outbound PSTN, required regions, E.164 formatting, caller ID, and concurrency;
- consent, suppression, quiet-hour, timezone, recording, and campaign authorization rules;
- how uploaded files reach n8n: multipart, local storage, or object storage.

Never request secrets in chat. Store them in profile environment files, n8n credentials, or a secret manager.

## Isolated agent profile

1. Create a dedicated profile; reuse model authentication only with authorization.
2. Do not clone messaging tokens, sessions, unrelated memory, or gateway secrets.
3. Give the profile a narrow call-operations role with confirmation, consent, and truthful-status rules.
4. Install one operator client with a small, testable webhook interface.
5. Use independent secrets for agent-to-n8n requests, inbound agent webhooks, and each subscription.
6. Restrict secret files to mode `600`.
7. Probe ports before starting another gateway. Keep webhook ports consistent across config and environment files.

## Outbound command contract

Prefer stable actions:

- `call.now`, `call.schedule`, `call.cancel`, `call.status`
- `contact.upsert`, `contact.import`
- `campaign.create`, `campaign.start`
- `knowledge.ingest`

Example:

```json
{
  "action": "call.now",
  "requestId": "uuid",
  "sentAt": "ISO-8601 UTC",
  "payload": {
    "phone": "+<country><number>",
    "name": "optional",
    "assistantId": "optional override",
    "phoneNumberId": "optional override",
    "variables": {}
  }
}
```

Rules:

- Validate E.164 before sending.
- Use `requestId` as the idempotency key.
- Require `scheduledAt` and timezone for scheduled calls.
- A one-person explicit call-now request authorizes that call only.
- Require confirmation before campaign start after showing audience, volume, objective, and schedule.
- Return real request ID, provider call ID, status, or error. Webhook acceptance is not call completion.
- For file imports, use multipart with a JSON command part and binary file part. Use object storage above the chosen direct-upload ceiling.

## n8n workflow

- Protect the webhook with Header Auth.
- Parse JSON or multipart input and validate the action.
- Route immediate and scheduled calls separately; use a wait/scheduler mechanism for `scheduledAt`.
- Call the managed voice platform through a credential-backed HTTP node.
- Keep assistant and phone IDs in n8n environment values or explicit approved overrides.
- Import workflows inactive until credentials are selected and one test is approved.
- Implement contacts, campaigns, and knowledge ingestion as separate durable workflows or storage-backed services after schemas are defined. Do not present placeholder branches as CRUD.

## Inbound events

Normalize provider payloads to a stable envelope:

```json
{
  "event": "call.summary",
  "callId": "...",
  "status": "completed",
  "result": "...",
  "summary": "..."
}
```

Sign the exact JSON body with HMAC-SHA256 and send `X-Hub-Signature-256: sha256=<hex>` plus an event header matching the agent subscription filter. If n8n is remote, expose a local webhook only through authenticated HTTPS tunneling or a reverse proxy.

## Verification order

1. Operator-client syntax and E.164 rejection.
2. n8n workflow JSON parses and imports inactive.
3. Model authentication responds under the isolated profile.
4. Gateway reports running and the intended port listens.
5. Health endpoint responds after a bounded readiness loop.
6. A signed real-shaped event returns the expected acceptance code.
7. Logs show an agent response and no related error.
8. One approved end-to-end call proves the actual carrier path.
9. Only then test transfer, imports, scheduling, or campaigns.

## Edge cases

- Gateway health can pass while a CLI advertises a stale webhook URL if config and environment ports differ.
- A workflow switch branch does not prove that contact or campaign persistence exists.
- Keep webhook acceptance, provider call creation, ringing, answer, and terminal outcome as distinct states.
- Restart tests should use a readiness loop rather than one immediate health request.
