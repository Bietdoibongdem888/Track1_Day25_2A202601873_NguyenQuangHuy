import fs from "node:fs/promises";
import { SpreadsheetFile, Workbook } from "@oai/artifact-tool";

const ROOT = process.cwd();
const OUT = `${ROOT}/deliverables/NguyenQuangHuy_Day25_model.xlsx`;
const QA = `${ROOT}/qa/workbook`;

const C = {
  navy: "#183B56",
  teal: "#0F766E",
  lightBlue: "#E8F1F7",
  paleBlue: "#F4F8FB",
  yellow: "#FFF2CC",
  green: "#E6F4EA",
  orange: "#FCE8D5",
  red: "#FDECEC",
  gray: "#F2F4F7",
  ink: "#1F2937",
  muted: "#5B6770",
  blueText: "#0000FF",
  greenText: "#008000",
  border: "#D9E2EC",
};

const money = '#,##0;[Red](#,##0);-';
const pct = '0.0%;[Red](0.0%);-';
const count = '#,##0;[Red](#,##0);-';
const dateFmt = 'yyyy-mm-dd';

function setTitle(sheet, lastCol, text) {
  const r = sheet.getRange(`A1:${lastCol}1`);
  r.merge();
  r.values = [[text]];
  r.format = { fill: C.navy, font: { bold: true, color: '#FFFFFF', size: 16 }, verticalAlignment: 'center' };
  r.format.rowHeight = 28;
}

function setSubtitle(sheet, lastCol, text) {
  const r = sheet.getRange(`A2:${lastCol}2`);
  r.merge();
  r.values = [[text]];
  r.format = { fill: C.paleBlue, font: { color: C.muted, italic: true, size: 10 }, wrapText: true };
  r.format.rowHeight = 28;
}

function section(sheet, range, text) {
  const r = sheet.getRange(range);
  r.merge();
  r.values = [[text]];
  r.format = { fill: C.teal, font: { bold: true, color: '#FFFFFF' }, verticalAlignment: 'center' };
  r.format.rowHeight = 22;
}

function header(sheet, range) {
  const r = sheet.getRange(range);
  r.format = { fill: C.lightBlue, font: { bold: true, color: C.ink }, wrapText: true, borders: { preset: 'all', style: 'thin', color: C.border } };
}

function body(sheet, range) {
  sheet.getRange(range).format = { font: { color: C.ink }, wrapText: true, borders: { preset: 'insideHorizontal', style: 'thin', color: C.border } };
}

function inputs(sheet, ranges) {
  for (const range of ranges) {
    sheet.getRange(range).format = { fill: C.yellow, font: { color: C.blueText }, wrapText: true };
  }
}

function formulas(sheet, ranges) {
  for (const range of ranges) {
    sheet.getRange(range).format = { font: { color: '#000000' }, wrapText: true };
  }
}

function widths(sheet, map) {
  for (const [col, width] of Object.entries(map)) sheet.getRange(`${col}:${col}`).format.columnWidth = width;
}

function moneyFmt(sheet, range) { sheet.getRange(range).format.numberFormat = money; }
function pctFmt(sheet, range) { sheet.getRange(range).format.numberFormat = pct; }
function countFmt(sheet, range) { sheet.getRange(range).format.numberFormat = count; }

const wb = Workbook.create();
const s0 = wb.worksheets.add('0_README');
const s1 = wb.worksheets.add('1_Cost_Job');
const s2 = wb.worksheets.add('2_Pricing');
const s3 = wb.worksheets.add('3_Value_Metric');
const s4 = wb.worksheets.add('4_Channel_Fit');
const s5 = wb.worksheets.add('5_90Day_Plan');
const s6 = wb.worksheets.add('6_Benchmarks');

for (const s of [s0, s1, s2, s3, s4, s5, s6]) {
  s.showGridLines = false;
}

// 0_README - explicit template limitation and model map.
setTitle(s0, 'F', 'DAY25 | AI Pricing, GTM & Evidence Model');
setSubtitle(s0, 'F', 'Student: Nguyen Quang Huy | ID: 2A202601873 | Product: P-015 AI Fraud Investigation Copilot | Currency: VND unless noted');
s0.getRange('A4:F4').values = [['Status: PARTIAL - official Day28 workbook/DOCX template not found in searched local paths; transparent substitute used', '', '', '', '', '']];
s0.getRange('A4:F4').merge(true);
s0.getRange('A4:F4').format = { fill: C.orange, font: { bold: true, color: '#7A3E00' }, wrapText: true };
section(s0, 'A6:F6', 'How to use this model');
s0.getRange('A7:F13').values = [
  ['Purpose', 'Defensible pricing, GTM affordability and evidence pack for P-015.', '', '', '', ''],
  ['Editable inputs', 'Yellow cells with blue text. Do not overwrite formula cells.', '', '', '', ''],
  ['Formula outputs', 'Black text; cross-sheet links are green where useful for tracing.', '', '', '', ''],
  ['Source of truth', 'P-015 repo artifacts and docs; current first-party vendor pages checked 2026-08-27; labeled assumptions where measured data is absent.', '', '', '', ''],
  ['Primary decision', 'Hybrid value metric: monthly platform fee plus per completed investigation job.', '', '', '', ''],
  ['Critical caveat', 'Commercial completion / containment is an 80% LOCAL CONTROLLED EVAL PROXY from 4/5 grounded packages; it is not customer evidence. Autonomous completion in the same run is 20%.', '', '', '', ''],
  ['Template note', 'This workbook preserves required Day25 tab names but does not represent the missing official Day28 layout.', '', '', '', ''],
];
for (let r = 7; r <= 13; r++) { s0.getRange(`B${r}:F${r}`).merge(); }
body(s0, 'A7:F13');
s0.getRange('A7:A13').format = { font: { bold: true, color: C.navy }, fill: C.gray };
section(s0, 'A15:F15', 'Workbook map');
s0.getRange('A16:F23').values = [
  ['Tab', 'Role', 'Key outputs', 'Evidence status', 'Primary source', 'Owner'],
  ['1_Cost_Job', 'Unit cost build', 'Cost/attempt; Cost/completed-job; retry; HITL; denominator', 'Formula-driven with assumptions', 'P-015 artifacts + OpenAI/Supabase pricing', 'Nguyen Quang Huy'],
  ['2_Pricing', 'Price and GM', 'Floor; proposed price; unit/blended GM; breakeven; sensitivity; anchors', 'Formula-driven with controlled-eval proxy', 'Day25 decision assumptions + local eval', 'Nguyen Quang Huy'],
  ['3_Value_Metric', 'Metric decision', 'Attribution; Autonomy; exact 3-sentence note', 'Evidence-backed / partial', 'P-015 eval artifacts and architecture docs', 'Nguyen Quang Huy'],
  ['4_Channel_Fit', 'GTM affordability', 'Sales-Led; CAC budget; estimated CAC; gap; pain moment', 'Planning assumptions', 'Day25 channel logic', 'Nguyen Quang Huy'],
  ['5_90Day_Plan', 'Execution plan', 'Learn / Leverage / Expand milestones', 'Targets, not actuals', 'Day25 plan', 'Nguyen Quang Huy'],
  ['6_Benchmarks', 'Comparable pricing', 'Two current first-party benchmarks', 'Checked 2026-08-27', 'Stripe Radar; Fingerprint', 'Nguyen Quang Huy'],
  ['QA', 'Manual gate', 'See evidence and scripts folders', 'Not a subjective rubric proof', 'Local audit scripts', 'Nguyen Quang Huy'],
];
header(s0, 'A16:F16'); body(s0, 'A17:F23');
s0.getRange('A25:F25').values = [['Legend', 'Yellow/blue = input', 'Black = formula', 'Green = internal link', 'Orange = limitation/warning', 'Green fill = passed threshold']];
s0.getRange('A25:F25').format = { fill: C.gray, font: { bold: true, color: C.ink }, wrapText: true };
widths(s0, { A: 18, B: 44, C: 29, D: 27, E: 44, F: 20 });
s0.freezePanes.freezeRows(2);

// 1_Cost_Job - completed-job denominator and auditable unit cost.
setTitle(s1, 'E', '1 | COST / COMPLETED INVESTIGATION JOB');
setSubtitle(s1, 'E', 'Base-case unit economics for one customer-month. Direct COGS includes API, retry, infra allocation, internal QA and allocated direct overhead. Customer escalation labor is disclosed separately under Variant A.');
section(s1, 'A4:E4', 'Volume and completion inputs');
s1.getRange('A5:E17').values = [
  ['Driver', 'Unit', 'Base', 'Status', 'Source / rationale'],
  ['Jobs attempted', 'jobs / month', 3000, 'ASSUMPTION', 'Planning volume for one mid-market fintech customer.'],
  ['Completion / containment rate', '% of attempts', 0.8, 'LOCAL CONTROLLED EVAL', '4/5 grounded, schema-valid commercial packages in evidence/containment-eval.md; not production customer completion. Autonomous completion in the same run is 1/5 (20%).'],
  ['Completed jobs', 'jobs / month', null, 'FORMULA', 'Jobs attempted x completion rate. Denominator for Cost/Job.'],
  ['Escalation rate', '% of completed', 0.35, 'ESTIMATE', 'Human review remains material; 4/5 local cases required review, but that sample is not a production rate.'],
  ['Escalated jobs', 'jobs / month', null, 'FORMULA', 'Completed jobs x escalation rate.'],
  ['Internal QA review rate', '% of completed', 0.1, 'ESTIMATE', 'Our COGS only: 10% QA sample for safety/grounding review.'],
  ['QA reviewed jobs', 'jobs / month', null, 'FORMULA', 'Completed jobs x QA review rate.'],
  ['QA minutes / reviewed job', 'minutes', 3, 'ASSUMPTION', 'Short structured quality check, not full investigation.'],
  ['Escalation minutes / escalated job', 'minutes', 20, 'ASSUMPTION', 'Customer-owned analyst escalation effort disclosed, excluded from our COGS.'],
  ['Reviewer labor rate', 'VND / hour', 250000, 'ASSUMPTION', 'Fully loaded specialist labor planning rate. Validate in pilot.'],
  ['Planning FX', 'VND / USD', 26000, 'ASSUMPTION', 'Used only to translate vendor API/infra list prices into VND.'],
  ['Completion denominator check', 'check', null, 'FORMULA', 'Must be positive and distinct from attempted jobs.'],
];
header(s1, 'A5:E5'); body(s1, 'A6:E17');
s1.getRange('C8').formulas = [['=C6*C7']];
s1.getRange('C10').formulas = [['=C8*C9']];
s1.getRange('C12').formulas = [['=C8*C11']];
s1.getRange('C17').formulas = [['=IF(AND(C8>0,C8<=C6),"PASS - denominator = completed jobs","FAIL - denominator invalid")']];
section(s1, 'A19:E19', 'API token math and cache analysis');
s1.getRange('A20:E36').values = [
  ['Driver', 'Unit', 'Base', 'Status', 'Source / rationale'],
  ['Model', 'model', 'gpt-5.5', 'REFERENCE', 'OpenAI pricing page checked 2026-08-27. Local P-015 path is deterministic; this is the optional LLM-enabled cost scenario.'],
  ['Model calls / job', 'calls', 1, 'ASSUMPTION', 'One structured investigation synthesis call per completed attempt.'],
  ['Fresh input tokens / call', 'tokens', 10000, 'ASSUMPTION', 'Transaction, analyst question and case-specific context.'],
  ['Cached input tokens / call', 'tokens', 14000, 'ASSUMPTION', 'Stable system/policy context eligible for prompt caching.'],
  ['Output tokens / call', 'tokens', 2000, 'ASSUMPTION', 'Structured report and next-step recommendation.'],
  ['Input price', 'USD / 1M tokens', 5, 'VERIFIED LIST', 'OpenAI GPT-5.5 Standard short-context input price, checked 2026-08-27.'],
  ['Cached input price', 'USD / 1M tokens', 0.5, 'VERIFIED LIST', 'OpenAI GPT-5.5 Standard cached input price, checked 2026-08-27.'],
  ['Output price', 'USD / 1M tokens', 30, 'VERIFIED LIST', 'OpenAI GPT-5.5 Standard short-context output price, checked 2026-08-27.'],
  ['API cost / attempt with cache', 'VND / attempt', null, 'FORMULA', 'Fresh input + cached input + output at published rates, translated at planning FX.'],
  ['API cost / attempt without cache', 'VND / attempt', null, 'FORMULA', 'All input priced as fresh input; output unchanged.'],
  ['Cache savings / attempt', 'VND / attempt', null, 'FORMULA', 'Without-cache cost less with-cache cost.'],
  ['Cache savings', '%', null, 'FORMULA', 'Absolute savings divided by without-cache cost.'],
  ['Batch price scenario', 'USD / 1M tokens', 2.5, 'REFERENCE', 'OpenAI GPT-5.5 Batch input price; not used in base because case workflow is near-real-time.'],
  ['Batch output price scenario', 'USD / 1M tokens', 15, 'REFERENCE', 'OpenAI GPT-5.5 Batch output price; latency trade-off must be tested.'],
  ['Current local LLM calls', 'calls in eval', 0, 'VERIFIED LOCAL', 'P-015 evaluation report states deterministic path and 0 ms LLM latency; not a production API usage observation.'],
  ['API cost audit check', 'check', null, 'FORMULA', 'Must be non-zero in the optional LLM-enabled base scenario.'],
];
header(s1, 'A20:E20'); body(s1, 'A21:E36');
s1.getRange('C29').formulas = [['=C22*((C23/1000000*C26)+(C24/1000000*C27)+(C25/1000000*C28))*C16']];
s1.getRange('C30').formulas = [['=C22*(((C23+C24)/1000000*C26)+(C25/1000000*C28))*C16']];
s1.getRange('C31').formulas = [['=C30-C29']];
s1.getRange('C32').formulas = [['=C31/C30']];
s1.getRange('C36').formulas = [['=IF(C29>0,"PASS - non-zero API scenario","FAIL - API silently zero")']];
section(s1, 'A38:E38', 'Retry, infrastructure and direct overhead');
s1.getRange('A39:E46').values = [
  ['Driver', 'Unit', 'Base', 'Status', 'Source / rationale'],
  ['Retry rate', '% of attempts', 0.08, 'ESTIMATE', 'Conservative fallback within prompt guidance; no measured production retry log found.'],
  ['Retry cost / month', 'VND / month', null, 'FORMULA', 'Attempted jobs x retry rate x cached API cost.'],
  ['Retry cost / completed job', 'VND / completed job', null, 'FORMULA', 'Retry monthly cost divided by completed jobs.'],
  ['Fixed infra allocation', 'VND / month', 4000000, 'ASSUMPTION', 'Supabase Pro $25/month plus app/compute/logging allocation; verify with deployed telemetry.'],
  ['Infra / completed job', 'VND / completed job', null, 'FORMULA', 'Fixed infra allocation divided by completed jobs.'],
  ['Allocated direct overhead', 'VND / month', 1500000, 'ASSUMPTION', 'Shared observability, data operations and evaluation support allocated to one customer.'],
  ['Direct overhead / completed job', 'VND / completed job', null, 'FORMULA', 'Allocated direct overhead divided by completed jobs.'],
];
header(s1, 'A39:E39'); body(s1, 'A40:E46');
s1.getRange('C41').formulas = [['=C6*C40*C29']];
s1.getRange('C42').formulas = [['=C41/C8']];
s1.getRange('C44').formulas = [['=C43/C8']];
s1.getRange('C46').formulas = [['=C45/C8']];
section(s1, 'A48:E48', 'HITL variant and direct-cost build');
s1.getRange('A49:E61').values = [
  ['Driver', 'Unit', 'Base', 'Status', 'Source / rationale'],
  ['HITL variant', 'policy', 'Variant A - software product; customer handles escalations', 'DECISION', 'Product is a copilot; human owns final resolution. Internal QA remains in our COGS.'],
  ['QA cost / month', 'VND / month', null, 'FORMULA', 'QA reviewed jobs x QA minutes x reviewer rate.'],
  ['Vendor-borne escalation labor', 'VND / month', null, 'DISCLOSED', 'Escalated jobs x escalation minutes x reviewer rate; excluded under Variant A.'],
  ['Customer-borne escalation labor', 'VND / month', null, 'DISCLOSED', 'Same amount, disclosed as customer workload rather than vendor COGS.'],
  ['Direct API monthly cost', 'VND / month', null, 'FORMULA', 'Attempted jobs x cached API cost.'],
  ['Direct infra monthly cost', 'VND / month', null, 'FORMULA', 'Fixed infra allocation.'],
  ['Direct retry monthly cost', 'VND / month', null, 'FORMULA', 'Retry cost/month.'],
  ['Direct HITL monthly cost', 'VND / month', null, 'FORMULA', 'Internal QA only under Variant A.'],
  ['Direct overhead monthly', 'VND / month', null, 'FORMULA', 'Allocated direct overhead.'],
  ['Total direct monthly cost', 'VND / month', null, 'FORMULA', 'Sum of direct service cost categories.'],
  ['Cost / attempted job', 'VND / attempt', null, 'FORMULA', 'Total direct monthly cost divided by attempted jobs.'],
  ['Cost / completed job', 'VND / completed job', null, 'FORMULA', 'Total direct monthly cost divided by completed jobs.'],
];
header(s1, 'A49:E49'); body(s1, 'A50:E61');
s1.getRange('C51').formulas = [['=C12*C13/60*C15']];
s1.getRange('C52').formulas = [['=C10*C14/60*C15']];
s1.getRange('C53').formulas = [['=C52']];
s1.getRange('C54').formulas = [['=C6*C29']];
s1.getRange('C55').formulas = [['=C43']];
s1.getRange('C56').formulas = [['=C41']];
s1.getRange('C57').formulas = [['=C51']];
s1.getRange('C58').formulas = [['=C45']];
s1.getRange('C59').formulas = [['=SUM(C54:C58)']];
s1.getRange('C60').formulas = [['=C59/C6']];
s1.getRange('C61').formulas = [['=C59/C8']];
s1.getRange('A63:E66').values = [
  ['Cost/Job audit', 'Value', 'Formula / interpretation', 'Status', 'Why it matters'],
  ['Incorrect attempted denominator', null, 'Cost / attempted job', 'FORMULA', 'This is the understated answer a model would show if it divided by attempts.'],
  ['Understatement from wrong denominator', null, 'Completed-job cost less attempted-job cost', 'FORMULA', 'Explicit economic error from the wrong denominator.'],
  ['Understatement %', null, 'Understatement divided by true Cost/Job', 'FORMULA', 'Should be material and visible.'],
];
header(s1, 'A63:E63'); body(s1, 'A64:E66');
s1.getRange('B64').formulas = [['=C60']];
s1.getRange('B65').formulas = [['=C61-C60']];
s1.getRange('B66').formulas = [['=B65/C61']];
inputs(s1, ['C6:C7','C9:C9','C11:C11','C13:C16','C21:C28','C33:C35','C40:C40','C43:C43','C45:C45','C50:C50']);
formulas(s1, ['C8:C8','C10:C10','C12:C12','C17:C17','C29:C32','C36:C36','C41:C42','C44:C44','C46:C46','C51:C61','B64:B66']);
countFmt(s1, 'C6:C6'); pctFmt(s1, 'C7:C7'); countFmt(s1, 'C8:C8'); pctFmt(s1, 'C9:C9'); pctFmt(s1, 'C11:C11'); countFmt(s1, 'C10:C10'); countFmt(s1, 'C12:C14'); moneyFmt(s1, 'C15:C16'); countFmt(s1, 'C23:C25'); moneyFmt(s1, 'C26:C28'); moneyFmt(s1, 'C29:C31'); pctFmt(s1, 'C32:C32'); moneyFmt(s1, 'C34:C35'); pctFmt(s1, 'C40:C40'); moneyFmt(s1, 'C41:C46'); moneyFmt(s1, 'C51:C61'); moneyFmt(s1, 'B64:B65'); pctFmt(s1, 'B66:B66');
widths(s1, { A: 31, B: 22, C: 22, D: 18, E: 62 });
s1.freezePanes.freezeRows(5);

// 2_Pricing - price floor, GM, breakeven algebra and value anchors.
setTitle(s2, 'E', '2 | PRICING, GROSS MARGIN & BREAKEVEN');
setSubtitle(s2, 'E', 'Usage price is per completed job. Platform fee is a separate hybrid component that purchases workflow, integration and auditability. All price inputs are planning decisions, not observed market transactions.');
section(s2, 'A4:E4', 'Proposed price and unit economics');
s2.getRange('A5:E21').values = [
  ['Driver', 'Unit', 'Base', 'Status', 'Source / rationale'],
  ['Platform fee / customer / month', 'VND / month', 30000000, 'ASSUMPTION', 'Hybrid base fee for workflow access, integration surface and auditability.'],
  ['Usage price / completed job', 'VND / completed job', 32000, 'DECISION', 'Set above floor and near labor-replacement anchor; validate with buyer interviews.'],
  ['Monthly ARPU', 'VND / month', null, 'FORMULA', 'Platform fee + usage price x completed jobs.'],
  ['Price floor', 'VND / completed job', null, 'FORMULA', '3 x Cost / completed job.'],
  ['Floor check', 'check', null, 'FORMULA', 'Usage price must be >= price floor.'],
  ['Usage gross margin', '%', null, 'FORMULA', 'Usage price less variable Cost/Job divided by usage price.'],
  ['Blended gross margin', '%', null, 'FORMULA', 'Monthly ARPU less monthly direct cost divided by monthly ARPU.'],
  ['GM health', 'check', null, 'FORMULA', 'Target >= 60%; >85% would trigger missing-cost audit.'],
  ['Current / evaluated containment', '%', null, 'LOCAL CONTROLLED EVAL', 'Linked from Cost/Job: 4/5 grounded-package completion; separate autonomous completion is 20%; production containment remains unmeasured.'],
  ['GM target', '%', 0.6, 'DECISION RULE', 'Prompt health threshold.'],
  ['Required containment for GM target', '%', null, 'FORMULA', 'Algebraic minimum at proposed usage price.'],
  ['Safety buffer', 'percentage points', null, 'FORMULA', 'Controlled-eval commercial completion proxy less required containment.'],
  ['Containment error scenario', '%', null, 'FORMULA', 'Half of current estimate: 2x relative error in the adverse direction.'],
  ['GM at containment error scenario', '%', null, 'FORMULA', 'Shows whether a 2x error breaks the model.'],
  ['Critical driver', 'text', 'Completion proxy; 80% -> 40% drops usage GM below 60%.', 'RED TEAM', 'At 2x adverse error, completed jobs halve and fixed cost is spread over fewer jobs.'],
  ['Economic decision', 'check', null, 'FORMULA', 'Proceed with paid pilot only while production completion evidence improves.'],
];
header(s2, 'A5:E5'); body(s2, 'A6:E21');
s2.getRange('C8').formulas = [['=C6+\'1_Cost_Job\'!C8*C7']];
s2.getRange('C9').formulas = [['=\'1_Cost_Job\'!C61*3']];
s2.getRange('C10').formulas = [['=C7>=C9']];
s2.getRange('C11').formulas = [['=(C7-\'1_Cost_Job\'!C61)/C7']];
s2.getRange('C12').formulas = [['=(C8-\'1_Cost_Job\'!C59)/C8']];
s2.getRange('C13').formulas = [['=IF(C12>=C15,"PASS - GM >= target",IF(C12>=0.5,"WARNING - GM 50%-60%","UNHEALTHY - GM < 50%"))']];
s2.getRange('C14').formulas = [['=\'1_Cost_Job\'!C7']];
s2.getRange('C16').formulas = [['=((\'1_Cost_Job\'!C6*\'1_Cost_Job\'!C29*(1+\'1_Cost_Job\'!C40)+\'1_Cost_Job\'!C43+\'1_Cost_Job\'!C45)/(\'1_Cost_Job\'!C6*((1-C15)*C7-(\'1_Cost_Job\'!C51/\'1_Cost_Job\'!C8))))']];
s2.getRange('C17').formulas = [['=C14-C16']];
s2.getRange('C18').formulas = [['=C14/2']];
s2.getRange('C19').formulas = [['=1-((\'1_Cost_Job\'!C6*\'1_Cost_Job\'!C29*(1+\'1_Cost_Job\'!C40)+\'1_Cost_Job\'!C43+\'1_Cost_Job\'!C45+\'1_Cost_Job\'!C6*C18*(\'1_Cost_Job\'!C51/\'1_Cost_Job\'!C8))/(C18*\'1_Cost_Job\'!C6*C7))']];
s2.getRange('C21').formulas = [['=IF(C19>=C15,"PASS - withstands 2x adverse containment error","REMEDIATION - containment/price/cost action required")']];
section(s2, 'A23:E23', 'Value anchors');
s2.getRange('A24:E33').values = [
  ['Driver', 'Unit', 'Base', 'Status', 'Source / rationale'],
  ['Manual evidence-assembly minutes displaced / job', 'minutes', 15, 'ASSUMPTION', 'Pilot hypothesis: agent packages history/evidence/policy context; analyst still decides.'],
  ['Fully loaded analyst labor rate', 'VND / hour', 250000, 'ASSUMPTION', 'Same rate as Cost/Job reviewer labor; validate against buyer labor data.'],
  ['Labor value displaced / job', 'VND / job', null, 'FORMULA', 'Minutes displaced / 60 x labor rate.'],
  ['Suggested share captured', '% of displaced value', 0.5, 'DECISION', 'Conservative 50% capture of labor value.'],
  ['Labor-replacement price anchor / job', 'VND / job', null, 'FORMULA', 'Labor value displaced x capture share.'],
  ['Monthly customer labor savings', 'VND / month', null, 'FORMULA', 'Minutes displaced x labor rate x jobs attempted x containment.'],
  ['Annual customer labor savings', 'VND / year', null, 'FORMULA', 'Monthly savings x 12.'],
  ['Proposed usage price / full labor value', '%', null, 'FORMULA', 'Usage price divided by labor value displaced.'],
  ['Anchor check', 'check', null, 'FORMULA', 'Proposed price is above floor and not above full displaced labor value.'],
];
header(s2, 'A24:E24'); body(s2, 'A25:E33');
s2.getRange('C27').formulas = [['=C25/60*C26']];
s2.getRange('C29').formulas = [['=C27*C28']];
s2.getRange('C30').formulas = [['=C25/60*C26*\'1_Cost_Job\'!C6*C14']];
s2.getRange('C31').formulas = [['=C30*12']];
s2.getRange('C32').formulas = [['=C7/C27']];
s2.getRange('C33').formulas = [['=IF(AND(C7>=C9,C7<=C27),"PASS - above floor and below full labor value","REVIEW - strategic premium needs evidence")']];
section(s2, 'A35:E35', 'Value Metric Decision Note | exactly 3 core sentences');
s2.getRange('A36:E39').merge();
s2.getRange('A36').values = [['Chosen value metric: Hybrid - a 30,000,000 VND/month platform fee for account-level workflow access, integration/configuration and governance/auditability plus 32,000 VND per completed, grounded investigation package; the variable charge measures a customer-visible unit with an objective boundary. Attribution is 2/5 because the 5-case local control eval produced 4/5 grounded packages but no measured analyst time saved or customer outcome, while Autonomy is 1/5 because only 1/5 completed without required human intervention and 4/5 cases routed to review. Outcome pricing is not appropriate without causal customer results; pure Seat pricing does not map cleanly to marginal AI usage and pure Usage can reduce bill predictability, so Hybrid is safer while aligning the variable charge to completed work.']];
s2.getRange('A36:E39').format = { fill: C.paleBlue, font: { color: C.ink }, wrapText: true, verticalAlignment: 'top', borders: { preset: 'outside', style: 'thin', color: C.border } };
s2.getRange('A36:E39').format.rowHeight = 56;
section(s2, 'A41:F41', 'Containment Sensitivity | variable usage price = 32,000 VND / completed job');
s2.getRange('A42:F47').values = [
  ['Containment', 'Completed jobs', 'Escalations', 'Direct monthly cost', 'Cost / completed job', 'Usage GM'],
  [0.5, null, null, null, null, null],
  [0.6, null, null, null, null, null],
  [0.7, null, null, null, null, null],
  [0.8, null, null, null, null, null],
  [0.9, null, null, null, null, null],
];
header(s2, 'A42:F42'); body(s2, 'A43:F47');
for (let r = 43; r <= 47; r++) {
  s2.getRange(`B${r}`).formulas = [[`='1_Cost_Job'!C6*A${r}`]];
  s2.getRange(`C${r}`).formulas = [[`=B${r}*'1_Cost_Job'!C9`]];
  s2.getRange(`D${r}`).formulas = [[`='1_Cost_Job'!C6*'1_Cost_Job'!C29*(1+'1_Cost_Job'!C40)+'1_Cost_Job'!C43+'1_Cost_Job'!C45+(B${r}*'1_Cost_Job'!C11*'1_Cost_Job'!C13/60*'1_Cost_Job'!C15)`]];
  s2.getRange(`E${r}`).formulas = [[`=D${r}/B${r}`]];
  s2.getRange(`F${r}`).formulas = [[`=1-(E${r}/C7)`]];
}
inputs(s2, ['A43:A47']); formulas(s2, ['B43:F47']);
pctFmt(s2, 'A43:A47'); countFmt(s2, 'B43:C47'); moneyFmt(s2, 'D43:E47'); pctFmt(s2, 'F43:F47');
s2.getRange('F43:F47').conditionalFormats.add('cellIs', { operator: 'lessThan', formula: 0.6, format: { fill: C.red } });
section(s2, 'A49:F49', 'Value-Created Anchor Audit');
s2.getRange('A50:F52').values = [
  ['Anchor', 'Value', 'Status', 'Source / rationale', 'Decision', 'Evidence gap'],
  ['Outcome / loss-avoidance capture', 'N/A', 'MISSING EVIDENCE', 'No measured fraud-loss reduction, false-positive reduction or customer outcome exists.', 'Do not use outcome pricing.', 'Pilot must measure outcome delta before any outcome metric.'],
  ['Labor replacement', null, 'CALCULATED', '15 min x 250,000 VND/hour x 50% capture; linked to Value anchors above.', 'Use as usage anchor.', 'Validate buyer labor and time-on-task in pilot.'],
];
header(s2, 'A50:F50'); body(s2, 'A51:F52');
s2.getRange('B52').formulas = [['=C29']];
formulas(s2, ['B52:B52']); moneyFmt(s2, 'B52:B52');
inputs(s2, ['C6:C7','C15:C15','C25:C26','C28:C28']);
formulas(s2, ['C8:C14','C16:C19','C21:C21','C27:C27','C29:C33']);
moneyFmt(s2, 'C6:C9'); pctFmt(s2, 'C11:C12'); pctFmt(s2, 'C14:C19'); moneyFmt(s2, 'C25:C27'); pctFmt(s2, 'C28:C28'); moneyFmt(s2, 'C29:C31'); pctFmt(s2, 'C32:C32');
widths(s2, { A: 36, B: 23, C: 24, D: 20, E: 64, F: 36 });
s2.freezePanes.freezeRows(5);

// 3_Value_Metric
setTitle(s3, 'E', '3 | VALUE METRIC DECISION');
setSubtitle(s3, 'E', 'Attribution asks whether P-015 caused a provable customer result. Autonomy asks whether P-015 completes the job end-to-end. Scores are current-state evidence, not roadmap claims.');
section(s3, 'A4:E4', 'Seat / Usage / Outcome / Hybrid scoring');
s3.getRange('A5:E9').values = [
  ['Metric', 'Attribution (1-5)', 'Autonomy (1-5)', 'Evidence fit', 'Decision'],
  ['Seat', 2, 1, 'Low attribution and low autonomy; seat is easy to budget but heavy use can decouple revenue from cost.', 'REJECT'],
  ['Usage', 2, 1, 'Completed-job usage reflects cost and value better than a seat, but needs a base fee for workflow/integration.', 'PARTIAL'],
  ['Outcome', 2, 1, 'Not justified: no measured analyst outcome, fraud-loss attribution or autonomous final resolution.', 'REJECT'],
  ['Hybrid', 2, 1, 'Matches low-attribution/low-autonomy matrix and Day24 hybrid direction; platform access + completed job.', 'SELECTED'],
];
header(s3, 'A5:E5'); body(s3, 'A6:E9');
s3.getRange('A11:E17').values = [
  ['Decision field', 'Value', 'Source / evidence', 'Status', 'Notes'],
  ['Selected value metric', 'Hybrid', '3_Value_Metric decision table and 2_Pricing Decision Note', 'VERIFIED DECISION', 'Monthly platform fee plus per completed investigation job.'],
  ['Attribution score', 2, 'P-015 artifacts/agent_metrics.json: structured output 100%, grounding 80%; no customer time/outcome measurement.', 'PARTIAL EVIDENCE', 'Proxy quality evidence is not causal value evidence.'],
  ['Autonomy score', 1, 'P-015 evaluation_report.md and architecture docs: human review required for 4/5 cases; AI recommends only.', 'VERIFIED CURRENT STATE', 'No outcome billing until final-resolution ownership is instrumented.'],
  ['Containment definition', 'Schema-valid grounded investigation package with required evidence/decision fields; customer final disposition recorded separately.', 'P-015 metrics-pack core action and scope; adapted for the copilot billing boundary.', 'DEFINITION', 'Bill only when objective package completion rule is met; do not treat human-gated review as autonomous completion.'],
  ['Matrix result', 'Low Attribution + Low Autonomy -> Seat / Hybrid', 'Day25 assignment rule', 'VERIFIED RULE', 'Hybrid selected because variable cost scales with completed jobs.'],
  ['Decision Note', null, '2_Pricing!A36:E39', 'FORMULA LINK', 'Exactly 3 core sentences; no market override claimed.'],
];
header(s3, 'A11:E11'); body(s3, 'A12:E17');
s3.getRange('B17:E17').merge();
s3.getRange('B17').formulas = [['=\'2_Pricing\'!A36']];
s3.getRange('B17:E17').format = { fill: C.paleBlue, font: { color: C.greenText }, wrapText: true };
inputs(s3, ['B6:C9']); formulas(s3, ['B17:B17']);
widths(s3, { A: 28, B: 20, C: 31, D: 50, E: 23 });
s3.freezePanes.freezeRows(5);

// 4_Channel_Fit
setTitle(s4, 'E', '4 | CHANNEL FIT & SALES-LED AFFORDABILITY');
setSubtitle(s4, 'E', 'Exactly one primary channel for the first 90 days: Sales-Led. The product touches fraud operations, existing systems and procurement, so a focused sales motion is the current evidence-aligned choice.');
section(s4, 'A4:E4', 'Channel and CAC budget');
s4.getRange('A5:E24').values = [
  ['Driver', 'Unit', 'Base', 'Status', 'Source / rationale'],
  ['Primary channel', 'choice', 'Sales-Led', 'DECISION', 'One channel only; integration/security/procurement make direct sales the first motion.'],
  ['Segment', 'segment', 'Mid-market fintech / payment processor', 'DECISION', 'First niche from P-015 business direction.'],
  ['Monthly ARPU', 'VND / month', null, 'FORMULA', 'Blended ARPU from hybrid pricing.'],
  ['Blended GM', '%', null, 'FORMULA', 'Blended GM from pricing sheet.'],
  ['Allowed payback', 'months', 12, 'DECISION', 'Conservative below mid-market <18-month assignment ceiling.'],
  ['CAC budget / customer', 'VND / customer', null, 'FORMULA', 'ARPU x GM x payback months.'],
  ['ACV', 'VND / year', null, 'FORMULA', 'Monthly ARPU x 12.'],
  ['Annual quota / AE', 'VND / year', 3600000000, 'ASSUMPTION', 'Focused AE quota for a new vertical motion.'],
  ['Deals / AE / year', 'deals', null, 'FORMULA', 'Annual quota / ACV.'],
  ['Realistic selling days / year', 'days', 220, 'ASSUMPTION', 'Working selling days after leave/holidays.'],
  ['Deals / AE / selling day', 'deals / day', null, 'FORMULA', 'Deals per AE per year / selling days.'],
  ['Fully loaded AE cost', 'VND / year', 600000000, 'ASSUMPTION', 'Compensation + benefits + sales tooling allocation.'],
  ['Qualified opportunities / AE / year', 'opportunities', 12, 'ASSUMPTION', 'Planning funnel volume; validate in first 90 days.'],
  ['Win rate', '%', 0.25, 'ASSUMPTION', 'Planning win rate for qualified mid-market opportunities.'],
  ['Selling cost / qualified opportunity', 'VND / opportunity', null, 'FORMULA', 'AE cost / qualified opportunities.'],
  ['Selling cost / won deal', 'VND / won deal', null, 'FORMULA', 'Selling cost / opportunity / win rate.'],
  ['Pre-sales + onboarding allocation', 'VND / customer', 150000000, 'ASSUMPTION', 'Integration and procurement effort allocation.'],
  ['Estimated CAC / channel', 'VND / customer', null, 'FORMULA', 'Selling cost / won deal + pre-sales/onboarding.'],
  ['Affordability gap', 'VND / customer', null, 'FORMULA', 'CAC budget less estimated CAC; positive is affordable.'],
];
header(s4, 'A5:E5'); body(s4, 'A6:E26');
s4.getRange('C8').formulas = [['=\'2_Pricing\'!C8']];
s4.getRange('C9').formulas = [['=\'2_Pricing\'!C12']];
s4.getRange('C11').formulas = [['=C8*C9*C10']];
s4.getRange('C12').formulas = [['=C8*12']];
s4.getRange('C14').formulas = [['=C13/C12']];
s4.getRange('C16').formulas = [['=C14/C15']];
s4.getRange('C20').formulas = [['=C17/C18']];
s4.getRange('C21').formulas = [['=C20/C19']];
s4.getRange('C23').formulas = [['=C21+C22']];
s4.getRange('C24').formulas = [['=C11-C23']];
s4.getRange('A25:E26').values = [
  ['ACV (USD reference)', 'USD / year', null, 'FORMULA', 'ACV in VND divided by the explicit planning FX; reference only, not a quoted USD contract price.'],
  ['Affordability ratio', 'x', null, 'FORMULA', 'CAC budget divided by estimated CAC; above 1.00x indicates headroom.'],
];
s4.getRange('C25').formulas = [["=C12/'1_Cost_Job'!C16"]];
s4.getRange('C26').formulas = [['=C11/C23']];
s4.getRange('A28:E33').values = [
  ['GTM proof point', 'Answer', 'Evidence / rationale', 'Status', 'Risk if wrong'],
  ['Affordability decision', null, 'CAC budget compared with estimated CAC.', 'FORMULA', 'If negative, narrow ICP or use founder-led pilots before hiring AE.'],
  ['Pain Moment', 'Between 09:00 and 11:00 after an overnight alert burst, a fraud analyst triages high-risk transactions in the existing fraud-operations alert investigation queue/dashboard and needs a grounded case package before manual disposition.', 'P-015 business direction and analyst workflow; user-facing surface is the existing alert investigation queue/dashboard.', 'EVIDENCE-ALIGNED', 'Timing and task must be confirmed in customer interviews.'],
  ['Integration surface', 'Backend: Kafka fraud_alerts -> fraud engine/agent -> REST /api/v1/fraud/analyze. User-facing: existing fraud analyst alert investigation queue/dashboard side panel.', 'P-015 architecture, API contract, case-management UI and deployment docs.', 'PARTIAL / LOCAL', 'Full live Kafka/ML integration is not currently verified.'],
  ['Channel red-team', 'Strongest counterargument: procurement and integration cycles can exceed 90 days.', 'Sales-Led survives only with 2 design partners and a tightly scoped copilot pilot.', 'PARTIAL', 'Fallback is founder-led design partner motion, not a second primary channel.'],
  ['Channel status', null, 'Primary channel must remain exactly one.', 'FORMULA', 'Status gate for Day25.'],
];
header(s4, 'A28:E28'); body(s4, 'A29:E33');
s4.getRange('B29').formulas = [['=IF(C23>=0,"PASS - estimated CAC within budget","REMEDIATION - CAC exceeds budget")']];
s4.getRange('B33').formulas = [['=IF(C6="Sales-Led","PASS - exactly one primary channel","FAIL - choose exactly one channel")']];
inputs(s4, ['C6:C7','C10:C10','C13:C13','C15:C15','C17:C18','C19:C19','C22:C22']); formulas(s4, ['C8:C9','C11:C12','C14:C14','C16:C16','C20:C21','C23:C26','B29:B29','B33:B33']);
moneyFmt(s4, 'C8:C8'); pctFmt(s4, 'C9:C9'); moneyFmt(s4, 'C10:C13'); countFmt(s4, 'C14:C15'); s4.getRange('C16').format.numberFormat = '0.000;[Red](0.000);-'; moneyFmt(s4, 'C17:C18'); pctFmt(s4, 'C19:C19'); moneyFmt(s4, 'C20:C24'); s4.getRange('C25').format.numberFormat = '$#,##0;[Red]($#,##0);-'; s4.getRange('C26').format.numberFormat = '0.00x';
s4.getRange('C16').format.numberFormat = '0.000;[Red](0.000);-';
widths(s4, { A: 36, B: 53, C: 24, D: 20, E: 48 });
s4.freezePanes.freezeRows(5);

// 5_90Day_Plan
setTitle(s5, 'G', '5 | 90-DAY PLAN: LEARN -> LEVERAGE -> EXPAND');
setSubtitle(s5, 'G', 'Targets are plans, not achieved results. Month 4+ is an expansion gate and is explicitly outside the first 90-day commitment. Owner is the student only where the role is legitimate.');
s5.getRange('A4:G19').values = [
  ['Phase', 'Owner', 'Deadline', 'Metric', 'Target', 'Evidence produced', 'Status'],
  ['Month 1 - LEARN', 'Nguyen Quang Huy', new Date('2026-09-30'), 'Design partners', '2 targeted; not confirmed customers', 'ICP shortlist + outreach log', 'PLANNED'],
  ['Month 1 - LEARN', 'Nguyen Quang Huy', new Date('2026-09-30'), 'Stakeholder interviews', '8 completed interviews', 'Interview notes coded by pain moment', 'PLANNED'],
  ['Month 1 - LEARN', 'Nguyen Quang Huy', new Date('2026-09-30'), 'Evaluated jobs', '300 labeled alert investigations', 'Case manifest + completion labels', 'PLANNED'],
  ['Month 1 - LEARN', 'Nguyen Quang Huy', new Date('2026-09-30'), 'Failure modes', 'Top 5 failure modes with owners', 'Failure taxonomy + remediation backlog', 'PLANNED'],
  ['Month 1 - LEARN', 'Nguyen Quang Huy', new Date('2026-09-30'), 'Evidence improvement', 'Baseline p50/p95 latency and time-on-task recorded', 'Before/after measurement protocol', 'PLANNED'],
  ['Months 2-3 - LEVERAGE', 'Nguyen Quang Huy', new Date('2026-11-30'), 'Pilot customers', '2 paid or design-partner pilots targeted', 'Pilot agreements / scope records', 'PLANNED'],
  ['Months 2-3 - LEVERAGE', 'Nguyen Quang Huy', new Date('2026-11-30'), 'Evaluated jobs', '6,000 jobs across pilot scope', 'Versioned eval report', 'PLANNED'],
  ['Months 2-3 - LEVERAGE', 'Nguyen Quang Huy', new Date('2026-11-30'), 'Containment', '>=85% measured completion', 'Completion log with denominator', 'PLANNED'],
  ['Months 2-3 - LEVERAGE', 'Nguyen Quang Huy', new Date('2026-11-30'), 'Blended GM', '>=70% after telemetry', 'Cost ledger + monthly margin review', 'PLANNED'],
  ['Months 2-3 - LEVERAGE', 'Nguyen Quang Huy', new Date('2026-11-30'), 'CAC', '<=350,000,000 VND/customer', 'CRM funnel and won-deal cost', 'PLANNED'],
  ['Months 2-3 - LEVERAGE', 'Nguyen Quang Huy', new Date('2026-11-30'), 'Sales-led KPI', '12 qualified opps and 3 wins target', 'Pipeline report', 'PLANNED'],
  ['Month 4+ - EXPAND', 'Nguyen Quang Huy', new Date('2027-01-31'), 'Expansion gate', 'Only after >=85% completion, 2 paying customers and security gap closure', 'Expansion decision memo', 'NOT IN FIRST 90 DAYS'],
  ['Month 4+ - EXPAND', 'Nguyen Quang Huy', new Date('2027-01-31'), 'Next niche', 'Payment processors with multi-merchant queues', 'ICP extension hypothesis', 'NOT IN FIRST 90 DAYS'],
  ['Month 4+ - EXPAND', 'Nguyen Quang Huy', new Date('2027-01-31'), 'Trigger', 'Pilot evidence and procurement checklist pass', 'Signed gate review', 'NOT IN FIRST 90 DAYS'],
  ['Plan control', 'Nguyen Quang Huy', new Date('2026-09-05'), 'Primary channel', 'Sales-Led only', 'Channel decision log', 'CONTROL'],
];
header(s5, 'A4:G4'); body(s5, 'A5:G19');
s5.getRange('C5:C19').format.numberFormat = dateFmt;
s5.getRange('G5:G19').dataValidation = { rule: { type: 'list', values: ['PLANNED', 'IN PROGRESS', 'COMPLETE', 'NOT IN FIRST 90 DAYS', 'BLOCKED', 'CONTROL'] } };
s5.getRange('G5:G19').format = { fill: C.yellow, font: { color: C.blueText } };
s5.getRange('A5:A19').format = { font: { bold: true, color: C.navy } };
widths(s5, { A: 26, B: 22, C: 16, D: 25, E: 42, F: 44, G: 22 });
s5.freezePanes.freezeRows(4);

// 6_Benchmarks
setTitle(s6, 'J', '6 | CURRENT FIRST-PARTY BENCHMARKS');
setSubtitle(s6, 'J', 'Checked 2026-08-27. Benchmarks are adjacent fraud/risk products, not exact substitutes for P-015 investigation work. Published list/starting prices are recorded without pretending custom enterprise pricing is public.');
s6.getRange('A4:J6').values = [
  ['Product', 'Comparable job', 'Value metric', 'Published price', 'Currency', 'Billing unit', 'Source URL', 'Date checked', 'List / promo status', 'Notes'],
  ['Stripe Radar', 'Automated transaction fraud screening and fraud alerts', 'Plan subscription plus transaction evaluation / pay-as-you-go', 'Radar Standard starting at $10/month; Radar Plus $14/month; Radar Pro $20/month for business pricing shown', 'USD', 'subscription / evaluated transaction', 'https://stripe.com/radar/pricing', new Date('2026-08-27'), 'Starting/list price shown', 'Relevant fraud-budget anchor; P-015 is a deeper investigation copilot, so do not benchmark 1:1.'],
  ['Fingerprint Pro Plus', 'Browser/mobile device identification and fraud signals', 'API request / identification', '$99/month for 20K API calls; then $4 per 1,000 additional API calls', 'USD', 'API call', 'https://fingerprint.com/pricing/', new Date('2026-08-27'), 'Starting/list price shown', 'Closest public usage unit: risk signal generation. Enterprise is custom.'],
];
header(s6, 'A4:J4'); body(s6, 'A5:J6');
s6.getRange('H5:H6').format.numberFormat = dateFmt;
s6.getRange('G5:G6').format = { font: { color: C.greenText, underline: true } };
section(s6, 'A8:J8', 'Vendor pricing used in Cost/Job model');
s6.getRange('A9:J13').values = [
  ['Vendor', 'Product/model', 'Input price', 'Cached input price', 'Output price', 'Batch price', 'Unit', 'Source', 'Date checked', 'Verification note'],
  ['OpenAI', 'gpt-5.5 Standard short context', 5, 0.5, 30, 'Input $2.50 / Output $15.00', 'USD / 1M tokens', 'https://platform.openai.com/pricing?model=contentfilter-alpha-001', new Date('2026-08-27'), 'Current page lists gpt-5.5 standard input $5, cached input $0.50, output $30; batch input $2.50 and output $15.00.'],
  ['Supabase', 'Pro plan', 25, null, null, null, 'USD / month', 'https://supabase.com/pricing', new Date('2026-08-27'), 'Used only as a direct-infra anchor; model allocates additional app/compute/logging reserve.'],
  ['P-015 local eval', 'Deterministic fallback path', 0, 0, 0, 'N/A', 'local run', 'P-015/artifacts/agent/agent_metrics.json', new Date('2026-08-13'), '0 ms LLM latency is evidence that the local evaluator made no remote LLM call; not a production cost claim.'],
  ['Model-control rule', 'Optional LLM base case', null, null, null, 'Batch not in base', 'decision', 'P-015/docs/ai_fraud_agent.md', new Date('2026-08-27'), 'Use realtime standard pricing until latency and batch eligibility are measured.'],
];
header(s6, 'A9:J9'); body(s6, 'A10:J13');
s6.getRange('I10:I13').format.numberFormat = dateFmt;
s6.getRange('H10:H13').format = { font: { color: C.greenText, underline: true } };
widths(s6, { A: 20, B: 34, C: 24, D: 27, E: 24, F: 27, G: 28, H: 48, I: 16, J: 58 });
s6.freezePanes.freezeRows(4);

// General formatting and conditional formatting.
for (const s of [s0, s1, s2, s3, s4, s5, s6]) {
  const used = s.getUsedRange();
  used.format.font = { name: 'Aptos', size: 10 };
}
// Re-apply title fonts after base font pass.
for (const [s, col] of [[s0,'F'],[s1,'E'],[s2,'E'],[s3,'E'],[s4,'E'],[s5,'G'],[s6,'J']]) {
  s.getRange(`A1:${col}1`).format.font = { name: 'Aptos Display', size: 16, bold: true, color: '#FFFFFF' };
}
s1.getRange('C7').conditionalFormats.add('cellIs', { operator: 'greaterThanOrEqual', formula: 0.6, format: { fill: C.green } });
s2.getRange('C12').conditionalFormats.add('cellIs', { operator: 'greaterThanOrEqual', formula: 0.6, format: { fill: C.green } });
s2.getRange('C19').conditionalFormats.add('cellIs', { operator: 'lessThan', formula: 0.6, format: { fill: C.red } });
s4.getRange('C23').conditionalFormats.add('cellIs', { operator: 'greaterThanOrEqual', formula: 0, format: { fill: C.green } });

// Make source comments auditable without crowding working tables.
wb.comments.setSelf({ displayName: 'Nguyen Quang Huy' });
wb.comments.addThread({ cell: s1.getRange('C26') }, 'Source: https://platform.openai.com/pricing?model=contentfilter-alpha-001 checked 2026-08-27. GPT-5.5 Standard short-context input price used in the base scenario.');
wb.comments.addThread({ cell: s1.getRange('C44') }, 'Source: https://supabase.com/pricing checked 2026-08-27. Pro plan is $25/month; additional app/compute/logging reserve is an explicit assumption.');
wb.comments.addThread({ cell: s2.getRange('C16') }, 'Formula: solve direct_cost / (price x attempts x containment) <= 1 - GM_target. QA cost per completion is included in the denominator adjustment.');

await fs.mkdir(`${ROOT}/deliverables`, { recursive: true });
await fs.mkdir(QA, { recursive: true });
const xlsx = await SpreadsheetFile.exportXlsx(wb);
await xlsx.save(OUT);

// Render every sheet for visual QA.
for (const name of ['0_README','1_Cost_Job','2_Pricing','3_Value_Metric','4_Channel_Fit','5_90Day_Plan','6_Benchmarks']) {
  const preview = await wb.render({ sheetName: name, autoCrop: 'all', scale: 1, format: 'png' });
  await fs.writeFile(`${QA}/${name.replaceAll('/', '_')}.png`, new Uint8Array(await preview.arrayBuffer()));
}

const inspect = await wb.inspect({ kind: 'table', range: '1_Cost_Job!A49:E61', include: 'values,formulas', tableMaxRows: 20, tableMaxCols: 6, maxChars: 8000 });
console.log(inspect.ndjson);
const errors = await wb.inspect({ kind: 'match', searchTerm: '#REF!|#DIV/0!|#VALUE!|#NAME\\?|#N/A', options: { useRegex: true, maxResults: 100 }, summary: 'final formula error scan' });
console.log(errors.ndjson);
console.log(JSON.stringify({ output: OUT, qaSheets: 7 }));
