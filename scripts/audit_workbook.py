"""Independent XML audit for the official Day25 workbook migration."""
from __future__ import annotations

import math
import sys
import zipfile
from pathlib import Path
from xml.etree import ElementTree as ET

try:
    sys.stdout.reconfigure(encoding="utf-8")
except AttributeError:
    pass

NS = {
    "m": "http://schemas.openxmlformats.org/spreadsheetml/2006/main",
    "r": "http://schemas.openxmlformats.org/officeDocument/2006/relationships",
    "p": "http://schemas.openxmlformats.org/package/2006/relationships",
}
EXPECTED = ["0_README", "1_Cost_Job", "2_Pricing", "3_Value_Metric", "4_Channel_Fit", "5_90Day_Plan", "6_Benchmarks"]
REPAIRS = {
    ("2_Pricing", "B5"): ("1_Cost_Job!B66", "'1_Cost_Job'!B66"),
    ("2_Pricing", "B29"): ("1_Cost_Job!B31+1_Cost_Job!B38+1_Cost_Job!B43+1_Cost_Job!B47", "'1_Cost_Job'!B31+'1_Cost_Job'!B38+'1_Cost_Job'!B43+'1_Cost_Job'!B47"),
    ("2_Pricing", "B30"): ("1_Cost_Job!B51*(1_Cost_Job!B52/60)*1_Cost_Job!B50", "'1_Cost_Job'!B51*('1_Cost_Job'!B52/60)*'1_Cost_Job'!B50"),
    ("2_Pricing", "B31"): ("IF(1_Cost_Job!B6=\"B\",(1_Cost_Job!B53/60)*1_Cost_Job!B50,0)", "IF('1_Cost_Job'!B6=\"B\",('1_Cost_Job'!B53/60)*'1_Cost_Job'!B50,0)"),
    ("2_Pricing", "B34"): ("1_Cost_Job!B10", "'1_Cost_Job'!B10"),
    ("4_Channel_Fit", "B6"): ("2_Pricing!B21", "'2_Pricing'!B21"),
}
YELLOW_INPUTS = {
    "1_Cost_Job": {"B5", "B6", "B9", "B10", *{f"B{x}" for x in range(15, 23)}, "B30", *{f"B{x}" for x in range(34, 38)}, "B41", "B42", "B46", *{f"B{x}" for x in range(50, 54)}, "B59", "B68"},
    "2_Pricing": {"B6", "B10", "B11", "B14", "B19", "B32"},
    "3_Value_Metric": {*{f"B{x}" for x in range(5, 10)}, *{f"B{x}" for x in range(13, 18)}, *{f"{c}{r}" for r in (26, 27) for c in "ABCD"}, *{f"B{x}" for x in range(30, 35)}},
    "4_Channel_Fit": {"B5", "B7", "B13", "B14", "B20", "B21", *{f"{c}{r}" for r in range(28, 34) for c in "BCD"}, *{f"B{x}" for x in range(38, 43)}},
    "5_90Day_Plan": {*{f"B{x}" for x in range(5, 9)}, *{f"{c}{r}" for r in range(12, 19) for c in "BCD"}, *{f"{c}{r}" for r in range(23, 26) for c in "BCD"}, *{f"B{x}" for x in range(29, 33)}},
    "6_Benchmarks": {"B3"},
}


def _target(target: str) -> str:
    target = target.lstrip("/")
    return target if target.startswith("xl/") else "xl/" + target


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
            target = targets[sh.attrib["{http://schemas.openxmlformats.org/officeDocument/2006/relationships}id"]]
            root = ET.fromstring(zf.read(_target(target)))
            cells = {}
            for c in root.findall(".//m:c", NS):
                ref = c.attrib["r"]
                formula_node = c.find("m:f", NS)
                value_node = c.find("m:v", NS)
                value = None if value_node is None else value_node.text
                if c.attrib.get("t") == "s" and value is not None:
                    value = shared[int(value)]
                elif c.attrib.get("t") == "inlineStr":
                    value = "".join(t.text or "" for t in c.findall("m:is//m:t", NS))
                cells[ref] = {"value": value, "formula": None if formula_node is None else (formula_node.text or ""), "style": c.attrib.get("s", "0")}
            sheets[name] = cells
        return sheets


def formula_map(path: Path):
    sheets = read_book(path)
    return {(sheet, ref): data["formula"] for sheet, cells in sheets.items() for ref, data in cells.items() if data["formula"] is not None}


def style_map(path: Path):
    sheets = read_book(path)
    return {(sheet, ref): data["style"] for sheet, cells in sheets.items() for ref, data in cells.items()}


def val(sheets, sheet, ref):
    return sheets.get(sheet, {}).get(ref, {}).get("value")


def formula(sheets, sheet, ref):
    return sheets.get(sheet, {}).get(ref, {}).get("formula")


def number(sheets, sheet, ref):
    try:
        return float(val(sheets, sheet, ref))
    except (TypeError, ValueError):
        return math.nan


def main() -> int:
    root = Path(__file__).resolve().parents[1]
    path = Path(sys.argv[1]) if len(sys.argv) > 1 else root / "deliverables" / "NguyenQuangHuy_Day25_model.xlsx"
    original = root / "templates" / "official" / "Day25-AI-Product-GTM-Monetization-Model.xlsx"
    failures = []
    if not path.exists():
        print("AUTOMATED CHECK - workbook exists: FAIL")
        return 1
    with zipfile.ZipFile(path) as zf:
        zip_ok = zf.testzip() is None
    print(f"AUTOMATED CHECK - ZIP integrity: {'PASS' if zip_ok else 'FAIL'}")
    if not zip_ok:
        failures.append("zip")

    sheets = read_book(path)
    tabs_ok = list(sheets) == EXPECTED
    print(f"AUTOMATED CHECK - official tabs: {'PASS' if tabs_ok else 'FAIL'} ({list(sheets)})")
    if not tabs_ok:
        failures.append("tabs")

    populated = all(val(sheets, sheet, ref) not in (None, "") for sheet, refs in YELLOW_INPUTS.items() for ref in refs)
    print(f"AUTOMATED CHECK - yellow input population: {'PASS' if populated else 'FAIL'}")
    if not populated:
        failures.append("yellow-inputs")

    required_formulas = {
        "1_Cost_Job": ["B11", "B23", "B27", "B28", "B29", "B31", "B38", "B43", "B47", "B54", "B55", "B56", "B62", "B63", "B64", "B65", "B66", "B67", "B69", "B72", "C72", "B77", "C77"],
        "2_Pricing": ["B5", "B7", "B12", "B13", "B15", "B16", "B20", "B21", "B22", "B23", "B24", "B25", "B29", "B30", "B31", "B33", "B34", "B35", "B39", "C39", "B44", "C44"],
        "3_Value_Metric": ["B10", "B18", "B21"],
        "4_Channel_Fit": ["B6", "B8", "B9", "B10", "B15", "B16", "B17", "B22", "B23", "B24", "B34", "C34", "D34", "B35"],
    }
    formula_ok = all(formula(sheets, sheet, ref) for sheet, refs in required_formulas.items() for ref in refs)
    formula_count = sum(1 for cells in sheets.values() for c in cells.values() if c["formula"] is not None)
    print(f"AUTOMATED CHECK - official formula coverage: {'PASS' if formula_ok else 'FAIL'} ({formula_count} formulas)")
    if not formula_ok:
        failures.append("formula-coverage")

    error_tokens = ("#REF!", "#DIV/0!", "#VALUE!", "#NAME?", "#N/A")
    errors = [(sheet, ref, data["value"]) for sheet, cells in sheets.items() for ref, data in cells.items() if any(token in str(data["value"] or "") for token in error_tokens) or any(token in str(data["formula"] or "") for token in error_tokens)]
    print(f"AUTOMATED CHECK - cached/formula error tokens: {'PASS' if not errors else 'FAIL'}")
    if errors:
        failures.append("formula-errors")

    attempts = number(sheets, "1_Cost_Job", "B9")
    autonomy = number(sheets, "1_Cost_Job", "B10")
    autonomous_jobs = number(sheets, "1_Cost_Job", "B11")
    package_jobs = number(sheets, "1_Cost_Job", "B12")
    retry_cost = number(sheets, "1_Cost_Job", "B47")
    hitl_cost = number(sheets, "1_Cost_Job", "B56")
    cost_per_job = number(sheets, "1_Cost_Job", "B66")
    selling_price = number(sheets, "2_Pricing", "B19")
    gm = number(sheets, "2_Pricing", "B21")
    breakeven = number(sheets, "2_Pricing", "B33")
    rates_ok = abs(autonomy - 0.20) < 1e-9 and abs(autonomous_jobs - 600) < 1e-9 and abs(package_jobs - 2400) < 1e-9 and abs(attempts - 3000) < 1e-9
    print(f"SEMANTIC CHECK - autonomous containment 20% is separate from package completion: {'PASS' if rates_ok else 'FAIL'} (B10={autonomy:.3g}, B11={autonomous_jobs:.0f}, B12={package_jobs:.0f})")
    if not rates_ok:
        failures.append("containment-semantics")
    retry_ok = retry_cost > 0
    hitl_ok = hitl_cost > 0
    cost_formula = formula(sheets, "1_Cost_Job", "B66") or ""
    denominator_ok = math.isfinite(cost_per_job) and "B11" in cost_formula and "B9" not in cost_formula
    print(f"AUTOMATED CHECK - retry modeled: {'PASS' if retry_ok else 'FAIL'}")
    print(f"AUTOMATED CHECK - human-review cost modeled: {'PASS' if hitl_ok else 'FAIL'}")
    print(f"SEMANTIC CHECK - Cost/Job denominator is B11 autonomous jobs: {'PASS' if denominator_ok else 'FAIL'}")
    if not retry_ok: failures.append("retry")
    if not hitl_ok: failures.append("hitl")
    if not denominator_ok: failures.append("denominator")
    label = str(val(sheets, "1_Cost_Job", "A10") or "").lower()
    label_ok = "containment" in label and ("autonom" in label or "làm xong" in label)
    pricing_ok = selling_price > number(sheets, "2_Pricing", "B7") and gm >= 0.60 and 0 < breakeven < autonomy
    print(f"SEMANTIC CHECK - containment label is explicit: {'PASS' if label_ok else 'FAIL'}")
    print(f"ECONOMIC CHECK - floor, GM and breakeven pass at current 20%: {'PASS' if pricing_ok else 'FAIL'}")
    if not label_ok: failures.append("containment-label")
    if not pricing_ok: failures.append("economics")

    preservation_ok = False
    if original.exists():
        before = formula_map(original)
        after = formula_map(path)
        changed = {key for key in set(before) | set(after) if before.get(key) != after.get(key)}
        preservation_ok = changed == set(REPAIRS) and all(after.get(key) == new for key, (_, new) in REPAIRS.items())
        style_ok = style_map(original) == style_map(path)
        print(f"FORMULA PRESERVATION - unauthorized formula mutations: {'PASS' if preservation_ok else 'FAIL'} (changed={len(changed)}, documented repairs={len(REPAIRS)})")
        print(f"STYLE PRESERVATION - cell style matrix: {'PASS' if style_ok else 'FAIL'}")
        if not preservation_ok: failures.append("formula-preservation")
        if not style_ok: failures.append("style-preservation")
    else:
        print("FORMULA PRESERVATION - official source: BLOCKED")
        failures.append("official-source")

    benchmark_ok = str(val(sheets, "6_Benchmarks", "B3") or "") == "2026-08-27"
    print(f"AUTOMATED CHECK - benchmark check date: {'PASS' if benchmark_ok else 'FAIL'} ({val(sheets, '6_Benchmarks', 'B3')})")
    if not benchmark_ok: failures.append("benchmark-date")

    print(f"AUTOMATED AUDIT STATUS: {'PASS' if not failures else 'FAIL'}")
    if failures:
        print("FAILURES: " + ", ".join(failures))
    return 0 if not failures else 1


if __name__ == "__main__":
    raise SystemExit(main())
