# Release audit — 25 October 2026

Public target: 1arvinma/dmosoffline, v1.2.0-open.

## Before publication
- Existing GitHub main had only README.md and LICENSE, with one initial commit using a GitHub noreply address. Its existing prealpha release asset was downloaded and checked against GitHub's SHA-256. It contains seven source/scaffold files, no PDF archives or signing stores, and no matches for the audited device paths, personal support contacts or credential markers. It was left unchanged.
- New release is assembled from an explicit clean source tree, not the whole development workspace. No personal starter party, imported campaign files, compatibility table, real-party regression fixture or signing material is selected for publication.
- A copied test that referenced real-party names/values was found during the audit and replaced with a synthetic Example Hero record before publication.
- 63 clean-source tests passed: engine/imports, onboarding, unique stat slots, populated routes, EF notes, empty fresh start, sheet escaping/privacy and touch-dice behavior.
- Release scanner checks all selected source/generated assets for private identifiers, local user paths, credential patterns, key-store extensions and starter-data assignment. Only the three allowlisted content PDFs are permitted, each with a recorded SHA-256.
- Content: unchanged official SRD 5.1, unchanged official SRD 5.2.1, and owner-authorized EF Alpha Races. SRDs and EF: CC BY 4.0 with separate attribution. EF: Quest LLC / quest.rasht; artwork: Mopodraws. EF JPEG previews and reviewed app notes are identified as adaptations. PDF.js's optional example research PDF is excluded.
- Copyrighted commercial-book PDFs, source extracts and the third-party compatibility module are excluded. Buying/possessing a PDF or making an app free does not provide redistribution rights.
- Public code retains the repository's existing Unlicense. Content/dependency licenses remain separate.

## Build and distribution
Windows x64 installer and Android APK/AAB are built from this clean source tree. Runtime files and licensed content are bundled; Android's sole requested permission is MODIFY_AUDIO_SETTINGS, not INTERNET. Android uses the existing public-edition signing key; keys/passwords remain outside the repository and release archive. Windows binaries are not publisher-code-signed.

## Limits
Physical Android installation, native printing/share-provider acceptance and external music-player compatibility still need device tests. The open rules PDFs are references; automatic commercial-book class progression has not been relicensed. Class feature notes remain manually reviewed; Oracle uses EF alpha reminders. No claim that every possible bug is fixed, every device is supported, or a store has approved the release.

The audit covers this repository's current tree, its one reachable pre-existing commit and listed prealpha asset, plus the new selected release files. It is not an account-wide guarantee about unrelated repositories, forks or caches. A GitHub username/repository URL and the requested Quest/Mopodraws credits are intentional public identifiers.

## Later privacy correction

The original full-string scan missed reconstructable personal-marker fragments in the scanner itself. The 1.3.0 scanner now loads private values from an external unpublished configuration. Do not interpret the original scan as a guarantee of historical privacy; see CONTENT-PACK-RELEASE-AUDIT.md for the corrected scope.
