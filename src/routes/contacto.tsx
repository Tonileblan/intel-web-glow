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
            className="inline-flex min-h-12 items-center gap-2 rounded-xl bg-primary px-6 text-sm font-semibold text-white shadow-xs transition-all hover:bg-red-700 hover:shadow-md"
          >
            <Phone className="size-4" />
            <span>Llamar: {site.phone}</span>
          </a>
          <a
            href={`mailto:${site.email}`}
            className="inline-flex min-h-12 items-center gap-2 rounded-xl border border-slate-300 bg-white px-6 text-sm font-semibold text-slate-800 shadow-2xs transition-colors hover:bg-slate-50"
          >
            <Mail className="size-4 text-primary" />
            <span>{site.email}</span>
          </a>
        </div>
      </PageHero>

      <section className="px-4 py-16 sm:px-6 md:py-24" aria-labelledby="formulario">
        <div className="mx-auto max-w-6xl">
          <div className="mb-12 text-center">
            <h2
              id="formulario"
              className="text-3xl font-bold tracking-tight text-slate-900 sm:text-4xl"
            >
              Solicitud de Estudio Gratuito
            </h2>
            <p className="mt-3 text-base text-slate-600">
              Rellena el formulario rápido y un técnico especialista se pondrá en contacto contigo.
            </p>
          </div>

          <Reveal>
            <QuickAuditForm />
          </Reveal>

          {/* Contact Details Cards */}
          <div className="mt-16 grid gap-6 sm:grid-cols-2 lg:grid-cols-4">
            <Reveal delay={0.05}>
              <div className="rounded-2xl border border-slate-200 bg-white p-6 shadow-xs">
                <div className="inline-flex size-10 items-center justify-center rounded-lg bg-red-50 text-primary">
                  <Phone className="size-5" />
                </div>
                <h3 className="mt-4 font-bold text-slate-900">Teléfono 24 Horas</h3>
                <p className="mt-1 text-xs text-slate-500">Atención comercial y urgencias</p>
                <a
                  href={site.phoneHref}
                  className="mt-3 inline-block font-semibold text-slate-900 hover:text-primary"
                >
                  {site.phone}
                </a>
              </div>
            </Reveal>

            <Reveal delay={0.1}>
              <div className="rounded-2xl border border-slate-200 bg-white p-6 shadow-xs">
                <div className="inline-flex size-10 items-center justify-center rounded-lg bg-slate-100 text-slate-900">
                  <Mail className="size-5 text-primary" />
                </div>
                <h3 className="mt-4 font-bold text-slate-900">Correo Electrónico</h3>
                <p className="mt-1 text-xs text-slate-500">Respuesta en &lt; 2 horas</p>
                <a
                  href={`mailto:${site.email}`}
                  className="mt-3 inline-block font-semibold text-slate-900 hover:text-primary"
                >
                  {site.email}
                </a>
              </div>
            </Reveal>

            <Reveal delay={0.15}>
              <div className="rounded-2xl border border-slate-200 bg-white p-6 shadow-xs">
                <div className="inline-flex size-10 items-center justify-center rounded-lg bg-slate-100 text-slate-900">
                  <MapPin className="size-5 text-primary" />
                </div>
                <h3 className="mt-4 font-bold text-slate-900">Oficinas Centrales</h3>
                <p className="mt-1 text-xs text-slate-500">Pol. Ind. La Polvorista</p>
                <p className="mt-3 text-xs leading-relaxed text-slate-700">
                  C/ Caravaca de la Cruz 13, Nave C-7, Molina de Segura (Murcia)
                </p>
              </div>
            </Reveal>

            <Reveal delay={0.2}>
              <div className="rounded-2xl border border-slate-200 bg-white p-6 shadow-xs">
                <div className="inline-flex size-10 items-center justify-center rounded-lg bg-slate-100 text-slate-900">
                  <Clock className="size-5 text-primary" />
                </div>
                <h3 className="mt-4 font-bold text-slate-900">Horario de Oficina</h3>
                <p className="mt-1 text-xs text-slate-500">Lunes a viernes 9:00 - 18:00</p>
                <p className="mt-3 font-mono text-xs font-semibold text-emerald-600">
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
