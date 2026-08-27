"""Structural and page-count checks for the editable one-pager and final PDF."""
from __future__ import annotations

import sys
import zipfile
from pathlib import Path

from pypdf import PdfReader


def main() -> int:
    root = Path(__file__).resolve().parents[1]
    docx = root / "deliverables" / "NguyenQuangHuy_Day25_onepager.docx"
    pdf = root / "deliverables" / "NguyenQuangHuy_Day25_onepager.pdf"
    if not docx.exists() or not pdf.exists():
        print("AUTOMATED CHECK - one-pager artifacts: FAIL")
        return 1
    with zipfile.ZipFile(docx) as archive:
        xml = archive.read("word/document.xml").decode("utf-8", errors="ignore")
    reader = PdfReader(str(pdf))
    pdf_text = "\n".join(page.extract_text() or "" for page in reader.pages)
    markers = ["P-015", "7,648", "32,000", "76.1%", "82.8%", "44.3%", "Sales-Led", "PARTIAL", "autonomous containment", "human-review", "package-completion"]
    ok = True
    for marker in markers:
        present = marker in xml or marker in pdf_text
        print(f"AUTOMATED CHECK - one-pager marker {marker}: {'PASS' if present else 'FAIL'}")
        ok = ok and present
    pages_ok = len(reader.pages) == 1
    print(f"AUTOMATED CHECK - final PDF page count: {'PASS' if pages_ok else 'FAIL'} ({len(reader.pages)})")
    return 0 if ok and pages_ok else 1


if __name__ == "__main__":
    raise SystemExit(main())
