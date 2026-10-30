# Localized specification handoffs

## When to use

A bounded documentation package defines a future product or assisted pilot, using local project documents as reuse evidence, with an explicit human approval gate. Pair with spec-driven-workflow where available; this reference handles evidence packaging and validation boundaries, not implementation.

## Deliverable and authority contract

- Preserve requested language and exact required paths; honor no-Git/no-publication instructions even if a general workflow normally calls for commits.
- Keep specifications Draft with author, date, version, reviewer and explicit approval pending.
- README must distinguish defined MVP from implemented product. A dashboard or recorded demo is not operational software.
- Leave files delegated to another agent untouched. Other projects are read-only evidence sources unless independently authorized.
- Stop at documentation and documentary validation. Do not generate product tests, provision services, contact participants or begin development merely because a validator passes.
- Proposed API contracts must be labeled proposed. A human operating protocol can explicitly have no new API; do not invent endpoints for a linter.

## Language-sensitive validation procedure

1. Inspect the actual installed script: header regexes, metadata markers, normative keywords, criterion numbering and scenario-clause recognition.
2. Run the original document with strict output and record score, findings and exit code.
3. If the failure is attributable to parser labels, create a temporary copy mapping only recognized structure. Keep the canonical document untouched.
4. Example Spanish-to-parser labels: Contexto → Context; Requisitos funcionales → Functional Requirements; Requisitos no funcionales → Non-Functional Requirements; Criterios de aceptación → Acceptance Criteria; Casos límite → Edge Cases; Contratos de API → API Contracts; Modelos de datos → Data Models; Fuera de alcance → Out of Scope. Metadata Autor/Fecha/Estado maps to Author/Date/Status. Scenario clauses Dado/Dada/Dados/Dadas, Cuando, Entonces map to Given, When, Then. Normative DEBE/NO DEBE/DEBERÍA maps to MUST/MUST NOT/SHOULD.
5. Prefer anchored header and clause-prefix transformations, avoiding prose, identifiers and code fences. Do not add missing clauses, references, requirements or entities. Preserve an auditable mapping.
6. Invoke the same unchanged validator on the temporary copy. Record both results; remove temporary files on exit. A small project-local adapter is suitable when ancillary validation files are authorized.
7. Independently compare all defined FR/NFR IDs to references in acceptance criteria. Check references in both directions; inspect each criterion for a testable result, not merely an ID mention.
8. Review contracts, data models, consent, retention, authorization, error cases and feasibility manually. The parser's score cannot certify those semantics.

Observed example: one parser revision recognized English-only headings and scenario tokens; three Spanish originals scored 0/100 while label-normalized copies scored 100/100 without findings. This is an observation about that parser revision, not a permanent claim about tool support. Inspect again before applying the workaround. Report original failure and normalized pass separately; never state that untranslated originals passed directly.

## Reuse evidence ladder

Document source path and relevant section, claim, candidate reuse, limits and required verification. A declared stack or security feature is documentary evidence, not runtime evidence. An existing single-admin CRM does not establish per-business authorization. Browser-local storage does not establish remote backup, encryption or durable persistence. Human-reviewed recommendations, local rules and actual model integration are different capabilities; label the origin honestly.

Conceptual candidates remain untested until inspected and exercised. Future reuse gates include ownership/licensing, dependency compatibility, synthetic fixtures, isolated persistence/retry tests, access-crossing negative tests, export/deletion and restoration. Never borrow client databases, contacts, credentials or private notes as test fixtures.

## Assisted-pilot measurement safeguards

- Define cohort, period, baseline source, denominator and minimum evaluable observations before launch. Historical self-report is not instrumented evidence.
- Separate meaningful owner activity from operator assistance. Measure support time, onboarding time, drafts created/reviewed/edited, copies, declared sends, attempts/errors and perceived burden.
- A copy is not a send; a declared send is not verified delivery; acceptance of a priced offer is not payment or revenue.
- If success requires repeated use AND improvement AND paid-offer acceptance, test all conditions for each business, then count qualifying businesses. Do not pool separate successes across the cohort.
- Null means unavailable, not zero. Insufficient/comparison-incompatible data yields inconclusive results. Do not change thresholds after observing outcomes.
- Keep commercial success separate from operational permission to scale. Security incidents, unresolved isolation or excessive support can block rollout even when customers express interest.
- Proposed thresholds, prices, roles, dates and retention policies need approval; no inferred commitments. Reconfirm external-event logistics rather than treating conversation history as an official agenda.

## Final report

Return exact artifact paths, actual validation commands/results, original versus normalized outcomes, remaining approval gates and actions deliberately not taken. Documentary validation is not a claim of runtime correctness, legal compliance or production readiness.
