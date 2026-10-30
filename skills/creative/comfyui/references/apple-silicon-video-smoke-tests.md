# Apple Silicon video smoke tests

Use this when validating a large video workflow locally on a memory-constrained Mac.

## Minimal representative test

1. Copy the workflow; never weaken the production file in place.
2. Keep one output node and remove the other `SaveVideo`/final-conform outputs. ComfyUI executes only ancestors of requested output nodes, even if conversion still includes disconnected nodes in the prompt preview.
3. Reduce the retained branch before submission:
   - 0.1–0.25 MP
   - minimum valid frame-grid duration
   - 4–8 steps
   - enable the workflow's compatible turbo/lightning LoRA when present
4. Run `--print-prompt` first, then submit with `--wait --json`.
5. Verify with `ffprobe` and `comfy preview`; inspect the contact sheet before calling the test successful.

## Silent MPS visual corruption

A job can report `completed`, encode a valid MP4, and still be visually unusable (solarized colors, geometric blobs, progressive melting). Treat execution success and visual success as separate gates.

Diagnostic sequence:

1. `ffprobe` the output, then run `comfy preview` and inspect the contact sheet.
2. If it looks corrupt, fetch a fresh official template and run a tiny control: simple stock prompt, 0.1–0.25 MP, minimum useful frame count, 4–8 steps.
3. If both the production run and control corrupt, SHA-256 the UNet, VAE, and text encoder and compare with their authoritative repository LFS hashes. This separates damaged files from backend computation defects.
4. Search current ComfyUI/PyTorch issues for the exact Apple silicon generation and temporal shape. Wan-family MPS corruption has occurred as a silent, deterministic, temporal-length-dependent kernel defect; re-check current upstream status rather than assuming it remains universal.
5. Do not burn another full render on prompt/scheduler/precision tweaks after the control reproduces the same corruption. Offer CUDA/cloud, or CPU only when the user accepts the runtime.

A short or low-resolution control proves the failure class only when it reproduces the same artifact. A clean control does not prove a longer temporal shape is safe; increase frames before resolution because temporal attention can be the boundary.

## MPS int8 fallback

Symptom:

`aten::_int_mm is not currently implemented for the MPS device`

Restart ComfyUI with the fallback set in the server process environment:

```bash
comfy stop
PYTORCH_ENABLE_MPS_FALLBACK=1 comfy launch --background -- --novram --cache-none --mmap-torch-files --reserve-vram 4
```

Verify the environment reached the child process before resubmitting. The fallback is slower and can duplicate CPU/MPS allocations. If the retry ends in MPS OOM while dequantizing int8/convrot weights, do not disable the MPS high-watermark limit on a shared machine: that can destabilize macOS and does not make insufficient unified memory disappear.

## MPS silent video corruption

A workflow can complete with a valid MP4 while its frames are solarized, abstract, or progressively melted. This is a known Apple Silicon MPS failure mode for Wan 2.1/2.2 on affected silicon generations; it is not necessarily a bad prompt or corrupt model file.

1. Always run `comfy preview` and inspect the contact sheet after a smoke test.
2. Reproduce with the untouched official template and a simple prompt at low resolution/steps.
3. Verify model SHA-256 against the publisher before redownloading.
4. If both the target and untouched smoke test are corrupt, do not spend another full Wan render retrying precision, VAE tiling, CFG, or split attention; those are documented non-fixes for this defect.
5. Use a different architecture locally (a small LTXV workflow is a practical fallback), CPU execution if time is irrelevant, or CUDA/Cloud with user approval.

## Compatibility fallback

If the target architecture cannot fit unified memory, use a smaller *compatible* installed model/template to validate the local ComfyUI pipeline separately. Example class: Wan 2.1 1.3B instead of a much larger audiovisual model. This proves local execution, encoding, and output delivery—not compatibility of the original workflow. State that distinction explicitly.

Prefer a fetched official template that already selects the installed model, VAE, and text encoder. Slot-edit resolution, frames, steps, prompt, and output prefix; avoid hand-building the graph.
