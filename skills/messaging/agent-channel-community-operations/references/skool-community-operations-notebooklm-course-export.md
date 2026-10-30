# Export one Skool course for NotebookLM

Use this pattern when the user wants a Skool course turned into a NotebookLM knowledge source and production prompts.

## Workflow

1. Resolve the exact community and course before extracting anything.
2. List the course structure, then fetch every visible lesson by stable lesson ID.
3. Keep unrelated courses out of the export even if they appear in the same community inventory.
4. Build two separate files:
   - `wiki_<course>_dataset.md`: source knowledge only.
   - `prompts_notebooklm_<course>.md`: instructions for podcast, video, infographic, and source audit.
5. In the wiki, preserve:
   - published course description;
   - modules and lesson order;
   - concepts, procedures, examples, prompts, activities, outputs, tools, glossary, ethics, and source limits;
   - exact numbers and constraints;
   - explicit labels for observed content versus editorial interpretation.
6. Do not invent missing lesson content. If a title promises one topic but the body duplicates another lesson, record the mismatch.
7. Check lesson counts, duplicate bodies, missing resources, stale prices, and tool-plan claims. Mark volatile facts for verification.
8. Keep generation prompts outside the uploaded dataset so NotebookLM does not treat instructions as course facts.
9. Add a final audit prompt requiring the generated artifact to be checked against the sources.

## Prompt set

Provide at least:

- Long podcast and short podcast.
- Explanatory video and vertical short video.
- Educational infographic and checklist infographic.
- Final source-grounding audit.

Each prompt should specify audience, duration or format, narrative structure, tone, required facts, prohibited inventions, ethics, and human review.

## Verification

- Re-read the opening of both files.
- Confirm the wiki names only the requested course.
- Confirm production prompts are not embedded as source facts.
- Report anomalies briefly to the user instead of silently repairing the remote course.
