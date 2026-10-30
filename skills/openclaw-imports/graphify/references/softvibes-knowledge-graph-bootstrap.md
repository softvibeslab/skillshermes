# Softvibes knowledge graph bootstrap notes

Session pattern: user asked to unify multiple agents/projects into one shared knowledge graph. Build a `raw/` corpus first, then run Graphify.

## Folder pattern

Example used successfully:

```text
/Users/USERNAME/Documents/SoftvibesKnowledgeGraph/
  raw/
    00_directriz/
    01_contexto_humano/
    02_proyectos/
    03_fuentes_rovi/
    04_leadvibes/
    05_agentes/
    _inbox_mariovibes/
  graphify-out/
  MANIFEST.json
```

## Seed docs to create before extraction

- `00_directriz/directriz_madre_softvibes.md`: the cross-project thesis and framing.
- `01_contexto_humano/principios_antropologia_digital.md`: human/anthropology/digital sociology principles.
- `02_proyectos/mapa_proyectos_softvibes.md`: project map and relations.
- `05_agentes/roles_agentes_softvibes.md`: orchestrator and specialist-agent roles.
- `_inbox_mariovibes/INSTRUCCIONES_PARA_MARIOVIBES.md`: paste/export instructions for the other bot’s context.

## Current CLI reality checked in session

Do not call `graphify raw`; current CLI errors with `unknown command 'raw'`.
Use:

```bash
cd /path/to/project
# Full headless extraction
OLLAMA_API_KEY=local graphify extract raw --backend ollama --model llama3.2:latest --out . --max-concurrency 1

# Recluster existing graph.json
 graphify cluster-only .
```

`graphify extract` requires an LLM provider key unless using `--backend ollama` with local Ollama.

If graphify was installed with uv tool and `--backend ollama` complains that `openai` is missing, reinstall the tool with the extra dependency:

```bash
uv tool install graphifyy --with openai --force
```

## Bootstrap fallback

If semantic extraction times out or local Ollama returns invalid JSON, make a small honest seed `graphify-out/graph.json` manually from explicit project/directriz facts, then run:

```bash
graphify cluster-only .
```

This produces `GRAPH_REPORT.md`, `graph.html`, and a navigable initial graph. Label it as v0.1/bootstrap and replace or enrich it later when better LLM extraction is available.
