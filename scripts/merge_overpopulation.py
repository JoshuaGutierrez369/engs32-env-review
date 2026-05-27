# -*- coding: utf-8 -*-
"""Insert LO5O (Lec 5.1 Overpopulation) bank into questions.js (idempotent)."""
from __future__ import annotations

import json
from pathlib import Path

from engs_overpopulation_bank import all_overpopulation_questions

ROOT = Path(__file__).resolve().parent.parent
QUESTIONS = ROOT / "questions.js"
MARKER = "  /* LO5.1 — Overpopulation (23 MCQ/T-F) */\n"
POLLUTION_MARKER = "  /* LO5.2 — Water pollution · LO5.3 — Air pollution (23 MCQ/T-F each) */\n"


def main() -> None:
    raw = QUESTIONS.read_text(encoding="utf-8")
    if '"LO5O"' in raw or "lo5o-01" in raw:
        print("LO5O already present — skip")
        return
    block = "".join(
        "  " + json.dumps(q, ensure_ascii=False, separators=(",", ":")) + ",\n"
        for q in all_overpopulation_questions()
    )
    if POLLUTION_MARKER not in raw:
        raise ValueError("Expected pollution section marker in questions.js")
    raw = raw.replace(POLLUTION_MARKER, MARKER + block + POLLUTION_MARKER, 1)
    QUESTIONS.write_text(raw, encoding="utf-8")
    print("wrote", QUESTIONS, "+23 LO5O items")


if __name__ == "__main__":
    main()
