# Sensitive wellness lead ranking and synthetic simulation

Use this pattern when a coach, therapist, psychologist, or emotional-wellness brand asks for a global Top-N lead list, lead simulation, or audience-ranking experiment.

## Core correction

Do not interpret “find the best 500 leads worldwide” as permission to scrape people who appear vulnerable. Split the task into two distinct artifacts:

1. **Synthetic simulation** — personified archetypes and aggregate cohorts used to test messages, objections, geography, and scoring.
2. **Operational ranking** — deterministic ranking applied later only to first-party or opt-in records.

Never fabricate N named prospects to satisfy a quota. Top-N is a maximum: if only 180 records pass eligibility, return 180.

## Evidence hierarchy

Rank voluntary intent, not inferred distress:

1. Completed application or explicit request for a call.
2. Prior purchase with valid follow-up permission.
3. Webinar/event attendance with consent.
4. Inbound DM or explicit CTA response.
5. Started but incomplete application.
6. Recent reply to an authorized email/story.
7. Repeated contextual engagement only when a legitimate opt-in channel exists.

A follow, like, save, diagnosis-like phrase, or public post about pain is not permission for cold outreach.

## Eligibility gate before scoring

Require all applicable conditions:

- adult/elegible audience;
- consent or legitimate prior relationship;
- channel and purpose match the consent;
- not unsubscribed, blocked, or marked do-not-contact;
- language, modality, schedule, and service jurisdiction are compatible;
- no crisis signal that should route to human support instead of sales;
- enough evidence exists to explain inclusion.

Missing conditions become `NO_ELEGIBLE` or `REVISIÓN_HUMANA`; do not fill gaps by inference.

## Explainable 100-point score

- Consent and relationship: 0–25.
- Demonstrated intent: 0–25.
- Fit with the declared transformation: 0–20.
- Timing/readiness: 0–15.
- Operational compatibility: 0–10.
- Data quality: 0–5.

Use only self-declared goals for fit. Ability to pay may be used only when the person explicitly accepted an investment range or supplied budget; never infer it from city, job, appearance, nationality, or device.

Tie-break in this order: consent, intent, recency, declared fit, data quality, human review.

## Geography

Separate:

- **Documented cohorts** from existing audience research or first-party analytics.
- **Exploratory cohorts** proposed as hypotheses.

Geography may inform language, timezone, currency, regulation, modality, and cultural copy. It must not become a proxy for wealth, vulnerability, ethnicity, migration status, or lead quality.

For global work, analyze regions independently before pooling them. Label unvalidated markets explicitly.

## Synthetic-agent design

Use 8–15 agents, each representing a relationship/intent segment rather than one real person. Useful segments:

- recent buyer;
- dormant buyer;
- webinar attendee;
- responsive subscriber;
- inbound CTA/DM;
- incomplete applicant;
- complete applicant without appointment;
- past appointment without purchase;
- repeat engager without conversation;
- consented referral;
- ads form opt-in;
- collaboration/podcast opt-in.

Do not turn 500 real contacts into 500 LLM agents. It is expensive, privacy-invasive, and less useful than segment simulation.

## Minimal MiroFish-compatible package

MiroFish accepts seed documents plus a free-text simulation requirement. The minimum useful package is:

```text
experiment-name/
├── seed/
│   └── knowledge-base.md
└── SIMULATION_PROMPT.md
```

Seed upload formats are text-oriented (`.md`, `.txt`, `.pdf` in the UI). Keep the ontology-driving content within the first 50,000 characters. Put actors, organizations, event, scoring, constraints, and deliverables near the top.

Use synthetic IDs in reports. Ask for segment allocations and a Top 20 synthetic reference set, not 500 invented people.

## Prompt requirements

The simulation prompt should define:

- goal and simulated period;
- initial event;
- 8–15 synthetic agents;
- strategies to compare;
- eligibility gate and scoring rubric;
- exact prohibited inferences;
- required outputs;
- uncertainty labels: `HECHO`, `HIPÓTESIS`, `SIMULACIÓN`, `PENDIENTE`;
- pilot-first validation plan.

Useful comparison:

- Strategy A: intention first.
- Strategy B: narrative/offer fit first.
- Strategy C: balanced explainable score.

Ask for conservative, base, and expansive scenarios, but prohibit invented historical conversion rates or guarantees.

## Pilot before Top-N operation

Start with 20–30 warm opt-in records. Measure delivery, voluntary reply, application, appointment, attendance, confirmed sale, unsubscribe/block/report, and human handling time. Expand only after the small pilot proves the consent, message, qualification, and capacity assumptions.

## Privacy artifact rule

The simulation seed must contain no names, phone numbers, emails, private conversations, diagnoses, or clinical details. Use anonymized fields and aggregate distributions. Keep real records outside the simulation and apply the validated scoring model locally with human review.
