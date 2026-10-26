# Session Board (1.4.0)

Open Session Board in the active campaign navigation. Add scenes, encounters, locations, or story beats with a title, description, and private GM notes. Link party characters, Encounter entries in Library, current combat, and book PDF pages. Missing links remain visible and can be removed in Edit.

Drag cards into Prepare, Ready, or Played, or use Move and organize: Move to, up/down, Duplicate, and Delete. On phones, column buttons show counts and one column at a time. Moving or saving a card selects its destination column. Card titles open details in a dialog; keyboard and touch users can use every action without dragging.

Run scene marks one card active and opens its notes and linked encounter notes. A current-combat link shows the live roster and can open the combat tracker. Running does not reset initiative, replace combatants, change rounds, or change the scene's column. Played is always manual. End active scene only clears the active marker.

Boards live inside campaign data. Local saves, rotating snapshots, campaign exports, full workspace backups, and restores include every card and the active scene. Campaign imports create independent copies and remap character, Library, and scene IDs; full restores preserve IDs. PDFs stay in the existing separate content-pack store and are not embedded in campaign backups.

Version 1.4 uses save schema 3; older applications reject its exports rather than silently discard board data. The normal recovery snapshot is kept during migration. Export a full backup before upgrades. A stale browser window cannot overwrite a workspace saved by another window; export its unsaved work and reload to review the newer save.

## File drops

- PDFs, including multiple PDFs together: drop anywhere, inspect the book list, then install locally.
- One DMOS content ZIP: drop anywhere and inspect its manifest before installation.
- Player or old party JSON: drop on Party to preview adding characters to that campaign.
- Campaign or workspace JSON: drop on Overview or Settings to preview importing new campaign copies. Full replacement remains the separate Restore full backup action.

Mixed file types are rejected. Finish an open dialog before dropping more files. File pickers remain available for touch devices that do not provide desktop file dragging. General ZIP files must be extracted first; the content ZIP parser retains its strict existing DMOS format and limits.

## Device music

The persistent music strip provides previous, play/pause, next, and full controls. Windows offers a native system-style menu; Android offers native buttons plus the actual device music-stream volume slider. Start playback in the other music app first. DMOS does not read its library, track name, or playback progress. Player support varies. No new dependencies or permissions were added.
