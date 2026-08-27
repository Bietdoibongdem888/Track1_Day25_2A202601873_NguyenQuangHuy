import fs from "node:fs/promises";
import { FileBlob, SpreadsheetFile } from "@oai/artifact-tool";

const root = process.cwd();
const source = `${root}/templates/official/Day25-AI-Product-GTM-Monetization-Model.xlsx`;
const output = `${root}/deliverables/NguyenQuangHuy_Day25_model.xlsx`;
const qaDir = `${root}/qa/official_workbook`;
await fs.mkdir(`${root}/deliverables`, { recursive: true });
await fs.mkdir(qaDir, { recursive: true });

const wb = await SpreadsheetFile.importXlsx(await FileBlob.load(source));
const s1 = wb.worksheets.getItem("1_Cost_Job");
const s2 = wb.worksheets.getItem("2_Pricing");
const s3 = wb.worksheets.getItem("3_Value_Metric");
const s4 = wb.worksheets.getItem("4_Channel_Fit");
const s5 = wb.worksheets.getItem("5_90Day_Plan");
const s6 = wb.worksheets.getItem("6_Benchmarks");

// Yellow input cells only: values are written without touching existing formats.
s1.getRange("B5:B6").values = [[
  "Grounded fraud package; customer decides.",
], ["A"]];
s1.getRange("B9:B10").values = [[3000], [0.20]];
s1.getRange("B15:B22").values = [[4], [20], [5], [0.40], [6], [3000], [1000], [300]];
s1.getRange("B30").values = [[0]];
s1.getRange("B34:B37").values = [[0], [0], [0], [0]];
s1.getRange("B41:B42").values = [[0.005], [0]];
s1.getRange("B46").values = [[0.08]];
s1.getRange("B50:B53").values = [[9.58], [0.05], [2], [6]];
s1.getRange("B59").values = [[0]];
s1.getRange("B68").values = [[26095.90]];

s2.getRange("B6").values = [[3]];
s2.getRange("B10:B11").values = [[4000], [600]];
s2.getRange("B14").values = [[1500]];
s2.getRange("B19").values = [[1.75]];
s2.getRange("B32").values = [[0.60]];

s3.getRange("B5:B9").values = [[0], [1], [0], [0], [1]];
s3.getRange("B13:B17").values = [[0], [0], [1], [0], [0]];
s3.getRange("A26:D27").values = [
  ["Intercom Fin", "Resolution / Procedure handoff outcome", "$0.99 / outcome", "https://www.intercom.com/help/en/articles/8205718-fin-ai-agent-outcomes"],
  ["Zendesk AI agents", "Verified / automated resolution", "As low as $1.50 / resolution", "https://www.zendesk.com/service/ai/top-ai-agents/"],
];
s3.getRange("B30:B34").values = [
  ["HYBRID"],
  ["Not different: scorecard suggests SEAT or HYBRID; Hybrid separates access from measured usage."],
  ["I choose Hybrid: platform access/governance plus per completed grounded package; the official tab models the usage leg."],
  ["Attribution 2/10 and Autonomy 1/10: local 5-case evidence is not customer causal proof and 4/5 cases need review."],
  ["Below about 12.4% autonomous containment, GM falls below 50% at the $1.75/job usage price."],
];

s4.getRange("B5").values = [[1050]];
s4.getRange("B7").values = [["Mid"]];
s4.getRange("B13:B14").values = [[500000], [220]];
s4.getRange("B20:B21").values = [[3000], [0.25]];
s4.getRange("B28:D33").values = [
  [1, 5, 2],
  [1, 5, 2],
  [1, 5, 2],
  [1, 5, 1],
  [1, 5, 2],
  [1, 5, 2],
];
s4.getRange("B38:B42").values = [
  ["Sales-Led"],
  ["N/A - Sales-Led selected"],
  ["N/A - Sales-Led selected"],
  ["N/A - no partner channel selected"],
  ["N/A - fallback is founder-led Sales-Led pilot"],
];

s5.getRange("B5:B8").values = [
  ["09:00-11:00 after an overnight alert burst"],
  ["Fraud analyst triages high-risk transaction alerts and prepares evidence/risk rationale before manual disposition"],
  ["Existing fraud-operations alert investigation queue/dashboard"],
  ["Queue side panel; Kafka -> fraud engine -> REST analyze"],
];
s5.getRange("B12:D18").values = [
  ["Sales-Led founder-led design-partner motion", "Sales-Led paid pilot motion", "Sales-Led expansion within adjacent payment-processor accounts"],
  ["2 design partners", "2 pilot customers / 6,000 labeled jobs", "2 paying customers + 1 adjacent segment"],
  ["8 fraud-ops interviews; produce pain notes and security-gap log", "Run 2 pilots; instrument completion, autonomy, retries and latency", "Standardize procurement pack; add multi-merchant processor playbook"],
  ["Create 300-case baseline manifest and manual-vs-Copilot protocol", "Weekly analyst review; compare paired time-on-task and safety outcomes", "Quarterly customer review; expand only after KPI gates"],
  ["Evidence: interview notes, 300-case manifest, security-gap register", "Evidence: pilot log, paired-time dataset, weekly safety/latency report", "Evidence: signed pilot report, procurement closeout and expansion case study"],
  ["KPI: 8 interviews, 2 design partners, 300 labeled jobs", "KPI: >=85% package completion; autonomy separate; >=70% blended GM; CAC <=$32k", "KPI: 2 paid; no unsafe auto-action; auth/RBAC + retention closed"],
  ["Nguyen Quang Huy + 2 design-partner fraud leads", "Nguyen Quang Huy; customer fraud team owns final disposition", "Nguyen Quang Huy + customer champion"],
];
s5.getRange("B23:D25").values = [
  ["PARTIAL - LOCAL CONTROLLED EVAL", "5 cases: 80% commercial package completion, 20% autonomous containment, 80% human review, 20% grounding failure; not customer evidence", "Nguyen Quang Huy - 2026-09-30"],
  ["PARTIAL", "Grounding/fallback/redaction evidenced; auth/RBAC, retention, TLS, vendor terms and live deployment remain open", "Nguyen Quang Huy - before pilot / 2026-10-15"],
  ["PLANNED / NOT EXECUTED / MISSING EVIDENCE", "2 design partners, 6,000 labeled jobs and paired manual baseline; no customer result claimed", "Nguyen Quang Huy - 2026-12-04"],
];
s5.getRange("B29:B32").values = [
  ["Có - product, buyer and unit are stated"],
  ["Có - Cost/Job, floor, price and GM are shown"],
  ["Có - Sales-Led and affordability math are shown"],
  ["NOT YET TESTED - target <=3 clarification questions"],
];

// The supplied file has objectively broken unquoted cross-sheet references. Repair only those formulas.
s2.getRange("B5").formulas = [["='1_Cost_Job'!B66"]];
s2.getRange("B29").formulas = [["='1_Cost_Job'!B31+'1_Cost_Job'!B38+'1_Cost_Job'!B43+'1_Cost_Job'!B47"]];
s2.getRange("B30").formulas = [["='1_Cost_Job'!B51*('1_Cost_Job'!B52/60)*'1_Cost_Job'!B50"]];
s2.getRange("B31").formulas = [["=IF('1_Cost_Job'!B6=\"B\",('1_Cost_Job'!B53/60)*'1_Cost_Job'!B50,0)"]];
s2.getRange("B34").formulas = [["='1_Cost_Job'!B10"]];
s4.getRange("B6").formulas = [["='2_Pricing'!B21"]];

// The one editable field on the read-only benchmark sheet is the mandatory check date.
s6.getRange("B3").values = [["2026-08-27"]];

// Keep planning assumptions auditable without changing the official layout.
wb.comments.setSelf({ displayName: "Nguyen Quang Huy" });
const comments = [
  [s1, "B5", "Official job definition: customer-valued investigation package; final disposition remains customer-owned."],
  [s1, "B10", "LOCAL CONTROLLED EVAL: autonomous containment = 1/5 = 20%. Commercial package completion = 4/5 = 80% is kept separate in evidence/containment-eval.md."],
  [s1, "B15", "CURRENT FIRST-PARTY SOURCE checked 2026-08-27: OpenAI GPT-5.6 Sol Standard short-context input = $4.00 / 1M tokens; current promotional/list distinction documented in evidence/pricing-sources.md."],
  [s1, "B17", "CURRENT FIRST-PARTY SOURCE checked 2026-08-27: GPT-5.6 Sol cache writes = $5.00 / 1M tokens (1.25x standard input)."],
  [s1, "B18", "CURRENT FIRST-PARTY SOURCE checked 2026-08-27: GPT-5.6 Sol cached input = $0.40 / 1M tokens."],
  [s1, "B41", "PLANNING ASSUMPTION - NOT PRODUCTION MEASUREMENT: $0.005 per attempt allocation for retrieval, embedding/vector DB, storage, logging and app/runtime reserve."],
  [s1, "B46", "PLANNING ASSUMPTION - NOT PRODUCTION MEASUREMENT: 8% retry rate retained until retry telemetry is instrumented."],
  [s1, "B50", "PLANNING ASSUMPTION: $9.58/hour derived from 250,000 VND/hour fully-loaded reviewer rate divided by 26,095.90 VND/USD FX."],
  [s1, "B68", "CURRENT PLANNING FX checked 2026-08-27: 26,095.90 VND/USD mid-market, XE. See evidence/pricing-sources.md."],
  [s2, "B11", "Official pricing denominator aligned to completed autonomous jobs/month from 1_Cost_Job!B11 = 600; attempts and non-contained cases remain separate."],
  [s2, "B19", "Planning price selected at $1.75/job: above the official 3x floor, within the 70% labor anchor, and bounded by current outcome/resolution benchmarks; not a customer quote."],
  [s3, "B5", "Official 0-2 score: no production job log linked to final customer disposition is verified."],
  [s3, "B13", "Official 0-2 score: end-to-end autonomous completion is not current state; local autonomous containment is 1/5."],
  [s4, "B5", "Formula input for official Channel Fit: $1,050/month = $1.75/job x 600 completed autonomous jobs/month. Pure usage scenario; Hybrid recommendation is documented separately."],
  [s4, "B20", "PLANNING ASSUMPTION - NOT CRM MEASUREMENT: $3,000 cost per opportunity for the founder-led first-90-day design-partner motion; this is below the displayed enterprise benchmark and must be replaced after pilot funnel data."],
  [s5, "B23", "Evidence status is intentionally PARTIAL: local controlled evidence exists, but no customer pilot or production telemetry."],
];
for (const [sheet, cell, note] of comments) wb.comments.addThread({ cell: sheet.getRange(cell) }, note);

const inspection = await wb.inspect({ kind: "workbook,sheet,table", maxChars: 6000, tableMaxRows: 5, tableMaxCols: 8, tableMaxCellChars: 100 });
await fs.writeFile(`${qaDir}/migration_inspect.ndjson`, inspection.ndjson ?? String(inspection), "utf8");

const xlsx = await SpreadsheetFile.exportXlsx(wb);
await xlsx.save(output);

for (let i = 0; i < 7; i++) {
  const sheet = wb.worksheets.getItemAt(i);
  const preview = await wb.render({ sheetName: sheet.name, autoCrop: "all", scale: 1, format: "png" });
  await fs.writeFile(`${qaDir}/${String(i).padStart(2, "0")}_${sheet.name}.png`, new Uint8Array(await preview.arrayBuffer()));
}

console.log(JSON.stringify({ output, sheets: 7, repairedFormulaCells: ["2_Pricing!B5", "2_Pricing!B29", "2_Pricing!B30", "2_Pricing!B31", "2_Pricing!B34", "4_Channel_Fit!B6"] }, null, 2));
