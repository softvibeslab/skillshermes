# Ollama ↔ Hermes tool-call verification

Use this when a local model chats successfully but its readiness as an agent is unknown.

## 1. Probe the OpenAI-compatible endpoint

```python
import json
import urllib.request

MODEL = "qwen2.5:14b"
BASE = "http://127.0.0.1:11434/v1"

tool = {
    "type": "function",
    "function": {
        "name": "list_files",
        "description": "List files",
        "parameters": {"type": "object", "properties": {}},
    },
}
payload = {
    "model": MODEL,
    "messages": [{"role": "user", "content": "Call list_files now."}],
    "tools": [tool],
    "stream": False,
}
request = urllib.request.Request(
    f"{BASE}/chat/completions",
    data=json.dumps(payload).encode(),
    headers={"Content-Type": "application/json"},
)
with urllib.request.urlopen(request, timeout=300) as response:
    message = json.load(response)["choices"][0]["message"]

assert message.get("tool_calls"), message
print(json.dumps(message["tool_calls"], indent=2))
```

Pass: `message.tool_calls` is populated with the requested function and valid JSON arguments.

Fail: the function request appears only as JSON/XML-looking text inside `message.content`. This is useful chat output but not a native function call, so Hermes cannot dispatch it as a tool without an adapter/template change. Re-probe another installed model before downloading a new one.

## 2. Configure actual runtime context

Hermes may reject a local model when Ollama loaded a smaller runtime context than the declared value. Set both:

```yaml
model:
  context_length: 65536
  ollama_num_ctx: 65536
```

Stop/reload the model, then retry. Confirm the value is feasible for the host; larger KV caches consume more memory.

## 3. Verify through Hermes

Use an unpredictable sentinel rather than a familiar project file:

```bash
printf 'HERMES_LOCAL_TOOL_CHECK=<random-sentinel>\n' > /tmp/hermes-local-tool-check.txt
<profile-alias> chat -v -q \
  'Debes usar read_file sobre /tmp/hermes-local-tool-check.txt. No uses terminal. Devuelve exactamente el valor después del signo igual.'
rm -f /tmp/hermes-local-tool-check.txt
```

Require all five:

1. The verbose trace lists a manageable tool count; if the model prints a shell command instead of calling `read_file`, disable unrelated toolsets and retry in a fresh session.
2. A structured `read_file` tool call appears with the exact path.
3. `read_file` completes successfully in the intended workspace.
4. Hermes makes a second model call after receiving the tool result.
5. The final answer reproduces the sentinel literally. Record tool execution and final-answer fidelity as separate results; a model can pass the first and fail the second.

If the file-tool cwd is the user's home instead of the project, make the profile alias `cd` into the project before `exec hermes -p ...` and rerun the test.

### Context diagnostics

- Hermes may enforce a 64K minimum before inference. Set both `context_length` and `ollama_num_ctx` to 65,536 when that guard fires, then unload the model and retry.
- A later auxiliary request (for example title generation) can leave `ollama ps` showing a smaller context such as 4K. This does not prove the preceding main agent call used 4K. Use the verbose main-request log (`Ollama num_ctx: will request ...`) plus the successful agent trace as the primary evidence.

## Session observation (re-probe; do not hard-code)

With Ollama 0.32.13 in one macOS setup, `qwen2.5:14b` emitted native tool calls while `qwen2.5-coder:14b` rendered the requested call as content text. This is model/runtime/version-dependent evidence, not a permanent model capability claim. Always run the probe against the installed versions.
