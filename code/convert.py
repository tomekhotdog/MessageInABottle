"""Phase 0: Convert Message in a Bottle PDF to Markdown using markitdown."""

from markitdown import MarkItDown

md = MarkItDown()
result = md.convert("raw/MessageInABottle.pdf")

with open("hanseatic_letters.md", "w", encoding="utf-8") as f:
    f.write(result.text_content)

print(f"Conversion complete. Output length: {len(result.text_content)} characters")
print(f"Line count: {result.text_content.count(chr(10))}")
