---
name: voice-agent-telephony-integration
description: Design and validate voice-agent and call-center integrations across orchestration tools, voice AI platforms, SIP infrastructure, softphones, SDKs, carriers, dashboards, and CRM workflows. Use for Vapi/Twilio-like voice agents, SIP trunks, PSTN calling, transfers, outbound campaigns, n8n automation, or deciding whether a softphone/PBX/SDK is actually needed.
---

# Voice Agent Telephony Integration

Design the smallest reliable path from an administrative interface to a real telephone call. Treat product names as roles, not interchangeable boxes.

## Start with the call path

Write the intended path before recommending software:

```text
Chat/Form/Dashboard → Orchestrator → Voice-agent platform → SIP/PSTN carrier → Contact
                                      ↘ optional transfer → Human endpoint
```

For each hop, identify protocol, authentication, ownership, callback/event path, and failure boundary.

## Role separation

- **Orchestrator** (for example n8n): contacts, imports, campaign state, scheduling, HTTP calls, webhooks, retries, audit. It is not a media engine.
- **Voice-agent platform** (for example Vapi): conversational runtime, speech pipeline, call control, tools, recordings/transcripts, transfers, call API. Prefer its REST API for deterministic orchestration; MCP is optional for interactive agent tooling.
- **Carrier / SIP trunk provider**: DID/caller ID, PSTN ingress/egress, balance, geographic permissions, concurrency, emergency/regulatory constraints.
- **Softphone**: human endpoint and manual test client. Never assume it is required for automated calling.
- **Client SDK**: library for building a custom SIP user agent. It is not a ready REST service; backend control normally requires a deployed adapter/daemon.
- **SIP server / proxy / PBX / B2BUA**: registration, routing, extensions, policy, transcoding, conferencing, or trunk interconnection. It does not automatically include PSTN service.
- **Account-management API**: may manage SIP identities but not originate calls. Verify scope before treating any REST API as call control.

## Decision ladder

Stop at the first route that satisfies the requirement:

1. **Voice platform + carrier directly** — default MVP. No softphone, SDK, or self-hosted SIP server.
2. **Add a human endpoint** — another softphone, SIP desk phone, WebRTC client, or ordinary telephone destination when transfer is required.
3. **Add a PBX/SIP server** — only for owned extensions, registration, internal routing, policies, multi-tenant service, advanced transfer, or provider compatibility.
4. **Build with a SIP SDK** — only when custom media/device control, a proprietary client, or removing the managed voice platform is an explicit requirement.

Do not install infrastructure merely because it appears in the same vendor ecosystem.

## Mandatory carrier discovery gate

Do not generate production workflow JSON or claim readiness until these are confirmed:

- SIP host, port, transport (UDP/TCP/TLS), registration-vs-trunk model.
- Authentication model: digest credentials, IP ACL, mutual TLS, or token.
- Outbound PSTN permission, supported countries, DID/caller ID ownership.
- E.164 and provider-specific dial format.
- Codecs and DTMF mode.
- Concurrent-call and CPS limits.
- NAT/media requirements; RTP IP ranges and ports.
- Transfer support, especially SIP REFER or platform-mediated transfer.
- Webhook/event guarantees and provider call identifiers.
- Whether simultaneous registrations are allowed.

A SIP username that resembles a phone number is not proof of a DID. A successful registration is not proof of PSTN egress.

## Security and compliance

- Treat all SIP credentials, API keys, trunk addresses, and private routing data as secrets.
- If a credential appears in chat or logs, mark it compromised, redact it as `[REDACTED]`, and require rotation before tests.
- Store secrets in the orchestrator/platform credential manager; never embed them in prompts, code nodes, exported workflows, or screenshots.
- Require opt-in/consent records, suppression lists, quiet hours/time zones, caller identity rules, recording disclosure where applicable, and auditable campaign history.
- Use separate identities/credentials for automation and human operators when concurrent registration or routing could collide.

## Data and campaign workflow

For contact imports, use this minimum sequence:

```text
Upload → extract → normalize E.164 → validate → deduplicate → consent/suppression check
→ queue → rate/concurrency gate → create call → receive webhook → update state → retry policy
```

Accept documents/images only through an explicit extraction/OCR step. Preserve the original source and record confidence/errors; do not silently invent missing phone numbers.

Use idempotency keys and provider call IDs. Model terminal states separately from retryable transport failures. A single bounded worker/loop is enough for the MVP; add distributed queues only after measured throughput requires them.

## Chat-controlled call-center control plane

When the requirement is to create or schedule calls from chat, import contacts, run campaigns, or return call results to an agent, use this minimal bidirectional architecture:

```text
Chat → isolated Hermes profile → authenticated n8n webhook → voice platform → SIP/PSTN
Voice-platform event → n8n normalization → signed Hermes webhook → agent/log/chat
```

Keep the command contract action-based (`call.now`, `call.schedule`, `call.cancel`, `call.status`, `contact.upsert`, `contact.import`, `campaign.create`, `campaign.start`, `knowledge.ingest`). Validate E.164 numbers, use a UUID request ID for idempotency, require timezone-aware scheduling, and return provider call IDs and actual states rather than treating webhook acceptance as call completion.

An explicit one-person “call now” request authorizes only that call. Before starting a campaign, show the audience, volume, objective, and schedule and require explicit confirmation. Keep imported n8n workflows inactive until credentials are selected and a test call is approved. Use separate durable workflows/storage for contacts, campaigns, and knowledge ingestion once their schemas are known; an unconnected routing branch is not an implementation.

For inbound results, normalize provider events to a stable envelope, sign the exact JSON body with HMAC-SHA256, and expose local Hermes webhooks only through authenticated HTTPS tunneling or a reverse proxy. Use an isolated profile, independent secrets, restrictive file permissions, a narrow role, port-consistency checks, and a readiness loop after restarts.

See `references/call-center-control-plane.md` for the detailed command envelope, n8n pattern, profile boundaries, inbound event contract, and verification order. See `references/callcenter-agent-profile.md` for a session-specific implementation record that must be revalidated before reuse.

## Verification sequence

1. Rotate any exposed credential.
2. Prove one outbound PSTN call using the intended platform/carrier path.
3. Confirm caller ID, two-way audio, DTMF, codec, and webhook lifecycle.
4. Prove one transfer to the intended human endpoint if required.
5. Trigger the same call through the orchestrator.
6. Import a tiny consented contact fixture and verify dedupe/idempotency.
7. Only then enable batches with conservative concurrency.

## Pitfalls

- Do not automate a softphone GUI.
- Do not call a client SDK a REST API or MCP server unless official documentation explicitly provides one.
- Do not confuse SIP account management with call origination.
- Do not claim a proxy/B2BUA supplies PSTN numbers; it still needs a carrier/trunk.
- Do not share one SIP registration between a bot and an operator without proving the provider's contact-binding behavior.
- Do not build a dashboard before proving the underlying call path.

## References

- See `references/call-center-control-plane.md` for chat-controlled call operations, command envelopes, n8n routing, signed inbound events, and layered verification.
- See `references/callcenter-agent-profile.md` for a session-specific implementation record; revalidate every path, port, credential boundary, and historical verification before reuse.
- See `references/linphone-vapi-n8n.md` for a concrete role map and decision notes for Linphone/Flexisip/Liblinphone, Vapi, and n8n.
- See `references/hermes-n8n-control-plane.md` for isolated Hermes profile setup, credential-approval boundaries, the webhook command envelope, knowledge ingestion, and end-to-end verification.