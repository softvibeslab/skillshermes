# Vendor web-surface evidence hierarchy

Use when several URLs from one vendor are presented as equivalent “repos,” “docs,” or sources. Classify each surface before extracting facts.

| Surface | Best use | Authority rule |
|---|---|---|
| Versioned manual/API reference | Behavior, compatibility, configuration | Match product/version |
| Official code/schema/release | Executable behavior | Pin commit/tag/release |
| Developer portal | Discovery and navigation | Descend to linked docs/code |
| Official academy/training | Reproducible learning | Recheck version-sensitive steps |
| Community forum | Emerging failures and workarounds | Signal only; verify against primary sources |
| Marketing/blog | Concepts and announcements | Independently verify claims/dates |

Workflow:
1. Correct a false source label gently; do not preserve it in the artifact.
2. Record role, authority, version/date, and bias for every surface.
3. Extract only claims that surface can support. A portal proves a route exists, not runtime behavior.
4. For dynamic sites, fall back to public JSON/API or rendered DOM; extraction success adds no authority.
5. Persist one fiche per surface and a synthesis describing how each source should be used.
6. For forum reports, capture exact error, versions, URL, and date; validate any workaround against docs, releases, or code.

Pitfalls:
- Do not ingest a vendor ecosystem indiscriminately.
- Community recency never outranks versioned documentation.
- Training coverage is not proof of production readiness.
- Product grouping on a portal is not an architectural requirement to combine every product.
- A transient fetch failure calls for another extraction strategy, not a durable claim that the site is unusable.