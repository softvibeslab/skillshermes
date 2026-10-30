# Stale Instance and Dual-Authentication Diagnosis

## Symptom

The public dashboard loads, but a newly implemented feature reports `404`, `Failed to fetch`, or asks for an admin token that never works.

## Root-cause sequence

1. Read the tunnel control API or tunnel process arguments to find the actual local target.
2. Identify the listener PID on that port and its start time.
3. Probe a feature-specific API route on the tunneled port and every known development port.
4. Interpret the difference:

| Public/local result | Likely meaning |
|---|---|
| Root `200`, feature API `404` | Old build or wrong application instance |
| Feature API `503` | Route exists, required server configuration is missing |
| Feature API `401` without app token | Route and admin gate are active |
| Feature API `200` with both auth layers | End-to-end deployment is healthy |

## Minimal recovery

- Keep the public tunnel if it already targets the desired port.
- Stop only the stale listener.
- Start the current server on that port with its required application token and runtime roots.
- Verify the public feature route, not only `/`.

## Credential handling

If the original application token is unavailable, do not guess or scrape broad environment dumps. Generate a new high-entropy token, restart the intended application with it, and validate it through the public endpoint. Share tunnel credentials and application credentials as separate layers.
