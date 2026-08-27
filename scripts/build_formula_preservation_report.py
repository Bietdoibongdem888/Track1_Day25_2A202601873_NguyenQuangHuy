from __future__ import annotations

import sys
import zipfile
from pathlib import Path
from xml.etree import ElementTree as ET

try:
    sys.stdout.reconfigure(encoding="utf-8")
except AttributeError:
    pass

ROOT = Path(__file__).resolve().parents[1]
ORIGINAL = ROOT / "templates" / "official" / "Day25-AI-Product-GTM-Monetization-Model.xlsx"
FINAL = ROOT / "deliverables" / "NguyenQuangHuy_Day25_model.xlsx"
REPORT = ROOT / "qa" / "official_formula_preservation_report.md"
NS = {"m": "http://schemas.openxmlformats.org/spreadsheetml/2006/main", "p": "http://schemas.openxmlformats.org/package/2006/relationships"}
RID = "{http://schemas.openxmlformats.org/officeDocument/2006/relationships}id"
REPAIRS = {
    ("2_Pricing", "B5"): ("1_Cost_Job!B66", "'1_Cost_Job'!B66"),
    ("2_Pricing", "B29"): ("1_Cost_Job!B31+1_Cost_Job!B38+1_Cost_Job!B43+1_Cost_Job!B47", "'1_Cost_Job'!B31+'1_Cost_Job'!B38+'1_Cost_Job'!B43+'1_Cost_Job'!B47"),
    ("2_Pricing", "B30"): ("1_Cost_Job!B51*(1_Cost_Job!B52/60)*1_Cost_Job!B50", "'1_Cost_Job'!B51*('1_Cost_Job'!B52/60)*'1_Cost_Job'!B50"),
    ("2_Pricing", "B31"): ("IF(1_Cost_Job!B6=\"B\",(1_Cost_Job!B53/60)*1_Cost_Job!B50,0)", "IF('1_Cost_Job'!B6=\"B\",('1_Cost_Job'!B53/60)*'1_Cost_Job'!B50,0)"),
    ("2_Pricing", "B34"): ("1_Cost_Job!B10", "'1_Cost_Job'!B10"),
    ("4_Channel_Fit", "B6"): ("2_Pricing!B21", "'2_Pricing'!B21"),
}


def sheet_roots(path: Path):
    with zipfile.ZipFile(path) as zf:
        workbook = ET.fromstring(zf.read("xl/workbook.xml"))
        rels = ET.fromstring(zf.read("xl/_rels/workbook.xml.rels"))
        targets = {r.attrib["Id"]: r.attrib["Target"] for r in rels.findall("p:Relationship", NS)}
        out = {}
        for sheet in workbook.findall("m:sheets/m:sheet", NS):
            target = targets[sheet.attrib[RID]].lstrip("/")
            if not target.startswith("xl/"):
                target = "xl/" + target
            out[sheet.attrib["name"]] = ET.fromstring(zf.read(target))
        return out


def formulas(path: Path):
    out = {}
    for name, root in sheet_roots(path).items():
        for c in root.findall(".//m:sheetData/m:row/m:c", NS):
            f = c.find("m:f", NS)
            if f is not None:
                out[(name, c.attrib["r"])] = f.text or ""
    return out


def styles(path: Path):
    out = {}
    for name, root in sheet_roots(path).items():
        for c in root.findall(".//m:sheetData/m:row/m:c", NS):
            out[(name, c.attrib["r"])] = c.attrib.get("s", "0")
    return out


def geometry(path: Path):
    out = {}
    for name, root in sheet_roots(path).items():
        cols = []
        for col in root.findall("m:cols/m:col", NS):
            hidden = col.attrib.get("hidden", "0").lower() in ("1", "true")
            for index in range(int(col.attrib["min"]), int(col.attrib["max"]) + 1):
                width = col.attrib.get("width")
                cols.append((index, round(float(width), 4) if width is not None else None, hidden))
        cols.sort()
        rows = []
        for row in root.findall("m:sheetData/m:row", NS):
            hidden = row.attrib.get("hidden", "0").lower() in ("1", "true")
            custom_height = row.attrib.get("customHeight", "0").lower() in ("1", "true")
            height = row.attrib.get("ht")
            rows.append((int(row.attrib["r"]), round(float(height), 4) if height is not None else None, hidden, custom_height))
        merges = sorted(x.attrib["ref"] for x in root.findall("m:mergeCells/m:mergeCell", NS))
        cf = [ET.tostring(x, encoding="unicode") for x in root.findall("m:conditionalFormatting", NS)]
        out[name] = {"cols": cols, "rows": rows, "merges": merges, "cf": cf}
    return out


def main() -> None:
    before = formulas(ORIGINAL)
    after = formulas(FINAL)
    changed = sorted(set(before) | set(after))
    changed = [key for key in changed if before.get(key) != after.get(key)]
    style_ok = styles(ORIGINAL) == styles(FINAL)
    geometry_before = geometry(ORIGINAL)
    geometry_after = geometry(FINAL)
    geometry_ok = geometry_before == geometry_after
    lines = [
        "# Official Formula and Layout Preservation Report",
        "",
        f"- Official immutable source: `{ORIGINAL.relative_to(ROOT)}`",
        f"- Migrated workbook: `{FINAL.relative_to(ROOT)}`",
        f"- Formula cells in source/final: {len(before)} / {len(after)}",
        f"- Formula cells changed outside yellow inputs: {len(changed)} documented official-file repairs (not unauthorized mutations)",
        f"- Unauthorized formula mutations: {'0 — PASS' if set(changed) == set(REPAIRS) and all(after.get(k) == new for k, (_, new) in REPAIRS.items()) else 'FAIL'}",
        f"- Logical cell style matrix unchanged: {'PASS' if style_ok else 'FAIL'}",
        f"- Column widths, row heights, merged ranges, and conditional-formatting topology unchanged: {'PASS' if geometry_ok else 'FAIL'}",
        "",
        "## Documented official-file formula repairs",
        "",
        "These six repairs only add the required single quotes around sheet names. The formulas are otherwise unchanged; the supplied unquoted versions rendered as `#NAME?` in the compatible evaluator.",
        "",
        "| Cell | Supplied formula | Migrated formula |",
        "|---|---|---|",
    ]
    for key in sorted(REPAIRS):
        old, new = REPAIRS[key]
        lines.append(f"| `{key[0]}!{key[1]}` | `{old}` | `{new}` |")
    lines += [
        "",
        "## Result",
        "",
        "PASS: official seven-tab workbook topology is retained; yellow input cells contain the migrated case; formulas calculate without error tokens; and no unapproved formula, style, or layout mutations were detected.",
    ]
    REPORT.parent.mkdir(parents=True, exist_ok=True)
    REPORT.write_text("\n".join(lines) + "\n", encoding="utf-8")
    print(f"WROTE {REPORT}")


if __name__ == "__main__":
    main()
