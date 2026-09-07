import { createFileRoute } from "@tanstack/react-router";
import { Clock, Mail, MapPin, Phone, ShieldCheck, Sparkles } from "lucide-react";

import { PageHero } from "@/components/PageHero";
import { Reveal } from "@/components/Reveal";
import { QuickAuditForm } from "@/components/QuickAuditForm";
import { pageMeta, site } from "@/lib/site";

export const Route = createFileRoute("/contacto")({
  head: () =>
    pageMeta({
      title: "Contacto y Valoración Técnica Gratuita | Control 61",
      description:
        "Pide una valoración gratuita de tu instalación de seguridad en Murcia. Teléfono 968 62 29 84, atención de averías 24 h e info@control61.es.",
      path: "/contacto",
    }),
  component: ContactoPage,
});

function ContactoPage() {
  return (
    <>
      <PageHero
        eyebrow="Contacto Directo & Auditoría"
        title="Cuéntanos qué espacio necesitas proteger"
        text="Te visitamos sobre el terreno, analizamos las vulnerabilidades reales y te preparamos una propuesta técnica clara y sin sorpresas. Valoración gratuita y sin compromiso."
      >
        <div className="mt-8 flex flex-wrap gap-3.5">
          <a
            href={site.phoneHref}
            className="inline-flex min-h-12 items-center gap-2 rounded-xl bg-primary px-6 text-sm font-semibold text-white shadow-lg transition-all hover:bg-red-600 hover:shadow-red-600/30"
          >
            <Phone className="size-4" />
            <span>Llamar: {site.phone}</span>
          </a>
          <a
            href={`mailto:${site.email}`}
            className="inline-flex min-h-12 items-center gap-2 rounded-xl border border-slate-800 bg-slate-900 px-6 text-sm font-semibold text-slate-200 shadow-md backdrop-blur-md transition-colors hover:bg-slate-800 hover:text-white"
          >
            <Mail className="size-4 text-red-500" />
            <span>{site.email}</span>
          </a>
        </div>
      </PageHero>

      <section className="px-4 py-16 sm:px-6 md:py-24" aria-labelledby="formulario">
        <div className="mx-auto max-w-6xl">
          <div className="mb-12 text-center">
            <h2
              id="formulario"
              className="text-3xl font-bold tracking-tight text-white sm:text-4xl"
            >
              Solicitud de Estudio Gratuito
            </h2>
            <p className="mt-3 text-base text-slate-300">
              Rellena el formulario rápido y un técnico especialista se pondrá en contacto contigo.
            </p>
          </div>

          <Reveal>
            <QuickAuditForm />
          </Reveal>

          {/* Contact Details Cards */}
          <div className="mt-16 grid gap-6 sm:grid-cols-2 lg:grid-cols-4">
            <Reveal delay={0.05}>
              <div className="rounded-2xl border border-slate-800 bg-slate-900/70 p-6 shadow-xl backdrop-blur-md transition-all hover:border-red-500/40 hover:bg-slate-900">
                <div className="inline-flex size-10 items-center justify-center rounded-lg bg-red-950/60 text-red-500 ring-1 ring-red-900/50">
                  <Phone className="size-5" />
                </div>
                <h3 className="mt-4 font-bold text-white">Teléfono 24 Horas</h3>
                <p className="mt-1 text-xs text-slate-400">Atención comercial y urgencias</p>
                <a
                  href={site.phoneHref}
                  className="mt-3 inline-block font-semibold text-white hover:text-red-400"
                >
                  {site.phone}
                </a>
              </div>
            </Reveal>

            <Reveal delay={0.1}>
              <div className="rounded-2xl border border-slate-800 bg-slate-900/70 p-6 shadow-xl backdrop-blur-md transition-all hover:border-red-500/40 hover:bg-slate-900">
                <div className="inline-flex size-10 items-center justify-center rounded-lg bg-slate-800 text-red-500 ring-1 ring-slate-700">
                  <Mail className="size-5" />
                </div>
                <h3 className="mt-4 font-bold text-white">Correo Electrónico</h3>
                <p className="mt-1 text-xs text-slate-400">Respuesta en &lt; 2 horas</p>
                <a
                  href={`mailto:${site.email}`}
                  className="mt-3 inline-block font-semibold text-white hover:text-red-400"
                >
                  {site.email}
                </a>
              </div>
            </Reveal>

            <Reveal delay={0.15}>
              <div className="rounded-2xl border border-slate-800 bg-slate-900/70 p-6 shadow-xl backdrop-blur-md transition-all hover:border-red-500/40 hover:bg-slate-900">
                <div className="inline-flex size-10 items-center justify-center rounded-lg bg-slate-800 text-red-500 ring-1 ring-slate-700">
                  <MapPin className="size-5" />
                </div>
                <h3 className="mt-4 font-bold text-white">Oficinas Centrales</h3>
                <p className="mt-1 text-xs text-slate-400">Pol. Ind. La Polvorista</p>
                <p className="mt-3 text-xs leading-relaxed text-slate-300">
                  C/ Caravaca de la Cruz 13, Nave C-7, Molina de Segura (Murcia)
                </p>
              </div>
            </Reveal>

            <Reveal delay={0.2}>
              <div className="rounded-2xl border border-slate-800 bg-slate-900/70 p-6 shadow-xl backdrop-blur-md transition-all hover:border-red-500/40 hover:bg-slate-900">
                <div className="inline-flex size-10 items-center justify-center rounded-lg bg-slate-800 text-red-500 ring-1 ring-slate-700">
                  <Clock className="size-5" />
                </div>
                <h3 className="mt-4 font-bold text-white">Horario de Oficina</h3>
                <p className="mt-1 text-xs text-slate-400">Lunes a viernes 9:00 - 18:00</p>
                <p className="mt-3 font-mono text-xs font-semibold text-emerald-400">
                  ● Servicio de guardia 24/7 activo
                </p>
              </div>
            </Reveal>
          </div>
        </div>
      </section>
    </>
  );
}
