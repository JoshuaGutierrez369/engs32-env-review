# -*- coding: utf-8 -*-
"""Audit ENVS_QB: correct answers should be supportable from lecture PDF corpus."""
from __future__ import annotations

import re
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
QUESTIONS = ROOT / "questions.js"
CORPUS = Path(__file__).resolve().parent / "materials_corpus.txt"
REPORT = Path(__file__).resolve().parent / "audit_report.txt"

LO_TO_LECTURES: dict[str, list[str]] = {
    "LO5W": ["Lec 5.2"],
    "LO5A": ["Lec 5.3"],
    "LO7": ["Lec 5.4", "Lec 5.5"],
    "LO8": ["Lec 5.4", "Lec 5.5"],
    "LO9": ["Lec 6"],
    "LO10": ["Lec 6"],
    "LO11": ["Lec 6"],
    "LO12": ["Lec 7"],
    "LO13": ["Lec 7"],
}

LECTURE_SECTIONS: dict[str, str] = {}

LECTURE_REF_BY_LO: dict[str, str] = {
    "LO5W": "CvSU ENGS 32 — Lec 5.2 Water Pollution (PDF)",
    "LO5A": "CvSU ENGS 32 — Lec 5.3 Air Pollution (PDF)",
    "LO7": "CvSU ENGS 32 — Lec 5.4 Solid Waste / Lec 5.5 Climate Change (PDF)",
    "LO8": "CvSU ENGS 32 — Lec 5.4 / 5.5 (PDF)",
    "LO9": "CvSU ENGS 32 — Lec 6 EIA (PDF)",
    "LO10": "CvSU ENGS 32 — Lec 6 EIA (PDF)",
    "LO11": "CvSU ENGS 32 — Lec 6 EIA (PDF)",
    "LO12": "CvSU ENGS 32 — Lec 7 Sustainable Development (PDF)",
    "LO13": "CvSU ENGS 32 — Lec 7 Sustainable Development (PDF)",
}


def _norm(s: str) -> str:
    s = s.lower()
    for a, b in (
        ("₂", "2"),
        ("₃", "3"),
        ("°", " "),
        ("–", "-"),
        ("—", "-"),
        ("\u2019", "'"),
        ("−", "-"),
        ("·", " "),
    ):
        s = s.replace(a, b)
    s = re.sub(r"[^\w\s.%-]", " ", s)
    return re.sub(r"\s+", " ", s)


def load_corpus() -> None:
    raw = CORPUS.read_text(encoding="utf-8")
    parts = re.split(r"={60}\n([^=]+)\n={60}", raw)
    for i in range(1, len(parts), 2):
        label = parts[i].strip().split("—")[0].strip()
        body = parts[i + 1] if i + 1 < len(parts) else ""
        LECTURE_SECTIONS[label] = _norm(body)


def parse_question_line(line: str) -> dict | None:
    line = line.strip().rstrip(",")
    if not line.startswith("{"):
        return None
    q: dict = {}
    m = re.search(r'"?id"?\s*:\s*"?([^",]+)"?', line)
    if not m:
        return None
    q["id"] = m.group(1)
    m = re.search(r'"?lo"?\s*:\s*"?([^",]+)"?', line)
    q["lo"] = m.group(1) if m else ""
    m = re.search(r'"?type"?\s*:\s*"?([^",]+)"?', line)
    q["type"] = m.group(1) if m else "mcq"
    if q["type"] == "tf":
        m = re.search(r'"?ans"?\s*:\s*(true|false)', line)
        q["ans"] = m.group(1) == "true"
        q["correct_text"] = ""
    else:
        m = re.search(r'"?ans"?\s*:\s*"?([a-d])"?', line)
        q["ans"] = m.group(1) if m else ""
        q["correct_text"] = ""
        if q["ans"]:
            pat = rf'"?ltr"?\s*:\s*"?{q["ans"]}"?\s*,\s*"?text"?\s*:\s*"([^"]*)"'
            m2 = re.search(pat, line)
            if m2:
                q["correct_text"] = m2.group(1)
    m = re.search(r'"?text"?\s*:\s*"([^"]*)"', line)
    q["text"] = m.group(1) if m else ""
    refs = re.findall(r'"?refs"?\s*:\s*\[([^\]]*)\]', line)
    if not refs:
        refs = re.findall(r'"refs"\s*:\s*\[([^\]]*)\]', line)
    q["refs_raw"] = refs[0] if refs else ""
    return q


def load_questions() -> list[dict]:
    raw = QUESTIONS.read_text(encoding="utf-8")
    out: list[dict] = []
    for line in raw.splitlines():
        if line.strip().startswith("{") and "id" in line[:80]:
            q = parse_question_line(line)
            if not q:
                continue
            if re.match(r"^e\d+$", q["id"]):
                continue
            if not q.get("text") and q.get("type") != "tf":
                continue
            out.append(q)
    return out


def keywords(text: str) -> list[str]:
    text = _norm(text)
    out: list[str] = []
    for num in re.findall(r"\d+(?:\.\d+)?", text):
        if len(num) >= 2:
            out.append(num)
    words = re.findall(r"[a-z0-9]{3,}", text)
    bigrams = [words[i] + " " + words[i + 1] for i in range(min(len(words) - 1, 8))]
    return list(dict.fromkeys(out + words[:14] + bigrams[:8]))


def grounded(q: dict) -> tuple[bool, str]:
    qid = q.get("id", "")
    lo = q.get("lo", "")
    lectures = list(LO_TO_LECTURES.get(lo, []))
    if qid.startswith("lo7-") and int(qid.split("-")[1]) >= 11:
        if "Lec 5.5" not in lectures:
            lectures.append("Lec 5.5")
    if qid == "lo7-22":
        lectures = ["Lec 5.3"]
    corpuses = " ".join(LECTURE_SECTIONS.get(l, "") for l in lectures)
    if not corpuses.strip():
        return False, f"no corpus for {lectures}"
    if q.get("type") == "tf":
        kws = keywords(q.get("text", ""))
    else:
        kws = keywords(q.get("correct_text", "") or q.get("text", ""))
    if not kws:
        return False, "no keywords"
    hits = []
    for k in kws:
        if k in corpuses:
            hits.append(k)
            continue
        if re.match(r"^\d", k) and k.replace(".", "") in corpuses.replace(".", " "):
            hits.append(k)
    need = max(1, min(3, len(kws) // 4))
    if len(hits) >= need:
        return True, f"{len(hits)}/{len(kws)} hits in {lectures}"
    return False, f"{len(hits)}/{len(kws)} hits; missed e.g. {kws[0]!r}"


def has_lecture_ref(q: dict) -> bool:
    r = q.get("refs_raw", "")
    return bool(
        re.search(
            r"ENGS\s*32|lec\s*5\.|lec\s*6|lec\s*7|Water Pollution|Air Pollution|Solid Waste|Climate Change|EIA|Sustainable",
            r,
            re.I,
        )
    )


def main() -> None:
    load_corpus()
    bank = load_questions()
    lines = [f"Audited {len(bank)} questions against materials_corpus.txt\n"]
    no_ref = [q["id"] for q in bank if not has_lecture_ref(q)]
    lines.append(f"Missing lecture PDF ref in refs[]: {len(no_ref)}\n")
    if no_ref:
        lines.append("  " + ", ".join(no_ref) + "\n")
    bad = []
    for q in bank:
        ok, msg = grounded(q)
        if not ok:
            bad.append((q, msg))
    lines.append(f"Corpus keyword grounding failures: {len(bad)}\n")
    for q, msg in bad:
        lines.append(f"  {q['id']} [{q['lo']}]: {msg}\n")
        lines.append(f"    Q: {q.get('text','')[:100]}\n")
        lines.append(f"    A: {(q.get('correct_text') or str(q.get('ans')))[:80]}\n")
    REPORT.write_text("".join(lines), encoding="utf-8")
    print(REPORT.read_text(encoding="utf-8"))


if __name__ == "__main__":
    main()
