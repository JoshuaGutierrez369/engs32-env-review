# -*- coding: utf-8 -*-
"""Insert LO5W / LO5A banks into questions.js (idempotent)."""
from __future__ import annotations

import json
import re
from pathlib import Path

from engs_pollution_bank import all_pollution_questions

ROOT = Path(__file__).resolve().parent.parent
QUESTIONS = ROOT / "questions.js"


def _sanitize_json_line(line: str) -> str:
    s = line.strip().rstrip(",")
    for a, b in (
        ("\u201c", '"'),
        ("\u201d", '"'),
        ("\u2018", "'"),
        ("\u2019", "'"),
    ):
        s = s.replace(a, b)
    # questions.js uses JS object literals (unquoted keys)
    s = re.sub(r"([\{,])\s*([a-zA-Z_][a-zA-Z0-9_]*)\s*:", r'\1"\2":', s)
    return s


def load_existing() -> tuple[list[dict], list[dict], str]:
    raw = QUESTIONS.read_text(encoding="utf-8")
    header = raw[: raw.index("window.ENVS_QB")]
    bank: list[dict] = []
    essays: list[dict] = []
    mode = None
    for line in raw.splitlines():
        if line.strip().startswith("window.ENVS_QB"):
            mode = "qb"
            continue
        if line.strip().startswith("window.ENVS_ESSAYS"):
            mode = "essays"
            continue
        if mode == "qb" and line.strip().startswith("{id:"):
            bank.append(json.loads(_sanitize_json_line(line)))
        elif mode == "essays" and line.strip().startswith("{id:"):
            essays.append(json.loads(_sanitize_json_line(line)))
    return bank, essays, header


def fmt_item(q: dict) -> str:
    return "  " + json.dumps(q, ensure_ascii=False, separators=(",", ":")) + ","


def main() -> None:
    raw = QUESTIONS.read_text(encoding="utf-8")
    if 'lo:"LO5W"' in raw or '"LO5W"' in raw:
        print("LO5W/LO5A already present — skip")
        return
    lines_path = Path(__file__).resolve().parent / "_pollution_lines.txt"
    if not lines_path.exists():
        import json as _json

        lines_path.write_text(
            "".join(
                "  "
                + _json.dumps(q, ensure_ascii=False, separators=(",", ":"))
                + ",\n"
                for q in all_pollution_questions()
            ),
            encoding="utf-8",
        )
    block = lines_path.read_text(encoding="utf-8")
    marker = "  /* LO5.2 — Water pollution · LO5.3 — Air pollution (23 MCQ/T-F each) */\n"
    if marker not in raw:
        raise ValueError("Expected pollution section marker in questions.js")
    raw = raw.replace(marker, marker + block, 1)
    QUESTIONS.write_text(raw, encoding="utf-8")
    print("wrote", QUESTIONS, "+46 pollution items")


if __name__ == "__main__":
    main()
