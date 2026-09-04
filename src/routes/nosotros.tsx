import { createFileRoute } from "@tanstack/react-router";
import { HandshakeIcon, Compass, Users } from "lucide-react";

import { Counter } from "@/components/Counter";
import { CtaSection } from "@/components/CtaSection";
import { PageHero } from "@/components/PageHero";
import { Reveal } from "@/components/Reveal";
import { pageMeta, site } from "@/lib/site";

export const Route = createFileRoute("/nosotros")({
  head: () =>
    pageMeta({
      title: "Sobre Control 61 — Expertos en tranquilidad",
      description:
        "Más de 20 años instalando y manteniendo sistemas de seguridad en la Región de Murcia. Soluciones honestas, sin trucos ni contratos a largo plazo.",
      path: "/nosotros",
    }),
  component: NosotrosPage,
});

const values = [
  {
    icon: HandshakeIcon,
    title: "Sin trucos ni contratos atrapa",
    text: "Presupuestos claros y permanencias razonables. Si algo no te hace falta, te lo decimos.",
  },
  {
    icon: Compass,
    title: "Soluciones a medida",
    text: "Cada instalación parte de una visita y un análisis de riesgo, no de un paquete cerrado.",
  },
  {
    icon: Users,
    title: "Equipo propio",
    text: "Técnicos formados de la casa, que conocen tu instalación y te atienden por su nombre.",
  },
] as const;

function NosotrosPage() {
  return (
    <>
      <PageHero
        eyebrow="Nosotros"
        title={`Somos ${site.legalName}, y trabajamos como ${site.brand}`}
        text="Más de dos décadas protegiendo empresas, instituciones y hogares en la Región de Murcia, con experiencia previa en seguridad y aplicación de la ley."
        image="/hero-control-room.jpg"
        imageAlt="Centro de control de seguridad con monitores encendidos"
      />

      <section className="border-b border-border px-6 py-16" aria-labelledby="cifras">
        <div className="mx-auto max-w-6xl">
          <h2 id="cifras" className="sr-only">
            Cifras de Control 61
          </h2>
          <dl className="grid gap-8 sm:grid-cols-3">
            {site.stats.map((stat) => (
              <div key={stat.label}>
                <dt className="text-4xl font-semibold text-primary">
                  <Counter value={stat.value} prefix={stat.prefix} />
                </dt>
                <dd className="mt-1 text-sm text-muted-foreground">{stat.label}</dd>
              </div>
            ))}
          </dl>
        </div>
      </section>

      <section className="px-6 py-20" aria-labelledby="valores">
        <div className="mx-auto max-w-6xl">
          <Reveal>
            <h2 id="valores" className="text-3xl font-semibold tracking-tight">
              Cómo entendemos la seguridad
            </h2>
          </Reveal>
          <ul className="mt-10 grid gap-6 md:grid-cols-3">
            {values.map((value, i) => (
              <Reveal key={value.title} delay={i * 0.08}>
                <li className="h-full rounded-xl border border-border bg-card p-6">
                  <value.icon className="size-6 text-primary" aria-hidden="true" />
                  <h3 className="mt-4 text-lg font-medium">{value.title}</h3>
                  <p className="mt-2 text-sm text-muted-foreground">{value.text}</p>
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
