import csv,json, pathlib, openpyxl
root=pathlib.Path(__file__).resolve().parents[2]
w=openpyxl.load_workbook('C:/Users/radme/Downloads/google_interview_master_tracker.xlsm',data_only=True)
pool={int(r[0]):{'title':r[1],'difficulty':r[2],'frequency':r[3],'solved':r[5]} for r in list(w['Question Pool'].values)[5:] if isinstance(r[0],(int,float))}
freq={int(r['ID']):r for r in csv.DictReader((root/'companywise-questions/google-questions-30_days.csv').open(encoding='utf-8-sig'))}
done={int(r[4]):{'status':r[10],'result':r[11],'confidence':r[13]} for r in list(w['Daily Plan'].values)[1:] if isinstance(r[4],(int,float)) and (r[10] in ['Done','Review Needed'])}
md={int(p.name.split('-')[0]):p.read_text(encoding='utf-8') for p in (root/'leetcode').glob('*.md')}
(pathlib.Path(__file__).parent/'source.json').write_text(json.dumps({'pool':pool,'freq':freq,'done':done,'md':md}),encoding='utf-8')
print('Read',len(md),'Markdown records;',len(freq),'CSV problems;',len(pool),'workbook pool records;',len(done),'daily-plan attempts.')
