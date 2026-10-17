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
  import urllib.parse as up
  link=(G+g) if g!=p else (P+p)
  wa='https://wa.me/?text='+up.quote(f'¡Mira esto! {title} 👉 {link}\n(EN) Check this out 👉 {link}\nDe/From Bucky Little Shop')
  return f'''<div class="card"><img src="../img/{k}.webp" width="800" height="800" loading="lazy" alt="{E(title)}"><div><h3>{E(title)}</h3><p>{E(desc)}</p><span class="price">${price} USD</span>
'''+(f'<a class="btn" href="{G+g}" rel="noopener">Comprar / Buy</a><a class="alt" href="{P+p}" rel="noopener">Pagar con Payhip / Mercado Pago</a>' if g!=p else f'<a class="btn" href="{P+p}" rel="noopener">Comprar / Buy</a><span class="alt">Pago con Payhip / Mercado Pago</span>')+f'<a class="btn wa" href="{wa}" target="_blank" rel="noopener" style="display:block;text-align:center;margin-top:8px">Compartir por WhatsApp / Share</a></div></div>'
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
<link rel="icon" href="../favicon.ico"><meta name="theme-color" content="#7a4a26"><style>{CSS}.alt,a.alt,footer a,.crumb a,p>a:first-child{{display:inline-block;padding:6px 0;min-height:24px}}</style>
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
   ("mega","Mega Paquete de Fiestas","Todas las fiestas en un solo paquete: Muertos, Acción de Gracias, Navidad y más. El mejor precio.","29","oypqoh","9P4Oc"),
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
 '<div style="background:#FFF1E2;border:2px dashed #F0932F;border-radius:14px;padding:14px 18px;margin:18px 0"><h2 style="margin-top:0">Lotería de Día de Muertos GRATIS (muestra)</h2><p>2 tablas y las 24 cartas para recortar, con vocabulario en español (la calavera, el cempasúchil, el papel picado…). Ideal para el salón o para jugar en familia. Sin registro.</p><p><a class="btn" href="Loteria-Dia-de-Muertos-GRATIS_Bucky_Carta-Letter.pdf" download>Descargar PDF Carta (Letter)</a> <a class="btn" href="Loteria-Dia-de-Muertos-GRATIS_Bucky_A4.pdf" download>Descargar PDF A4</a></p><p style="font-size:.9rem">¿Quieres las 6 tablas, bingo, sopas de letras y más? Están en los <a href="https://payhip.com/b/Io2Lj">Juegos de clase en español</a>.</p></div>'+mbody,M,mfaq,men,"Guía y kit imprimible para la ofrenda de Día de Muertos:","Día de Muertos")
X=[("tarjetas-navidad","Tarjetas navideñas de Bucky (12 + 16 etiquetas)","12 tarjetas para doblar con mensaje adentro + 16 etiquetas para regalo. ES + EN.","3.99","kV1Uf","kV1Uf"),("pasatiempos-navidad","Pasatiempos navideños en letra grande","20 sopas de letras + 15 crucigramas con respuestas. Ideal para abuelas y abuelos.","4.99","srtKQ","srtKQ"),("combo-posada","Combo Posada + Agenda 2027","Kit de posada e intercambio + Agenda 2027 + letanía de regalo. 40 % menos que por separado.","14.49","2qHnv","2qHnv"),("bundle","Paquete fiesta navideña (completo)","Juegos, intercambio de regalos y decoración. El paquete completo al mejor precio.","15.99","bkgnnd","0NkMo"),
   ("games","Juegos para posada y fiesta navideña","Juegos imprimibles para posadas, oficina o familia: lotería, bingo, trivia y más.","9.99","cnexgy","yR2hw"),
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
<ul><li><b>Lotería o bingo navideño:</b> funciona con niños y adultos, y con premios sencillos.</li><li><b>¿Quién soy? navideño:</b> perfecto para la oficina.</li><li><b>Adivina la canción o el villancico.</b></li><li><b>Palabras revueltas y trivia navideña</b> para toda la familia.</li><li><b>Intercambio “robado”</b> (el regalo se puede robar hasta 2 veces).</li></ul>
<h2>Intercambio de regalos: reglas fáciles</h2>
<ul><li>Fija un monto (por ejemplo $200, $300 o $500 pesos).</li><li>Haz el sorteo con papelitos o tarjetas y pide a cada quien su lista de deseos.</li><li>Pon una etiqueta con el nombre en cada regalo para evitar confusiones.</li></ul>
<h2>Checklist de la fiesta navideña</h2>
<ul><li>☐ Invitaciones enviadas</li><li>☐ Lista de invitados y menú</li><li>☐ Juegos impresos y premios</li><li>☐ Sorteo del intercambio</li><li>☐ Decoración y música</li><li>☐ Piñata, velitas y letanía (si es posada)</li></ul>
<p><b>¿Ya piensas en 2027?</b> Empieza el año organizado con nuestra <a href="https://payhip.com/b/becqk">Agenda 2027 imprimible y digital</a>.</p>'''
xfaq=[("¿Cuándo son las posadas?","Las posadas tradicionales se celebran del 16 al 24 de diciembre, nueve noches antes de Navidad."),
("¿Qué juegos puedo hacer en una posada?","Lotería o bingo navideño, adivinanzas, trivia, ¿quién es quién? y el intercambio de regalos son los favoritos. Nuestros kits traen juegos listos para imprimir."),
("¿Los juegos sirven para la oficina?","Sí. Funcionan con grupos chicos o grandes, en familia, escuela u oficina."),
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

TG=[("combo-gratitud","Gratitude + Christmas Combo (EN + ES)","Thanksgiving kit + 13 Christmas party games. Save 44%.","9.99","9LMt6","9LMt6"),("thanksgiving","Thanksgiving Printables Kit (EN + ES)","Gratitude cards, games, place cards and table decor. Bilingual, Letter + A4.","7.79","ckmaso","LQBfv"),
    ("mega","All Holidays Mega Pack","Thanksgiving, Christmas, Día de Muertos and more in one bundle. Best value.","29","oypqoh","9P4Oc"),
    ("teachers","Spanish Classroom Games Bundle","Bingo, loterías, word searches and conversation cards for Spanish class.","6.99","Io2Lj","Io2Lj"),
    ("kids-mega","Kids Activity Mega Pack","Mazes, coloring, dot-to-dot and puzzles to keep kids busy.","7.99","Ss82o","Ss82o")]
tfaq=[("When is Thanksgiving 2026?","Thanksgiving 2026 is on Thursday, November 26."),("How do I get the files?","Right after checkout you get a download link on screen and by email. Print at home or at a print shop. Nothing is shipped."),("Is it in Spanish too?","Yes. The kit includes English and Spanish versions, great for bilingual families and Spanish classes."),("Can I use it in my classroom?","Yes, the license covers personal and single-classroom use.")]
html_t=page("thanksgiving-printables","Thanksgiving Printables: Last-Minute Kids Activities, Gratitude Cards & Table Decor | Bucky",
 "Instant-download Thanksgiving printables for kids and classrooms: gratitude cards, games, place cards and table decor, in English and Spanish. Print at home today.",
 "Last-minute Thanksgiving printables for kids & classrooms",
 "Gratitude cards, games and table decor you can <b>download and print today</b>, in English and Spanish, for home or the classroom.",
 open("tg_body.html").read(),TG,tfaq,"<h2>Acción de Gracias (español)</h2><p>Kit imprimible de Acción de Gracias con tarjetas de gratitud, juegos y decoración, en español e inglés. Descarga instantánea.</p>","Thanksgiving printables for kids & classrooms:","Thanksgiving")
html_t=html_t.replace('<html lang="es">','<html lang="en">',1)
for a,b in [("<a href=\"../\">Inicio</a>","<a href=\"../\">Home</a>"),("Compartir por WhatsApp / Share","Share on WhatsApp"),("Compartir por WhatsApp","Share on WhatsApp"),("Imprimibles listos para descargar","Ready-to-download printables"),("Preguntas frecuentes","FAQ"),("Pagar con Payhip / Mercado Pago","Pay with Payhip / Mercado Pago"),("Pago con Payhip / Mercado Pago","Checkout via Payhip / Mercado Pago"),("Comprar / Buy","Buy now"),("Descarga instantánea · Archivos digitales, no se envía nada físico · <a href=\"../\">Ver toda la tienda</a>","Instant download · Digital files, nothing is shipped · <a href=\"../\">See the whole shop</a>")]:html_t=html_t.replace(a,b)
open("thanksgiving-printables/index.html","w").write(html_t)
LT=[("combo-posada","Combo Posada + Agenda 2027","Kit de posada e intercambio + Agenda 2027 + letanía de regalo. 40 % menos que por separado.","14.49","2qHnv","2qHnv"),("games","Juegos para posada y fiesta navideña","Juegos imprimibles para posadas, oficina o familia.","9.99","cnexgy","yR2hw"),
    ("bundle","Paquete fiesta navideña (completo)","Juegos, intercambio y decoración al mejor precio.","15.99","bkgnnd","0NkMo"),
    ("bingo","Lotería / Bingo navideño","Cartones con dibujos para niños y adultos.","5.99","lbizh","AQVW1"),
    ("secret-santa","Kit de intercambio de regalos","Tarjetas, listas de deseos y etiquetas.","6.99","mfqlci","PGsBK")]
lfaq=[("¿Cuándo se pide posada?","En las posadas, del 16 al 24 de diciembre, normalmente al inicio de la fiesta y antes de la piñata."),("¿Quién canta cada parte?","Los peregrinos (afuera, con velitas) piden posada y los posaderos (adentro) responden. Al final todos cantan juntos “Entren, santos peregrinos”."),("¿Puedo imprimir la letra?","Sí. Descarga la hoja en PDF (carta o A4) o usa el botón “Imprimir la letra”."),("¿La letra es la misma en todo México?","Hay variantes regionales en algunos versos; aquí está una de las versiones tradicionales más cantadas.")]
html_l=page("letania-posadas","Letra para pedir posada completa (para imprimir) + cómo se canta | Bucky",
 "Letra completa para pedir posada: versos de peregrinos y posaderos, “Entren, santos peregrinos” y cómo se canta paso a paso. Lista para imprimir gratis.",
 "Letra para pedir posada (completa y para imprimir)",
 "La letra tradicional para pedir posada, con los versos de <b>afuera</b> y de <b>adentro</b>, lista para imprimir y repartir. Abajo encuentras juegos imprimibles para seguir la fiesta.",
 '<div style="background:#FFF1E2;border:2px dashed #F0932F;border-radius:14px;padding:14px 18px;margin:18px 0"><h2 style="margin-top:0">Hoja de la letanía GRATIS en PDF</h2><p>2 páginas con colores para Afuera, Adentro y Todos, en letra grande para leer con velitas. Sin registro.</p><p><a class="btn" href="Letania-para-pedir-posada_ES_US-Letter.pdf" download>Descargar PDF Carta (Letter)</a> <a class="btn" href="Letania-para-pedir-posada_ES_A4.pdf" download>Descargar PDF A4</a></p></div>'+open("lt_body.html").read(),LT,lfaq,"<h2>Las Posadas song lyrics (English)</h2><p>These are the traditional Spanish lyrics for <i>pedir posada</i>, the call-and-response song of Mexico's Las Posadas (Dec 16–24). Pilgrims sing outside and innkeepers answer from inside, and everyone sings together when the door opens. Print them for your Spanish class or family celebration, and see our bilingual Christmas party games below.</p>","Letra para pedir posada, lista para imprimir:","Letra para pedir posada")
html_l=html_l.replace('<div class="cta">','<div class="cta" style="display:none">',1)
open("letania-posadas/index.html","w").write(html_l)

SS=[("secret-santa","Kit de intercambio de regalos","Tarjetas para el sorteo, listas de deseos y etiquetas para regalos. ES + EN.","6.99","mfqlci","PGsBK"),
    ("bundle","Paquete fiesta navideña (completo)","Juegos, intercambio y decoración al mejor precio.","15.99","bkgnnd","0NkMo"),
    ("games","Juegos para posada y fiesta navideña","Juegos imprimibles para oficina, escuela o familia.","9.99","cnexgy","yR2hw"),
    ("planner","Agenda 2027 digital e imprimible","Un regalo útil: agenda 2027 imprimible y digital.","7.99","becqk","becqk")]
sfaq=[("¿Cuánto se gasta en un intercambio de regalos?","Lo más común en México es entre $200 y $500 pesos. Lo importante es que todos respeten el mismo monto."),("¿Cómo se hace el sorteo?","Escribe los nombres en tarjetas, que cada quien saque una sin enseñarla y vuelva a sacar si le toca su propio nombre. Nuestro kit trae tarjetas listas."),("¿Qué regalo dar si no conozco bien a la persona?","Algo útil y neutral: taza o termo, vela, planta, dulces o una libreta bonita."),("¿Estas ideas tienen ligas de afiliados?","No. Son ideas genéricas para que compres donde prefieras.")]
html_s=page("ideas-intercambio-regalos","Ideas para intercambio de regalos de $200, $300 y $500 pesos (2026) | Bucky",
 "Ideas para intercambio de regalos por precio: $200, $300 y $500 pesos, para la oficina, maestros y niños, más reglas fáciles y el sorteo. Kit imprimible de intercambio.",
 "Ideas para intercambio de regalos por precio: $200, $300 y $500",
 "¿Te tocó intercambio y no sabes qué regalar? Aquí tienes <b>ideas por monto</b>, regalos para la oficina, los maestros y los niños, y las reglas para que el intercambio salga perfecto.",
 open("ss_body.html").read(),SS,sfaq,"<h2>Secret Santa gift ideas by price (English)</h2><p>Gift ideas for a Secret Santa exchange at about $10, $15 and $25 USD: mugs with cocoa, fun socks, candles, tumblers, coffee kits, spa kits, small speakers, LED lights and puzzles. They're generic ideas with no affiliate links. Our printable Secret Santa kit includes draw cards, wish lists and gift tags in English and Spanish.</p>","Ideas para intercambio de regalos por precio:","Ideas para intercambio de regalos")
open("ideas-intercambio-regalos/index.html","w").write(html_s)
AD=[("tarjetas-navidad","Tarjetas navideñas de Bucky (12 + 16 etiquetas)","12 tarjetas para doblar con mensaje adentro + 16 etiquetas para regalo. ES + EN.","3.99","kV1Uf","kV1Uf"),("reyes-kit","Kit Día de Reyes de Bucky","14 páginas: carta, corona, colorear, sopa de letras, laberinto, memorama y diploma. ES + EN.","4.99","VEPLY","VEPLY"),("devocional-adviento","Devocional de Adviento de Ana Hope (ES + EN)","24 devociones de una página: versículo (RV1909 / KJV), reflexión, oración y acción. Carta y A4.","4.99","rsbKI","rsbKI"),("bundle","Paquete fiesta navideña (completo)","Todo el paquete de Navidad de una vez: juegos, intercambio y decoración.","15.99","bkgnnd","0NkMo"),
    ("bingo","Lotería / Bingo navideño","Cartones con dibujos para niños y adultos.","5.99","lbizh","AQVW1"),
    ("games","Juegos para posada y fiesta navideña","Juegos imprimibles para posadas, oficina o familia.","9.99","cnexgy","yR2hw"),
    ("secret-santa","Kit de intercambio de regalos","Tarjetas, listas de deseos y etiquetas.","6.99","mfqlci","PGsBK")]
afaq=[("¿El calendario de Adviento es gratis?","Sí. Cada día del 1 al 24 de diciembre se abre un imprimible gratis en PDF, sin registro."),("¿A qué hora se abre cada puerta?","A la medianoche, hora de la Ciudad de México."),("¿En qué idioma vienen?","Cada PDF trae la página en español y en inglés."),("¿Me perdí un día, lo puedo descargar?","Sí, las puertas anteriores siguen abiertas hasta el 24 de diciembre y después.")]
html_a=page("adviento","Calendario de Adviento GRATIS 2026: un imprimible navideño cada día | Bucky",
 "Calendario de Adviento gratis del 1 al 24 de diciembre: cada día se abre un imprimible navideño en PDF (español e inglés): juegos, etiquetas, trivia y bingo. Sin registro.",
 "Calendario de Adviento de Bucky: un imprimible gratis cada día",
 "Del <b>1 al 24 de diciembre</b> se abre una puerta cada día con un <b>imprimible navideño gratis</b> en español e inglés. Guarda esta página y vuelve cada día.",
 open("adv_body.html").read(),AD,afaq,"<h2>Free Advent printable calendar (English)</h2><p>From December 1 to 24, a new door opens each day (Mexico City time) with a <b>free Christmas printable PDF</b> in English and Spanish: gift tags, trivia, bingo, party games and more. There's no signup. Want everything now? Get the full Christmas Party Bundle below.</p>","Calendario de Adviento gratis, un imprimible cada día:","Calendario de Adviento")
html_a=html_a.replace('<div class="cta">','<div class="cta" style="display:none">',1)
open("adviento/index.html","w").write(html_a)
open("dia-de-muertos/index.html","w").write(html_m);open("posadas-navidad/index.html","w").write(html_x)
JPA=[("combo-posada","Combo Posada + Agenda 2027","Kit de posada e intercambio + Agenda 2027 + letanía de regalo. 40 % menos que por separado.","14.49","2qHnv","2qHnv"),
 ("games","Juegos para posada (13 juegos)","Lotería, basta, trivia, villancicos con emojis, mímica, cuento izquierda–derecha y más. ES + EN.","9.99","cnexgy","yR2hw"),
 ("bingo","Lotería / Bingo navideño","Cartones con dibujos para grupos grandes.","5.99","lbizh","AQVW1"),
 ("secret-santa","Kit de intercambio de regalos","Tarjetas para el sorteo, listas de deseos y etiquetas.","6.99","mfqlci","PGsBK")]
jfaq=[("¿Qué juegos funcionan en una posada de oficina?","Los rápidos y por equipos: trivia navideña, villancicos con emojis, bingo de invitados y ¿qué preferirías?. Deja el intercambio con robo para el final."),("¿Cuántos juegos necesito para una posada?","Con 3 o 4 juegos de 10 minutos alcanza para una fiesta de 2 a 3 horas, más la piñata y el intercambio."),("¿Los juegos imprimibles traen respuestas?","Sí. La trivia, los villancicos con emojis y las palabras revueltas traen hoja de respuestas."),("¿Sirven para personas que no hablan español?","Sí, cada juego del kit viene en español y en inglés.")]
html_j=page("juegos-posada-adultos","12 juegos para posada para adultos (oficina y familia) + imprimibles | Bucky",
 "12 juegos para posada para adultos: lotería navideña, basta, intercambio con robo, trivia, villancicos con emojis y más. Ideas para la oficina y la familia, con juegos listos para imprimir.",
 "Juegos para posada para adultos: 12 ideas que sí funcionan",
 "Juegos divertidos <b>para adultos</b> que también pueden jugar peques y personas mayores: para la posada de la oficina, con amistades o en familia. Varios vienen listos para imprimir.",
 open("jpa_body.html").read(),JPA,jfaq,"<h2>Posada party games for adults (English)</h2><p>Twelve party games for a Mexican posada or office Christmas party: Christmas lotería, Basta (Scattergories), white-elephant gift swap, the left–right gift story, Christmas trivia, emoji carols, Who Am I?, charades, Would You Rather, find-the-guest bingo, minute-to-win-it challenges and an ugly sweater contest. Our printable Posada Games kit includes nine of them in English and Spanish.</p>","Juegos para posada para adultos:","Juegos para posada para adultos")
open("juegos-posada-adultos/index.html","w").write(html_j)
TNG=[("tarjetas-navidad","Tarjetas navideñas de Bucky (12 + 16 etiquetas)","12 tarjetas para doblar con mensaje adentro + 16 etiquetas para regalo. ES + EN.","3.99","kV1Uf","kV1Uf"),("tarjetas-felicitacion","24 tarjetas de felicitación para imprimir","Cumpleaños, aniversario, Día de las Madres, condolencias, gracias y más, con mensaje adentro. ES + EN.","4.99","mbhYp","mbhYp"),
 ("secret-santa","Kit de intercambio de regalos","Etiquetas para regalos, tarjetas para el sorteo y listas de deseos.","6.99","mfqlci","PGsBK"),
 ("bundle","Paquete fiesta navideña (completo)","Juegos, intercambio y decoración para la posada.","15.99","bkgnnd","0NkMo"),
 ("combo-posada","Combo Posada + Agenda 2027","Kit de posada + Agenda 2027 + letanía. 40 % menos.","14.49","2qHnv","2qHnv")]
tfaq=[("¿Las tarjetas navideñas son gratis?","Sí. Las 4 tarjetas de esta página son gratis para uso personal, sin registro."),("¿De qué tamaño quedan?","Dobladas miden 10.8 × 14 cm en papel carta (unos 10.5 × 14.8 cm en A4). Caben en un sobre pequeño."),("¿Tengo que imprimir por los dos lados?","No. Se imprimen de un solo lado y se doblan en cuatro."),("¿Puedo venderlas?","No, son para uso personal: regalarlas, usarlas en casa o en tu salón.")]
html_t=page("tarjetas-navidenas-gratis","Tarjetas navideñas para imprimir GRATIS (PDF, español e inglés) | Bucky",
 "Descarga gratis tarjetas navideñas para imprimir en PDF: ¡Feliz Navidad! y ¡Felices posadas!, con mensaje adentro, en español e inglés. Tamaño carta y A4, sin registro.",
 "Tarjetas navideñas para imprimir gratis",
 "Tarjetas tiernas de Bucky <b>listas para imprimir, doblar y regalar</b>, con el mensaje ya escrito adentro. Gratis, en tamaño carta y A4.",
 open("tng_body.html").read(),TNG,tfaq,"<h2>Free printable Christmas cards (English)</h2><p>Download 4 free printable Christmas cards with Bucky: Merry Christmas and Happy Posadas in English, and ¡Feliz Navidad! and ¡Felices posadas! in Spanish. Each card prints on one side of a Letter or A4 page and folds into quarters, with the message already inside. Free for personal use, no signup.</p>","Tarjetas navideñas para imprimir gratis:","Tarjetas navideñas gratis")
html_t=html_t.replace('<div class="cta">','<div class="cta" style="display:none">',1)
open("tarjetas-navidenas-gratis/index.html","w").write(html_t)
MN=[("tarjetas-navidad","Tarjetas navideñas de Bucky (12 + 16 etiquetas)","12 tarjetas para doblar con mensaje adentro + 16 etiquetas para regalo. ES + EN.","3.99","kV1Uf","kV1Uf"),("kids-mega","Mega paquete de actividades para niños","Cientos de páginas: colorear, laberintos, sopas de letras y más. ES + EN.","7.99","Ss82o","Ss82o"),
 ("bucky-coloring","Páginas para colorear de Bucky","Dibujos de Bucky para colorear en casa o en el salón.","2.99","U64TI","U64TI"),
 ("bucky-storybooks","Cuentos de Bucky (3 cuentos + colorear)","3 cuentos imprimibles para peques de 3 a 7 años. ES + EN.","4.99","U0mF4","U0mF4"),
 ("bundle","Paquete fiesta navideña (completo)","Juegos, intercambio y decoración para la posada.","15.99","bkgnnd","0NkMo")]
mfaq=[("¿Las manualidades son gratis?","Sí. El PDF de 4 páginas es gratis para uso personal o en tu salón, sin registro."),("¿Para qué edad son?","De 3 a 10 años, aproximadamente. Peques de 3 a 5 años necesitan ayuda para recortar."),("¿Qué papel uso?","Papel normal funciona; en cartulina ligera los adornos y la estrella quedan más firmes."),("¿Vienen en inglés?","Las instrucciones vienen en español y en inglés en cada página.")]
html_mn=page("manualidades-navidenas-ninos","Manualidades navideñas para niños imprimibles GRATIS (PDF) | Bucky",
 "Manualidades navideñas para niños para imprimir gratis: adornos para colorear y recortar, cadena de papel, estrella para el árbol y Bucky para colorear. PDF carta y A4.",
 "Manualidades navideñas para niños imprimibles",
 "Manualidades <b>fáciles y gratis</b> para hacer en casa o en el salón: imprime, colorea, recorta y adorna. Listas en tamaño carta y A4.",
 open("mn_body.html").read(),MN,mfaq,"<h2>Free printable Christmas crafts for kids (English)</h2><p>Download a free 4-page Christmas craft PDF: 6 ornaments to color, cut and hang, a colorful paper chain, a Bucky coloring page and a tree-top star. Instructions are in English and Spanish, in US Letter and A4. Free for home or classroom use, no signup.</p>","Manualidades navideñas gratis para niños:","Manualidades navideñas")
html_mn=html_mn.replace('<div class="cta">','<div class="cta" style="display:none">',1)
open("manualidades-navidenas-ninos/index.html","w").write(html_mn)
RR=[("reyes-kit","Kit Día de Reyes de Bucky","14 páginas: carta, corona, colorear, sopa de letras, laberinto, memorama y diploma. ES + EN.","4.99","VEPLY","VEPLY"),("recetas-familia","Recetas mexicanas de la familia","Recetario imprimible con tamales, pozole, salsas, bebidas y postres. ES + EN.","5.99","Qnl6V","Qnl6V"),
 ("kids-mega","Mega paquete de actividades para niños","Para las vacaciones de invierno: colorear, laberintos y más.","7.99","Ss82o","Ss82o"),
 ("planner","Agenda 2027 digital e imprimible","Empieza el año organizado.","7.99","becqk","becqk"),
 ("bucky-coloring","Páginas para colorear de Bucky","Dibujos de Bucky para colorear.","2.99","U64TI","U64TI")]
rfaq=[("¿Cuándo se parte la Rosca de Reyes?","El 6 de enero, Día de Reyes, normalmente en la merienda con chocolate caliente."),("¿Qué pasa si me sale el muñequito?","La tradición dice que invitas los tamales el 2 de febrero, Día de la Candelaria."),("¿Qué significa la forma de la rosca?","Su forma redonda representa una corona y la fruta de encima, las joyas de los Reyes Magos."),("¿La carta y la corona son gratis?","Sí, el PDF de muestra es gratis para uso personal, en español y en inglés.")]
html_rr=page("rosca-de-reyes","Rosca de Reyes: significado, tradición y actividades para niños (gratis) | Bucky",
 "Qué es la Rosca de Reyes, qué significa el muñequito, cómo partirla y actividades para niños: carta a los Reyes Magos y corona de papel gratis para imprimir.",
 "Rosca de Reyes: significado, tradiciones y actividades",
 "Todo sobre la <b>Rosca de Reyes</b> del 6 de enero, explicado fácil para compartir con peques, más una <b>carta a los Reyes Magos y una corona gratis</b> para imprimir.",
 open("rr_body.html").read(),RR,rfaq,"<h2>Rosca de Reyes and Three Kings Day (English)</h2><p>The Rosca de Reyes is a ring-shaped sweet bread shared on January 6, Three Kings Day. Hidden inside is a small figurine of baby Jesus, and whoever finds it hosts a tamales party on February 2 (Candelaria). Download a free letter to the Three Kings and a paper crown in English and Spanish.</p>","Rosca de Reyes, tradición y actividades gratis:","Rosca de Reyes")
html_rr=html_rr.replace('<div class="cta">','<div class="cta" style="display:none">',1)
open("rosca-de-reyes/index.html","w").write(html_rr)
sm='<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9" xmlns:xhtml="http://www.w3.org/1999/xhtml"><url><loc>'+U+'</loc><lastmod>2026-10-16</lastmod><xhtml:link rel="alternate" hreflang="es" href="'+U+'"/><xhtml:link rel="alternate" hreflang="en" href="'+U+'?lang=en"/></url>'+"".join(f'<url><loc>{U}{s}/</loc><lastmod>2026-10-16</lastmod></url>' for s in ("dia-de-muertos","posadas-navidad","calendario-2027","calaveritas","thanksgiving-printables","letania-posadas","ideas-intercambio-regalos","adviento","juegos-posada-adultos","tarjetas-navidenas-gratis","manualidades-navidenas-ninos","rosca-de-reyes"))+'</urlset>\n'
open("sitemap.xml","w").write(sm);print("ok")
