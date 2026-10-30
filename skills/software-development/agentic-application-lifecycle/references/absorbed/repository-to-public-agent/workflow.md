---
name: repository-to-public-agent
description: Turn an existing repository into a specialized, runnable agent and deliver a verified public URL. Use when a user asks to analyze/clone a repo, specialize or extend it, run it, and make it publicly accessible.
---

# Repository to Public Agent

Deliver the whole outcome, not a local demo. The completion artifact is a verified public URL backed by the specialized agent.

## Definition of done

All must be true:

1. The repository is cloned into the intended workspace.
2. Its architecture, startup path, configuration, tests, and deployment model are understood.
3. Existing abstractions and dependencies are reused before adding code or packages.
4. The smallest specialization that satisfies the request is implemented.
5. A focused runnable check protects every non-trivial new path.
6. Local startup and relevant tests pass.
7. The public deployment is reachable from outside localhost.
8. The final response includes the exact public URL and any access requirements.

A local URL, an unverified tunnel command, or “ready to deploy” is not completion.

## Workflow

### 1. Inspect before editing

- Read the README, manifests, entrypoints, environment examples, deployment files, and agent/profile conventions.
- Trace the real request flow from UI/API entrypoint to agent execution.
- Search for existing helpers, profile schemas, authentication, deployment scripts, and tests.
- Record the minimum set of files that must change.

### 2. Establish a baseline

- Install using the repository's existing package manager and lockfile.
- Run the smallest existing test or startup check that proves the untouched repository works.
- Identify required secrets without printing or committing them.

### 3. Specialize minimally

Prefer, in order:

1. Existing repository profile/plugin/agent mechanism.
2. Existing helper or configuration schema.
3. Standard library or native platform feature.
4. Already-installed dependency.
5. Minimum new code.

Do not introduce a second framework, parallel configuration system, speculative abstractions, or a new dependency for a few lines of code.

### 4. Preserve trust boundaries

- Keep authentication and authorization server-side.
- Treat browser storage as untrusted; never expose privileged long-lived secrets to client code.
- Validate names, paths, URLs, and user-controlled configuration at the boundary.
- Protect reserved/default profiles and destructive operations in the backend, not only the UI.
- Back up mutable configuration before rename/delete/bulk updates when recovery matters.
- Escape rendered content and retain accessibility basics.

### 5. Verify locally

Leave one focused check for each non-trivial branch, parser, destructive path, or security rule. Then verify:

- syntax/build;
- focused tests;
- relevant existing suite;
- local health endpoint or real UI flow;
- agent-specific behavior rather than only page rendering.

### 6. Publish before polishing

Reserve execution budget for deployment. As soon as the minimum vertical slice works:

1. Start the production-equivalent local process.
2. Select the repository's existing deploy target or an already-configured hosting/tunnel option.
3. Publish it.
4. Fetch the public URL independently.
5. Exercise a representative public flow.
6. Only then spend remaining time on nonessential UI polish or extra tests.

If durable hosting requires unavailable credentials, use an already-authorized target or a temporary tunnel only when the user accepts its lifetime and constraints. Never invent a URL.

## Public verification gate

Before reporting success, verify from the public origin:

- HTTP response is successful;
- expected page/API identity is present;
- static assets load;
- authentication behavior is correct;
- one representative agent action completes;
- no localhost-only callback or asset URL remains.

Report whether the URL is durable or temporary and any expiration/process-lifetime caveat.

## Failure handling

- Retry transient deployment or tunnel startup with a bounded alternate strategy.
- If the public gate fails, fix the root cause and repeat the gate.
- If publication is genuinely blocked by user-owned credentials or permission approval, state the exact blocker and preserve the verified local state; do not claim the task is complete.

## Output

Keep the final concise:

- Public URL
- What was specialized
- Verification result
- Access/lifetime caveat, if any

Session-specific implementation notes belong in `references/`; see `references/agentic-os-profile-hub.md` for one example.