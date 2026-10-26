# Upgrading DMOS Table

## Windows
Export a **full workspace** in Updates & recovery, close DMOS and run the newer Windows installer over the existing installation. Do not delete the local profile. The stable installer AppId is retained and the installer reuses the previous location, shortcuts and tasks. Campaign data lives in the existing DMOS Table user profile, outside installed app files. Uninstall retains that profile.

New installers compare the installed DisplayVersion and reject a downgrade. This cannot change the already published 1.2.0 installer's behavior: avoid using that old installer to overwrite a newer version.

## Android
Install the newer APK **over** the existing DMOS Table app. Do not uninstall first or clear app data. The package remains `com.dmos.table`; release version codes must increase and release APKs must keep the existing public-edition signing certificate. The OS checks that identity. A differently signed APK is not an in-place update.

Private DMOS Local is a separate package/profile. Export/import to move between editions; updating DMOS Table cannot automatically read private-edition storage.

## Save protection
On first launch after an upgrade, the exact original workspace is copied to a separate local pre-upgrade recovery slot before migration. Record IDs, live combat references, preferences and active campaign are preserved. If the recovery copy cannot fit, editing pauses until the original is exported successfully. Cancelling that native export keeps the original locked and unchanged. Browser-only flows also require confirmation that the backup download finished before editing or replacement proceeds.

Updates & recovery can download that recovery slot. Full workspace exports now include preferences, active campaign and save/app version metadata. **Restore full backup** replaces the workspace only after an explicit confirmation and a successful export of the current save. Normal campaign Import still adds copies instead of replacing preferences. Exports made before 1.2.1 may lack preferences; the original on-device workspace and pre-upgrade copy preserve them when available.

Unsupported/newer saves stay protected; they are not silently reset or overwritten. Install the matching newer app, download the untouched original, or explicitly restore a supported backup. Browser storage can still be cleared by the user/OS: keep external backups. Pre-upgrade copies and exports contain private campaign data and must never be attached to public releases.

## Offline updates
There is no background updater or automatic download/installation. The release button opens the project's fixed GitHub releases page in the device browser; the app itself remains offline. Download the matching installer/APK and verify published SHA-256 checksums. This also works with files transferred by USB.

## Maintainer checklist
1. Edit `release.json`: increment app version and Android version code; increment schemaVersion for incompatible data changes. Keep Windows AppId/profile and Android package fixed.
2. Run `node scripts/sync-version.cjs` (also run automatically by assemble/build). Version scripts, native metadata and installer version derive from that file.
3. Run `node --test tests/*.test.cjs` and the privacy/content audit. Keep synthetic fixtures only. Test from the previous public version's saved workspace, including a live combat turn, notes, preferences, quota failure and cancelled backup.
4. Build with the existing signing key kept outside the repository. Never publish keys, passwords or local profiles. Keep private key backups offline.
5. Test install-over-existing on actual Windows/Android devices, including same-signature identity and launch-after-update. Automated tests do not replace those OS acceptance checks.
6. Build the full source ZIP with `python scripts/package-source.py`, then publish only the new version's files and SHA256SUMS.txt. Do not publish private directories or recovery data.
7. For rollback, use a separate profile and a pre-upgrade backup. Do not point older binaries at a live newer save.

### Google Play signing continuity
If Play App Signing is enrolled later, choose a signing strategy that preserves the existing public APK certificate for in-place updates. A Google-signed build using a different app-signing key will not normally install over these directly distributed APKs. The local file named as an upload key is also the signer of current direct APKs; do not replace that identity casually. Resolve this in Play Console before public rollout. Never publish the keystore or its password.
