"""Semantic and formula audit for Day25 completion versus containment terminology."""
from __future__ import annotations

import csv
import html
import re
import sys
import zipfile
from pathlib import Path

from pypdf import PdfReader

import audit_workbook


ROOT = Path(__file__).resolve().parents[1]
DOCX = ROOT / "deliverables" / "NguyenQuangHuy_Day25_onepager.docx"
PDF = ROOT / "deliverables" / "NguyenQuangHuy_Day25_onepager.pdf"
WORKBOOK = ROOT / "deliverables" / "NguyenQuangHuy_Day25_model.xlsx"
EVAL_CSV = ROOT / "evidence" / "containment-eval.csv"

BAD_LABELS = [
    re.compile(r"commercial completion\s*/\s*containment", re.I),
    re.compile(r"completion\s*/\s*containment", re.I),
    re.compile(r"containment proxy", re.I),
    re.compile(r"breakeven containment", re.I),
    re.compile(r"required containment", re.I),
    re.compile(r"containment error", re.I),
    re.compile(r"current\s*/\s*evaluated containment", re.I),
    re.compile(r"customer containment", re.I),
    re.compile(r"production containment", re.I),
]


def docx_text(path: Path) -> str:
    with zipfile.ZipFile(path) as archive:
        xml = archive.read("word/document.xml").decode("utf-8", errors="ignore")
    return " ".join(html.unescape(x) for x in re.findall(r"<w:t[^>]*>(.*?)</w:t>", xml))


def pdf_text(path: Path) -> str:
    reader = PdfReader(str(path))
    return "\n".join(page.extract_text() or "" for page in reader.pages)


def text_sources() -> dict[Path, str]:
    paths = [ROOT / "README.md", ROOT / "FINAL_AUDIT_REPORT.md", ROOT / "RECOVERY_GAP_ANALYSIS.md"]
    paths.extend(sorted((ROOT / "evidence").glob("*.md")))
    paths.extend(sorted((ROOT / "evidence").glob("*.csv")))
    paths.extend(sorted((ROOT / "scripts").glob("*.py")))
    paths.extend(sorted((ROOT / "scripts").glob("*.mjs")))
    paths = [p for p in paths if p.name != "semantic_consistency_audit.py"]
    return {p: p.read_text(encoding="utf-8", errors="ignore") for p in paths}


def main() -> int:
    failures: list[str] = []
    sources = text_sources()
    sources[DOCX] = docx_text(DOCX)
    sources[PDF] = pdf_text(PDF)

    legacy_hits = []
    for path, content in sources.items():
        for pattern in BAD_LABELS:
            if pattern.search(content):
                legacy_hits.append(f"{path.name}: {pattern.pattern}")
    print(f"SEMANTIC CHECK - forbidden legacy labels: {'PASS' if not legacy_hits else 'FAIL'}")
    if legacy_hits:
        failures.append("legacy-labels")
        for hit in legacy_hits:
            print(f"  {hit}")

    canonical = {
        "commercial package completion": "80%",
        "autonomous containment": "20%",
        "human-review/escalation": "80%",
        "grounding failure": "20%",
        "breakeven package-completion rate": "44.3%",
    }
    combined = "\n".join(sources.values()).lower()
    canonical_ok = True
    for phrase, expected in canonical.items():
        present = phrase in combined and expected.lower() in combined
        print(f"SEMANTIC CHECK - {phrase}: {'PASS' if present else 'FAIL'} ({expected})")
        canonical_ok = canonical_ok and present
    if not canonical_ok:
        failures.append("canonical-rates")

    sheets = audit_workbook.read_book(WORKBOOK)
    c14 = float(audit_workbook.val(sheets, "2_Pricing", "C14") or 0)
    c16 = float(audit_workbook.val(sheets, "2_Pricing", "C16") or 0)
    c17 = float(audit_workbook.val(sheets, "2_Pricing", "C17") or 0)
    c16_label = str(audit_workbook.val(sheets, "2_Pricing", "A16") or "")
    c16_formula = str(audit_workbook.formula(sheets, "2_Pricing", "C16") or "")
    formula_case_a = (
        "package-completion" in c16_label.lower()
        and "containment" not in c16_label.lower()
        and "'1_Cost_Job'!C6" in c16_formula
        and "'1_Cost_Job'!C29" in c16_formula
        and "'1_Cost_Job'!C40" in c16_formula
        and "'1_Cost_Job'!C43" in c16_formula
        and "'1_Cost_Job'!C45" in c16_formula
        and "C7" in c16_formula
        and "C8" in c16_formula
        and "C15" in c16_formula
    )
    values_ok = abs(c14 - 0.8) < 1e-9 and abs(c16 - 0.443176911976912) < 1e-9 and abs(c17 - (c14 - c16)) < 1e-9
    print(f"FORMULA CHECK - C16 solves Case A package-completion rate: {'PASS' if formula_case_a else 'FAIL'}")
    print(f"FORMULA CHECK - C14/C16/C17 values 80.0% / 44.3% / +35.7 pp: {'PASS' if values_ok else 'FAIL'}")
    if not formula_case_a or not values_ok:
        failures.append("formula-case-a")

    with EVAL_CSV.open(newline="", encoding="utf-8") as handle:
        rows = list(csv.DictReader(handle))
    counts = {
        "attempted": len(rows),
        "commercial": sum(row["completed_commercial_package"] == "True" for row in rows),
        "autonomous": sum(row["completed_autonomously"] == "True" for row in rows),
        "human_review": sum(row["human_intervention_required"] == "True" for row in rows),
        "grounding_failure": sum(row["grounding_evidence_condition"] == "FAIL" for row in rows),
    }
    expected_counts = {"attempted": 5, "commercial": 4, "autonomous": 1, "human_review": 4, "grounding_failure": 1}
    counts_ok = counts == expected_counts
    print(f"EVAL CHECK - case counts 5 / 4 / 1 / 4 / 1: {'PASS' if counts_ok else 'FAIL'} ({counts})")
    if not counts_ok:
        failures.append("eval-counts")

    print(f"SEMANTIC AUDIT STATUS: {'PASS' if not failures else 'FAIL'}")
    return 0 if not failures else 1


if __name__ == "__main__":
    raise SystemExit(main())
