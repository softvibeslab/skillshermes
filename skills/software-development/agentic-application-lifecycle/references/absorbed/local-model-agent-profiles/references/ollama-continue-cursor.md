# Ollama models in Cursor through Continue

Use this when a user wants local coding models inside Cursor. Keep Hermes and IDE configuration separate: Hermes uses its isolated profile; Cursor uses Continue's user config.

## Recommended split

- Larger tool-capable coding model: `chat`, `edit`, `apply`.
- Smaller coder model: `autocomplete`.
- Avoid keeping two large models resident on memory-constrained machines. Ollama normally evicts the previous model when necessary; verify with `ollama ps`.

## Continue configuration

File: `~/.continue/config.yaml`

```yaml
name: Local Coding
version: 1.0.0
schema: v1

models:
  - name: Local Coding Agent
    provider: ollama
    model: <tool-capable-model>
    apiBase: http://127.0.0.1:11434
    roles: [chat, edit, apply]
    capabilities: [tool_use]
    defaultCompletionOptions:
      contextLength: 32768
      maxTokens: 4096
      temperature: 0.1
      keepAlive: 1800

  - name: Local Autocomplete
    provider: ollama
    model: <fast-coder-model>
    apiBase: http://127.0.0.1:11434
    roles: [autocomplete]
    defaultCompletionOptions:
      contextLength: 8192
      temperature: 0.1
    autocompleteOptions:
      debounceDelay: 300
      maxPromptTokens: 2048
      onlyMyCode: true

rules:
  - Inspect relevant code before editing and reuse existing project patterns.
  - Prefer the smallest root-cause fix and run the smallest relevant check.
  - Never deploy, publish, delete project data, or expose secrets without explicit approval.
```

Continue's Ollama provider uses the native base URL **without `/v1`**. Hermes' custom OpenAI-compatible provider normally uses `http://127.0.0.1:11434/v1`.

## Activation and verification

1. Install Continue through Cursor's bundled CLI:
   ```sh
   /Applications/Cursor.app/Contents/Resources/app/bin/cursor --install-extension Continue.continue
   ```
2. Validate that the extension is installed:
   ```sh
   /Applications/Cursor.app/Contents/Resources/app/bin/cursor --list-extensions --show-versions
   ```
3. Save `~/.continue/config.yaml` and validate its YAML syntax.
4. Reload the IDE. If background keyboard automation cannot reach `Developer: Reload Window`, gracefully restart Cursor with AppleScript and reopen it; this reliably initializes the extension host.
5. Confirm Continue appears in Cursor's status bar or side panel.
6. Probe each model directly with a tiny exact-response request before blaming the IDE:
   ```sh
   ollama run <model> 'Respond exactly: MODEL_OK'
   ```
7. Check `ollama ps` after switching models to confirm actual residency, processor, and context.
8. In Continue, send one read-only project-inspection prompt, then test inline autocomplete in a code file.

## Memory guidance

Use a smaller IDE context than a standalone Hermes profile when Cursor and autocomplete are running concurrently. A 32K chat context plus an 8K autocomplete context is a practical starting point on unified-memory Macs; tune from measured memory pressure, not advertised maximum context.

## Pitfalls

- Cursor's native agent/model UI and Continue are separate. A local model configured in Continue will not necessarily appear in Cursor's built-in model picker.
- Restarting only the model server does not reload an edited Continue config; reload the Cursor extension host/window.
- A model listed by `ollama list` is installed, not necessarily loaded. Use a direct probe and `ollama ps`.
- Avoid claiming visual model selection was verified unless the Continue panel actually displayed it. Extension installation, config validity, model response, and UI selection are separate checks.
