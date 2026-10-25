# Free one-page 2027 calendar, US English edition with US holidays -> printable-calendar-2027/*.pdf. Run: python3 cal2027us.py && node cal2027us.js
import calendar,base64,io
from PIL import Image
im=Image.open("/workspace/buckyproducts/etsy/_shared/bucky-poses/v3-derived/cut_wave.png");im.thumbnail((360,360));b=io.BytesIO();im.save(b,"PNG",optimize=True)
BK="data:image/png;base64,"+base64.b64encode(b.getvalue()).decode()
MN=["January","February","March","April","May","June","July","August","September","October","November","December"]
COL=["#E76F51","#F4A261","#2A9D8F","#8E7DBE","#E9C46A","#4CC9F0","#F28482","#7FB069","#E76F51","#F4A261","#8E7DBE","#2A9D8F"]
FED={(1,1),(1,18),(2,15),(5,31),(6,19),(7,4),(9,6),(10,11),(11,11),(11,25),(12,25)}
SPEC={(2,14),(3,17),(3,28),(5,9),(6,20),(10,31),(12,31)}
def month(m):
  rows=calendar.Calendar(6).monthdayscalendar(2027,m)
  h="".join(f"<th>{d}</th>" for d in ["S","M","T","W","T","F","S"])
  body="".join("<tr>"+"".join(f'<td class="{"h" if (m,d) in FED else "s" if (m,d) in SPEC else ""}">{d or ""}</td>' for d in r)+"</tr>" for r in rows)
  return f'<div class="m"><div class="mt" style="background:{COL[m-1]}">{MN[m-1]}</div><table><tr>{h}</tr>{body}</table></div>'
def html(size):
  w,h=("8.5in","11in") if size=="letter" else ("210mm","297mm")
  return f'''<!doctype html><html><head><meta charset="utf-8"><style>@page{{size:{w} {h};margin:0}}body{{margin:0;font-family:"Baloo 2","Nunito",system-ui,sans-serif;color:#3b2414}}
.p{{width:{w};height:{h};box-sizing:border-box;overflow:hidden;padding:.45in .45in .35in;display:flex;flex-direction:column}}
.hd{{display:flex;align-items:center;justify-content:space-between}}.hd h1{{font-size:38pt;margin:0;line-height:1;color:#7a4a26}}.hd p{{margin:2px 0 0;font-size:12pt}}.hd img{{height:1in}}
.g{{display:grid;grid-template-columns:repeat(3,1fr);gap:.12in;flex:1;min-height:0;margin-top:.12in}}.m{{border:1.5px solid #e8d5bf;border-radius:10px;overflow:hidden}}.mt{{color:#fff;font-weight:800;font-size:12pt;padding:3px 8px}}
table{{width:100%;border-collapse:collapse;font-size:9.5pt;text-align:center}}th{{font-size:8pt;color:#a0522d;padding:2px 0}}td{{padding:1px 0;height:13px}}td.h{{background:#FDE2D6;border-radius:50%;font-weight:800}}td.s{{box-shadow:inset 0 0 0 1.5px #2A9D8F;border-radius:50%}}
.ft{{display:flex;justify-content:space-between;align-items:center;font-size:8.5pt;margin-top:.08in}}.ft b{{color:#E76F51}}</style></head><body><div class="p">
<div class="hd"><div><h1>2027 Calendar</h1><p>Free printable · one page · weeks start on Sunday</p></div><img src="{BK}" alt="Bucky"></div>
<div class="g">{"".join(month(m) for m in range(1,13))}</div>
<div class="ft"><span><b>●</b> US federal holidays: Jan 1, Jan 18, Feb 15, May 31, Jun 19, Jul 4, Sep 6, Oct 11, Nov 11, Nov 25, Dec 25 &nbsp; ○ Valentine's, St. Patrick's, Easter (Mar 28), Mother's Day, Father's Day, Halloween, New Year's Eve</span></div>
<div class="ft"><span>© 2026 Bucky Little Shop · Personal &amp; classroom use. Do not resell.</span><span>Plan the whole year: <b>buckyproducts.github.io/shop/printable-calendar-2027/</b></span></div></div></body></html>'''
for s in ("letter","A4"):open(f"printable-calendar-2027/_src_{s}.html","w").write(html(s))
print("ok")
