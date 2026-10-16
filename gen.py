import json,html
U='https://buckyproducts.github.io/shop/'
G='https://buckylittleshop.gumroad.com/l/';P='https://payhip.com/b/'
PR=[('halloween','hftpjb','pnztC','7.79','Kit de fiesta de Halloween','Halloween Party Kit','Juegos, invitaciones, etiquetas y decoración imprimible. Listo en minutos.','Games, invitations, labels and printable decor. Ready in minutes.','season'),
('muertos','ypkit','OA4gi','10.49','Kit de Día de Muertos','Día de Muertos Kit','Papel picado, ofrenda, juegos y actividades para toda la familia.','Papel picado, ofrenda, games and activities for the whole family.','season'),
('thanksgiving','ckmaso','LQBfv','7.79','Kit de Acción de Gracias','Thanksgiving Kit','Juegos, tarjetas de gratitud y decoración para tu mesa.','Games, gratitude cards and table decor.','season'),
('bundle','bkgnnd','0NkMo','15.99','Paquete fiesta navideña','Christmas Party Bundle','El paquete completo: juegos, intercambio y decoración. Mejor precio.','The complete pack: games, gift exchange and decor. Best value.','xmas'),
('bingo','lbizh','AQVW1','5.99','Lotería/Bingo navideño con imágenes','Christmas Picture Bingo','Cartones con dibujos, ideal para niños y adultos.','Picture cards, perfect for kids and adults.','xmas'),
('games','cnexgy','yR2hw','9.99','Juegos para fiesta navideña','Christmas Party Games','Juegos imprimibles para posadas, oficina o familia.','Printable games for posadas, office or family.','xmas'),
('secret-santa','mfqlci','PGsBK','6.99','Kit de intercambio de regalos','Secret Santa Kit','Tarjetas, listas de deseos y etiquetas para tu intercambio.','Cards, wish lists and tags for your gift exchange.','xmas'),
('negocio','blmxs','ahHFW','9','100 prompts de IA para tu negocio','100 AI Prompts for Your Business','Ventas, marketing, redes y atención al cliente con ChatGPT y más.','Sales, marketing, social and customer service with ChatGPT and more.','ai'),
('maestros','pzsrkz','Sd4pC','7','IA para maestros','AI for Teachers','Planeaciones, exámenes y rúbricas en minutos.','Lesson plans, quizzes and rubrics in minutes.','ai'),
('bots','ywdtt','ygTLV','15','Manual para dirigir bots de IA','AI Bot Manager Playbook','Guía práctica + 28 plantillas para trabajar con agentes de IA.','Practical guide + 28 templates for working with AI agents.','ai')]
TAG={'season':('Temporada','Seasonal'),'xmas':('Navidad','Christmas'),'ai':('IA','AI')}
def t(es,en): return f'<span data-es>{es}</span><span data-en>{en}</span>'
cards=''
ld=[]
for i,(k,g,p,pr,ne,nn,de,dn,tg) in enumerate(PR):
    lazy='eager' if i<2 else 'lazy'
    cards+=f'''<article class="card"><div class="ph"><img src="img/{k}.webp" width="800" height="800" loading="{lazy}" decoding="async" alt="{html.escape(nn)}"><span class="tag">{t(*TAG[tg])}</span></div>
<div class="cb"><h3>{t(ne,nn)}</h3><p>{t(de,dn)}</p><div class="row"><span class="price">${pr} <small>USD</small></span><a class="buy" href="{G+g}" rel="noopener">{t('Comprar','Buy now')}</a></div>
<a class="alt" href="{P+p}" rel="noopener">{t('Pagar con Payhip / Mercado Pago','Pay with Payhip / Mercado Pago')}</a></div></article>\n'''
    ld.append({"@type":"Product","name":nn,"alternateName":ne,"description":dn,"image":U+f"img/{k}.webp","brand":{"@type":"Brand","name":"Bucky Little Shop"},"offers":{"@type":"Offer","price":pr,"priceCurrency":"USD","availability":"https://schema.org/InStock","url":G+g}})
TAG.update({'free':('Gratis','Free'),'edu':('Educación','Education'),'party':('Fiestas','Parties'),'kids':('Niños','Kids'),'tools':('Plantillas','Templates'),'guide':('Guía','Guide'),'bucky':('Bucky','Bucky'),'family':('Familia · letra grande','Family · large print'),'ana':('Fe','Faith')})
XP=json.load(open('payhip.json'))
SEC=[('season','Más de temporada','More seasonal'),('free','Gratis','Free'),('party','Fiestas y eventos','Parties & events'),('kids','Niños y aula','Kids & classroom'),('edu','Niños y aula','Kids & classroom'),('tools','Plantillas y agendas','Templates & planners'),('guide','Guías prácticas','How-to guides'),('bucky','Personaje Bucky','Bucky character'),('family','Familia y letra grande','Family & large print')]
def pc(o):
    pr='0' if float(o['pr'])==0 else o['pr']
    price=t('Gratis','Free') if pr=='0' else f"${pr} <small>USD</small>"
    ld.append({"@type":"Product","name":o['en'],"alternateName":o['es'],"description":o['den'],"image":U+f"img/{o['k']}.webp","brand":{"@type":"Brand","name":"Ana Hope Shop" if o['c']=='ana' else "Bucky Little Shop"},"offers":{"@type":"Offer","price":pr,"priceCurrency":"USD","availability":"https://schema.org/InStock","url":P+o['p']}})
    e=html.escape
    return (f'<article class="card"><div class="ph"><img src="img/{o["k"]}.webp" width="{o["w"]}" height="{o["h"]}" loading="lazy" decoding="async" alt="{e(o["en"])}"><span class="tag">{t(*TAG[o["c"]])}</span></div>\n'
     f'<div class="cb"><h3>{t(e(o["es"]),e(o["en"]))}</h3><p>{t(e(o["des"]),e(o["den"]))}</p><div class="row"><span class="price">{price}</span><a class="buy" href="{P+o["p"]}" rel="noopener">{t("Obtener" if pr=="0" else "Comprar","Get it" if pr=="0" else "Buy now")}</a></div>\n'
     f'<span class="alt">{t("Pago con Payhip / Mercado Pago","Checkout via Payhip / Mercado Pago")}</span></div></article>\n')
xcards='';last=None
for c,es,en in SEC:
    items=[o for o in XP if o['c']==c]
    if not items: continue
    if (es,en)!=last: xcards+=f'<h3 class="gh">{t(es,en)}</h3>'
    last=(es,en)
    xcards+='<div class="grid">'+''.join(pc(o) for o in items)+'</div>'
acards='<div class="grid">'+''.join(pc(o) for o in XP if o['c']=='ana')+'</div>'
LD=json.dumps({"@context":"https://schema.org","@graph":[{"@type":"Organization","name":"Bucky Little Shop","url":U,"logo":U+"img/logo.webp"}]+ld},ensure_ascii=False)
FAQ=[('¿Cómo recibo mi archivo?','How do I get my file?','Justo después de pagar recibes un enlace de descarga en pantalla y por correo.','Right after checkout you get a download link on screen and by email.'),
('¿Se envía algo físico?','Is anything shipped?','No. Son archivos digitales (PDF). Tú los imprimes en casa o en una papelería.','No. These are digital files (PDF). Print them at home or at a print shop.'),
('¿Están en español?','Are they in Spanish?','Sí. La mayoría incluye versión en español y en inglés.','Yes. Most include both Spanish and English versions.'),
('¿Qué tamaño de papel?','What paper size?','Carta (Letter) y la mayoría también A4.','US Letter, and most also A4.'),
('¿Puedo pagar con Mercado Pago?','Can I pay with Mercado Pago?','Sí, usa el enlace “Pagar con Payhip / Mercado Pago” debajo de cada producto.','Yes, use the “Pay with Payhip / Mercado Pago” link under each product.'),
('¿Puedo revender los archivos?','Can I resell the files?','No. Son para uso personal, familiar o en el aula.','No. They are for personal, family or classroom use.')]
faq=''.join(f'<details><summary>{t(a,b)}</summary><p>{t(c,d)}</p></details>' for a,b,c,d in FAQ)
H=f'''<!doctype html><html lang="es"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<title>Bucky Little Shop · Imprimibles para fiestas y guías de IA</title>
<meta name="description" content="Kits imprimibles de Halloween, Día de Muertos, Acción de Gracias y Navidad, más guías de IA en español. Descarga instantánea.">
<link rel="canonical" href="{U}"><link rel="alternate" hreflang="es" href="{U}"><link rel="alternate" hreflang="en" href="{U}?lang=en"><link rel="alternate" hreflang="x-default" href="{U}">
<meta property="og:type" content="website"><meta property="og:url" content="{U}"><meta property="og:title" content="Bucky Little Shop"><meta property="og:description" content="Imprimibles para fiestas y guías de IA · Party printables and AI guides. Descarga instantánea / Instant download."><meta property="og:image" content="{U}og.png"><meta property="og:image:width" content="1200"><meta property="og:image:height" content="630"><meta name="twitter:card" content="summary_large_image">
<link rel="icon" href="favicon.ico" sizes="any"><link rel="icon" type="image/png" href="favicon-32.png"><link rel="apple-touch-icon" href="apple-touch-icon.png"><meta name="theme-color" content="#7a4a26">
<link rel="preload" as="image" href="img/logo.webp">
<script>(function(){{var q=new URLSearchParams(location.search).get('lang'),s=null;try{{s=localStorage.getItem('lang')}}catch(e){{}};document.documentElement.lang=(q==='en'||q==='es')?q:(s||'es')}})()</script>
<style>
:root{{--br:#7a4a26;--or:#e9822b;--cr:#fff6ea;--ink:#2d1d12;--mut:#6b5646;--ok:#2f7d4f}}
*{{box-sizing:border-box}}body{{margin:0;font:16px/1.55 system-ui,-apple-system,"Segoe UI",Roboto,sans-serif;color:var(--ink);background:var(--cr)}}
html[lang=es] [data-en],html[lang=en] [data-es]{{display:none}}
a{{color:var(--br)}}.w{{max-width:1120px;margin:0 auto;padding:0 18px}}
header{{position:sticky;top:0;z-index:5;background:rgba(255,246,234,.92);backdrop-filter:blur(8px);border-bottom:1px solid #f0dcc4}}
.hd{{display:flex;align-items:center;justify-content:space-between;height:62px;gap:10px}}.brand{{display:flex;align-items:center;gap:10px;font-weight:800;text-decoration:none;color:var(--ink);font-size:18px}}.brand img{{width:42px;height:42px;border-radius:50%}}
nav{{display:flex;align-items:center;gap:14px}}nav a.nl{{text-decoration:none;font-weight:600}}@media(max-width:640px){{nav a.nl{{display:none}}}}
.lg{{display:flex;border:2px solid var(--br);border-radius:999px;overflow:hidden}}.lg button{{border:0;background:none;padding:6px 12px;font-weight:700;color:var(--br);cursor:pointer;min-height:36px}}html[lang=es] .lg [data-l=es],html[lang=en] .lg [data-l=en]{{background:var(--br);color:#fff}}
.hero{{display:grid;grid-template-columns:1.2fr 1fr;gap:28px;align-items:center;padding:42px 0}}.hero h1{{font-size:clamp(30px,5vw,50px);line-height:1.1;margin:0 0 14px}}.hero p{{font-size:18px;color:var(--mut);margin:0 0 22px}}
.hero img{{width:100%;max-width:420px;height:auto;justify-self:center;border-radius:50%;box-shadow:0 18px 50px rgba(122,74,38,.18)}}
@media(max-width:760px){{.hero{{grid-template-columns:1fr;text-align:center;padding:24px 0}}.hero img{{max-width:240px;grid-row:1}}}}
.cta{{display:inline-block;background:var(--or);color:#fff;font-weight:800;text-decoration:none;padding:14px 26px;border-radius:14px;box-shadow:0 6px 0 #c4661a}}.cta:hover{{transform:translateY(-1px)}}
.badges{{display:flex;flex-wrap:wrap;gap:8px 16px;margin-top:20px;font-weight:600;color:var(--ok);font-size:15px}}@media(max-width:760px){{.badges{{justify-content:center}}}}
h2{{font-size:clamp(24px,3.5vw,34px);margin:0 0 6px}}.sub{{color:var(--mut);margin:0 0 22px}}section{{padding:34px 0}}
.grid{{display:grid;grid-template-columns:repeat(auto-fill,minmax(250px,1fr));gap:20px}}
.card{{background:#fff;border-radius:18px;overflow:hidden;box-shadow:0 4px 18px rgba(122,74,38,.10);display:flex;flex-direction:column;transition:transform .15s}}.card:hover{{transform:translateY(-3px)}}
.ph{{position:relative;aspect-ratio:1;background:#f6eadb}}.ph img{{width:100%;height:100%;object-fit:cover;display:block}}.tag{{position:absolute;top:10px;left:10px;background:#fff;color:var(--br);font-size:12px;font-weight:800;padding:4px 10px;border-radius:999px}}
.cb{{padding:14px 16px 16px;display:flex;flex-direction:column;flex:1}}.cb h3{{margin:0 0 6px;font-size:18px;line-height:1.25}}.cb p{{margin:0 0 12px;color:var(--mut);font-size:14.5px;flex:1}}
.row{{display:flex;align-items:center;justify-content:space-between;gap:10px}}.price{{font-size:22px;font-weight:800}}.price small{{font-size:12px;color:var(--mut)}}
.buy{{background:var(--or);color:#fff;text-decoration:none;font-weight:800;padding:11px 18px;border-radius:12px;min-height:44px;display:inline-flex;align-items:center}}.buy:hover{{background:#d2701d}}
.gh{{margin:30px 0 14px;font-size:22px}}.ana{{background:#FBF6EA;border-top:6px solid #EAE0F6}}.ana h2{{color:#7E62B0}}.ana .ah{{display:flex;align-items:center;gap:18px;margin-bottom:20px;flex-wrap:wrap}}.ana .ah img{{width:120px;height:auto}}.ana .card{{box-shadow:0 4px 18px rgba(126,98,176,.14)}}.ana .ph{{background:#DCEBF7}}.ana .tag{{color:#7E62B0}}.ana .buy{{background:#7E62B0}}.ana .buy:hover{{background:#6a4f9c}}.ana .price{{color:#4A3F5C}}.ana .alt{{color:#6E9A6A}}
.alt{{margin-top:10px;font-size:13px;color:var(--mut);text-align:right}}
.steps{{display:grid;grid-template-columns:repeat(auto-fit,minmax(220px,1fr));gap:18px;counter-reset:s}}.step{{background:#fff;border-radius:16px;padding:20px;border:2px dashed #f0d2ad}}.step b{{display:inline-grid;place-items:center;width:38px;height:38px;border-radius:50%;background:var(--br);color:#fff;margin-bottom:8px}}.step h3{{margin:0 0 4px}}.step p{{margin:0;color:var(--mut)}}
.dl{{background:var(--br);color:#fff;border-radius:22px;padding:28px;display:grid;grid-template-columns:repeat(auto-fit,minmax(200px,1fr));gap:18px}}.dl h3{{margin:0 0 4px;color:#ffd9a8}}.dl p{{margin:0;opacity:.92}}
details{{background:#fff;border-radius:14px;padding:14px 18px;margin-bottom:10px}}summary{{cursor:pointer;font-weight:700}}details p{{margin:10px 0 0;color:var(--mut)}}
footer{{background:#2d1d12;color:#f3e3d1;padding:30px 0;margin-top:30px;font-size:14px}}footer a{{color:#ffd9a8}}.ft{{display:flex;flex-wrap:wrap;gap:12px 28px;justify-content:space-between;align-items:center}}
:focus-visible{{outline:3px solid var(--or);outline-offset:2px}}
</style>
<script type="application/ld+json">{LD}</script></head><body>
<header><div class="w hd"><a class="brand" href="./"><img src="img/icon-192.png" width="42" height="42" alt="">Bucky Little Shop</a>
<nav><a class="nl" href="#productos">{t('Productos','Products')}</a><a class="nl" href="#ana">Ana Hope</a><a class="nl" href="#faq">FAQ</a><div class="lg" role="group" aria-label="Idioma / Language"><button data-l="es" type="button">ES</button><button data-l="en" type="button">EN</button></div></nav></div></header>
<main>
<div class="w hero"><div><h1>{t('Imprimibles para fiestas y guías de IA, listos en minutos','Party printables and AI guides, ready in minutes')}</h1>
<p>{t('Kits de Halloween, Día de Muertos, Acción de Gracias y Navidad, más guías prácticas de IA en español. Paga, descarga e imprime hoy mismo.','Halloween, Día de Muertos, Thanksgiving and Christmas kits, plus practical AI guides in Spanish. Pay, download and print today.')}</p>
<a class="cta" href="#productos">{t('Ver productos','Shop now')}</a>
<div class="badges"><span>⚡ {t('Descarga instantánea','Instant download')}</span><span>🌎 {t('Español + inglés','Spanish + English')}</span><span>🔒 {t('Pago seguro','Secure checkout')}</span></div></div>
<img src="img/logo.webp" width="400" height="400" alt="Bucky Little Shop"></div>
<section id="productos"><div class="w"><h2>{t('Productos','Products')}</h2><p class="sub">{t('Primero lo de temporada 🎃💀🦃🎄','Seasonal picks first 🎃💀🦃🎄')}</p><div class="grid">
{cards}</div>{xcards}</div></section>
<section id="ana" class="ana"><div class="w"><div class="ah"><img src="img/ana-logo.webp" width="160" height="160" loading="lazy" alt="Ana Hope Shop"><div><h2>Ana Hope Shop</h2><p class="sub">{t('Oraciones, rosarios y versículos para imprimir, en letra grande.','Prayers, rosaries and Bible verses to print, in large type.')}</p></div></div>{acards}</div></section>
<section><div class="w"><div class="dl">
<div><h3>⚡ {t('Descarga instantánea','Instant download')}</h3><p>{t('Recibe tu PDF en segundos, sin esperar envíos.','Get your PDF in seconds, no shipping wait.')}</p></div>
<div><h3>🖨️ {t('Imprime en casa','Print at home')}</h3><p>{t('Tamaño carta y A4. Imprime cuantas veces quieras para tu evento.','Letter and A4. Print as many as you need for your event.')}</p></div>
<div><h3>💬 {t('Hecho para ti','Made for you')}</h3><p>{t('Diseños cálidos y bilingües, pensados para familias, escuelas y negocios.','Warm, bilingual designs for families, schools and small businesses.')}</p></div></div></div></section>
<section id="como"><div class="w"><h2>{t('Cómo funciona','How it works')}</h2><p class="sub">{t('Tres pasos y listo.','Three steps and done.')}</p><div class="steps">
<div class="step"><b>1</b><h3>{t('Elige','Choose')}</h3><p>{t('Escoge tu kit o guía favorita.','Pick your favorite kit or guide.')}</p></div>
<div class="step"><b>2</b><h3>{t('Paga seguro','Pay securely')}</h3><p>{t('Con tarjeta en Gumroad, o con Payhip / Mercado Pago.','By card on Gumroad, or with Payhip / Mercado Pago.')}</p></div>
<div class="step"><b>3</b><h3>{t('Descarga e imprime','Download & print')}</h3><p>{t('Tu enlace llega al instante y a tu correo.','Your link arrives instantly and by email.')}</p></div></div></div></section>
<section id="faq"><div class="w"><h2>{t('Preguntas frecuentes','FAQ')}</h2><p class="sub"></p>{faq}</div></section>
</main>
<footer><div class="w ft"><div><a href="dia-de-muertos/">Ofrenda de Día de Muertos</a> · <a href="posadas-navidad/">Juegos para posada y Navidad</a> · <a href="calendario-2027/">Calendario 2027 gratis</a> · <a href="calaveritas/">Generador de calaveritas</a><br><strong>Bucky Little Shop</strong> · © 2026 Bucky Products<br>{t('Productos digitales. No se envía nada físico.','Digital products. Nothing is shipped.')}</div>
<div><a href="https://buckyproducts.github.io/ia-facil/">IA Fácil</a> · <a href="https://buckylittleshop.gumroad.com/">Gumroad</a></div></div></footer>
<script>
var M={{es:{{t:"Bucky Little Shop · Imprimibles para fiestas y guías de IA",d:"Kits imprimibles de Halloween, Día de Muertos, Acción de Gracias y Navidad, más guías de IA en español. Descarga instantánea."}},en:{{t:"Bucky Little Shop · Party Printables & AI Guides",d:"Printable Halloween, Día de Muertos, Thanksgiving and Christmas party kits, plus AI guides in Spanish. Instant download."}}}};
function L(l){{document.documentElement.lang=l;document.title=M[l].t;document.querySelector('meta[name=description]').content=M[l].d;try{{localStorage.setItem('lang',l)}}catch(e){{}};document.querySelectorAll('.lg button').forEach(function(b){{b.setAttribute('aria-pressed',b.dataset.l===l)}})}}
document.querySelectorAll('.lg button').forEach(function(b){{b.onclick=function(){{L(b.dataset.l)}}}});L(document.documentElement.lang);
</script></body></html>'''
open('index.html','w').write(H)
open('robots.txt','w').write(f'User-agent: *\nAllow: /\nSitemap: {U}sitemap.xml\n')
open('sitemap.xml','w').write(f'<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9" xmlns:xhtml="http://www.w3.org/1999/xhtml"><url><loc>{U}</loc><lastmod>2026-10-16</lastmod><xhtml:link rel="alternate" hreflang="es" href="{U}"/><xhtml:link rel="alternate" hreflang="en" href="{U}?lang=en"/></url></urlset>\n')

exec(open('landing.py').read())  # seasonal SEO pages + sitemap
