const {chromium}=require("/workspace/.pw/node_modules/playwright");
(async()=>{const b=await chromium.launch();const p=await b.newPage();
for(const [s,o] of [["letter","Free-Printable-2027-Calendar-US-Letter_Bucky.pdf"],["A4","Free-Printable-2027-Calendar-A4_Bucky.pdf"]]){
await p.goto("file://"+__dirname+"/printable-calendar-2027/_src_"+s+".html");await p.waitForTimeout(500);await p.pdf({path:__dirname+"/printable-calendar-2027/"+o,preferCSSPageSize:true,printBackground:true});}
await b.close();})();
