# English-first SEO landing pages (US buyers are ~85% of Gumroad views). Run: python3 en_landing.py
import json,html,re
E=html.escape
U='https://buckyproducts.github.io/shop/';G='https://buckylittleshop.gumroad.com/l/'
CSS=re.search(r"CSS='''(.*?)'''",open('landing.py').read(),re.S).group(1)
P={x['k']:x for x in json.load(open('payhip.json'))}
def card(k,note=None):
  x=P[k];price='FREE' if x['pr'] in('0','0.00') else '$'+x['pr']+' USD'
  return f'''<div class="card"><img src="../img/{k}.webp" width="800" height="800" loading="lazy" alt="{E(x['en'])}"><div><h3>{E(x['en'])}</h3><p>{E(note or x['den'])}</p><span class="price">{price}</span><a class="btn" href="{G+x['g']}" rel="noopener">{'Get it free' if price=='FREE' else 'Buy and download'}</a></div></div>'''
def page(slug,title,desc,h1,lead,top,body,rest,faq,crumb):
  url=U+slug+'/'
  ld={"@context":"https://schema.org","@graph":[{"@type":"WebPage","name":title,"url":url,"description":desc,"inLanguage":"en"},
   {"@type":"BreadcrumbList","itemListElement":[{"@type":"ListItem","position":1,"name":"Bucky Little Shop","item":U},{"@type":"ListItem","position":2,"name":crumb,"item":url}]},
   {"@type":"FAQPage","mainEntity":[{"@type":"Question","name":q,"acceptedAnswer":{"@type":"Answer","text":a}} for q,a in faq]}]}
  return f'''<!doctype html><html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<title>{E(title)}</title><meta name="description" content="{E(desc)}"><link rel="canonical" href="{url}">
<meta property="og:type" content="article"><meta property="og:url" content="{url}"><meta property="og:title" content="{E(title)}"><meta property="og:description" content="{E(desc)}"><meta property="og:image" content="{U}img/{top[0]}.webp">
<link rel="icon" href="../favicon.ico"><meta name="theme-color" content="#7a4a26"><style>{CSS}</style>
<script type="application/ld+json">{json.dumps(ld,ensure_ascii=False)}</script></head><body>
<header><a href="../"><img src="../img/logo.webp" alt="Bucky Little Shop" width="40" height="40"></a><a href="../">Bucky Little Shop</a></header>
<main><p><a href="../">Home</a> › {E(crumb)}</p><h1>{E(h1)}</h1><p class="lead">{lead}</p>
<div class="cta">{"".join(card(k) for k in top)}</div>{body}
<h2>More Christmas printables, ready to download</h2><div class="cta">{"".join(card(k) for k in rest)}</div>
<h2>Questions</h2>{"".join(f"<details><summary>{E(q)}</summary><p>{E(a)}</p></details>" for q,a in faq)}
<p>¿Prefieres en español? Mira <a href="../posadas-navidad/">posadas y Navidad</a>, <a href="../tarjetas-navidenas-gratis/">tarjetas navideñas gratis</a> y <a href="../ideas-intercambio-regalos/">ideas para intercambio de regalos</a>.</p></main>
<footer>© 2026 Bucky Little Shop · Instant download · Digital files, nothing is shipped · <a href="../">See the whole shop</a></footer></body></html>'''
body='''<h2>Christmas printables for every part of the season</h2>
<ul><li><b>Party games:</b> charades, Would You Rather and Christmas Scattergories work for family nights, classrooms and office parties. Print one copy per player and you're ready.</li>
<li><b>Cards and gift tags:</b> print on cardstock, fold and write a name. It's the fastest way to finish wrapping on December 23.</li>
<li><b>Quiet-time activities:</b> word searches, crosswords and coloring pages keep kids busy on winter break and give grandparents a large-print option.</li>
<li><b>Planning ahead:</b> a 2027 planner and calendar help you start January organized.</li></ul>
<h2>How to print them at home</h2>
<ol><li>Download the PDF right after checkout (or right away for the free kit).</li><li>Print on US Letter or A4. Use plain paper for games and puzzles, and cardstock (65 to 110 lb) for cards and tags.</li><li>Choose "Actual size" or "Fit to page" in your printer settings.</li><li>Cut along the lines, and you're done. Print as many copies as you need for your own home or classroom.</li></ol>
<p>Every file is bilingual (English and Spanish), so it works for dual-language classrooms and bilingual families too.</p>'''
faq=[("Are these Christmas printables free?","The Christmas Mini Kit is free. The other kits are paid instant downloads between $3.99 and $29."),
 ("What paper size are they?","US Letter, and most also come in A4. Print at home or at any copy shop."),
 ("Will anything be shipped to me?","No. These are digital PDF files you download and print yourself."),
 ("Can I use them in my classroom?","Yes. Personal and classroom use is fine; please don't resell the files.")]
h=page("christmas-printables","Christmas Printables: Free Games, Cards, Tags and Puzzles (PDF) | Bucky",
 "Christmas printables to download today: a free Christmas mini kit with party games, cards and gift tags, plus large-print Christmas puzzles, kids activities and a 2027 planner. US Letter and A4.",
 "Christmas printables for home, class and parties",
 "Start with the <b>free Christmas mini kit</b> (games, a card, 8 gift tags and a coloring page), then add cards, puzzles and party games. Instant PDF download, US Letter and A4.",
 ["kit-navideno-gratis","tarjetas-navidad"],body,
 ["pasatiempos-navidad","combo-posada","kids-mega","combo-gratitud","devocional-adviento","planner","mega"],faq,"Christmas printables")
open("christmas-printables/index.html","w").write(h)
s=open("sitemap.xml").read()
if "christmas-printables/" not in s: open("sitemap.xml","w").write(s.replace("</urlset>",f"<url><loc>{U}christmas-printables/</loc><lastmod>2026-10-24</lastmod></url></urlset>"))
print("ok")
