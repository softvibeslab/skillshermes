# Project-channel context bootstrap

Use this when a workspace has one Slack channel per project and the user wants Hermes added plus a current status posted.

## Minimal workflow

1. List messaging targets first. Treat a resolvable `slack:<channel>` target as evidence that the app can currently address that channel, not as proof that project context is accurate.
2. Build the channel → repository map from channel names and local discovery. Mark uncertain matches explicitly; never silently bind a project to a plausible-looking repo.
3. Inspect each repository using the same small evidence set:
   - README / PROJECT_CONTEXT / STATUS / TODO / release checklists
   - active branch, upstream relation, recent commit
   - dirty/untracked work
   - latest recorded test/build/deploy evidence, with its date
4. Post one compact context card per channel:
   - purpose
   - verified current state
   - blockers/risks
   - one next step
   - exact repository path
5. For private channels, invite Hermes through the channel UI when API membership is unavailable. Re-list messaging targets afterward; the private channel should now resolve.
6. Send the card through the messaging API/tool and retain the returned channel/message IDs as verification.

## Slack UI pitfall

An invite confirmation can be opened from a mention while Slack navigation changes underneath it. Before pressing **Add**, verify the visible channel name. Afterward verify both the join event in that exact channel and the refreshed messaging target. If the wrong channel was selected, navigate by the labeled channel/history item rather than stale coordinates.

## Status language

Separate current evidence from historical evidence:

- “Tests pass” only when rerun now.
- “A dated report records tests passing” when relying on repository documentation.
- “Candidate repository” when project identity is not confirmed.

Do not persist volatile status in global memory. Keep it in the project channel or project documentation.