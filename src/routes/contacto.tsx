import { createFileRoute } from "@tanstack/react-router";
import { Clock, Mail, MapPin, Phone } from "lucide-react";

import { PageHero } from "@/components/PageHero";
import { Reveal } from "@/components/Reveal";
import { pageMeta, site } from "@/lib/site";

export const Route = createFileRoute("/contacto")({
  head: () =>
    pageMeta({
      title: "Contacto y valoración gratuita | Control 61",
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
        eyebrow="Contacto"
        title="Cuéntanos qué quieres proteger"
        text="Te visitamos, analizamos los riesgos y te damos una propuesta clara. Valoración gratuita y sin compromiso."
      >
        <div className="mt-8 flex flex-wrap gap-3">
          <a
            href={site.phoneHref}
            className="inline-flex min-h-11 items-center gap-2 rounded-md bg-primary px-5 text-sm font-medium text-primary-foreground transition-colors hover:bg-primary/90"
          >
            <Phone className="size-4" aria-hidden="true" />
            {site.phone}
          </a>
          <a
            href={`mailto:${site.email}`}
            className="inline-flex min-h-11 items-center gap-2 rounded-md border border-border px-5 text-sm font-medium transition-colors hover:bg-accent"
          >
            <Mail className="size-4" aria-hidden="true" />
            {site.email}
          </a>
        </div>
      </PageHero>

      <section className="px-6 py-20" aria-labelledby="formulario">
        <div className="mx-auto grid max-w-6xl gap-12 md:grid-cols-[1.2fr_1fr]">
          <Reveal>
            <h2 id="formulario" className="text-3xl font-semibold tracking-tight">
              Solicitar valoración gratuita
            </h2>
            <p className="mt-3 text-muted-foreground">
              Rellena los datos y te llamamos para concretar la visita.
            </p>
            <form className="mt-8 grid gap-4">
              <div className="grid gap-4 sm:grid-cols-2">
                <label className="grid gap-2 text-sm">
                  Nombre
                  <input
                    name="nombre"
                    required
                    autoComplete="name"
                    className="min-h-11 rounded-md border border-input bg-background px-3 text-sm outline-none focus:border-primary"
                  />
                </label>
                <label className="grid gap-2 text-sm">
                  Teléfono
                  <input
                    name="telefono"
                    type="tel"
                    required
                    autoComplete="tel"
                    className="min-h-11 rounded-md border border-input bg-background px-3 text-sm outline-none focus:border-primary"
                  />
                </label>
              </div>
              <label className="grid gap-2 text-sm">
                Email
                <input
                  name="email"
                  type="email"
                  autoComplete="email"
                  className="min-h-11 rounded-md border border-input bg-background px-3 text-sm outline-none focus:border-primary"
                />
              </label>
              <label className="grid gap-2 text-sm">
                Tipo de instalación
                <select
                  name="tipo"
                  className="min-h-11 rounded-md border border-input bg-background px-3 text-sm outline-none focus:border-primary"
                >
                  <option>Empresa, nave o comercio</option>
                  <option>Institución o administración pública</option>
                  <option>Vivienda</option>
                  <option>Comunidad o urbanización</option>
                  <option>Mantenimiento de una instalación existente</option>
                </select>
              </label>
              <label className="grid gap-2 text-sm">
                Cuéntanos brevemente
                <textarea
                  name="mensaje"
                  rows={5}
                  className="rounded-md border border-input bg-background p-3 text-sm outline-none focus:border-primary"
                />
              </label>
              <button
                type="submit"
                className="mt-2 inline-flex min-h-11 items-center justify-center rounded-md bg-primary px-5 text-sm font-medium text-primary-foreground transition-colors hover:bg-primary/90"
              >
                Enviar solicitud
              </button>
              <p className="text-xs text-muted-foreground">
                Envío pendiente de conexión: por ahora, contáctanos por teléfono o email.
              </p>
            </form>
          </Reveal>

          <Reveal delay={0.1}>
            <div className="rounded-2xl border border-border bg-card p-6">
              <h2 className="text-lg font-medium">Datos de contacto</h2>
              <ul className="mt-5 space-y-4 text-sm text-muted-foreground">
                <li className="flex gap-3">
                  <Phone className="mt-0.5 size-4 shrink-0 text-primary" aria-hidden="true" />
                  <a href={site.phoneHref} className="hover:text-foreground">
                    {site.phone}
                  </a>
                </li>
                <li className="flex gap-3">
                  <Mail className="mt-0.5 size-4 shrink-0 text-primary" aria-hidden="true" />
                  <a href={`mailto:${site.email}`} className="hover:text-foreground">
                    {site.email}
                  </a>
                </li>
                <li className="flex gap-3">
                  <MapPin className="mt-0.5 size-4 shrink-0 text-primary" aria-hidden="true" />
                  <span>{site.address}</span>
                </li>
                <li className="flex gap-3">
                  <Clock className="mt-0.5 size-4 shrink-0 text-primary" aria-hidden="true" />
                  <span>{site.schedule}</span>
                </li>
              </ul>
            </div>
          </Reveal>
        </div>
      </section>
    </>
  );
}
