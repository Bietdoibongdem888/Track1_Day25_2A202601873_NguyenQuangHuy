from __future__ import annotations

from pathlib import Path

from reportlab.lib import colors
from reportlab.lib.enums import TA_CENTER, TA_LEFT
from reportlab.lib.pagesizes import letter
from reportlab.lib.styles import ParagraphStyle, getSampleStyleSheet
from reportlab.lib.units import inch
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.platypus import (
    KeepTogether,
    Paragraph,
    SimpleDocTemplate,
    Spacer,
    Table,
    TableStyle,
)


ROOT = Path(__file__).resolve().parents[1]
OUTPUT = ROOT / "deliverables" / "NguyenQuangHuy_Day25_onepager.pdf"
QA_DIR = ROOT / "qa" / "onepager"

ARIAL = Path(r"C:\Windows\Fonts\arial.ttf")
ARIAL_BOLD = Path(r"C:\Windows\Fonts\arialbd.ttf")
ARIAL_ITALIC = Path(r"C:\Windows\Fonts\ariali.ttf")
if ARIAL.exists():
    pdfmetrics.registerFont(TTFont("Arial", str(ARIAL)))
    pdfmetrics.registerFont(TTFont("Arial-Bold", str(ARIAL_BOLD)))
    pdfmetrics.registerFont(TTFont("Arial-Italic", str(ARIAL_ITALIC)))
    FONT = "Arial"
    BOLD = "Arial-Bold"
else:
    FONT = "Helvetica"
    BOLD = "Helvetica-Bold"


PURPLE = colors.HexColor("#4F46E5")
INK = colors.HexColor("#1F2937")
MUTED = colors.HexColor("#6B7280")
PALE = colors.HexColor("#EEF2FF")
GRID = colors.HexColor("#D1D5DB")
GREEN = colors.HexColor("#166534")

styles = getSampleStyleSheet()
body = ParagraphStyle("body", parent=styles["BodyText"], fontName=FONT, fontSize=6.25, leading=7.45, textColor=INK, spaceAfter=0)
small = ParagraphStyle("small", parent=body, fontSize=5.55, leading=6.5)
tiny = ParagraphStyle("tiny", parent=body, fontSize=5.1, leading=5.9)
cell = ParagraphStyle("cell", parent=body, fontSize=5.45, leading=6.3)
cell_bold = ParagraphStyle("cell_bold", parent=cell, fontName=BOLD)
section = ParagraphStyle("section", parent=body, fontName=BOLD, fontSize=8.5, leading=10, textColor=PURPLE, spaceBefore=2, spaceAfter=2)
subhead = ParagraphStyle("subhead", parent=body, fontName=BOLD, fontSize=6.7, leading=7.8, textColor=PURPLE, spaceBefore=1, spaceAfter=1)
title = ParagraphStyle("title", parent=body, fontName=BOLD, fontSize=16, leading=17, textColor=PURPLE, alignment=TA_CENTER)
meta = ParagraphStyle("meta", parent=body, fontSize=6.1, leading=7.1, alignment=TA_CENTER, textColor=MUTED)
foot = ParagraphStyle("foot", parent=body, fontSize=5.4, leading=6.1, alignment=TA_CENTER, textColor=MUTED)


def P(text: str, style=body):
    return Paragraph(text, style)


def styled_table(data, widths, header=True, font_size=5.45, row_heights=None):
    wrapped = []
    for r, row in enumerate(data):
        wrapped.append([P(str(value), cell_bold if header and r == 0 else cell) for value in row])
    table = Table(wrapped, colWidths=widths, rowHeights=row_heights, repeatRows=1 if header else 0, hAlign="LEFT")
    commands = [
        ("GRID", (0, 0), (-1, -1), 0.35, GRID),
        ("VALIGN", (0, 0), (-1, -1), "TOP"),
        ("LEFTPADDING", (0, 0), (-1, -1), 3),
        ("RIGHTPADDING", (0, 0), (-1, -1), 3),
        ("TOPPADDING", (0, 0), (-1, -1), 2),
        ("BOTTOMPADDING", (0, 0), (-1, -1), 2),
    ]
    if header:
        commands += [("BACKGROUND", (0, 0), (-1, 0), PALE), ("TEXTCOLOR", (0, 0), (-1, 0), PURPLE)]
    table.setStyle(TableStyle(commands))
    return table


def main() -> None:
    OUTPUT.parent.mkdir(parents=True, exist_ok=True)
    QA_DIR.mkdir(parents=True, exist_ok=True)
    doc = SimpleDocTemplate(
        str(OUTPUT),
        pagesize=letter,
        leftMargin=0.75 * inch,
        rightMargin=0.75 * inch,
        topMargin=0.40 * inch,
        bottomMargin=0.35 * inch,
        title="Day25 Monetization One-Pager — Nguyen Quang Huy",
        author="Nguyen Quang Huy",
    )
    story = []
    story += [P("DAY 25 · AI-IN-ACTION · TRACK 1", title), P("MONETIZATION ONE-PAGER", ParagraphStyle("title2", parent=title, fontSize=10.2, leading=11.2, spaceAfter=2)), P("Tên / Nhóm: Nguyen Quang Huy  |  Sản phẩm: P-015 AI Fraud Investigation Copilot", meta), P("Value Metric đã chọn: HYBRID (official $/job scenario below)  |  Kênh: Sales-Led  |  Ngày: 2026-08-27", meta), Spacer(1, 3), P("Every numeric claim below traces to the official Day25 workbook or named P-015 evidence; 20% is autonomous containment, not 80% package completion.", small), Spacer(1, 3)]

    story += [P("1 · PRICING", section), P("Ngân sách khách hàng", subhead), P("Software / fraud-operations tooling; buyer: Head of Risk / COO; an authorized customer analyst owns final disposition. Commercial recommendation is Hybrid: platform/governance access plus measured usage; the official model below is the pure $/completed-autonomous-job usage leg.", body), Spacer(1, 2)]
    key = [
        ["Chỉ số", "Giá trị", "Lấy từ đâu"],
        ["Cost/Job", "$0.5422/job (~₫14,150)", "1_Cost_Job!B66; VND B69"],
        ["Giá sàn", "$1.6267/job (~₫42,447)", "2_Pricing!B7"],
        ["Giá đề xuất", "$1.75/job (~₫45,668)", "2_Pricing!B19"],
        ["GM", "69.0%", "2_Pricing!B21"],
        ["Breakeven", "15.5% autonomous", "2_Pricing!B33"],
        ["Containment hiện tại", "20.0% autonomous (1/5)", "1_Cost_Job!B10; eval CSV"],
    ]
    story += [styled_table(key, [1.15 * inch, 1.55 * inch, 2.25 * inch]), Spacer(1, 2)]

    story += [P("Value Metric + lý do", subhead), P("HYBRID: platform/governance access plus usage. Attribution score 2/10; autonomy score 1/10; no customer causal outcome evidence, and 4/5 local cases require human review.", body), P("Chosen unit: one completed grounded investigation package, priced per completed autonomous job in the official cost/pricing case. Evidence reports 4/5 package completion and 1/5 autonomous containment; these are distinct rates. Intercom Fin ($0.99/outcome) and Zendesk AI agents (as low as $1.50/resolution) are adjacent anchors, not P-015 customer proof.", small), P("Sources checked 2026-08-27: intercom.com/help/en/articles/8205718-fin-ai-agent-outcomes · zendesk.com/service/ai/top-ai-agents/", tiny), Spacer(1, 2)]

    story += [P("Các con số", subhead), P("Official model: $0.5422 Cost/Job; $1.6267 floor; $1.75 price; 69.0% GM; 15.5% breakeven autonomous containment; current 20.0%.", body), P("Cách neo giá", subhead), P("Anchor: official 70% labor ceiling is $1.75/job (B14/B16/B11). Proposed $1.75 is a planning decision, not a market quote; value and floor checks pass.", body), P("Mô hình gãy khi nào?", subhead), P("If autonomous containment falls below about 12.4%, GM falls below 50% at the $1.75/job usage price (the official sensitivity table starts at 50%).", body), Spacer(1, 2)]

    story += [P("2 · GO-TO-MARKET", section), P("Kênh đã chọn", subhead), P("Sales-Led only for 90 days; founder-led design-partner motion targets mid-market fintech/payment processors.", body), Spacer(1, 2)]
    channel = [
        ["Chỉ số", "Giá trị", "Lấy từ đâu"],
        ["ARPU", "$1,050/month", "4_Channel_Fit!B5"],
        ["CAC budget", "$13,043.88/customer", "4_Channel_Fit!B9"],
        ["Deals/AE/day", "0.180", "4_Channel_Fit!B16"],
        ["Estimated CAC", "$12,000", "4_Channel_Fit!B22"],
        ["Estimated / budget", "0.92x; coverage 1.09x", "4_Channel_Fit!B23; derived"],
    ]
    story += [styled_table(channel, [1.3 * inch, 1.65 * inch, 2.0 * inch]), Spacer(1, 2)]
    story += [P("Numeric channel evidence: ARPU $1,050/month; ACV $12,600/year; CAC budget $13,043.88; estimated CAC $12,000; deals/AE/day 0.180. The $3,000/opportunity input is founder-led planning, not CRM evidence; replace it after pilot funnel data.", small), P("Pain Moment", subhead), P("09:00–11:00 after an overnight alert burst: fraud analyst triages high-risk alerts in the existing fraud-operations alert queue/dashboard before manual disposition.", body), P("Embedding", subhead), P("Existing fraud-operations alert investigation queue/dashboard side panel. Backend: Kafka fraud_alerts → fraud engine/agent → REST /api/v1/fraud/analyze; live integration is PARTIAL / NOT VERIFIED.", small), Spacer(1, 2)]

    story += [P("90-Day Plan", subhead)]
    plan = [
        ["", "Tháng 1 — Học", "Tháng 2–3 — Đòn bẩy", "Tháng 4+ — Mở rộng"],
        ["Kênh", "Sales-Led founder-led design-partner motion", "Sales-Led paid pilot motion", "Sales-Led expansion within adjacent payment-processor accounts"],
        ["Mục tiêu số khách", "2 design partners", "2 pilot customers / 6,000 labeled jobs", "2 paying customers + 1 adjacent segment"],
        ["Việc cụ thể", "8 fraud-ops interviews; pain notes + security-gap log", "Run 2 pilots; instrument completion, autonomy, retries, latency", "Standardize procurement pack; multi-merchant processor playbook"],
        ["KPI đo được", "8 interviews, 2 partners, 300 labeled jobs", ">=85% package completion; autonomy separate; >=70% blended GM; CAC <=$32k", "2 paying customers; no unsafe auto-action; auth/RBAC + retention closed"],
        ["Ai chịu trách nhiệm", "Nguyen Quang Huy + 2 fraud leads", "Nguyen Quang Huy; customer owns final disposition", "Nguyen Quang Huy + customer champion"],
    ]
    story += [styled_table(plan, [0.85 * inch, 1.45 * inch, 1.65 * inch, 1.55 * inch]), Spacer(1, 2)]

    story += [P("3 · EVIDENCE PACK", section), P("Missing evidence is labeled with owner and deadline; no customer or production claim is fabricated.", small), Spacer(1, 1)]
    evidence = [
        ["Tài sản", "Đã có?", "Nội dung 1 câu — hoặc việc cần làm", "Ai · Deadline"],
        ["Eval Results (Day21–22)", "PARTIAL", "5-case local eval: 80% package completion, 20% autonomous containment, 80% human review, 20% grounding failure; not customer evidence.", "Nguyen Quang Huy · 2026-09-30"],
        ["Risk Checklist (Day24)", "PARTIAL", "Grounding/fallback/redaction evidenced; auth/RBAC, retention, TLS, vendor terms and live deployment remain open.", "Nguyen Quang Huy · before pilot / 2026-10-15"],
        ["Pilot Report", "PLANNED / NOT EXECUTED", "2 design partners, 6,000 labeled jobs and paired manual baseline; no customer result claimed.", "Nguyen Quang Huy · 2026-12-04"],
    ]
    story += [styled_table(evidence, [1.25 * inch, 0.83 * inch, 2.55 * inch, 1.45 * inch]), Spacer(1, 2)]
    story += [P("Stranger test: NOT YET TESTED (target ≤3 clarification questions). Prepared answers are stated above; pilot evidence remains planned.", foot), P("AI-IN-ACTION · TRACK 1 · official template migration · evidence-led planning", foot)]

    doc.build(story)
    print(f"WROTE {OUTPUT}")


if __name__ == "__main__":
    main()
