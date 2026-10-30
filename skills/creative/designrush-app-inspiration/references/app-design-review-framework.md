# App Design Review Framework

Use this rubric when evaluating DesignRush app references. Record only what is visible or explicitly stated; label interpretation separately.

## Evidence vocabulary

- **Observed:** directly visible in an image/page or explicitly stated by DesignRush.
- **Inferred:** plausible design intent derived from observed evidence.
- **Not verified:** source did not expose enough information.
- **Award winner:** DesignRush visibly labels the entry Winner and may show a jury score.
- **Featured:** promotional/editorial placement; not the same as an award.
- **Popular:** ranking or engagement signal; not proof of usability.

## 1. Product and audience fit

- What job appears central?
- Which audience cues are visible?
- Does the tone match the user's category and trust requirements?
- Is the reference useful for the same reason, or only visually attractive?

## 2. Information hierarchy

Inspect:

- primary action and first-attention element;
- heading/body/supporting-data hierarchy;
- progressive disclosure;
- empty, loading, error, or confirmation states when shown;
- density relative to the task.

Good transfer: hierarchy logic. Do not transfer exact copy or screen composition.

## 3. Navigation and flow

Inspect:

- bottom tabs, stacks, side navigation, gesture navigation, search, or command surfaces;
- location awareness and back behavior;
- number and clarity of top-level destinations;
- whether the critical task is reachable with minimal ambiguity;
- platform conventions and likely deep-link behavior.

## 4. Visual system

Capture roles, not raw assets:

- color: background, surface, text, accent, semantic states;
- typography: display/body/utility character and contrast;
- geometry: radius, border, shadow, elevation, icon style;
- layout: grid, alignment, whitespace, overlap, edge treatment;
- imagery: photography, illustration, 3D, data visualization.

## 5. Interaction and motion

Use only visible or described evidence:

- press/selection/loading feedback;
- transition purpose and spatial continuity;
- gestures and discoverability;
- reduced-motion implications;
- whether motion clarifies or merely decorates.

Never claim animation behavior from a static image.

## 6. Accessibility and usability risks

Check what can be checked visually:

- likely text contrast;
- touch target size and spacing;
- text size and truncation risk;
- reliance on color alone;
- icon-only controls without visible labels;
- dense or ambiguous navigation;
- content behind unsafe screen areas.

An award is not evidence of WCAG compliance or validated usability.

## 7. Signature and restraint

Name:

- **Signature:** the one memorable design move worth translating.
- **Restraint:** the elements kept quiet so the signature remains effective.
- **Ceiling:** where the pattern would fail for the user's app.

## 8. Synthesis score

Score only to prioritize references, not to declare an objective winner:

| Dimension | Weight |
|---|---:|
| Product/audience relevance | 30% |
| Flow/navigation relevance | 20% |
| Transferable visual system | 20% |
| Accessibility plausibility | 15% |
| Distinctive but usable signature | 15% |

Rate each dimension 1–5. If visual evidence is missing, mark it `N/V` rather than guessing and exclude it from the weighted score.

## Final extraction format

```text
Reference: <name + URL>
Evidence signal: Winner | Featured | Popular | Listing
Observed: <facts>
Inferred: <interpretation>
Transfer: <principle to adapt>
Avoid copying: <specific protected/distinctive elements>
Risks/gaps: <not verified or incompatible aspects>
```
