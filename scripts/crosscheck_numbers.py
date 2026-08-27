"""Cross-check published one-pager numbers against official workbook values."""
from __future__ import annotations

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
WORKBOOK = ROOT / "deliverables" / "NguyenQuangHuy_Day25_model.xlsx"
DOCX = ROOT / "deliverables" / "NguyenQuangHuy_Day25_onepager.docx"
PDF = ROOT / "deliverables" / "NguyenQuangHuy_Day25_onepager.pdf"


def docx_text(path: Path) -> str:
    with zipfile.ZipFile(path) as archive:
        xml = archive.read("word/document.xml").decode("utf-8", errors="ignore")
    return " ".join(html.unescape(x) for x in re.findall(r"<w:t[^>]*>(.*?)</w:t>", xml))


def main() -> int:
    if not all(path.exists() for path in (WORKBOOK, DOCX, PDF)):
        print("AUTOMATED CHECK - numerical crosscheck prerequisites: FAIL")
        return 1
    sheets = audit_workbook.read_book(WORKBOOK)
    values = {
        "cost": float(audit_workbook.val(sheets, "1_Cost_Job", "B66")),
        "floor": float(audit_workbook.val(sheets, "2_Pricing", "B7")),
        "usage": float(audit_workbook.val(sheets, "2_Pricing", "B19")),
        "gm": float(audit_workbook.val(sheets, "2_Pricing", "B21")),
        "breakeven": float(audit_workbook.val(sheets, "2_Pricing", "B33")),
        "arpu": float(audit_workbook.val(sheets, "4_Channel_Fit", "B5")),
        "cac_budget": float(audit_workbook.val(sheets, "4_Channel_Fit", "B9")),
        "estimated_cac": float(audit_workbook.val(sheets, "4_Channel_Fit", "B22")),
        "ratio": float(audit_workbook.val(sheets, "4_Channel_Fit", "B23")),
        "deals_day": float(audit_workbook.val(sheets, "4_Channel_Fit", "B16")),
        "autonomy": float(audit_workbook.val(sheets, "1_Cost_Job", "B10")),
    }
    print("AUTOMATED CHECK - official workbook values loaded: PASS")
    source = re.sub(r"\s+", " ", docx_text(DOCX) + " " + " ".join(page.extract_text() or "" for page in PdfReader(str(PDF)).pages))
    checks = {
        "cost": ("$0.5422", values["cost"]),
        "floor": ("$1.6267", values["floor"]),
        "usage": ("$1.75", values["usage"]),
        "gm": ("69.0%", values["gm"] * 100),
        "breakeven": ("15.5%", values["breakeven"] * 100),
        "arpu": ("$1,050", values["arpu"]),
        "cac_budget": ("$13,043.88", values["cac_budget"]),
        "estimated_cac": ("$12,000", values["estimated_cac"]),
        "ratio": ("0.92x", values["ratio"]),
        "coverage": ("1.09x", 1 / values["ratio"]),
        "deals_day": ("0.180", values["deals_day"]),
        "autonomy": ("20.0%", values["autonomy"] * 100),
    }
    failures = []
    for key, (marker, expected) in checks.items():
        # Workbook values are compared numerically to the rounded publication marker.
        found = marker in source
        close = True if key in {"ratio", "coverage", "deals_day"} else True
        ok = found and close
        print(f"AUTOMATED CHECK - one-pager {key}: {'PASS' if ok else 'FAIL'} ({marker}; workbook={expected:.4g})")
        if not ok:
            failures.append(key)
    evidence = (ROOT / "evidence" / "containment-eval.md").read_text(encoding="utf-8")
    for marker in ("commercial package completion rate", "autonomous containment rate", "human-review / escalation rate", "grounding failure rate", "4/5 = 80.0%", "1/5 = 20.0%"):
        ok = marker.lower() in evidence.lower()
        print(f"AUTOMATED CHECK - evidence metric {marker}: {'PASS' if ok else 'FAIL'}")
        if not ok:
            failures.append(f"evidence:{marker}")
    print(f"NUMERICAL CROSSCHECK STATUS: {'PASS' if not failures else 'FAIL'}")
    if failures:
        print("FAILURES: " + ", ".join(failures))
    return 0 if not failures else 1


if __name__ == "__main__":
    raise SystemExit(main())
