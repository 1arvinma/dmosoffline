# Offline content packs

For a single owned PDF, use **Books & rules → Add PDF books**, choose it, review, then install. Its text is indexed locally; this does not automatically create class/species rules. Reimporting the same filename replaces that local source after confirmation.

For prepared packs, use **Content packs → Import content ZIP**, review the name, version and credits, then install. Reference-only packs ask each player to choose their own legally obtained PDFs; indexing happens locally. This enables source reading and search, without distributing the books. A reference pack does not supply commercial character automation or a book license.

Packs stay in IndexedDB in the current app profile. Install app updates over the same edition without uninstalling or clearing data. Windows public/private profiles and Android packages are separate. Campaign exports do not contain pack files: keep your original ZIP/PDFs for transfer or recovery. No pack makes background network requests.

To update content, use the same pack ID and book IDs with a higher `contentVersion` (for example 1.0.1). Same-version reinstallation repairs missing files. Downgrades and book IDs owned by another installed pack are rejected. The previous pack remains until the new files and metadata commit in one transaction. A failed validation or aborted transaction keeps it. Removal affects the installed copy only; built-in sources reappear and campaign data remains. Enable new sources under Books & rules if the campaign has an explicit source selection.

Windows builds also have **Create a player ZIP**. Reference-only export contains bibliographic metadata, file hashes and page counts; no PDF, prose, artwork, campaign data, device path or signing key. Embedded export is for content you can legally redistribute. Commercial embedding requires a permission attestation and a license note. An “at your own risk” label does not provide redistribution rights.

The public Quest pack contains only SRD 5.1, SRD 5.2.1 and EF Alpha Races. EF Alpha is original work in progress by **Quest LLC / quest.rasht**, with artwork by **Mopodraws**, under CC BY 4.0. Preserve all attribution. Commercial PDFs stay out of public releases.

For repeatable exports, run `node scripts/create-content-pack.cjs REQUEST.json OUTPUT.zip`. Example request:

```json
{"id":"quest-open-library","name":"Quest open library","contentVersion":"1.0.0","mode":"embedded","bookIds":["book-srd-51","book-srd-521","book-oracle-alpha"]}
```

The ZIP format uses ZIP_STORED, not compressed entries. It contains `manifest.json`, declared `books/*.pdf`, `indexes/*.json` and optional `catalog.json`. Reference entries set `external:true`. The importer validates paths, declared files, bounded sizes, CRC and PDF SHA256. It treats catalog data as data, never scripts. Imported text is escaped in the UI. Limits: 2 GB total, 256 MB per PDF, 64 books, 3000 pages per book. Large PDF indexing needs free device memory/storage. Keep enough space for the old and new pack during an update.

No encryption or licensing enforcement is implied. Players are responsible for having the right to use supplied material. Only distribute content under an applicable license or permission.

## Sage species

Sage lists the nine species available in SRD 5.2.1 (Dragonborn, Dwarf, Elf, Gnome, Goliath, Halfling, Human, Orc and Tiefling) before separately labeled legacy choices. Character and player-form choices retain their source. Revised species reminders link to SRD 5.2.1 pages 84–86, with level-gated features at the correct levels. Aasimar is not in this SRD catalog; custom ancestry remains available. Class progression notes remain explicitly labeled with their existing 2014 sources; choosing Sage does not silently rewrite a character build.
