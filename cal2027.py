# Free one-page 2027 calendar (ES/EN) -> calendario-2027/*.pdf + preview png. Run: python3 cal2027.py && node cal2027.js
import calendar,base64,json
from PIL import Image
import io
im=Image.open("/workspace/buckyproducts/etsy/_shared/bucky-poses/v3-derived/cut_wave.png");im.thumbnail((360,360));b=io.BytesIO();im.save(b,"PNG",optimize=True)
BK="data:image/png;base64,"+base64.b64encode(b.getvalue()).decode()
ME=["Enero","Febrero","Marzo","Abril","Mayo","Junio","Julio","Agosto","Septiembre","Octubre","Noviembre","Diciembre"]
MN=["January","February","March","April","May","June","July","August","September","October","November","December"]
COL=["#E76F51","#F4A261","#2A9D8F","#8E7DBE","#E9C46A","#4CC9F0","#F28482","#7FB069","#E76F51","#F4A261","#8E7DBE","#2A9D8F"]
HOL={(1,1),(2,1),(3,15),(5,1),(9,16),(11,15),(12,12),(12,25),(11,2),(1,6),(5,10),(4,30)}
def month(m):
  c=calendar.Calendar(6);rows=c.monthdayscalendar(2027,m)
  h="".join(f"<th>{d}</th>" for d in ["D","L","M","M","J","V","S"])
  body="".join("<tr>"+"".join(f'<td class="{"h" if (m,d) in HOL else ""}">{d or ""}</td>' for d in r)+"</tr>" for r in rows)
  return f'<div class="m"><div class="mt" style="background:{COL[m-1]}">{ME[m-1]} <span>/ {MN[m-1]}</span></div><table><tr>{h}</tr>{body}</table></div>'
def html(size):
  w,h=("8.5in","11in") if size=="letter" else ("210mm","297mm")
  return f'''<!doctype html><html><head><meta charset="utf-8"><style>@page{{size:{w} {h};margin:0}}body{{margin:0;font-family:"Baloo 2","Nunito",system-ui,sans-serif;color:#3b2414}}
.p{{width:{w};height:{h};box-sizing:border-box;overflow:hidden;padding:.45in .45in .35in;display:flex;flex-direction:column}}
.hd{{display:flex;align-items:center;justify-content:space-between}}.hd h1{{font-size:38pt;margin:0;line-height:1;color:#7a4a26}}.hd p{{margin:2px 0 0;font-size:12pt}}.hd img{{height:1in}}
.g{{display:grid;grid-template-columns:repeat(3,1fr);gap:.12in;flex:1;min-height:0;margin-top:.12in}}.m{{border:1.5px solid #e8d5bf;border-radius:10px;overflow:hidden}}.mt{{color:#fff;font-weight:800;font-size:12pt;padding:3px 8px}}.mt span{{font-weight:600;font-size:9pt;opacity:.9}}
table{{width:100%;border-collapse:collapse;font-size:9.5pt;text-align:center}}th{{font-size:8pt;color:#a0522d;padding:2px 0}}td{{padding:1px 0;height:13px}}td.h{{background:#FDE2D6;border-radius:50%;font-weight:800}}
.ft{{display:flex;justify-content:space-between;align-items:center;font-size:9pt;margin-top:.1in}}.ft b{{color:#E76F51}}</style></head><body><div class="p">
<div class="hd"><div><h1>Calendario 2027</h1><p>2027 Calendar · gratis para imprimir / free printable · D = Domingo / Sunday</p></div><img src="{BK}" alt="Bucky"></div>
<div class="g">{"".join(month(m) for m in range(1,13))}</div>
<div class="ft"><span>● Días festivos y fechas especiales en México / Mexican holidays & special dates</span><span>¿Quieres organizar todo tu 2027? <b>Agenda 2027 completa: buckyproducts.github.io/shop/calendario-2027/</b></span></div>
<div class="ft"><span>© 2026 Bucky Little Shop · Uso personal y en el salón. No se permite revender. / Personal & classroom use. Do not resell.</span></div></div></body></html>'''
for s in ("letter","A4"):open(f"calendario-2027/_src_{s}.html","w").write(html(s))
print("ok")
