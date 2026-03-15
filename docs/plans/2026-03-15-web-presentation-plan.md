# Web Presentation Implementation Plan

> **For Claude:** REQUIRED SUB-SKILL: Use superpowers:executing-plans to implement this plan task-by-task.

**Goal:** Build a static single-page app presenting 36 merchants' letters and 46 admin documents with modern English translations, filterable and deep-linkable.

**Architecture:** Single HTML file with embedded CSS/JS and baked-in JSON data. A Python build script reads `letters.json` and `documents.json`, injects them into an HTML template, and outputs `dist/index.html`. Hash-based routing for deep links (`#letter/27`, `#doc/37`).

**Tech Stack:** Vanilla HTML/CSS/JS (no framework), Python build script, Google Fonts (Libre Baskerville, Crimson Pro, DM Mono)

---

### Task 1: Build Script and HTML Shell

**Files:**
- Create: `build.py`
- Create: `site/template.html`
- Create: `dist/` (output directory)

**Step 1: Create the build script**

```python
# build.py
"""Build the static site by injecting JSON data into the HTML template."""

import json
from pathlib import Path

def build():
    letters = json.loads(Path("letters.json").read_text(encoding="utf-8"))
    documents = json.loads(Path("documents.json").read_text(encoding="utf-8"))

    template = Path("site/template.html").read_text(encoding="utf-8")

    # Inject data as JS variables
    letters_js = json.dumps(letters, ensure_ascii=False)
    documents_js = json.dumps(documents, ensure_ascii=False)

    html = template.replace(
        "/* __LETTERS_DATA__ */",
        f"const LETTERS = {letters_js};"
    ).replace(
        "/* __DOCUMENTS_DATA__ */",
        f"const DOCUMENTS = {documents_js};"
    )

    dist = Path("dist")
    dist.mkdir(exist_ok=True)
    (dist / "index.html").write_text(html, encoding="utf-8")
    print(f"Built dist/index.html ({len(html):,} bytes)")
    print(f"  {len(letters)} letters, {len(documents)} documents embedded")

if __name__ == "__main__":
    build()
```

**Step 2: Create the HTML template shell**

Create `site/template.html` with:
- DOCTYPE, meta viewport, charset
- Google Fonts link (Libre Baskerville, Crimson Pro, DM Mono)
- Empty `<style>` block (populated in Task 2)
- `<script>` block with data injection placeholders:
  ```html
  <script>
  /* __LETTERS_DATA__ */
  /* __DOCUMENTS_DATA__ */
  </script>
  ```
- Basic page structure:
  ```html
  <header id="site-header"></header>
  <nav class="tabs" id="site-nav"></nav>
  <main id="main-content"></main>
  <div class="detail-overlay" id="detail-overlay"></div>
  <footer id="site-footer"></footer>
  ```

**Step 3: Run the build and verify**

Run: `uv run python build.py`
Expected: `dist/index.html` created, console reports letter/document counts.

Run: `open dist/index.html`
Expected: Blank page loads without errors in browser console.

**Step 4: Commit**

```bash
git add build.py site/template.html
git commit -m "feat: add build script and HTML template shell"
```

---

### Task 2: CSS — Full Styling

**Files:**
- Modify: `site/template.html` (add all CSS into the `<style>` block)

Implement the complete CSS based on the hybrid A+C design. This is a large block — do it all at once since there's nothing to test incrementally.

**CSS variables (root):**

```css
:root {
  --parchment: #f2ece0;
  --parchment-warm: #ede5d5;
  --sepia: #3d2e1e;
  --sepia-mid: #5e4a35;
  --sepia-light: #8b7a66;
  --sepia-faint: #b3a792;
  --oxide: #8e3b2a;
  --oxide-light: #a85040;
  --oxide-faint: rgba(142, 59, 42, 0.12);
  --white: #f8f5ee;
  --rule: #d1c7b4;
  --rule-light: #ddd5c4;
  --shadow: rgba(61, 46, 30, 0.06);
}
```

**Required CSS sections:**
1. Reset and base (`body`, fonts, paper texture `::before` overlay)
2. Header (ornament, title, subtitle, description)
3. Sticky nav tabs
4. Featured letter card
5. Filter pills
6. Letter list rows (number, sender→recipient, summary, date, language, notable badge)
7. Document list rows (number, title, summary, date, type badge)
8. Section headers for Case File grouping
9. Detail overlay + slide-in panel (right side, 720px max, with animation)
10. Detail panel contents (header, meta row, theme tags, summary, translation text, AI note, collapsible original, collapsible editorial notes)
11. About page content styling
12. Footer
13. Animations (staggered fade-in for list rows, slide-in for detail panel)
14. Responsive: at `max-width: 640px`, detail panel goes full width, metadata stacks vertically

Use the prototype files as reference:
- `prototypes/option_a_archive.html` for list layout and slide-in panel
- `prototypes/option_c_folio.html` for typography, colours, featured card, and decorative elements

**Step 1: Add all CSS to template**

Write the full CSS into the `<style>` block in `site/template.html`.

**Step 2: Rebuild and verify**

Run: `uv run python build.py && open dist/index.html`
Expected: Page has correct background colour, fonts load (check network tab).

**Step 3: Commit**

```bash
git add site/template.html
git commit -m "feat: add complete CSS styling"
```

---

### Task 3: JavaScript — Routing and Tab Navigation

**Files:**
- Modify: `site/template.html` (add JS after the data injection block)

**Step 1: Implement the router and tab switching**

Add a `<script>` block after the data block. Implement:

```javascript
// State
let currentTab = 'letters';  // 'letters' | 'casefile' | 'about'
let currentDetail = null;     // { type: 'letter'|'doc', id: number } or null
let filters = { type: 'all', language: 'all', notable: false };

// Router
function parseHash() {
  const hash = location.hash.slice(1);
  if (hash.startsWith('letter/')) {
    return { tab: 'letters', detail: { type: 'letter', id: parseInt(hash.split('/')[1]) } };
  }
  if (hash.startsWith('doc/')) {
    return { tab: 'casefile', detail: { type: 'doc', id: parseInt(hash.split('/')[1]) } };
  }
  if (hash === 'about') return { tab: 'about', detail: null };
  if (hash === 'casefile') return { tab: 'casefile', detail: null };
  return { tab: 'letters', detail: null };
}

function navigate(tab, detail) {
  currentTab = tab;
  currentDetail = detail;
  if (detail) {
    location.hash = `${detail.type === 'letter' ? 'letter' : 'doc'}/${detail.id}`;
  } else if (tab === 'about') {
    location.hash = 'about';
  } else if (tab === 'casefile') {
    location.hash = 'casefile';
  } else {
    history.replaceState(null, '', location.pathname);
  }
  render();
}

window.addEventListener('hashchange', () => {
  const state = parseHash();
  currentTab = state.tab;
  currentDetail = state.detail;
  render();
});

// Initial load
const initialState = parseHash();
currentTab = initialState.tab;
currentDetail = initialState.detail;
```

Also implement `renderNav()` which creates the three tab buttons in `#site-nav`, with click handlers calling `navigate()`, and highlights the active tab.

**Step 2: Add a minimal render() stub**

```javascript
function render() {
  renderNav();
  renderHeader();
  const main = document.getElementById('main-content');
  main.innerHTML = `<p style="padding:2rem;color:var(--sepia-light)">Tab: ${currentTab}</p>`;
  // Detail panel placeholder
  const overlay = document.getElementById('detail-overlay');
  overlay.className = currentDetail ? 'detail-overlay open' : 'detail-overlay';
  overlay.innerHTML = currentDetail
    ? `<div class="detail-panel"><p>Detail: ${currentDetail.type} ${currentDetail.id}</p></div>`
    : '';
}
```

**Step 3: Rebuild and test**

Run: `uv run python build.py && open dist/index.html`

Test:
- Clicking tabs switches the displayed tab name
- Navigating to `dist/index.html#letter/27` shows "Detail: letter 27"
- Navigating to `dist/index.html#about` shows "Tab: about"
- Back button works

**Step 4: Commit**

```bash
git add site/template.html
git commit -m "feat: add routing and tab navigation"
```

---

### Task 4: JavaScript — Header, Footer, About Page

**Files:**
- Modify: `site/template.html`

**Step 1: Implement renderHeader()**

Renders into `#site-header`:
- Diamond ornament div
- `<h1>Message in a Bottle</h1>`
- Subtitle: "Merchants' Letters from the English Channel, 1533"
- Description paragraph about the letters

Also implement `renderFooter()` into `#site-footer`:
- Credit line with link to Brepols publication: `https://www.brepols.net/products/IS-9782503595405-1`
- AI translation disclaimer

**Step 2: Implement renderAbout()**

Renders into `#main-content` when `currentTab === 'about'`. Static HTML content:
- **The Story** — 2-3 paragraphs about the ship seizure, what the letters are, why they matter
- **About the Translations** — AI-generated disclaimer, methodology
- **The Original Publication** — Credit to Jenks & Wubs-Mrozewicz (2022), link to Brepols
- **This Digital Edition** — Brief note on the project

**Step 3: Wire into render()**

Update `render()` to call `renderAbout()` when on the about tab.

**Step 4: Rebuild and test**

Run: `uv run python build.py && open dist/index.html#about`
Expected: About page renders with all sections, link to Brepols works.

**Step 5: Commit**

```bash
git add site/template.html
git commit -m "feat: add header, footer, and about page"
```

---

### Task 5: JavaScript — Letters Index (List + Filters + Featured)

**Files:**
- Modify: `site/template.html`

**Step 1: Implement renderLetters()**

Renders into `#main-content` when `currentTab === 'letters'`. Structure:

1. **Featured card** — Letter 27 (find by id in LETTERS array):
   - Sender line, meta line (origin, date, language)
   - Pull quote (hardcoded excerpt from translation: "I, Kathryna your mother, have a great desire to see you once more with my own living eyes...")
   - Summary text
   - "Read this letter →" link that calls `navigate('letters', {type:'letter', id:27})`

2. **Section divider** with "All Letters" heading

3. **Filter bar** — render pills for:
   - Type: All, Business, Personal, Mixed
   - Language: Middle English, Middle Dutch, Low German
   - Notable toggle

   Each pill click updates the `filters` state and re-renders the list.

4. **Letter list** — for each letter matching current filters:
   ```javascript
   function matchesFilters(letter) {
     if (filters.type !== 'all' && letter.letter_type !== filters.type) return false;
     if (filters.language !== 'all' && letter.language !== filters.language) return false;
     if (filters.notable && !letter.notable) return false;
     return true;
   }
   ```

   Each row renders: number, sender → recipient heading, summary (truncated to 160 chars), date, language, notable badge. Click handler: `navigate('letters', {type:'letter', id: letter.id})`.

**Step 2: Rebuild and test**

Run: `uv run python build.py && open dist/index.html`

Test:
- Featured card appears with Letter 27 content
- All 36 letters listed below
- Clicking "Business" filter shows only business letters
- Clicking "Middle Dutch" shows only Middle Dutch letters
- Clicking "Notable" shows only notable letters
- Clicking a letter row opens the detail overlay (still placeholder)
- Filter combinations work (e.g. Business + Middle English)

**Step 3: Commit**

```bash
git add site/template.html
git commit -m "feat: add letters index with filters and featured card"
```

---

### Task 6: JavaScript — Case File Index

**Files:**
- Modify: `site/template.html`

**Step 1: Implement renderCaseFile()**

Renders into `#main-content` when `currentTab === 'casefile'`. Structure:

1. **Introduction paragraph** — brief context about the admin documents (depositions, inventories, quitclaims) that tell the legal aftermath of the seizure.

2. **Documents grouped by section** — iterate over sections in order (II, III, IV, V, VI, VII):
   ```javascript
   const SECTION_ORDER = ['II', 'III', 'IV', 'V', 'VI', 'VII'];
   ```

   For each section: render a section header with the section title, then list all documents in that section.

3. **Document rows** — similar to letter rows but with:
   - Document number
   - Title (from `doc.title`)
   - Summary (truncated)
   - Date + document type badge (styled differently per type — use the `document_type` field)

   Click handler: `navigate('casefile', {type:'doc', id: doc.id})`

**Step 2: Rebuild and test**

Run: `uv run python build.py && open dist/index.html#casefile`

Test:
- Documents grouped under section headers
- All 46 documents listed
- Section headers show correct titles
- Clicking a document opens the detail overlay (still placeholder)

**Step 3: Commit**

```bash
git add site/template.html
git commit -m "feat: add case file index grouped by section"
```

---

### Task 7: JavaScript — Detail Panel

**Files:**
- Modify: `site/template.html`

This is the most complex component. It handles both letters and documents.

**Step 1: Implement renderDetail()**

Called from `render()` when `currentDetail` is set. Renders into `#detail-overlay`.

```javascript
function renderDetail() {
  const overlay = document.getElementById('detail-overlay');
  if (!currentDetail) {
    overlay.className = 'detail-overlay';
    overlay.innerHTML = '';
    document.body.style.overflow = '';
    return;
  }

  const isLetter = currentDetail.type === 'letter';
  const item = isLetter
    ? LETTERS.find(l => l.id === currentDetail.id)
    : DOCUMENTS.find(d => d.id === currentDetail.id);

  if (!item) {
    overlay.className = 'detail-overlay';
    overlay.innerHTML = '';
    return;
  }

  document.body.style.overflow = 'hidden';
  overlay.className = 'detail-overlay open';
  // ... build HTML
}
```

**Panel HTML structure for letters:**
- Close button (click → `navigate(currentTab, null)`)
- Number (large, faded)
- `${letter.sender} to ${letter.recipient}` heading
- Meta row: date, origin, language, type (letter_type)
- Theme tags from `letter.themes` array
- Summary section (italic)
- Translation section: `letter.modern_english_translation` — split on `\n\n` into `<p>` tags
- AI disclaimer note
- Toggle button "Show original transcription ({language})" — click reveals collapsible div
- Original: `letter.original_transcription` — split into paragraphs
- If `letter.editorial_notes` is non-empty: toggle button for editorial notes, collapsible div

**Panel HTML structure for documents:**
- Same pattern but uses: `doc.title` for heading, `doc.location` for origin, `doc.document_type` for type, `doc.content` for original text, `doc.notable_reason` shown if notable

**Step 2: Wire overlay close behaviour**

- Click on overlay backdrop → close
- Escape key → close
- Close button → close
- All call `navigate(currentTab, null)`

**Step 3: Wire toggle buttons**

Use event delegation on the panel:
```javascript
panel.addEventListener('click', (e) => {
  const toggle = e.target.closest('.toggle-btn');
  if (toggle) {
    const target = document.getElementById(toggle.dataset.target);
    target.classList.toggle('open');
    // Update button text
  }
});
```

**Step 4: Rebuild and test**

Run: `uv run python build.py && open dist/index.html#letter/27`

Test:
- Detail panel slides in from right with Letter 27 content
- Summary, translation, metadata all render correctly
- "Show original transcription" toggle works
- Clicking backdrop or pressing Escape closes the panel
- URL updates when opening/closing
- Test a document: `#doc/40` — the schedule of English losses
- Back button navigates between detail states
- Opening `#letter/999` (invalid) shows no panel

**Step 5: Commit**

```bash
git add site/template.html
git commit -m "feat: add detail panel for letters and documents"
```

---

### Task 8: Polish and Responsive

**Files:**
- Modify: `site/template.html`

**Step 1: Scroll-to-active behaviour**

When navigating to a letter/doc via hash on page load, scroll the corresponding row into view after rendering:
```javascript
function scrollToActive() {
  if (!currentDetail) return;
  const selector = `[data-id="${currentDetail.type}-${currentDetail.id}"]`;
  const el = document.querySelector(selector);
  if (el) el.scrollIntoView({ behavior: 'smooth', block: 'center' });
}
```

**Step 2: Responsive adjustments**

Add media query `@media (max-width: 640px)`:
- Detail panel: `width: 100vw` instead of `min(720px, 90vw)`
- Letter row meta: stack vertically
- Featured card: reduce padding
- Header: smaller title font size
- Filter pills: smaller text, wrap freely

**Step 3: Empty state for filters**

When no letters match current filters, show: "No letters match the current filters."

**Step 4: Staggered row animations**

Apply animation delays to list rows using inline styles during render:
```javascript
rows.forEach((row, i) => {
  row.style.animationDelay = `${0.03 * i}s`;
});
```

**Step 5: Rebuild and test**

Run: `uv run python build.py && open dist/index.html`

Test:
- Resize browser to mobile width — layout adapts
- Filter to impossible combination — empty state shows
- Open page at `#letter/15` — row scrolls into view
- Row animations stagger nicely on tab switch

**Step 6: Commit**

```bash
git add site/template.html
git commit -m "feat: responsive layout, scroll-to-active, empty state, animations"
```

---

### Task 9: Final Build and Verification

**Files:**
- No new files

**Step 1: Full rebuild**

Run: `uv run python build.py`
Expected: `dist/index.html` created, size reported.

**Step 2: End-to-end test checklist**

Open `dist/index.html` in browser. Verify:

- [ ] Header renders with correct title, subtitle, ornaments
- [ ] Three tabs work: Letters, Case File, About
- [ ] Featured letter (27) shows with pull quote
- [ ] All 36 letters listed with correct data
- [ ] Filters work: Business, Personal, Mixed, each language, Notable
- [ ] Clicking letter opens detail panel with slide-in animation
- [ ] Detail panel shows: summary, full translation, metadata, themes
- [ ] AI disclaimer visible in detail panel
- [ ] "Show original transcription" toggle works
- [ ] Editorial notes toggle works (for letters that have them)
- [ ] Closing panel (click backdrop / Escape / X button) works
- [ ] Case File tab shows 46 documents grouped by 6 sections
- [ ] Document detail panel works
- [ ] About page renders with Brepols link
- [ ] Deep link `#letter/27` opens directly to Letter 27
- [ ] Deep link `#doc/40` opens directly to Doc 40
- [ ] `#about` opens About tab
- [ ] Back/forward browser navigation works
- [ ] Mobile responsive (resize to 375px width)
- [ ] No console errors

**Step 3: Commit**

```bash
git add dist/index.html
git commit -m "feat: build final dist/index.html"
```
