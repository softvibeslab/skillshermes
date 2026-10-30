# Reuse-first pilot kickoff

## Trigger
A founder wants to turn several existing applications or agent systems into a new product, create a GitHub repository, document the MVP, and start specifications, often before an event.

## Bounded discovery
1. Recover the actual proposal and explicit exclusions from the conversation and project documents. Do not reconstruct missing decisions as facts.
2. Define one demonstrable user journey and inspect only assets relevant to it.
3. Record each candidate's source path/URL, inspected entrypoint, intended reuse, dependencies, privacy boundary, and evidence level: discovered / inspected / tested / integrated.
4. Missing README: list root contents, locate actual docs and entrypoints, then inspect the smallest relevant slice. A placeholder README is not proof of product functionality or its absence.
5. Fetch before decoding. Check the upstream API exit status; avoid treating the last command's successful exit in a compound shell command as success of all preceding lookups.

## Minimum artifacts
- README.md: problem, audience, current delivery state, links, and actual run instructions only when code exists.
- PROJECT_CONTEXT.md: canonical scope, source-of-truth links, verified reuse evidence, assumptions, and next decision.
- specs/001-core-journey.md: Draft status, functional/nonfunctional requirements, Given/When/Then acceptance criteria, edge cases, contracts/data model, exclusions, and reviewer decision.
- A small backlog linked to requirements; Issues or a markdown checklist suffice when a separate board is not requested.

Keep commercial hypotheses separate from tested facts. In an entrepreneur-quality-of-life product, include baseline task time and perceived workload alongside technical completion; do not promise savings before measurement.

## Approval and delivery gates
A request for initial SPECS permits drafting; it does not establish approval of newly invented requirements. If the active workflow requires approval before implementation, complete the authorized documentation/setup and present the concrete spec decision. Never self-approve or substitute a manual pilot for requested software without making the scope change explicit.

For an authorized new repository, default private unless the user requests publication, check for an existing destination first, and stage only reviewed artifacts. Verify the remote URL, visibility, branch, and uploaded files. If there is runnable code, verify its main journey separately from git publication. A board, star, repository, deployed URL, and working product are distinct outcomes.

## Interrupted or denied work
An explicit authorization denial is not a missing-permission error to work around. Stop the affected workflow and report completed versus unexecuted steps. Do not retry the same outcome through another command or tool. On an explicitly authorized resume, inspect real state before repeating creation. Skills maintenance is not consent to resume the product task.

## Final handoff
Report only evidence-backed outcomes: repository URL/visibility, actual artifact paths, tested MVP behavior if any, approval or integration still pending, and the next narrow decision. Avoid a feature tour for files or functionality that were only proposed.
