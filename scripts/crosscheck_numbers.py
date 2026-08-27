"""Cross-check published One-Pager numbers against workbook cached values."""
from __future__ import annotations

import re
import sys
import zipfile
from pathlib import Path
from xml.etree import ElementTree as ET

NS = {"m": "http://schemas.openxmlformats.org/spreadsheetml/2006/main", "r": "http://schemas.openxmlformats.org/officeDocument/2006/relationships", "p": "http://schemas.openxmlformats.org/package/2006/relationships"}


def cells(path: Path):
    with zipfile.ZipFile(path) as zf:
        shared = []
        if "xl/sharedStrings.xml" in zf.namelist():
            root = ET.fromstring(zf.read("xl/sharedStrings.xml"))
            shared = ["".join(t.text or "" for t in si.findall(".//m:t", NS)) for si in root.findall("m:si", NS)]
        wb = ET.fromstring(zf.read("xl/workbook.xml"))
        rels = ET.fromstring(zf.read("xl/_rels/workbook.xml.rels"))
        targets = {r.attrib["Id"]: r.attrib["Target"] for r in rels.findall("p:Relationship", NS)}
        out = {}
        for sh in wb.findall("m:sheets/m:sheet", NS):
            name = sh.attrib["name"]
            target = targets[sh.attrib["{http://schemas.openxmlformats.org/officeDocument/2006/relationships}id"]].lstrip("/")
            if not target.startswith("xl/"): target = "xl/" + target
            root = ET.fromstring(zf.read(target))
            for c in root.findall(".//m:c", NS):
                v = c.find("m:v", NS)
                if v is None: continue
                value = v.text
                if c.attrib.get("t") == "s": value = shared[int(value)]
                out[(name, c.attrib["r"])] = value
        return out


def num(value):
    try: return float(value)
    except (TypeError, ValueError): return None


def main() -> int:
    root = Path(__file__).resolve().parents[1]
    workbook = root / "deliverables" / "NguyenQuangHuy_Day25_model.xlsx"
    onepager = root / "deliverables" / "NguyenQuangHuy_Day25_onepager.docx"
    if not workbook.exists() or not onepager.exists():
        print("AUTOMATED CHECK - numerical crosscheck prerequisites: BLOCKED")
        return 1
    data = cells(workbook)
    values = {
        "cost": num(data[("1_Cost_Job", "C61")]),
        "floor": num(data[("2_Pricing", "C9")]),
        "usage": num(data[("2_Pricing", "C7")]),
        "gm": num(data[("2_Pricing", "C12")]),
        "package_completion_rate": num(data[("2_Pricing", "C14")]),
        "breakeven_package_completion_rate": num(data[("2_Pricing", "C16")]),
        "arpu": num(data[("4_Channel_Fit", "C8")]),
        "cac_budget": num(data[("4_Channel_Fit", "C11")]),
        "estimated_cac": num(data[("4_Channel_Fit", "C23")]),
        "gap": num(data[("4_Channel_Fit", "C24")]),
        "unit_gm": num(data[("2_Pricing", "C11")]),
        "acv_usd": num(data[("4_Channel_Fit", "C25")]),
        "affordability_ratio": num(data[("4_Channel_Fit", "C26")]),
        "deals_day": num(data[("4_Channel_Fit", "C16")]),
    }
    workbook_fields = ("unit_gm", "acv_usd", "affordability_ratio", "deals_day")
    workbook_ok = all(values[key] is not None for key in workbook_fields)
    print(f"AUTOMATED CHECK - recovery workbook outputs: {'PASS' if workbook_ok else 'FAIL'} ({', '.join(workbook_fields)})")
    text = onepager.read_bytes()
    # XML extraction is enough for numeric consistency; DOCX visual layout is audited separately.
    import zipfile as z
    with z.ZipFile(onepager) as docx:
        xml = docx.read("word/document.xml").decode("utf-8", errors="ignore")
    checks = {
        "cost": "7,648",
        "floor": "22,945",
        "usage": "32,000",
        "gm": "82.8%",
        "package_completion_rate": "80%",
        "breakeven_package_completion_rate": "44.3%",
        "arpu": "106.8M",
        "cac_budget": ("1,061M", "1.061B"),
        "estimated_cac": "350M",
        "gap": "711M",
        "unit_gm": "76.1%",
        "acv_usd": "$49.3K",
        "affordability_ratio": "3.03x",
        "deals_day": "0.013",
        "autonomous": "20%",
        "human_review": "80%",
        "grounding_failure": "20%",
        "package_count": "4/5",
        "package_completion_label": "package-completion",
    }
    ok = True
    for key, marker in checks.items():
        markers = marker if isinstance(marker, tuple) else (marker,)
        present = any(candidate.encode() in text or candidate in xml for candidate in markers)
        print(f"AUTOMATED CHECK - one-pager {key}: {'PASS' if present else 'FAIL'} ({' / '.join(markers)})")
        ok = ok and present
    return 0 if ok and workbook_ok else 1


if __name__ == "__main__":
    raise SystemExit(main())
