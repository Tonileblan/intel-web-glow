import { createFileRoute, Link } from "@tanstack/react-router";
import {
  ArrowRight,
  ArrowUpRight,
  Building2,
  Camera,
  CheckCircle2,
  Clock,
  Fingerprint,
  Flame,
  HardHat,
  Home,
  Landmark,
  Lock,
  Phone,
  Radio,
  ShieldAlert,
  ShieldCheck,
  Sparkles,
  Wrench,
  Zap,
} from "lucide-react";

import { Counter } from "@/components/Counter";
import { CtaSection } from "@/components/CtaSection";
import { ClientLogos } from "@/components/ClientLogos";
import { Reveal } from "@/components/Reveal";
import { SecurityConsoleHUD } from "@/components/SecurityConsoleHUD";
import { BentoGridServices } from "@/components/BentoGridServices";
import { DefenseArchitecture } from "@/components/DefenseArchitecture";
import { TestimonialsSection } from "@/components/TestimonialsSection";
import selloRea from "@/assets/Registro-de-Empresas-Acreditadas.png";
import selloRina from "@/assets/Rina-Iso2-1.png";
import { SITE_URL, site } from "@/lib/site";

const title = "Control 61 — Sistemas de Seguridad, CCTV con IA y Alarmas en Murcia";
const description =
  "Empresa homologada en seguridad integral en Murcia: instalación de alarmas Grado 2 y 3, CCTV con IA, control de accesos y monitorización 24 h. Valoración técnica gratuita.";

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
            streetAddress: "Pol. Ind. La Polvorista, C/ Caravaca de la Cruz 13, Nave C-7",
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

const reasons = [
  {
    title: "Sin cuotas trampa ni permanencias abusivas",
    text: "Presupuestos cerrados y transparentes. Eres dueño de tus equipos sin cláusulas de rescisión ocultas.",
    icon: ShieldCheck,
  },
  {
    title: "Auditoría previa y estudio sobre el terreno",
    text: "Analizamos los accesos y riesgos reales de tu instalación antes de redactar cualquier propuesta técnica.",
    icon: Sparkles,
  },
  {
    title: "Técnicos certificados e ingenieros en plantilla",
    text: "Equipo propio homologado con formación continua. Cero subcontratación de calidad cuestionable.",
    icon: CheckCircle2,
  },
  {
    title: "Servicio técnico y averías urgentes 24 horas",
    text: "Un teléfono atendido por personal técnico de guardia que responde y actúa cuando el sistema falla.",
    icon: Zap,
  },
] as const;

function Index() {
  return (
    <>
      {/* Hero Section */}
      <section className="relative isolate overflow-hidden bg-tech-grid pb-20 pt-12 md:pb-28 md:pt-16">
        {/* Soft Brand Glow in background */}
        <div className="pointer-events-none absolute -top-32 left-1/2 -z-10 h-[500px] w-[800px] -translate-x-1/2 rounded-full bg-red-100/40 blur-3xl" />

        <div className="mx-auto max-w-6xl px-4 sm:px-6">
          <div className="flex flex-col items-center text-center">
            {/* Live System Status Badge */}
            <div className="inline-flex items-center gap-2 rounded-full border border-slate-200 bg-white px-3.5 py-1.5 font-mono text-xs font-semibold text-slate-700 shadow-2xs">
              <span className="relative flex size-2">
                <span className="absolute inline-flex size-full animate-ping rounded-full bg-emerald-400 opacity-75"></span>
                <span className="relative inline-flex size-2 rounded-full bg-emerald-500"></span>
              </span>
              <span>SISTEMAS ACTIVOS</span>
              <span className="text-slate-300">|</span>
              <span className="text-slate-500">MONITORIZACIÓN 24/7 REAL</span>
            </div>

            {/* Main Headline */}
            <h1 className="mt-6 max-w-4xl text-4xl font-extrabold tracking-tight text-slate-900 sm:text-5xl md:text-6xl md:leading-[1.12]">
              Sistemas de seguridad avanzada, <span className="text-primary">CCTV con IA</span> y
              protección integral
            </h1>

            {/* Subtitle */}
            <p className="mt-6 max-w-2xl text-base text-slate-600 sm:text-lg">
              Ingeniería e instalación de alarmas de Grado 2 y 3, videovigilancia de alta precisión
              y control de accesos para empresas, instituciones y hogares en Murcia y Levante.
            </p>

            {/* Primary Action Buttons */}
            <div className="mt-8 flex flex-wrap justify-center gap-3.5">
              <Link
                to="/contacto"
                className="inline-flex min-h-12 items-center gap-2 rounded-xl bg-primary px-6 text-sm font-semibold text-white shadow-xs transition-all hover:bg-red-700 hover:shadow-md"
              >
                <span>Solicitar valoración gratuita</span>
                <ArrowUpRight className="size-4" />
              </Link>
              <a
                href={site.phoneHref}
                className="inline-flex min-h-12 items-center gap-2 rounded-xl border border-slate-300 bg-white px-6 text-sm font-semibold text-slate-800 shadow-2xs transition-colors hover:bg-slate-50"
              >
                <Phone className="size-4 text-primary" />
                <span>{site.phone} · Averías 24h</span>
              </a>
            </div>

            {/* Trust Metrics & Counters */}
            <dl className="mt-14 grid w-full max-w-4xl grid-cols-2 gap-4 sm:grid-cols-4 sm:gap-6">
              <div className="rounded-xl border border-slate-200/80 bg-white/90 p-4 text-center shadow-2xs backdrop-blur-xs">
                <dt className="text-2xl font-bold tracking-tight text-slate-900 sm:text-3xl">
                  <Counter value={2500} prefix="+" />
                </dt>
                <dd className="mt-1 text-xs font-medium text-slate-500">Clientes protegidos</dd>
              </div>

              <div className="rounded-xl border border-slate-200/80 bg-white/90 p-4 text-center shadow-2xs backdrop-blur-xs">
                <dt className="text-2xl font-bold tracking-tight text-slate-900 sm:text-3xl">
                  <Counter value={99} prefix="" />
                  .9%
                </dt>
                <dd className="mt-1 text-xs font-medium text-slate-500">Disponibilidad de red</dd>
              </div>

              <div className="rounded-xl border border-slate-200/80 bg-white/90 p-4 text-center shadow-2xs backdrop-blur-xs">
                <dt className="text-2xl font-bold tracking-tight text-primary sm:text-3xl font-mono">
                  &lt; 15s
                </dt>
                <dd className="mt-1 text-xs font-medium text-slate-500">Respuesta SOC / CRA</dd>
              </div>

              <div className="rounded-xl border border-slate-200/80 bg-white/90 p-4 text-center shadow-2xs backdrop-blur-xs">
                <dt className="text-2xl font-bold tracking-tight text-slate-900 sm:text-3xl">
                  <Counter value={20} prefix="+" />
                </dt>
                <dd className="mt-1 text-xs font-medium text-slate-500">Años de experiencia</dd>
              </div>
            </dl>
          </div>

          {/* Interactive Security Console HUD */}
          <div className="mt-12">
            <Reveal delay={0.15}>
              <SecurityConsoleHUD />
            </Reveal>
          </div>
        </div>
      </section>

      {/* Client Logos Carousel */}
      <ClientLogos text="Más de 2.500 empresas, naves industriales, comunidades de vecinos y dependencias públicas protegidas en la Región de Murcia." />

      {/* Bento Grid Services Section */}
      <BentoGridServices />

      {/* 4-Step Defense Workflow Architecture */}
      <DefenseArchitecture />

      {/* Why Control 61 Section */}
      <section
        className="border-b border-slate-200/80 bg-white px-4 py-20 sm:px-6 md:py-28"
        aria-labelledby="porque"
      >
        <div className="mx-auto grid max-w-6xl gap-12 lg:grid-cols-12 lg:items-center">
          <div className="lg:col-span-5">
            <Reveal>
              <p className="inline-flex items-center gap-1.5 rounded-full border border-slate-200 bg-slate-50 px-3 py-1 font-mono text-xs font-semibold text-slate-700">
                <ShieldCheck className="size-3.5 text-primary" />
                VALOR DIFERENCIAL
              </p>
              <h2
                id="porque"
                className="mt-3 text-3xl font-bold tracking-tight text-slate-900 sm:text-4xl"
              >
                Por qué las empresas eligen {site.brand}
              </h2>
              <p className="mt-4 text-base leading-relaxed text-slate-600">
                Nacimos con amplia experiencia técnica y operativa en el sector de la seguridad
                privada. Nuestro trabajo es implementar sistemas fiables que funcionen sin fallos
                para que dejes de preocuparte por la seguridad de tus instalaciones.
              </p>

              <div className="mt-8 flex flex-wrap items-center gap-4">
                <img
                  src={selloRina}
                  alt="Certificación ISO 9001, ISO 14001 e ISO 45001 emitida por RINA"
                  width={1200}
                  height={628}
                  loading="lazy"
                  className="h-14 w-auto rounded-lg border border-slate-200 bg-white p-1.5 shadow-2xs"
                />
                <img
                  src={selloRea}
                  alt="Registro de Empresas Acreditadas (REA)"
                  width={1080}
                  height={680}
                  loading="lazy"
                  className="h-14 w-auto rounded-lg border border-slate-200 bg-white p-1.5 shadow-2xs"
                />
                <Link
                  to="/acreditaciones"
                  className="text-xs font-semibold text-primary hover:underline"
                >
                  Ver todas las acreditaciones →
                </Link>
              </div>
            </Reveal>
          </div>

          <div className="lg:col-span-7">
            <div className="grid gap-4 sm:grid-cols-2">
              {reasons.map((reason, i) => {
                const Icon = reason.icon;
                return (
                  <Reveal key={reason.title} delay={i * 0.08}>
                    <div className="flex h-full flex-col justify-between rounded-xl border border-slate-200 bg-slate-50/70 p-5 transition-all hover:border-slate-300 hover:bg-white hover:shadow-xs">
                      <div>
                        <div className="inline-flex size-10 items-center justify-center rounded-lg bg-white shadow-2xs ring-1 ring-slate-200">
                          <Icon className="size-5 text-primary" />
                        </div>
                        <h3 className="mt-4 text-base font-bold text-slate-900">{reason.title}</h3>
                        <p className="mt-2 text-xs leading-relaxed text-slate-600">{reason.text}</p>
                      </div>
                    </div>
                  </Reveal>
                );
              })}
            </div>
          </div>
        </div>
      </section>

      {/* Testimonials & Corporate Social Proof */}
      <TestimonialsSection />

      {/* Final 1-Step Fast Conversion CTA */}
      <CtaSection />
    </>
  );
}
