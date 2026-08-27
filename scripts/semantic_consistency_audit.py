"""Audit containment, package-completion, and human-disposition semantics."""
from __future__ import annotations

import csv
import html
import re
import sys
import zipfile
from pathlib import Path

from pypdf import PdfReader

import audit_workbook

try:
    sys.stdout.reconfigure(encoding="utf-8")
except AttributeError:
    pass

ROOT = Path(__file__).resolve().parents[1]
DOCX = ROOT / "deliverables" / "NguyenQuangHuy_Day25_onepager.docx"
PDF = ROOT / "deliverables" / "NguyenQuangHuy_Day25_onepager.pdf"
WORKBOOK = ROOT / "deliverables" / "NguyenQuangHuy_Day25_model.xlsx"
EVAL_CSV = ROOT / "evidence" / "containment-eval.csv"


def docx_text(path: Path) -> str:
    with zipfile.ZipFile(path) as archive:
        xml = archive.read("word/document.xml").decode("utf-8", errors="ignore")
    return " ".join(html.unescape(x) for x in re.findall(r"<w:t[^>]*>(.*?)</w:t>", xml))


def main() -> int:
    failures = []
    source_paths = [ROOT / "README.md", ROOT / "FINAL_AUDIT_REPORT.md", ROOT / "RECOVERY_GAP_ANALYSIS.md", ROOT / "SUBMISSION_MANIFEST.md", ROOT / "templates" / "SEARCH_LOG.md"]
    source_paths += sorted((ROOT / "evidence").glob("*.md")) + sorted((ROOT / "evidence").glob("*.csv"))
    texts = {path: path.read_text(encoding="utf-8", errors="ignore") for path in source_paths if path.exists()}
    texts[DOCX] = docx_text(DOCX)
    texts[PDF] = "\n".join(page.extract_text() or "" for page in PdfReader(str(PDF)).pages)
    sheets_for_text = audit_workbook.read_book(WORKBOOK)
    texts[WORKBOOK] = "\n".join(str(cell.get("value") or "") for sheet in sheets_for_text.values() for cell in sheet.values())
    combined = "\n".join(texts.values())
    lower = combined.lower()

    bad_mislabels = [
        r"(?:80(?:\.0)?%|4/5)\s+autonomous(?:\s+containment)?",
        r"autonomous\s+(?:containment|completion)(?:\s+rate)?\s*(?:is|=|:)\s*80(?:\.0)?%",
        r"20(?:\.0)?%\s+(?:commercial\s+)?package completion",
        r"(?:commercial\s+)?package completion(?:\s+rate)?\s*(?:is|=|:)\s*20(?:\.0)?%",
    ]
    mislabels = [pattern for pattern in bad_mislabels if re.search(pattern, lower)]
    print(f"SEMANTIC CHECK - no 80/20 containment mislabeling: {'PASS' if not mislabels else 'FAIL'}")
    if mislabels:
        failures.append("mislabeling")

    canonical = {
        "commercial package completion": "80.0%",
        "autonomous containment": "20.0%",
        "human-review / escalation": "80.0%",
        "grounding failure": "20.0%",
    }
    canonical_ok = True
    for phrase, expected in canonical.items():
        ok = phrase in lower and expected.lower() in lower
        print(f"SEMANTIC CHECK - {phrase}: {'PASS' if ok else 'FAIL'} ({expected})")
        canonical_ok = canonical_ok and ok
    if not canonical_ok:
        failures.append("canonical-rates")

    job_definition_ok = (
        "one completed grounded investigation package" in lower
        and "final disposition" in lower
        and ("customer owns final disposition" in lower or "customer-owned" in lower or "customer final disposition remains" in lower)
        and "autonomous completion" in lower
    )
    print(f"SEMANTIC CHECK - commercial job definition and human disposition boundary: {'PASS' if job_definition_ok else 'FAIL'}")
    if not job_definition_ok:
        failures.append("job-definition")

    sheets = sheets_for_text
    cost_formula = audit_workbook.formula(sheets, "1_Cost_Job", "B66") or ""
    denominator_ok = "B11" in cost_formula and "B9" not in cost_formula
    pricing_formula = audit_workbook.formula(sheets, "2_Pricing", "B33") or ""
    pricing_label = str(audit_workbook.val(sheets, "2_Pricing", "A33") or "").lower()
    economic_semantics_ok = "containment" in pricing_label and "B19" in pricing_formula and float(audit_workbook.val(sheets, "2_Pricing", "B33")) < float(audit_workbook.val(sheets, "1_Cost_Job", "B10"))
    print(f"FORMULA CHECK - Cost/Job uses autonomous-job denominator B11: {'PASS' if denominator_ok else 'FAIL'}")
    print(f"FORMULA CHECK - B33 is autonomous-containment breakeven, not package completion: {'PASS' if economic_semantics_ok else 'FAIL'}")
    if not denominator_ok: failures.append("denominator")
    if not economic_semantics_ok: failures.append("breakeven-semantics")

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
    if failures:
        print("FAILURES: " + ", ".join(failures))
    return 0 if not failures else 1


if __name__ == "__main__":
    raise SystemExit(main())
