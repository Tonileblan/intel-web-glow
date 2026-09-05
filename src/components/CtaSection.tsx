import { Link } from "@tanstack/react-router";
import { Phone, ArrowUpRight, ShieldCheck, Sparkles } from "lucide-react";

import { site } from "@/lib/site";
import { Reveal } from "./Reveal";
import { QuickAuditForm } from "./QuickAuditForm";

export function CtaSection({
  title = "Solicita tu estudio y valoración técnica gratuita",
  text = "Evaluamos tus instalaciones sobre el terreno, detectamos vulnerabilidades reales y te proponemos una solución técnica a medida sin compromiso.",
  showForm = true,
}: {
  title?: string;
  text?: string;
  showForm?: boolean;
}) {
  return (
    <section className="relative overflow-hidden border-t border-slate-200/80 bg-slate-50/60 px-4 py-20 sm:px-6 md:py-28" aria-labelledby="cta-heading">
      {/* Background Decorative Gradient */}
      <div className="pointer-events-none absolute -top-40 left-1/2 -z-10 h-96 w-[700px] -translate-x-1/2 rounded-full bg-red-100/40 blur-3xl" />

      <div className="mx-auto max-w-6xl">
        <Reveal>
          <div className="mb-12 text-center">
            <p className="inline-flex items-center gap-1.5 rounded-full border border-red-200 bg-white px-3 py-1 font-mono text-xs font-semibold uppercase text-primary shadow-2xs">
              <Sparkles className="size-3.5" />
              PRIMER PASO HACIA TU TRANQUILIDAD
            </p>
            <h2 id="cta-heading" className="mt-3 text-3xl font-bold tracking-tight text-slate-900 sm:text-4xl">
              {title}
            </h2>
            <p className="mx-auto mt-3 max-w-2xl text-base text-slate-600">
              {text}
            </p>
          </div>
        </Reveal>

        {showForm ? (
          <Reveal delay={0.1}>
            <QuickAuditForm />
          </Reveal>
        ) : (
          <Reveal delay={0.1}>
            <div className="mx-auto max-w-3xl rounded-2xl border border-slate-200 bg-white p-8 text-center shadow-md sm:p-12">
              <div className="flex flex-wrap justify-center gap-4">
                <Link
                  to="/contacto"
                  className="inline-flex min-h-12 items-center gap-2 rounded-xl bg-primary px-6 text-sm font-semibold text-white shadow-xs transition-all hover:bg-red-700 hover:shadow-md"
                >
                  <span>Pedir valoración gratuita</span>
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
            </div>
          </Reveal>
        )}
      </div>
    </section>
  );
}
