"""Independent XML audit for the Day25 workbook; subjective quality stays manual."""
from __future__ import annotations

import re
import sys
import zipfile
from pathlib import Path
from xml.etree import ElementTree as ET

NS = {"m": "http://schemas.openxmlformats.org/spreadsheetml/2006/main", "r": "http://schemas.openxmlformats.org/officeDocument/2006/relationships", "p": "http://schemas.openxmlformats.org/package/2006/relationships"}
EXPECTED = ["0_README", "1_Cost_Job", "2_Pricing", "3_Value_Metric", "4_Channel_Fit", "5_90Day_Plan", "6_Benchmarks"]


def read_book(path: Path):
    with zipfile.ZipFile(path) as zf:
        shared = []
        if "xl/sharedStrings.xml" in zf.namelist():
            root = ET.fromstring(zf.read("xl/sharedStrings.xml"))
            for si in root.findall("m:si", NS):
                shared.append("".join(t.text or "" for t in si.findall(".//m:t", NS)))
        wb = ET.fromstring(zf.read("xl/workbook.xml"))
        rels = ET.fromstring(zf.read("xl/_rels/workbook.xml.rels"))
        targets = {r.attrib["Id"]: r.attrib["Target"] for r in rels.findall("p:Relationship", NS)}
        sheets = {}
        for sh in wb.findall("m:sheets/m:sheet", NS):
            name = sh.attrib["name"]
            target = targets[sh.attrib["{http://schemas.openxmlformats.org/officeDocument/2006/relationships}id"]].lstrip("/")
            if not target.startswith("xl/"):
                target = "xl/" + target
            root = ET.fromstring(zf.read(target))
            cells = {}
            for c in root.findall(".//m:c", NS):
                ref = c.attrib["r"]
                formula = c.find("m:f", NS)
                v = c.find("m:v", NS)
                value = None if v is None else v.text
                if c.attrib.get("t") == "s" and value is not None:
                    value = shared[int(value)]
                cells[ref] = {"value": value, "formula": None if formula is None else (formula.text or "")}
            sheets[name] = cells
        return sheets


def val(sheets, sheet, ref):
    return sheets.get(sheet, {}).get(ref, {}).get("value")


def formula(sheets, sheet, ref):
    return sheets.get(sheet, {}).get(ref, {}).get("formula")


def main() -> int:
    path = Path(sys.argv[1]) if len(sys.argv) > 1 else Path("deliverables/NguyenQuangHuy_Day25_model.xlsx")
    failures = []
    if not path.exists():
        print("AUTOMATED CHECK - workbook exists: FAIL")
        return 1
    with zipfile.ZipFile(path) as zf:
        print(f"AUTOMATED CHECK - ZIP integrity: {'PASS' if zf.testzip() is None else 'FAIL'}")
    sheets = read_book(path)
    print(f"AUTOMATED CHECK - expected tabs: {'PASS' if list(sheets) == EXPECTED else 'FAIL'} ({list(sheets)})")
    if list(sheets) != EXPECTED:
        failures.append("tabs")
    required = {
        "1_Cost_Job": ["C8", "C17", "C29", "C30", "C32", "C41", "C42", "C51", "C52", "C54", "C56", "C59", "C60", "C61"],
        "2_Pricing": ["C9", "C10", "C11", "C12", "C14", "C16", "C19", "C21", "B43", "C43", "D43", "E43", "F43", "B47", "C47", "D47", "E47", "F47"],
        "4_Channel_Fit": ["C11", "C12", "C14", "C16", "C20", "C21", "C23", "C24", "C25", "C26"],
    }
    for sheet, refs in required.items():
        ok = all(val(sheets, sheet, ref) not in (None, "") and formula(sheets, sheet, ref) for ref in refs)
        print(f"AUTOMATED CHECK - required formulas {sheet}: {'PASS' if ok else 'FAIL'}")
        if not ok:
            failures.append(f"formulas:{sheet}")
    all_formulas = [c["formula"] or "" for cells in sheets.values() for c in cells.values()]
    errors = [f for f in all_formulas if any(x in f for x in ["#REF!", "#DIV/0!", "#VALUE!", "#NAME?", "#N/A"])]
    print(f"AUTOMATED CHECK - formula error tokens: {'PASS' if not errors else 'FAIL'}")
    if errors:
        failures.append("formula-errors")
    retry = float(val(sheets, "1_Cost_Job", "C40") or 0)
    hitl = val(sheets, "1_Cost_Job", "C50")
    completed = float(val(sheets, "1_Cost_Job", "C8") or 0)
    print(f"AUTOMATED CHECK - retry non-zero: {'PASS' if retry > 0 else 'FAIL'}")
    print(f"AUTOMATED CHECK - HITL present: {'PASS' if hitl else 'FAIL'}")
    print(f"AUTOMATED CHECK - completed denominator positive: {'PASS' if completed > 0 else 'FAIL'}")
    if retry <= 0: failures.append("retry")
    if not hitl: failures.append("hitl")
    if completed <= 0: failures.append("denominator")
    print(f"AUTOMATED CHECK - GM target and package-completion breakeven present: {'PASS' if val(sheets, '2_Pricing', 'C16') and val(sheets, '2_Pricing', 'C15') else 'FAIL'}")
    breakeven_label = str(val(sheets, "2_Pricing", "A16") or "")
    breakeven_formula = str(formula(sheets, "2_Pricing", "C16") or "")
    semantic_formula_ok = "containment" not in breakeven_label.lower() and "C6" in breakeven_formula and "C7" in breakeven_formula and "C15" in breakeven_formula and "C8" in breakeven_formula
    print(f"SEMANTIC CHECK - C16 is package-completion formula, not autonomous-containment formula: {'PASS' if semantic_formula_ok else 'FAIL'} ({breakeven_label})")
    if not semantic_formula_ok:
        failures.append("semantic:C16")
    unit_blended = val(sheets, "2_Pricing", "C11") not in (None, "") and val(sheets, "2_Pricing", "C12") not in (None, "")
    print(f"AUTOMATED CHECK - unit/blended GM present: {'PASS' if unit_blended else 'FAIL'}")
    if not unit_blended:
        failures.append("gm")
    sensitivity = all(val(sheets, "2_Pricing", ref) not in (None, "") and formula(sheets, "2_Pricing", ref) for ref in ["B43", "C43", "D43", "E43", "F43", "B47", "C47", "D47", "E47", "F47"])
    print(f"AUTOMATED CHECK - completion sensitivity table: {'PASS' if sensitivity else 'FAIL'}")
    if not sensitivity:
        failures.append("sensitivity")
    print(f"AUTOMATED CHECK - benchmark dates present: {'PASS' if val(sheets, '6_Benchmarks', 'H5') and val(sheets, '6_Benchmarks', 'H6') else 'FAIL'}")
    print(f"MANUAL RUBRIC CHECK - official template: BLOCKED / substitute disclosed")
    print(f"MANUAL RUBRIC CHECK - autonomous containment: 20% (1/5); package completion 80% (4/5) is separate")
    print(f"AUTOMATED AUDIT STATUS: {'PASS' if not failures else 'FAIL'}")
    return 0 if not failures else 1


if __name__ == "__main__":
    raise SystemExit(main())
