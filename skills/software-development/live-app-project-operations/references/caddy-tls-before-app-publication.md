# Caddy: valid TLS before application publication

## Trigger

A hostname resolves to the intended VPS, Caddy serves other sites, but the target fails its TLS handshake. Diagnose hostname routing separately from backend readiness.

## Minimal sequence

1. Query A/AAAA records and confirm the intended SSH destination. Recover the documented SSH user and key path, not passwords from history. Use BatchMode, IdentitiesOnly and strict host-key checking.
2. Inspect Caddy's systemd ExecStart to find the actual config. Follow imports; do not assume `/etc/caddy/Caddyfile` contains every site.
3. Check whether the exact hostname appears in the active configuration as well as disk files. The local Caddy admin API may expose the active JSON when enabled; filter output locally to hostname presence/relevant routing. Never print the complete JSON/config blindly.
4. If absent, and authorized, stage a new fragment in the existing import directory. Do not overwrite an existing filename. During secure integration, use a closed maintenance vhost:

```caddyfile
control.example.com {
    header Cache-Control no-store
    header X-Content-Type-Options nosniff
    respond "Control panel: secure setup in progress." 503
}
```

5. Validate the entire configuration using `caddy validate --config <actual-config>`. Reload the existing service only after validation succeeds. Preserve a rollback copy when modifying an existing owned fragment; if staging fails, restore/remove only that fragment and verify the previous config remains valid.
6. Request `https://control.example.com` with certificate verification enabled. Use a bounded retry only while certificate issuance is actually pending. An intentional 503 is not a reason to repeat requests with generic HTTP retry behavior.
7. Report evidence separately: DNS correct; TLS validated; maintenance 503; application not published. Curl can exit zero for HTTP errors unless configured otherwise, so inspect the response status.

## Publication gate

Replace maintenance routing only after the backend is loopback/private-bound and its authentication/proxy contract is tested. Verify unauthenticated rejection for UI, API and assets; authenticated success; foreign Origin/CSRF rejection; and browser functionality. Do not solve an Origin guard by blindly rewriting every incoming Origin as trusted.

A remote dashboard and a local Mac profile store are separate systems. Decide and verify the private transport before claiming remote management of Mac profiles. A healthy HTTPS vhost does not prove that transport, CRUD completion, or access to any profiles.

## Lessons from the observed recovery

An absent hostname in both imported files and active configuration explained a TLS internal-error response. Adding only an isolated maintenance vhost, validating and reloading Caddy yielded verified HTTPS with an intentional 503, without publishing privileged application routes. The reusable result is this safe diagnostic/staging pattern—not a claim that the application was deployed.
