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

# --- Christmas gift tags (2026-10-25) ---
body='''<h2>Printable Christmas gift tags: why they beat store-bought</h2>
<p>A pack of foil tags runs out the night you need it. Printable tags don't: download the PDF once and print another sheet whenever the pile of presents grows. They also match, so the whole stack under the tree looks planned even if you wrapped it at midnight.</p>
<h2>How to print and attach gift tags</h2>
<ol><li>Download the PDF (the free mini kit comes with 8 tags, the Christmas Cards set with 16).</li>
<li>Print on white cardstock, 65 to 110 lb, at "Actual size" so the tags keep their shape. Plain paper works too if you glue the tag onto the package instead of hanging it.</li>
<li>Cut along the lines with scissors or a paper trimmer. A round hole punch at the top corner turns any tag into a hanging tag.</li>
<li>Thread twine, ribbon or baker's string through the hole, or use a strip of double-sided tape to stick the tag flat on the paper.</li></ol>
<h2>Quick ideas</h2>
<ul><li><b>Teacher and neighbor gifts:</b> pair a tag with cookies, a candle or a mug and you have a gift in five minutes.</li>
<li><b>Secret Santa and gift exchanges:</b> write the number or code on the back so nobody peeks before the reveal.</li>
<li><b>Bilingual families:</b> the tags come in English and Spanish, so you can write "Merry Christmas" for one side of the family and "Feliz Navidad" for the other.</li>
<li><b>Matching cards:</b> the Christmas Cards set includes 12 folding cards with the same look as its tags.</li></ul>'''
faq=[("Are there free printable Christmas gift tags here?","Yes. The free Christmas Mini Kit includes 8 printable gift tags, plus party games, a card and a coloring page."),
 ("What paper should I use for gift tags?","White cardstock between 65 and 110 lb holds up best on ribbon. Regular printer paper is fine if you tape or glue the tag flat."),
 ("Can I print the tags more than once?","Yes. Print as many as you need for your own gifts, home or classroom. Please don't resell the files."),
 ("Is anything shipped?","No. These are digital PDF files you download and print at home or at a copy shop.")]
h=page("christmas-gift-tags","Printable Christmas Gift Tags (Free + Bilingual PDF) | Bucky",
 "Printable Christmas gift tags you can download today: 8 free tags in the Christmas Mini Kit, plus 16 matching tags and 12 cards in English and Spanish. Print on cardstock, US Letter and A4.",
 "Printable Christmas gift tags, free and ready to print",
 "Grab <b>8 free Christmas gift tags</b> in the mini kit, or get <b>16 tags plus 12 matching folding cards</b> in the Christmas Cards set. Instant PDF download, English and Spanish, US Letter and A4.",
 ["kit-navideno-gratis","tarjetas-navidad"],body,
 ["bucky-stickers","tarjetas-felicitacion","combo-posada","combo-gratitud","mega"],faq,"Christmas gift tags")
import os;os.makedirs("christmas-gift-tags",exist_ok=True)
open("christmas-gift-tags/index.html","w").write(h)
s=open("sitemap.xml").read()
if "christmas-gift-tags/" not in s: open("sitemap.xml","w").write(s.replace("</urlset>",f"<url><loc>{U}christmas-gift-tags/</loc><lastmod>2026-10-25</lastmod></url></urlset>"))
print("ok gift tags")

# --- Christmas party games (2026-10-25, FB group posts 12:30 slot) ---
body='''<h2>Printable Christmas party games that work for any crowd</h2>
<p>The best Christmas party games need no setup, no app and no extra shopping: print one sheet per player, hand out pens and start. That's why printable games work so well for family nights, classroom parties, office get-togethers and church events.</p>
<ul><li><b>Christmas charades:</b> great for mixed ages. Cut the cards, fold them into a bowl and let teams act out a reindeer, a snowman or wrapping a present.</li>
<li><b>Christmas Would You Rather:</b> an easy icebreaker for office parties and teens. No winners or losers, just good conversation.</li>
<li><b>Christmas Scattergories:</b> pick a letter and fill in a Christmas food, song or gift in under a minute. Works for 3 to 30 players.</li>
<li><b>Word searches and crosswords:</b> a quiet option for grandparents and kids who'd rather sit out the loud games. The large-print versions are easy on the eyes.</li>
<li><b>Gift exchange games:</b> pair a White Elephant or Secret Santa round with printable rules so nobody argues about stealing.</li></ul>
<h2>How to run a printable game night</h2>
<ol><li>Download the PDF and print on US Letter or A4 plain paper. Cardstock is nice for charades cards you'll reuse.</li>
<li>Print one game sheet per player or per team, plus a few spares.</li>
<li>Set a timer on your phone (60 to 90 seconds per round keeps the energy up).</li>
<li>Have a small prize ready: a candy cane, a mug or first pick at the gift exchange.</li></ol>
<p>Every game comes in English and Spanish, so bilingual families and dual-language classrooms can play together.</p>'''
faq=[("Are there free printable Christmas party games?","Yes. The free Christmas Mini Kit includes Christmas charades, Would You Rather and Christmas Scattergories, plus a card, gift tags and a coloring page."),
 ("What Christmas games work for adults at an office party?","Would You Rather, Christmas Scattergories and charades are quick, need no setup and work for large groups. Print a sheet per person and set a timer."),
 ("What games work for kids and families?","Charades, word searches and coloring pages work for all ages. The Kids Activity Mega Pack adds 60 screen-free pages for winter break."),
 ("Is anything shipped?","No. These are digital PDF files you download and print at home or at a copy shop.")]
h=page("christmas-party-games","Printable Christmas Party Games (Free PDF for Family, Kids, Office) | Bucky",
 "Printable Christmas party games to download today: free Christmas charades, Would You Rather and Scattergories, plus 13 more Christmas games and large-print puzzles. English and Spanish, US Letter and A4.",
 "Printable Christmas party games for family, kids and office parties",
 "Start with the <b>free Christmas Mini Kit</b> (charades, Would You Rather and Christmas Scattergories), then add <b>13 more Christmas games</b> or large-print puzzles. Instant PDF download, English and Spanish.",
 ["kit-navideno-gratis","combo-gratitud"],body,
 ["pasatiempos-navidad","combo-posada","kids-mega","rompecabezas-letra-grande","mega"],faq,"Christmas party games")
os.makedirs("christmas-party-games",exist_ok=True)
open("christmas-party-games/index.html","w").write(h)
s=open("sitemap.xml").read()
if "christmas-party-games/" not in s: open("sitemap.xml","w").write(s.replace("</urlset>",f"<url><loc>{U}christmas-party-games/</loc><lastmod>2026-10-25</lastmod></url></urlset>"))
print("ok party games")

# --- Secret Santa (2026-10-25, FB Page 8 PM slot) ---
for k,g,pp,pr,es,en,des,den,c in [('secret-santa','mfqlci','PGsBK','6.99','Kit de intercambio de regalos','Secret Santa Kit','','Draw cards, wish lists and gift tags for your gift exchange. EN + ES.','xmas'),
 ('bundle','bkgnnd','0NkMo','15.99','Paquete fiesta navideña','Christmas Party Bundle','','The complete pack: party games, gift exchange kit and decor. Best value.','xmas'),
 ('games','cnexgy','yR2hw','9.99','Juegos para fiesta navideña','Christmas Party Games','','Printable games for office, family and classroom parties.','xmas')]:
  P.setdefault(k,{'k':k,'g':g,'pr':pr,'en':en,'den':den})
body='''<h2>How to run a Secret Santa that actually works</h2>
<ol><li><b>Set the budget and the date.</b> Agree on one price limit for everyone ($10, $15, $20 or $25 are the most common) and the day you'll swap gifts.</li>
<li><b>Hand out wish lists.</b> Each person fills in a short list: favorite color, snack, hobby, size and one thing they don't want. It saves everyone from guessing.</li>
<li><b>Draw names.</b> Write each name on a draw card, fold it and put them all in a bowl or hat. If someone pulls their own name, they put it back and draw again.</li>
<li><b>Keep it secret.</b> Label each gift with a printable tag that shows only the recipient's name, so the giver stays a mystery until the reveal.</li>
<li><b>Reveal.</b> At the party, everyone guesses who their Secret Santa was before opening.</li></ol>
<h2>Secret Santa gift ideas by budget</h2>
<ul><li><b>Under $10:</b> hot cocoa and a mug, fun socks, a scented candle, a small succulent, a deck of cards or a box of favorite candy.</li>
<li><b>Under $15:</b> an insulated tumbler, a coffee or tea sampler, a cozy throw-size blanket, a puzzle or a nice notebook and pen.</li>
<li><b>Under $25:</b> a small Bluetooth speaker, a spa or bath kit, LED string lights, a board game or a plant with a pretty pot.</li></ul>
<p>These are generic ideas with no affiliate links, so buy wherever you like.</p>
<h2>Office, family and classroom tips</h2>
<ul><li><b>Office:</b> keep gifts neutral and set the budget in the invite. A printed wish list helps coworkers who barely know each other.</li>
<li><b>Family:</b> draw names after Thanksgiving dinner so everyone has a month to shop.</li>
<li><b>Classroom:</b> keep the budget low ($5 to $10) and let kids decorate their own tags.</li>
<li><b>Long distance:</b> email the draw results privately and mail gifts with the printed tag inside.</li></ul>
<p>Every file is bilingual, English and Spanish. ¿Lo buscas en español? Mira nuestras <a href="../ideas-intercambio-regalos/">ideas para intercambio de regalos</a>.</p>'''
faq=[("What is a good Secret Santa budget?","Most groups choose $10 to $25. What matters most is that everyone agrees on the same limit before the draw."),
 ("How do you draw names for Secret Santa?","Write every name on a card, fold them into a bowl and have each person draw one in private. If someone draws their own name, they put it back and draw again. The Secret Santa Kit includes printable draw cards."),
 ("What should I give a coworker I don't know well?","Something useful and neutral: a mug with cocoa, a candle, a tumbler, a plant or a nice notebook."),
 ("Is anything shipped?","No. These are digital PDF files you download and print at home or at a copy shop.")]
h=page("secret-santa","Secret Santa Printables: Draw Cards, Wish Lists, Gift Tags + Ideas | Bucky",
 "Plan a Secret Santa in minutes: printable draw cards, wish lists and gift tags, plus gift ideas under $10, $15 and $25 for office, family and classroom exchanges. English and Spanish PDF.",
 "Secret Santa printables and gift ideas for office, family and class",
 "Run your gift exchange without the stress: the <b>Secret Santa Kit</b> has <b>draw cards, wish lists and gift tags</b> ready to print, and below you'll find <b>gift ideas by budget</b>. Instant PDF download, English and Spanish, US Letter and A4.",
 ["secret-santa","kit-navideno-gratis"],body,
 ["tarjetas-navidad","games","bundle","combo-posada","mega"],faq,"Secret Santa")
os.makedirs("secret-santa",exist_ok=True)
open("secret-santa/index.html","w").write(h)
s=open("sitemap.xml").read()
if "/secret-santa/" not in s: open("sitemap.xml","w").write(s.replace("</urlset>",f"<url><loc>{U}secret-santa/</loc><lastmod>2026-10-25</lastmod></url></urlset>"))
print("ok secret santa")
