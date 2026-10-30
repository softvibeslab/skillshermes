---
name: prototype-codebase-audit
description: Audit static or frontend-only prototypes by tracing their real flows, validating documentation against runtime behavior, separating demo security from production controls, and verifying the result in a browser. Use for HTML/CSS/JS demos, generated Stitch exports, proof-of-concepts, mock dashboards, camera/biometric demos, and "analyze this project" requests where production readiness matters.
---

# Prototype Codebase Audit

Classify what exists before judging it: visual demo, functional prototype, or production candidate. A polished interface is not evidence of production architecture.

## Workflow

1. Inventory entry points, routes/hashes, scripts, styles, local assets, archives, generated references, package/build files, tests, and repository state.
2. Read the project documentation and design spec, then trace the executable flow end to end. Treat documented screens and integrations as absent until they are reachable in code or browser.
3. Inspect every caller/handler behind primary and sibling actions. Compare actions such as Confirm/Reject; identical handlers often expose the real product defect.
4. Map data boundaries: in-memory state, localStorage/IndexedDB, static fixtures, network calls, exports, dashboards, and any backend. Verify whether separate pages actually share state.
5. Audit security/privacy claims against implementation. Client-side credentials, roles, masks, timers, and hidden fields are presentation only.
6. Run the minimum checks: syntax, local asset references, image signatures, browser happy path, one failure/recovery path, separate admin/dashboard entry points, console errors, and permission-denied behavior.
7. If remediation includes debranding, sanitize the whole distributable—not only active source. Inspect archives first; remove or neutralize generated references, screenshots, filenames, docs, fixtures, storage keys, remote assets, distinctive colors, and branded examples. Prefer a generic label over inventing a replacement brand.
8. Report the real architecture, mismatches, flow defects, security/privacy limits, UX/accessibility findings, and the minimum next path for demo versus production.

## High-risk prototype checks

- Encryption of an export does not protect an unciphered source copy in browser storage or memory.
- Never normalize retention of CVV; expose only a verification result.
- Camera/biometric flows require purpose, consent, retention, deletion, and a non-biometric alternative before public use.
- Real-brand financial or identity forms can resemble phishing even with a demo banner.
- External fonts/images create network and privacy dependencies that can contradict offline claims.
- A hardcoded dashboard is not an integration, and a direct hash route is not an authorization boundary.

## Verification discipline

- Validate local `src`/`href` targets.
- Check file magic bytes; generated `.png` files may contain text error responses.
- Serve through localhost when camera or browser APIs require a secure context.
- State explicitly what could not be exercised, such as real camera capture.
- Do not modify the project unless the user asked for fixes.

See `references/static-prototype-audit.md` for the detailed reusable checklist and report structure.
See `references/prototype-brand-sanitization.md` for full-package debranding scope, minimal neutralization, and verification.

## Output

Lead with a plain verdict. Prioritize discrepancies and risks over a file tour. Distinguish "acceptable for an isolated demo" from "acceptable in production" and give the shortest remediation path for each.
