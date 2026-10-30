# Evaluating third-party Hermes messaging plugins

Use before installing an external platform plugin into any live Hermes profile, especially a public gateway with broad tool access.

## Minimal review sequence

1. Clone without installing into Hermes. Inspect `README`, package metadata, plugin manifest, entry point, adapter, transport client, setup/secret writer, outbound tools, and tests.
2. Confirm what the product really is: direct platform integration versus a hosted relay. Map every trust boundary and identify who can observe message content, phone numbers, recipient metadata, media URLs, and credentials.
3. Inspect current upstream state: latest release versus source version, recent commits, open compatibility PRs, CI, license metadata, and maintenance activity. Treat an open compatibility report as evidence to test, not proof that every local Hermes version is affected.
4. Build the package in isolation. Run its tests against Hermes code without installing it into the live Hermes venv. For a small Python plugin, a useful pattern is:

```bash
PYTHONPATH="$HOME/.hermes/hermes-agent" \
uv run --with pytest --with pytest-asyncio --with pyyaml pytest -q
uv build
```

If tests import `gateway.*`, failure in a plain standalone venv usually means the parent Hermes package is absent, not that plugin logic failed. Add only the parent source path and its minimal import dependency, then rerun. Report both attempts accurately.
5. Remove generated `.venv`, lockfiles, and build artifacts created only for inspection; verify a clean git status.

## Security review checklist

- **Credential transport:** reject API keys in query strings; require authorization headers and TLS. Custom server URLs should not silently permit plaintext `ws://` except explicit loopback development.
- **Attachment downloads:** require HTTPS, trusted hosts, DNS/IP checks blocking loopback/private/link-local/metadata ranges, streaming byte limits, bounded concurrency, and per-message count/size limits. A size check after `resp.content` is already too late.
- **Replay/idempotency:** persist processed message IDs or server cursors. Local receive timestamps and in-memory state do not prevent duplicates after reconnect or restart.
- **Inbound authorization:** verify DM, group-member, and group-chat allowlists end to end. Do not assume registration metadata alone proves Hermes applies it before media download or side effects.
- **Agent tools:** inspect tools that contact arbitrary recipients, create groups, spend money, or send an initial message. Require recipient allowlists, rate limits, audit logs, and human approval in the handler itself where consequences are material.
- **Secret setup:** use masked input, atomic writes, and mode `0600`. Do not recommend shell commands that place live secrets in history or plaintext YAML.
- **Relay privacy:** document retention, subprocessors, data residency, incident response, and whether the relay can read content and metadata. TLS is not end-to-end encryption.
- **Reliability:** reject pending requests immediately on disconnect, expose fatal/degraded state, bound reconnect attempts deliberately, and avoid unbounded task creation.

## Public-profile gate

A plugin that can send real-world messages must not be enabled blindly in a public Telegram/Discord profile with terminal, file, messaging, or arbitrary agent tools.

Default safe deployment:

1. Dedicated private Hermes profile.
2. Platform-specific sender allowlist; never allow-all for initial rollout.
3. Expose the plugin toolset only to its own platform via `platform_toolsets`; do not map it to public Telegram.
4. Disable or wrap group creation / arbitrary-recipient tools until approval, rate limits, and recipient policy exist.
5. Use separate credentials, number, storage, and logs from public profiles.
6. Perform a live smoke test only after static review and local tests pass.

## Reporting

Separate verified evidence from inference. Include architecture, test/build results, current upstream/release status, prioritized risks with file/line references, and a clear fit verdict for private pilot versus public production. Do not equate passing unit tests with safe production readiness.
