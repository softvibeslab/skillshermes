# Mixed workspace example: sites, menus, and agent profiles

## Durable discovery pattern

A workspace may combine:
- top-level initiatives;
- collections such as `SoftvibesSites/`, `LandingVibes/analysis/`, and `AgentVibes/`;
- product families nested below collections, such as `MenuVibes/`;
- independent nested Git repositories;
- operational agent profiles stored outside the source workspace.

Build one candidate set from top-level initiatives, Git roots, manifests, and direct children of known collections. Then remove generic support directories unless they independently contain a Git root or manifest.

## Useful workbook split

- `Resumen`: totals, categories, maturity counts, scope and timestamp.
- `Proyectos`: one row per principal initiative or valid subproject.
- `Repositorios Git`: only independent Git roots.
- `Agentes Hermes`: profile/config inventory stored outside project source; do not mix this count into source projects.
- `Hallazgos`: duplicate names, missing root docs, `.env` presence, and test coverage.
- `Nombres duplicados`: review queue only.

## Recency follow-up

A raw modification sort often puts collection roots and support folders first because child activity propagates upward or generated artifacts are newer. For “latest landings, menus, and agents”:

1. filter to the category;
2. remove category roots such as the sites collection itself;
3. remove `assets`, `img`, `output`, `graphify-out`, `tools`, and similar support entries;
4. show concrete leaf products with date, purpose, and status;
5. for agents, present source projects and Hermes profiles as two separate lists.

Call the date “latest filesystem modification.” Use Git commit dates only when requested or when filesystem timestamps are unreliable.

## Spreadsheet writer fallback

Check installed libraries before adding dependencies. A system Python may already have pandas + `xlsxwriter` even if another isolated tool runtime does not. Run the generation in the environment that owns the installed writer; treat interpreter separation as a runtime choice, not a permanent tool limitation.
