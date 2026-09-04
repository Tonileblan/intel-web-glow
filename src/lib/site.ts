export const SITE_URL = "https://intel-web-glow.lovable.app";

export const site = {
  brand: "Control 61",
  legalName: "Desarrollos y Sistemas Inteligentes S.L.",
  claim: "Expertos en tranquilidad",
  phone: "968 62 29 84",
  phoneHref: "tel:+34968622984",
  email: "info@control61.es",
  address:
    "Pol. Ind. La Polvorista, C/ Caravaca de la Cruz 13, Nave C-7, 30500 Molina de Segura (Murcia)",
  schedule: "Lunes a viernes de 9:00 a 18:00 · Atención de averías 24 h",
  stats: [
    { value: 2500, prefix: "+", label: "clientes protegidos" },
    { value: 20, prefix: "+", label: "años de experiencia" },
    { value: 5000, prefix: "+", label: "proyectos terminados" },
  ],
  nav: [
    { to: "/empresas", label: "Empresas" },
    { to: "/instituciones", label: "Instituciones" },
    { to: "/hogar", label: "Hogar" },
    { to: "/cctv", label: "CCTV" },
    { to: "/mantenimiento", label: "Mantenimiento" },
    { to: "/acreditaciones", label: "Acreditaciones" },
    { to: "/nosotros", label: "Nosotros" },
  ],
  extraNav: [{ to: "/obra-nueva", label: "Obra nueva y reformas" }],
  legalNav: [
    { to: "/aviso-legal", label: "Aviso legal" },
    { to: "/privacidad", label: "Privacidad" },
    { to: "/cookies", label: "Cookies" },
  ],
} as const;

export function pageMeta({
  title,
  description,
  path,
}: {
  title: string;
  description: string;
  path: string;
}) {
  const url = `${SITE_URL}${path === "/" ? "" : path}`;
  return {
    meta: [
      { title },
      { name: "description", content: description },
      { property: "og:title", content: title },
      { property: "og:description", content: description },
      { property: "og:type", content: "website" },
      { property: "og:url", content: url },
      { name: "twitter:card", content: "summary_large_image" },
    ],
    links: [{ rel: "canonical", href: url }],
  };
}
