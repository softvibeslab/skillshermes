# AgenticOS Skool launch reference

Concrete example for `hermes-project-ops-launch`.

## Project shape

- Workspace: `/Users/USERNAME/Documents/SoftvibesLab/AgenticOS-Skool`
- Profile/alias/board slug: `agenticos-skool`
- Purpose: Skool community teaching practical agentic workflows under Softvibes.
- Token state: Telegram bot token pending from BotFather.

## Files created

- `PLAN.md` — full launch strategy.
- `DASHBOARD.md` — sprint/KPI tracker.
- `PROMPTS.md` — prompts for course, content, community, agents.
- `TOOLS_SKILLS_MCPS.md` — recommended skills, tools, MCPs.
- `TELEGRAM_SETUP.md` — token and gateway instructions.
- `scripts/set_telegram_token.py` — one-command token setter.
- `scripts/start_kanban_sprint.sh` — sprint activation handoff.

## Business framing

- Brand/project: AgenticOS by Softvibes.
- Method: SER → HACER → TENER.
- Value ladder: free Avatar IA course → low-ticket community → bootcamp → high ticket → DFY.
- Core promise: practical building of avatars, agents, systems, and monetizable workflows.

## Operating pattern

1. Build all non-credentialed assets first.
2. Create profile + SOUL.md for persistent project identity.
3. Create Kanban board with epics/subtasks.
4. Keep tasks blocked/manual until token and launch approval exist.
5. Provide exact final commands:

```bash
python3 scripts/set_telegram_token.py '<BOTFATHER_TOKEN>'
agenticos-skool gateway start
agenticos-skool gateway status
./scripts/start_kanban_sprint.sh
```

## Pitfall captured

Telegram setup is two-part: BotFather token starts the bot, but secure operation may also require the user's Telegram ID in the allowlist. Mention this in handoff instead of implying token alone is always enough.