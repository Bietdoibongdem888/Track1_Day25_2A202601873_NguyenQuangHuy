from pathlib import Path

from reportlab.lib import colors
from reportlab.lib.enums import TA_CENTER, TA_LEFT, TA_RIGHT
from reportlab.lib.pagesizes import letter
from reportlab.lib.styles import ParagraphStyle, getSampleStyleSheet
from reportlab.lib.units import inch
from reportlab.platypus import (
    BaseDocTemplate,
    Frame,
    KeepTogether,
    PageTemplate,
    Paragraph,
    Spacer,
    Table,
    TableStyle,
)


ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "deliverables" / "NguyenQuangHuy_Day25_onepager.pdf"

NAVY = colors.HexColor("#183B56")
TEAL = colors.HexColor("#0F766E")
BLUE_GRAY = colors.HexColor("#E8EEF5")
LIGHT = colors.HexColor("#F4F8FB")
MUTED = colors.HexColor("#5B6770")
INK = colors.HexColor("#1F2937")
GOLD = colors.HexColor("#7A5A00")
ORANGE = colors.HexColor("#FCE8D5")
RED = colors.HexColor("#9B1C1C")
GREEN = colors.HexColor("#1F7A4C")


styles = getSampleStyleSheet()
styles.add(ParagraphStyle("MemoTitle", parent=styles["Normal"], fontName="Helvetica-Bold", fontSize=19, leading=21, textColor=NAVY, spaceAfter=1))
styles.add(ParagraphStyle("MemoSub", parent=styles["Normal"], fontName="Helvetica-Bold", fontSize=8.4, leading=10, textColor=MUTED, spaceAfter=5))
styles.add(ParagraphStyle("LeadLabel", parent=styles["Normal"], fontName="Helvetica-Bold", fontSize=6.6, leading=7.5, textColor=TEAL, spaceAfter=1))
styles.add(ParagraphStyle("Lead", parent=styles["Normal"], fontName="Helvetica", fontSize=7.65, leading=9.2, textColor=INK))
styles.add(ParagraphStyle("MetricValue", parent=styles["Normal"], fontName="Helvetica-Bold", fontSize=10.2, leading=11, alignment=TA_CENTER, textColor=NAVY))
styles.add(ParagraphStyle("MetricLabel", parent=styles["Normal"], fontName="Helvetica-Bold", fontSize=5.5, leading=6.2, alignment=TA_CENTER, textColor=MUTED))
styles.add(ParagraphStyle("BlockTitle", parent=styles["Normal"], fontName="Helvetica-Bold", fontSize=10, leading=11.2, textColor=TEAL, spaceAfter=1))
styles.add(ParagraphStyle("BlockSub", parent=styles["Normal"], fontName="Helvetica-Oblique", fontSize=6.4, leading=7.3, textColor=MUTED, spaceAfter=3))
styles.add(ParagraphStyle("Body", parent=styles["Normal"], fontName="Helvetica", fontSize=6.75, leading=8.1, textColor=INK, spaceAfter=2))
styles.add(ParagraphStyle("SmallBody", parent=styles["Normal"], fontName="Helvetica", fontSize=6.45, leading=7.55, textColor=INK, spaceAfter=2))
styles.add(ParagraphStyle("Note", parent=styles["Normal"], fontName="Helvetica-Bold", fontSize=6.35, leading=7.3, textColor=GOLD))
styles.add(ParagraphStyle("NoteRed", parent=styles["Normal"], fontName="Helvetica-Bold", fontSize=6.35, leading=7.3, textColor=RED))
styles.add(ParagraphStyle("Source", parent=styles["Normal"], fontName="Helvetica-Oblique", fontSize=5.6, leading=6.5, textColor=MUTED))


def p(text, style="Body"):
    return Paragraph(text, styles[style])


def labeled(label, text, style="Body"):
    return p(f"<b><font color='#183B56'>{label}:</font></b> {text}", style)


def footer(canvas, doc):
    canvas.saveState()
    canvas.setFont("Helvetica-Bold", 6.2)
    canvas.setFillColor(MUTED)
    canvas.drawRightString(letter[0] - 0.42 * inch, letter[1] - 0.28 * inch, "DAY25 | P-015 | PRICING + GTM + EVIDENCE")
    canvas.setFont("Helvetica", 6.0)
    canvas.drawCentredString(letter[0] / 2, 0.22 * inch, "READY WITH DISCLOSED LIMITATIONS - see evidence/ and FINAL_AUDIT_REPORT.md | 2026-08-27")
    canvas.restoreState()


def note_box(text, fill, text_style="Note"):
    table = Table([[p(text, text_style)]], colWidths=[2.18 * inch])
    table.setStyle(TableStyle([
        ("BACKGROUND", (0, 0), (-1, -1), fill),
        ("BOX", (0, 0), (-1, -1), 0.45, colors.HexColor("#E9C8A0") if fill == ORANGE else colors.HexColor("#E9B7B7")),
        ("LEFTPADDING", (0, 0), (-1, -1), 5),
        ("RIGHTPADDING", (0, 0), (-1, -1), 5),
        ("TOPPADDING", (0, 0), (-1, -1), 3),
        ("BOTTOMPADDING", (0, 0), (-1, -1), 3),
    ]))
    return table


def block(title, subtitle, items, note=None, note_fill=None, note_style="Note"):
    flow = [p(title, "BlockTitle"), p(subtitle, "BlockSub")]
    flow.extend(items)
    if note:
        flow.extend([Spacer(1, 2), note_box(note, note_fill, note_style)])
    return flow


def build():
    doc = BaseDocTemplate(
        str(OUT),
        pagesize=letter,
        leftMargin=0.42 * inch,
        rightMargin=0.42 * inch,
        topMargin=0.42 * inch,
        bottomMargin=0.36 * inch,
        title="P-015 Day25 Pricing, GTM and Evidence Memo",
        author="Nguyen Quang Huy",
    )
    frame = Frame(doc.leftMargin, doc.bottomMargin, doc.width, doc.height, id="normal", leftPadding=0, rightPadding=0, topPadding=0, bottomPadding=0)
    doc.addPageTemplates([PageTemplate(id="memo", frames=[frame], onPage=footer)])

    story = [
        p("P-015 | AI FRAUD INVESTIGATION COPILOT", "MemoTitle"),
        p("Pricing, GTM and evidence memo | Nguyen Quang Huy | 2A202601873", "MemoSub"),
    ]
    lead = Table([[p("WHAT IS SOLD", "LeadLabel"), p("A grounded investigation package for each eligible suspicious alert, embedded into an existing fraud-operations workflow. The AI assembles evidence and policy context; an authorized human owns the final disposition.", "Lead")]], colWidths=[0.72 * inch, doc.width - 0.72 * inch])
    lead.setStyle(TableStyle([
        ("BACKGROUND", (0, 0), (-1, -1), colors.HexColor("#E9F5F3")),
        ("BOX", (0, 0), (-1, -1), 0.6, colors.HexColor("#B6D6D2")),
        ("VALIGN", (0, 0), (-1, -1), "TOP"),
        ("LEFTPADDING", (0, 0), (-1, -1), 6),
        ("RIGHTPADDING", (0, 0), (-1, -1), 6),
        ("TOPPADDING", (0, 0), (-1, -1), 4),
        ("BOTTOMPADDING", (0, 0), (-1, -1), 3),
    ]))
    story.extend([lead, Spacer(1, 4)])

    metric_data = [[
        p("7,648", "MetricValue"), p("22,945", "MetricValue"), p("32,000 + 30M", "MetricValue"),
        p("82.8%", "MetricValue"), p("80% EVAL", "MetricValue"), p("44.3%", "MetricValue"),
    ], [
        p("VND / JOB", "MetricLabel"), p("PRICE FLOOR", "MetricLabel"), p("USAGE + PLATFORM", "MetricLabel"),
        p("BLENDED GM", "MetricLabel"), p("CONTAINMENT PROXY", "MetricLabel"), p("GM BREAKEVEN", "MetricLabel"),
    ]]
    metrics = Table(metric_data, colWidths=[doc.width / 6] * 6, rowHeights=[0.21 * inch, 0.16 * inch])
    metrics.setStyle(TableStyle([
        ("BACKGROUND", (0, 0), (-1, -1), LIGHT),
        ("BOX", (0, 0), (-1, -1), 0.5, colors.HexColor("#C9D6E2")),
        ("INNERGRID", (0, 0), (-1, -1), 0.35, colors.HexColor("#C9D6E2")),
        ("VALIGN", (0, 0), (-1, -1), "MIDDLE"),
        ("TOPPADDING", (0, 0), (-1, -1), 1),
        ("BOTTOMPADDING", (0, 0), (-1, -1), 1),
    ]))
    story.extend([metrics, Spacer(1, 4)])

    pricing = block(
        "01 | PRICING",
        "Sell the software workflow, not an unproven autonomous outcome",
        [
            labeled("Customer", "Mid-market fintech / payment processor"),
            labeled("Buyer / budget", "Head of Risk or COO / software and fraud-operations tooling"),
            labeled("One job", "Complete when the copilot returns a schema-valid, grounded investigation package with required evidence/decision fields; customer final disposition is recorded separately."),
            labeled("Value metric", "Hybrid: 30M VND platform fee/month + 32,000 VND per completed job."),
            labeled("Base fee", "30M/month purchases account-level workflow access, integration/configuration and governance/auditability; it is not a second charge for the package itself.", "SmallBody"),
            labeled("Unit GM", "76.1% on variable usage; 82.8% blended after the 30M/month platform fee at the base case.", "SmallBody"),
            labeled("Rationale", "Attribution 2/5: the 5-case local control eval produced 4/5 grounded packages (80%), but no customer time-saved or outcome measurement. Autonomy 1/5: only 1/5 completed without required human intervention; 4/5 cases route to review. Hybrid follows the low-attribution/low-autonomy matrix and avoids unsupported outcome billing.", "SmallBody"),
            labeled("Value anchor", "15 min at 250,000 VND/hour = 62,500 VND/job full value; 50% capture = 31,250 VND/job. Proposed 32,000 VND is above the 22,945 VND floor and below full labor value.", "SmallBody"),
        ],
        "RED TEAM: if the 80% package-completion proxy is wrong by 2x to 40%, usage GM falls to 56.1%. Production completion is the economic gate.", ORANGE, "Note",
    )
    gtm = block(
        "02 | GTM",
        "One channel for 90 days: Sales-Led",
        [
            labeled("Affordability", "ARPU 106.8M VND/month | ACV 1.282B VND / $49.3K reference | 12-month payback", "SmallBody"),
            labeled("CAC math", "Budget 1.061B | estimated CAC 350M | gap 711M | affordability ratio 3.03x", "SmallBody"),
            labeled("Deals / AE", "2.81 deals/year | 0.013 deals/selling day; mathematically feasible but planning-only.", "SmallBody"),
            labeled("Pain Moment", "09:00-11:00 after an overnight alert burst: a fraud analyst triages high-risk transactions in the existing fraud-operations alert queue/dashboard and needs a grounded case package before manual disposition.", "SmallBody"),
            labeled("Surface", "User-facing: existing fraud-analyst alert investigation queue/dashboard side panel. Backend: Kafka fraud_alerts -> fraud engine/agent -> REST /api/v1/fraud/analyze. Live integration is PARTIAL / NOT VERIFIED.", "SmallBody"),
            labeled("Month 1 | Learn", "2 design partners, 8 interviews, 300 labeled jobs; produce pain notes, failure taxonomy and time-on-task baseline.", "SmallBody"),
            labeled("Months 2-3 | Leverage", "2 pilots / 6,000 jobs / >=85% completion / >=70% GM / CAC <=350M; track 12 qualified opportunities and 3 wins.", "SmallBody"),
            labeled("Month 4+ | Expand", "Only after >=85% completion, 2 paying customers and security-gap closure. Next niche: multi-merchant payment processors.", "SmallBody"),
        ],
    )
    evidence = block(
        "03 | EVIDENCE",
        "Procurement can see what is proven and what is open",
        [
            labeled("Eval Results", "PARTIAL. Local control eval: 5 attempted, 4 grounded packages (80% commercial completion proxy), 1 autonomous completion (20%), 4 human-review cases and 1 grounding failure; retry telemetry is not instrumented. Eight RAG queries: 100% citation accuracy. Upstream ML recall: 80.08% validation / 84.84% integration. Not customer evidence.", "SmallBody"),
            labeled("Risk Checklist", "PARTIAL. Grounding, fallback, injection defense, score preservation, redaction and human review are evidenced. Auth/RBAC, rate limit, TLS, retention/deletion, durable audit export, vendor terms and live deployment remain open.", "SmallBody"),
            labeled("Pilot Report", "MISSING EVIDENCE. No customer or participant is fabricated. PLANNED - NOT YET EXECUTED: start 2026-10-01, end 2026-11-26, 2 design partners, 6,000 jobs; owner Nguyen Quang Huy; measure completion, time saved, latency, retries, Cost/Job and safety.", "SmallBody"),
            labeled("Submission gate", "READY WITH DISCLOSED LIMITATIONS. Official Day28 templates were not found locally; this memo and workbook are transparent substitutes. Numeric claims trace to workbook cells in evidence/onepager-traceability.md. Production readiness remains gated.", "SmallBody"),
        ],
        "Decision: READY for artifact review/submission. Production claims remain gated on the planned pilot and open controls.", colors.HexColor("#FDECEC"), "NoteRed",
    )

    body = Table([[pricing, gtm, evidence]], colWidths=[doc.width / 3] * 3)
    body.setStyle(TableStyle([
        ("BOX", (0, 0), (-1, -1), 0.5, colors.HexColor("#D9E2EC")),
        ("INNERGRID", (0, 0), (-1, -1), 0.5, colors.HexColor("#D9E2EC")),
        ("VALIGN", (0, 0), (-1, -1), "TOP"),
        ("LEFTPADDING", (0, 0), (-1, -1), 6),
        ("RIGHTPADDING", (0, 0), (-1, -1), 6),
        ("TOPPADDING", (0, 0), (-1, -1), 5),
        ("BOTTOMPADDING", (0, 0), (-1, -1), 5),
    ]))
    story.extend([body, Spacer(1, 3), p("Source trail: P-015 artifacts/agent + artifacts/ml/lightgbm; P-015 docs/business_product_direction.md, ai_fraud_agent.md, security.md, deployment_guide.md; current OpenAI, Supabase, Stripe Radar and Fingerprint pricing checked 2026-08-27. See workbook and evidence pack for full notes.", "Source")])
    doc.build(story)
    print(OUT)


if __name__ == "__main__":
    build()
