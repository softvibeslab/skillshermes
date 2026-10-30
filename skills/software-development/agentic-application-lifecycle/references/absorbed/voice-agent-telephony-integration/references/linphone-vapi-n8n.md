# Linphone + Vapi + n8n role map

Use this note when the user wants an automated call center “using Linphone” but the real requirement is chat/dashboard-controlled voice calls.

## Minimal recommended route

```text
Chat / form / CRUD dashboard
→ n8n (contacts, campaign state, HTTP calls, webhooks)
→ Vapi REST API (voice agent and call lifecycle)
→ compatible SIP trunk / PSTN carrier
→ real telephone number
```

Linphone Desktop is optional and should be limited to manual testing or a human transfer endpoint.

## Product boundaries

### Linphone Desktop

A graphical SIP user agent/softphone. Useful for a human operator or manual SIP test. It is not the backend automation API and its GUI should not be automated.

### Liblinphone / Linphone SDK

Cross-platform client library used to build SIP applications. It can register SIP identities and control calls, but using it headlessly requires compiling/deploying code, running the event loop/media stack, and exposing a custom control adapter if n8n needs HTTP access. Use only when building a custom client/service is intentional.

### Flexisip

Server-side SIP suite: proxy, authentication/routing, presence, conferencing, push, and B2BUA/trunk interconnection. It can sit beside systems such as Asterisk or FreeSWITCH. It is infrastructure, not a carrier, and does not itself provide PSTN lines or virtual numbers.

Flexisip Account Manager exposes FlexiAPI for SIP account/identity administration. That API must not be mistaken for an API that originates calls.

Flexisip is justified when the project needs its own SIP domain, extensions, registrations, policies, routing, push support, conferencing, multi-tenant service, or B2BUA interconnection. Skip it for a managed voice-platform MVP.

### Vapi

Managed voice-agent/call-control layer. For n8n, REST plus webhooks is the simplest deterministic integration. MCP is useful for model-driven tool access but is not required for the basic outbound-call workflow. BYO SIP requires a compatible trunk/carrier configuration; ordinary softphone credentials may not be sufficient.

### n8n

Administrative and workflow layer: chat/form triggers, file extraction, normalized contact records, campaign funnel, HTTP calls to Vapi, webhook processing, idempotency, retries, and audit. It does not replace the SIP media or PSTN layer.

## Headless interpretation

- **Without Linphone Desktop:** yes; use Vapi + carrier, or build a Liblinphone-based service.
- **Without any Linphone component:** yes; Vapi + carrier is the preferred MVP.
- **Without installing anything anywhere:** only if n8n and Vapi are hosted services and the carrier is managed. A self-hosted SDK, daemon, PBX, or Flexisip still means deploying software.

## Human transfers without Linphone Desktop

Transfer to one of:

- Another SIP softphone.
- SIP desk phone.
- Browser WebRTC endpoint.
- PBX extension.
- Ordinary mobile/landline through PSTN.

Confirm how Vapi and the carrier perform the transfer (for example SIP REFER versus platform-mediated bridge) before choosing the endpoint.

## Provider question set

Ask the carrier for:

1. SIP host, port, and UDP/TCP/TLS transport.
2. Registration account versus trunk model.
3. Credential or IP-ACL authentication.
4. DID/E.164 number and caller-ID rules.
5. Outbound PSTN countries and dial format.
6. Codecs and DTMF.
7. Concurrent calls/CPS.
8. RTP/IP allowlists.
9. External platform compatibility.
10. SIP REFER and transfer behavior.
11. Simultaneous registration policy.

Never infer DID/PSTN capability from the username or from registration success.

## Security note

If SIP credentials were pasted into a conversation, redact all values, rotate the password before any test, and place the replacement only in managed credentials. Do not reproduce the compromised values in summaries or examples.

## Primary sources

- Flexisip overview: https://www.linphone.org/en/flexisip-sip-server/
- Flexisip repository: https://gitlab.linphone.org/BC/public/flexisip
- Liblinphone SDK: https://www.linphone.org/en/liblinphone-voip-sdk/
- Vapi SIP trunking: https://docs.vapi.ai/advanced/sip/sip-trunk
- Vapi MCP: https://docs.vapi.ai/tools/mcp
