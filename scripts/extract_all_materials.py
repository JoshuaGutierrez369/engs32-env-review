# -*- coding: utf-8 -*-
"""Extract all ENGS 32 lecture PDFs into materials_corpus.txt for answer auditing."""
from __future__ import annotations

from pathlib import Path

import pypdf

DOWNLOADS = Path(r"C:\Users\joshu\Downloads")
PDFS = [
    ("Lec 5.1", DOWNLOADS / "ENGS 32 - Lec 5.1 - Overpopulation.pdf"),
    ("Lec 5.2", DOWNLOADS / "ENGS 32 - Lec 5.2 - Water Pollution.pdf"),
    ("Lec 5.3", DOWNLOADS / "ENGS 32 - Lec 5.3 - Air Pollution.pdf"),
    ("Lec 5.4", DOWNLOADS / "ENGS 32 - Lec 5.4 - Solid Waste.pdf"),
    ("Lec 5.5", DOWNLOADS / "ENGS 32 - Lec 5.5 - Climate Change.pdf"),
    ("Lec 6", DOWNLOADS / "ENGS 32 - Lec 6 - EIA.pdf"),
    ("Lec 7", DOWNLOADS / "ENGS 32 - Lec 7 - Sustainable Development.pdf"),
]

OUT = Path(__file__).resolve().parent / "materials_corpus.txt"


def main() -> None:
    parts: list[str] = []
    for label, path in PDFS:
        if not path.exists():
            parts.append(f"\n\n=== MISSING: {label} ({path}) ===\n")
            continue
        r = pypdf.PdfReader(str(path))
        text = "\n".join((p.extract_text() or "") for p in r.pages)
        parts.append(f"\n\n{'=' * 60}\n{label} — {path.name}\n{'=' * 60}\n{text}")
    OUT.write_text("".join(parts), encoding="utf-8")
    print("wrote", OUT, "bytes", OUT.stat().st_size)


if __name__ == "__main__":
    main()
