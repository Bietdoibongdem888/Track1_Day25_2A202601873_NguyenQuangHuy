"""Aggregate Day25 automated checks without overstating subjective rubric quality."""
from __future__ import annotations

import subprocess
import sys
from pathlib import Path


def main() -> int:
    root = Path(__file__).resolve().parents[1]
    commands = [
        [sys.executable, str(root / "scripts" / "audit_workbook.py")],
        [sys.executable, str(root / "scripts" / "audit_onepager.py")],
        [sys.executable, str(root / "scripts" / "crosscheck_numbers.py")],
        [sys.executable, str(root / "scripts" / "semantic_consistency_audit.py")],
    ]
    statuses = []
    for command in commands:
        result = subprocess.run(command, cwd=root, text=True, capture_output=True)
        print(result.stdout, end="")
        if result.stderr: print(result.stderr, end="")
        statuses.append(result.returncode == 0)
    required = [
        root / "deliverables" / "NguyenQuangHuy_Day25_model.xlsx",
        root / "deliverables" / "NguyenQuangHuy_Day25_onepager.docx",
        root / "deliverables" / "NguyenQuangHuy_Day25_onepager.pdf",
        root / "README.md",
        root / "RECOVERY_GAP_ANALYSIS.md",
        root / "SUBMISSION_MANIFEST.md",
        root / "evidence" / "product-selection.md",
        root / "evidence" / "eval-evidence.md",
        root / "evidence" / "containment-eval.csv",
        root / "evidence" / "risk-evidence.md",
        root / "evidence" / "evidence-pack.md",
        root / "evidence" / "onepager-traceability.md",
        root / "templates" / "SEARCH_LOG.md",
        root / "FINAL_AUDIT_REPORT.md",
    ]
    required.extend(sorted((root / "evidence").glob("*.md")))
    required.extend(sorted((root / "evidence").glob("*.csv")))
    required.extend(sorted((root / "qa" / "workbook").glob("*.png")))
    required.extend(sorted((root / "qa" / "onepager").glob("*.png")))
    artifacts_ok = all(p.exists() and p.stat().st_size > 0 for p in required)
    print(f"AUTOMATED CHECK - required final artifacts: {'PASS' if artifacts_ok else 'FAIL'}")
    print(f"LOCAL AUTOMATED AUDITS: {'PASS' if all(statuses) else 'FAIL'}")
    print(f"COMMITTED QA EVIDENCE: {'PRESENT' if artifacts_ok else 'MISSING'}")
    print("GITHUB ACTIONS: NOT CONFIGURED / NOT REQUIRED BY LAB")
    print(f"MANUAL RUBRIC CHECK - official Day28 template: BLOCKED / disclosed")
    print(f"MANUAL RUBRIC CHECK - pilot evidence: MISSING EVIDENCE / plan supplied")
    print(f"VISUAL QA - Excel: inspect qa/workbook/*.png")
    print(f"VISUAL QA - PDF: inspect qa/onepager/page-*.png")
    ok = all(statuses) and artifacts_ok
    print(f"FINAL GATE AUTOMATED STATUS: {'PASS' if ok else 'FAIL'}")
    return 0 if ok else 1


if __name__ == "__main__":
    raise SystemExit(main())
