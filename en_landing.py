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
h=page("christmas-printables","Christmas Printables: Free Games, Cards and Gift Tags (PDF)",
 "Christmas printables to download today: a free kit of party games, cards and gift tags, plus large-print puzzles and kids activities. US Letter and A4.",
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
h=page("christmas-gift-tags","Printable Christmas Gift Tags: Free Bilingual PDF | Bucky",
 "Free printable Christmas gift tags: 8 free tags in the Christmas Mini Kit, plus 16 matching tags and 12 cards in English and Spanish. Letter and A4.",
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
h=page("christmas-party-games","Printable Christmas Party Games: Free PDF for Family & Kids",
 "Free printable Christmas party games: charades, Would You Rather and Scattergories, plus 13 more games for family, kids and office. Letter and A4 PDF.",
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
h=page("secret-santa","Secret Santa Printables: Name Slips, Wish Lists & Gift Tags",
 "Printable Secret Santa name slips, wish lists and gift tags, plus gift ideas under $10, $15 and $25 for office, family and class exchanges. Instant PDF.",
 "Secret Santa printables and gift ideas for office, family and class",
 "Run your gift exchange without the stress: the <b>Secret Santa Kit</b> has <b>draw cards, wish lists and gift tags</b> ready to print, and below you'll find <b>gift ideas by budget</b>. Instant PDF download, English and Spanish, US Letter and A4.",
 ["secret-santa","kit-navideno-gratis"],body,
 ["tarjetas-navidad","games","bundle","combo-posada","mega"],faq,"Secret Santa")
os.makedirs("secret-santa",exist_ok=True)
open("secret-santa/index.html","w").write(h)
s=open("sitemap.xml").read()
if "/secret-santa/" not in s: open("sitemap.xml","w").write(s.replace("</urlset>",f"<url><loc>{U}secret-santa/</loc><lastmod>2026-10-25</lastmod></url></urlset>"))
print("ok secret santa")

# --- Free printable 2027 calendar, US edition (2026-10-25, nightly) ---
for k,g,pr,en,den in [('organizador-hogar','hefzy','6.99','Home Organizer Binder Printable','Bills, passwords, contacts, meals and cleaning pages in one binder.'),
 ('sheets','zeovm','9.99','Budget, Meal & Wedding Spreadsheet Bundle','Monthly budget, meal planner and wedding planner templates.')]:
  P.setdefault(k,{'k':k,'g':g,'pr':pr,'en':en,'den':den})
D='Free-Printable-2027-Calendar-'
body=f'''<h2>Download the free 2027 calendar</h2>
<p><img src="preview.webp" width="800" height="1035" loading="lazy" alt="Free printable 2027 calendar on one page with US holidays marked" style="max-width:340px;width:100%;border:1px solid #e8d5bf;border-radius:10px"></p>
<p><a class="btn" href="{D}US-Letter_Bucky.pdf" download>Download US Letter PDF</a> &nbsp; <a class="btn" href="{D}A4_Bucky.pdf" download>Download A4 PDF</a></p>
<p>No email, no sign-up. All 12 months fit on one page, weeks start on Sunday, and every US federal holiday is circled.</p>
<h2>2027 US federal holidays</h2>
<ul><li>New Year's Day: Friday, January 1</li><li>Martin Luther King Jr. Day: Monday, January 18</li><li>Presidents' Day: Monday, February 15</li><li>Memorial Day: Monday, May 31</li><li>Juneteenth: Saturday, June 19</li><li>Independence Day: Sunday, July 4</li><li>Labor Day: Monday, September 6</li><li>Columbus Day / Indigenous Peoples' Day: Monday, October 11</li><li>Veterans Day: Thursday, November 11</li><li>Thanksgiving: Thursday, November 25</li><li>Christmas Day: Saturday, December 25</li></ul>
<p>When a holiday falls on a weekend, the day off is usually moved: Juneteenth to Friday, June 18, Independence Day to Monday, July 5, and Christmas to Friday, December 24. Check with your employer or school.</p>
<h2>Other 2027 dates people plan around</h2>
<ul><li>Valentine's Day: Sunday, February 14</li><li>St. Patrick's Day: Wednesday, March 17</li><li>Easter: Sunday, March 28</li><li>Mother's Day: Sunday, May 9</li><li>Father's Day: Sunday, June 20</li><li>Halloween: Sunday, October 31</li></ul>
<h2>How to print it</h2>
<ol><li>Pick US Letter (USA, Canada, Mexico) or A4 (most other countries).</li><li>Print at "Actual size" or "Fit to page". Plain paper works; cardstock lasts all year on the fridge.</li><li>Want more room to write? The 2027 Planner below has monthly and weekly pages.</li></ol>
<p>¿Lo quieres con los días festivos de México? Descarga el <a href="../calendario-2027/">calendario 2027 gratis en español</a>.</p>'''
faq=[("Is this 2027 calendar really free?","Yes. Download the PDF in US Letter or A4 with no email or sign-up. Print as many copies as you need for home or class."),
 ("Does the 2027 calendar include US holidays?","Yes. All 11 federal holidays are circled, and Valentine's Day, St. Patrick's Day, Easter, Mother's Day, Father's Day, Halloween and New Year's Eve are marked."),
 ("When is Easter in 2027?","Easter Sunday is March 28, 2027."),
 ("When is Thanksgiving 2027?","Thanksgiving is Thursday, November 25, 2027.")]
h=page("printable-calendar-2027","Free Printable 2027 Calendar with US Holidays (PDF) | Bucky",
 "Free one-page 2027 calendar with all US federal holidays plus Easter, Mother's Day and Halloween. Instant PDF in US Letter and A4, no sign-up.",
 "Free printable 2027 calendar with US holidays",
 "Download a <b>free one-page 2027 calendar</b> with every <b>US federal holiday</b> circled. US Letter and A4 PDF, no sign-up. Need more space? The <b>2027 Planner</b> has monthly and weekly pages.",
 ["planner","combo-posada"],body,
 ["organizador-hogar","sheets","kit-navideno-gratis","mega"],faq,"2027 calendar")
h=h.replace("<h2>More Christmas printables, ready to download</h2>","<h2>More printables to get organized</h2>")
open("printable-calendar-2027/index.html","w").write(h)
s=open("sitemap.xml").read()
if "/printable-calendar-2027/" not in s: open("sitemap.xml","w").write(s.replace("</urlset>",f"<url><loc>{U}printable-calendar-2027/</loc><lastmod>2026-10-25</lastmod></url></urlset>"))
print("ok calendar")

# --- Advent devotional (2026-10-26, FB Page 10 AM slot) ---
body='''<h2>What is Advent?</h2>
<p>Advent is the season of waiting and preparing for Christmas. The word comes from the Latin <i>adventus</i>, "arrival" or "coming." Many churches begin Advent four Sundays before Christmas, so in 2026 it starts on <b>Sunday, November 29</b>. Many families simply count down from December 1 to December 24 instead. Traditionally the four weeks focus on <b>hope, peace, joy and love</b>, and many homes light one more candle on an Advent wreath each Sunday.</p>
<h2>How to use a daily Advent devotional with your family</h2>
<ol><li><b>Pick one time and keep it.</b> Breakfast, after dinner or bedtime all work. Ten minutes a day is enough, and doing it at the same time every day is what makes it stick.</li>
<li><b>Read the verse out loud.</b> Let a different person read each day. Younger kids can repeat a short phrase after a parent.</li>
<li><b>Read the reflection and ask one question.</b> "What does this verse tell us about God?" or "Who could we help this week?" One question gets a better conversation than five.</li>
<li><b>Pray together.</b> Use the printed prayer, or let each person add one sentence of thanks.</li>
<li><b>Do the action.</b> Each day has a small step: call a grandparent, share a snack, write a kind note. This is the part kids remember.</li></ol>
<h2>Tips for families with kids</h2>
<ul><li><b>Make it visible.</b> Clip the day's page to the fridge or keep the printed set in a basket by the table with a candle.</li>
<li><b>Let kids color or draw.</b> While an adult reads, little ones can color a Bible verse page. They listen better with busy hands.</li>
<li><b>Missed a day? Just keep going.</b> Read two pages the next day, or skip ahead. Advent is about drawing near, not keeping a perfect record.</li>
<li><b>Hide a verse card.</b> Tuck a Bible verse card into a lunchbox, a coat pocket or under a pillow as a little Advent surprise.</li>
<li><b>End on Christmas Eve.</b> Day 24 leads into the Christmas story in Luke 2. Read it together before bed.</li></ul>
<h2>An Advent Bible reading plan you can print</h2>
<p>The <b>Advent Devotional: 24 Days</b> gives you one King James Version verse for each day from December 1 to 24, with a short reflection, a prayer and a simple action. It follows the story from the prophets' promises to the angels and the shepherds, so the whole family reads toward Christmas together. It's a PDF you download right away and print at home, US Letter and A4.</p>
<p>¿Buscas en español? El devocional también tiene versión en español (RV1909), y en nuestro <a href="../adviento/">calendario de Adviento gratis</a> encontrarás un imprimible para cada día de diciembre.</p>'''
faq=[("When does Advent start in 2026?","Many churches begin Advent on the fourth Sunday before Christmas, which is Sunday, November 29, 2026. The devotional runs December 1 to 24, so you can start either way."),
 ("Is this Advent devotional good for kids?","Yes. Each day is short: one verse, a few sentences of reflection, a prayer and a small action. Families read it together in about ten minutes, and older kids can read it on their own."),
 ("Which Bible translation does it use?","The English pages use the King James Version (KJV). The Spanish pages use the Reina-Valera 1909."),
 ("Is anything shipped?","No. These are digital PDF files you download and print at home or at a copy shop.")]
h=page("advent-devotional","Printable Advent Devotional for Families: 24 Days (PDF)",
 "Printable Advent devotional for families and kids: 24 days of KJV Bible readings, Dec 1 to 24, each with a reflection, prayer and action. Letter and A4 PDF.",
 "Printable Advent devotional for families and kids",
 "Count down to Christmas with God's Word: the <b>Advent Devotional</b> gives you <b>24 daily Bible readings</b> (KJV), each with a short reflection, a prayer and a simple action for the whole family. Instant PDF download, US Letter and A4.",
 ["devocional-adviento","kit-navideno-gratis"],body,
 ["tarjetas-biblicas","colorear-biblico","rosario-novenas","mega"],faq,"Advent devotional")
h=h.replace("<h2>More Christmas printables, ready to download</h2>","<h2>More faith printables for the season</h2>")
os.makedirs("advent-devotional",exist_ok=True)
open("advent-devotional/index.html","w").write(h)
s=open("sitemap.xml").read()
if "/advent-devotional/" not in s: open("sitemap.xml","w").write(s.replace("</urlset>",f"<url><loc>{U}advent-devotional/</loc><lastmod>2026-10-26</lastmod></url></urlset>"))
print("ok advent devotional")

# --- Large-print puzzles (2026-10-26, FB group posts 12:30 slot) ---
body='''<h2>Why large-print puzzles help</h2>
<p>Regular puzzle books use small type and crowded grids, which turns a relaxing activity into eye strain. Large-print puzzles use big, bold letters and roomy grids, so readers with low vision, older adults and anyone who is tired of squinting can solve comfortably. Because these are printables, you can print one page or the whole book, as many times as you like, and make the pages even bigger by printing at "Fit to page" on US Letter.</p>
<h2>Which puzzles are inside</h2>
<ul><li><b>100 Large Print Puzzles for Seniors:</b> word searches, crosswords, sudoku and mazes in large print, with every answer included. You get a complete English book and a complete Spanish book.</li>
<li><b>Large Print Christmas Puzzles:</b> 20 holiday word searches and 15 crosswords with answers, in English and Spanish. A good stocking stuffer for a grandparent or a quiet activity for Christmas afternoon.</li></ul>
<h2>Ideas for using them</h2>
<ul><li><b>Gifts for grandparents:</b> print the set, punch holes and put it in a binder with a pen and a highlighter. It's a thoughtful gift you can make the night before a visit.</li>
<li><b>Senior centers, assisted living and memory care:</b> activity coordinators can print a fresh stack for every group session. Pick easier word searches for some residents and sudoku for others.</li>
<li><b>Caregivers:</b> a puzzle page is a calm, screen-free activity for waiting rooms, recovery days and quiet afternoons.</li>
<li><b>Family time:</b> solve a crossword together across generations. The bilingual books also work for families where grandparents prefer Spanish.</li></ul>
<h2>How to print large-print puzzles at home</h2>
<ol><li>Download the PDF right after checkout.</li><li>Print on plain US Letter or A4 paper. Choose "Fit to page" to make the type as big as possible.</li><li>Use a dark felt-tip pen or marker instead of a pencil, since bold lines are easier to see.</li><li>Keep the answer pages aside so nobody peeks.</li></ol>
<p>¿Buscas en español? Los dos libros traen versión completa en español: sopas de letras, crucigramas, sudokus y laberintos en letra grande.</p>'''
faq=[("What size is the print?","The puzzles are laid out in large type with roomy grids for easy reading. Printing with \"Fit to page\" on US Letter makes them as big as your paper allows."),
 ("Are the answers included?","Yes. Both books include an answer key for every puzzle."),
 ("Are these puzzles good for seniors with memory loss?","Many caregivers and activity coordinators use word searches and simple mazes as calm, low-pressure activities. Start with the easier pages and let the person go at their own pace."),
 ("Is anything shipped?","No. These are digital PDF files you download and print at home, at a senior center or at a copy shop.")]
h=page("large-print-puzzles","Large Print Puzzles for Seniors: Printable Word Search, Crossword and Sudoku (PDF) | Bucky",
 "Printable large-print puzzles for seniors: word searches, crosswords, sudoku and mazes with answers, plus large-print Christmas puzzles. English and Spanish. US Letter and A4 PDF, print as many as you need.",
 "Printable large-print puzzles for seniors",
 "Big letters, roomy grids and every answer included: <b>100 large-print puzzles</b> (word search, crossword, sudoku and mazes) plus a <b>large-print Christmas puzzle book</b>. Instant PDF download in English and Spanish, US Letter and A4.",
 ["rompecabezas-letra-grande","pasatiempos-navidad"],body,
 ["rosario-novenas","colorear-biblico","chatgpt-paso-a-paso","kit-navideno-gratis","mega"],faq,"Large-print puzzles")
h=h.replace("<h2>More Christmas printables, ready to download</h2>","<h2>More large-print and relaxing printables</h2>")
os.makedirs("large-print-puzzles",exist_ok=True)
open("large-print-puzzles/index.html","w").write(h)
s=open("sitemap.xml").read()
if "/large-print-puzzles/" not in s: open("sitemap.xml","w").write(s.replace("</urlset>",f"<url><loc>{U}large-print-puzzles/</loc><lastmod>2026-10-26</lastmod></url></urlset>"))
print("ok large print puzzles")

# --- Christmas activities for kids (2026-10-26, FB Page 8 PM slot) ---
body='''<h2>Screen-free Christmas activities kids actually enjoy</h2>
<p>Winter break is long, and by the third day most kids have watched every holiday movie twice. Printable activities fix that without a trip to the craft store: print a few pages in the morning and you have a quiet hour while you wrap presents, cook or work from home.</p>
<ul><li><b>Coloring pages:</b> the easiest win for ages 3 to 7. Thick lines are easier for little hands, and a finished page makes a nice card for a grandparent.</li>
<li><b>Christmas games:</b> charades, Would You Rather and Christmas Scattergories get the whole family playing after dinner, with no setup.</li>
<li><b>Mazes, dot-to-dots and word searches:</b> perfect for early finishers in class, restaurant waits and the car ride to Grandma's.</li>
<li><b>Story time:</b> read a short printable story together, then let kids color the pictures from it.</li>
<li><b>Stickers and crafts:</b> print stickers on sticker paper to decorate cards, gift bags and homemade ornaments.</li></ul>
<h2>Ideas by age</h2>
<ul><li><b>Ages 3 to 5:</b> big coloring pages, simple mazes and stickers. Keep sessions short, 10 to 15 minutes, and let them pick the page.</li>
<li><b>Ages 6 to 9:</b> word searches, dot-to-dots and charades. They love playing a game they can "run" for the adults.</li>
<li><b>Ages 10 and up:</b> Scattergories, Would You Rather and drawing challenges. Older kids can also help the little ones with their pages.</li></ul>
<h2>A simple winter break plan</h2>
<ol><li>Print a small stack on Sunday night: two coloring pages, one game and one puzzle per child.</li>
<li>Keep them in a folder with crayons so kids can grab an activity on their own.</li>
<li>Save the party games for an evening when the whole family is home.</li>
<li>Hang finished pages on the fridge or turn them into cards for teachers and neighbors.</li>
<li>After Christmas, the Three Kings Day kit keeps the fun going until January 6.</li></ol>
<p>Every file is bilingual, English and Spanish, so it works for dual-language classrooms and families who speak both. ¿Lo buscas en español? Mira nuestras <a href="../manualidades-navidenas-ninos/">manualidades navideñas para niños</a>.</p>'''
faq=[("Are there free Christmas activities for kids here?","Yes. The free Christmas Mini Kit has Christmas charades, Would You Rather, Christmas Scattergories, a card, 8 gift tags and a coloring page."),
 ("What ages are these activities for?","Most pages work for ages 3 to 10. Coloring pages and stickers suit preschoolers, and games and word searches suit older kids and the whole family."),
 ("Can teachers use them in class?","Yes. Personal and classroom use is fine, so print as many copies as your class needs. Please don't resell the files."),
 ("Is anything shipped?","No. These are digital PDF files you download and print at home or at a copy shop.")]
h=page("christmas-activities-for-kids","Printable Christmas Activities for Kids: Coloring, Games and Mazes (PDF) | Bucky",
 "Printable Christmas activities for kids: a free Christmas mini kit with games and a coloring page, plus 60 screen-free activity pages, coloring pages and stories for winter break. English and Spanish, US Letter and A4.",
 "Printable Christmas activities for kids",
 "Keep kids happy and off screens all winter break: start with the <b>free Christmas Mini Kit</b> (games and a coloring page), then add <b>60 screen-free activity pages</b>, coloring pages and stories. Instant PDF download, English and Spanish, US Letter and A4.",
 ["kit-navideno-gratis","kids-mega"],body,
 ["bucky-coloring","bucky-storybooks","bucky-stickers","combo-gratitud","reyes-kit","mega"],faq,"Christmas activities for kids")
h=h.replace("<h2>More Christmas printables, ready to download</h2>","<h2>More printables for kids this season</h2>")
os.makedirs("christmas-activities-for-kids",exist_ok=True)
open("christmas-activities-for-kids/index.html","w").write(h)
s=open("sitemap.xml").read()
if "/christmas-activities-for-kids/" not in s: open("sitemap.xml","w").write(s.replace("</urlset>",f"<url><loc>{U}christmas-activities-for-kids/</loc><lastmod>2026-10-26</lastmod></url></urlset>"))
print("ok christmas activities for kids")

# --- Christmas word search (2026-10-27, FB Page 10 AM slot) ---
body='''<h2>Why a printable Christmas word search works so well</h2>
<p>A word search is the one activity almost everyone can do: kids who just learned to read, teens killing time on winter break, and grandparents who want something calm after dinner. Print a page, hand over a pencil and the table goes quiet for twenty minutes.</p>
<ul><li><b>Family gatherings:</b> leave a stack of word searches next to the coffee so guests have something to do while the turkey or the ham finishes.</li>
<li><b>Classrooms:</b> a Christmas word search is an easy early-finisher page in the last week before break, and the answer key makes checking fast.</li>
<li><b>Seniors and memory care:</b> large print and roomy grids are easier on the eyes, and a familiar holiday theme makes the words easier to find.</li>
<li><b>Travel and waiting rooms:</b> fold a page into a bag for the airport, the car or the doctor's office.</li></ul>
<h2>Make it a game</h2>
<ol><li>Print one copy of the same puzzle for every player.</li>
<li>Set a timer for five or ten minutes. Whoever finds the most words wins a candy cane.</li>
<li>For mixed ages, let younger kids team up with an adult, or give the adults a handicap of one minute.</li>
<li>Use the answer key at the end to settle any arguments.</li></ol>
<h2>Printing tips</h2>
<p>Print on plain US Letter or A4 paper at "Actual size". Use a pencil so pages can be checked against the answer key, or slip a page into a sheet protector and use a dry-erase marker to reuse it all season.</p>
<p>The puzzle books are bilingual, English and Spanish, so they also work for dual-language classrooms and bilingual families. ¿Lo buscas en español? Hay sopas de letras navideñas en el mismo libro.</p>'''
faq=[("Do the Christmas word searches come with answers?","Yes. The Large Print Christmas Puzzles book includes an answer key for all 20 word searches and 15 crosswords."),
 ("Are they large print?","Yes. The Christmas puzzle book and the 100 Large Print Puzzles book both use big letters and roomy grids, so they work well for seniors and young readers."),
 ("What paper size are they?","US Letter and A4. Print at home, at school or at a copy shop."),
 ("Is anything shipped?","No. These are digital PDF files you download right after checkout and print yourself."),
 ("Can I print copies for my class or family?","Yes. Personal and classroom use is fine, so print as many as you need. Please don't resell the files.")]
h=page("christmas-word-search","Christmas Word Search Printable: 20 Puzzles + Answers",
 "Printable Christmas word search puzzles in large print: 20 word searches and 15 crosswords with answers, for kids, families and seniors. US Letter and A4 PDF.",
 "Printable Christmas word search puzzles",
 "<b>20 Christmas word searches and 15 crosswords</b> in large print, with every answer included. Print them for family gatherings, the classroom or a quiet afternoon. Instant PDF download, English and Spanish, US Letter and A4.",
 ["pasatiempos-navidad","rompecabezas-letra-grande"],body,
 ["kit-navideno-gratis","kids-mega","combo-gratitud","mega"],faq,"Christmas word search")
h=h.replace("<h2>More Christmas printables, ready to download</h2>","<h2>More Christmas games and activities</h2>")
os.makedirs("christmas-word-search",exist_ok=True)
open("christmas-word-search/index.html","w").write(h)
s=open("sitemap.xml").read()
if "/christmas-word-search/" not in s: open("sitemap.xml","w").write(s.replace("</urlset>",f"<url><loc>{U}christmas-word-search/</loc><lastmod>2026-10-27</lastmod></url></urlset>"))
print("ok christmas word search")

# --- Christmas bingo (2026-10-28, FB Page 10 AM slot) ---
for k,g,pr,en,den in [('christmas-bingo','lbizh','5.99','Christmas Picture Bingo','50 watercolor picture bingo cards, 45 calling cards and 20 word bingo cards. English and Spanish, Letter and A4.')]:
  P.setdefault(k,{'k':k,'g':g,'pr':pr,'en':en,'den':den})
body='''<h2>Why picture bingo is the easiest Christmas party game</h2>
<p>Bingo needs no rules explanation, no teams and no prep beyond printing. Picture bingo goes one step further: every square has a painted picture with its label, so kids who can't read yet can play right next to grandparents. When the adults want something a little faster, switch to the word bingo cards.</p>
<ul><li><b>Family Christmas parties:</b> one game fits everyone from age 3 to 93, and it fills the half hour between dinner and dessert.</li>
<li><b>Classroom holiday parties:</b> a teacher or room parent can call the pictures while kids mark their cards.</li>
<li><b>Office and church gatherings:</b> the word bingo cards are quick to play with adults and need nothing but a pen.</li>
<li><b>Bilingual families:</b> the same game comes in English and in Spanish, so everyone can play in the language they like.</li></ul>
<h2>How to play Christmas bingo</h2>
<ol><li>Print the cards (two picture cards per page) and cut the picture calling cards apart.</li>
<li>Give each player a card and some markers: candy, mini marshmallows, buttons or a crayon.</li>
<li>Shuffle the calling cards in a bowl or hat. Draw one at a time and say it out loud.</li>
<li>Players mark the matching square. The first to complete a row, column or diagonal shouts "Bingo!" and wins.</li>
<li>For a longer game, play blackout: the winner is the first to cover the whole card.</li></ol>
<h2>Printing tips</h2>
<p>Print on plain US Letter or A4 paper at "Actual size", or on light cardstock if you want the cards to last all season. Slip a card into a sheet protector and use a dry-erase marker to reuse it round after round. Prize ideas: candy canes, hot cocoa packets, a small ornament, or first pick at the cookie tray.</p>
<p>¿Lo buscas en español? El juego trae una versión completa en español: lotería de imágenes navideña y bingo de palabras.</p>'''
faq=[("How many Christmas bingo cards are included?","50 unique picture bingo cards (2 per page) with 45 picture calling cards, plus 20 word bingo cards with a 40-word calling list."),
 ("Can kids who can't read play?","Yes. Every square on the picture cards has a painted picture with its label, so young kids and non-readers can play."),
 ("Will two players have the same card?","No. All 50 picture cards are different, and no two share more than 17 of their 24 pictures."),
 ("What paper size and language?","You get 4 PDF files: English US Letter, English A4, Spanish US Letter and Spanish A4."),
 ("Is anything shipped?","No. It's a digital download you print at home or at a copy shop.")]
h=page("christmas-bingo","Printable Christmas Bingo: 50 Picture Cards + Word Bingo",
 "Printable Christmas bingo for families and parties: 50 unique picture cards kids can play, 45 calling cards and 20 word bingo cards. English, Spanish, PDF.",
 "Printable Christmas bingo cards for the whole family",
 "<b>50 unique Christmas picture bingo cards</b> that kids and non-readers can play, <b>45 calling cards</b>, and <b>20 word bingo cards</b> for adults. Instant PDF download in English and Spanish, US Letter and A4, for <b>$5.99</b>.",
 ["christmas-bingo","kit-navideno-gratis"],body,
 ["games","bundle","combo-gratitud","kids-mega","mega"],faq,"Christmas bingo")
h=h.replace("<h2>More Christmas printables, ready to download</h2>","<h2>More Christmas party games and printables</h2>")
os.makedirs("christmas-bingo",exist_ok=True)
open("christmas-bingo/index.html","w").write(h)
s=open("sitemap.xml").read()
if "/christmas-bingo/" not in s: open("sitemap.xml","w").write(s.replace("</urlset>",f"<url><loc>{U}christmas-bingo/</loc><lastmod>2026-10-28</lastmod></url></urlset>"))
print("ok christmas bingo")

# --- Printable Christmas cards (2026-10-29, FB Page 10 AM slot) ---
body='''<h2>Why print your own Christmas cards</h2>
<p>A box of store cards costs more than a whole printable set, and it never has the right card for the teacher, the neighbor and the grandparents all at once. With a PDF you print exactly the cards you need tonight, and print more next week when you remember one more person.</p>
<ul><li><b>Messages already written:</b> every card in the Bucky Christmas Cards set has a warm message inside plus space to sign, so you only add a name.</li>
<li><b>Cards for everyone on the list:</b> Merry Christmas, Happy Holidays, Peace on Earth, Blessed Christmas, Thank You Teacher, Grandma &amp; Grandpa, Happy New Year and more.</li>
<li><b>Fits a standard envelope:</b> the finished card is 4.25 &times; 5.5 in, the size of an A2 envelope.</li>
<li><b>Bilingual:</b> every card comes in English and in Spanish, for bilingual families and dual-language classrooms.</li></ul>
<h2>How to print and fold a quarter-fold card</h2>
<ol><li>Download the PDF and print on white cardstock (65 to 110 lb) at "Actual size". The cards print on one side only, so there is no double-sided setting to fight with.</li>
<li>Fold the sheet in half the long way, then in half again, so the picture ends up on the front.</li>
<li>Run a thumbnail or a ruler along each fold for a crisp edge.</li>
<li>Sign inside, slip it into an A2 envelope and add a matching gift tag to the present.</li></ol>
<p>Not sure yet? The <b>free Christmas Mini Kit</b> includes one folding Christmas card and 8 gift tags, so you can try a print before you buy. ¿Buscas tarjetas en español? Cada tarjeta viene también en español, y hay <a href="../tarjetas-navidenas-gratis/">tarjetas navideñas gratis</a>.</p>'''
faq=[("Are there free printable Christmas cards?","Yes. The free Christmas Mini Kit includes one folding Christmas card and 8 To/From gift tags. The full Bucky Christmas Cards set has 12 cards and 16 gift tags for $3.99."),
 ("What size are the cards?","Each card folds down to 4.25 x 5.5 inches and fits a standard A2 envelope. The A4 version folds to about 10.5 x 14.8 cm."),
 ("Do I need to print double-sided?","No. The cards print on one side of the sheet; you fold the page in four and the message lands inside."),
 ("What paper should I use?","White cardstock, 65 to 110 lb, gives the best result. Plain printer paper works for a quick card."),
 ("Is anything shipped?","No. You get 4 PDF files (English US Letter, English A4, Spanish US Letter and Spanish A4) to print yourself.")]
h=page("printable-christmas-cards","Printable Christmas Cards: 12 Foldable Cards + a Free Card",
 "Printable Christmas cards with the message already inside: 12 quarter-fold cards and 16 gift tags for $3.99, or a free card to start. English and Spanish PDF.",
 "Printable Christmas cards you can make tonight",
 "<b>12 folding Christmas cards</b> with a warm message already inside, plus <b>16 To/From gift tags</b>, for <b>$3.99</b>. Print on one side, fold in four and give. Instant PDF download in English and Spanish, US Letter and A4. Want to try first? Grab the <b>free mini kit</b> with one card and 8 tags.",
 ["tarjetas-navidad","kit-navideno-gratis"],body,
 ["tarjetas-felicitacion","tarjetas-biblicas","combo-gratitud","mega"],faq,"Printable Christmas cards")
h=h.replace("<h2>More Christmas printables, ready to download</h2>","<h2>More cards and Christmas printables</h2>")
os.makedirs("printable-christmas-cards",exist_ok=True)
open("printable-christmas-cards/index.html","w").write(h)
s=open("sitemap.xml").read()
if "/printable-christmas-cards/" not in s: open("sitemap.xml","w").write(s.replace("</urlset>",f"<url><loc>{U}printable-christmas-cards/</loc><lastmod>2026-10-29</lastmod></url></urlset>"))
print("ok printable christmas cards")

# --- Printable Thanksgiving games (2026-10-30, FB Page 10 AM slot) ---
P["thanksgiving"]={"k":"thanksgiving","g":"ckmaso","pr":"7.79","en":"Thanksgiving Games Bundle","den":"Picture bingo, trivia, charades, Scattergories, a pie contest, gratitude cards, place cards and a kids' table mat. 38 pages, EN + ES."}
body='''<h2>Thanksgiving games the whole table can play</h2>
<p>The turkey takes hours, and the gap between "everyone's here" and "dinner's ready" is where printable games earn their keep. These work for a big family dinner, a Friendsgiving with roommates, or a classroom party the day before break.</p>
<ul><li><b>Thanksgiving picture bingo:</b> 20 different cards with a picture and a word on every square, plus 30 calling cards, so kids who can't read yet play alongside grandparents.</li>
<li><b>Thanksgiving trivia:</b> 20 family-friendly questions with an answer key. Split the room into two teams and keep score on a napkin.</li>
<li><b>Who Am I? and charades:</b> 24 cards for a game that needs nothing but the cards and a little courage.</li>
<li><b>Thanksgiving Scattergories:</b> a game sheet with 12 categories and 3 rounds. Print one per player.</li>
<li><b>The Great Pie-Off:</b> a sign, 8 star-rating ballots, 6 entry cards and 6 awards (Best in Show, Flakiest Crust, People's Choice and more) turn dessert into a contest.</li></ul>
<h2>Gratitude activities and a kids' table that runs itself</h2>
<p>Put a stack of "I'm thankful for" cards (16 with prompts) by each plate and read them out before the pie. The gratitude tree poster comes with 18 leaves to color and stick on. For the kids' table there's an activity mat with tic-tac-toe, count-and-write, draw your plate and a turkey to color, plus a coloring page, a word search and a maze.</p>
<h2>How to print them</h2>
<ol><li>Download the 4 PDFs right after checkout: English US Letter, English A4, Spanish US Letter and Spanish A4.</li>
<li>Print at "Actual size". Use cardstock for bingo cards, place cards and thankful cards, and plain paper for trivia and Scattergories sheets.</li>
<li>Cut, fold and play. No printer at home? Any copy shop can print it the same day.</li></ol>
<p>Thanksgiving 2026 is Thursday, November 26. ¿Lo buscas en español? Todo el kit viene también en español, ideal para familias bilingües: bingo, trivia, mímica y tarjetas de gratitud.</p>'''
faq=[("When is Thanksgiving 2026?","Thursday, November 26, 2026."),
 ("What games are in the Thanksgiving Games Bundle?","Picture bingo (20 cards and 30 calling cards), Thanksgiving trivia (20 questions with answers), Who Am I? and charades (24 cards), Thanksgiving Scattergories, and the Great Pie-Off dessert contest, plus gratitude cards, place cards, menus and a kids' activity mat."),
 ("How many pages is it?","38 pages per language, in 4 PDF files: English US Letter, English A4, Spanish US Letter and Spanish A4."),
 ("Can small kids play?","Yes. Every bingo square has a picture next to the word, and the kids' table mat and coloring page are made for little ones."),
 ("Is anything shipped?","No. It's a digital download you print at home or at a copy shop. The files are not editable; you fill them in by hand.")]
h=page("thanksgiving-games","Printable Thanksgiving Games: Bingo, Trivia & Family Fun",
 "Printable Thanksgiving games for family and kids: picture bingo, trivia, charades, Scattergories and a pie contest. 38 pages, English and Spanish PDF, $7.79.",
 "Printable Thanksgiving games for family and kids",
 "<b>Thanksgiving picture bingo, trivia, charades, Scattergories and a pie contest</b>, plus gratitude cards, place cards and a kids' table mat, in one <b>38-page</b> download for <b>$7.79</b>. Instant PDF in English and Spanish, US Letter and A4.",
 ["thanksgiving","combo-gratitud"],body,
 ["kids-mega","rompecabezas-letra-grande","kit-navideno-gratis","mega"],faq,"Thanksgiving games")
h=h.replace("<h2>More Christmas printables, ready to download</h2>","<h2>More printables for Thanksgiving week and beyond</h2>")
h=h.replace('<a href="../ideas-intercambio-regalos/">ideas para intercambio de regalos</a>.</p>','<a href="../ideas-intercambio-regalos/">ideas para intercambio de regalos</a>. In English: <a href="../thanksgiving-printables/">more Thanksgiving printables</a>.</p>')
os.makedirs("thanksgiving-games",exist_ok=True)
open("thanksgiving-games/index.html","w").write(h)
s=open("sitemap.xml").read()
if "/thanksgiving-games/" not in s: open("sitemap.xml","w").write(s.replace("</urlset>",f"<url><loc>{U}thanksgiving-games/</loc><lastmod>2026-10-30</lastmod></url></urlset>"))
print("ok thanksgiving games")
import subprocess; subprocess.run(["python3", "utm.py"])
