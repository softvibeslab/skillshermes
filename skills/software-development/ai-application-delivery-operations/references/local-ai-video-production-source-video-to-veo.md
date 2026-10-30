# Source video → Veo production brief

Use this when a user provides a local MP4 and asks for a stronger generative-video treatment.

## Minimum analysis pass

1. Inspect duration, codecs, resolution, frame rate, audio, and size with `ffprobe`.
2. Build one contact sheet before watching frame-by-frame. For medium videos, sample every 20–30 seconds:

```bash
mkdir -p /tmp/video-analysis
ffmpeg -hide_banner -loglevel error -i input.mp4 \
  -vf "fps=1/30,scale=480:-1,tile=4x4:padding=8:margin=8" \
  -frames:v 1 /tmp/video-analysis/contact-sheet.jpg
```

3. Extract mono 16 kHz audio and transcribe locally. Prefer an already-installed Whisper implementation; do not add another package unless necessary:

```bash
ffmpeg -hide_banner -loglevel error -i input.mp4 \
  -vn -ac 1 -ar 16000 -c:a pcm_s16le /tmp/video-analysis/audio.wav
```

4. Combine transcript + contact-sheet evidence into:
   - core transformation/problem,
   - strongest product mechanism,
   - human consequence,
   - one memorable closing line.
5. Design one excellent 8-second Veo shot first. Generate multiple clips only after the first establishes visual language and the user accepts expected spend.

## Veo availability probe

Do not guess model names. If a Gemini key is already configured, list models and select one advertising `predictLongRunning`. Never print the key.

```python
import os, requests
key = os.getenv("GEMINI_API_KEY") or os.getenv("GOOGLE_API_KEY")
r = requests.get(
    "https://generativelanguage.googleapis.com/v1beta/models",
    params={"key": key}, timeout=30,
)
r.raise_for_status()
for model in r.json().get("models", []):
    methods = model.get("supportedGenerationMethods", [])
    if "veo" in model.get("name", "").lower() or "predictLongRunning" in methods:
        print(model["name"], methods)
```

## Prompt shape for the first shot

Write the prompt as a directed shot, not as a feature list:

- subject and emotional state,
- physical transformation,
- camera movement,
- lighting and palette,
- spatial metaphor for the product mechanism,
- sound design and spoken line,
- exclusions: illegible UI text, random logos, warped hands, generic hologram clutter.

Prefer visual causality: show confusion becoming one executable action rather than displaying an architecture diagram literally.

## Safety and verification

- Model discovery is read-only; generation may incur charges.
- If the user's request explicitly authorizes generation, start with one sample. If authorization or billing scope is ambiguous, confirm the number and duration of clips before calling the paid endpoint.
- Poll the long-running operation to completion, download the result, and verify with `ffprobe` plus a contact sheet before reporting success.
- Never claim one Veo version is “better” or “superior” without a measured comparison or authoritative source.
