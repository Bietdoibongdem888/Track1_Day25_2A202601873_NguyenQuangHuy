"""Aggregate Day25 official-template checks and required-artifact checks."""
from __future__ import annotations

import re
import subprocess
import sys
from pathlib import Path

try:
    sys.stdout.reconfigure(encoding="utf-8")
except AttributeError:
    pass

ROOT = Path(__file__).resolve().parents[1]


def secret_scan() -> bool:
    patterns = [
        re.compile(r"sk-[A-Za-z0-9]{20,}"),
        re.compile(r"ghp_[A-Za-z0-9]{20,}"),
        re.compile(r"xox[baprs]-[A-Za-z0-9-]{20,}"),
        re.compile(r"-----BEGIN (?:RSA |EC |OPENSSH )?PRIVATE KEY-----"),
    ]
    tracked = subprocess.run(["git", "ls-files"], cwd=ROOT, text=True, capture_output=True, check=False)
    if tracked.returncode != 0:
        return False
    hits = []
    for item in tracked.stdout.splitlines():
        path = ROOT / item
        if not path.is_file() or path.suffix.lower() in {".png", ".xlsx", ".docx", ".pdf"}:
            continue
        text = path.read_text(encoding="utf-8", errors="ignore")
        if any(pattern.search(text) for pattern in patterns):
            hits.append(item)
    print(f"AUTOMATED CHECK - tracked secret patterns: {'PASS' if not hits else 'FAIL'}")
    if hits:
        print("  " + ", ".join(hits))
    return not hits


def main() -> int:
    commands = [
        [sys.executable, str(ROOT / "scripts" / "audit_workbook.py")],
        [sys.executable, str(ROOT / "scripts" / "audit_onepager.py")],
        [sys.executable, str(ROOT / "scripts" / "crosscheck_numbers.py")],
        [sys.executable, str(ROOT / "scripts" / "semantic_consistency_audit.py")],
    ]
    statuses = []
    for command in commands:
        result = subprocess.run(command, cwd=ROOT, text=True, capture_output=True)
        print(result.stdout, end="")
        if result.stderr:
            print(result.stderr, end="")
        statuses.append(result.returncode == 0)

    required = [
        ROOT / "deliverables" / "NguyenQuangHuy_Day25_model.xlsx",
        ROOT / "deliverables" / "NguyenQuangHuy_Day25_onepager.docx",
        ROOT / "deliverables" / "NguyenQuangHuy_Day25_onepager.pdf",
        ROOT / "README.md",
        ROOT / "FINAL_AUDIT_REPORT.md",
        ROOT / "RECOVERY_GAP_ANALYSIS.md",
        ROOT / "SUBMISSION_MANIFEST.md",
        ROOT / "templates" / "SEARCH_LOG.md",
        ROOT / "templates" / "official" / "Day25-AI-Product-GTM-Monetization-Model.xlsx",
        ROOT / "templates" / "official" / "Day25-AI-Product-GTM-One-Pager-Template.docx",
        ROOT / "qa" / "official_formula_preservation_report.md",
        ROOT / "evidence" / "containment-eval.csv",
        ROOT / "evidence" / "containment-eval.md",
        ROOT / "evidence" / "onepager-traceability.md",
        ROOT / "evidence" / "pricing-sources.md",
        ROOT / "evidence" / "value-metric-benchmarks.md",
    ]
    required += sorted((ROOT / "evidence").glob("*.md"))
    required += sorted((ROOT / "evidence").glob("*.csv"))
    required += sorted((ROOT / "qa" / "official_workbook").glob("*.png"))
    required += sorted((ROOT / "qa" / "onepager").glob("page-*.png"))
    artifacts_ok = all(path.exists() and path.stat().st_size > 0 for path in required)
    print(f"AUTOMATED CHECK - required official final artifacts: {'PASS' if artifacts_ok else 'FAIL'}")
    secrets_ok = secret_scan()
    diff_check = subprocess.run(["git", "diff", "--check"], cwd=ROOT, text=True, capture_output=True, check=False)
    diff_ok = diff_check.returncode == 0
    print(f"AUTOMATED CHECK - git diff --check: {'PASS' if diff_ok else 'FAIL'}")
    print("MANUAL LIMITATION - pilot evidence: PLANNED / NOT EXECUTED / MISSING EVIDENCE")
    print("MANUAL LIMITATION - stranger test: NOT YET TESTED")
    print("VISUAL QA - Excel: inspect qa/official_workbook/*.png")
    print("VISUAL QA - PDF: inspect qa/onepager/page-1.png")
    ok = all(statuses) and artifacts_ok and secrets_ok and diff_ok
    print(f"FINAL GATE AUTOMATED STATUS: {'PASS' if ok else 'FAIL'}")
    return 0 if ok else 1


if __name__ == "__main__":
    raise SystemExit(main())
