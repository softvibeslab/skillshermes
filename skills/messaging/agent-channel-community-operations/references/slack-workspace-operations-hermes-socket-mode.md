# Hermes + Slack Socket Mode checklist

Use this reference when a Hermes gateway must receive Slack mentions without exposing a public webhook.

## Setup

1. Generate or inspect the Hermes Slack app manifest.
2. In Slack app settings, enable Socket Mode.
3. Create an app-level token with `connections:write`.
4. Install the app to the intended workspace and capture the bot OAuth token.
5. Store both secrets in the Hermes profile/environment; do not paste them into chat.
6. Configure the Slack user allowlist for the people permitted to invoke Hermes.
7. Start or restart the intended Hermes gateway/profile.
8. Invite the bot to the target channel.

## Scope notes

Receiving mentions and posting replies is separate from workspace administration. If Hermes must create public channels through the API, add `channels:manage`, reinstall/reauthorize the app, and then use `conversations.create`. Socket Mode itself does not provide this permission.

## Verification

- Gateway log reports a successful Slack/Socket Mode connection.
- The bot appears as a member of the target channel.
- `@bot hola` produces exactly one response.
- The response comes from the intended Hermes profile.

## Common diagnoses

- **Connected but no channel response:** bot is not a channel member, event subscription is missing, or the sender is not allowlisted.
- **Can reply but cannot create channels:** installed token lacks channel-management scope; update scopes and reauthorize.
- **Duplicate replies:** the same Slack credentials are active in multiple gateways/profiles.
- **GUI automation drifts:** another app stole focus or the dialog changed; recapture state, or switch to the Web API after adding the required scope.
