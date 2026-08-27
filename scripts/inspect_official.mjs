import fs from "node:fs/promises";
import { FileBlob, SpreadsheetFile } from "@oai/artifact-tool";

const root = process.cwd();
const inputPath = `${root}/templates/official/Day25-AI-Product-GTM-Monetization-Model.xlsx`;
const outDir = `${root}/qa/official_workbook_original`;
await fs.mkdir(outDir, { recursive: true });

const wb = await SpreadsheetFile.importXlsx(await FileBlob.load(inputPath));
const summary = await wb.inspect({ kind: "workbook,sheet,table", maxChars: 12000, tableMaxRows: 8, tableMaxCols: 10, tableMaxCellChars: 120 });
await fs.writeFile(`${outDir}/summary.ndjson`, summary.ndjson ?? String(summary), "utf8");

for (let i = 0; i < 20; i++) {
  let sheet;
  try { sheet = wb.worksheets.getItemAt(i); } catch { break; }
  if (!sheet) break;
  const name = sheet.name;
  const used = sheet.getUsedRange();
  const values = used ? used.values : [];
  const formulas = used ? used.formulas : [];
  await fs.writeFile(`${outDir}/${String(i).padStart(2, "0")}_${name}_values.json`, JSON.stringify({ name, values, formulas }, null, 2), "utf8");
  const preview = await wb.render({ sheetName: name, autoCrop: "all", scale: 1, format: "png" });
  await fs.writeFile(`${outDir}/${String(i).padStart(2, "0")}_${name}.png`, new Uint8Array(await preview.arrayBuffer()));
}

console.log(summary.ndjson ?? summary);
