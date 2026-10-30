# Recovering a Slack permalink from the local desktop cache

Use this only when the user supplied a Slack permalink, the official Slack API cannot read the conversation (commonly an old/private DM), and the authenticated Slack desktop app is on the same Mac. Prefer API or visible UI first.

## Escalation order

1. Parse the permalink into workspace, channel ID, and message timestamp.
2. Try `conversations.history` / thread APIs with the configured token.
3. Open the exact deep link in Slack desktop:

```text
slack://channel?team=<TEAM_ID>&id=<CHANNEL_ID>&message=<TS>
```

4. Verify navigation rather than trusting `open` alone. Slack's `webapp-console.log` records `JUMP-TO-MESSAGE` and the target channel/timestamp.
5. If UI extraction is unavailable, inspect the local Chromium LevelDB only as a last-resort read path.

## LevelDB recovery shape

Slack may cache a pasted permalink under a key ending in `::draftUnfurls`. The value observed on macOS had:

- a one-byte wrapper;
- UTF-16LE JSON;
- nested entries keyed by draft destination and permalink;
- the readable Slack preview under `data.fallback`.

The `.ldb` file is an SSTable, not a flat text file. Parse its footer, index block, and referenced data blocks; decompress blocks whose trailer type is Snappy; then iterate prefix-compressed entries. Select only the key ending in `::draftUnfurls`, decode its value, parse JSON, and print only `data.fallback`.

## Security boundary

The same LevelDB can contain `localConfig_v2` and authenticated Slack session material. **Never print full blocks, neighboring values, tokens, cookies, or raw local configuration.** Filter by the exact key before rendering anything, and return only the requested message preview. Do not copy the cache or credentials to another host.

## Limits

- `draftUnfurls` is opportunistic and may disappear; it is not a durable Slack API.
- A preview may be truncated. Label it as preview text, not full message history.
- This does not grant permission to inspect unrelated DMs or cached workspace data.
- Do not persist recovered private message content in a skill, memory, or repository.
