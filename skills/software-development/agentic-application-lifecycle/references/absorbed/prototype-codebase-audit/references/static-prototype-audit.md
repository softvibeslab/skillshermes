# Static Prototype Audit Checklist

## Discovery

- Identify all entry points and whether each is connected to the others.
- List routes/hashes from executable code, not only documentation.
- Separate current source from ZIP snapshots and generated reference screens.
- Note missing Git history, build metadata, dependencies, and tests as maturity signals—not defects by themselves.

## Runtime truth

- Compare each documented edge and button with its actual handler.
- Exercise the happy path and at least one recovery path.
- Open admin/dashboard pages independently and verify their data source.
- Check direct-route behavior and browser Back/Forward handling.
- Inspect console errors and permission-denied states.

## Data and security

- Inventory every stored field and image, including unencrypted originals retained beside encrypted exports.
- Distinguish masking from access control and frontend passwords from authentication.
- Check third-party requests made by fonts, images, analytics, or APIs.
- For financial data, flag full PAN/CVV retention patterns and misleading security language.
- For biometrics, check consent, purpose, retention, deletion, alternatives, and public-brand risk.
- For cryptographic exports, verify the consumer/decryption workflow, key ownership, schema validation, and failure handling.

## Deterministic checks

- Parse HTML and confirm local `src`/`href` targets exist.
- Run language syntax checks.
- Compare file extension with magic bytes for generated images.
- Confirm archives are intentional deliverables rather than stale source copies.
- Use localhost for APIs restricted under `file://`.

## Report template

1. Verdict and maturity classification.
2. Real architecture and data boundaries.
3. Critical documentation/runtime mismatches.
4. Product-flow bugs.
5. Security and privacy limitations.
6. UX and accessibility strengths/risks.
7. Verification performed and untested areas.
8. Minimum path if it remains a demo.
9. Separate minimum path if production is intended.

Keep the report evidence-led. Cite files/functions or line ranges for important claims. Avoid treating missing enterprise features as defects when the stated scope is only a demo.