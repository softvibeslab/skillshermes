# MoneyPrinterTurbo community launch reference

Use this reference when launching a Softvibes/AgenticOS community around an open-source media automation repo such as MoneyPrinterTurbo.

## Durable pattern

Frame the community as a content production system, not as a "money printer" promise.

Core positioning:

> Fábricas de contenido con agentes: tú eliges el mensaje, el sistema hace la maquila.

Teach the shift from manual editing to pipeline operation:

idea → script → search terms → stock/local B-roll → TTS/voice → subtitles → composition/render → human QA → publication

## Repo assessment summary

Original repo: `harry0703/MoneyPrinterTurbo`

Best initial base because it has:
- Streamlit WebUI and FastAPI API.
- Docker release compose file with prebuilt image.
- `uv.lock` and Python 3.11 requirement for reproducible setup.
- Built-in Pexels/Pixabay/Coverr/local material sources.
- Edge TTS default, Whisper subtitle fallback, many LLM providers including OpenAI-compatible, Gemini, DeepSeek, Ollama, LiteLLM.

Extended fork: `Asad-Ismail/MoneyPrinterTurbo-Extended`

Use as advanced lab only after the original works. It adds:
- Word-by-word subtitle highlighting.
- Semantic video/text matching.
- Chatterbox local TTS and voice cloning.

## Implementation order

1. Clone original and extended repos under the project root.
2. Create a separate community/docs workspace, e.g. `MoneyPrinterTurbo-Community`.
3. Write two files first:
   - `WIKI_COMUNIDAD.md`: audience, promise, modules, rituals, legal/ethical checklist, prompts, value ladder.
   - `IMPLEMENTACION.md`: setup path, config keys, API snippets, demo topic, roadmap, non-goals.
4. Pick original repo as MVP base; keep extended fork as advanced module.
5. Do not build a new backend before validating WebUI/API output quality.

## Minimal setup docs to include

Docker release:

```bash
cd /path/to/MoneyPrinterTurbo
cp config.example.toml config.toml
# edit config.toml: stock media key + LLM provider
docker compose -f docker-compose.release.yml up
```

uv local:

```bash
cd /path/to/MoneyPrinterTurbo
cp config.example.toml config.toml
uv python install 3.11
uv sync --frozen
uv run streamlit run ./webui/Main.py --browser.gatherUsageStats=False --server.showEmailPrompt=False
```

API:

```bash
uv run python main.py
# docs at http://127.0.0.1:8080/docs
```

CLI:

```bash
uv run python cli.py --video-subject "Cómo los agentes de IA te ayudan a estar en flow"
```

## Community content structure

Course/free lead magnet:
- What an AI content factory is.
- Install and configure.
- First video.
- Quality and prompt tuning.
- Repeatable weekly pipeline.
- Monetization package.

Value ladder:
- Free first-video course.
- Low-ticket community with prompts/reviews.
- DWY bootcamp to build the content factory.
- High-ticket system install for businesses/agencies.
- DFY monthly content operation.

Rituals:
- Monday prompt/topic drop.
- Wednesday technical clinic.
- Friday showcase.
- Sunday retro.

## Non-goals / safety

Do not promise automatic income.
Do not auto-publish until the manual QA flow works.
Do not clone voices without explicit permission.
Do not expose the API publicly without auth/rate limits.
Do not skip stock footage/music license review.

## QA gates

Every generated video needs human review for:
- Hook clarity.
- Visual relevance.
- Voice/subtitle quality.
- Claim accuracy.
- Stock/music/voice license safety.
- CTA and platform fit.
