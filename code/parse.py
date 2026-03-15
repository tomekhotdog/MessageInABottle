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
NOISE_PATTERNS = [
    re.compile(r"^\d{1,3}$"),                              # bare page numbers
    re.compile(r"^[ivx]+:\s+.*[a-z]\s{2,}[a-z]", re.I),   # broken spaced-out section headers
    re.compile(r"^source\s+edi\s*tion", re.I),             # "source  edi tion"
    re.compile(r"^a\s*ppe\s*ndi\s*x\s+i", re.I),          # "a ppe ndi x i"
    re.compile(r"^list\s+of\s+do\s*cumen", re.I),          # "list of  do cumen ts"
    re.compile(r"^bibliogr\s*aphy", re.I),                  # "bibliogr aphy"
]


def is_noise(line: str) -> bool:
    stripped = line.strip()
    if not stripped:
        return False
    return any(p.match(stripped) for p in NOISE_PATTERNS)


def clean_text(text_lines: list[str]) -> str:
    """Remove noise lines and collapse excessive blank lines."""
    cleaned = [l for l in text_lines if not is_noise(l)]
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
    return "\n".join(result).strip()


# --- Find section boundaries ---
SECTION_MARKERS = [
    ("I", re.compile(r"^I:\s*Merchants.?\s*letters", re.I)),
    ("II", re.compile(r"^II:\s*Capture", re.I)),
    ("III", re.compile(r"^III:\s*Losses", re.I)),
    ("IV", re.compile(r"^IV:\s*Goods taken from Venetian", re.I)),
    ("V", re.compile(r"^V:\s*Hanseatic losses", re.I)),
    ("VI", re.compile(r"^VI:\s*Goods taken in Spanish", re.I)),
    ("VII", re.compile(r"^VII:\s*Goods taken from ships", re.I)),
    ("INDEX", re.compile(r"^Index of people and places$", re.I)),
]

section_starts: dict[str, int] = {}
# Start searching after line 4000 to skip Table of Contents matches
for i, line in enumerate(lines):
    if i < 4000:
        continue
    for name, pat in SECTION_MARKERS:
        if name not in section_starts and pat.match(line.strip()):
            section_starts[name] = i

assert "I" in section_starts, "Could not find Section I"
print(f"Section boundaries: { {k: v for k, v in sorted(section_starts.items(), key=lambda x: x[1])} }")

# --- Write context.md ---
context_text = clean_text(lines[: section_starts["I"]])
(CATALOGUED / "context.md").write_text(
    "---\ntitle: \"Message in a Bottle — Context & Introductions\"\n"
    "description: \"Front matter, scholarly introductions, diplomatic notes, "
    "bibliography, and appendices\"\n---\n\n" + context_text + "\n",
    encoding="utf-8",
)
print(f"Wrote catalogued/context.md ({len(context_text)} chars)")

# --- Document parsing ---
DOC_RE = re.compile(r"^\[(\d+)\.\]\s*(.*)")

# Language map for the 36 letters (verified from content inspection)
LETTER_LANG = {
    1: "Middle English", 2: "Middle English", 3: "Middle English",
    4: "Middle English", 5: "Middle English", 6: "Middle English",
    7: "Middle English", 8: "Middle Dutch", 9: "Middle English",
    10: "Middle Dutch", 11: "Middle English", 12: "Middle Dutch",
    13: "Middle English", 14: "Middle Dutch", 15: "Middle English",
    16: "Middle English", 17: "Middle Dutch", 18: "Middle Dutch",
    19: "Low German", 20: "Middle English", 21: "Middle English",
    22: "Middle English", 23: "Middle English", 24: "Middle English",
    25: "Middle Dutch", 26: "Middle English", 27: "Middle Dutch",
    28: "Middle English", 29: "Middle Dutch", 30: "Middle English",
    31: "Middle English", 32: "Middle English", 33: "Middle English",
    34: "Middle English", 35: "Middle English", 36: "Low German",
}


def is_document_start(i: int, num: int) -> bool:
    """Check if [N.] at line i is a true document start (not a sub-item within a doc).

    True document starts have:
    - A descriptive header (sender/recipient or description), not "Item..." content
    - Followed within a few lines by an archival reference (HL AHL...)
    """
    m = DOC_RE.match(lines[i])
    rest = m.group(2).strip() if m else ""

    # If the rest of the line starts with "Item" or similar inventory content, it's a sub-item
    if rest and (rest.startswith("Item") or rest.startswith("item")):
        return False

    # Check next few non-blank lines for archival reference or descriptive header
    for j in range(i, min(i + 15, len(lines))):
        stripped = lines[j].strip()
        if "HL AHL" in stripped or "HL AHL," in stripped:
            return True

    # If the [N.] is alone on a line, check the next content line
    if not rest:
        for j in range(i + 1, min(i + 5, len(lines))):
            stripped = lines[j].strip()
            if not stripped:
                continue
            if stripped.startswith("Item") or stripped.startswith("item"):
                return False
            # Descriptive headers tend to be longer and not start with inventory terms
            return True

    return True


def find_doc_boundaries(start: int, end: int, valid_range: range) -> list[tuple[int, int, int]]:
    """Find [N.] document starts within line range. Returns [(num, start_line, end_line), ...]."""
    docs = []
    seen_nums = set()
    for i in range(start, end):
        m = DOC_RE.match(lines[i])
        if m:
            num = int(m.group(1))
            if num in valid_range and is_document_start(i, num):
                # Avoid duplicate document numbers (sub-items can have same number)
                if num in seen_nums:
                    continue
                seen_nums.add(num)
                if docs:
                    docs[-1] = (docs[-1][0], docs[-1][1], i)
                docs.append((num, i, end))
    return docs


def get_header_text(start: int, end: int) -> str:
    """Extract the full header text after [N.], joining continuation lines."""
    m = DOC_RE.match(lines[start])
    first_part = m.group(2).strip() if m else ""

    if first_part:
        # Header is on the same line as [N.], but may continue
        if "—" not in first_part:
            for j in range(start + 1, min(start + 5, end)):
                if lines[j].strip() and not lines[j].strip().startswith("HL "):
                    first_part += " " + lines[j].strip()
                    if "—" in first_part or "." in lines[j].strip()[-3:]:
                        break
        return first_part

    # Header is on subsequent lines
    header_parts = []
    for j in range(start + 1, min(start + 6, end)):
        stripped = lines[j].strip()
        if not stripped:
            if header_parts:
                continue
            else:
                continue
        if stripped.startswith("HL ") or stripped.startswith("HL AHL"):
            break
        header_parts.append(stripped)
        if "—" in stripped and ("." in stripped.split("—")[-1]):
            break
    return " ".join(header_parts)


def parse_letter_metadata(header: str) -> dict:
    """Parse 'Sender to Recipient. — Date. Location.' from header text."""
    result = {"sender": "", "recipient": "", "date": "", "origin": "", "destination": ""}

    # Split on em-dash
    if "—" in header:
        before_dash, after_dash = header.split("—", 1)
        before_dash = before_dash.strip().rstrip(".")
        after_dash = after_dash.strip().rstrip(".")

        # Parse date and location from after dash
        # Pattern: "Date. Location" or just "Date" or "(undated)"
        date_loc_parts = [p.strip() for p in after_dash.split(".") if p.strip()]
        if date_loc_parts:
            result["date"] = date_loc_parts[0]
        if len(date_loc_parts) > 1:
            result["origin"] = date_loc_parts[-1]

        # Parse sender/recipient from before dash
        # Pattern: "Sender [in Place] to Recipient [in Place]"
        # Try splitting on " to " (but be careful of "Antwerp to" etc.)
        to_match = re.search(r"\s+to\s+", before_dash)
        if to_match:
            sender_part = before_dash[: to_match.start()].strip()
            recipient_part = before_dash[to_match.end() :].strip()

            # Extract destination from recipient "X in London"
            in_match = re.search(r"\s+in\s+(London|London')\s*$", recipient_part, re.I)
            if in_match:
                result["destination"] = "London"
                recipient_part = recipient_part[: in_match.start()].strip()
            elif "London" in recipient_part:
                result["destination"] = "London"

            # Extract origin from sender "X in Antwerp"
            sender_in = re.search(
                r"\s+in\s+(Antwerp|Brussels|Cologne|Andwarpe|Andwerp|Andwarp|London)\s*$",
                sender_part, re.I
            )
            if sender_in:
                if not result["origin"]:
                    result["origin"] = sender_in.group(1)
                sender_part = sender_part[: sender_in.start()].strip()

            result["sender"] = sender_part
            result["recipient"] = recipient_part
        else:
            # No "to" — might be an admin doc description
            result["sender"] = before_dash
    else:
        result["sender"] = header

    return result


def split_body_and_notes(start: int, end: int) -> tuple[str, str, str]:
    """Extract archival_ref, body text, and editorial notes from document lines."""
    doc_lines = lines[start:end]

    # Skip the [N.] line and blank lines
    i = 0
    m = DOC_RE.match(doc_lines[0])
    i = 1  # past [N.]

    # Skip to header text (which we've already parsed separately)
    # Find where archival reference starts (HL AHL...)
    arch_start = None
    arch_end = None
    for j in range(i, min(len(doc_lines), 30)):
        stripped = doc_lines[j].strip()
        if stripped.startswith("HL AHL") or stripped.startswith("HL AHL,"):
            arch_start = j
            break

    # Find where archival reference ends (blank line after it, or first line of body)
    if arch_start is not None:
        for j in range(arch_start, min(len(doc_lines), arch_start + 20)):
            stripped = doc_lines[j].strip()
            if j > arch_start and stripped == "":
                # Check if next non-blank line is still archival
                next_content = None
                for k in range(j + 1, min(len(doc_lines), j + 5)):
                    if doc_lines[k].strip():
                        next_content = doc_lines[k].strip()
                        break
                if next_content and (
                    next_content.startswith("HL ") or
                    next_content.startswith("classification") or
                    next_content.startswith("as ASA") or
                    next_content.startswith("Sealed") or
                    next_content.startswith("closed") or
                    next_content.startswith("dorse:") or
                    next_content.startswith("On the dorse") or
                    next_content.startswith("the dorse:") or
                    next_content.startswith("with the signet") or
                    next_content.startswith("Original")
                ):
                    continue
                arch_end = j
                break
        if arch_end is None:
            arch_end = arch_start + 10  # fallback

    archival_ref = ""
    body_start_idx = 1
    if arch_start is not None and arch_end is not None:
        archival_ref = "\n".join(doc_lines[arch_start:arch_end]).strip()
        body_start_idx = arch_end
    else:
        # No archival ref found, body starts after header
        for j in range(i, min(len(doc_lines), 10)):
            if doc_lines[j].strip() == "":
                body_start_idx = j
                break

    # Everything from body_start to end is body + editorial notes
    body_and_notes = doc_lines[body_start_idx:]

    # Split editorial notes from body
    # Editorial notes are at the end, matching patterns like:
    #   "a to follows, struck through HL."
    #   "a-a Interlined HL."
    #   "b Corrected in HL from..."
    #   "N) " (numbered references like "1)")
    EDITORIAL_RE = re.compile(
        r"^[a-h](?:-[a-h])?\s+(?:Corrected|Interlined|Sic|Reading|One|Two|follows|Hole|Struck|to follows|he follows|"
        r"my follows|s\[al\]|ick|vre|scho|nany|nott|nomar|hym|fat|1 follows|w follows|ha\[ve\]|"
        r"ut follows|letter follows|yp|ys HL|dy|therd|ki\[ppe\]|several|4 C|den follows|"
        r"p follows|for follows)",
        re.I
    )
    EDITORIAL_NUM_RE = re.compile(r"^\d+\)$")
    FOOTNOTE_RE = re.compile(r"^\d+\s+\S")  # numbered footnotes like "1  Thomas Manners..."
    HL_NOTE_RE = re.compile(r"(?:struck through|interlined|in error|HL\.|follows,|expunged|uncertain)\s*$", re.I)

    # Scan from the end to find where editorial notes begin
    notes_lines = []
    body_lines = list(body_and_notes)

    # Work backwards from end, collecting editorial note lines
    j = len(body_lines) - 1
    while j >= 0:
        stripped = body_lines[j].strip()
        if not stripped:
            j -= 1
            continue
        is_editorial = (
            EDITORIAL_RE.match(stripped) or
            EDITORIAL_NUM_RE.match(stripped) or
            HL_NOTE_RE.search(stripped) or
            (len(stripped) < 80 and "HL" in stripped and (
                "follows" in stripped.lower() or
                "struck" in stripped.lower() or
                "interlined" in stripped.lower() or
                "corrected" in stripped.lower() or
                "in error" in stripped.lower()
            ))
        )
        if is_editorial:
            notes_lines.insert(0, body_lines[j])
            body_lines[j] = ""  # remove from body
            j -= 1
        else:
            break  # stop once we hit non-editorial content

    body_text = clean_text(body_lines)
    notes_text = "\n".join(l for l in notes_lines if l.strip()).strip()

    return archival_ref, body_text, notes_text


def get_section_range(section_name: str) -> tuple[int, int]:
    """Get line range for a section."""
    ordered = sorted(section_starts.items(), key=lambda x: x[1])
    for i, (name, start) in enumerate(ordered):
        if name == section_name:
            end = ordered[i + 1][1] if i + 1 < len(ordered) else len(lines)
            return start, end
    raise ValueError(f"Section {section_name} not found")


# === PARSE SECTION I: Letters [1]-[36] ===

sec_i_start, sec_i_end = get_section_range("I")
letter_bounds = find_doc_boundaries(sec_i_start, sec_i_end, range(1, 37))
print(f"Found {len(letter_bounds)} letters in Section I")

letters = []
for num, start, end in letter_bounds:
    header = get_header_text(start, end)
    meta = parse_letter_metadata(header)
    archival_ref, body, notes = split_body_and_notes(start, end)
    language = LETTER_LANG.get(num, "Unknown")

    record = {
        "id": num,
        "sender": meta["sender"],
        "recipient": meta["recipient"],
        "date": meta["date"],
        "origin": meta["origin"],
        "destination": meta["destination"],
        "language": language,
        "original_transcription": body,
        "editorial_notes": notes,
        "archival_reference": archival_ref,
        "file": f"catalogued/letter_{num:02d}.md",
    }
    letters.append(record)

    # Write individual .md
    md = f"""---
id: {num}
sender: "{meta['sender']}"
recipient: "{meta['recipient']}"
date: "{meta['date']}"
origin: "{meta['origin']}"
destination: "{meta['destination']}"
language: "{language}"
---

# Letter {num}: {meta['sender']} to {meta['recipient']}

## Archival Reference

{archival_ref}

## Transcription

{body}

## Editorial Notes

{notes}
"""
    (CATALOGUED / f"letter_{num:02d}.md").write_text(md, encoding="utf-8")

with open("letters.json", "w", encoding="utf-8") as f:
    json.dump(letters, f, indent=2, ensure_ascii=False)

print(f"Wrote {len(letters)} letter files + letters.json")

# === PARSE SECTIONS II-VII: Admin documents [37]-[82] ===

SECTION_TITLES = {
    "II": "Capture of the ship of Adrian Johnson off England 19 Aug. 1533",
    "III": "Losses in the ship of Adrian Johnson (1533): English losses",
    "IV": "Goods taken from Venetian merchants in the ship of Adrian Johnson (19 Aug. 1533)",
    "V": "Hanseatic losses in the taking of Adrian Johnson's ship",
    "VI": "Goods taken in Spanish ships",
    "VII": "Goods taken from ships of the Low Countries",
}

# Document ranges per section
DOC_RANGES = {
    "II": range(37, 40),    # [37]-[39]
    "III": range(40, 52),   # [40]-[51]
    "IV": range(52, 58),    # [52]-[57]
    "V": range(58, 66),     # [58]-[65]
    "VI": range(66, 79),    # [66]-[78]
    "VII": range(79, 83),   # [79]-[82]
}

documents = []
for sec_name in ["II", "III", "IV", "V", "VI", "VII"]:
    if sec_name not in section_starts:
        print(f"Warning: Section {sec_name} not found, skipping")
        continue

    sec_start, sec_end = get_section_range(sec_name)
    doc_range = DOC_RANGES[sec_name]
    doc_bounds = find_doc_boundaries(sec_start, sec_end, doc_range)
    print(f"Section {sec_name}: found {len(doc_bounds)} documents")

    for num, start, end in doc_bounds:
        header = get_header_text(start, end)
        archival_ref, body, notes = split_body_and_notes(start, end)

        # For admin docs, parse date/location from header
        date = ""
        location = ""
        if "—" in header:
            after_dash = header.split("—", 1)[1].strip().rstrip(".")
            parts = [p.strip() for p in after_dash.split(".") if p.strip()]
            if parts:
                date = parts[0]
            if len(parts) > 1:
                location = parts[-1]

        # Detect language from content
        language = "Low German"  # default for admin docs
        body_lower = body[:500].lower()
        if "item shipped" in body_lower or "shipped by" in body_lower or "laden by" in body_lower:
            language = "Middle English"
        elif "in primis" in body_lower or "anno domini" in body_lower or "notum" in body_lower:
            language = "Latin"
        elif "item noch" in body_lower or "item ein" in body_lower or "gemarket" in body_lower:
            language = "Low German"
        elif any(w in body_lower for w in ["scheped", "shipped", "content", "bale", "mercer"]):
            language = "Middle English"

        record = {
            "id": num,
            "section": sec_name,
            "section_title": SECTION_TITLES[sec_name],
            "title": header.split("—")[0].strip().rstrip(".") if "—" in header else header,
            "date": date,
            "location": location,
            "language": language,
            "content": body,
            "editorial_notes": notes,
            "archival_reference": archival_ref,
            "file": f"catalogued/doc_{num:02d}.md",
        }
        documents.append(record)

        md = f"""---
id: {num}
section: "{sec_name}"
section_title: "{SECTION_TITLES[sec_name]}"
title: "{record['title']}"
date: "{date}"
location: "{location}"
language: "{language}"
---

# Document {num}: {record['title']}

**Section {sec_name}:** {SECTION_TITLES[sec_name]}

## Archival Reference

{archival_ref}

## Content

{body}

## Editorial Notes

{notes}
"""
        (CATALOGUED / f"doc_{num:02d}.md").write_text(md, encoding="utf-8")

with open("documents.json", "w", encoding="utf-8") as f:
    json.dump(documents, f, indent=2, ensure_ascii=False)

print(f"Wrote {len(documents)} document files + documents.json")
print(f"\nTotal output: {len(letters)} letters + {len(documents)} admin docs + context.md")
