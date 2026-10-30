---
name: macos-hardware-diagnostics
description: Diagnose and safely contain Mac hardware-adjacent symptoms using built-in evidence, reversible tests, and explicit service thresholds. Use for hot Macs, fan or thermal concerns, gray/blurred/blank/flickering internal displays, sleep/wake display failures, HDMI-dependent recovery, suspected throttling, and requests for temporary fan overrides.
version: 1.0.0
platforms: [macos]
metadata:
  hermes:
    tags: [macos, hardware, diagnostics, display, thermal, fans]
    category: apple
---

# macOS Hardware Diagnostics

Classify Mac thermal and display-path incidents without jumping from one symptom or log string to a component replacement. Gather evidence first, use reversible isolation, protect data, and escalate when early-boot or physical-path evidence crosses a service threshold.

## Step 1: Detect the incident class and available evidence

Collect the shared baseline:

```sh
system_profiler SPHardwareDataType SPDisplaysDataType SPPowerDataType -detailLevel mini
sw_vers
pmset -g custom
pmset -g therm
pmset -g assertions
```

Route by symptom:

- **Heat, fans, throttling, or maximum-fan request** → Thermal and fan workflow.
- **Gray, blurred, blank, flickering, failed wake, lid-angle sensitivity, or HDMI-dependent recovery** → Internal display workflow.
- **External TV cuts off the desktop on all four edges** → Suspect overscan/TV zoom, separate from internal-panel failure; follow `references/external-tv-overscan.md`. Inspect the explicitly selected external display for Underscan, then prefer the TV's native pixel-mapping control. Preserve readable output and verify the physical edges with the user.
- **External HDMI/USB-C monitor black or not detected** → Follow `references/external-display-not-detected.md`. Separate macOS enumeration, the monitor's own menu/input label, and the physical image. Recheck after a real connection change or an explicit validation request; otherwise advance to one discriminating test instead of repeating enumeration and the same questions. Thunderbolt non-enumeration does not rule out USB-C DisplayPort Alt Mode.
- **Both** → Run both evidence tracks, but do not infer thermal causation unless thermal pressure or repeatable heat correlation exists.

Do not use Intel-era SMC/NVRAM reset advice as the default on Apple silicon. Do not click permission dialogs or bypass administrator prompts.

## Step 2: Preserve state and establish scope

Record the Mac model/chip, macOS build, power state, incident timestamp, onset conditions, affected displays, and whether the symptom appears before login, after wake, under sustained load, or only in one account.

Before reboot-heavy diagnostics or service, complete a backup and copy irreplaceable files to a second destination. Never terminate high-load applications without permission.

## Step 3A: Thermal and fan workflow

1. Read `pmset -g therm`; distinguish recorded thermal pressure from a merely warm chassis.
2. Sample sustained load more than once:

   ```sh
   uptime
   ps -Ao pid,%cpu,%mem,comm -r | head -12
   ```

3. Inspect available sensors without assuming legacy Intel SMC keys exist:

   ```sh
   ioreg -r -c AppleSMC -l
   ```

   If authorized, `sudo powermetrics --samplers smc -i 1000 -n 1` may expose better data.
4. Report only measured sensors and their actual labels. Do not call battery or virtual temperature a CPU temperature.
5. Prefer automatic fan control. If the user explicitly requests a temporary override, follow `references/macs-fan-control.md`, verify preset plus helper/runtime state, and explain how to return to Automatic.

**Exit gate:** thermal pressure, sustained load, measured temperatures, and any fan-mode change are separately identified and verified.

### High-CPU background processes and storage analysis

When Activity Monitor shows `StorageManagementService` or `ApplicationsStorageExtension`, distinguish storage-size calculation from Spotlight indexing. Inspect a short native `sample <pid> 3` capture if permitted: `ComputeSize` and directory-iterator frames support directory traversal and size calculation, not proof of a stuck process. An open Storage settings panel is a hypothesis to test, not an established cause. Ask the user to close that panel and compare subsequent samples before suggesting termination.

Explain CPU accounting: a process can exceed 100% by using multiple cores; a process percentage is not the percentage of the whole machine. Separate sustained load from a single screenshot. Interpret swap alongside current memory pressure and compressed memory; swap already allocated is not evidence of current thrashing. Summed application RSS is approximate and can double-count shared memory.

For requests to turn diagnostics into a local monitoring/control dashboard, consult `references/local-process-control.md`. Treat its controls as safety requirements to implement and test, not as a verified implementation from a prior session.

## Step 3B: Internal display workflow

**Symptom-first triage:** When the user says the screen is gray/dark and then clarifies that nothing is visible, accept the physical observation and inspect display logs immediately. An enabled Dark appearance is not an explanation for an unreadable panel. A sharp, colorful screenshot proves only that the captured image is intact; it does not prove that the physical display is working. Ask whether an external display is readable, without making the user repeat the symptom.

1. Search the incident interval in unified logs and DiagnosticReports for kernel, WindowServer, powerd, DCP, IOMFB, backlight, calibration, link, sleep/wake, watchdog, SOCD, and panic evidence.
2. Classify the strongest evidence as session/software, firmware/display pipeline, or physical panel/path. A clean external display lowers the probability of total GPU failure but does not clear the internal panel path.
3. During active corruption, mirror to a known-good external display and take a screenshot. If the external output and screenshot are sharp while the internal panel is blurred, move the investigation downstream of composition.
4. Preserve a photo or video showing both physical displays. A screenshot cannot capture panel-path corruption.
5. Attempt only bounded reversible modesets. First establish which display is the user's only readable output and preserve it. Do not disable mirroring or disconnect the external display blindly when it is the recovery path. Select the internal display explicitly and, if available, test fixed 60 Hz; disable mirroring only when usable external output and a recovery route are established. Verify the target display and resulting mode. If the target cannot be identified, stop before changing settings and use the inspection/recovery procedure in `references/display-control-verification.md`.
6. Use `references/iomfb-dcp-signals.md` and `references/live-panel-path-incident.md`; correlate multiple signals rather than mapping one private Apple string to a replaceable part.

**Exit gate:** the fault is localized as far as evidence allows, containment has been tested once, and uncertainty between firmware, link/cable, controller, panel, and backlight remains explicit.

### Display inventory and connection changes

When asked to list connected screens, separate **physically connected (user-reported)**, **enumerated/online (macOS)**, and **physically readable (user-confirmed)**. Do not describe the OS list as a complete physical inventory. If the user adds a USB-C monitor that is absent from enumeration, retain it as an unrecognized third display rather than contradicting the report.

After a switch from USB-C to HDMI or removal of a recovery TV, refresh enumeration and identify the currently connected monitor before adjusting modes. Do not carry forward the old TV's identity, display ID, mirroring state, or readability. An asserted HDMI_HPD with only the built-in screen online means physical hotplug detection and desktop activation disagree; it does not establish successful video delivery.

For requests to “recalibrate and adjust resolution,” distinguish resolution/refresh, scaling/overscan, and color calibration. Monitor OSD values such as resolution at Hz, horizontal kHz, and pixel-clock MHz describe reported timing, not independent proof of an active desktop or editable macOS display. Do not change the internal panel to match an absent external monitor. Explain the blocker briefly, preserve visibility, and pursue detection first. Report whether Detect Displays was actually invoked or remains a manual next step—opening the settings pane is not a detection attempt.

### External HDMI missing from the display list

**Inspect monitor-side compatibility settings before speculative overrides.** When the OSD is readable, review the supplied photos and manual, distinguish visible settings from unverified options, and follow `references/external-display-not-detected.md` for a one-variable-at-a-time input/HDR test. A suggested change is not a verified fix. Do not infer active desktop video from an OSD timing readout, hotplug, EDID, or a historical starting-mode log alone.

**Honor completed isolation and user corrections.** When the user says the display works on another computer and asks to stop cable tests, acknowledge that once and move to Mac configuration, loaded graphics components, and time-correlated display logs. Do not restart the physical checklist or repeatedly ask an unanswered topology question. Working on another source narrows the investigation but does not prove every part of the Mac-side path is healthy. Ask about topology again only if it changes a concrete next intervention, explaining why.

**Keep an isolation ledger, not a repeated questionnaire.** Track each completed test and its result, including user-reported results, and consult it before proposing another action. If the monitor works on another computer and this Mac works with another monitor over the same physical interface, describe a pairing-specific failure—not a generally dead HDMI port or proven monitor defect. AirPlay is not a substitute for the wired cross-test. If this pairing previously worked, establish whether onset followed an OS update, wake, or reconnection; do not label it inherently incompatible. Ask only an unanswered question that changes the next intervention. After Safe Mode and reset attempts fail, do not restart those checklists or prioritize login utilities without new evidence.

**Model-specific reset requests need model-specific evidence.** Search the exact model and a shortened model identifier, then verify any manual against the unit and photographed menus. Never invent long-press combinations, hidden reset menus, or flash firmware for a similar-looking model. No search results means no verified procedure found, not proof that none exists. See the documentation stop rule in `references/external-display-not-detected.md`.

For a configuration/driver investigation, report separately: Apple graphics components loaded; current online/active displays; historical EDID and mode-selection events; relevant configuration overrides or running display utilities. Loaded drivers do not prove correct operation, and historical mode selection does not establish the current resolution or an active external display. Do not recommend third-party HDMI drivers or delete WindowServer preferences merely because enumeration failed. A WindowServer restart can log the user out: obtain explicit permission before session-disrupting recovery.

Do not infer no physical detection solely from `system_profiler SPDisplaysDataType` or an empty `ioreg -r -c AppleDisplay` query on Apple silicon. Cross-check `ioreg -l -w 0` for HDMI_HPD, active transports and EDID, and bounded `log show --last 10m --style compact --info` queries for WindowServer hotplug, modes, and kernel HDMI events. `log show` has no `--max-count`; bound time and reduce output in Python. An EDID/link present while CoreGraphics lists only the internal display means detection and desktop activation disagree, not proof of a bad cable or a specific component. Correlate timestamps; mode errors during unplug are not evidence of failure after reconnect. Never force a mode on a display ID available only in historical logs. If UI accessibility returns empty labels/zero bounds, do not click unidentified controls.

## Step 3C: Background-process monitoring and local dashboards

When a CPU investigation becomes a request for continuous monitoring or pause/stop/resume controls, follow `references/local-process-dashboard.md`. Reuse an existing local dashboard first; keep metrics, process controls, launchd service management, and AI recommendations separate.

Require backend-enforced protections for the system, active agent/runtime, terminal, and browser hosting the dashboard. A warning is not a substitute for protecting the only control/recovery surface. Revalidate process identity before signals; executable-path equality alone cannot detect every reused PID. Keep local AI opt-in and advisory, and distinguish an integrated button from a successfully tested inference.

For per-profile or per-agent views, distinguish configured profiles from observed running process groups. Attribute only with evidence, retain an explicit “Sin atribuir” group, and label summed RSS as approximate. Provide drill-down to the contributing processes, bounded CPU history, and working search/filter/sort controls. Never infer tokens, costs, or GPU use from CPU/RAM readings. See the attribution and verification checklist in `references/local-process-dashboard.md`.

**Exit gate:** metric freshness and overhead checked; control protections tested without disrupting user applications; service-control and AI verification limits stated explicitly. Dashboard updates must not restart agents merely to refresh monitoring. Do not promise optimization without affecting the user's activities.

## Step 4: Isolate safely

For display-path incidents, choose the smallest discriminating test after backup rather than treating updates, cold boot, Apple Diagnostics, Safe Mode, Recovery, and Disk Utility First Aid as a mandatory sequence. Disk repair/reinstall guidance for a Mac that cannot finish startup is not automatically appropriate when macOS runs normally on an external TV. Consider a non-destructive reinstall only while software/firmware remains plausible.

Apple silicon Diagnostics: shut down normally, hold the physical power button until startup Options appears, release it, then hold Command-D. Keep the recovery display and AC power connected. macOS Tahoe 26 and later can offer a specific integrated-display diagnostic. This requires user participation at the physical button; do not claim to have executed it remotely. Verify current instructions at https://support.apple.com/es-mx/102550 and request the result/reference code. A located YouTube title is not a validated procedure: label unreviewed videos and prioritize the official guide.

For thermal incidents, compare repeated samples under equivalent load and power mode. High Power Mode is not a cooling control and may increase heat.

Change one variable at a time. Verify the actual setting after each change.

## Step 5: Escalate or restore

Recommend Apple or an authorized provider when display corruption appears at the Apple logo, Recovery, or Diagnostics; changes with lid angle; shows lines/zones; returns a display code; persists after update and Safe Mode; or repeatedly requires HDMI recovery.

Restore temporary fan overrides to Automatic after urgent cooling. Remove emergency `caffeinate` sessions and temporary `Never` display settings when no longer needed.

## Step 6: Report

Return:

1. Hardware and OS baseline.
2. Incident class and evidence timeline.
3. Measurements actually obtained, with sensor/source labels.
4. Reversible changes applied and verification performed.
5. What was deliberately not changed.
6. Current containment, backup status, and service threshold.
7. Remaining uncertainty and the smallest next test.

## Pitfalls

- Do not diagnose overheating without thermal evidence.
- Do not equate WindowServer CPU use with root cause.
- Do not claim a fan RPM from app launch or preset state alone.
- Do not attribute early-boot corruption solely to login items.
- Do not reinstall macOS first or promise it will repair a physical display path.
- Do not continue disruptive resets after a framebuffer control test and verified modeset localize a downstream fault.

## References

- `references/iomfb-dcp-signals.md` — correlated DCP/IOMFB/backlight signal interpretation.
- `references/live-panel-path-incident.md` — active internal-panel incident capture and bounded recovery.
- `references/macs-fan-control.md` — temporary fan override setup, verification, and restoration.
