---
name: third-party-ai-app-evaluation
description: Install and evaluate third-party AI applications before integrating them into a privacy-sensitive product. Covers isolated setup, runnable verification, dependency/security/license review, data-flow analysis, and sidecar-vs-embedded integration decisions.
version: 1.0.0
created_by: agent
metadata:
  hermes:
    tags: [third-party, ai-apps, integration, security, privacy, licensing, evaluation]
---

# Third-Party AI App Evaluation

Use this when asked to install a GitHub AI application and explain how it could support an existing product.

## Goal

Produce a runnable, isolated installation and a grounded integration recommendation without contaminating the target product, exposing private data, or treating an upstream demo as production-ready.

## Workflow

1. **Keep repositories separate**
   - Clone into the user's normal code workspace, not inside the target repository.
   - Check whether the destination exists; update with fast-forward only when clean.
   - Read the license before proposing code reuse.

2. **Inspect before installing**
   - Read README, package manifests, Python metadata, `.env.example`, Docker files, API routes, storage adapters, and authentication/CORS configuration.
   - Identify mandatory external services, model APIs, cloud memory/vector/graph systems, exposed ports, and data retention paths.
   - Distinguish “OpenAI-compatible LLM” from “fully local”: other required cloud dependencies may still make the system non-local.

3. **Install in isolation**
   - Use the repository's documented package manager.
   - Keep Python in a project-local virtual environment; let `uv` select a compatible interpreter when the system Python is outside the declared range.
   - Do not create a real `.env` until credentials and data-handling scope are approved.
   - Never start a public service by default.
   - Treat an upstream `--dry-run` as untrusted until verified: snapshot the documented write targets first and inspect them afterward. Preview paths sometimes still execute unguarded copy/setup steps.

4. **Leave one runnable verification chain**
   - Build the frontend.
   - Run the smallest existing test suite.
   - Start the backend locally with temporary non-secret placeholders only when its health path does not call external services.
   - Probe health on localhost, then terminate the process.
   - Record warnings separately from failures.

5. **Audit without blind auto-fixes**
   - Run dependency audits and report direct/transitive severity.
   - Do not run broad `audit fix`, forced upgrades, or lockfile rewrites automatically; upstream version constraints may break.
   - If installation modified tracked lockfiles without an intentional dependency change, restore them after verification so the clone stays clean.

6. **Assess product fit**
   Evaluate:
   - exact capability supplied;
   - required compute and external services;
   - privacy boundary and whether raw data leaves the machine;
   - authentication, CORS, debug mode, upload limits, and API exposure;
   - license obligations, especially network-copyleft licenses;
   - whether outputs are evidence, hypotheses, simulations, or predictions;
   - operational cost and failure modes.

7. **Choose the first integration rung that holds**
   - Reference/idea only.
   - Manual offline experiment.
   - Separate localhost laboratory.
   - Isolated sidecar accessed over versioned HTTP.
   - Direct code reuse only when license, security, maintenance, and product value justify it.

   Prefer a sidecar for AGPL or operationally heavy applications. Calling a separate service reduces coupling but does not erase that service's own source-offer obligations; obtain legal review for commercial deployment.

8. **Protect real-world data**
   - Begin with synthetic fixtures or aggregated/redacted inputs.
   - Never upload chats, phone numbers, contacts, private messages, credentials, or identifiable profiles merely to test product fit.
   - Keep experiment seeds/results in a separate experiment directory rather than either repository; scan them for PII and secret patterns before upload.
   - Store local app secrets only in ignored environment files with restrictive permissions. If a credential is pasted into chat, configure it only when requested, avoid echoing it, and recommend rotation because transcripts are not a secrets manager.
   - Treat simulated outcomes as scenario exploration, not factual prediction.
   - Require human review before an output affects outreach, ranking, allocation, or decisions about people.

9. **Validate semantic output, not only task completion**
   - A green API task, generated report file, or completed process proves execution, not correctness.
   - Compare outputs against the seed domain, allowed actor classes, requested dimensions, language, and observable traces.
   - Reject domain drift, unseeded entities, unsupported percentages, prompt/tool leakage, and recommendations without evidence.
   - Preserve bad outputs only as `INVALID-*` diagnostic artifacts with a short validation note; never summarize them into product advice.
   - If a small model passes transport but fails semantics, rerun the same bounded fixture with a stronger model rather than expanding agents, rounds, or integrations.

## Deliverable

Report:
- absolute installation path;
- install/build/test/health results;
- how to start locally;
- missing configuration;
- security and license findings;
- 3–5 concrete product use cases;
- recommended integration boundary;
- what was deliberately not deployed or connected.

## Packaging and deployment boundaries

- Separate the user-facing client from the service that is actually self-hostable. A desktop GUI may belong on the workstation while only its relay/API stack belongs on a headless VPS.
- Read the production deployment documentation before using a root-level Compose file; many repositories keep the root bundle for development only.
- Before touching a VPS, verify non-interactive key-based SSH access, runtime prerequisites, occupied ports, deployment path, and whether DNS/TLS is available. Never ask for or type a server password; have the user authorize a public key.
- If an application owns a private package-manager prefix, repair dependencies inside that prefix. A generic system-global reinstall can succeed while leaving the application's private copy broken.
- Treat identical failures across many workers as evidence of a shared launcher/runtime failure before debugging workers individually.

## References

- `references/third-party-ai-app-evaluation-mirofish-nexo.md` — MiroFish-specific findings and a privacy-safe Nexo/Radar scenario-lab pattern.
- `references/third-party-ai-app-evaluation-buzz-self-hosting.md` — Buzz desktop/relay deployment boundary, VPS prerequisites, and private-prefix Codex ACP diagnosis.
