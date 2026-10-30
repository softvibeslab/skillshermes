---
name: secure-public-app-operations
description: Safely expose a local web application through a public tunnel, especially when the app has both tunnel authentication and application-level admin authentication. Use for ngrok or equivalent tunnels, stale-port diagnosis, credential rotation, and end-to-end public verification.
---

# Secure Public App Operations

Expose the intended application instance, not merely whatever process happens to answer on the configured port.

## Workflow

1. **Identify the intended instance**
   - Record the local port, expected application route, protected API route, and required environment variables.
   - Check which PID owns the port and when it started.
   - Compare the public tunnel target with the intended local port.

2. **Test behavior, not just reachability**
   - A `200` from `/` only proves that something is serving HTML.
   - Probe one feature-specific API route. A `404` often means the tunnel reaches an older process or wrong build.
   - Compare the same route on each candidate local port before changing anything.

3. **Configure layered authentication**
   - Tunnel authentication protects the entire public origin.
   - Application admin authentication protects privileged operations.
   - Generate a fresh high-entropy admin token when the active value cannot be safely recovered or verified.
   - Pass secrets through environment variables or a secret manager; never write them into source files or logs.

4. **Replace stale instances minimally**
   - Stop only the process bound to the target port.
   - Start the current application with all required environment variables.
   - Keep the existing tunnel when it already targets the correct port; restarting the tunnel is unnecessary.

5. **Verify the public path end to end**
   - Public request without tunnel credentials should be rejected.
   - Public dashboard with tunnel credentials should load.
   - Protected API without the application token should be rejected.
   - Protected API with both authentication layers should succeed and return plausible domain data.
   - Report the URL and required credential layers separately.

## Safety Rules

- Never infer a secret from an old test process or report a token that has not been verified against the live public endpoint.
- Do not expose a local administrative service publicly without an outer authentication layer.
- Avoid broad process kills; select the listener PID for the exact port.
- Do not print unrelated environment variables while looking for one secret.
- If credentials appear in process arguments, rotate them when practical because process listings may expose them locally.

## Verification

Run `scripts/verify_dual_auth_tunnel.sh` with secrets supplied via environment variables. It prints only status codes and never echoes credentials.

See `references/stale-instance-and-dual-auth.md` for the diagnostic pattern and interpretation table.
