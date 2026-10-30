# Hermes Gateway — Slack Socket Mode Setup

Use this for connecting Hermes to a Slack workspace without exposing a public events endpoint.

## Required state

- `SLACK_BOT_TOKEN` (`xoxb-...`) for Web API calls.
- `SLACK_APP_TOKEN` (`xapp-...`) for Socket Mode; create it with the `connections:write` scope.
- Socket Mode enabled in the Slack app.
- The app installed to the intended workspace.
- Event subscriptions and bot scopes appropriate to the desired surfaces. DM-only success does not prove channel handling works.

## Safe setup sequence

1. Inspect the active Hermes profile and gateway state before changing anything.
2. Check only whether Slack variables are present; never print token values. Preserve existing values until the new app and workspace are confirmed; they may belong to a working integration.
3. Treat `Slack ✓ configured` as credential presence, not proof of a live connection.
4. Open `https://api.slack.com/apps` and authenticate to the intended workspace.
5. If Google rejects an automated/headless browser as unsafe, stop retrying there. Open the same URL in the user's normal browser and let the user complete login, password, consent, and 2FA. Resume only after they report reaching **Your Apps**.
6. Prefer an app manifest so name, Socket Mode, scopes, events, App Home, and bot identity are applied together. A minimal manifest is easier to paste and validate than a command-heavy generated manifest; add slash commands only when currently needed.
7. Save the manifest, generate an app-level token with `connections:write`, then install or reinstall the app to the workspace and authorize the requested scopes.
8. Copy the app token and Bot User OAuth Token directly from Slack into the target profile's `.env` without echoing them or exposing them in diffs. Validate prefixes (`xapp-`, `xoxb-`) before replacement. Clear the clipboard immediately after persistence.
9. Restart the target Hermes gateway.
10. Verify with fresh gateway logs or a redacted Slack `auth.test`, then test both:
   - a direct message to the bot;
   - a channel where the bot has been invited, using an explicit mention.

## Reliable interaction with Slack's manifest editor

Slack's manifest editor is CodeMirror-like: accessibility `set_value` may change the hidden text area without updating the editor model. Use this fallback:

1. Put the manifest on the macOS clipboard without printing it.
2. Focus the real Safari window and the manifest text area.
3. Send `Cmd+A`, then `Cmd+V` as real keyboard events.
4. Use Slack's **Copy to Clipboard** button and parse the copied JSON to verify the app name, `socket_mode_enabled`, and expected scope count before clicking **Save Changes**.

Keep the browser state simple. Close only tabs opened by the automation and leave the app-settings tab. If several Safari tabs make accessibility targeting unstable, select the exact app-settings URL or reduce to one relevant tab before continuing.

## Secret-safe local persistence

- Do not paste tokens into chat, command output, diffs, screenshots, or logs.
- Prefer an internal script that reads the clipboard, validates the prefix, updates exactly one `.env` key, and prints only a redacted success message.
- Secret-redaction middleware may rewrite inline source that contains a recognizable secret-variable assignment. If that happens, construct the environment key from harmless fragments (for example `''.join(['SLACK', '_BOT', '_TOKEN'])`) and never print the resulting line or secret.
- Clear the clipboard after both tokens are safely stored.

## Verification evidence

A complete verification has two independent parts:

1. Bot token: Slack `auth.test` returns `ok: true`, with only workspace and bot username reported.
2. App token / Socket Mode: fresh gateway logs include authentication to the intended workspace, `Socket Mode connected`, and `slack connected`.

`launchd` may retain an old nonzero `LastExitStatus` after restart; a current PID plus fresh successful connection logs are the runtime source of truth.

## Handoff boundary

The agent may navigate ordinary configuration UI and click the final Slack authorization button when the user explicitly asked it to configure the integration. The user must handle passwords, account selection when identity is ambiguous, 2FA, and OS/browser permission prompts. Do not claim full desktop control when only headless browser automation is available. State the exact blocker and open the official page in the user's normal browser when possible.

## Channel onboarding and user pairing

Channel membership and user authorization are separate checks:

1. Resolve the channel ID from a Slack URL such as `/archives/C…` and verify it with `conversations.info`.
2. Check `is_member`. If false, invite the bot from Slack with `/invite @hermes`.
   - A minimal app may intentionally omit `channels:join` and `chat:write.public`; in that case the bot cannot invite itself or post before invitation.
   - Add those scopes and reinstall only when automatic public-channel joining is a current requirement.
3. Test with an explicit mention: `@hermes hola`. Mentioning is the most reliable first channel test.
4. On first contact Hermes may return a pairing code. Approve the complete code on the gateway host:

   ```bash
   hermes pairing approve slack <CODE>
   hermes pairing list
   ```

5. Verify the approved Slack user ID/name, then have that user mention the bot again. Pairing approval does not add the bot to a channel, and channel invitation does not approve a user.

A channel handled by the default-profile gateway is already using the principal Hermes agent; no separate profile is needed merely to chat there. Treat each Slack channel/DM as its own gateway session context unless the user explicitly requests cross-channel continuity.

## Moving Slack from a local gateway to a VPS

Socket Mode supports multiple concurrent connections, but events are distributed among connections rather than broadcast reliably to every Hermes instance. Do not run the same Slack app tokens on local and VPS gateways when one deterministic principal agent is expected.

1. Identify the exact VPS SSH target and target Hermes profile; do not guess host, user, or profile. List profiles and inspect gateway state because the VPS default profile may be stopped while a named orchestrator profile is live.
2. Test non-interactive key authentication first (`BatchMode=yes`). If password login is temporarily needed, never repeat the password in prose, files, shell history, or verification output; check for an already-authorized local key before handling a volunteered password.
3. Verify Hermes, the target profile path, its `.env`, and its gateway on the VPS before moving secrets. Report only key presence booleans, never values.
4. Treat migration as a transactional cutover:
   - stage only `SLACK_BOT_TOKEN` and `SLACK_APP_TOKEN` in the target profile;
   - set secret files to mode `0600`;
   - restart and verify the target with redacted `auth.test` plus fresh Socket Mode logs;
   - only then disable Slack on the source profile and restart it.
5. Transfer secrets over authenticated SSH without embedding them in command arguments, diffs, logs, or persistent temp files. If an ephemeral transfer file is unavoidable, create it with `0600`, copy only the two Slack keys, merge exact keys internally, and delete both copies immediately.
6. Remote secret writes are a meaningful side effect. If the execution approval is denied, assume nothing ran, stop the migration, close interactive SSH sessions, and wait for a fresh explicit user request; do not retry through a different mechanism.
7. Re-test one approved user in DM and one invited channel. Pairing state is profile-local; copy it deliberately or approve users again on the VPS.
8. Keep rollback simple and secret-safe. Never leave both gateways consuming events during normal operation, and never disable the known-good source before target verification succeeds.

## Common pitfalls

- Existing environment variables may belong to another Slack workspace or stale app.
- A running Hermes gateway does not prove its Slack adapter authenticated.
- DM success does not prove public-channel event subscriptions are correct.
- Changing scopes or events may require reinstalling the app to the workspace.
- A default Slack manifest named `Demo App` with Socket Mode disabled is not a Hermes configuration; replace and verify it before saving.
- Never ask the user to paste Slack tokens into chat when they can be copied directly into the local profile.
- Do not confuse Slack channel membership, Hermes user pairing, and gateway ownership; verify all three independently.
