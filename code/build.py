"""Build the static site by injecting JSON data into the HTML template."""

import json
from pathlib import Path


def build():
    root = Path(__file__).resolve().parent.parent
    code = root / "code"

    letters = json.loads((root / "letters.json").read_text(encoding="utf-8"))
    documents = json.loads((root / "documents.json").read_text(encoding="utf-8"))

    template = (code / "site" / "template.html").read_text(encoding="utf-8")

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

    dist = root / "dist"
    dist.mkdir(exist_ok=True)
    (dist / "index.html").write_text(html, encoding="utf-8")
    print(f"Built dist/index.html ({len(html):,} bytes)")
    print(f"  {len(letters)} letters, {len(documents)} documents embedded")


if __name__ == "__main__":
    build()
