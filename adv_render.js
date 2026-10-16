// Render Advent day pages directly from the bundle1 source HTML (text-based, fonts subset per file).
const {chromium}=require("/workspace/.pw/node_modules/playwright");
const S="/workspace/buckyproducts/etsy/bundle1/src/";const P=[3,4,5,6,7,18,19,20,22,23,24,25,57,61,62,64,66,68,69,70,71,72,73,75];
(async()=>{const b=await chromium.launch();const pe=await b.newPage(),ps=await b.newPage();
await pe.goto("file://"+S+"en_letter.html");await ps.goto("file://"+S+"es_letter.html");await pe.waitForTimeout(800);await ps.waitForTimeout(800);
for(let i=0;i<P.length;i++){const d=String(i+1).padStart(2,"0");
 await ps.pdf({path:`/workspace/tmp/adv/es_${d}.pdf`,preferCSSPageSize:true,printBackground:true,pageRanges:String(P[i])});
 await pe.pdf({path:`/workspace/tmp/adv/en_${d}.pdf`,preferCSSPageSize:true,printBackground:true,pageRanges:String(P[i])});}
await b.close();})();
