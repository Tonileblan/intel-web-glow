# Reconstrucción del prototipo: marca, Header, Footer y páginas ES

El proyecto está hoy en el template base más la home de una sola página que hice para arreglar el SEO: solo existen `__root.tsx`, `index.tsx` y `sitemap[.]xml.ts`; no hay componentes propios, ni `src/assets/`, ni `src/lib/site.ts`, ni `motion` instalado. Esta fase rehace la capa de marca y todas las páginas en español del plan aprobado. El asistente IA, la versión en inglés y el blog quedan para fases posteriores.

## Marca y assets

- Descargar de control61.es y guardar como assets del proyecto: logo (`Logo-Limpio.png`), sello RINA ISO (`Rina-Iso2-1.png`) y sello REA (`Registro-de-Empresas-Acreditadas.png`).
- Favicon cuadrado derivado del logo en `public/favicon.png`, declarado en el root, y borrado del `favicon.ico` por defecto.
- Fotografía de stock generada y coherente (base oscura + acento rojo, como una sola sesión): centro de control, nave/comercio, edificio público, hogar, técnico en mantenimiento, obra.
- Sistema de diseño: mantener la paleta oscura con rojo corporativo ya presente en `src/styles.css` y añadir los tokens que falten (gradientes, sombra de acento, superficies elevadas). Nada de colores hardcodeados en componentes.

## Chrome del sitio

- `src/lib/site.ts`: marca, razón social, claim, teléfono 24 h, email, dirección, cifras y navegación en un único sitio.
- `Header`: logo, navegación de escritorio, menú móvil, teléfono visible y CTA "Valoración gratuita"; estado compacto al hacer scroll.
- `Footer`: logo, sellos RINA y REA, servicios, contacto y enlaces legales.
- Ambos se montan en `__root.tsx` alrededor del `<Outlet />`, con un solo `<main>` en el layout.
- Piezas reutilizables: `PageHero`, `FeatureGrid`, `CtaSection`, `Reveal` (revelado al scroll) y `Counter` (cifras animadas), con Motion y respetando `prefers-reduced-motion`.

## Páginas en español

Una ruta por sección, cada una con su propio `head()` (title, description, og) y un solo H1:

- `/` — home rehecha sobre el nuevo sistema: hero con fotografía, cifras animadas, servicios, sellos de confianza y CTA.
- `/empresas` — sistemas integrales, intrusión, incendio, accesos, CCTV, monitorización.
- `/instituciones` — ayuntamientos, edificios públicos, instalaciones municipales, eventos y patrimonio.
- `/hogar` — viviendas y urbanizaciones.
- `/cctv` — videovigilancia y búsqueda inteligente de vídeo, con mención a RGPD.
- `/obra-nueva` — proyectos de obra y renovaciones.
- `/mantenimiento` — contratos preventivos y correctivos, revisiones legales, tiempos de respuesta.
- `/acreditaciones` — ISO 9001/14001/45001 (RINA/CISQ/IQNet), REA, Registro en Industria (PCI) y Registro en Seguridad Privada, cada uno en clave de beneficio, con el sello y el escaneo original ampliable.
- `/nosotros` — 20+ años, equipo, cifras, filosofía sin contratos abusivos.
- `/contacto` — formulario de valoración gratuita (solo maquetado en esta fase), teléfono 24 h, email, dirección y horario.
- Legales `/aviso-legal`, `/privacidad`, `/cookies` con el contenido actual de la web; los datos que faltan (CIF, registro mercantil, número de inscripción en Seguridad Privada) quedan marcados como pendientes de confirmar, no inventados.

Los datos de las acreditaciones que no se leen con certeza en los escaneos (números, alcance exacto, vigencias) se dejan sin publicar hasta que el cliente los valide.

## Detalles técnicos

- TanStack Start con una ruta por página; `src/routeTree.gen.ts` se regenera solo.
- Se instala `motion` para las animaciones.
- Imágenes con tamaños responsivos, `loading="lazy"` fuera del hero y `alt` descriptivo.
- Datos estructurados `SecuritySystemInstaller` en la home y canónicas por página; el sitemap se amplía con todas las rutas nuevas.
- Verificación al terminar: build + lint y repaso visual de cada ruta en el preview.

## Fuera de alcance en esta fase

Asistente IA con Lovable Cloud, blog y artículos, envío real del formulario, y la versión en inglés con hreflang.
