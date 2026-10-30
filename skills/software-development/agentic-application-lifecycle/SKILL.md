---
name: agentic-application-lifecycle
description: >
  Inspect, specialize, configure, secure, deploy, and verify agentic applications across repositories, local model profiles, public web endpoints, tunnels, and voice/telephony integrations. Use for prototype readiness audits, turning a repository into a runnable public agent, Ollama-backed coding profiles, layered public-app authentication, SIP/PSTN voice agents, or end-to-end agent delivery.
---

# Agentic Application Lifecycle

Operate the full class of agent-enabled applications from reality check to verified production-equivalent access. Route to the relevant lifecycle stages rather than creating a separate skill for each repository, deployment incident, model provider, or integration.

## Step 1: Detect architecture and available paths

Inventory repository instructions, manifests, entrypoints, routes, state stores, tests, deployment files, profiles, model endpoints, integrations, ports, credentials requirements, and runtime processes.

Detect rather than assume:

- repository package manager and established extension/profile mechanism;
- local versus hosted inference and structured tool-call support;
- server/client trust boundaries;
- existing deploy target, reverse proxy, or tunnel;
- external roles such as orchestrator, voice platform, carrier, SIP server, human endpoint, and CRM;
- authorization to edit, start processes, expose publicly, place calls, or deploy.

Prefer existing project mechanisms and configured infrastructure. Do not add a second framework or new service when a native path satisfies the outcome.

## Step 2: Classify current reality

State whether the system is a visual demo, functional prototype, production candidate, or live service. Trace the executable flow end to end; documentation, dashboards, hidden fields, client-side roles, and hardcoded data are not proof of backend behavior or authorization.

Check sibling actions, error/recovery paths, data persistence, network calls, separate admin surfaces, local asset integrity, console errors, and security/privacy claims. Report discrepancies before proposing architecture.

## Step 3: Define the minimum vertical slice

Write a definition of done that proves the requested class of behavior:

- repository specialization: smallest change through existing abstractions;
- local model profile: isolated profile, correct workspace, constrained tools, safe approvals, and one real tool call;
- public application: intended process on intended port, layered authentication, external reachability, and one representative action;
- voice agent: explicit call path from control plane through voice platform and carrier to PSTN/contact, with callback lifecycle.

Reserve execution budget for end-to-end verification; publish or place one controlled test before nonessential polish.

## Repository-to-dashboard onboarding

When asked to clone, explain, add onboarding, and publish a repository, inspect its existing dashboard before creating another app. Extend the current navigation and authentication with a small guided entry page, a setup checklist, and a working integration example. Derive checklist state from actual configuration; distinguish configured from successfully tested. Keep provider credentials separate from the gateway's client-facing key, and explain free-tier limits rather than implying unlimited free inference.

Treat publication and domain functionality as separate verification claims: build/tests, desktop/mobile navigation, public-origin reachability, and unauthenticated rejection can pass while live inference remains untested. If provider keys are absent, explicitly report that boundary; do not invent a successful completion or request secrets in chat. Verify both administration and inference protections before exposing a gateway. Report production dependency findings separately from development-tool findings.

Provide a concise local operator guide with start/stop/restart commands, configuration locations, and the setup order. Do not put generated credentials in the repository, guide, URL, or final response; if a private local credential file is used, restrict its permissions and deliver only its path. A temporary tunnel URL must be labeled process-lifetime access, not durable hosting, with its dependency on the host and tunnel clearly stated.

See `references/gateway-dashboard-onboarding.md` for the FreeLLMAPI-derived setup sequence and verification matrix.

## Step 4: Preserve trust boundaries

Keep authentication and authorization server-side. Treat browser storage and UI state as untrusted. Validate names, paths, URLs, webhook bodies, and user-controlled configuration at boundaries. Back up mutable configuration when recovery matters.

Use isolated profiles and least-privilege tools. Never clone unrelated secrets, sessions, messaging tokens, or memory. Keep gateways stopped unless requested. Pass secrets through environment variables or secret managers, redact logs, rotate exposed credentials, and never report an unverified token.

For public admin services, require an outer tunnel/proxy authentication layer plus application-level authorization. Stop only the exact listener process when replacing a stale instance.

## Secure browser credential setup

For API-key setup in an existing dashboard, first read the full relevant handler/provider, tests, and static files and check Git status. Prefer a surgical extension of existing authentication, CSRF, styles, and provider seams. For code-only requests, use installed SDK inspection and offline mocks: do not deploy, open a tunnel, edit other profiles, or make live provider calls. Never ask for the key in chat.

Validate an explicit candidate key with a bounded read-only SDK request before persistence or provider activation. Preserve environment precedence, sanitize all errors, expose only configuration/validation status, and publish private credential files atomically. Reject existing configuration unless replacement was explicitly designed; atomic replacement alone does not prevent concurrent overwrite. Clear the password input on submission and use relative URLs for proxy subpaths, verifying trailing-slash behavior separately from HTTPS/private ingress.

Leave runnable safety checks for authorization, CSRF, input shape, secret leakage, file permissions, and failure preserving previous configuration. Report exact changed paths and executed test results; distinguish mocked success from live verification and stop rather than bypass a denied command.

See `references/secure-credential-setup.md` for the persistence/activation ordering, concurrent-write pitfall, proxy-prefix checks, and offline regression matrix.

## Step 5: Configure model and workspace execution

For local OpenAI-compatible inference, verify endpoint reachability, declared and runtime context, host capacity, and model/tool compatibility. Coding quality and structured function calling are separate capabilities.

Bind both terminal and file-tool behavior to the intended project. Add concise project instructions with constraints and verification commands. Start with a narrow tool surface and expand only after the model reliably selects tools.

Probe structured `tool_calls` at the endpoint, then force a read-only agent tool call against an unpredictable sentinel. Require the trace to show tool name, arguments, successful result, and the post-tool model turn. Validate execution and final prose separately.

## Step 6: Integrate external control planes

Model vendors by role, not brand:

- orchestrator manages contacts, scheduling, retries, webhooks, and audit;
- voice platform manages conversational media and call control;
- carrier/trunk provides DID/caller ID and PSTN ingress/egress;
- softphone is an optional human endpoint;
- PBX/SIP server provides routing/registration policy, not automatic PSTN service;
- client SDK is not automatically a ready REST service.

For telephony, confirm host/port/transport, registration versus trunking, authentication, outbound permission, caller identity, E.164 format, codecs/DTMF, concurrency/CPS, RTP/NAT, transfer support, and event guarantees before generating production workflows.

Use idempotent action contracts and normalized signed webhook events. A one-person “call now” authorizes only that call; campaigns require explicit audience, volume, objective, and schedule confirmation plus consent/suppression controls.

## Scoped lifecycle telemetry changes

When the user requests a time-boxed, code-only change, treat the named files and exclusions as the execution boundary: read the wrapper and existing event writer, implement the smallest change, run offline tests, and return paths plus test results. Do not expand into deployment, profile edits, services, or live LLM calls when another operator owns them.

Telemetry must describe observed lifecycle facts rather than wrapper-level success: attempted is pending, started follows successful launch, completed requires a ready successful terminal result, fallback/error is failed, and still-running work remains pending. Keep correlation separate from the model's task. Reuse the existing validated event writer; isolate telemetry failures from delegation and log only a generic local warning, not exception text or private outputs.

See `references/lifecycle-telemetry.md` for the event contract, privacy boundary, offline test matrix, and secure-filesystem fixture pitfall.

## Native delegation compatibility across runtime versions

When repairing a plugin without upgrading its host, resolve the executable/symlink and inspect that installed runtime, not just upstream APIs. Trace the full call chain from the calling agent through dispatch, registry, handler kwargs, and child lifecycle. A native tool being registered does not prove the plugin receives the authenticated caller context needed to invoke it safely.

Prefer the existing parent-bound lifecycle. Use a native registry handler as compatibility only when the actual caller's parent context and permission checks are demonstrably preserved, including leaf-role restrictions, depth/budget limits, child registration, and cancellation. Do not infer the caller from a global CLI agent or start an autonomous CLI subprocess as a substitute.

If the contract cannot safely supply the parent, return an explicit non-delegated handoff: preserve the specialist/task prompt, instruct the caller to load the specialist and invoke its own native delegation tool only if enabled, and provide an honest current-turn fallback. Preserve existing telemetry and distinguish successful handoff construction from actual child execution. Report a safe fallback as a fallback, not as repaired automatic delegation.

See `references/parent-bound-delegation-compatibility.md` for source-inspection checkpoints, a capability decision table, and stdlib regression tests. These checks are capability-based; re-inspect each installed runtime rather than treating one host's missing API as permanent.

## Step 7: Verify in layers

Run the smallest checks that catch real failure:

1. syntax/build and focused tests;
2. local health plus one domain-specific feature route;
3. failure/recovery and permission-denied behavior;
4. process/port identity and current build;
5. public-origin HTTP, assets, authentication, callbacks, and one representative action;
6. for local models, exact sentinel tool result;
7. for voice, one consented PSTN call, two-way audio, DTMF, caller ID, webhook lifecycle, and transfer if required.

A `200` at `/`, an exit code of zero, a successful SIP registration, or an unverified tunnel command is not completion.

## Step 8: Release and report

If public delivery is requested, independently fetch the public URL and exercise the real flow. State whether access is durable or process-lifetime limited. If credentials or approval block deployment, preserve verified local state and name the exact blocker without claiming completion.

Return:

1. Current classification and architecture.
2. Changes or specialization made.
3. Tests and live verification performed.
4. Public URL/call identifiers only when independently verified.
5. Authentication, access, compliance, and lifetime caveats.
6. Minimum next action.

## Reference files

Detailed workflow banks under `references/absorbed/` preserve implementation recipes and scripts:

- `prototype-codebase-audit/` — static prototype tracing, debranding, security/privacy, and browser audit.
- `repository-to-public-agent/` — repository specialization and public deployment workflow.
- `secure-public-app-operations/` — stale-port diagnosis, dual-auth tunnels, and verification script.
- `local-model-agent-profiles/` — Ollama/compatible profile setup, context/tool-call probes, and IDE adapter notes.
- `voice-agent-telephony-integration/` — SIP/PSTN role maps, n8n control planes, campaign contracts, and call verification.
