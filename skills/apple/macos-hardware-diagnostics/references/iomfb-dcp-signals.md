# DCP / IOMFB signal interpretation

Use these messages as correlated evidence, not standalone proof of a failed part.

## High-value examples

- `Calibration failed to query calibrated backlight scaling factor from IOMFB`: the calibration/backlight path could not obtain expected framebuffer state. Correlate with visible brightness, gray-screen, wake, and link events.
- `IOMFB: panel charge parity violation`: an abnormal panel-path/framebuffer condition. Public evidence is insufficient to map this to one replaceable component.
- `Received brightness update when backlight is disabled`: a brightness request arrived while the backlight was considered off; useful around display sleep/wake transitions.

## Extracting useful evidence without overcounting

Start with a bounded unified-log interval (for example, the last 20 minutes) and predicates for `IOMFB`, `DCP`, `backlight`, and `Calibration failed`. Save raw output, then summarize exact message families with counts and first/last timestamps. Broad matches for `error`, `fail`, or `disabled` are discovery filters, not a count of actual faults: normal transitions such as `PPS disabled` and even records marked `E` can appear alongside failures.

Additional correlating messages include `stopALPM fail to wait for AUX availability`, `IOAVVideoInterface open failed`, and `Fixed payload verification failed`. These may involve external-display initialization too; do not assign every DCP/IOAV message to the internal panel. Re-read `system_profiler SPDisplaysDataType` after the user connects HDMI because topology, main display, and mirroring can change during the investigation. Preserve raw logs in a durable diagnostic folder, not only `/tmp`, when they may be needed for service.

## Stronger correlation pattern

1. Internal display/link or backlight turns off.
2. Wake or initialization begins.
3. DCP/IOMFB calibration, parity, or state-ordering errors occur.
4. The internal panel becomes gray, blurred, blank, or unstable.
5. An external-display modeset temporarily restores it.

This supports a DCP/IOMFB/internal-panel-path problem while leaving firmware/software and physical panel/backlight/connection causes open.

## Evidence that changes probability

- Fault at Apple logo, Recovery, or Diagnostics increases low-level firmware/hardware probability.
- Clean external output with broken internal output lowers total-GPU-failure probability but does not clear the internal display path.
- No GPU/kernel panic lowers panic-driven failure probability but does not clear the panel path.
- No thermal pressure means fan-control changes are not a display remedy.
- WindowServer resource reports are supporting symptoms only.

## Containment pattern

When failures cluster around wake, increase `displaysleep` and verify with `pmset -g custom`; temporarily disable automatic brightness; keep a fixed moderate brightness; avoid lid-close and repeated sleep/wake; and back up before reboot-heavy diagnostics. These are containment steps, not repairs.