# Upgrade release audit — DMOS Table 1.2.1

- 83 automated checks pass, including 1.2.0-to-1.2.1 save migration, stable IDs and live combat references, preference preservation, full restore/export, future-version protection, quota failures, cancelled backups and fixed trusted release links.
- The upgrade fixture is synthetic and was generated with the previous 1.2.0 engine. It contains no real campaign data. Browser testing restored it through the normal file picker, verified that the current workspace downloaded first, then reloaded and confirmed round 3 / Example Opponent and the saved dice preferences.
- App version, Android version code and save schema are centralized in release.json. Version synchronization and release validation check stable application identities and monotonic release metadata.
- Windows keeps the same installer AppId, DMOS Table profile, local origin and persistent partition. Installer reuse/downgrade checks compile. Android keeps com.dmos.table and the existing public APK signing certificate; version code increases from 3 to 4. APK signatures and AAB structure are verified.
- Privacy/content scanning still excludes personal campaigns, private contacts, device paths and signing material. Exactly three licensed PDFs remain: SRD 5.1, SRD 5.2.1, EF Alpha Races. Quest LLC / quest.rasht and Mopodraws attribution and separate content/software licenses are retained.
- No background network updater was added. Only a deliberate click opens a fixed GitHub URL in the system browser. Renderer-controlled URLs and remote-frame requests are rejected on Windows; Android has no INTERNET permission.

Limits: actual installer-over-existing and Android device installation/printing/media-player acceptance still require physical device testing. The installer archive/build, signature identity and migration logic are verified; these are not claims of OS installation testing. The already published 1.2.0 installer cannot be retroactively given downgrade protection. Keep an external workspace backup before installation and do not uninstall Android first.

Browser-only backup flows require explicit confirmation that the download finished before unlocking or replacing saves. Native Android export completion is reported only after stream close/flush; invalid or cancelled picker results resolve as cancelled.
