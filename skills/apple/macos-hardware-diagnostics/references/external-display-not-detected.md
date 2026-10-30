# External display black or not detected

## Separate three observations

- macOS enumeration: `system_profiler SPDisplaysDataType` reports whether the external display is currently registered. Only Color LCD means no external display was listed at that instant; it does not identify the faulty component.
- Monitor on-screen display (OSD): an HDMI label usually identifies the selected input, not a successful video handshake. Ask whether the physical Menu button displays the monitor's own menu.
- Physical image: black, backlit black, and an explicit No signal message are different observations. Absence of No signal is not proof of a valid connection.

## Bounded triage

1. Capture display enumeration once. After the user actually changes a cable, port, power state, or input, capture it again and report the delta briefly.
2. Establish the active topology with one concrete question: direct HDMI, USB-C-to-HDMI adapter, or USB-C-to-USB-C. If the user tried both routes, accept that and choose one route for the next controlled test; do not repeat the same ambiguous either/or question.
3. For a black monitor, test its physical Menu button. If its own menu is absent, isolate monitor power/OSD before changing Mac resolutions. A single monitor power cycle with the video cable disconnected can distinguish monitor behavior from source behavior. Ask about its power LED; do not declare hardware failure from one missing menu.
4. If the OSD works, select the exact connected input, keep one connection active, and change one variable: known-good cable, another input, or a known-good source. Prefer the test not already attempted.
5. A direct USB-C connection requires video capability in both the cable and monitor port. USB-C connector shape alone proves neither. Thunderbolt/USB4 reporting No device connected does not rule out a USB-C DisplayPort Alt Mode adapter or display. Empty USB output or an empty legacy `ioreg` class query is not independent proof of a disconnected or defective monitor.
6. If an external display becomes enumerated but stays black, switch to detected-but-black triage; preserve the readable screen and verify the target before any mode change. See `display-control-verification.md`.

## Mac configuration and driver branch

Use this branch immediately when the user has already tested the display successfully on another computer and requests software diagnosis rather than more cable tests.

- Cross-check current enumeration with CoreGraphics `CGGetOnlineDisplayList`, `CGDisplayIsActive`, and `CGDisplayIsBuiltin`. Preserve the only readable display.
- Inspect loaded Apple graphics components with `kmutil showloaded`; AppleDCP/AGX presence is evidence of loading, not evidence of error-free operation. Inspect running display utilities without interpreting no process matches as proof that none are installed.
- Inspect display preferences read-only. Numerous historical UUID mappings alone do not establish corruption.
- Bound WindowServer/kernel log queries by time and relevant events. Reduce output before returning it: prefer connection transitions, errors, selected modes, and nearby context over complete supported-mode tables. Do not silently truncate away the event sequence.
- Interpret `Failed to reevaluate modes in response to available modes changed` alongside subsequent events. A later `resolved mode list`, selected starting mode, or EDID update may show that processing continued. Neither the error nor a later mode-selection message alone proves the cause or current activation. Never use a display ID found only in historical logs for a mode change.
- Distinguish an attempted historical resolution from the current setting; qualify statements such as “macOS attempted this mode at that time.”
- If Settings controls cannot be identified reliably, use the safe capture alternatives in `display-control-verification.md`. An appropriate bounded manual fallback is System Settings → Displays → hold Option → Detect Displays, if available. State that this action is pending until the user performs it; do not imply it was executed remotely.
- After an actual detection or configuration change, recheck current enumeration and ask whether the physical image returned. Do not claim repair from logs alone.

## Monitor OSD compatibility branch

Use after reviewing the user's photos, particularly when Mac-side recovery or Safe Mode has already failed. Safe Mode persistence lowers the likelihood of login software; it does not prove hardware failure or eliminate OS/firmware causes.

- Read all supplied menu photos before requesting more. Generic manuals covering several sizes/resolutions do not establish this unit's exact model or native timing.
- Record visible settings verbatim. For example, `Fuente: Auto` and `UltraHDRMode: Auto` expose two reversible tests; they do not establish the cause.
- First select the actual connected input explicitly (e.g. Auto → HDMI), exit the OSD, and ask whether the desktop appears. If unchanged, test HDR processing off only if the monitor offers an Off/Apag. option. If choices are unknown, ask what is offered rather than inventing a menu path. Do not batch the tests or change color, aspect, and brightness without evidence.
- Explain that an OSD timing such as 1920 × 1200 at 60 Hz is a monitor-reported value, not confirmation of an active macOS desktop. It may describe a detected timing or retained information; do not assert which without a connection-change comparison.
- Hotplug plus EDID confirms detection/metadata activity, not successful pixel delivery. A `starting mode` number is not a resolution to decode by guesswork. If CoreGraphics lists only the internal display, do not force a mode on the historical external ID or jump to an EDID override.
- After a physical input/HDR change, recheck enumeration and obtain the user's visible-image result. Keep untested suggestions explicitly unverified; no successful fix is established merely by finding a plausible setting.
- On portable monitors, HDMI carries video, not their main power supply. If power remains unexamined, use the actual manual/power label to verify the separate supply; do not assume specifications from a generic booklet or repeat already-completed power tests.

## Pairing-specific failures and documentation stop rule

Maintain a compact ledger: test, route, observed result, evidence source (tool or user). Two successful wired cross-tests—monitor on another source, Mac on another monitor—narrow the fault to the pairing or its particular path; they do not distinguish OS regression, firmware, negotiation, or cable behavior. A user-reported USB-C attempt counts as completed, but do not silently upgrade it into proof that the cable and port support video. Revisit a detail only when it decides a specific next test, explaining why.

- Preserve the user's statement that the pairing previously worked. Ask about update/wake/reconnection onset early if unanswered; do not repeatedly ask whether either device works elsewhere.
- If several monitors were connected during the log window, correlate timestamps and identities before attributing EDID, CEC names, product IDs, or mode errors to the problem monitor.
- Preserve remote access (including Chrome Remote Desktop) as a recovery route; a readable remote session does not validate the physical output.
- For a factory reset, obtain the exact model from the label or listing. Search both the exact identifier and its shortened family name; verify manufacturer/model applicability before giving instructions. A generic booklet or visually similar product is insufficient for button sequences or firmware.
- If a search tool returns only a run/storage handle, retrieve the actual results before concluding that the search was empty. After bounded alternate queries fail, say “I did not find a verified reset procedure,” not “this model has no reset.” Request a purchase/support link only if it would provide a genuinely new documentation source.
- Stop speculative reset instructions when neither documentation nor the photographed OSD exposes a reset. State that repair is unconfirmed and give one evidence-driven next step, such as onset correlation or model-specific vendor support—not another round of completed tests.

## Avoid diagnostic loops

Do not keep issuing identical enumeration commands as the entire investigation when the connection has not changed. A user explicitly asking to validate deserves a fresh check, but pair persistent non-detection with one discriminating next test, not the same checklist again. If cable/input/source tests remain inconclusive, collect monitor and adapter models and inspect relevant display-link logs before recommending disruptive resets or service.

Report the boundary of evidence: “macOS does not list it” is supported by enumeration; “bad cable,” “dead port,” or “monitor failure” require isolation evidence. Never claim the problem was resolved without enumeration plus the user's confirmation of a visible image.
