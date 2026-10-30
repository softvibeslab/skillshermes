# Behance Search Query Playbook

Canonical route:

`https://www.behance.net/search/projects/{URL_ENCODED_QUERY}`

Encode the complete query with a standard URL encoder. Spaces must become `%20`; preserve no raw spaces.

## Query formula

`[product/domain] + [platform] + [critical flow] + [UI UX or design system]`

Always generate:

1. Direct product query.
2. Hardest-flow query.
3. Adjacent interaction query.

## Agentic OS examples

| Intent | Query | URL |
|---|---|---|
| Mobile agent ecosystem | `AI agent ecosystem mobile app UI UX` | https://www.behance.net/search/projects/AI%20agent%20ecosystem%20mobile%20app%20UI%20UX |
| Orchestration | `multi agent orchestration workflow dashboard UX` | https://www.behance.net/search/projects/multi%20agent%20orchestration%20workflow%20dashboard%20UX |
| Human control | `AI task approval activity history SaaS design` | https://www.behance.net/search/projects/AI%20task%20approval%20activity%20history%20SaaS%20design |
| Chat and voice | `AI assistant chat voice mobile app UI UX` | https://www.behance.net/search/projects/AI%20assistant%20chat%20voice%20mobile%20app%20UI%20UX |
| Agent marketplace | `AI agent marketplace mobile app product design` | https://www.behance.net/search/projects/AI%20agent%20marketplace%20mobile%20app%20product%20design |
| CRM agents | `AI CRM agent dashboard workflow UX` | https://www.behance.net/search/projects/AI%20CRM%20agent%20dashboard%20workflow%20UX |

## Query quality rules

- Prefer concrete jobs (`approve task`, `build workflow`, `inspect history`) over broad style words.
- Add platform (`mobile app`, `SaaS dashboard`, `website`) when it affects interaction.
- Avoid searches composed only of aesthetics such as `futuristic AI purple`.
- Use one adjacent domain when direct results are repetitive: operations center, project management, CRM, automation builder, or multiplayer collaboration.
- Do not interpret recommendation order or popularity as quality proof.
