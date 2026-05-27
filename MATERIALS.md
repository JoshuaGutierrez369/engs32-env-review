# Study materials (answer key source)

All **keyed answers** in this reviewer are written to match the **CvSU ENGS 32 lecture PDFs** bundled with the course—not third-party summaries alone.

## Required PDFs

| File | Topics in app |
|------|----------------|
| `ENGS 32 - Lec 5.2 - Water Pollution.pdf` | LO5W |
| `ENGS 32 - Lec 5.3 - Air Pollution.pdf` | LO5A (and air-linked items) |
| `ENGS 32 - Lec 5.4 - Solid Waste.pdf` | LO7, LO8 |
| `ENGS 32 - Lec 5.5 - Climate Change.pdf` | LO7 (climate block) |
| `ENGS 32 - Lec 6 - EIA.pdf` | LO9–LO11 |
| `ENGS 32 - Lec 7 - Sustainable Development.pdf` | LO12–LO13 |

Place these files in your Downloads folder (or the same folder you use for offline study) alongside the reviewer.

## How questions cite sources

- Each item’s `refs` array **starts with** the matching lecture PDF.
- Links to Lawphil, UNDP, IPCC, etc. appear only as **“(optional cross-check)”** when the slide already states the fact (e.g., RA 9003 enactment date on Lec 5.4 slides).

## Regenerating the text index

```bash
python scripts/extract_all_materials.py
python scripts/align_to_materials.py
python scripts/audit_materials.py
```

`scripts/materials_corpus.txt` is the searchable extract used for audits.
