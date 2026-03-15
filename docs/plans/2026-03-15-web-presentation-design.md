# Web Presentation Design

**Goal:** Build a static single-page application presenting 36 merchants' letters and 46 administrative documents as a browsable collection, with modern English translations, for a general audience.

## Architecture

Static HTML/CSS/JS single-page app. No framework — the dataset (82 items) is small enough to embed both JSON files directly. Hash-based routing for deep linking (`#letter/27`, `#doc/37`).

Data sources: `letters.json` (36 records) and `documents.json` (46 records), embedded at build time via a simple Python build script that injects the JSON into the HTML.

Deployable to any static host (GitHub Pages, Netlify, Vercel).

## Visual Direction

Hybrid of prototypes A (The Archive) and C (The Folio).

- **Typography:** Libre Baskerville (display headings), Crimson Pro (body text), DM Mono (metadata labels, monospace accents)
- **Palette:** Warm sepia/parchment — `#f2ece0` base, `#3d2e1e` ink, `#8e3b2a` oxide accent, `#f8f5ee` white/card, `#d1c7b4` rules
- **Texture:** Subtle SVG noise overlay for paper grain feel
- **Decorative:** Graduated horizontal rule lines, diamond ornaments — restrained, historically evocative without being kitsch
- **Tone:** Professional enough for historians, attractive enough for a general audience arriving from social media

## Layout & Navigation

Three top-level tabs in a sticky nav bar:

1. **The Letters** (default view)
2. **The Case File** (admin documents)
3. **About**

## The Letters Tab

### Featured Letter
At the top: a highlighted card for Letter 27 (Katrijne Tehaselare's farewell). Includes a pull quote from the translation, the summary, and a "Read this letter" link. Visually distinct from the list below (border, `FEATURED` label).

### Filters
Pill-style filter bar:
- Type: All / Business / Personal / Mixed
- Language: Middle English / Middle Dutch / Low German
- Notable (toggle)

Filters are combinable (AND logic). "All" resets.

### Letter Index
List layout, one row per letter:
- Letter number (large, faded)
- Sender → recipient (heading)
- Summary (truncated to ~2 lines)
- Date + language (right-aligned metadata)
- Notable badge (small, oxide-coloured, where applicable)

Sorted by document number (1–36).

### Letter Detail Panel
Slide-in panel from right side of viewport. Triggered by clicking a row. Updates URL hash to `#letter/{id}`.

Contents (top to bottom):
1. Close button (top right)
2. Letter number (large, faded)
3. Sender → recipient heading
4. Metadata row: date, origin, language, type
5. Theme tags (small pills)
6. **Summary** — italic, serves as the hook
7. **Modern English Translation** — full text, primary content
8. AI disclaimer note (small, left-bordered)
9. **Original Transcription** — collapsed by default, toggle button to expand. Label includes the language name.
10. **Editorial Notes** — collapsed by default, if present.

### Overlay
Semi-transparent backdrop behind the panel. Click to close. Escape key to close.

## The Case File Tab

Documents grouped by section with clear section headers:
- II: Capture of the ship of Adrian Johnson
- III: English losses
- IV: Venetian losses
- V: Hanseatic/Cologne losses
- VI: Spanish losses
- VII: Further restitution

Same list layout as letters. Each row shows:
- Document number
- Title
- Summary (truncated)
- Date + document type badge (deposition, inventory, legal instrument, etc.)

Same slide-in detail panel pattern. Hash: `#doc/{id}`.

## About Tab

Static content page. Sections:
- Narrative introduction to the letters and their context (the ship seizure, who wrote them, why they survived)
- About the translations (AI-generated, not peer-reviewed, for accessibility)
- About the original publication: Jenks & Wubs-Mrozewicz, *Message in a Bottle* (2022), open-access via [Brepols](https://www.brepols.net/products/IS-9782503595405-1)
- Credits

Hash: `#about`.

## Routing

| Hash | Behaviour |
|------|-----------|
| (none) | Letters tab, no detail |
| `#letter/{id}` | Letters tab, detail panel open for that letter |
| `#doc/{id}` | Case File tab, detail panel open for that document |
| `#about` | About tab |
| `#casefile` | Case File tab, no detail |

On page load, parse hash and navigate accordingly. On hash change (back/forward), update view. Clicking a letter/document updates the hash. Closing the detail panel removes the item part of the hash.

## Data Shape

Letters (from `letters.json`):
- id, sender, recipient, date, origin, destination, language
- modern_english_translation, original_transcription (from `content` field in .md)
- summary, letter_type, themes, people_mentioned, goods_mentioned, notable
- editorial_notes, archival_reference

Documents (from `documents.json`):
- id, section, section_title, title, date, location, language
- modern_english_translation, content (original text)
- summary, document_type, themes, people_mentioned, goods_mentioned, notable, notable_reason
- editorial_notes, archival_reference

## Build Process

A Python build script (`build.py`) that:
1. Reads `letters.json` and `documents.json`
2. Injects them as JavaScript variables into an HTML template
3. Outputs a single `index.html` (plus any static assets) to a `dist/` directory

No npm, no bundler, no node_modules. Just Python + the browser.
