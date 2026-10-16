# SEO landing pages for seasonal search intent. Run: python3 landing.py
import json,html
U='https://buckyproducts.github.io/shop/';G='https://buckylittleshop.gumroad.com/l/';P='https://payhip.com/b/'
E=html.escape
CSS='''*{box-sizing:border-box}body{margin:0;font-family:system-ui,-apple-system,"Segoe UI",Roboto,sans-serif;color:#3b2414;background:#fffaf3;line-height:1.6}
a{color:#a0522d}header{background:#7a4a26;color:#fff;padding:12px 20px;display:flex;align-items:center;gap:12px}header a{color:#fff;text-decoration:none;font-weight:700}header img{width:40px;height:40px;border-radius:50%}
main{max-width:860px;margin:0 auto;padding:20px}h1{font-size:2rem;line-height:1.2;margin:.4em 0}h2{margin-top:1.8em;color:#7a4a26}.lead{font-size:1.15rem}
.cta{display:grid;grid-template-columns:repeat(auto-fit,minmax(240px,1fr));gap:16px;margin:20px 0}.card{background:#fff;border:1px solid #ecd9c3;border-radius:14px;overflow:hidden}
.card img{width:100%;height:auto;display:block}.card div{padding:12px}.card h3{margin:0 0 6px;font-size:1.05rem}.btn{display:inline-block;background:#e76f51;color:#fff;padding:10px 16px;border-radius:999px;text-decoration:none;font-weight:700;margin:4px 0}
.alt{display:block;font-size:.85rem;margin-top:4px}.price{font-weight:800;margin-right:8px}ol li,ul li{margin:.3em 0}details{background:#fff;border:1px solid #ecd9c3;border-radius:10px;padding:10px 14px;margin:8px 0}summary{font-weight:700;cursor:pointer}
.en{background:#f3ebe1;border-radius:14px;padding:4px 20px 14px;margin-top:30px}footer{text-align:center;padding:30px;font-size:.9rem;color:#7a5a40}.wa{background:#25D366}'''
def card(k,title,desc,price,g,p):
  return f'''<div class="card"><img src="../img/{k}.webp" width="800" height="800" loading="lazy" alt="{E(title)}"><div><h3>{E(title)}</h3><p>{E(desc)}</p><span class="price">${price} USD</span>
'''+(f'<a class="btn" href="{G+g}" rel="noopener">Comprar / Buy</a><a class="alt" href="{P+p}" rel="noopener">Pagar con Payhip / Mercado Pago</a>' if g!=p else f'<a class="btn" href="{P+p}" rel="noopener">Comprar / Buy</a><span class="alt">Pago con Payhip / Mercado Pago</span>')+'</div></div>'
def page(slug,title,desc,h1,lead,body_es,cards,faq,en_html,wa_text,crumb):
  url=U+slug+'/'
  ld={"@context":"https://schema.org","@graph":[
    {"@type":"WebPage","name":title,"url":url,"description":desc,"inLanguage":"es"},
    {"@type":"BreadcrumbList","itemListElement":[{"@type":"ListItem","position":1,"name":"Bucky Little Shop","item":U},{"@type":"ListItem","position":2,"name":crumb,"item":url}]},
    {"@type":"FAQPage","mainEntity":[{"@type":"Question","name":q,"acceptedAnswer":{"@type":"Answer","text":a}} for q,a in faq]}]}
  wa="https://wa.me/?text="+html.escape(__import__('urllib.parse').parse.quote(wa_text+" "+url))
  return f'''<!doctype html><html lang="es"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<title>{E(title)}</title><meta name="description" content="{E(desc)}"><link rel="canonical" href="{url}">
<meta property="og:type" content="article"><meta property="og:url" content="{url}"><meta property="og:title" content="{E(title)}"><meta property="og:description" content="{E(desc)}"><meta property="og:image" content="{U}img/{cards[0][0]}.webp"><meta name="twitter:card" content="summary_large_image">
<link rel="icon" href="../favicon.ico"><meta name="theme-color" content="#7a4a26"><style>{CSS}</style>
<script type="application/ld+json">{json.dumps(ld,ensure_ascii=False)}</script></head><body>
<header><a href="../"><img src="../img/logo.webp" alt="Bucky Little Shop" width="40" height="40"></a><a href="../">Bucky Little Shop</a></header>
<main><p><a href="../">Inicio</a> › {E(crumb)}</p><h1>{E(h1)}</h1><p class="lead">{lead}</p>
<div class="cta">{"".join(card(*c) for c in cards[:2])}</div>
{body_es}
<h2>Imprimibles listos para descargar</h2><div class="cta">{"".join(card(*c) for c in cards)}</div>
<p><a class="btn wa" href="{wa}" rel="noopener">Compartir por WhatsApp</a></p>
<h2>Preguntas frecuentes</h2>{"".join(f"<details><summary>{E(q)}</summary><p>{E(a)}</p></details>" for q,a in faq)}
<section class="en" lang="en">{en_html}</section></main>
<footer>© 2026 Bucky Little Shop · Descarga instantánea · Archivos digitales, no se envía nada físico · <a href="../">Ver toda la tienda</a></footer></body></html>'''

M=[("muertos","Kit de Día de Muertos (ES + EN)","Papel picado, ofrenda, calaveritas para colorear, juegos y actividades para casa o el salón.","10.49","ypkit","OA4gi"),
   ("mega","Mega Paquete de Fiestas","Todas las fiestas en un solo paquete: Muertos, Acción de Gracias, Navidad y más. El mejor precio.","29","9P4Oc","9P4Oc"),
   ("kids-mega","Mega Paquete de Actividades para Niños","Laberintos, sopas de letras, para colorear y más, para tener a los niños ocupados.","7.99","Ss82o","Ss82o"),
   ("spanish","Paquete para aprender español / inglés","Vocabulario y actividades bilingües para el salón de clases.","6.99","F1aOK","F1aOK")]
# payhip-only items: point both buttons to payhip
def fix(c):
  k,t,d,pr,g,p=c
  return c
mbody='''<h2>Cómo poner una ofrenda de Día de Muertos paso a paso</h2>
<ol><li><b>Elige el lugar:</b> una mesa o repisa. Puedes hacer niveles con cajas cubiertas con mantel o papel.</li>
<li><b>Coloca la foto</b> de tu ser querido en el nivel más alto.</li>
<li><b>Agrega los cuatro elementos:</b> agua (un vaso), tierra (frutas, semillas, pan de muerto), viento (papel picado) y fuego (velas).</li>
<li><b>Flor de cempasúchil:</b> sus pétalos marcan el camino. Si no consigues flor natural, puedes usar flores de papel.</li>
<li><b>Calaveritas de azúcar o de papel</b> con el nombre de la persona.</li>
<li><b>Lo que le gustaba:</b> su comida, su bebida favorita o un objeto especial.</li>
<li><b>Sal y copal</b> para purificar, según la tradición de tu familia.</li></ol>
<h2>Niveles de la ofrenda: ¿qué va en cada uno?</h2>
<ul><li><b>Ofrenda de 2 niveles:</b> el cielo y la tierra.</li><li><b>De 3 niveles:</b> el cielo, la tierra y el inframundo (o el purgatorio, en la tradición católica).</li><li><b>De 7 niveles:</b> representan los pasos para llegar al descanso. Es la más elaborada.</li></ul>
<p>Para una casa o un salón de clases, la de 2 o 3 niveles es perfecta y se arma en una tarde.</p>
<h2>Papel picado para imprimir (sin herramientas especiales)</h2>
<p>El papel picado tradicional se hace con cincel sobre papel china. Para hacerlo en casa con niños, imprime una plantilla, dobla el papel y recorta con tijeras siguiendo las líneas. Pégalo en un hilo y cuélgalo arriba de la ofrenda. Nuestro kit trae plantillas listas para imprimir en tamaño carta y A4.</p>
<h2>Actividades de Día de Muertos para niños y para el salón</h2>
<ul><li>Calaveritas para colorear y decorar.</li><li>Escribir una calaverita literaria (un verso divertido y respetuoso).</li><li>Lotería o bingo con vocabulario de Día de Muertos.</li><li>Armar una mini ofrenda del salón con fotos de mascotas o personajes históricos.</li></ul>'''
mfaq=[("¿Cuándo se pone la ofrenda de Día de Muertos?","Tradicionalmente se arma a finales de octubre y se mantiene el 1 y 2 de noviembre. Muchas familias la ponen desde el 28 de octubre."),
("¿Qué incluye el kit imprimible de Día de Muertos?","Plantillas de papel picado, calaveritas para colorear, elementos para la ofrenda, juegos y actividades. Viene en español e inglés, tamaño carta y A4."),
("¿Cómo recibo los archivos?","Justo después de pagar recibes un enlace de descarga en pantalla y por correo. Son PDF para imprimir en casa o en la papelería."),
("¿Puedo usarlo en mi salón de clases?","Sí, la licencia permite uso personal y en un salón de clases. No se permite revender ni compartir los archivos."),
("¿Puedo pagar con Mercado Pago?","Sí, usa el enlace “Pagar con Payhip / Mercado Pago” debajo de cada producto.")]
men='''<h2>Day of the Dead printables (English)</h2><p>Teaching Día de Muertos in a Spanish or bilingual classroom? Our <b>bilingual Day of the Dead kit</b> includes papel picado templates, an ofrenda (altar) setup guide, calavera coloring pages and games, all in English and Spanish, US Letter and A4. You get an instant download, print as many copies as your class needs, and nothing is shipped.</p>
<p><b>Quick ofrenda guide:</b> put the photo on the top level, then add water, fruit and pan de muerto (earth), papel picado (wind), candles (fire), marigolds (cempasúchil) and the person's favorite things. Nov 1 honors children and Nov 2 honors adults.</p>'''
html_m=page("dia-de-muertos","Ofrenda de Día de Muertos: guía paso a paso + imprimibles | Bucky",
 "Cómo poner una ofrenda de Día de Muertos paso a paso, qué va en cada nivel, papel picado para imprimir y actividades para niños. Kit bilingüe ES/EN, descarga instantánea.",
 "Ofrenda de Día de Muertos: guía paso a paso + imprimibles",
 "Todo lo que necesitas para poner tu ofrenda en casa o en el salón: qué lleva, qué va en cada nivel, papel picado para imprimir y actividades para niños. Al final encuentras nuestro <b>kit imprimible bilingüe</b> listo para descargar hoy.",
 mbody,M,mfaq,men,"Guía y kit imprimible para la ofrenda de Día de Muertos:","Día de Muertos")
X=[("bundle","Paquete fiesta navideña (completo)","Juegos, intercambio de regalos y decoración. El paquete completo al mejor precio.","15.99","bkgnnd","0NkMo"),
   ("games","Juegos para posada y fiesta navideña","Juegos imprimibles para posadas, oficina o familia, de 5 a 50 personas.","9.99","cnexgy","yR2hw"),
   ("bingo","Lotería / Bingo navideño con imágenes","Cartones con dibujos, ideal para niños y adultos.","5.99","lbizh","AQVW1"),
   ("secret-santa","Kit de intercambio de regalos","Tarjetas, listas de deseos, sorteo y etiquetas para tu intercambio.","6.99","mfqlci","PGsBK"),
   ("planner","Agenda 2027 digital e imprimible","Empieza el año organizado: agenda imprimible y digital con hipervínculos.","7.99","becqk","becqk")]
xbody='''<h2>Cómo organizar una posada paso a paso</h2>
<ol><li><b>Fecha:</b> las posadas tradicionales van del 16 al 24 de diciembre. Para la oficina o la escuela, cualquier fecha de diciembre funciona.</li>
<li><b>Invitaciones:</b> envíalas con 2 o 3 semanas de anticipación, sobre todo si habrá intercambio de regalos.</li>
<li><b>Pedir posada:</b> divide a los invitados en “peregrinos” (afuera) y “posaderos” (adentro) y canten la letanía con velitas.</li>
<li><b>Piñata, ponche y tamales:</b> la piñata de 7 picos, el ponche de frutas y algo rico para compartir.</li>
<li><b>Juegos:</b> prepara 3 o 4 juegos impresos para que nadie se aburra (más abajo hay ideas).</li>
<li><b>Intercambio de regalos:</b> define un monto, haz el sorteo con anticipación y usa etiquetas con nombre.</li></ol>
<h2>Juegos para posada y fiesta navideña</h2>
<ul><li><b>Lotería o bingo navideño:</b> funciona con niños y adultos, y con premios sencillos.</li><li><b>¿Quién es quién? navideño:</b> perfecto para la oficina.</li><li><b>Adivina la canción o el villancico.</b></li><li><b>Sopa de letras y trivia navideña</b> para los más pequeños.</li><li><b>Intercambio “robado”</b> (el regalo se puede robar hasta 2 veces).</li></ul>
<h2>Intercambio de regalos: reglas fáciles</h2>
<ul><li>Fija un monto (por ejemplo $200, $300 o $500 pesos).</li><li>Haz el sorteo con papelitos o tarjetas y pide a cada quien su lista de deseos.</li><li>Pon una etiqueta con el nombre en cada regalo para evitar confusiones.</li></ul>
<h2>Checklist de la fiesta navideña</h2>
<ul><li>☐ Invitaciones enviadas</li><li>☐ Lista de invitados y menú</li><li>☐ Juegos impresos y premios</li><li>☐ Sorteo del intercambio</li><li>☐ Decoración y música</li><li>☐ Piñata, velitas y letanía (si es posada)</li></ul>
<p><b>¿Ya piensas en 2027?</b> Empieza el año organizado con nuestra <a href="https://payhip.com/b/becqk">Agenda 2027 imprimible y digital</a>.</p>'''
xfaq=[("¿Cuándo son las posadas?","Las posadas tradicionales se celebran del 16 al 24 de diciembre, nueve noches antes de Navidad."),
("¿Qué juegos puedo hacer en una posada?","Lotería o bingo navideño, adivinanzas, trivia, ¿quién es quién? y el intercambio de regalos son los favoritos. Nuestros kits traen juegos listos para imprimir."),
("¿Los juegos sirven para la oficina?","Sí. Están pensados para grupos de 5 a 50 personas, para familia, escuela u oficina."),
("¿Vienen en español?","Sí, los imprimibles vienen en español y la mayoría también en inglés, tamaño carta y A4."),
("¿Cómo recibo los archivos?","Recibes un enlace de descarga inmediata en pantalla y por correo. Son PDF, no se envía nada físico.")]
xen='''<h2>Christmas party games & Las Posadas printables (English)</h2><p>Planning a Christmas party, a Las Posadas celebration or a Spanish class holiday activity? Our <b>printable Christmas party games</b>, <b>picture bingo (lotería navideña)</b> and <b>Secret Santa kit</b> come in English and Spanish, US Letter and A4, as an instant download. They're good for families, classrooms and office parties.</p>
<p><b>What is Las Posadas?</b> It's a Mexican tradition held Dec 16–24 that reenacts Mary and Joseph's search for shelter. Guests split into pilgrims and innkeepers and sing a call-and-response song, then the night goes on with a piñata, ponche and tamales.</p>'''
html_x=page("posadas-navidad","Juegos para posada y fiesta navideña + intercambio de regalos | Bucky",
 "Cómo organizar una posada paso a paso, juegos para posada y fiesta navideña, reglas del intercambio de regalos y checklist. Imprimibles en español e inglés, descarga instantánea.",
 "Juegos para posada y fiesta navideña: guía + imprimibles",
 "Organiza tu posada o la fiesta de Navidad de la oficina sin estrés: pasos, juegos, reglas del intercambio de regalos y un checklist. Abajo encuentras nuestros <b>juegos e imprimibles navideños</b> listos para descargar.",
 xbody,X,xfaq,xen,"Juegos e imprimibles para tu posada o fiesta navideña:","Posadas y Navidad")

C=[("planner","Agenda 2027 digital e imprimible","Agenda completa 2027: vista anual, mensual, semanal, metas y hábitos. Inicio lunes o domingo, digital con hipervínculos e imprimible.","7.99","becqk","becqk"),
   ("sheets","Plantillas de presupuesto, menú y boda","Organiza tu dinero y tu menú en 2027 con hojas de cálculo listas.","9.99","063kf","063kf"),
   ("organizador-hogar","Organizador del Hogar Rellenable","Carpeta para organizar la casa: limpieza, menús, pagos y contactos.","6.99","FWMd4","FWMd4")]
cbody='''<h2>Descarga gratis el calendario 2027</h2>
<p><img src="preview.webp" width="510" height="660" alt="Calendario 2027 imprimible gratis en una hoja" style="max-width:100%;height:auto;border:1px solid #ecd9c3;border-radius:10px"></p>
<p><a class="btn" href="Calendario-2027-Imprimible-Gratis_Bucky_Carta-Letter.pdf" download>Descargar PDF tamaño Carta (Letter)</a> <a class="btn" href="Calendario-2027-Imprimible-Gratis_Bucky_A4.pdf" download>Descargar PDF tamaño A4</a></p>
<p>Gratis, sin registro. Es una sola hoja con los 12 meses, la semana empieza en domingo y vienen marcados los días festivos y las fechas especiales de México. Imprímelo en casa o en la papelería; para uso personal o en el salón.</p>
<h2>Días festivos de México en 2027</h2>
<ul><li><b>1 de enero:</b> Año Nuevo</li><li><b>6 de enero:</b> Día de Reyes</li><li><b>1 de febrero:</b> Día de la Constitución (descanso oficial, primer lunes de febrero)</li><li><b>15 de marzo:</b> Natalicio de Benito Juárez (descanso oficial, tercer lunes de marzo)</li><li><b>30 de abril:</b> Día del Niño</li><li><b>1 de mayo:</b> Día del Trabajo</li><li><b>10 de mayo:</b> Día de las Madres</li><li><b>16 de septiembre:</b> Día de la Independencia</li><li><b>2 de noviembre:</b> Día de Muertos</li><li><b>15 de noviembre:</b> Revolución Mexicana (descanso oficial, tercer lunes de noviembre)</li><li><b>12 de diciembre:</b> Día de la Virgen de Guadalupe</li><li><b>25 de diciembre:</b> Navidad</li></ul>
<h2>¿Necesitas más que un calendario?</h2>
<p>La <a href="https://payhip.com/b/becqk">Agenda 2027 de Bucky</a> trae vista anual y mensual, páginas semanales, metas, hábitos, finanzas y notas. Viene en versión digital con hipervínculos (GoodNotes, Notability, Xodo) y en versión imprimible, con inicio en lunes o en domingo, por $7.99 USD.</p>'''
cfaq=[("¿El calendario 2027 es gratis?","Sí, es 100 % gratis y sin registro. Descarga el PDF en tamaño Carta o A4 e imprime todas las copias que necesites para uso personal o en el salón."),
("¿En qué día empieza la semana?","El calendario gratis empieza en domingo. La Agenda 2027 completa viene con inicio en lunes y en domingo."),
("¿Trae los días festivos de México?","Sí, vienen marcados los días festivos oficiales y las fechas especiales más importantes de México en 2027."),
("¿Cuál es la diferencia con la Agenda 2027?","El calendario es una sola hoja con el año completo. La agenda es un planificador completo con páginas mensuales, semanales, metas y hábitos, en versión digital e imprimible.")]
cen='''<h2>Free printable 2027 calendar (English)</h2><p>Download our <b>free one-page 2027 calendar</b> in US Letter or A4 with no signup. It shows all 12 months with bilingual Spanish/English month names, the week starts on Sunday, and Mexican holidays are marked. Need more? The <a href="https://payhip.com/b/becqk">Bucky 2027 Planner</a> ($7.99) includes monthly and weekly pages, goals and habit trackers, in a hyperlinked digital version and a printable one.</p>'''
html_c=page("calendario-2027","Calendario 2027 para imprimir GRATIS (PDF, una hoja) | Bucky",
 "Descarga gratis el calendario 2027 para imprimir en una sola hoja, tamaño Carta y A4, con los días festivos de México. Sin registro. También: Agenda 2027 digital e imprimible.",
 "Calendario 2027 para imprimir gratis (PDF)",
 "Un calendario 2027 bonito, en una sola hoja, con los días festivos de México. <b>Descárgalo gratis</b> en tamaño Carta o A4, sin registro.",
 cbody,C,cfaq,cen,"Calendario 2027 gratis para imprimir:","Calendario 2027")
html_c=html_c.replace('<div class="cta">','<div class="cta" style="display:none">',1)
open("calendario-2027/index.html","w").write(html_c)

kfaq=[("¿Qué es una calaverita literaria?","Es un verso rimado y divertido que se escribe en Día de Muertos, donde la Muerte viene por una persona viva. Es una tradición mexicana."),
("¿Puedo usar estas calaveritas para la tarea?","Sí, úsalas como inspiración. Te recomendamos cambiar algunos versos y agregar detalles de la persona para que sea tuya."),
("¿Cuántos versos debe tener una calaverita?","No hay una regla fija; lo común son 2 a 4 estrofas de 4 versos con rima."),
("¿El generador es gratis?","Sí, es gratis y funciona en el celular. Puedes copiar, imprimir o mandar tu calaverita por WhatsApp.")]
ken='''<h2>Calaveritas literarias generator (English)</h2><p>A <i>calaverita literaria</i> is a short, funny rhyming poem written for Día de Muertos (Day of the Dead), in which La Catrina comes for a living person who escapes in some witty way. Type a name, pick who it's for, and get a Spanish calaverita you can copy, print or share. It's great for Spanish classes. For the classroom ofrenda, see our bilingual Day of the Dead kit below.</p>'''
html_k=page("calaveritas","Generador de calaveritas literarias GRATIS (con nombre) | Bucky",
 "Crea una calaverita literaria con el nombre que quieras: para tu maestra, mamá, amigos o compañeros. Gratis, cópiala, imprímela o mándala por WhatsApp. Cómo escribir tu calaverita paso a paso.",
 "Generador de calaveritas literarias con nombre",
 "Escribe un nombre, elige para quién es y obtén una <b>calaverita literaria</b> divertida y respetuosa para Día de Muertos. Puedes copiarla, imprimirla o mandarla por WhatsApp.",
 open("calav_body.html").read(),M,kfaq,ken,"Haz una calaverita literaria con el nombre que quieras:","Calaveritas literarias")
html_k=html_k.replace('<div class="cta">','<div class="cta" style="display:none">',1)
open("calaveritas/index.html","w").write(html_k)
open("dia-de-muertos/index.html","w").write(html_m);open("posadas-navidad/index.html","w").write(html_x)
sm='<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9" xmlns:xhtml="http://www.w3.org/1999/xhtml"><url><loc>'+U+'</loc><lastmod>2026-10-16</lastmod><xhtml:link rel="alternate" hreflang="es" href="'+U+'"/><xhtml:link rel="alternate" hreflang="en" href="'+U+'?lang=en"/></url>'+"".join(f'<url><loc>{U}{s}/</loc><lastmod>2026-10-16</lastmod></url>' for s in ("dia-de-muertos","posadas-navidad","calendario-2027","calaveritas"))+'</urlset>\n'
open("sitemap.xml","w").write(sm);print("ok")
