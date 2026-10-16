const {chromium}=require("/workspace/.pw/node_modules/playwright");
(async()=>{const b=await chromium.launch();const p=await b.newPage();
for(const [s,o] of [["letter","Calendario-2027-Imprimible-Gratis_Bucky_Carta-Letter.pdf"],["A4","Calendario-2027-Imprimible-Gratis_Bucky_A4.pdf"]]){
await p.goto("file://"+__dirname+"/calendario-2027/_src_"+s+".html");await p.waitForTimeout(500);await p.pdf({path:__dirname+"/calendario-2027/"+o,preferCSSPageSize:true,printBackground:true});}
await b.close();})();
