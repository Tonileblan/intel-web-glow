# Control 61 — nueva web moderna con asistente IA (ES/EN)

Rediseño completo de control61.es manteniendo el logo y los colores de marca (rojo corporativo sobre negro/blanco), con copy reescrito a partir del contenido actual y un chat con IA que responde dudas de los visitantes usando el contenido real de la empresa.

## Lo que ya he extraído de la web actual

- **Posicionamiento y claims**: "Expertos en tranquilidad", "Más de 20 años de experiencia en seguridad y aplicación de la ley", "Sin trucos ni contratos a largo plazo", "Soluciones honestas y personalizadas".
- **Cifras**: +2.500 clientes, +20 años de experiencia, +5.000 proyectos terminados.
- **Servicios**: seguridad para empresas, seguridad para hogar/particulares, CCTV y videovigilancia, nueva construcción/obra, alarmas robo e incendio, control de acceso, monitorización remota 24h.
- **Contacto**: info@control61.es · 968 62 29 84 (24h) · Pol. Ind. La Polvorista, C/ Caravaca de la Cruz 13, Nave C-7, 30500 Molina de Segura (Murcia).
- **Razón social legal**: Desarrollos y Sistemas Inteligentes S.L.
- **Marca**: logo "Logo-Limpio.png" y paleta con rojo corporativo (#f50303 / #cc0000 / #e20000), negros y grises, azul oscuro puntual (#213b60 / #011627).
- **Clientes**: carrusel con ~45 logos de clientes.
- **Legales existentes**: Política de Privacidad (con mención a Mailchimp) y aviso de cookies.

**Acreditaciones y certificados encontrados** (todas las páginas los muestran solo como imágenes escaneadas, sin texto indexable):

- ISO 9001 (calidad), ISO 14001 (medio ambiente) e ISO 45001 (seguridad y salud laboral), certificadas por **RINA** (miembro de la Federación CISQ, red IQNet).
- Certificado de Empresa Acreditada **REA** (Registro de Empresas Acreditadas, Ministerio de Trabajo), para trabajos en el sector de la construcción.
- Registro en Industria (instalador de PCI, protección contra incendios).
- Registro en Seguridad Privada (Ministerio del Interior).

Estos cuatro bloques son el mayor activo comercial infrautilizado de la web actual: hoy están escondidos en páginas sueltas con un JPG. En la nueva web pasan a ser un módulo de confianza con sello vectorizado (RINA/CISQ/IQNet, REA, Industria, Seguridad Privada), alcance, entidad emisora, número y vigencia en texto real (indexable por Google y consultable por el asistente IA), más el escaneo original ampliable y descargable. Extraeré los números y fechas de los escaneos por reconocimiento de texto y te los pasaré para que el cliente los valide antes de publicarlos; lo que no se lea con certeza queda pendiente de confirmación en lugar de inventarse.

Un hueco que hay que cerrar con el cliente:

- **Textos legales completos**: la web actual tiene Política de Privacidad y aviso de cookies; faltan Aviso Legal con datos fiscales (CIF, registro mercantil) y una política de cookies separada. Necesito el CIF y los datos registrales para dejarlos correctos.

## Estructura de la nueva web

- **Inicio**: hero con propuesta de valor, prueba social (cifras + logos de clientes), 3 bloques de servicios, "la diferencia Control 61", CTA de valoración gratuita, asistente IA accesible.
- **Empresas**: sistemas completos, alarmas robo/incendio, control de acceso, CCTV, monitorización.
- **Particulares / Hogar**.
- **CCTV y videovigilancia**: incluyendo búsqueda inteligente de vídeo.
- **Obra nueva y renovaciones**.
- **Nosotros**: 20+ años, equipo con experiencia en aplicación de la ley, cifras, filosofía sin contratos abusivos.
- **Acreditaciones y certificaciones**: ISO 9001 / 14001 / 45001, Empresa Acreditada REA, Registro en Industria (PCI) y Registro en Seguridad Privada, cada uno explicado en clave de beneficio para el cliente, con número, alcance, emisor y descarga del documento. Los sellos también aparecen como prueba de confianza en inicio, páginas de empresas y footer, y el asistente IA puede citarlos.
- **Contacto**: formulario de valoración gratuita, teléfono 24h, email, mapa, horario.
- **Legales**: Aviso Legal, Política de Privacidad, Política de Cookies + banner de cookies.

Todo en español e inglés, con selector de idioma y URLs separadas por idioma (`/` y `/en/...`) para que ambas versiones posicionen.

## Experiencia con IA

Asistente de chat flotante, disponible en todas las páginas:

- Responde en el idioma del visitante sobre servicios, tecnologías, zonas de actuación y proceso de instalación, usando exclusivamente la información real de Control 61 (base de conocimiento redactada a partir del contenido extraído).
- No inventa precios: cuando la pregunta requiere presupuesto, recoge datos y propone la valoración gratuita.
- Puede derivar a WhatsApp/teléfono 24h en casos urgentes.
- Deja registro de la conversación y de los contactos generados para que el cliente los vea.

## Diseño

- Se mantiene el logo actual y el rojo corporativo como acento único sobre una base oscura sobria, con tipografía moderna de alto contraste, mucho aire y microanimaciones al hacer scroll. Nada de plantilla WordPress genérica: retícula clara, fotografía a sangre y bloques de confianza.
- Mobile first, accesible (contraste AA), carga rápida.

## SEO

- Títulos y descripciones propios por página orientados a "sistemas de seguridad Murcia", "alarmas empresas Molina de Segura", "CCTV videovigilancia Murcia".
- Un solo H1 por página, HTML semántico, alt en imágenes, datos estructurados de negocio local (LocalBusiness/SecuritySystemInstaller) con dirección y teléfono, canónicas y hreflang ES/EN.

## Detalles técnicos

- TanStack Start + React con rutas por página e idioma; sistema de diseño en `src/styles.css` con tokens semánticos derivados de la paleta de marca.
- Se activa Lovable Cloud para: el asistente IA (a través de Lovable AI, sin claves del cliente), almacenamiento de conversaciones y de los leads del formulario de contacto, y envío de aviso por email al recibir un contacto.
- El asistente se implementa en el servidor (nunca se expone la clave), con streaming de respuesta y manejo visible de errores/límites.
- Imágenes: reutilizo los assets públicos actuales (logo, fotos de servicios, logos de clientes) descargándolos; donde falte calidad, genero visuales nuevos coherentes con la marca.

## Fases

1. Sistema de diseño + Inicio en español, con el logo y colores reales.
2. Páginas de servicios, Nosotros y Contacto (ES).
3. Asistente IA con la base de conocimiento de Control 61.
4. Versión en inglés + SEO técnico e hreflang.
5. Legales (con los datos que aporte el cliente) y banner de cookies.

## Lo que necesito del cliente

CIF y datos de registro mercantil, número de inscripción en el Registro de Empresas de Seguridad, certificaciones y grados, CRA con la que trabaja, horario de atención, y logo en vectorial (SVG/PDF) si lo tiene.
