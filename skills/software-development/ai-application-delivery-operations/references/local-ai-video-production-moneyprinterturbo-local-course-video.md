# MoneyPrinterTurbo + local course video findings

Session context: user asked to clone and investigate 14 repos around AI course creation, HeyGen alternatives, and local video generation. Repos were cloned under `/Users/USERNAME/Documents/GitHub/video-ai-course-research`; durable report was written to `ANALISIS.md`.

## Best base found

MoneyPrinterTurbo (`harry0703/MoneyPrinterTurbo`) is the best immediate base for local-first short video generation:

- MIT license
- Python/FastAPI/Streamlit/Docker
- CLI/API/WebUI
- video task pipeline already implemented
- supports Ollama as LLM provider
- supports faster-whisper local subtitles
- supports local video materials
- has Chatterbox TTS self-hosted config hooks
- uses MoviePy 2.x; no ImageMagick needed for current subtitle rendering

Pipeline found in `app/services/task.py`:

```text
generate_script
generate_terms
generate_audio
generate_subtitle
get_video_materials
generate_final_videos
optional cross-post
```

Useful `VideoParams` fields:

- `video_subject`
- `video_script`
- `video_terms`
- `video_aspect`
- `video_concat_mode`
- `video_clip_duration`
- `match_materials_to_script`
- `video_count`
- `video_source`: `pexels`, `pixabay`, `local`
- `video_materials`
- `custom_audio_file`
- `voice_name`
- subtitle font/styling fields
- `custom_system_prompt`

## Recommended local config

```toml
llm_provider = "ollama"
ollama_base_url = "http://127.0.0.1:11434/v1"
ollama_model_name = "llama3.1:8b"
subtitle_provider = "whisper"

[chatterbox]
base_url = "http://127.0.0.1:4123/v1"
api_key = ""
model_id = "chatterbox"
voices = ["default-Female"]
```

Use `voice_name` like:

```text
chatterbox:default-Female
```

## Start commands

```bash
cd /Users/USERNAME/Documents/GitHub/video-ai-course-research/MoneyPrinterTurbo
cp config.example.toml config.toml
uv sync
uv run streamlit run ./webui/Main.py --browser.gatherUsageStats=False --server.showEmailPrompt=False
uv run python main.py
uv run python cli.py --video-subject "Cómo los agentes de IA ayudan a crear cursos"
```

Local materials path:

```bash
uv run python cli.py \
  --video-subject "Cómo usar agentes de IA para vender más" \
  --video-source local \
  --video-materials "clips/intro.mp4,clips/demo.mp4,clips/outro.mp4"
```

## Related repo roles

- `Automated-Course-Content-Generator` — simple course outline/modules/quizzes/PDF/PPT; useful prompt/flow reference.
- `learning-journey`, `ai-course-generator`, `Full-Stack-AI-Course-Creator-Learning-Journey` — Next.js course UX/reference flows; don't copy whole apps first.
- `Scrapling` — robust scraping/research for sources, trends, course inputs.
- `ElevenLabs-Clone` — heavy but useful audio reference: StyleTTS2, Seed-VC, Make-An-Audio, FastAPI/Next.js/Docker.
- `ViMax` — strong agentic storyboard/Idea2Video/Script2Video concepts, but not local-first; depends on configured LLM/image/video APIs.
- `MoneyPrinterV2` — useful reference but AGPL-3.0; avoid copying into product unless obligations are accepted.
- `heygen-app`/`heygen`/`awesome-heygen-ai-alternatives` — cloud/API or market research; not local model base.

## Implementation order

1. Run MoneyPrinterTurbo with Edge TTS + Ollama.
2. Generate one video from CLI using local clips.
3. Switch subtitle provider to `whisper`.
4. Add Chatterbox TTS local.
5. Build a wrapper that reads one lesson JSON and calls MoneyPrinterTurbo.
6. Only then batch-render course modules.
7. Add ViMax-like storyboarding later if scene quality/continuity is insufficient.
