import fs from 'node:fs/promises';
import {createRequire} from 'node:module';
import {pathToFileURL} from 'node:url';
const req=createRequire('C:/Users/radme/.cache/codex-runtimes/codex-primary-runtime/dependencies/node/node_modules/package.json');
const {Workbook,SpreadsheetFile}=await import(pathToFileURL(req.resolve('@oai/artifact-tool')).href);
const out=new URL('./',import.meta.url);
const src=JSON.parse(await fs.readFile(new URL('source.json',out),'utf8'));
// Ordered by observed gaps, transfer value, supplied frequency and daily workload.
// Historical solves are not labelled new; the latest detailed evidence takes precedence.
const schedule=[
 ['2026-10-19',[200,560]],
 ['2026-10-20',[236,322]],
 ['2026-10-21',[207,875]],
 ['2026-10-22',[394]],
 ['2026-10-23',[],'Practice session with former Staff SWE'],
 ['2026-10-24',[128,15]],
 ['2026-10-25',[11,904]],
 ['2026-10-26',[39,22]],
 ['2026-10-27',[206,2]],
 ['2026-10-28',[146]],
 ['2026-10-29',[54,5]],
 ['2026-10-30',[56,57]],
 ['2026-10-31',[994,417]],
 ['2026-11-01',[34,981]],
 ['2026-11-02',[215,49]],
 ['2026-11-03',[55,300]],
 ['2026-11-04',[416]],
 ['2026-11-05',[1631]],
 ['2026-11-06',[518,543]],
 ['2026-11-07',[208,435]],
 ['2026-11-08',[410]],
 ['2026-11-09',[42]],
 ['2026-11-10',[239]],
 ['2026-11-11',[310,2096]],
 ['2026-11-12',[322,560]],
 ['2026-11-13',[875,394]],
 ['2026-11-14',[15,200]],
 ['2026-11-15',[146]],
 ['2026-11-16',[3]],
 ['2026-11-17',[],'Technical assessment 1'],
 ['2026-11-17',[],'Technical assessment 2'],
];
const rows=[]; const seen=new Set(); const audit=[];
for(const [date,ids,event] of schedule){
 if(event){rows.push([new Date(date+'T00:00:00Z'),date==='2026-10-23'?'Mock':'Assessment',null,event,null,'Scheduled',null,null,null,null]);continue;}
 for(const id of ids){
  const key=String(id), f=src.freq[key]; if(!f)throw Error('Missing frequency source '+id);
  const previous=src.md[key]||src.done[key]||src.pool[key]?.solved==='Yes'||seen.has(id);
  let type=previous?'Re-do':'New';
  if(date==='2026-11-14')type='Rehearsal';
  if(date==='2026-11-16')type='Warm-up';
  rows.push([new Date(date+'T00:00:00Z'),type,id,f.Title,f.Difficulty[0]+f.Difficulty.slice(1).toLowerCase(),'Not Started',null,null,null,null]);
  audit.push({date,id,title:f.Title,type,frequency:Number(f['Frequency %']),historicallySolved:!!previous});
  seen.add(id);
 }
}
const w=Workbook.create(); const s=w.worksheets.add('Coding Readiness Roadmap');s.showGridLines=false;s.tabColor='#202428';
const headers=['Date','Task Type','LC #','Problem','Difficulty','Status','Result','Actual Min','Confidence (1-5)','Notes'];
s.getRange('A1:J1').values=[headers];
s.getRange(`A2:J${rows.length+1}`).values=rows;
const last=rows.length+1,all=s.getRange(`A1:J${last}`);
all.format.font={name:'Arial',size:11,color:'#202428'};all.format.verticalAlignment='center';all.format.rowHeight=37;
const widths={A:142,B:105,C:58,D:395,E:80,F:110,G:105,H:80,I:105,J:330};
for(const [c,width] of Object.entries(widths))s.getRange(`${c}1:${c}${last}`).format.columnWidthPx=width;
s.getRange(`A2:A${last}`).setNumberFormat('ddd, mmm d');
s.getRange(`A2:A${last}`).format.horizontalAlignment='center';
s.getRange(`C2:C${last}`).format.horizontalAlignment='center';
s.getRange(`C2:C${last}`).setNumberFormat('0');
s.getRange(`H2:I${last}`).setNumberFormat('0');
s.getRange(`D2:D${last}`).format.wrapText=true;
s.getRange('A1:J1').format={fill:'#202428',font:{name:'Arial',size:11,bold:true,color:'#FFFFFF'},rowHeight:42,wrapText:true,horizontalAlignment:'center',verticalAlignment:'center'};
s.freezePanes.freezeRows(1);
const t=s.tables.add(`A1:J${last}`,true,'CodingRoadmap');t.style='TableStyleLight9';
// Explicit fills retain the source's restrained blue bands while keeping user inputs clear.
let prior='',group=-1;
rows.forEach((row,i)=>{
 const r=i+2,key=row[0].toISOString().slice(0,10);if(key!==prior){group++;prior=key;}
 s.getRange(`A${r}:E${r}`).format.fill=group%2===0?'#E7F2F8':'#FFFFFF';
 s.getRange(`F${r}:J${r}`).format.fill=group%2===0?'#FFF8E8':'#FFFCF4';
 if(row[1]==='Mock'||row[1]==='Assessment'){
  s.getRange(`A${r}:F${r}`).format.fill='#DCE8F2';
  s.getRange(`A${r}:F${r}`).format.font.bold=true;
 }
});
s.getRange(`F2:F${last}`).dataValidation={rule:{type:'list',values:['Not Started','In Progress','Done','Review Needed','Scheduled','Skipped']}};
s.getRange(`G2:G${last}`).dataValidation={rule:{type:'list',values:['Clean','With Hint','Incorrect','Not Finished']}};
s.dataValidations.add({range:`I2:I${last}`,rule:{type:'whole',operator:'between',formula1:1,formula2:5}});
s.getRange(`F2:F${last}`).conditionalFormats.add('containsText',{text:'Done',format:{fill:'#E4EFDF',font:{color:'#28542B'}}});
w.recalculate();
console.log((await w.inspect({kind:'table',range:'Coding Readiness Roadmap!A1:J10',tableMaxRows:10,tableMaxCols:10,maxChars:3800})).ndjson);
console.log((await w.inspect({kind:'match',searchTerm:'#REF!|#DIV/0!|#VALUE!|#NAME\\?|#N/A|#NUM!',options:{useRegex:true,maxResults:10},maxChars:1000})).ndjson);
if(s.getRange(`J2:J${last}`).values.some(r=>r[0]!==null&&r[0]!==''))throw Error('Notes must be empty');
for(const [file,range] of [['preview-start.png','A1:J12'],['preview-end.png',`A${last-11}:J${last}`]]){
 const p=await w.render({sheetName:'Coding Readiness Roadmap',range,scale:1,format:'png'});
 await fs.writeFile(new URL(file,out),new Uint8Array(await p.arrayBuffer()));
}
await (await SpreadsheetFile.exportXlsx(w)).save(new URL('coding_readiness_roadmap.xlsx',out).pathname.replace(/^\/(\w:)/,'$1'));
await fs.writeFile(new URL('selection-audit.json',out),JSON.stringify(audit,null,2));
console.log(JSON.stringify({rows:rows.length,problemAttempts:audit.length,distinctProblems:seen.size,new:audit.filter(x=>x.type==='New').length,repeat:audit.filter(x=>x.type==='Re-do').length,last,output:'coding_readiness_roadmap.xlsx'}));

