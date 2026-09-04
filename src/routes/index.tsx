import { createFileRoute, Link } from "@tanstack/react-router";
import {
  ArrowRight,
  Building2,
  Camera,
  Flame,
  HardHat,
  Home,
  Landmark,
  Phone,
  ShieldCheck,
  Wrench,
} from "lucide-react";

import { Counter } from "@/components/Counter";
import { CtaSection } from "@/components/CtaSection";
import { Reveal } from "@/components/Reveal";
import selloRea from "@/assets/Registro-de-Empresas-Acreditadas.png";
import selloRina from "@/assets/Rina-Iso2-1.png";
import { SITE_URL, site } from "@/lib/site";

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
          name: site.brand,
          legalName: site.legalName,
          url: SITE_URL,
          telephone: "+34968622984",
          email: site.email,
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
    to: "/empresas",
    title: "Empresas",
    text: "Naves, comercios y oficinas: intrusión, incendio, accesos y CCTV en una sola instalación.",
  },
  {
    icon: Landmark,
    to: "/instituciones",
    title: "Instituciones",
    text: "Ayuntamientos, edificios públicos, instalaciones municipales y eventos.",
  },
  {
    icon: Home,
    to: "/hogar",
    title: "Hogar y urbanizaciones",
    text: "Alarmas conectadas y videovigilancia de zonas comunes, sin contratos abusivos.",
  },
  {
    icon: Camera,
    to: "/cctv",
    title: "CCTV",
    text: "Cámaras de alta resolución con búsqueda inteligente de vídeo y cumplimiento del RGPD.",
  },
  {
    icon: Wrench,
    to: "/mantenimiento",
    title: "Mantenimiento",
    text: "Contratos preventivos y correctivos con revisiones legales al día y averías 24 h.",
  },
  {
    icon: HardHat,
    to: "/obra-nueva",
    title: "Obra nueva",
    text: "Previsión en proyecto, canalizaciones en obra y legalización de la instalación.",
  },
] as const;

const reasons = [
  {
    title: "Sin trucos ni contratos a largo plazo",
    text: "Presupuestos claros y permanencias razonables. Si algo no te hace falta, te lo decimos.",
  },
  {
    title: "Soluciones personalizadas",
    text: "Cada proyecto arranca con una visita y un análisis de riesgo real, no con un paquete cerrado.",
  },
  {
    title: "Instalación profesional",
    text: "Equipo propio y certificado, obra limpia y formación al entregar el sistema.",
  },
  {
    title: "Atención 24 h ante averías",
    text: "Un teléfono que responde cuando el sistema falla, también fuera del horario de oficina.",
  },
] as const;

function Index() {
  return (
    <>
      <section className="relative isolate overflow-hidden border-b border-border">
        <img
          src="/hero-control-room.jpg"
          alt="Centro de control de videovigilancia con múltiples monitores encendidos"
          width={1920}
          height={1080}
          className="absolute inset-0 -z-10 size-full object-cover"
        />
        <div
          className="absolute inset-0 -z-10 bg-gradient-to-r from-background via-background/92 to-background/45"
          aria-hidden="true"
        />
        <div className="mx-auto max-w-6xl px-6 py-24 md:py-32">
          <div className="animate-in fade-in slide-in-from-bottom-4 duration-700">
            <p className="inline-flex items-center gap-2 rounded-full border border-border bg-card/80 px-3 py-1 text-xs font-semibold uppercase tracking-[0.2em] text-muted-foreground backdrop-blur">
              <ShieldCheck className="size-4 text-primary" aria-hidden="true" />
              {site.claim}
            </p>
            <h1 className="mt-6 max-w-4xl text-4xl font-semibold leading-tight tracking-tight md:text-6xl">
              Sistemas de seguridad para empresas, instituciones y hogares en{" "}
              <span className="text-primary">Murcia</span>
            </h1>
            <p className="mt-6 max-w-2xl text-lg text-muted-foreground">
              Diseñamos, instalamos y mantenemos alarmas, videovigilancia y control de
              accesos con más de 20 años de experiencia. Soluciones honestas y
              personalizadas, sin trucos ni contratos a largo plazo.
            </p>
            <div className="mt-8 flex flex-wrap gap-3">
              <Link
                to="/contacto"
                className="inline-flex min-h-11 items-center gap-2 rounded-md bg-primary px-5 text-sm font-medium text-primary-foreground transition-colors hover:bg-primary/90"
              >
                Solicitar valoración gratuita
                <ArrowRight className="size-4" aria-hidden="true" />
              </Link>
              <a
                href={site.phoneHref}
                className="inline-flex min-h-11 items-center gap-2 rounded-md border border-border bg-card/80 px-5 text-sm font-medium backdrop-blur transition-colors hover:bg-accent"
              >
                <Phone className="size-4" aria-hidden="true" />
                {site.phone} · 24 h
              </a>
            </div>
          </div>

          <dl className="mt-16 grid gap-8 sm:grid-cols-3">
            {site.stats.map((stat, i) => (
              <Reveal key={stat.label} delay={i * 0.08}>
                <div>
                  <dt className="text-4xl font-semibold text-primary">
                    <Counter value={stat.value} prefix={stat.prefix} />
                  </dt>
                  <dd className="mt-1 text-sm text-muted-foreground">{stat.label}</dd>
                </div>
              </Reveal>
            ))}
          </dl>
        </div>
      </section>

      <section className="px-6 py-20" aria-labelledby="servicios">
        <div className="mx-auto max-w-6xl">
          <Reveal>
            <h2 id="servicios" className="text-3xl font-semibold tracking-tight">
              Qué hacemos
            </h2>
            <p className="mt-3 max-w-2xl text-muted-foreground">
              Un único proveedor para proyectar, instalar y mantener toda la seguridad de
              tus instalaciones.
            </p>
          </Reveal>
          <ul className="mt-10 grid gap-6 sm:grid-cols-2 lg:grid-cols-3">
            {services.map((service, i) => (
              <Reveal key={service.title} delay={i * 0.06}>
                <li className="h-full">
                  <Link
                    to={service.to}
                    className="group flex h-full flex-col rounded-xl border border-border bg-card p-6 transition-colors hover:border-primary"
                  >
                    <service.icon className="size-6 text-primary" aria-hidden="true" />
                    <h3 className="mt-4 text-lg font-medium">{service.title}</h3>
                    <p className="mt-2 text-sm text-muted-foreground">{service.text}</p>
                    <span className="mt-4 inline-flex items-center gap-1 text-sm font-medium text-primary">
                      Ver más
                      <ArrowRight
                        className="size-4 transition-transform group-hover:translate-x-1"
                        aria-hidden="true"
                      />
                    </span>
                  </Link>
                </li>
              </Reveal>
            ))}
          </ul>
        </div>
      </section>

      <section className="border-y border-border px-6 py-20" aria-labelledby="porque">
        <div className="mx-auto grid max-w-6xl gap-10 md:grid-cols-2">
          <Reveal>
            <h2 id="porque" className="text-3xl font-semibold tracking-tight">
              Por qué {site.brand}
            </h2>
            <p className="mt-4 text-muted-foreground">
              Nacimos con experiencia previa en seguridad y aplicación de la ley, y hemos
              protegido desde pequeños comercios hasta instalaciones municipales. Nuestro
              trabajo es que dejes de pensar en la seguridad.
            </p>
            <div className="mt-8 flex flex-wrap items-center gap-4">
              <img
                src={selloRina}
                alt="Certificación ISO 9001, ISO 14001 e ISO 45001 emitida por RINA"
                width={1200}
                height={628}
                loading="lazy"
                className="h-16 w-auto rounded bg-white/95 p-1.5"
              />
              <img
                src={selloRea}
                alt="Registro de Empresas Acreditadas (REA)"
                width={1080}
                height={680}
                loading="lazy"
                className="h-16 w-auto rounded bg-white/95 p-1.5"
              />
              <Link
                to="/acreditaciones"
                className="text-sm font-medium text-primary hover:underline"
              >
                Ver todas las acreditaciones
              </Link>
            </div>
          </Reveal>
          <ul className="grid gap-4">
            {reasons.map((reason, i) => (
              <Reveal key={reason.title} delay={i * 0.06}>
                <li className="rounded-xl border border-border bg-card p-5">
                  <h3 className="flex items-start gap-2 font-medium">
                    <Flame className="mt-0.5 size-4 shrink-0 text-primary" aria-hidden="true" />
                    {reason.title}
                  </h3>
                  <p className="mt-2 text-sm text-muted-foreground">{reason.text}</p>
                </li>
              </Reveal>
            ))}
          </ul>
        </div>
      </section>

      <CtaSection />
    </>
  );
}
