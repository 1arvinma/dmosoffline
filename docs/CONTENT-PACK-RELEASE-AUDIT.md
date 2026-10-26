# DMOS 1.3.0 content-pack release audit

## Public source and hosted-file recheck

Compared the source trees, commit metadata and hosted asset SHA256 values with the inspected source ZIP/APK/AAB/installer files. Commit author addresses use GitHub noreply. The earlier automated scan checked 269 text entries for complete private-marker strings and signing files, but a later manual review found that the old audit script itself held reconstructable fragments of personal markers. That was missed by the full-string scan; earlier statements must not be read as a guarantee that historical source archives contain no personal information.

The current scanner contains no personal marker values. It accepts an optional external JSON configuration through DMOS_PRIVATE_MARKERS_FILE; the configuration is kept outside the source publication tree. The final current tree and new source archive are scanned using that external configuration, including distinguishing fragments. Older release source archives and commit history require separate removal/rewrite approval; until that cleanup is complete, historical privacy is not claimed. Copies already downloaded or cached cannot be recalled.

Google Play Console for the signed-in account opens at “Creating a developer account”. There is no uploaded Play release in that account to audit. The AAB is a preparation artifact; this release does not claim Play publication.

## New public build

101 Node tests pass, covering existing campaign/import/combat/score allocation/upgrade recovery checks plus ZIP validation, SHA256 boundary cases, damaged/unsafe/undeclared/compressed content, reference metadata, version conflicts and native ZIP writer round trips. Owned-PDF loading-task cleanup is tested on both successful indexing and parser failure. The private edition also passes 79 engine/onboarding/score/save migration/Sage checks with its original update identity.

Browser checks use synthetic campaigns and PDFs on separate localhost origins. Verified ZIP preview, installed-pack persistence after reload, 1.0.0 → 1.0.1 upgrade, offline search, extracted page dialog and the original PDF viewer. Reference-only import selects and indexes a synthetic owned PDF locally, then survives reload. A browser test found and fixed PDF.js cleanup before final packaging. The redesigned music dialog was visually checked at 375 × 812. The private edition starts with an empty fresh workspace and retains 17 book sources. These checks do not install over real user data.

Public assets contain only allowlisted SRD 5.1, SRD 5.2.1 and EF Alpha Races, plus their indexes/previews. No personal campaigns, party imports, commercial-book module or signing stores are bundled. Private binaries stay local, retain their existing com.dmos.local / DMOS Local identities and supplied library, and grant no redistribution license. No commercial-PDF ZIP is published: availability elsewhere and risk labels do not provide redistribution permission.

Content packs live in a separate IndexedDB database. Import validation occurs before writes; same-pack replacement uses a single readwrite transaction. Failed validation/aborted transactions keep old content. Packs are not part of campaign JSON backups. Users must retain original ZIP/PDF files for device transfer or recovery. New app versions keep storage identities; do not uninstall Android before updating.

Native package verification includes APK signatures and signing continuity, package/version/permission inspection, public AAB validation, Windows installer archive CRC and packaged-asset equality. No Android Internet permission; only MODIFY_AUDIO_SETTINGS. The Windows installer remains unsigned. Physical Android/Windows install-over-existing, real file-provider limits and third-party player media behavior still require device acceptance, so 1.3.0 remains a prerelease.

## Sage picker and direct PDF import

Fixed the missing SRD 5.2.1 species catalog and the obsolete “no 2024 book supplied” notice. Sage now groups the nine SRD species first, preserves explicit legacy source selections and provides revised source/level-aware ancestry notes. Player forms use distinct source-bearing choice IDs. Browser checked the Sage picker and direct PDF selection; Books & rules now exposes Add PDF books beside Content packs.

## Shared upgrade files

- Quest open-library ZIP: three licensed PDFs, indexes and catalog; Quest LLC / quest.rasht and Mopodraws credits preserved.
- Owned-books reference ZIP: bibliography, page counts and hashes for 14 sources; no PDF, book prose, artwork, campaign, local path or signing data. Each player supplies their own copies.
- Neither package includes user saves or an entitlement bypass.

