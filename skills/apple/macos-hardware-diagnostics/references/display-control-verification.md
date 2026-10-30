# Display controls: preserve visibility and verify changes

Use when an internal panel is unreadable and an external monitor or TV is the recovery output.

## Inspection and recovery

1. Establish which physical display is readable, whether mirroring is active, and how to restore the current working configuration before a modeset.
2. Load the macOS computer-use skill before desktop automation. Discover the actual running app identity rather than assuming its localized display name matches the automation target.
3. Treat a zero-sized capture or empty accessibility tree as inconclusive inspection, not evidence that display controls are unavailable. Rediscover the app/window and retry a scoped SOM or AX capture. A populated tree with blank labels and zero bounds is also insufficient to identify the internal-display controls safely. Do not click remembered coordinates or anonymous element indices. For framebuffer evidence, native `screencapture -x <output.png>` followed by image inspection can provide an independent capture; prefer a scoped window capture when possible to avoid unrelated private content. This fallback does not itself authorize coordinate clicks or establish that the physical panel works.
4. Identify the internal display explicitly before changing refresh rate. A fixed 60 Hz option may not exist for every panel or current mode. Never change the TV's mode merely because its controls are visible.
5. Preserve the external recovery output. Do not blindly toggle mirroring, disconnect the TV, restart WindowServer, or reboot while the user depends on it for visibility.
6. After one reversible change, read back the setting and ask whether the physical panel improved. A successful click is not verification; a clean screenshot does not prove a physical panel is fixed.
7. If bounded inspection still cannot identify the control safely, request a photo of the Displays window or one manual step. State that no setting change has been verified.

## Evidence and reporting

Separate observations, attempted actions, verified changes, and hypotheses. After context loss, recover prior evidence before citing specific log errors or claiming a hardware diagnosis. If evidence cannot be recovered, label earlier statements as unverified rather than repeating them as findings.

Describe fixed-refresh testing as a reversible isolation test, not a promised repair. Escalation should cite supported recurrence or diagnostic evidence and retain uncertainty about firmware versus physical display path.
