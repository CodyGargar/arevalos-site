#!/usr/bin/env python3
"""Generates the Spanish (/es/) pages. Run: python3 build-es.py"""
import os, pathlib

OUT = pathlib.Path("es"); OUT.mkdir(exist_ok=True)

TEL1, TEL2 = "+12147188587", "+14693506499"
EMAIL = "arevalostransmission@gmail.com"

# es page -> (english counterpart, nav label)
PAGES = {
    "index.html": ("../index.html", "Inicio"),
    "reparacion-de-transmisiones.html": ("../transmission-repair.html", "Transmisiones"),
    "flotas-y-mayoreo.html": ("../fleet.html", "Flotas y Mayoreo"),
    "otros-servicios.html": ("../services.html", "Otros Servicios"),
    "contacto.html": ("../contact.html", "Contacto"),
}

def head(title, desc, canon, en_url, extra=""):
    return f"""<!DOCTYPE html>
<html lang="es">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{title}</title>
<meta name="description" content="{desc}">
<link rel="canonical" href="https://arevalosautorepair.com/es/{canon}">
<link rel="alternate" hreflang="es" href="https://arevalosautorepair.com/es/{canon}">
<link rel="alternate" hreflang="en" href="https://arevalosautorepair.com/{en_url}">
<link rel="alternate" hreflang="x-default" href="https://arevalosautorepair.com/{en_url}">
<link rel="icon" href="../assets/favicon.png" type="image/png">
<meta property="og:title" content="{title}">
<meta property="og:description" content="{desc}">
<meta property="og:locale" content="es_US">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Archivo:wght@600;700;800;900&family=IBM+Plex+Mono:wght@400;500;600&family=IBM+Plex+Sans:wght@400;500;600&display=swap" rel="stylesheet">
<link rel="stylesheet" href="../styles.css">
{extra}</head>
<body>
"""

def masthead(current, en_url):
    links = "".join(
        f'\n      <a href="{p}"{" aria-current=\"page\"" if p == current else ""}>{label}</a>'
        for p, (_, label) in PAGES.items())
    return f"""<header class="masthead">
  <div class="wrap masthead__bar">
    <a class="masthead__logo" href="index.html">
      <img src="../assets/logo-320.png" alt="Arevalo's Auto Repair">
      <span class="masthead__name">Arevalo's Auto Repair<span>Especialistas en Transmisiones · Irving, TX</span></span>
    </a>
    <button class="navtoggle" aria-expanded="false" aria-controls="nav">MENÚ</button>
    <nav class="nav" id="nav">{links}
      <a class="langswitch" href="{en_url}" hreflang="en" lang="en">English</a>
    </nav>
    <a class="masthead__call" href="tel:{TEL1}">214-718-8587</a>
  </div>
</header>
"""

FOOT = f"""<footer class="foot">
  <div class="wrap">
    <div class="foot__grid">
      <div>
        <img src="../assets/logo-320.png" alt="Arevalo's Auto Repair">
        <p>Reconstrucción de transmisiones para Ford, Chevy y Ram en Irving, Texas. Hecho aquí en el taller, con garantía y con el precio dado antes de empezar.</p>
      </div>
      <div>
        <h4>El taller</h4>
        <ul>
          <li>505 E Irving Blvd<br>Irving, TX 75060</li>
          <li><a href="tel:{TEL1}">214-718-8587</a></li>
          <li><a href="tel:{TEL2}">469-350-6499</a></li>
          <li><a href="mailto:{EMAIL}">{EMAIL}</a></li>
        </ul>
      </div>
      <div>
        <h4>Horario</h4>
        <ul>
          <li>Lunes a viernes · 8:00 AM – 6:00 PM</li>
          <li>Sábado · 9:00 AM – 4:00 PM</li>
          <li>Domingo · Cerrado</li>
        </ul>
      </div>
      <div>
        <h4>Páginas</h4>
        <ul>
          <li><a href="index.html">Inicio</a></li>
          <li><a href="reparacion-de-transmisiones.html">Transmisiones</a></li>
          <li><a href="flotas-y-mayoreo.html">Flotas y mayoreo</a></li>
          <li><a href="otros-servicios.html">Otros servicios</a></li>
          <li><a href="contacto.html">Contacto</a></li>
          <li><a href="https://www.facebook.com/arevalos.autorepair.3/" rel="noopener">Facebook</a></li>
        </ul>
      </div>
    </div>
    <div class="foot__legal">
      <span>© 2026 Arevalo's Auto Repair · Irving, TX</span>
      <span>Ford, Chevrolet y Ram son marcas de sus respectivos dueños. Somos un taller independiente.</span>
    </div>
  </div>
</footer>

<div class="callbar">
  <a class="is-primary" href="tel:{TEL1}">Llamar al taller</a>
  <a href="https://www.google.com/maps?q=505+E+Irving+Blvd,+Irving,+TX+75060">Cómo llegar</a>
</div>

<script src="../site.js"></script>
</body>
</html>
"""

GALLERY = """<section class="section gallery-section">
  <div class="wrap">
    <p class="eyebrow">Dentro del taller</p>
    <h2 style="font-size:clamp(28px,3.6vw,42px)">Trabajo real, en Irving Blvd.</h2>
    <div class="gallery">
      <img src="../assets/shop-1.jpg" alt="Taller Arevalo's Auto Repair en E Irving Blvd" loading="lazy">
      <img src="../assets/shop-2.jpg" alt="Camioneta en el elevador para sacar la transmisión" loading="lazy">
      <img src="../assets/shop-3.jpg" alt="Transmisión desarmada en la mesa de trabajo" loading="lazy">
      <img src="../assets/shop-4.jpg" alt="Transmisión reconstruida lista para instalar" loading="lazy">
      <img src="../assets/shop-5.jpg" alt="Técnico reconstruyendo una transmisión Ford" loading="lazy">
      <img src="../assets/shop-6.jpg" alt="Área de servicio de Arevalo's Auto Repair" loading="lazy">
    </div>
  </div>
</section>

"""

UNITS = [
 ("6R80", "Ford F-150, Expedition, Mustang"),
 ("10R80", "Ford F-150, Expedition, Ranger"),
 ("5R110W", "Ford Super Duty diésel"),
 ("6R140", "Ford F-250/F-350 Power Stroke"),
 ("4R70W / 4R75W", "Ford F-150, Crown Victoria"),
 ("6F35 / 6F50", "Ford Escape, Edge, Explorer"),
 ("4L60E", "Chevy Silverado, Tahoe, Camaro"),
 ("4L80E", "Chevy 2500/3500, Suburban"),
 ("6L80 / 6L90", "Chevy Silverado, Sierra, Tahoe"),
 ("8L90", "Chevy Silverado, GMC Sierra"),
 ("Allison 1000", "Chevy/GMC Duramax"),
 ("68RFE", "Ram 2500/3500 Cummins"),
 ("545RFE / 65RFE", "Ram 1500, Durango"),
 ("8HP70 / 850RE", "Ram 1500, Grand Cherokee"),
 ("46RE / 47RE", "Ram / Dodge más viejas"),
 ("¿No la ve?", "Llámenos — 214-718-8587"),
]

def units_html(items):
    return "".join(
        f'\n      <div class="unit"><div class="unit__code">{c}</div><div class="unit__fit">{f}</div></div>'
        for c, f in items)

BAND = """<section class="band">
  <div class="wrap">
    <h2>{h}</h2>
    <p>{p}</p>
    <div class="btn-row">
      <a class="btn btn--call" href="tel:{t}">Llame al 214-718-8587</a>
      <a class="btn btn--ghost" href="contacto.html">Mándenos los detalles</a>
    </div>
  </div>
</section>

"""

# ---------------------------------------------------------------- inicio
SCHEMA_ES = """<script type="application/ld+json">
{"@context":"https://schema.org","@type":"AutoRepair","name":"Arevalo's Auto Repair","url":"https://arevalosautorepair.com/es/","telephone":"+1-214-718-8587","email":"arevalostransmission@gmail.com","address":{"@type":"PostalAddress","streetAddress":"505 E Irving Blvd","addressLocality":"Irving","addressRegion":"TX","postalCode":"75060","addressCountry":"US"},"geo":{"@type":"GeoCoordinates","latitude":32.813906,"longitude":-96.94131},"availableLanguage":["es","en"]}
</script>
"""

inicio = head(
  "Reparación de Transmisiones en Irving, TX | Arevalo's Auto Repair",
  "Reconstrucción de transmisiones Ford, Chevy y Ram en Irving, TX. Diagnóstico gratis, grúa gratis hasta 15 millas, garantía de 6 meses. Desde $1,400. Llame al 214-718-8587. Hablamos español.",
  "index.html", "index.html", SCHEMA_ES)
inicio += masthead("index.html", "../index.html")
inicio += f"""
<section class="hero">
  <div class="wrap hero__grid">
    <div>
      <p class="eyebrow on-dark">505 E Irving Blvd · Irving, TX · Más de 20 años</p>
      <h1>Reconstrucción de transmisiones <em>Ford, Chevy y Ram</em>.</h1>
      <p class="hero__sub">Aquí en el taller la desarmamos y la reconstruimos nosotros — no le metemos una usada de yonke ni la mandamos a otro lado. Díganos qué está haciendo y se la revisamos gratis.</p>
      <div class="btn-row">
        <a class="btn btn--call" href="tel:{TEL1}">Llame al 214-718-8587</a>
        <a class="btn btn--ghost" href="contacto.html">Pedir presupuesto</a>
      </div>
    </div>

    <div class="ticket">
      <p class="ticket__head">Lo que incluye</p>
      <div class="ticket__row"><span class="ticket__k">Desde</span><span class="ticket__v">$1,400<small>Llame o escriba para su precio exacto</small></span></div>
      <div class="ticket__row"><span class="ticket__k">Garantía</span><span class="ticket__v">6 meses<small>Partes y mano de obra</small></span></div>
      <div class="ticket__row"><span class="ticket__k">Diagnóstico</span><span class="ticket__v">Gratis<small>Sin costo por revisar qué tiene</small></span></div>
      <div class="ticket__row"><span class="ticket__k">Grúa</span><span class="ticket__v">Gratis<small>Hasta 15 millas si hacemos el trabajo mayor</small></span></div>
      <a class="btn btn--call" href="tel:{TEL1}">Llamar al taller</a>
    </div>
  </div>
</section>

<section class="section section--dark">
  <div class="wrap">
    <p class="eyebrow on-dark">Transmisiones que reconstruimos</p>
    <h2 style="font-size:clamp(28px,3.6vw,42px)">Si está en una Ford, Chevy o Ram, ya la hemos abierto.</h2>
    <p class="lede" style="margin-top:16px">Estas son las más comunes. ¿Tiene otra? Llame y le decimos derecho si la podemos hacer.</p>
    <div class="units">{units_html(UNITS)}
    </div>
  </div>
</section>

<section class="section">
  <div class="wrap">
    <div class="split split--narrow">
      <div>
        <p class="eyebrow">Antes de seguir manejando</p>
        <h2 style="font-size:clamp(28px,3.6vw,42px)">Señas de que la transmisión ya va fallando</h2>
        <p class="lede" style="margin-top:16px">Seguir manejando con la transmisión patinando convierte una reconstrucción en un cambio completo. Si nota cualquiera de estas, llámenos.</p>
        <div class="btn-row"><a class="btn btn--call" href="tel:{TEL1}">Diagnóstico gratis — llame ahora</a></div>
      </div>
      <ul class="checklist">
        <li>Patina o se revoluciona entre cambios</li>
        <li>Cambia duro, golpea o tarda en entrar</li>
        <li>No camina en drive o en reversa</li>
        <li>Manchas de aceite rojo debajo</li>
        <li>Olor a quemado después de manejar</li>
        <li>Chillido, zumbido o rechinido</li>
        <li>Luz de check engine o de la llave</li>
        <li>Se va a modo de emergencia en carretera</li>
      </ul>
    </div>
  </div>
</section>

<section class="section section--tint">
  <div class="wrap">
    <p class="eyebrow">Cómo funciona</p>
    <h2 style="font-size:clamp(28px,3.6vw,42px)">De su casa a la carretera otra vez</h2>
    <div class="steps">
      <div class="step"><div><h3>Llámenos y díganos qué hace</h3><p>Año, marca, modelo y qué está sintiendo. Le damos un aproximado por teléfono antes de que gaste un peso. Si no camina, le mandamos la grúa.</p></div></div>
      <div class="step"><div><h3>Diagnóstico gratis</h3><p>Escaneamos códigos, revisamos aceite y presiones, y la probamos manejando si se puede. A veces es un solenoide o un sensor y no una reconstrucción — y así se lo decimos.</p></div></div>
      <div class="step"><div><h3>Presupuesto por escrito</h3><p>Usted ve el precio antes de que empecemos. Nada se hace hasta que usted diga que sí, y el número no cambia sin que le hablemos primero.</p></div></div>
      <div class="step"><div><h3>Reconstruida aquí mismo</h3><p>Se saca, se desarma, se lava y se revisa pieza por pieza. Clutches, retenes, bandas y partes duras gastadas se cambian. Luego se instala y se prueba en la calle.</p></div></div>
      <div class="step"><div><h3>Garantía de 6 meses</h3><p>Partes y mano de obra de la reconstrucción. Si algo no queda bien, tráigala de vuelta y lo vemos.</p></div></div>
    </div>
  </div>
</section>

<section class="section section--dark">
  <div class="wrap">
    <p class="eyebrow on-dark">Lo que dicen los clientes</p>
    <h2 style="font-size:clamp(28px,3.6vw,42px)">Veinte años de recomendaciones.</h2>
    <p class="lede" style="margin-top:16px">Comentarios de Google y Yelp. Léalos todos y deje el suyo en los enlaces de abajo.</p>

    <!-- RESEÑAS — VERIFICAR ANTES DE PUBLICAR. Confirme cada una contra su
         perfil de Google/Yelp y ponga el texto exacto del cliente con su
         nombre y fecha reales. -->
    <div class="quotes">
      <div class="quote">
        <p>Llevaron una Ford Transit 2021 de una compañía de construcción. La grúa llegó de Arlington en menos de una hora y la camioneta salió rápido.</p>
        <cite>Reseña de Google · Dueño de camioneta de trabajo</cite>
      </div>
      <div class="quote">
        <p>Otro taller de Irving pedía mucho más dinero y hasta diez semanas por partes. Aquí costó menos, quedó en una semana y la camioneta camina suave.</p>
        <cite>Reseña de Google · Dueño de camioneta de trabajo</cite>
      </div>
      <div class="quote">
        <p>Muy amables y buen trabajo. Es un negocio familiar y eso lo respeto.</p>
        <cite>Hamid N. · Yelp · Marzo 2025</cite>
      </div>
    </div>

    <div class="btn-row" style="margin-top:30px">
      <a class="btn btn--call" href="REPLACE_WITH_GOOGLE_REVIEW_LINK">Deje su reseña en Google</a>
      <a class="btn btn--ghost" href="https://www.yelp.com/biz/arevalos-auto-repair-irving">Ver reseñas en Yelp</a>
    </div>

    <div class="stats">
      <div class="stat"><div class="stat__n">20+</div><div class="stat__l">Años en el negocio</div></div>
      <div class="stat"><div class="stat__n">$1,400</div><div class="stat__l">Desde</div></div>
      <div class="stat"><div class="stat__n">6 meses</div><div class="stat__l">Garantía</div></div>
      <div class="stat"><div class="stat__n">15 mi</div><div class="stat__l">Grúa gratis</div></div>
    </div>
  </div>
</section>

""" + GALLERY + f"""<section class="section">
  <div class="wrap">
    <div class="split">
      <div>
        <p class="eyebrow">Dónde estamos</p>
        <h2 style="font-size:clamp(28px,3.6vw,42px)">Un solo taller. Irving Blvd.</h2>
        <p class="lede" style="margin-top:16px">Atendemos Irving, Las Colinas, Dallas, Grand Prairie, Farmers Branch, Coppell, Arlington y todo el área.</p>
        <ul class="infolist" style="margin-top:24px">
          <li><strong>Dirección</strong>505 E Irving Blvd, Irving, TX 75060</li>
          <li><strong>Teléfono</strong><a href="tel:{TEL1}">214-718-8587</a> · <a href="tel:{TEL2}">469-350-6499</a></li>
          <li><strong>Correo</strong><a href="mailto:{EMAIL}">{EMAIL}</a></li>
          <li><strong>Horario</strong>Lunes a viernes 8:00 AM – 6:00 PM<br>Sábado 9:00 AM – 4:00 PM<br>Domingo cerrado</li>
        </ul>
      </div>
      <div class="map">
        <iframe title="Mapa a Arevalo's Auto Repair, 505 E Irving Blvd, Irving, TX 75060"
          src="https://www.google.com/maps?q=505+E+Irving+Blvd,+Irving,+TX+75060&output=embed"
          loading="lazy" referrerpolicy="no-referrer-when-downgrade"></iframe>
      </div>
    </div>
  </div>
</section>

""" + BAND.format(h="¿No sabe si es la transmisión?", p="El diagnóstico es gratis. Llámenos, díganos qué está haciendo y le decimos qué tiene antes de que gaste nada.", t=TEL1) + FOOT
(OUT/"index.html").write_text(inicio)

# ------------------------------------------------- transmisiones (money page)
FORD = [("6R80","F-150, Expedition, Mustang"),("10R80","F-150, Expedition, Ranger"),
        ("5R110W","Super Duty diésel"),("6R140","F-250/F-350 Power Stroke"),
        ("4R70W / 4R75W","F-150, Crown Victoria"),("6F35 / 6F50","Escape, Edge, Explorer"),
        ("5R55S / 5R55W","Explorer, Mustang, Ranger"),("Transit / E-Series","Vans de trabajo")]
CHEVY = [("4L60E / 4L65E","Silverado, Tahoe, Camaro"),("4L80E / 4L85E","2500/3500, Suburban"),
         ("6L80 / 6L90","Silverado, Sierra, Tahoe"),("8L90 / 8L45","Silverado, Sierra, Colorado"),
         ("Allison 1000","Duramax 2500/3500"),("6T70 / 6T75","Equinox, Traverse, Malibu")]
RAM = [("68RFE","2500/3500 Cummins"),("545RFE / 65RFE","Ram 1500, Durango"),
       ("8HP70 / 850RE","Ram 1500, Grand Cherokee"),("46RE / 47RE / 48RE","Ram más viejas"),
       ("Aisin AS69RC","Ram 3500/4500/5500"),("¿No la ve?","Llámenos — 214-718-8587")]
sub = 'font-size:19px;margin-top:44px;font-family:var(--mono);font-weight:500;letter-spacing:.12em;text-transform:uppercase;color:var(--amber)'

FAQ_ES = """<script type="application/ld+json">
{"@context":"https://schema.org","@type":"FAQPage","inLanguage":"es","mainEntity":[
{"@type":"Question","name":"¿Cuánto cuesta reconstruir una transmisión?","acceptedAnswer":{"@type":"Answer","text":"Desde $1,400. El precio final depende de la transmisión, el vehículo y lo que encontremos al desarmarla. Llame con año, marca y modelo."}},
{"@type":"Question","name":"¿El diagnóstico es gratis?","acceptedAnswer":{"@type":"Answer","text":"Sí. Escaneamos códigos, revisamos aceite y presiones y la probamos manejando sin costo."}},
{"@type":"Question","name":"¿Tienen grúa?","acceptedAnswer":{"@type":"Answer","text":"La grúa es gratis hasta 15 millas del taller cuando hacemos el trabajo mayor."}},
{"@type":"Question","name":"¿Qué garantía dan?","acceptedAnswer":{"@type":"Answer","text":"Seis meses en partes y mano de obra de la reconstrucción."}},
{"@type":"Question","name":"¿Hablan español?","acceptedAnswer":{"@type":"Answer","text":"Sí. Todo el taller habla español."}}]}
</script>
"""

trans = head("Reparación de Transmisiones Irving TX — Ford, Chevy y Ram | Arevalo's",
  "Reconstrucción de transmisiones en Irving, TX para Ford, Chevy y Ram. 6R80, 10R80, 4L60E, 6L80, 68RFE y más. Diagnóstico gratis, garantía de 6 meses, desde $1,400.",
  "reparacion-de-transmisiones.html", "transmission-repair.html", FAQ_ES)
trans += masthead("reparacion-de-transmisiones.html", "../transmission-repair.html")
trans += f"""
<section class="pagehead">
  <div class="wrap">
    <p class="eyebrow on-dark">Transmisiones · Irving, TX</p>
    <h1>Reconstrucción de transmisiones Ford, Chevy y Ram</h1>
    <p>Reconstruidas aquí en Irving, con precio antes de empezar y garantía de seis meses. Diagnóstico gratis y grúa gratis hasta 15 millas cuando hacemos el trabajo mayor.</p>
    <div class="btn-row">
      <a class="btn btn--call" href="tel:{TEL1}">Llame al 214-718-8587</a>
      <a class="btn btn--ghost" href="contacto.html">Pedir presupuesto</a>
    </div>
  </div>
</section>

<section class="section">
  <div class="wrap">
    <div class="split split--narrow">
      <div><p class="eyebrow">Reconstruir o cambiar</p><h2 style="font-size:clamp(28px,3.6vw,42px)">Qué significa reconstruir</h2></div>
      <div>
        <p class="lede">Muchos talleres cotizan un "trabajo de transmisión" y lo que hacen es meterle una usada sacada de una camioneta chocada. Está comprando el desgaste de otra persona sin saber cuántas millas trae.</p>
        <p style="margin-top:16px">Reconstruir es otra cosa. Sacamos su transmisión, la desarmamos completa y revisamos cada pieza. Clutches, retenes, empaques, bandas, filtro y las partes duras gastadas se cambian. Se arma a especificación, se instala y se prueba manejando antes de entregarle las llaves.</p>
        <p>Cuesta más que meterle una de yonke y dura mucho más. Ese es todo el trato.</p>
      </div>
    </div>
  </div>
</section>

<section class="section section--dark">
  <div class="wrap">
    <p class="eyebrow on-dark">Cobertura</p>
    <h2 style="font-size:clamp(28px,3.6vw,42px)">Transmisiones que reconstruimos</h2>
    <p class="lede" style="margin-top:16px">Ford, Chevy y Ram es lo nuestro. Si no ve la suya, llame y pregunte.</p>
    <h3 style="{sub}">Ford</h3>
    <div class="units" style="margin-top:14px">{units_html(FORD)}
    </div>
    <h3 style="{sub}">Chevrolet y GMC</h3>
    <div class="units" style="margin-top:14px">{units_html(CHEVY)}
    </div>
    <h3 style="{sub}">Ram y Dodge</h3>
    <div class="units" style="margin-top:14px">{units_html(RAM)}
    </div>
  </div>
</section>

<section class="section section--tint">
  <div class="wrap">
    <div class="split split--narrow">
      <div>
        <p class="eyebrow">Síntomas</p>
        <h2 style="font-size:clamp(28px,3.6vw,42px)">Tráigala antes de que lo deje tirado</h2>
        <p class="lede" style="margin-top:16px">Casi todas avisan por semanas antes de fallar. Agarrada a tiempo, muchas veces es un solenoide, un sensor o el aceite, y no una reconstrucción completa.</p>
        <div class="btn-row"><a class="btn btn--call" href="tel:{TEL1}">Diagnóstico gratis — llame</a></div>
      </div>
      <ul class="checklist">
        <li>Patina o se revoluciona entre cambios</li>
        <li>Cambia duro, golpea o tarda</li>
        <li>No camina en drive ni en reversa</li>
        <li>Aceite rojo en la cochera</li>
        <li>Olor a quemado</li>
        <li>Chillido, zumbido o rechinido</li>
        <li>Vibra en carretera</li>
        <li>Se queda en una sola velocidad</li>
        <li>Luz de check engine o de la llave</li>
        <li>Parpadea el indicador de velocidades</li>
      </ul>
    </div>
  </div>
</section>

<section class="section section--dark">
  <div class="wrap">
    <div class="split">
      <div>
        <p class="eyebrow on-dark">Precios</p>
        <h2 style="font-size:clamp(28px,3.6vw,42px)">Desde $1,400</h2>
        <p class="lede" style="margin-top:16px">Dónde cae su trabajo depende de la transmisión, del vehículo y de lo que salga al desarmarla. Una 4L60E de media tonelada no es el mismo trabajo que una Allison atrás de un Duramax, y no le vamos a decir que sí lo es.</p>
        <p style="color:var(--chrome);margin-top:16px">Llame o escriba con año, marca, modelo y qué está haciendo, y le damos un número real.</p>
        <div class="btn-row">
          <a class="btn btn--call" href="tel:{TEL1}">Llame al 214-718-8587</a>
          <a class="btn btn--ghost" href="contacto.html">Pedir por correo</a>
        </div>
      </div>
      <div class="ticket">
        <p class="ticket__head">Las condiciones, claras</p>
        <div class="ticket__row"><span class="ticket__k">Desde</span><span class="ticket__v">$1,400</span></div>
        <div class="ticket__row"><span class="ticket__k">Diagnóstico</span><span class="ticket__v">Gratis</span></div>
        <div class="ticket__row"><span class="ticket__k">Garantía</span><span class="ticket__v">6 meses<small>Partes y mano de obra</small></span></div>
        <div class="ticket__row"><span class="ticket__k">Grúa</span><span class="ticket__v">Gratis<small>Hasta 15 millas con trabajo mayor</small></span></div>
        <div class="ticket__row"><span class="ticket__k">Presupuesto</span><span class="ticket__v">Antes de empezar<small>Usted lo aprueba</small></span></div>
      </div>
    </div>
  </div>
</section>

<section class="section">
  <div class="wrap" style="max-width:900px">
    <p class="eyebrow">Preguntas</p>
    <h2 style="font-size:clamp(28px,3.6vw,42px)">Respuestas derechas</h2>
    <div class="faq">
      <details open><summary>¿Cuánto cuesta reconstruir una transmisión?</summary><p>Desde $1,400. El número final depende de la transmisión, del vehículo y de lo que encontremos al abrirla. Llame o escriba con año, marca y modelo.</p></details>
      <details><summary>¿De veras es gratis el diagnóstico?</summary><p>Sí. Escaneamos códigos, revisamos aceite y presiones y la probamos manejando si camina, sin ningún costo.</p></details>
      <details><summary>¿Cuánto se tarda?</summary><p>Depende de la transmisión y de las partes. Le damos un tiempo realista al darle el presupuesto. Si es camioneta de trabajo, díganos y lo tomamos en cuenta.</p></details>
      <details><summary>¿Tienen grúa?</summary><p>Gratis hasta 15 millas del taller cuando hacemos el trabajo mayor. Más lejos, llame y lo arreglamos.</p></details>
      <details><summary>¿Qué cubre la garantía?</summary><p>Seis meses en partes y mano de obra de la reconstrucción que hicimos nosotros. Tráigala de vuelta y lo vemos.</p></details>
      <details><summary>¿Reconstruyen o ponen usadas?</summary><p>Reconstruimos aquí. Su transmisión se saca, se desarma, se lava, se revisa y se arma con partes nuevas de desgaste. No le vamos a poner una de yonke.</p></details>
      <details><summary>¿Trabajan otras marcas?</summary><p>Ford, Chevy y Ram es donde tenemos más experiencia, pero vemos otras caso por caso. Llame y le decimos con honestidad si es trabajo para nosotros.</p></details>
      <details><summary>¿Hablan español?</summary><p>Sí, todo el taller. Llame con confianza.</p></details>
    </div>
  </div>
</section>

""" + BAND.format(h="Díganos qué está haciendo.", p="Diagnóstico gratis, precio antes de empezar y garantía de seis meses. 505 E Irving Blvd, Irving.", t=TEL1) + FOOT
(OUT/"reparacion-de-transmisiones.html").write_text(trans)

# ----------------------------------------------------------- flotas y mayoreo
flotas = head("Transmisiones al Mayoreo y para Flotas | Arevalo's Auto Repair, Irving TX",
  "Reconstrucción de transmisiones al mayoreo para talleres, lotes de carros usados y flotas en Irving y Dallas. Precio de mayoreo, garantía de 6 meses, grúa gratis 15 millas.",
  "flotas-y-mayoreo.html", "fleet.html")
flotas += masthead("flotas-y-mayoreo.html", "../fleet.html")
flotas += f"""
<section class="pagehead">
  <div class="wrap">
    <p class="eyebrow on-dark">Para talleres, lotes y flotas</p>
    <h1>Mándenos la transmisión. Quédese con el cliente.</h1>
    <p>Si tiene un taller, un lote de carros usados o una flota de camionetas de trabajo, no tiene que rechazar los trabajos de transmisión ni mandarlos al otro lado de la ciudad. Reconstruimos Ford, Chevy y Ram aquí en 505 E Irving Blvd, con precio de mayoreo.</p>
    <div class="btn-row">
      <a class="btn btn--call" href="tel:{TEL1}">Llame al 214-718-8587</a>
      <a class="btn btn--ghost" href="#mayoreo">Pedir precios de mayoreo</a>
    </div>
  </div>
</section>

<section class="section">
  <div class="wrap">
    <p class="eyebrow">Con quién trabajamos</p>
    <h2 style="font-size:clamp(28px,3.6vw,42px)">Cuatro tipos de cuenta</h2>
    <div class="cards">
      <div class="card"><p class="card__tag">Talleres</p><h3>No rechace el trabajo</h3><p>La mayoría de los talleres generales no quieren abrir una transmisión — la herramienta, el tiempo en la mesa y el riesgo de que regrese no valen la pena. Mándenosla, póngale su ganancia y quédese con el cliente y con la mano de obra de sacarla y ponerla.</p></div>
      <div class="card"><p class="card__tag">Lotes de carros</p><h3>Arregle el trade-in</h3><p>Una transmisión patinando convierte un carro listo para vender en carro de subasta. Se lo cotizamos rápido para que decida si lo arregla o lo suelta, y se lo entregamos pronto para que no esté parado en el lote.</p></div>
      <div class="card"><p class="card__tag">Flotas y contratistas</p><h3>Las de trabajo van primero</h3><p>Jardinería, plomería, aire acondicionado, entregas, construcción — una camioneta en el elevador no está ganando. Díganos que es de trabajo y le decimos con honestidad qué tan rápido la sacamos y cuánto cuesta.</p></div>
      <div class="card"><p class="card__tag">Grúas</p><h3>Un taller a dónde mandarlos</h3><p>Usted ya está en el lugar donde se quedó tirado. Si es la transmisión, tráigalo y le atendemos bien a su cliente.</p></div>
    </div>
  </div>
</section>

<section class="section section--dark">
  <div class="wrap">
    <div class="split">
      <div>
        <p class="eyebrow on-dark">Las condiciones</p>
        <h2 style="font-size:clamp(28px,3.6vw,42px)">Qué incluye una cuenta de mayoreo</h2>
        <p class="lede" style="margin-top:16px">Sin contrato y sin mínimo. Mándenos un trabajo y vea cómo sale.</p>
        <div class="btn-row"><a class="btn btn--call" href="tel:{TEL1}">Llame y lo arreglamos</a></div>
      </div>
      <div class="ticket">
        <p class="ticket__head">Mayoreo</p>
        <div class="ticket__row"><span class="ticket__k">Precio</span><span class="ticket__v">De mayoreo<small>Llame por la lista actual</small></span></div>
        <div class="ticket__row"><span class="ticket__k">Diagnóstico</span><span class="ticket__v">Gratis<small>Cotizado antes de empezar</small></span></div>
        <div class="ticket__row"><span class="ticket__k">Garantía</span><span class="ticket__v">6 meses<small>Partes y mano de obra</small></span></div>
        <div class="ticket__row"><span class="ticket__k">Grúa</span><span class="ticket__v">Gratis<small>Hasta 15 millas con trabajo mayor</small></span></div>
        <div class="ticket__row"><span class="ticket__k">Solo la unidad</span><span class="ticket__v">Sí<small>Sáquela usted y mándenosla</small></span></div>
      </div>
    </div>
  </div>
</section>

<section class="section section--tint">
  <div class="wrap">
    <p class="eyebrow">Cómo mandarnos trabajo</p>
    <h2 style="font-size:clamp(28px,3.6vw,42px)">Tres maneras</h2>
    <div class="steps">
      <div class="step"><div><h3>Mándenos el vehículo completo</h3><p>Nosotros la sacamos, la reconstruimos, la instalamos y la probamos. Se la regresamos lista para entregarle a su cliente.</p></div></div>
      <div class="step"><div><h3>Mándenos solo la unidad</h3><p>Usted la saca, nosotros la reconstruimos en la mesa y se la regresamos para que la instale. Así se queda con esa mano de obra.</p></div></div>
      <div class="step"><div><h3>Mándenos al cliente</h3><p>Recomiéndenos directo. Lo atendemos bien y va a saber quién lo mandó.</p></div></div>
    </div>
  </div>
</section>

<section class="section" id="mayoreo">
  <div class="wrap">
    <div class="split">
      <div>
        <p class="eyebrow">Abrir cuenta</p>
        <h2 style="font-size:clamp(28px,3.6vw,42px)">Pedir precios de mayoreo</h2>
        <p class="lede" style="margin-top:16px">Mándenos esto y le pasamos precios de mayoreo de las transmisiones que más ve. O nomás llame al taller — es más rápido.</p>
        <ul class="infolist" style="margin-top:24px">
          <li><strong>Teléfono</strong><a href="tel:{TEL1}">214-718-8587</a> · <a href="tel:{TEL2}">469-350-6499</a></li>
          <li><strong>Correo</strong><a href="mailto:{EMAIL}">{EMAIL}</a></li>
          <li><strong>Taller</strong>505 E Irving Blvd, Irving, TX 75060</li>
          <li><strong>Horario</strong>Lun–Vie 8–6 · Sáb 9–4</li>
        </ul>
      </div>
      <form class="form" action="https://formspree.io/f/YOUR_FORM_ID" method="POST">
        <input type="hidden" name="_language" value="es">
        <div class="field"><label for="w-biz">Nombre del negocio</label><input id="w-biz" name="business" type="text" required></div>
        <div class="field"><label for="w-name">Su nombre</label><input id="w-name" name="name" type="text" required></div>
        <div class="field"><label for="w-phone">Teléfono</label><input id="w-phone" name="phone" type="tel" required></div>
        <div class="field"><label for="w-email">Correo</label><input id="w-email" name="email" type="email" required></div>
        <div class="field"><label for="w-type">Tipo de negocio</label>
          <select id="w-type" name="business_type"><option>Taller</option><option>Lote de carros usados</option><option>Flota / contratista</option><option>Grúa</option><option>Otro</option></select></div>
        <div class="field"><label for="w-note">Qué transmisiones ve más, o un trabajo que tenga ahorita</label>
          <textarea id="w-note" name="message" placeholder="Casi todo 6L80 y 68RFE — tengo una Silverado 2016 en el elevador"></textarea></div>
        <button class="btn btn--call" type="submit">Enviar</button>
      </form>
    </div>
  </div>
</section>

""" + BAND.format(h="¿Tiene un trabajo de transmisión parado en su lote?", p="Llame al taller y se lo cotizamos hoy. 505 E Irving Blvd, Irving.", t=TEL1) + FOOT
(OUT/"flotas-y-mayoreo.html").write_text(flotas)

# --------------------------------------------------------- otros servicios
otros = head("Otros Servicios de Taller en Irving, TX | Arevalo's Auto Repair",
  "Además de transmisiones: frenos, aire acondicionado, diagnóstico eléctrico, afinaciones y mecánica general en Irving, TX. Más de 20 años. Llame al 214-718-8587.",
  "otros-servicios.html", "services.html")
otros += masthead("otros-servicios.html", "../services.html")
otros += f"""
<section class="pagehead">
  <div class="wrap">
    <p class="eyebrow on-dark">Más allá de las transmisiones</p>
    <h1>Somos taller de transmisiones primero. Seguimos siendo taller.</h1>
    <p>Las transmisiones son lo nuestro y de ahí viene la mayoría del trabajo. Pero llevamos más de 20 años con taller completo aquí en Irving Blvd, y si su camioneta necesita otra cosa mientras está aquí, se la vemos.</p>
    <div class="btn-row">
      <a class="btn btn--call" href="tel:{TEL1}">Llame al 214-718-8587</a>
      <a class="btn btn--ghost" href="reparacion-de-transmisiones.html">Ver transmisiones</a>
    </div>
  </div>
</section>

<section class="section">
  <div class="wrap">
    <p class="eyebrow">También en el taller</p>
    <h2 style="font-size:clamp(28px,3.6vw,42px)">Mecánica general y mantenimiento</h2>
    <div class="cards">
      <div class="card"><h3>Frenos</h3><p>Balatas, discos, caliper, mangueras e hidráulico. Si oye rechinido o siente el pedal blando, no lo deje pasar.</p></div>
      <div class="card"><h3>Aire acondicionado</h3><p>Diagnóstico, carga, compresor y componentes. Con el calor de Texas no hay mucho margen para dejarlo.</p></div>
      <div class="card"><h3>Diagnóstico eléctrico</h3><p>Check engine, que no arranca, problemas de carga, sensores y cableado. Buscamos la falla en vez de andar cambiando partes.</p></div>
      <div class="card"><h3>Afinaciones y mantenimiento</h3><p>Bujías, bobinas, filtros, aceites y servicio programado. La manera más barata de cuidar una transmisión es cuidar el resto del vehículo.</p></div>
      <div class="card"><h3>Servicio de transmisión</h3><p>Cambio de aceite y filtro en una transmisión sana. No arregla una que ya patina, pero evita que una buena termine en reconstrucción.</p></div>
      <div class="card"><h3>¿Otra cosa?</h3><p>Llame y díganos. Si no es trabajo que hagamos, se lo decimos en vez de hacerle perder el tiempo.</p><a class="card__link" href="tel:{TEL1}">Llame al 214-718-8587 →</a></div>
    </div>
  </div>
</section>

<section class="section section--dark">
  <div class="wrap">
    <div class="split">
      <div>
        <p class="eyebrow on-dark">Sobre el taller</p>
        <h2 style="font-size:clamp(28px,3.6vw,42px)">Más de 20 años en Irving Blvd</h2>
        <p class="lede" style="margin-top:16px">Arevalo's Auto Repair es un taller familiar e independiente en Irving, Texas. Llevamos dos décadas creciendo por recomendación, y eso solo funciona si cotiza uno con honestidad, hace bien el trabajo y responde por él.</p>
        <p style="color:var(--chrome);margin-top:16px">Con los años el trabajo se fue concentrando en transmisiones — sobre todo camionetas Ford, Chevy y Ram — porque es el trabajo que otros talleres mandan a otro lado y en el que nosotros nos hicimos buenos. Las reconstruimos aquí, damos el precio antes de empezar y respondemos seis meses por lo que armamos.</p>
        <div class="btn-row">
          <a class="btn btn--call" href="tel:{TEL1}">Llamar al taller</a>
          <a class="btn btn--ghost" href="contacto.html">Cómo llegar y horario</a>
        </div>
      </div>
      <div class="ticket">
        <p class="ticket__head">El taller</p>
        <div class="ticket__row"><span class="ticket__k">Dirección</span><span class="ticket__v" style="font-size:17px">505 E Irving Blvd<small>Irving, TX 75060</small></span></div>
        <div class="ticket__row"><span class="ticket__k">Especialidad</span><span class="ticket__v" style="font-size:17px">Transmisiones<small>Ford · Chevy · Ram</small></span></div>
        <div class="ticket__row"><span class="ticket__k">Experiencia</span><span class="ticket__v">20+ años</span></div>
        <div class="ticket__row"><span class="ticket__k">Sucursales</span><span class="ticket__v">Una<small>Todo se hace aquí</small></span></div>
        <a class="btn btn--call" href="tel:{TEL1}">214-718-8587</a>
      </div>
    </div>
  </div>
</section>

""" + BAND.format(h="Un taller, un teléfono.", p="Transmisión o lo que sea — llame y díganos qué está haciendo.", t=TEL1) + FOOT
(OUT/"otros-servicios.html").write_text(otros)

# ------------------------------------------------------------------ contacto
contacto = head("Contacto y Presupuesto Gratis | Arevalo's Auto Repair, Irving TX",
  "Llame al 214-718-8587 o mándenos año, marca, modelo y los síntomas para un presupuesto gratis. 505 E Irving Blvd, Irving, TX 75060. Lun–Vie 8–6, Sáb 9–4. Hablamos español.",
  "contacto.html", "contact.html")
contacto += masthead("contacto.html", "../contact.html")
contacto += f"""
<section class="pagehead">
  <div class="wrap">
    <p class="eyebrow on-dark">Presupuesto gratis · Diagnóstico gratis</p>
    <h1>Díganos qué está haciendo</h1>
    <p>Llamar es lo más rápido — casi siempre le damos un aproximado por teléfono. Si ya cerramos, mándenos el formulario con año, marca, modelo y los síntomas y le hablamos.</p>
    <div class="btn-row">
      <a class="btn btn--call" href="tel:{TEL1}">Llame al 214-718-8587</a>
      <a class="btn btn--ghost" href="https://www.google.com/maps?q=505+E+Irving+Blvd,+Irving,+TX+75060">Cómo llegar</a>
    </div>
  </div>
</section>

<section class="section">
  <div class="wrap">
    <div class="split">
      <div>
        <p class="eyebrow">Pedir presupuesto</p>
        <h2 style="font-size:clamp(28px,3.6vw,42px)">Mándenos los detalles</h2>
        <p class="lede" style="margin-top:16px;margin-bottom:26px">Entre más nos diga, más cercano sale el estimado. Si no camina, avísenos — la grúa es gratis hasta 15 millas cuando hacemos el trabajo mayor.</p>
        <form class="form" action="https://formspree.io/f/YOUR_FORM_ID" method="POST">
          <input type="hidden" name="_language" value="es">
          <div class="field"><label for="c-name">Nombre</label><input id="c-name" name="name" type="text" required></div>
          <div class="field"><label for="c-phone">Teléfono</label><input id="c-phone" name="phone" type="tel" required></div>
          <div class="field"><label for="c-email">Correo</label><input id="c-email" name="email" type="email"></div>
          <div class="field"><label for="c-vehicle">Año, marca y modelo</label><input id="c-vehicle" name="vehicle" type="text" placeholder="Ford F-150 2015, motor 5.0" required></div>
          <div class="field"><label for="c-drivable">¿Todavía camina?</label>
            <select id="c-drivable" name="drivable"><option>Sí, todavía camina</option><option>Apenas / no es seguro manejarla</option><option>No, no se mueve</option></select></div>
          <div class="field"><label for="c-symptoms">¿Qué está haciendo?</label>
            <textarea id="c-symptoms" name="symptoms" placeholder="Patina al entrar a tercera, prendió el check engine, empezó hace dos semanas" required></textarea></div>
          <button class="btn btn--call" type="submit">Enviar</button>
        </form>
      </div>
      <div>
        <ul class="infolist">
          <li><strong>Teléfono</strong><a href="tel:{TEL1}" style="font-size:22px;font-family:var(--display);font-weight:800">214-718-8587</a><br><a href="tel:{TEL2}" style="font-size:22px;font-family:var(--display);font-weight:800">469-350-6499</a></li>
          <li><strong>Correo</strong><a href="mailto:{EMAIL}">{EMAIL}</a></li>
          <li><strong>Dirección</strong>505 E Irving Blvd<br>Irving, TX 75060</li>
          <li><strong>Horario</strong>Lunes a viernes · 8:00 AM – 6:00 PM<br>Sábado · 9:00 AM – 4:00 PM<br>Domingo · Cerrado</li>
          <li><strong>Atendemos</strong>Irving, Las Colinas, Dallas, Grand Prairie, Farmers Branch, Coppell, Arlington y todo el área</li>
        </ul>
        <div class="map" style="margin-top:24px">
          <iframe title="Mapa a Arevalo's Auto Repair, 505 E Irving Blvd, Irving, TX 75060"
            src="https://www.google.com/maps?q=505+E+Irving+Blvd,+Irving,+TX+75060&output=embed"
            loading="lazy" referrerpolicy="no-referrer-when-downgrade"></iframe>
        </div>
      </div>
    </div>
  </div>
</section>

""" + BAND.format(h="¿Se quedó tirado?", p="Llame al taller. Grúa gratis hasta 15 millas cuando hacemos el trabajo mayor.", t=TEL1) + FOOT
(OUT/"contacto.html").write_text(contacto)

print("wrote", len(list(OUT.glob("*.html"))), "Spanish pages")
