# Gateway dashboard onboarding and public preview

## Source and scope

Derived from a session cloning https://github.com/el operadorDevAndroid/freellmapi.git, extending its existing dashboard with Spanish onboarding, and providing a temporary public preview. The surviving handoff reports build and focused onboarding tests, desktop/mobile browser checks, and unauthenticated rejection for administration and inference. It explicitly reports that real inference was not tested because provider credentials were not configured. These are historical observations, not a guarantee about upstream or current deployment state.

## Reusable setup sequence

1. Sign in to the existing dashboard.
2. Add the user's provider key through the application's protected credential flow.
3. Configure available models and fallback order.
4. Run a representative prompt in the existing playground; only then mark inference verified.
5. Connect a client with the gateway's unified key and its verified OpenAI-compatible base URL, including `/v1` when that is the actual route.

Explain the two credential roles: upstream provider key authenticates the gateway to the provider; gateway key authenticates the user's application to the gateway. Do not publish either value in onboarding examples. Model fallback routes requests; it does not remove provider quotas or guarantee free access.

## Minimum onboarding surface

Reuse existing layout, authentication, styles, and navigation. Add a single entry page containing a configuration-driven checklist, short setup instructions, and a copyable integration example with placeholders. Avoid a duplicate dashboard, separate auth system, or a new framework just for onboarding. Translate new user-facing text consistently without rewriting unrelated screens.

## Verification matrix

- Build and focused tests: page renders and checklist behavior matches configuration.
- Browser: desktop/mobile navigation, assets, and console errors.
- Public origin: fetch the actual returned URL, not just localhost.
- Authorization: admin and inference routes reject unauthenticated requests; authenticated success is tested separately.
- Inference: one real provider-backed prompt when credentials and authorization exist; otherwise label untested.
- Dependencies: distinguish production vulnerabilities from development tooling; a clean production audit is not a complete security assessment.
- Lifetime: temporary tunnel availability depends on host, app process, and tunnel process; do not describe it as permanent hosting.

## Handoff

Lead with the verified public URL and its lifetime caveat. Give the setup sequence, then exact tests and untested boundaries. Keep credentials out of Git and prose. A private local credential file, if required, must have restricted permissions; report only its path. Save a local usage/restart guide, but never make a short-lived hostname a durable skill default. Re-discover routes, commands, and dependency versions from the next repository rather than copying this session's runtime assumptions.
