---
name: local-ai-video-production
description: "Build local-first AI video generation pipelines: course/script to short videos, local LLM/TTS/subtitles, and repo evaluation for video stacks."
version: 1.0.0
author: Hermes Agent
license: MIT
metadata:
  hermes:
    tags: [video, local-ai, tts, subtitles, ollama, course-generation]
    related_skills: [youtube-content, github-repo-management, ocr-and-documents]
---

# Local AI Video Production

Use when the user wants to generate videos with local/self-hosted models, compare AI video repos, turn course material into videos, or build a local-first alternative to HeyGen/ElevenLabs-style workflows.

## Lazy default architecture

Start with the smallest pipeline that can make one good video:

```text
course/script agent
  -> lesson JSON / script
  -> video engine CLI/API
  -> MP4 + SRT + audio + metadata

local pieces:
  LLM: Ollama or OpenAI-compatible local server
  TTS: Chatterbox/local TTS or Edge TTS as bootstrap
  Subtitles: faster-whisper local
  Assembly: MoviePy/ffmpeg-based engine
  Visuals: local clips first, stock APIs second, generative video later
```

Do not build a new UI until the CLI produces repeatable videos.

## Repo evaluation checklist

For each candidate repo, capture:

1. License: MIT/BSD preferred; AGPL means reference-only unless obligations are acceptable.
2. Runtime: Python/Node/Docker versions and model/API dependencies.
3. Local-first support: Ollama, local TTS, local whisper, local media.
4. Pipeline coverage: script, scenes, voice, subtitles, B-roll, render, publishing.
5. Operational weight: number of services/models needed before first successful video.
6. Product fit: base engine vs reference pattern vs docs/market research only.

## Source-video analysis before generative treatment

When transforming an existing video, analyze before prompting: inspect media metadata, build a sparse contact sheet, transcribe audio locally, and extract the single strongest transformation. Start with one excellent generative shot; batch clips only after the visual language works. Verify the rendered file before reporting success.

See `references/local-ai-video-production-local-ai-video-production-source-video-to-veo.md` for the ffmpeg/Whisper analysis recipe, Gemini/Veo model discovery probe, paid-generation boundary, prompt structure, and verification checklist.

## Course-to-video flow

Minimum contract:

```json
{
  "title": "Course title",
  "audience": "target learner",
  "modules": [
    {
      "title": "Module",
      "lessons": [
        {
          "title": "Lesson",
          "objective": "What the viewer learns",
          "script": "Narration script",
          "visual_keywords": ["keyword one", "keyword two"],
          "video_style": "vertical short, practical, energetic"
        }
      ]
    }
  ]
}
```

Generate one lesson video first. Batch course rendering comes after the single-lesson path is stable.

## MoneyPrinterTurbo pattern

MoneyPrinterTurbo is a strong default base when local-first short-video generation is needed because it already has:

- CLI/API/WebUI
- topic/script/keywords/audio/subtitle/material/render pipeline
- Ollama provider support
- faster-whisper subtitle support
- local material support
- Chatterbox TTS configuration hooks
- MIT license

Primary pipeline:

```text
generate_script -> generate_terms -> generate_audio -> generate_subtitle -> get_video_materials -> generate_final_videos
```

Useful local config shape:

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

Use local materials where possible:

```bash
uv run python cli.py \
  --video-subject "Topic" \
  --video-source local \
  --video-materials "clips/intro.mp4,clips/demo.mp4"
```

## What to avoid early

- Installing every researched repo. Clone and inspect first.
- Using cloud-only HeyGen wrappers when the user asked for local models.
- Copying AGPL code into a product without explicit acceptance.
- Starting with agentic video systems that require several external image/video APIs if the immediate goal is local-first.
- Building orchestration/UI before one CLI video works.

## Cloud generation with a deterministic fallback

When a source video must become a cinematic AI-generated short, analyze it before prompting: probe metadata, build a contact sheet, transcribe narration, and reduce it to one transformation arc. Discover the live video model instead of hardcoding a version. If generation is blocked by quota or billing, preserve the ready-to-run prompt and ship a clearly labeled concept teaser from the source footage; never present the fallback as model-generated.

Probe FFmpeg filters before relying on `drawtext` or `subtitles`. Minimal builds may omit them; render typography into frames with Pillow and animate those frames with FFmpeg instead.

## References

- `references/local-ai-video-production-moneyprinterturbo-local-course-video.md` — session-specific repo findings and recommended application map.
- `references/local-ai-video-production-veo-api-and-fallback-teaser.md` — source-video analysis, Veo long-running API flow, quota boundary, prompt structure, and verified FFmpeg/Pillow fallback.
