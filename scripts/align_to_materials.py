# -*- coding: utf-8 -*-
"""Align ENVS_QB refs/explanations so keyed answers trace to provided lecture PDFs."""
from __future__ import annotations

import json
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
QUESTIONS = ROOT / "questions.js"

PRIMARY_REF: dict[str, str] = {
    "LO5W": "CvSU ENGS 32 — Lec 5.2 Water Pollution (PDF)",
    "LO5A": "CvSU ENGS 32 — Lec 5.3 Air Pollution (PDF)",
    "LO7": "CvSU ENGS 32 — Lec 5.4 Solid Waste (PDF)",
    "LO8": "CvSU ENGS 32 — Lec 5.4 Solid Waste (PDF)",
    "LO9": "CvSU ENGS 32 — Lec 6 EIA (PDF)",
    "LO10": "CvSU ENGS 32 — Lec 6 EIA (PDF)",
    "LO11": "CvSU ENGS 32 — Lec 6 EIA (PDF)",
    "LO12": "CvSU ENGS 32 — Lec 7 Sustainable Development (PDF)",
    "LO13": "CvSU ENGS 32 — Lec 7 Sustainable Development (PDF)",
}

# LO7 climate items also use Lec 5.5
CLIMATE_IDS = {
    "lo7-11",
    "lo7-12",
    "lo7-13",
    "lo7-14",
    "lo7-15",
    "lo7-16",
    "lo7-17",
    "lo7-21",
    "lo7-23",
}

AIR_IDS = {"lo7-22"}

EXTERNAL_ONLY = re.compile(
    r"lawphil|ipcc|unfccc|undp|unep|adb|world bank|nathanson|glasson|masters|"
    r"canter|molles|smith|mihelcic|kaneko|hoekstra|wackernagel|iaia|officialgazette|"
    r"digest\.ph|epi\.yale|sdgs\.un\.org|http",
    re.I,
)

PATCHES: dict[str, dict] = {
    "lo7-07": {
        "text": "Per CvSU Lec 5.4, on which date was Republic Act No. 9003 enacted according to the lecture slides?",
        "choices": [
            {"ltr": "a", "text": "16 February 2001"},
            {"ltr": "b", "text": "26 January 2001"},
            {"ltr": "c", "text": "11 June 1978"},
            {"ltr": "d", "text": "26 January 2000"},
        ],
        "ans": "a",
        "expl": (
            "Correct (a): Lec 5.4 states RA 9003 was enacted on February 16, 2001. "
            "(b)–(d) are distractors from other statutes or common mismatches."
        ),
    },
    "lo13-01": {
        "text": "HDI in Lec 7 is a composite measure. Which third pillar joins life expectancy and education in the slides?",
        "choices": [
            {"ltr": "a", "text": "Military expenditure as % of GDP"},
            {"ltr": "b", "text": "Income"},
            {"ltr": "c", "text": "National social-media follower totals"},
            {"ltr": "d", "text": "Exclusive economic zone nautical miles"},
        ],
        "ans": "b",
        "expl": (
            "Correct (b): Lec 7 lists HDI factors as life expectancy, education, and income. "
            "(a)/(c)/(d) are not in the lecture composite."
        ),
    },
    "lo13-04": {
        "choices": [
            {"ltr": "a", "text": "Psychometric IQ with national laureates"},
            {
                "ltr": "b",
                "text": "Resources and land required to sustain consumption versus available biocapacity",
            },
            {"ltr": "c", "text": "Equity volatility indices only"},
            {"ltr": "d", "text": "A-weighted roadway noise contours alone"},
        ],
        "ans": "b",
        "expl": (
            "Correct (b): Lec 7 defines ecological footprint as resources/land needed to sustain "
            "consumption patterns and compare ecological demands. Other options are unrelated metrics."
        ),
    },
    "lo13-05": {
        "choices": [
            {"ltr": "a", "text": "Maximizing single-use polymers to inflate GDP"},
            {
                "ltr": "b",
                "text": "Minimize waste and maximize resource efficiency while reducing virgin resource use",
            },
            {"ltr": "c", "text": "Linear cradle-to-grave default without feedback"},
            {"ltr": "d", "text": "Exclusive reliance on third-country landfill"},
        ],
        "ans": "b",
        "expl": (
            "Correct (b): Lec 7 circular-economy slides stress minimizing wastes, maximizing resource "
            "efficiency, and reducing finite resource use. (a)/(c)/(d) contradict that framing."
        ),
    },
    "lo9-06": {
        "text": "EIA as a planning tool (Lec 6) means mitigation and project design should occur:",
        "choices": [
            {"ltr": "a", "text": "Only after abandonment when bonds mature"},
            {
                "ltr": "b",
                "text": "During planning and design—where to locate projects and how to design them—before commitments foreclose alternatives",
            },
            {"ltr": "c", "text": "Behind closed doors excluding stakeholders entirely"},
            {"ltr": "d", "text": "Solely when ODA co-financing triggers safeguard templates"},
        ],
        "ans": "b",
        "expl": (
            "Correct (b): Lec 6 presents EIA as a planning tool for siting, design, and minimizing "
            "adverse impacts before operational lock-in. (a)/(c)/(d) mis-time or mis-scope the process."
        ),
    },
    "lo7-22": {
        "lo": "LO5A",
        "text": "Photochemical smog in Lec 5.3 includes tropospheric ozone formed in sunlight. Tropospheric O₃ in urban afternoons is best classified as:",
        "choices": [
            {"ltr": "a", "text": "A primary pollutant exiting tailpipes unchanged"},
            {"ltr": "b", "text": "A secondary product of precursor chemistry (e.g., NOx and VOCs in sunlight)"},
            {"ltr": "c", "text": "Unrelated to air-quality management narratives"},
            {"ltr": "d", "text": "Only meaningful if dissolved in groundwater"},
        ],
        "ans": "b",
        "expl": (
            "Correct (b): Lec 5.3 lists tropospheric ozone among photochemical smog products formed "
            "in the presence of sunlight. (a) mislabels tailpipe primaries. (c)/(d) confuse media."
        ),
    },
    "lo7-23": {
        "type": "tf",
        "text": "Per Lec 5.5, both carbon dioxide and methane are named among greenhouse gases linked to enhanced radiative trapping.",
        "ans": True,
        "expl": (
            "TRUE: Lec 5.5 greenhouse-gas lists include carbon dioxide and methane among key contributors. "
            "FALSE would contradict the slide inventory."
        ),
    },
    "lo12-06": {
        "text": "Per Lec 7, how are the UN Sustainable Development Goals characterized?",
        "choices": [
            {
                "ltr": "a",
                "text": "Seventeen interlinked objectives forming a shared blueprint for people and the planet",
            },
            {"ltr": "b", "text": "Ten goals tied only to biodiversity"},
            {"ltr": "c", "text": "Fifteen goals covering OECD members exclusively"},
            {"ltr": "d", "text": "Twenty-five subsidiary targets with no headline goals"},
        ],
        "ans": "a",
        "expl": (
            "Correct (a): Lec 7 describes seventeen interlinked SDGs as a shared blueprint. "
            "(b)–(d) misstate the count or scope taught in-session."
        ),
    },
    "lo10-08": {
        "text": "Per Lec 6, Presidential Decree No. 1586 (1978) established which nationwide environmental assessment architecture?",
        "expl": (
            "TRUE: Lec 6 cites PD 1586 as establishing the Environmental Impact Statement System. "
            "FALSE would misplace PEISS inception."
        ),
    },
    "lo10-01": {
        "expl": (
            "Correct (b): Lec 6 states PD 1586 established the Environmental Impact Statement System. "
            "(a) is energy policy. (c) is solid-waste legislation. (d) is a foreign statute."
        ),
    },
    "lo7-06": {
        "expl": (
            'Correct (b): Lec 5.4 gives the short title "Ecological Solid Waste Management Act of 2000" for RA 9003. '
            "(a) is RA 6969. (c) is the Clean Air Act. (d) is the Renewable Energy Act."
        ),
    },
    "lo7-08": {
        "text": "Which policy declaration for RA 9003 is summarized in Lec 5.4?",
        "expl": (
            "Correct (b): Lec 5.4 frames RA 9003 as providing a legal framework for systematic, "
            "comprehensive ecological solid-waste management protecting health and environment. "
            "(a)/(c)/(d) caricature goals not stated on the slides."
        ),
    },
    "lo7-01": {
        "expl": (
            "Correct (c): Lec 5.4 treats waste as anthropogenic discard status versus natural cycling. "
            "(a) confuses persistence with waste definition. (b) denies biodegradation. "
            "(d) narrows generators."
        ),
    },
}


def _primary_for(qid: str, lo: str) -> str:
    if qid in CLIMATE_IDS:
        return "CvSU ENGS 32 — Lec 5.5 Climate Change (PDF)"
    if qid in AIR_IDS:
        return "CvSU ENGS 32 — Lec 5.3 Air Pollution (PDF)"
    return PRIMARY_REF.get(lo, PRIMARY_REF["LO7"])


def _normalize_refs(qid: str, lo: str, refs: list[str]) -> list[str]:
    primary = _primary_for(qid, lo)
    kept: list[str] = []
    for r in refs:
        rs = r.strip()
        if not rs or rs == primary:
            continue
        if re.search(r"cvSU|ENGS 32|Lec\s*5\.|Lec\s*6|Lec\s*7", rs, re.I):
            if primary.lower() not in rs.lower():
                kept.append(rs)
            continue
        if EXTERNAL_ONLY.search(rs):
            kept.append(rs + " (optional cross-check)")
        else:
            kept.append(rs)
    return [primary] + kept


def _format_choices(choices: list[dict]) -> str:
    parts = []
    for c in choices:
        t = c["text"].replace("\\", "\\\\").replace('"', '\\"')
        parts.append(f'{{ltr:"{c["ltr"]}",text:"{t}"}}')
    return "[" + ",".join(parts) + "]"


def _apply_patch_line(line: str, qid: str) -> str:
    patch = PATCHES.get(qid)
    if not patch:
        return line

    if "text" in patch:
        line = re.sub(
            r'text:"[^"]*"',
            'text:"' + patch["text"].replace("\\", "\\\\").replace('"', '\\"') + '"',
            line,
            count=1,
        )
    if "choices" in patch:
        line = re.sub(r"choices:\[[^\]]*\]", "choices:" + _format_choices(patch["choices"]), line, count=1)
    if "ans" in patch and patch.get("type") != "tf":
        if isinstance(patch["ans"], str):
            line = re.sub(r'ans:"[a-d]"', f'ans:"{patch["ans"]}"', line, count=1)
    if patch.get("type") == "tf":
        line = re.sub(r"type:\s*\"?mcq\"?", "type:tf", line, count=1)
        line = re.sub(r"choices:\[[^\]]*\],?", "", line, count=1)
        ans_val = "true" if patch["ans"] else "false"
        line = re.sub(r"ans:(?:\"[a-d]\"|true|false)", f"ans:{ans_val}", line, count=1)
    if "lo" in patch:
        line = re.sub(r'lo:"[^"]+"', f'lo:"{patch["lo"]}"', line, count=1)
    if "expl" in patch:
        expl = patch["expl"].replace("\\", "\\\\").replace('"', '\\"')
        line = re.sub(r'expl:"[^"]*"', f'expl:"{expl}"', line, count=1)

    return line


def _normalize_refs_on_line(line: str) -> str:
    m_id = re.search(r'id:"([^"]+)"', line)
    m_lo = re.search(r'lo:"([^"]+)"', line)
    m_refs = re.search(r"refs:\[(.*?)\](?=,|\})", line)
    if not m_id or not m_lo or not m_refs:
        return line

    qid, lo = m_id.group(1), m_lo.group(1)
    raw = m_refs.group(1)
    refs: list[str] = []
    for part in re.findall(r'"([^"]*)"', raw):
        refs.append(part)
    if not refs and raw.strip():
        refs = [raw.strip().strip('"')]

    new_refs = _normalize_refs(qid, lo, refs)
    refs_js = ",".join(json.dumps(r) for r in new_refs)
    return line[: m_refs.start()] + f"refs:[{refs_js}]" + line[m_refs.end() :]


def _patch_json_line(line: str) -> str:
    """Normalize refs on JSON-formatted pollution questions."""
    if '"refs"' not in line:
        return line
    m_id = re.search(r'"id"\s*:\s*"([^"]+)"', line)
    m_lo = re.search(r'"lo"\s*:\s*"([^"]+)"', line)
    m_refs = re.search(r'"refs"\s*:\s*\[(.*?)\]', line)
    if not m_id or not m_lo or not m_refs:
        return line
    qid, lo = m_id.group(1), m_lo.group(1)
    refs = json.loads("[" + m_refs.group(1) + "]")
    new_refs = _normalize_refs(qid, lo, refs)
    refs_js = ",".join(json.dumps(r) for r in new_refs)
    return line[: m_refs.start()] + f'"refs":[{refs_js}]' + line[m_refs.end() :]


def main() -> None:
    raw = QUESTIONS.read_text(encoding="utf-8")
    header = """/**
 * ENGS 32 — Environmental Science Question Bank
 * Keyed answers are grounded in the provided CvSU lecture PDFs (see MATERIALS.md).
 * External statute links are optional cross-checks only when cited.
 */
"""
    raw = re.sub(r"/\*\*[\s\S]*?\*/\s*", "", raw, count=1)

    out_lines: list[str] = [header, "window.ENVS_QB = [\n"]
    in_bank = False
    in_essays = False
    for line in raw.splitlines():
        if "window.ENVS_QB" in line:
            in_bank = True
            continue
        if line.strip().startswith("window.ENVS_ESSAYS"):
            in_bank = False
            in_essays = True
            out_lines.append(line + "\n")
            continue
        if in_essays:
            out_lines.append(line + "\n")
            if line.strip() == "];":
                in_essays = False
            continue
        if not in_bank:
            continue
        if line.strip() == "];":
            out_lines.append(line + "\n")
            in_bank = False
            continue
        stripped = line.strip()
        if stripped.startswith("{") and "id" in stripped[:120]:
            m = re.search(r'id:"([^"]+)"', stripped) or re.search(r'"id"\s*:\s*"([^"]+)"', stripped)
            if m:
                qid = m.group(1)
                if stripped.startswith('{"'):
                    line = _patch_json_line(line)
                else:
                    line = _apply_patch_line(line, qid)
                    line = _normalize_refs_on_line(line)
        out_lines.append(line + "\n")

    QUESTIONS.write_text("".join(out_lines), encoding="utf-8")
    print(f"Updated {QUESTIONS}")


if __name__ == "__main__":
    main()
