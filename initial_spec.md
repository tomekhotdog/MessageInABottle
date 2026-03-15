
Project: Hanseatic Letters — Translation & Presentation
I have a 260-page academic PDF called Message in a Bottle (Jenks & Wubs-Mrozewicz, 2022, open-access via Brepols). It contains scholarly transcriptions of 36 merchants' letters intercepted in the English Channel in 1533 — written in Middle English, Middle Dutch, Low German, and Latin — along with supporting administrative documents and academic introductions. The letters have never been translated into modern English.
The PDF is at message_in_a_bottle.pdf.
Goal: Build a clean data pipeline and then a web presentation that makes these letters accessible to a general audience for the first time.
Phase 0 — PDF to Markdown
Write a Python script convert.py that uses the markitdown library to convert message_in_a_bottle.pdf to hanseatic_letters.md. Run it. Then inspect the output and report back on quality — how clean is the conversion, are special characters and editorial symbols intact, how are footnotes handled, and how are the individual letters delineated. Flag anything that will need cleaning before we can reliably parse the structure.
Phase 1 — Parse & structure the markdown
Read hanseatic_letters.md and understand its structure. The document has:

Front matter and academic introductions (context we want to preserve)
Individual letter transcriptions, each with a document number, sender, recipient, date, place of origin, destination, and language
Footnotes and editorial apparatus (square brackets for lacunae, abbreviations, etc.)
Supporting administrative documents (depositions, cargo lists)

Split the content into discrete units. For each letter, create a structured JSON record with fields: id, sender, recipient, date, origin, destination, language, original_transcription, editorial_notes. Save these as individual files and a master letters.json.
Phase 2 — Translation
For each letter record, use the Anthropic API to produce a modern English translation of original_transcription. The prompt should instruct the model to:

Translate faithfully but readably — not word-for-word archaic, but not anachronistic either
Preserve proper nouns, place names, and merchant terminology with inline notes where helpful
Flag coded or ambiguous passages (e.g. prices in code, unclear abbreviations) rather than guessing

Store translations back into each letter's JSON record under modern_english_translation.
Phase 3 — Categorisation & enrichment
For each letter, use the API to generate:

A 2-3 sentence human summary (the "story" of the letter — who is writing, to whom, about what, any emotional or historical interest)
Tags: type (business / personal / mixed), themes (e.g. trade, family, politics, coded prices, women writing), people_mentioned, goods_mentioned, notable (boolean — is this letter particularly interesting for a general audience?)

Phase 4 — Web presentation
Build a clean, well-designed static website (React or plain HTML/CSS/JS, your call) that presents the letters as a browsable collection. Each letter gets its own page showing: the human summary, modern translation, original transcription, and editorial notes side by side. The index page should allow filtering by language, theme, and type. Design should feel like a quality editorial/historical project — not a database dump.