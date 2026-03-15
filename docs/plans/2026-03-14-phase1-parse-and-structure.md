# Phase 1: Parse & Structure Implementation Plan

> **For Claude:** REQUIRED SUB-SKILL: Use superpowers:executing-plans to implement this plan task-by-task.

**Goal:** Parse hanseatic_letters.md into structured JSON + individual .md files for all documents (36 letters + 46 admin documents) and contextual front matter.

**Architecture:** Single Python script (`parse.py`) that reads the markdown, splits it into sections, extracts metadata via regex, and writes out: (1) individual .md files with YAML frontmatter under `/catalogued/`, (2) `letters.json` for the 36 merchants' letters, (3) `documents.json` for the admin documents [37]–[82], (4) `catalogued/context.md` for front matter/introductions.

**Tech Stack:** Python 3, `re`, `json`, `pathlib`. No external dependencies.

---

### Task 1: Write the context extractor

**Files:**
- Create: `parse.py`

**Step 1: Write `parse.py` that extracts context (everything before Section I)**

The context runs from line 1 up to the line before `I: Merchants' letters (1533)` (line 5163 in the markdown). This includes: foreword, three introductions, diplomatic notes, bibliography, appendices.

```python
"""Phase 1: Parse hanseatic_letters.md into structured data + individual .md files."""

import re
import json
from pathlib import Path

CATALOGUED = Path("catalogued")
CATALOGUED.mkdir(exist_ok=True)

with open("hanseatic_letters.md", "r", encoding="utf-8") as f:
    full_text = f.read()

lines = full_text.split("\n")

# --- Noise filtering ---
# Remove orphan page numbers (bare numbers on their own line)
# Remove broken section headers like "i:  mercha nt s'  letters  (1533)"
# Remove "source  edi tion" artifacts
NOISE_PATTERNS = [
    re.compile(r"^\d{1,3}$"),                         # bare page numbers
    re.compile(r"^[ivx]+:.*[a-z]\s+[a-z]", re.I),    # broken spaced-out headers
    re.compile(r"^source\s+edi\s*tion", re.I),        # "source  edi tion"
    re.compile(r"^a\s*ppe\s*ndi\s*x", re.I),          # "a ppe ndi x"
]

def is_noise(line: str) -> bool:
    stripped = line.strip()
    if not stripped:
        return False
    return any(p.match(stripped) for p in NOISE_PATTERNS)

def clean_lines(text_lines: list[str]) -> str:
    """Remove noise lines and collapse excessive blank lines."""
    cleaned = [l for l in text_lines if not is_noise(l)]
    # Collapse runs of 3+ blank lines into 2
    result = []
    blank_count = 0
    for line in cleaned:
        if line.strip() == "":
            blank_count += 1
            if blank_count <= 2:
                result.append(line)
        else:
            blank_count = 0
            result.append(line)
    return "\n".join(result)
```

**Step 2: Find section boundaries and write context.md**

```python
# --- Find section boundaries ---
# Section I starts at "I: Merchants' letters (1533)"
section_i_line = None
for i, line in enumerate(lines):
    if line.strip() == "I: Merchants' letters (1533)":
        section_i_line = i
        break

assert section_i_line is not None, "Could not find Section I header"

# Context = everything before Section I
context_lines = lines[:section_i_line]
context_text = clean_lines(context_lines)

(CATALOGUED / "context.md").write_text(
    "---\ntitle: \"Message in a Bottle — Context & Introductions\"\n"
    "description: \"Front matter, scholarly introductions, diplomatic notes, "
    "bibliography, and appendices\"\n---\n\n" + context_text,
    encoding="utf-8",
)
print(f"Wrote catalogued/context.md ({len(context_text)} chars)")
```

**Step 3: Run and verify context.md was created**

Run: `uv run python parse.py`
Expected: prints char count, file exists at catalogued/context.md

---

### Task 2: Parse the 36 merchants' letters (Section I)

**Files:**
- Modify: `parse.py`

**Step 1: Add letter parsing logic**

Section I runs from `[1.]` (line ~5165) to just before `II: Capture of the ship of Adrian` (line ~7014). Letters are numbered [1.]–[36.]. Each letter has:

- Header: `[N.] Sender to Recipient. — Date. Location.` (sometimes split: number on one line, metadata on next)
- Archival reference starting with `HL AHL`
- Body text
- `[signed]` marker (most letters)
- Editorial notes (lettered a, b, c... footnotes at end)

Key regex for header: `^\[(\d+)\.\]\s*(.*)$`

For split headers (where `[N.]` is alone on a line), join with next non-blank line.

Metadata regex for the joined header line:
`^(.+?)\s+(?:in\s+\w+\s+)?to\s+(.+?)\.\s*—\s*(.+?)\.\s*(.+?)\.?$`

This is tricky due to variations. Fall back to storing the full header as `description` if regex doesn't match, and manually fix edge cases.

**Language assignment** — hardcode based on document numbers:
- Middle Dutch: 8, 10, 11, 12, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29
- Low German: 14, 15, 16, 17, 18, 19, 30, 31, 32, 36
- Latin: (none among the 36 letters)
- Middle English: all others (1, 2, 3, 4, 5, 6, 7, 9, 13, 33, 34, 35)

These will be verified by inspecting the actual content during implementation and adjusted as needed.

```python
# --- Parse Section I: Letters [1]-[36] ---

SECTION_HEADERS = {
    "II": re.compile(r"^II:\s*Capture", re.I),
    "III": re.compile(r"^III:\s*Losses", re.I),
    "IV": re.compile(r"^IV:\s*Goods taken from Venetian", re.I),
    "V": re.compile(r"^V:\s*Hanseatic losses", re.I),
    "VI": re.compile(r"^VI:\s*Goods taken in Spanish", re.I),
    "VII": re.compile(r"^VII:\s*Goods taken from ships", re.I),
}

DOC_START = re.compile(r"^\[(\d+)\.\]\s*(.*)")

def find_section_end(start_idx: int) -> int:
    """Find the line where the next section header appears after start_idx."""
    for i in range(start_idx + 1, len(lines)):
        for pat in SECTION_HEADERS.values():
            if pat.match(lines[i].strip()):
                return i
    return len(lines)

# Extract Section I range
section_i_end = find_section_end(section_i_line)

def parse_documents(start: int, end: int, expected_range=None):
    """Parse numbered documents [N.] from a line range. Returns list of dicts."""
    docs = []
    current_num = None
    current_start = None

    for i in range(start, end):
        m = DOC_START.match(lines[i])
        if m:
            num = int(m.group(1))
            # Only treat as new document if it's in expected range or sequential
            if expected_range and num not in expected_range:
                continue
            if current_num is not None:
                docs.append((current_num, current_start, i))
            current_num = num
            current_start = i
    if current_num is not None:
        docs.append((current_num, current_start, end))

    return docs

# Parse letters [1]-[36]
letter_ranges = parse_documents(section_i_line, section_i_end, expected_range=range(1, 37))
```

**Step 2: Extract metadata from each letter's header**

```python
HEADER_RE = re.compile(
    r"^(.+?)\s+(?:in\s+.+?\s+)?to\s+(.+?)\.\s*—\s*(.+?)\.(?:\s+(.+?))?\.?\s*$"
)

# Language map (verified against document content)
LANG_MAP = {
    # Will be populated during implementation after reading each letter
}

def parse_letter_header(num: int, start: int, end: int):
    """Extract metadata from letter header lines."""
    first_line = lines[start]
    m = DOC_START.match(first_line)
    header_text = m.group(2).strip() if m else ""

    # If header is on same line as [N.], use it; otherwise join next lines
    if not header_text:
        for j in range(start + 1, min(start + 5, end)):
            if lines[j].strip():
                header_text = lines[j].strip()
                # Check if it continues to next line (date/location wrap)
                if "—" not in header_text and j + 1 < end:
                    header_text += " " + lines[j + 1].strip()
                break

    return header_text

def extract_body(start: int, end: int) -> tuple[str, str]:
    """Split document text into transcription body and editorial notes."""
    doc_lines = lines[start:end]
    # Find where body starts (after archival reference)
    # Find where editorial notes start (lettered footnotes at end)
    # Return (body, notes)
    ...
```

**Step 3: Build JSON records and write .md files**

For each letter, write:
- `catalogued/letter_NN.md` with YAML frontmatter + transcription
- Append record to `letters.json`

```python
letters = []
for num, start, end in letter_ranges:
    header = parse_letter_header(num, start, end)
    body, notes = extract_body(start, end)

    record = {
        "id": num,
        "sender": ...,
        "recipient": ...,
        "date": ...,
        "origin": ...,
        "destination": ...,
        "language": ...,
        "original_transcription": body,
        "editorial_notes": notes,
        "file": f"catalogued/letter_{num:02d}.md",
    }
    letters.append(record)

    # Write .md file
    md_content = f"""---
id: {num}
sender: "{record['sender']}"
recipient: "{record['recipient']}"
date: "{record['date']}"
origin: "{record['origin']}"
destination: "{record['destination']}"
language: "{record['language']}"
---

# Letter {num}: {record['sender']} to {record['recipient']}

## Transcription

{body}

## Editorial Notes

{notes}
"""
    (CATALOGUED / f"letter_{num:02d}.md").write_text(md_content, encoding="utf-8")

with open("letters.json", "w", encoding="utf-8") as f:
    json.dump(letters, f, indent=2, ensure_ascii=False)
```

**Step 4: Run and verify**

Run: `uv run python parse.py`
Expected: 36 .md files in catalogued/, letters.json with 36 records, each with non-empty transcription

Run: `python -c "import json; d=json.load(open('letters.json')); print(len(d)); print(d[0]['sender'])"`
Expected: `36` and `Christopher Meryng`

---

### Task 3: Parse admin documents (Sections II–VII)

**Files:**
- Modify: `parse.py`

**Step 1: Add section II–VII parsing**

Same pattern as letters but documents [37]–[82]. Section boundaries:
- II: [37]–[39] (interrogations/depositions)
- III: [40]–[51] (English losses)
- IV: [52]–[57] (Venetian merchants)
- V: [58]–[65] (Hanseatic losses)
- VI: [66]–[78] (Spanish ships)
- VII: [79]–[82] (Low Countries ships)

Each admin doc gets:
- `catalogued/doc_NN.md` with YAML frontmatter (id, section, title, date, location, language)
- Record in `documents.json` with `file` pointing at the .md

The header format is similar: `[N.] Description. — Date. Location.`

Complications: within admin documents, sub-numbering `[1.]`, `[2.]` etc. appears for list items (cargo entries, interrogation points). These must NOT be treated as new documents — only document-level `[N.]` in the range [37]–[82] start new docs.

**Step 2: Run and verify**

Run: `uv run python parse.py`
Expected: 46 doc_NN.md files + documents.json with 46 records

---

### Task 4: Validate and fix edge cases

**Files:**
- Modify: `parse.py`

**Step 1: Spot-check output quality**

Read a sample of .md files and verify:
- Metadata fields populated correctly
- Transcription text is complete (not truncated, not including archival reference)
- Editorial notes separated from body
- No noise lines (page numbers, broken headers)
- Language assignments correct

**Step 2: Fix any parsing issues found**

Adjust regexes, language map, or boundary detection as needed.

**Step 3: Final validation**

Run: `uv run python parse.py`
Verify: all files present, JSON valid, spot-check 3-4 letters and 2-3 admin docs

**Step 4: Commit**

```bash
git init
git add parse.py convert.py letters.json documents.json catalogued/ docs/plans/
git commit -m "feat: Phase 0-1 — PDF conversion and structured parsing of all documents"
```
