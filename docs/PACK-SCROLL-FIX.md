# Package dialog scrolling — 1.4.1

Fixed the package import and ZIP creation dialogs. The previous shared dialog style hid overflow without providing a scroll container for content-pack lists. A long list could push the action buttons outside the reachable area.

The dialog now has an independently scrolling body, persistent actions, and visible validation messages. The ZIP export form retains its inputs and submit controls inside the same form. File selection, import validation, indexing, storage and licensing behavior are unchanged.

Validation used synthetic files and a separate preview origin:

- 64 individually selected PDFs at 320 x 640: body scroll height over 10,000 px, with both buttons visible; pointer scrolling reached the final file without Tab.
- A 64-book reference ZIP at 320 x 640: scrollable list, visible Cancel/Install controls and missing-PDF validation.
- 640 x 320 landscape: content remained scrollable and action buttons stayed inside the viewport.
- ZIP creation with 64 synthetic sources: last checkbox remained reachable; Save ZIP submitted its selected ID and the form fields to a local stub. No actual test ZIP was exported or personal files used.
- Existing 112 automated tests passed.

Windows/Android packages retain their existing upgrade identities and storage locations. Version 1.4.1 uses Android version code 7 and save schema 3. Physical-device acceptance is still recommended; this report describes browser viewport testing and package/build verification.
