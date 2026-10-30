# Source-grounded agent Wiki, knowledge base, and podcast

Use this pattern when an external agent catalog, prompt library, or orchestration repository must become understandable without copying the entire upstream project into the portfolio.

## 1. Inspect before explaining

Record:

- upstream repository URL;
- branch and exact commit analyzed;
- license and required attribution;
- agent/division counts derived from source files, not README claims;
- schema/frontmatter validity;
- native integration or router behavior;
- validation command and result.

Keep changing counts tied to the analyzed commit. Do not present them as timeless facts.

## 2. Prefer lazy specialization

A large catalog does not imply one persistent runtime profile per specialist. Default architecture:

```text
orchestrator → search catalog → inspect specialist → load context → delegate temporary worker → evidence → review
```

Create a persistent profile only when the role needs durable memory, credentials, a dedicated channel, a separate workspace, or recurring autonomous work. Otherwise, use on-demand delegation to avoid duplicated configuration and context overload.

## 3. Separate source, knowledge, and navigation

- Keep the upstream checkout separate or pinned as a submodule/source reference.
- Put canonical explanations in a versioned `knowledge-base/` directory.
- Put concise Wiki navigation pages in `docs/wiki/` or an equivalent staging directory.
- Publish those pages to the platform Wiki only after local review.
- The Wiki summarizes and links; it is not the sole source of truth.
- Preserve attribution and clearly distinguish upstream facts, local adaptations, and proposed architecture.

Minimum canonical set:

1. overview and relationship to the local product;
2. orchestration architecture;
3. specialist catalog or capability map;
4. source, license, provenance, and analyzed commit;
5. podcast or explainer prompt.

## 4. Build a source-grounded podcast prompt

A useful understanding-oriented prompt specifies:

- audience and prior knowledge;
- learning objectives stated as what the listener can explain afterward;
- target duration;
- hosts and conversational roles;
- ordered segments from problem to example to governance;
- one complete end-to-end case;
- tone and locale;
- factual boundaries and attribution;
- derivative outputs: title, description, timestamps, key ideas, glossary, and comprehension questions.

Require the generator to:

- define terms on first use;
- distinguish facts, proposals, and analogies;
- avoid invented metrics or cases;
- tie repository facts to the analyzed commit;
- state human approval boundaries;
- cite the upstream project and license.

## 5. Publication sequence

1. Write and validate canonical knowledge-base files.
2. Stage concise Wiki pages locally.
3. Validate relative links and scan for secrets/private paths.
4. Commit and push the main repository.
5. Clone or initialize the separate Wiki repository.
6. Copy only reviewed Wiki pages, commit, and push.
7. Verify the public Wiki and links by fetching them again.

If authorization or publication is denied, stop at the local staging state. Report exact created paths and say publication is pending; never describe the Wiki as public until remote verification succeeds.
