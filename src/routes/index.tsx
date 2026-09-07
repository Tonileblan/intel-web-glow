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
            streetAddress: "Pol. Ind. La标志ista, C/ Caravaca de la Cruz 13, Nave C-7",
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
        {/* Ambient Brand Glow */}
        <div className="pointer-events-none absolute -top-32 left-1/2 -z-10 h-[500px] w-[800px] -translate-x-1/2 rounded-full bg-red-600/15 blur-[120px]" />
        <div className="pointer-events-none absolute top-48 left-1/4 -z-10 h-72 w-72 rounded-full bg-sky-500/10 blur-[100px]" />

        <div className="mx-auto max-w-6xl px-4 sm:px-6">
          <div className="flex flex-col items-center text-center">
            {/* Live System Status Badge */}
            <div className="inline-flex items-center gap-2 rounded-full border border-slate-800 bg-slate-900/80 px-4 py-1.5 font-mono text-xs font-semibold text-slate-300 shadow-lg backdrop-blur-md">
              <span className="relative flex size-2">
                <span className="absolute inline-flex size-full animate-ping rounded-full bg-emerald-400 opacity-75"></span>
                <span className="relative inline-flex size-2 rounded-full bg-emerald-500"></span>
              </span>
              <span className="text-white">SISTEMAS ACTIVOS</span>
              <span className="text-slate-600">|</span>
              <span className="text-slate-400">MONITORIZACIÓN 24/7 REAL</span>
            </div>

            {/* Main Headline */}
            <h1 className="mt-6 max-w-4xl text-4xl font-extrabold tracking-tight text-white sm:text-5xl md:text-6xl md:leading-[1.12]">
              Sistemas de seguridad avanzada,{" "}
              <span className="text-red-500 underline decoration-red-500/30 decoration-wavy underline-offset-8">
                CCTV con IA
              </span>{" "}
              y protección integral
            </h1>

            {/* Subtitle */}
            <p className="mt-6 max-w-2xl text-base text-slate-300 sm:text-lg">
              Ingeniería e instalación de alarmas de Grado 2 y 3, videovigilancia de alta precisión
              y control de accesos para empresas, instituciones y hogares en Murcia y Levante.
            </p>

            {/* Primary Action Buttons */}
            <div className="mt-8 flex flex-wrap justify-center gap-3.5">
              <Link
                to="/contacto"
                className="inline-flex min-h-12 items-center gap-2 rounded-xl bg-primary px-6 text-sm font-semibold text-white shadow-lg transition-all hover:bg-red-600 hover:shadow-red-600/30"
              >
                <span>Solicitar valoración gratuita</span>
                <ArrowUpRight className="size-4" />
              </Link>
              <a
                href={site.phoneHref}
                className="inline-flex min-h-12 items-center gap-2 rounded-xl border border-slate-800 bg-slate-900/80 px-6 text-sm font-semibold text-slate-200 shadow-md backdrop-blur-md transition-colors hover:border-slate-700 hover:bg-slate-800"
              >
                <Phone className="size-4 text-red-500" />
                <span>{site.phone} · Averías 24h</span>
              </a>
            </div>

            {/* Trust Metrics & Counters */}
            <dl className="mt-14 grid w-full max-w-4xl grid-cols-2 gap-4 sm:grid-cols-4 sm:gap-6">
              <div className="rounded-xl border border-slate-800/80 bg-slate-900/60 p-4 text-center shadow-lg backdrop-blur-md transition-all hover:border-slate-700">
                <dt className="text-2xl font-bold tracking-tight text-white sm:text-3xl">
                  <Counter value={2500} prefix="+" />
                </dt>
                <dd className="mt-1 text-xs font-medium text-slate-400">Clientes protegidos</dd>
              </div>

              <div className="rounded-xl border border-slate-800/80 bg-slate-900/60 p-4 text-center shadow-lg backdrop-blur-md transition-all hover:border-slate-700">
                <dt className="text-2xl font-bold tracking-tight text-white sm:text-3xl">
                  <Counter value={99} prefix="" />
                  .9%
                </dt>
                <dd className="mt-1 text-xs font-medium text-slate-400">Disponibilidad de red</dd>
              </div>

              <div className="rounded-xl border border-slate-800/80 bg-slate-900/60 p-4 text-center shadow-lg backdrop-blur-md transition-all hover:border-slate-700">
                <dt className="text-2xl font-bold tracking-tight text-red-400 sm:text-3xl font-mono">
                  &lt; 15s
                </dt>
                <dd className="mt-1 text-xs font-medium text-slate-400">Respuesta SOC / CRA</dd>
              </div>

              <div className="rounded-xl border border-slate-800/80 bg-slate-900/60 p-4 text-center shadow-lg backdrop-blur-md transition-all hover:border-slate-700">
                <dt className="text-2xl font-bold tracking-tight text-white sm:text-3xl">
                  <Counter value={20} prefix="+" />
                </dt>
                <dd className="mt-1 text-xs font-medium text-slate-400">Años de experiencia</dd>
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
        className="border-y border-slate-800/80 bg-slate-950/60 px-4 py-20 sm:px-6 md:py-28"
        aria-labelledby="porque"
      >
        <div className="mx-auto grid max-w-6xl gap-12 lg:grid-cols-12 lg:items-center">
          <div className="lg:col-span-5">
            <Reveal>
              <p className="inline-flex items-center gap-1.5 rounded-full border border-slate-800 bg-slate-900 px-3.5 py-1 font-mono text-xs font-semibold text-slate-300">
                <ShieldCheck className="size-3.5 text-red-500" />
                VALOR DIFERENCIAL
              </p>
              <h2
                id="porque"
                className="mt-3 text-3xl font-bold tracking-tight text-white sm:text-4xl"
              >
                Por qué las empresas eligen {site.brand}
              </h2>
              <p className="mt-4 text-base leading-relaxed text-slate-300">
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
                  className="h-14 w-auto rounded-lg border border-slate-700 bg-white/95 p-1.5 shadow-md"
                />
                <img
                  src={selloRea}
                  alt="Registro de Empresas Acreditadas (REA)"
                  width={1080}
                  height={680}
                  loading="lazy"
                  className="h-14 w-auto rounded-lg border border-slate-700 bg-white/95 p-1.5 shadow-md"
                />
                <Link
                  to="/acreditaciones"
                  className="text-xs font-semibold text-red-400 hover:text-red-300 hover:underline"
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
                    <div className="flex h-full flex-col justify-between rounded-xl border border-slate-800 bg-slate-900/70 p-5 transition-all hover:border-red-500/40 hover:bg-slate-900 hover:shadow-lg">
                      <div>
                        <div className="inline-flex size-10 items-center justify-center rounded-lg bg-slate-800 shadow-md ring-1 ring-slate-700">
                          <Icon className="size-5 text-red-500" />
                        </div>
                        <h3 className="mt-4 text-base font-bold text-white">{reason.title}</h3>
                        <p className="mt-2 text-xs leading-relaxed text-slate-400">{reason.text}</p>
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
