# Live internal-panel-path incident recipe

Use when the internal Mac display is visibly blurred or gray while an external display remains usable.

## Preserve evidence first

- Keep HDMI/power connected, lid open, and avoid sleep or reboot until evidence is captured.
- Record the incident timestamp and extract a narrow unified-log interval.
- Photograph or video the internal panel and clean external output simultaneously.
- Take a macOS screenshot as a framebuffer control.

## High-value comparison

Internal panel blurred + mirrored external output sharp + screenshot sharp means the corrupt image is not present in macOS composition or the captured framebuffer. Correlate with DCP/IOMFB/backlight evidence; do not map one private Apple error code to a specific part.

Useful strings include `panel charge parity violation`, `Calibration failed`, `brightness update when backlight is disabled`, and DCP/IOMFB timeout, negotiation, link, or PMU errors.

## Reversible recovery boundary

1. Disable mirroring to force a display modeset; wait and inspect the physical panel.
2. If exposed, select the internal panel—not the external display—and set fixed `60 Hz`; verify the actual mode.
3. If the panel remains blurred, restore the preferred arrangement and stop experimenting.

A failed modeset plus sharp screenshots/external output and recurring DCP/IOMFB errors justifies backup, the latest compatible update, Apple Diagnostics, and physical service. Do not claim that restarting WindowServer or reinstalling macOS will repair a panel, link, TCON, or backlight failure.

## Reporting language

> The internal display remains blurred while HDMI output and macOS screenshots are sharp. A display modeset did not recover it, and DCP/IOMFB errors coincide with the incident. This localizes the fault downstream of the shared framebuffer, but only Apple diagnostics or physical inspection can distinguish firmware, link/cable, controller, panel, and backlight causes.