import { Link } from "@tanstack/react-router";
import { Phone } from "lucide-react";

import { site } from "@/lib/site";

import { Reveal } from "./Reveal";

export function CtaSection({
  title = "¿Hablamos de tu instalación?",
  text = "Te visitamos, analizamos los riesgos reales y te proponemos solo lo que necesitas. Valoración gratuita y sin compromiso.",
}: {
  title?: string;
  text?: string;
}) {
  return (
    <section className="border-t border-border px-6 py-20" aria-labelledby="cta">
      <Reveal>
        <div className="mx-auto max-w-4xl rounded-2xl border border-border bg-card p-8 text-center md:p-12">
          <h2 id="cta" className="text-3xl font-semibold tracking-tight">
            {title}
          </h2>
          <p className="mx-auto mt-4 max-w-2xl text-muted-foreground">{text}</p>
          <div className="mt-8 flex flex-wrap justify-center gap-3">
            <Link
              to="/contacto"
              className="inline-flex min-h-11 items-center rounded-md bg-primary px-5 text-sm font-medium text-primary-foreground transition-colors hover:bg-primary/90"
            >
              Pedir valoración gratuita
            </Link>
            <a
              href={site.phoneHref}
              className="inline-flex min-h-11 items-center gap-2 rounded-md border border-border px-5 text-sm font-medium transition-colors hover:bg-accent"
            >
              <Phone className="size-4" aria-hidden="true" />
              {site.phone} · 24 h
            </a>
          </div>
        </div>
      </Reveal>
    </section>
  );
}
