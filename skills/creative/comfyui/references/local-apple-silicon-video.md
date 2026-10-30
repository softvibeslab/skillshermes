# Apple Silicon: local video workflow preflight

Use this when the user explicitly wants local execution on an Apple Silicon Mac, especially for long or multi-scene video workflows.

## Sequence

1. Honor the routing choice. Keep every inspection and run pinned to local with `--where local`; do not silently fall back to Cloud.
2. Launch conservatively for memory-heavy graphs:

```bash
comfy launch --background -- --novram --cache-none --mmap-torch-files --reserve-vram 4
```

`--reserve-vram` is a calibration knob, not a universal constant. Lower it only after measuring memory pressure; raise it if macOS becomes unstable.

3. Verify the server, then verify the actual child process received the flags:

```bash
curl -fsS http://127.0.0.1:8188/system_stats >/dev/null
PARENT=$(pgrep -f 'comfy.*launch' | head -1)
pgrep -P "$PARENT" | xargs -I{} ps -p {} -o command=
```

If the launcher process layout differs, inspect the ComfyUI `main.py` process directly. The important check is the command line of the Python server, not the wrapper's reported configuration.

4. Validate conversion without submitting the expensive job:

```bash
comfy run --where local --workflow workflow.json --print-prompt >/dev/null
```

This catches format/translation problems before generation. It does not prove every model will fit in memory.

5. Run one minimal scene or a low-cost smoke workflow first. Measure completion time and memory behavior before submitting the full-duration graph.

## Pitfalls

- Do not treat a successful health endpoint as proof that launch flags reached the Python child; check the process command line.
- Do not submit a long, expensive video workflow merely because conversion succeeds. A one-scene smoke test is the smallest useful execution check.
- Keep local routing explicit when the user chose local. Cloud may be faster, but changing the execution target is a user decision.
- `--novram` and `--cache-none` trade speed for survivability. Remove them only after a successful representative test shows adequate memory headroom.
