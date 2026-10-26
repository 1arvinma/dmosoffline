# DMOS 1.4.0 verification

This report records preparation checks for the 1.4.0 GitHub release. Google Play publication remains pending account registration and payment.

Implemented Session Board, campaign-local save/export integration, desktop file-drop routing, multiple-PDF previews, a persistent music transport strip, Android native music controls and device-stream volume, and a Windows native media menu. No dependencies or app permissions were added.

Validation:

- 112 automated tests pass, including old migration/recovery tests and new board mutation, ID/link remapping, backup/export, current-combat preservation, stale-window save protection, file routing/limits/preview guards, and native media bridge checks.
- An isolated browser workspace confirmed scene creation, linked current-combat notes, Run scene, accessible Move to, desktop dragging between columns, keyboard duplication, confirmed deletion, and board persistence after reload.
- Phone viewport previews at 320 and 375 pixels show one selectable column, with counts and accessible movement controls. Selected-column badge contrast was corrected after visual review.
- Multiple PDF selection correctly previews separate assigned files; the test preview was cancelled without installing duplicate books.
- Windows installer compiled and its archive CRC passed. Android APK signature verifies and matches the existing Table signing identity, package com.dmos.table, version code 6. AAB validation succeeded. Android has no INTERNET permission.
- Source privacy/content audit passed with the unpublished private-marker configuration. Only the existing three approved PDFs are bundled; Quest LLC / quest.rasht and Mopodraws attribution remains.

Physical install-over-existing tests and actual media playback in third-party Windows/Android apps remain device acceptance checks. The Windows installer remains unsigned. File dragging depends on OS/WebView support; all existing pickers remain available. General ZIP archives are not supported as content packs; extract PDFs or use the existing DMOS ZIP format.

Save schema is now 3. Older app versions reject new exports rather than discard board data. Upgrade and restore retain their existing recovery-copy safeguards. Keep a full backup before upgrading.

The Windows installer keeps the established AppId and UsePreviousAppDir, hides the directory page to prevent accidental parallel installations, and serializes setup through a setup mutex. No install/uninstall cleanup targets the campaign profile. Install-over-existing on a separate physical device remains an acceptance check.
