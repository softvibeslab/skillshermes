# Edge legibility: calibration and regression

## Observed calibration example

The AIS-OS 3D viewer's served graph contained 57 nodes and 34 edges, with 30 degree-zero notes. Connections looked absent because the shared `displayLink` predicate sampled edges and base opacity was extremely low. The source knowledge was not missing.

Showing all existing edges by default, raising base width to 1.4 and base opacity to 0.65 improved visibility while retaining selection emphasis. An intermediate width of 0.65 was still too faint during screenshot review. These are historical calibration values, not fixed recommendations for other scenes.

Only renderer source and its compiled bundle changed; original notes were preserved. A lightweight Node regression check covered visibility logic and browser inspection confirmed all 34 edge settings. This did not establish mobile interaction quality or prove every line was unoccluded at every camera angle.

## Reusable check

Use the application's actual shared visibility function, or an existing testable export, rather than maintaining a copied implementation that can diverge.

Minimum cases:
- Default, unfiltered small-graph view does not silently suppress existing edges.
- Selection emphasizes incident edges and preserves the intended treatment of other edges.
- Clearing selection restores the default view.
- Deliberate filters remain effective.

Then verify the rebuilt runtime and a screenshot. A unit test cannot establish visual contrast, and runtime edge counts cannot establish unobstructed visibility.

## Diagnostic pitfalls

- Check sampling and style before reingesting documents or generating inferred links.
- Distinguish orphan notes from hidden connections in the response.
- Reload after rebuilding so source changes are not confused with stale browser assets.
- Inspect default camera distance: a line that is visible only at extreme zoom is not a legible overview.
- Retain source privacy boundaries and local-only binding for private graphs.
