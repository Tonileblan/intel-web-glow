import { createFileRoute } from "@tanstack/react-router";
import {
  Building2,
  Camera,
  Clock,
  Flame,
  Home,
  Landmark,
  Mail,
  MapPin,
  Phone,
  ShieldCheck,
  Wrench,
} from "lucide-react";

const SITE_URL = "https://intel-web-glow.lovable.app";

const title = "Control 61 — Sistemas de seguridad en Murcia";
const description =
  "Instaladores de alarmas, CCTV y control de accesos en Murcia. Más de 20 años protegiendo empresas, instituciones y hogares. Valoración gratuita y atención 24 h.";

export const Route = createFileRoute("/")({
  head: () => ({
    meta: [
      { title },
      { name: "description", content: description },
      { property: "og:title", content: title },
      { property: "og:description", content: description },
      { property: "og:type", content: "website" },
      { property: "og:url", content: SITE_URL },
      { name: "twitter:card", content: "summary_large_image" },
    ],
    links: [{ rel: "canonical", href: SITE_URL }],
    scripts: [
      {
        type: "application/ld+json",
        children: JSON.stringify({
          "@context": "https://schema.org",
          "@type": "SecuritySystemInstaller",
          name: "Control 61",
          legalName: "Desarrollos y Sistemas Inteligentes S.L.",
          url: SITE_URL,
          telephone: "+34968622984",
          email: "info@control61.es",
          address: {
            "@type": "PostalAddress",
            streetAddress:
              "Pol. Ind. La Polvorista, C/ Caravaca de la Cruz 13, Nave C-7",
            postalCode: "30500",
            addressLocality: "Molina de Segura",
            addressRegion: "Murcia",
            addressCountry: "ES",
          },
          areaServed: "Región de Murcia",
        }),
      },
    ],
  }),
  component: Index,
});

const services = [
  {
    icon: Building2,
    title: "Seguridad para empresas",
    text: "Sistemas integrales para naves, comercios y oficinas: intrusión, incendio, CCTV y accesos en una sola instalación.",
  },
  {
    icon: Landmark,
    title: "Instituciones y administraciones",
    text: "Experiencia trabajando para ayuntamientos, edificios públicos, instalaciones municipales y eventos.",
  },
  {
    icon: Home,
    title: "Hogar y particulares",
    text: "Alarmas conectadas y videovigilancia para viviendas y urbanizaciones, sin contratos abusivos.",
  },
  {
    icon: Camera,
    title: "CCTV y videovigilancia",
    text: "Cámaras de alta resolución con grabación y búsqueda inteligente de vídeo conforme al RGPD.",
  },
  {
    icon: Flame,
    title: "Alarmas de robo e incendio",
    text: "Detección temprana y sistemas de protección contra incendios instalados por empresa registrada en Industria.",
  },
  {
    icon: Wrench,
    title: "Mantenimiento de sistemas",
    text: "Contratos preventivos y correctivos para empresas, comunidades e instituciones, con revisiones legales al día.",
  },
];

const stats = [
  { value: "+2.500", label: "clientes protegidos" },
  { value: "+20", label: "años de experiencia" },
  { value: "+5.000", label: "proyectos terminados" },
];

function Index() {
  return (
    <main className="min-h-screen bg-background text-foreground">
      <section className="border-b border-border px-6 py-20 md:py-28">
        <div className="mx-auto max-w-5xl">
          <p className="inline-flex items-center gap-2 rounded-full border border-border px-3 py-1 text-xs font-medium uppercase tracking-widest text-muted-foreground">
            <ShieldCheck className="size-4 text-primary" />
            Expertos en tranquilidad
          </p>
          <h1 className="mt-6 text-4xl font-semibold leading-tight tracking-tight md:text-6xl">
            Sistemas de seguridad para empresas, instituciones y hogares en{" "}
            <span className="text-primary">Murcia</span>
          </h1>
          <p className="mt-6 max-w-2xl text-lg text-muted-foreground">
            Control 61 diseña, instala y mantiene alarmas, videovigilancia y control de
            accesos con más de 20 años de experiencia en seguridad y aplicación de la ley.
            Soluciones honestas y personalizadas, sin trucos ni contratos a largo plazo.
          </p>
          <div className="mt-8 flex flex-wrap gap-3">
            <a
              href="#contacto"
              className="inline-flex min-h-11 items-center rounded-md bg-primary px-5 text-sm font-medium text-primary-foreground transition-colors hover:bg-primary/90"
            >
              Solicitar valoración gratuita
            </a>
            <a
              href="tel:+34968622984"
              className="inline-flex min-h-11 items-center gap-2 rounded-md border border-border px-5 text-sm font-medium transition-colors hover:bg-accent"
            >
              <Phone className="size-4" />
              968 62 29 84 · 24 h
            </a>
          </div>
          <dl className="mt-14 grid gap-8 sm:grid-cols-3">
            {stats.map((stat) => (
              <div key={stat.label}>
                <dt className="text-3xl font-semibold text-primary">{stat.value}</dt>
                <dd className="text-sm text-muted-foreground">{stat.label}</dd>
              </div>
            ))}
          </dl>
        </div>
      </section>

      <section className="px-6 py-20" aria-labelledby="servicios">
        <div className="mx-auto max-w-5xl">
          <h2 id="servicios" className="text-3xl font-semibold tracking-tight">
            Qué hacemos
          </h2>
          <p className="mt-3 max-w-2xl text-muted-foreground">
            Un único proveedor para proyectar, instalar y mantener toda la seguridad de tus
            instalaciones.
          </p>
          <ul className="mt-10 grid gap-6 sm:grid-cols-2 lg:grid-cols-3">
            {services.map((service) => (
              <li
                key={service.title}
                className="rounded-xl border border-border bg-card p-6 transition-colors hover:border-primary"
              >
                <service.icon className="size-6 text-primary" aria-hidden="true" />
                <h3 className="mt-4 text-lg font-medium">{service.title}</h3>
                <p className="mt-2 text-sm text-muted-foreground">{service.text}</p>
              </li>
            ))}
          </ul>
        </div>
      </section>

      <section className="border-y border-border px-6 py-20" aria-labelledby="confianza">
        <div className="mx-auto max-w-5xl">
          <h2 id="confianza" className="text-3xl font-semibold tracking-tight">
            Empresa certificada y acreditada
          </h2>
          <ul className="mt-8 grid gap-4 sm:grid-cols-2">
            <li className="rounded-lg border border-border p-5">
              <h3 className="font-medium">ISO 9001, 14001 y 45001</h3>
              <p className="mt-1 text-sm text-muted-foreground">
                Calidad, medio ambiente y seguridad y salud laboral, certificadas por RINA.
              </p>
            </li>
            <li className="rounded-lg border border-border p-5">
              <h3 className="font-medium">Empresa acreditada REA</h3>
              <p className="mt-1 text-sm text-muted-foreground">
                Registro de Empresas Acreditadas para trabajos en el sector de la
                construcción.
              </p>
            </li>
            <li className="rounded-lg border border-border p-5">
              <h3 className="font-medium">Registro en Industria (PCI)</h3>
              <p className="mt-1 text-sm text-muted-foreground">
                Instalador autorizado de sistemas de protección contra incendios.
              </p>
            </li>
            <li className="rounded-lg border border-border p-5">
              <h3 className="font-medium">Registro en Seguridad Privada</h3>
              <p className="mt-1 text-sm text-muted-foreground">
                Empresa inscrita en el registro del Ministerio del Interior.
              </p>
            </li>
          </ul>
        </div>
      </section>

      <section id="contacto" className="px-6 py-20" aria-labelledby="contacto-titulo">
        <div className="mx-auto max-w-5xl">
          <h2 id="contacto-titulo" className="text-3xl font-semibold tracking-tight">
            Hablemos de tu instalación
          </h2>
          <p className="mt-3 max-w-2xl text-muted-foreground">
            Te visitamos, analizamos los riesgos reales y te proponemos solo lo que
            necesitas. La valoración es gratuita.
          </p>
          <ul className="mt-8 grid gap-4 text-sm sm:grid-cols-2">
            <li className="flex items-center gap-3">
              <Phone className="size-4 text-primary" aria-hidden="true" />
              <a href="tel:+34968622984" className="hover:text-primary">
                968 62 29 84 (24 horas)
              </a>
            </li>
            <li className="flex items-center gap-3">
              <Mail className="size-4 text-primary" aria-hidden="true" />
              <a href="mailto:info@control61.es" className="hover:text-primary">
                info@control61.es
              </a>
            </li>
            <li className="flex items-center gap-3">
              <MapPin className="size-4 text-primary" aria-hidden="true" />
              Pol. Ind. La Polvorista, C/ Caravaca de la Cruz 13, Nave C-7, 30500 Molina de
              Segura (Murcia)
            </li>
            <li className="flex items-center gap-3">
              <Clock className="size-4 text-primary" aria-hidden="true" />
              Atención de urgencias 24 h, todos los días
            </li>
          </ul>
        </div>
      </section>

      <footer className="border-t border-border px-6 py-10 text-sm text-muted-foreground">
        <div className="mx-auto max-w-5xl">
          Control 61 · Desarrollos y Sistemas Inteligentes S.L. · Seguridad en la Región de
          Murcia
        </div>
      </footer>
    </main>
  );
}
