# Project channel context pattern

Use this when a Slack project channel needs a durable Hermes briefing plus a current status post.

## Durable project context

```markdown
# Contexto operativo — <project>

Actualizado: <verified timestamp>

## Identidad
- Canal Slack: `<channel>`
- Workspace/repo local: `<path>`
- Repo remoto: `<url>`
- Hermes profile: `<profile or default>`

## Qué es
<One-paragraph purpose and user outcome.>

## MVP
- <Included capability>
- <Included capability>

Fuera del MVP: <explicit deferrals>.

## Estado verificado
- Etapa: **<stage>**
- <Git/tests/services facts>
- <Clearly labeled unverified claims>

## Riesgos y decisiones pendientes
1. <Risk or unresolved decision>

## Próximas acciones
1. <Concrete action>
2. <Concrete action>
3. <Concrete action>

## Fuentes de verdad
- `<paths>`
- Git, tests and live services override this snapshot.

## Regla para Hermes
Recheck Git, tests and live services before each status. Separate verified facts from inference. Return purpose, stage, progress, blockers, next action and suggested owner.
```

## Slack status post

Keep the channel post shorter than the durable file:

```text
✅ Proyecto identificado: <project>
📍 Canal: <channel>
📂 Repo: <path>
🧠 Contexto: <context-file>

Propósito: <one sentence>
Estatus verificado: <stage + strongest evidence>
Bloqueadores: <1–3 bullets>
Próximos pasos: <three numbered actions>
```

## Verification language

Use exact claims:

- **Posted:** messaging API/tool returned success with channel/message ID.
- **Membership confirmed:** channel membership lookup includes the bot.
- **Response verified:** the intended Hermes profile received the event and replied.

Never collapse these into “Hermes was added and is active” unless all three were checked.
