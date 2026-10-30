# Hermes model/runtime preflight: availability ≠ free access

Use this before switching a Hermes profile to a newly requested model, especially local/cloud hybrids such as Ollama `:cloud` tags.

## Durable rule

Treat these as separate gates:

1. **Name exists** — verify the exact model ID in the provider's live catalog. Do not infer from stale docs or memory.
2. **Artifact is installed** — a successful `pull` may download only a tiny cloud manifest, not model weights.
3. **Account is entitled** — run one minimal inference request. A manifest can be installed while execution still returns `401/403` or “subscription required.”
4. **Hermes is configured** — only after inference succeeds, update the target profile's provider/model/base URL.
5. **Hermes works end to end** — run one short Hermes query and verify the response.

Never change the profile default at gate 1 or 2. Keep the known-good model until gate 3 succeeds.

## Minimal checks

```bash
# Live OpenRouter catalog (exact IDs and pricing)
curl -fsSL https://openrouter.ai/api/v1/models -o /tmp/openrouter-models.json
python3 - /tmp/openrouter-models.json <<'PY'
import json, sys
with open(sys.argv[1]) as f:
    models = json.load(f)["data"]
for m in models:
    if "kimi" in (m["id"] + " " + m.get("name", "")).lower():
        print(m["id"], m.get("pricing", {}))
PY

# Ollama artifact presence
ollama list

# Entitlement/runtime probe — this is the decisive check
ollama run <exact-model-tag> 'Reply only: OK'
```

Avoid piping downloaded JSON directly into an interpreter; save it, then parse it as data.

## Interpreting results

- `pull success` + inference `403 subscription required`: installed cloud pointer, not usable/free access.
- Catalog entry without explicit zero pricing or `:free`: do not call it free.
- Local model tag with very large weights: inspect RAM, disk, CPU, and GPU before pulling; do not assume a server with ample disk has enough accelerator memory.
- No API key/entitlement: report the exact missing prerequisite and leave Hermes unchanged.

## Remote-server boundary

A pasted SSH transcript is context, not control of that existing terminal session. Before promising to act remotely, test non-interactive SSH access:

```bash
ssh -o BatchMode=yes -o ConnectTimeout=10 user@host 'true'
```

If it fails with `Permission denied (publickey,password)`, do not request or expose the server password. Ask the user to run the read-only probe in their terminal or configure SSH-key access. A user answering `1` in chat does not select option 1 inside a separate Claude Code/SSH TTY.
