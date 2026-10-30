# Dedicated profile with a shared Slack coordination channel

Use this pattern when the user wants a specialized Hermes profile and a Slack workroom, but has not provisioned a separate Slack app/token for that profile.

## Safe minimal setup

1. Create a **fresh** profile with a role description; do not clone all runtime state.
2. Copy only the known-good `config.yaml` and model `auth.json` when the profile needs the same model access.
3. Do **not** copy `.env`; this prevents inherited Telegram/Slack/WhatsApp credentials from launching a duplicate gateway.
4. Write a focused `SOUL.md` with mission, workflow, trust boundaries, states, evidence, and report format.
5. Set `terminal.cwd` to the durable operating repository when one exists.
6. Run one short `chat -q` smoke test that checks the role's most important approval and safety rules.
7. Create/reuse one Slack channel, invite the orchestrator bot and human owner, set topic/purpose, post the operating contract, and verify channel history.
8. Register two separate connections:
   - orchestrator → profile: `active` after the one-shot profile test passes;
   - Slack channel → profile: `documented` until an actual router or dedicated gateway proves delivery.

## Truthful activation states

A specialized profile can be operational through CLI/orchestrator handoff while its dedicated Slack routing is not active. Report these separately. A channel message posted by the shared/default bot proves channel access, not that the specialized profile handled the message.

Do not start a second Socket Mode gateway with the same Slack app credentials. Activate direct channel → profile delivery only after one of these exists:

- a separate Slack app/token for the profile; or
- an explicit, tested channel router owned by the orchestrator.

## Verification

- Profile appears in `hermes profile list` with the intended model.
- `.env` is absent or contains only profile-specific credentials.
- `SOUL.md` exists and the smoke test repeats the key approval boundary.
- Slack channel has the human owner and orchestrator bot.
- Topic, purpose, and initial status message read back successfully.
- Durable registry labels untested Slack routing `documented`, never `active`.
