# Initial callcenter-agent implementation

Session-specific implementation record; validate paths and ports before reuse.

## Local profile

- Profile: `callcenter-agent`
- Home: `/Users/USERNAME/.hermes/profiles/callcenter-agent`
- Operator skill: `skills/callcenter-operator/`
- Webhook gateway port: `8664`
- Incoming route: `/webhooks/callcenter-events`
- Gateway service: `ai.hermes.gateway-callcenter-agent`

The profile reuses the default model/OAuth files with explicit user authorization, but has its own `.env` and no copied messaging tokens. `.env` and `auth.json` use mode `600`.

## Artifacts

- `/Users/USERNAME/Downloads/callcenter-agent-n8n-webhook.json`
- `/Users/USERNAME/Downloads/vapi-sip-outbound-n8n.json`
- `/Users/USERNAME/Downloads/callcenter-agent-SETUP.md`

## Environment contract

Hermes profile:

- `N8N_CALLCENTER_WEBHOOK_URL`
- `N8N_CALLCENTER_TOKEN`
- `WEBHOOK_ENABLED`
- `WEBHOOK_PORT`
- `WEBHOOK_SECRET`
- `CALLCENTER_EVENTS_WEBHOOK_SECRET`

n8n:

- Header Auth credential `Callcenter Agent Webhook Token`
- Header Auth credential `Vapi API`
- `VAPI_ASSISTANT_ID`
- `VAPI_PHONE_NUMBER_ID`

## Historically verified; revalidate before reuse

- Profile model responded successfully.
- Operator client syntax and self-test passed.
- Gateway listened on port 8664 and `/health` returned OK.
- Signed `call.summary` event returned `202 accepted`.
- Gateway log recorded the agent response with no matching error-log entry.

## Still external at the time of capture

- n8n was not installed or listening locally, so its production webhook URL remained unset.
- Real voice-platform credentials and IDs still needed configuration.
- No real phone call was placed.
- The imported n8n workflow implemented immediate and scheduled calls only. Contact CRUD, campaign persistence, and knowledge ingestion required separate workflows/storage after data-model selection.
