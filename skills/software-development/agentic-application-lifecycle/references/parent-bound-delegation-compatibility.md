# Parent-bound native delegation compatibility

## Trigger and scope

Use when a plugin's newer lifecycle API is unavailable on an installed agent runtime and the user requires compatibility without a host upgrade. Respect exact file allowlists, configuration exclusions, and operator-owned deployment. Source inspection can extend outside the edit boundary; modifications cannot.

## Inspect before adapting

1. Resolve the executable and symlink to the installed source tree. Inspect the complete plugin, its callers, tests, and existing telemetry writer.
2. Follow the ordinary plugin dispatch path and enumerate the kwargs actually delivered. Separately trace any special native-tool dispatch path. Similar tool names do not imply identical caller context.
3. Inspect registry forwarding and the native delegate handler's parent argument. Read any convenience dispatch helper: does it receive the calling agent, use a global UI/CLI agent, or have no parent resolution in gateway?
4. Trace authorization, leaf/orchestrator permissions, depth/budget enforcement, active-child registration, and cancellation. Verify the invocation path preserves all of them; do not assume the handler enforces checks normally performed by the dispatcher.
5. AST inspection is useful for corroborating call kwargs and registration expressions without importing a runtime with startup side effects. It complements source tracing, not behavioral tests.

## Capability decision table

| Observed contract | Action |
|---|---|
| Parent-bound lifecycle available | Preserve it as preferred path, including telemetry and result semantics. |
| Lifecycle absent; registry receives authoritative caller context and native invocation preserves safety checks | Add the smallest native handler adapter; verify cancellation and permissions. |
| Native tool exists but caller context is missing or inferred from global state | Do not launch from the plugin; return explicit native-tool handoff. |
| Delegation unavailable to the caller | Offer current-turn use of the specialist prompt, explicitly non-delegated. |

Never promote task IDs or task text into proof of parent identity. Never obtain apparent compatibility by launching an independent agent CLI.

## Handoff contract

- `delegated: false`, stable machine-readable reason, and explicit statement that no child launched.
- Preserve original task and selected specialist prompt.
- Concrete ordered steps: specialist load, then the calling agent's normal native delegation call with the loaded prompt as context.
- Make delegation conditional on the tool being enabled for that caller; instructions cannot grant permissions.
- Keep telemetry truthful: an attempted launch that cannot happen may emit pending then failed under the existing event contract, never started/completed. Telemetry failure must not suppress the handoff or successful native delegation.
- If accessing a lifecycle facade can fail before launch, treat binding failure as unavailable. Do not indiscriminately catch post-launch errors and retry another launch path, which could duplicate children.

## Minimal stdlib checks

Use `unittest` and fakes following existing tests:

- Lifecycle preferred even when alternate dispatch exists.
- Missing request class and importable class with absent facade both hand off.
- Facade binding failure hands off without starting a child.
- Ordinary dispatcher kwargs lacking parent context never trigger global-parent resolution.
- Task, specialist identity, prompt, reason, and recovery steps survive fallback.
- Existing lifecycle telemetry, timeout/interruption behavior, and telemetry-failure isolation remain intact.
- If a native adapter is implemented, assert exact caller identity and verify unauthorized leaf/depth cases cannot invoke it; verify children remain registered for parent cancellation.

Run focused and related stdlib suites plus whitespace/diff checks. Report mocked tests separately from real provider-backed delegation; leave deployment and live calls to the designated operator when outside scope.

## Investigated example, not a permanent runtime limitation

In the Sales Academy compatibility investigation, the inspected Mac runtime's ordinary plugin dispatch passed `task_id`/`user_task`, while native delegate registration extracted `parent_agent` from kwargs. Native agent dispatch supplied `parent_agent=self` through a separate route. A convenience plugin dispatcher resolved a global CLI agent, which was not sufficient evidence of the actual caller in nested or gateway execution. The safe result was an explicit `sales_academy_load` → caller-native `delegate_task` handoff while retaining the newer lifecycle path.

Re-check these contracts on every target version. Do not encode a blanket claim that Hermes plugins cannot delegate, nor copy source line numbers or a local installation path as an API contract.
