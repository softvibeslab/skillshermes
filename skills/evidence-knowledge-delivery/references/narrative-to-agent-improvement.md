# From narrative inspiration to testable agent improvement

Use when a user draws an operational principle from a film, biography, interview, or success story and asks for an agent skill or improvement plan.

## Evidence layers

Keep four layers separate: depicted scene, retrospective testimony, independent historical record, and proposed operational transfer. An interview quote is not verified film dialogue; do not invent subtitles or timestamps. Separate event dates, interview dates, and page publication/update dates. Preserve chronology instead of collapsing successive attempts into one event.

Case anchor: José Hernández described a strategy change after the sixth rejection and eventual selection on the twelfth attempt. His interview recounts successive comparison and preparation, including pilot training, diving, and Russian-related work. This suggests hypotheses about preparation, not proof those attributes caused selection or form universal NASA requirements. The label “Principio Adela” was a proposed local name, not an established scientific method.

Relevant primary-source leads (revalidate before quoting):
- https://premierespeakers.com/speakers/jose-hernandez/posts/transcript-for-jos-hernndez-interview-on-the-beyond-speaking-podcast
- https://www.latimes.com/delos/story/2023-09-15/a-million-miles-away-alejandra-marquez-abella-jose-hernandez-nasa

## Convert the story into a hypothesis, not a prescription

Ask: Which demonstrable capabilities, practices, resources, and conditions distinguish comparable results; what is already present; what minimal intervention could test the gap?

- Benchmarking can use aspirational references with different resources if disclosed.
- Positive deviance requires genuinely comparable challenges and resources; matching job titles or visible spend is insufficient.
- Human deliberate practice is only an analogy for agent configuration/evaluation. Editing a skill does not train model weights.
- Seek failures with the proposed trait and successes without it. A winner's trait can be cause, consequence, selection signal, or coincidence.
- Count human support, review, access, maintenance, and care constraints. More effort cannot fix an unauthorized permission or external eligibility constraint.

Method leads: https://asq.org/quality-resources/benchmarking and https://positivedeviance.org/ . Do not reproduce quantitative claims from abstracts when relevant corrections remain unchecked.

## Minimal operational loop

1. Define task, beneficiary, observable success, budget, permissions, and stop rule.
2. Inspect available assets before proposing another agent or skill. A role description does not demonstrate runtime capability.
3. Freeze the current baseline, including its existing delegation behavior. Record model/version, tools, input state, and evaluator.
4. Locate the first supported deviation in observable traces. Classify specification/evaluator, environment/access, tool interface, missing information, context loss, coordination, verification, residual capability, or unknown.
5. Write evidence, candidate mechanism, rival explanation, and a refuting observation. Missing evidence is not a mandate to invent a gap.
6. Choose one reversible intervention. If a specialist found evidence but integration lost it, test evidence preservation rather than adding a researcher. Consider parallel tool calls before parallel agents when no independent reasoning is required.
7. Compare against baseline with equivalent conditions and total budget. If model, architecture, and budget change together, label a compound intervention rather than isolating architectural causality.
8. Retain, revert, or declare inconclusive. A valid result may be “change nothing” or “request access.”

## Two different validation gates

**Diagnostic skill quality:** Does it activate appropriately, cite real evidence, distinguish causes from symptoms, supply a falsifiable experiment, abstain when needed, and respect permissions? Include no-change, missing-access, noncomparable-reference, sequential-task, genuinely parallel-task, and malicious-source cases.

**Downstream improvement:** Does the selected intervention improve verified task outcomes, not just the persuasiveness of the diagnosis? Test separately. Use executable checks or source/state inspection where possible; optional LLM judges need calibration and cannot replace factual verification.

Separate development and reserved cases before tuning. The optimizer must not be able to read reserved answers/rubrics: another readable folder is not isolation. Reusing revealed reserved failures for tuning converts them to development cases. Record all runs and missing metrics as N/D; repeated trials of one case are not independent tasks. Small pilots can be inconclusive. Predefine meaningful improvement and critical regression limits without inventing statistical certainty.

Useful engineering leads:
- https://www.anthropic.com/engineering/building-effective-agents
- https://www.anthropic.com/engineering/demystifying-evals-for-ai-agents
- https://arxiv.org/abs/2503.13657 — failure taxonomy, not automatic root-cause proof.
- https://arxiv.org/abs/2512.08296 — version-sensitive agent scaling results; inspect current version and comparison budgets.
- https://www.anthropic.com/engineering/multi-agent-research-system — industrial case, not a universal causal estimate.

Count source independence: several engineering posts from one vendor are not independent replications. Do not copy historical benchmark percentages without checking version, denominator, and experimental conditions.

## Delivery and authorization

Deliver a synthesis plus a proposed skill contract: triggers/non-triggers, inputs, existing assets, gap evidence, rival hypothesis, intervention/control, evaluation, constraints, rollback, and decision status. Research approval does not authorize profile installation, SOUL rewrites, production experiments, spending, or recurring self-modification. Keep existing stop limits; renaming a retry as a new experiment must not evade them. Install only under explicitly authorized scope after the relevant validation gate.
