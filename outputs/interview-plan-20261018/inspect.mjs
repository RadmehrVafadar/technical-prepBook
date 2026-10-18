import fs from 'node:fs/promises';
import {createRequire} from 'node:module';
import {pathToFileURL} from 'node:url';
const req=createRequire('C:/Users/radme/.cache/codex-runtimes/codex-primary-runtime/dependencies/node/node_modules/package.json');
const {FileBlob,SpreadsheetFile}=await import(pathToFileURL(req.resolve('@oai/artifact-tool')).href);
const w=await SpreadsheetFile.importXlsx(await FileBlob.load('C:/Users/radme/Downloads/google_interview_master_tracker.xlsm'));
console.log((await w.inspect({kind:'table',range:"'Daily Plan'!A1:Q4",tableMaxCols:17,tableMaxRows:4,maxChars:1800})).ndjson);
try { const p=await w.render({sheetName:'Daily Plan',range:'A1:H8',scale:1,format:'png'}); await fs.writeFile(new URL('./before.png',import.meta.url),new Uint8Array(await p.arrayBuffer())); console.log('Rendered source'); } catch(e) {console.log('Source render:',e.message);}
