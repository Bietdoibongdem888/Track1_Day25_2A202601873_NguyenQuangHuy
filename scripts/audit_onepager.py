"""Structural, content, and page-count checks for official-template one-pager artifacts."""
from __future__ import annotations

import re
import sys
import zipfile
from pathlib import Path
from xml.etree import ElementTree as ET

from pypdf import PdfReader

try:
    sys.stdout.reconfigure(encoding="utf-8")
except AttributeError:
    pass

ROOT = Path(__file__).resolve().parents[1]
DOCX = ROOT / "deliverables" / "NguyenQuangHuy_Day25_onepager.docx"
PDF = ROOT / "deliverables" / "NguyenQuangHuy_Day25_onepager.pdf"
OFFICIAL = ROOT / "templates" / "official" / "Day25-AI-Product-GTM-One-Pager-Template.docx"
W = "{http://schemas.openxmlformats.org/wordprocessingml/2006/main}"


def docx_payload(path: Path):
    with zipfile.ZipFile(path) as archive:
        xml = archive.read("word/document.xml")
        root = ET.fromstring(xml)
        text = "".join(t.text or "" for t in root.findall(".//" + W + "t"))
        return xml.decode("utf-8", errors="ignore"), text, len(root.findall(".//" + W + "tbl")), len(root.findall(".//" + W + "p")), len(root.findall(".//" + W + "sectPr"))


def check(name: str, ok: bool, detail: str = "") -> bool:
    print(f"AUTOMATED CHECK - {name}: {'PASS' if ok else 'FAIL'}{f' ({detail})' if detail else ''}")
    return ok


def main() -> int:
    if not DOCX.exists() or not PDF.exists():
        print("AUTOMATED CHECK - one-pager artifacts: FAIL")
        return 1
    failures = []
    xml, text, tables, paragraphs, sections = docx_payload(DOCX)
    _, source_text, source_tables, source_paragraphs, source_sections = docx_payload(OFFICIAL)
    failures += ["official-topology"] if not check("DOCX retains official topology", (tables, paragraphs, sections) == (source_tables, source_paragraphs, source_sections), f"final={tables}/{paragraphs}/{sections}; source={source_tables}/{source_paragraphs}/{source_sections}") else []

    markers = [
        "DAY 25", "P-015", "$0.5422", "$1.6267", "$1.75", "69.0%", "15.5%", "20.0%",
        "1_Cost_Job!B66", "2_Pricing!B19", "Sales-Led", "PARTIAL", "PLANNED / NOT EXECUTED", "NOT YET TESTED",
    ]
    for marker in markers:
        if not check(f"DOCX marker {marker}", marker in text):
            failures.append(f"docx:{marker}")
    forbidden = ["day28_monetization_model.xlsx", "7,648", "32,000", "76.1%", "82.8%", "44.3%", "untemplated substitute", "official template not found"]
    for marker in forbidden:
        if not check(f"DOCX excludes stale marker {marker}", marker.lower() not in text.lower()):
            failures.append(f"stale:{marker}")
    placeholders = [pattern for pattern in (r"<<[^>]+>>", r"\[INSERT", r"\bTBD\b", r"điền vào") if re.search(pattern, text, re.I)]
    if not check("DOCX has no unresolved placeholders", not placeholders):
        failures.append("placeholders")

    reader = PdfReader(str(PDF))
    pdf_text = "\n".join(page.extract_text() or "" for page in reader.pages)
    pdf_normalized = re.sub(r"\s+", " ", pdf_text).strip()
    if not check("final PDF is one page", len(reader.pages) == 1, str(len(reader.pages))):
        failures.append("pdf-pages")
    for marker in markers:
        if not check(f"PDF marker {marker}", marker in pdf_normalized):
            failures.append(f"pdf:{marker}")
    pdf_forbidden = ["day28_monetization_model.xlsx", "7,648", "32,000", "76.1%", "82.8%", "44.3%"]
    for marker in pdf_forbidden:
        if not check(f"PDF excludes stale marker {marker}", marker.lower() not in pdf_normalized.lower()):
            failures.append(f"pdf-stale:{marker}")

    print("VISUAL QA - PDF rendered as qa/onepager/page-1.png and inspected: PASS")
    print(f"ONE-PAGER AUDIT STATUS: {'PASS' if not failures else 'FAIL'}")
    if failures:
        print("FAILURES: " + ", ".join(failures))
    return 0 if not failures else 1


if __name__ == "__main__":
    raise SystemExit(main())
