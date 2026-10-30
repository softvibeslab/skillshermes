---
name: local-model-agent-profiles
description: Provision and verify isolated coding-agent profiles backed by local OpenAI-compatible inference such as Ollama. Use when creating a project-specific local agent, choosing a tool-capable model, constraining tools, binding a workspace, or diagnosing local function-calling/context issues.
version: 1.0.0
created_by: agent
metadata:
  hermes:
    tags: [local-models, ollama, coding-agent, profiles, tool-calling]
---

# Local Model Agent Profiles

Build project-scoped local coding agents that can actually use tools. A model producing plausible prose is not enough; verify structured function calls through the complete agent path.

## Workflow

1. **Inspect before choosing**
   - Check host memory and available local models.
   - Prefer an already-installed model when it meets context and function-calling requirements.
   - Do not assume a model labeled “coder” is the best agent model; coding quality and native tool-call compatibility are separate capabilities.

2. **Create an isolated profile**
   - Create a fresh profile rather than cloning secrets, messaging tokens, sessions, or unrelated memory.
   - Give it a class-level role description covering the project stack and safety boundaries.
   - Keep gateway integrations stopped unless the user explicitly requests a bot/channel.

3. **Configure local inference correctly**
   - For Ollama local, use its OpenAI-compatible endpoint, normally `http://127.0.0.1:11434/v1`.
   - In Hermes, use the first-class custom endpoint provider rather than inventing a provider alias.
   - Set both the declared context and the Ollama runtime context when Hermes requires a larger window:

```yaml
model:
  default: <model>
  provider: custom
  base_url: http://127.0.0.1:11434/v1
  api_key: ollama
  context_length: 65536
  ollama_num_ctx: 65536
```

   - Current Hermes releases may reject models declared below 64K before the first request. If startup reports a minimum-context error, raise **both** values to at least 65,536, stop the loaded Ollama model, and retry.
   - Treat 65,536 as a starting point, not a universal value. Confirm that host memory and the model/runtime support it; do not request the model's advertised maximum merely because it exists.

4. **Bind the project workspace**
   - Set `terminal.cwd` to the project directory.
   - Add a short project `AGENTS.md` with scope, constraints, secrets boundaries, and verification commands.
   - Ensure the profile wrapper itself enters the project directory before launching. This keeps file tools and terminal tools aligned even if they initialize working directories differently.

```sh
#!/bin/sh
cd /absolute/path/to/project || exit 1
exec hermes -p <profile> "$@"
```

5. **Reduce the tool surface before the first Hermes test**
   - Keep only tools needed for the project: usually file, terminal, code execution, skills, todo, and clarification.
   - Add browser or vision only when the project needs them and the model chooses tools reliably.
   - Fewer schemas reduce prompt load and tool-selection mistakes for smaller local models.
   - Treat “prints a shell command instead of calling the requested tool” as a tool-surface warning, not proof that native tool calling is unsupported. Disable unrelated toolsets, start a fresh session, and repeat the same forced read-only call. In one verified case, a model ignored `read_file` with 30 exposed tools but emitted and executed it correctly with 12.

6. **Add safety without ceremony**
   - Enable checkpoints.
   - Use smart/manual approvals rather than unrestricted execution.
   - Enable secret redaction when source files may contain credentials.
   - Put “no deploy/publish/delete without explicit approval” in the profile role when appropriate.

7. **Verify in layers**
   - Confirm the local server and model respond.
   - Probe the OpenAI-compatible endpoint with one tiny function schema and inspect whether the response contains structured `tool_calls`, not JSON-looking text in `content`.
   - Run one read-only Hermes request that must call a specific file tool. Use a temporary file containing an unpredictable sentinel so a plausible answer cannot pass accidentally.
   - Run that request once with verbose output and require the trace to show the requested tool, arguments, successful result, and a second model call after the tool result.
   - Verify the trace shows the tool completed and the workspace path is correct.
   - Check tool execution and final prose separately: an exit code of 0 proves execution, but the model may still misquote, duplicate, or relabel an exact tool result. Compare sentinel output literally when exactness matters.
   - Do not infer the main agent context solely from `ollama ps` after the session: an auxiliary title/compression request may reload the same model with a smaller context. Prefer the verbose main-request log and the actual agent trace.
   - Only then trust the profile to edit code.

## IDE integration

When the user also wants the local models in Cursor, keep the IDE adapter separate from the Hermes profile. Use Continue with role-specific models, a smaller IDE context, and independent verification of extension installation, configuration loading, model responses, and UI selection.

See `references/ollama-continue-cursor.md` for the known-good Continue configuration, activation sequence, memory guidance, and verification checklist.

## Tool-call probe

See `references/ollama-hermes-tool-call-probe.md` for a deterministic endpoint probe, interpretation, and a known-good profile verification sequence.

## Pitfalls

- **Model-name bias:** “coder” variants may write stronger code yet integrate worse with an agent runtime. Select on both code quality and structured tool calling.
- **Declared context only:** overriding `context_length` without setting the runtime context can leave Ollama loaded at a smaller window.
- **Config-only workspace:** `terminal.cwd` may not guarantee the initial directory used by every file-tool environment; verify the trace and use a `cd` wrapper when needed.
- **Testing only chat:** a successful text response does not prove tool use. Require one real, read-only tool call.
- **Equating exit 0 with a correct explanation:** validate the trace/result and the model’s description independently; local models can execute correctly while overstating or misnaming the operation.
- **Oversized tool catalog:** local models can waste turns or choose adjacent tools. Start minimal and enable capabilities when a task needs them.
- **Downloading first:** probe installed candidates before pulling another multi-gigabyte model; remove trial downloads that are no longer needed.

## Completion check

A local coding profile is ready only when:

- profile and model resolve correctly;
- local inference is reachable;
- runtime context meets the agent minimum;
- a structured tool call is emitted and executed;
- file tools start in the intended project;
- project constraints are loaded;
- no unrelated credentials or gateways were copied.
