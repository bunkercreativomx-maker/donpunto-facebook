#!/usr/bin/env python3
"""Don Punto · Calendario Facebook 30 días (21 oct – 19 nov 2026). Genera calendar.json, PLAN.md e index.html."""
import json, datetime, html

START = datetime.date(2026, 10, 21)
DIAS = ['Lun', 'Mar', 'Mié', 'Jue', 'Vie', 'Sáb', 'Dom']

# pilar, formato, texto en imagen, copy, CTA, visual
P = [
 ("Dolor apps", "Imagen 1:1",
  "Un platillo de $100 en la app te deja $56",
  "Si vendes en apps de comida a domicilio al mismo precio que en tu mostrador, estás trabajando casi gratis.\n\nLa comisión de 30%, el IVA de esa comisión y las retenciones del SAT se llevan casi la mitad de cada platillo. Y nadie te lo dice cuando te das de alta.\n\nDon Punto calcula a cuánto subir cada platillo en cada app para que te llegue lo que tú quieres ganar.\n\nPruébalo 15 días gratis 👉 donpunto.com",
  "Prueba gratis", "Taquero real revisando su celular con cara de 'no puede ser', ticket de app en la mano. Número $56 gigante."),
 ("Engagement", "Imagen 1:1",
  "¿En cuántas apps vendes?",
  "Pregunta rápida para dueños de negocio de comida 🌮\n\n¿En cuántas apps de delivery estás hoy?\n\n0️⃣ Ninguna, puro mostrador\n1️⃣ Una\n2️⃣ Dos\n3️⃣ Tres o más\n\nContesta con el número en comentarios. Te respondemos con un consejo para tu caso.",
  "Comentario", "Mostrador de lonchería con 3 tablets/celulares de pedidos sonando. Persona real atendiendo."),
 ("Educación", "Carrusel 4 (1:1)",
  "Lo que la app se lleva y no ves",
  "Desglose de un platillo de $100 vendido en app (comisión 30%):\n\n1. Comisión de la app: −$30\n2. IVA de esa comisión: −$4.80\n3. Retenciones del SAT: un mordisco más\n4. Lo que te llega: alrededor de $56\n\nY de ahí todavía pagas ingredientes, gas, renta y sueldos.\n\nGuarda este post para cuando vayas a poner tus precios en apps. 📌",
  "Guardar", "Carrusel: cada tarjeta = foto real de un taco + barra que se va 'comiendo' el precio. CONFIRMAR cifra de retenciones (depende de RFC)."),
 ("Producto", "Imagen 1:1",
  "Pones lo que quieres ganar. Don Punto pone el precio.",
  "¿Quieres que te lleguen $100 limpios por tu orden de tacos en la app?\n\nEn Don Punto escribes tu costo y lo que quieres recibir, y te dice a cuánto subirlo en cada app. Platillo por platillo.\n\n¿Cambiaste el precio de la carne? Te lo vuelve a calcular.\n\nDeja de adivinar 👉 donpunto.com",
  "Visitar sitio", "Manos de dueña con delantal sosteniendo celular con la pantalla de precios por app (captura real)."),
 ("Dolor caja", "Imagen 1:1",
  "Contaste la caja 3 veces y no cuadra",
  "Son las 11 de la noche. Ya cerraste. Ya contaste. Y faltan $380.\n\n¿Fue un cambio mal dado? ¿Un pedido de app que no anotaste? ¿Un descuento sin avisar?\n\nCon Don Punto separas efectivo, tarjeta y apps, y sabes cuánto efectivo debe haber en el cajón ANTES de contarlo.\n\n¿Te ha pasado? Cuéntanos en comentarios cuánto te ha faltado. 👇",
  "Comentario", "Dueño cansado contando billetes en mostrador de noche, luz cálida, cajón abierto."),
 ("Producto", "Imagen 1:1",
  "Sin comprar equipo",
  "No necesitas terminal de $15,000 ni computadora nueva.\n\nDon Punto funciona en el celular, la tablet o la compu que ya tienes. Se instala como app en tu celular, tablet o computadora, sin pasar por ninguna tienda de apps.\n\nImprime en tu impresora térmica de 58 mm o en una impresora normal.\n\nRegístrate y pruébalo 15 días gratis 👉 donpunto.com",
  "Prueba gratis", "Tablet vieja recargada en mostrador de cafetería junto a impresora de tickets."),
 ("Comunidad", "Imagen 1:1",
  "Domingo de antojo",
  "Hoy es día de comer bien 😋\n\n¿Cuál es el platillo que más vendes en tu negocio? Presúmelo en comentarios (con foto si quieres) y le damos like a todos.\n\nLos negocios de comida son los que mueven a México. 🇲🇽",
  "Comentario", "Mesa familiar con platillos mexicanos de fonda, foto documental cálida. Sin texto pesado."),
 ("Dolor apps", "Reel / Imagen 1:1 + 9:16",
  "¿Mismo precio en mostrador y en app?",
  "El error más caro de los negocios de comida en apps: subir el menú igual que en el mostrador.\n\nVendes más pedidos… y ganas menos. Trabajas más… y te llevas menos.\n\nLa solución no es salirte de las apps. Es poner el precio correcto.\n\nEscribe PRECIO en comentarios y te mandamos cómo calcular el tuyo.",
  "Comentario palabra clave", "Split: mismo taco, dos etiquetas de precio (mostrador vs app). Dueño real señalando."),
 ("Educación", "Carrusel 4 (1:1)",
  "IVA 16% vs 8% frontera",
  "Si tu negocio está en zona fronteriza (Juárez, Tijuana, Reynosa, Nogales…) puede aplicarte IVA de 8% en lugar de 16%.\n\nEso cambia lo que te quedas de cada venta.\n\nDon Punto separa el IVA de cada venta en 16% u 8% (tú eliges el ajuste) para que veas qué parte es tuya y cuál es del SAT.\n\nDudas fiscales específicas: consúltalas con tu contador. 📌 Guarda este post.",
  "Guardar", "Ticket real impreso con IVA separado, sobre mostrador; foto de dueño con calculadora."),
 ("Producto", "Imagen 1:1",
  "Tu cierre del día, en tu celular",
  "Imagínate llegar a tu casa y que te llegue esto:\n\n🔔 \"Cierre de hoy: 63 ventas · ticket promedio $142\"\n\nEso hace Don Punto cada noche. Sabes cómo te fue aunque no hayas estado en el negocio.\n\nPruébalo 15 días gratis 👉 donpunto.com",
  "Prueba gratis", "Dueña en su sala de noche viendo la notificación en el celular, sonriendo."),
 ("Confianza", "Imagen 1:1",
  "¿Y si se va el internet?",
  "Sigues cobrando.\n\nDon Punto funciona sin conexión en el mismo equipo. Cuando regresa el internet, tus ventas se respaldan solas en la nube.\n\nNada de perder la venta de la hora pico porque se cayó el módem. 📶❌✅\n\nComparte con alguien que siempre batalla con el internet en su local.",
  "Compartir", "Cajera cobrando tranquila mientras el módem tiene luz roja en la repisa."),
 ("Producto", "Imagen 1:1",
  "Tómale foto a tu menú",
  "¿Capturar 80 platillos a mano? No.\n\nEn Don Punto le tomas foto a tu menú impreso y la IA lo convierte en productos con precio. En minutos tienes tu punto de venta listo para cobrar.\n\nCrea tu cuenta y cobra tu primera venta hoy 👉 donpunto.com",
  "Visitar sitio", "Mano con celular fotografiando menú impreso pegado en pared de taquería."),
 ("Dolor control", "Imagen 1:1",
  "¿Quién borró ese ticket?",
  "Cancelaciones, descuentos \"a los cuates\", tickets que desaparecen…\n\nEn Don Punto borrar o descontar pide el PIN del dueño. Y la caja solo ve el punto de venta: reportes, ganancias y ajustes quedan protegidos.\n\nConfía en tu equipo, pero con números claros. 🔒\n\n¿Qué te da más miedo de dejar tu negocio solo? Te leemos.",
  "Comentario", "Dueño de espaldas, cajero joven cobrando; candado/teclado PIN en tablet."),
 ("Comunidad", "Imagen 1:1",
  "Del puesto al local",
  "Muchos negocios empezaron con un comal, una mesa y ganas.\n\n¿Cómo empezó el tuyo? ¿Cuántos años llevas?\n\nCuéntanos tu historia en comentarios. Las mejores las compartimos (con tu permiso) en nuestra página. 🙌",
  "Comentario", "Foto documental: señora mayor en puesto de gorditas con su hija joven. Cálida."),
 ("Educación", "Carrusel 4 (1:1)",
  "¿Cuánto te cuesta de verdad un taco?",
  "La mayoría de los negocios pone precio \"a ojo\" o copiando al de enfrente.\n\nPara saber si ganas, necesitas el costo de la receta:\n1. Tortilla\n2. Proteína (por gramos)\n3. Salsa, cebolla, cilantro, limón\n4. Desechable si es para llevar\n\nEn Don Punto armas la receta y ves costo y margen de cada platillo. 📌 Guarda y haz el ejercicio con tu platillo estrella.",
  "Guardar", "Ingredientes de un taco separados en tabla de picar, foto cenital real."),
 ("Conversión", "Imagen 1:1",
  "15 días gratis. Sin contratos.",
  "Pruébalo completo durante 15 días.\n\n✅ Sin contratos ni penalizaciones\n✅ Te avisamos al celular 3 días antes de cobrar\n✅ Cancelas desde tu cuenta cuando quieras\n✅ Después: Básico $350 o Pro $799 al mes\n\nRegistras tu tarjeta al empezar, pero no se cobra nada hasta el día 16.\n\nEmpieza hoy 👉 donpunto.com",
  "Prueba gratis", "Dueño joven de food truck sonriendo con tablet en la ventanilla."),
 ("Día de Muertos", "Imagen 1:1",
  "Hoy recordamos a quien nos enseñó el sazón",
  "En muchos negocios de comida, la receta estrella viene de la abuela, del papá, de la tía.\n\nHoy les ponemos su ofrenda. 🕯️🌼\n\n¿De quién es la receta que hace famoso a tu negocio? Dedícale unas palabras en comentarios.",
  "Comentario", "Ofrenda real con foto antigua, cempasúchil y un plato de mole junto a un comal. Sin venta."),
 ("Dolor apps", "Imagen 1:1",
  "Vender más no es ganar más",
  "Si tus pedidos de app subieron pero tu cuenta del banco no, revisa tus precios.\n\nCon Don Punto ves tus ventas por canal: mostrador y cada app de delivery, por separado. Sabes de dónde viene tu dinero de verdad.\n\nEscribe CANAL en comentarios y te mostramos cómo se ve el reporte.",
  "Comentario palabra clave", "Repartidor recogiendo bolsas en mostrador, dueña viendo reporte en tablet."),
 ("Producto", "Imagen 1:1",
  "Hecho para la hora pico",
  "12 órdenes esperando. Fila hasta la banqueta.\n\nDon Punto tiene botones grandes, cobro en dos toques, extras (sin cebolla, extra queso), cuentas abiertas por mesa y ticket para cliente y cocina al mismo tiempo.\n\nMenos errores, más rápido. 🔥\n\nPruébalo 15 días gratis 👉 donpunto.com",
  "Prueba gratis", "Taquería llena de noche, taquero cortando pastor, cajera cobrando en tablet."),
 ("Engagement", "Imagen 1:1",
  "¿Libreta, hoja de cálculo o sistema?",
  "Sé honesto 😅 ¿Cómo llevas hoy las ventas de tu negocio?\n\n📒 Libreta\n📊 Hoja de cálculo\n🧠 De memoria\n💻 Un sistema\n\nResponde con el emoji. Sin juzgar, todos empezamos con la libreta.",
  "Comentario", "Libreta de ventas real manchada de salsa junto a una tablet. Mostrador."),
 ("Confianza", "Imagen 1:1",
  "Reportes que entiendes en 10 segundos",
  "No necesitas ser contador para saber cómo te fue.\n\nVentas de hoy, de la semana y del mes, por canal y con el IVA ya separado. Imprimes tu corte Z al cerrar y listo.\n\nComparte con ese amigo que todavía hace el corte con calculadora. 😉",
  "Compartir", "Dueña de cafetería revisando tablet con reporte, taza en mano, mañana."),
 ("Educación", "Carrusel 4 (1:1)",
  "3 señales de que tu negocio pierde dinero sin saberlo",
  "1. No sabes cuánto te cuesta tu platillo más vendido.\n2. Tienes el mismo precio en mostrador y en apps.\n3. Tu caja \"casi\" cuadra… casi todos los días.\n\nSi te identificaste con 2 de 3, no estás solo. Y se arregla con números claros.\n\nGuarda este post y compártelo con tu socio. 📌",
  "Guardar", "Cada tarjeta: foto real de dueño en su local + número grande 1/2/3."),
 ("Producto Pro", "Imagen 1:1",
  "¿Ya tienes empleados? Cada quien con su PIN",
  "Con el plan Pro cada cajero y gerente entra con su propio PIN y permisos distintos.\n\nSabes quién cobró, quién hizo descuentos y quién canceló tickets. Y ves el reporte por persona.\n\nPlan Pro: $799 al mes, 15 días gratis para probarlo 👉 donpunto.com",
  "Visitar sitio", "Equipo de 3 personas en cocina abierta de restaurante pequeño, una cobrando."),
 ("Producto Pro", "Imagen 1:1",
  "El inventario que se descuenta solo",
  "Con el plan Pro, vendes una orden de tacos y Don Punto resta la tortilla, la carne y la salsa de tu inventario.\n\nCuando algo se está acabando, te llega un aviso al celular. Ya no te enteras del faltante a media hora pico.\n\nEscribe INVENTARIO en comentarios y te contamos cómo se configura.",
  "Comentario palabra clave", "Bodeguita/refri de negocio con insumos, dueño revisando celular con alerta."),
 ("Comunidad", "Imagen 1:1",
  "El negocio no descansa, pero tú sí deberías",
  "Abrir temprano, cerrar tarde, hacer compras, cuadrar caja…\n\nDinos en comentarios: ¿qué día descansas tú? 😴\n\n(Si contestaste \"ninguno\", este post es para ti 💛)",
  "Comentario", "Dueño sentado en una silla de plástico afuera de su local cerrado, al atardecer."),
 ("Producto Pro", "Imagen 1:1",
  "Clientes que regresan",
  "Tu cliente de cada viernes merece algo.\n\nEn Don Punto Pro guardas a tus clientes con su teléfono, ves lo que compran y les das recompensas por visita.\n\nUn cliente que regresa vale más que diez que pasan una vez. 🎁\n\nConoce el plan Pro 👉 donpunto.com",
  "Visitar sitio", "Clienta frecuente recibiendo su orden con sonrisa, mesera conocida. Fonda."),
 ("Dolor apps", "Reel / Imagen 1:1 + 9:16",
  "Haz la cuenta con tu platillo",
  "¿Cuánto te deja de verdad tu platillo en la app? Haz la cuenta.

Dentro de Don Punto tienes la calculadora de apps:

1. Pon lo que cuesta tu platillo en mostrador
2. Elige la comisión de tu app
3. Te dice cuánto te queda y a cuánto subirlo

Regístrate y pruébalo 15 días gratis 👉 donpunto.com

Y cuéntanos en comentarios cuánto te salió. 👇",
  "Comentario", "Mano sosteniendo celular con la calculadora de la landing (captura real), platillo al fondo."),
 ("Confianza", "Imagen 1:1",
  "Preguntas que nos hacen",
  "Las 4 dudas más comunes:\n\n❓ ¿Timbra facturas? No. Separa el IVA y te ayuda con tus números, pero no timbra CFDI.\n❓ ¿Qué impresora uso? Cualquier impresora instalada: térmica de 58 mm o carta.\n❓ ¿Necesito equipo? No, usas tu celular, tablet o compu.\n❓ ¿Hay contrato? No, mes a mes.\n\n¿Otra duda? Déjala en comentarios y te respondemos.",
  "Comentario", "Dueña con lentes leyendo su celular en mostrador, signos de pregunta sutiles."),
 ("Conversión", "Imagen 1:1",
  "Tu primera venta, hoy",
  "Así de rápido empiezas:\n\n1️⃣ Crea tu cuenta con tu correo y el nombre de tu negocio\n2️⃣ Sube tu menú (captúralo, desde una hoja de cálculo o con foto)\n3️⃣ Cobra en mostrador y apps, con corte e IVA separado\n\n15 días gratis. Básico $350 / Pro $799 al mes después.\n\n👉 donpunto.com",
  "Prueba gratis", "Taquero abriendo la cortina de su local en la mañana, tablet en mano."),
 ("Conversión", "Imagen 1:1",
  "Deja de adivinar cuánto ganas",
  "Un mes después de usar Don Punto vas a saber cuál es tu platillo estrella, cuál no se vende, cuánto ganas en cada app y si tu caja cuadra.\n\nEso no es un sistema. Es tranquilidad.\n\nPruébalo 15 días gratis 👉 donpunto.com",
  "Prueba gratis", "Dueña de taquería de brazos cruzados, orgullosa, frente a su local lleno."),
]

assert len(P) == 30, len(P)
ORDER=[0,1,2,3,6,4,5,7,8,9,10,13,16,11,12,14,15,17,24,18,19,20,21,22,23,26,25,27,28,29]
assert sorted(ORDER)==list(range(30))
P=[P[i] for i in ORDER]
posts = []
for i, (pilar, fmt, hook, copy, cta, visual) in enumerate(P):
    d = START + datetime.timedelta(days=i)
    posts.append(dict(day=i + 1, date=d.isoformat(), weekday=DIAS[d.weekday()], pillar=pilar, format=fmt,
                      imageText=hook, copy=copy, cta=cta, visual=visual,
                      hashtags="#DonPunto #PuntoDeVenta #NegociosDeComida #Restaurantes #Taquerías"))

json.dump(dict(client="donpunto", campaign="oct-nov-2026", language="es-MX",
               window=f"{posts[0]['date']} a {posts[-1]['date']}", posts=posts),
          open('calendar.json', 'w'), ensure_ascii=False, indent=2)

# Markdown
md = ["# Don Punto · Facebook 30 días", f"Ventana: {posts[0]['date']} → {posts[-1]['date']} · Idioma: español MX · Hora sugerida: 12:30 y 20:00 alternado\n",
      "| # | Fecha | Pilar | Formato | Texto en imagen | CTA |", "|---|---|---|---|---|---|"]
for p in posts:
    md.append(f"| {p['day']} | {p['weekday']} {p['date'][5:]} | {p['pillar']} | {p['format']} | {p['imageText']} | {p['cta']} |")
md.append("")
for p in posts:
    md += [f"## Día {p['day']} · {p['weekday']} {p['date']} · {p['pillar']}", f"**Imagen:** {p['imageText']}", "", p['copy'], "", p['hashtags'], "", f"_Visual:_ {p['visual']}", ""]
open('PLAN.md', 'w').write("\n".join(md))

# HTML
from collections import Counter
mix = Counter(p['pillar'].split()[0] for p in posts)
cards = []
for p in posts:
    cards.append(f"""<article class=card data-pillar="{html.escape(p['pillar'])}">
<div class=meta><span class=num>Día {p['day']}</span><span>{p['weekday']} {p['date'][8:]}/{p['date'][5:7]}</span><span class=tag>{html.escape(p['pillar'])}</span><span class=fmt>{html.escape(p['format'])}</span></div>
<h3>{html.escape(p['imageText'])}</h3>
<pre>{html.escape(p['copy'])}

{p['hashtags']}</pre>
<button onclick="navigator.clipboard.writeText(this.previousElementSibling.textContent);this.textContent='¡Copiado!'">Copiar copy</button>
<p class=vis><b>Visual:</b> {html.escape(p['visual'])}</p>
<p class=cta>CTA: {html.escape(p['cta'])}</p></article>""")
page = f"""<!doctype html><html lang=es><meta charset=utf-8><meta name=viewport content="width=device-width,initial-scale=1">
<title>Don Punto · Facebook 30 días</title>
<style>
body{{font-family:system-ui,-apple-system,sans-serif;background:#FAFAF7;color:#0f1d18;margin:0;padding:24px}}
header{{max-width:1100px;margin:0 auto 24px}} h1{{margin:0 0 6px;font-size:28px}} .sub{{color:#5b6b64}}
.mix span{{display:inline-block;background:#e7efe9;border-radius:99px;padding:4px 10px;margin:4px 4px 0 0;font-size:13px}}
.grid{{max-width:1100px;margin:0 auto;display:grid;grid-template-columns:repeat(auto-fill,minmax(320px,1fr));gap:16px}}
.card{{background:#fff;border:1px solid #e3e7e4;border-radius:16px;padding:18px}}
.meta{{display:flex;flex-wrap:wrap;gap:6px;font-size:12px;color:#5b6b64}} .num{{font-weight:700;color:#0f6b4f}}
.tag{{background:#fff4d6;border-radius:6px;padding:1px 6px}} .fmt{{background:#eef2f0;border-radius:6px;padding:1px 6px}}
h3{{margin:10px 0;font-size:19px}} pre{{white-space:pre-wrap;font-family:inherit;font-size:14px;line-height:1.45;background:#f6f8f7;padding:12px;border-radius:10px;margin:0}}
button{{margin-top:8px;border:0;background:#0f6b4f;color:#fff;border-radius:99px;padding:8px 14px;cursor:pointer}}
.vis{{font-size:13px;color:#46554f}} .cta{{font-size:12px;color:#0f6b4f;font-weight:600;margin:0}}
</style>
<header><h1>Don Punto · Facebook 30 días</h1>
<div class=sub>{posts[0]['date']} → {posts[-1]['date']} · Español MX · Borrador para aprobación (copys). Imágenes: después de aprobar.</div>
<div class=mix>{''.join(f'<span>{k}: {v}</span>' for k,v in mix.most_common())}</div></header>
<main class=grid>{''.join(cards)}</main></html>"""
open('index.html', 'w').write(page)
print(len(posts), mix)
