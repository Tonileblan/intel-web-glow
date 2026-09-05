import { createFileRoute } from "@tanstack/react-router";
import {
  ShieldCheck,
  Target,
  Users,
  Handshake,
  Clock,
  Award,
  Sparkles,
  CheckCircle2,
  Lock,
} from "lucide-react";

import { Counter } from "@/components/Counter";
import { CtaSection } from "@/components/CtaSection";
import { PageHero } from "@/components/PageHero";
import { Reveal } from "@/components/Reveal";
import { pageMeta, site } from "@/lib/site";

export const Route = createFileRoute("/nosotros")({
  head: () =>
    pageMeta({
      title: "Misión, Valores y Compromiso | Control 61",
      description:
        "Conoce la misión y valores de Control 61. Más de 20 años protegiendo hogares, empresas e instituciones en la Región de Murcia con honestidad, rigor e innovación.",
      path: "/nosotros",
    }),
  component: NosotrosPage,
});

const pillars = [
  {
    title: "Nuestra Misión",
    description:
      "Garantizar la tranquilidad y protección de nuestros clientes a través de ingeniería de seguridad avanzada, asesoramiento honesto y un servicio técnico cercano e inmediato. Existimos para ofrecer seguridad real y duradera, sin ataduras artificiales ni falsas promesas.",
    icon: Target,
  },
  {
    title: "Nuestra Visión",
    description:
      "Ser el referente de confianza e innovación en sistemas de seguridad y protección integral en el sureste español, reconocidos por nuestra excelencia técnica, ética profesional y el trato humano directo de nuestro equipo.",
    icon: Sparkles,
  },
] as const;

const values = [
  {
    icon: ShieldCheck,
    title: "Honestidad y Transparencia",
    text: "Presupuestos claros y sin sorpresas. Si algo no es estrictamente necesario para proteger tu espacio, te lo decimos con total franqueza.",
  },
  {
    icon: Handshake,
    title: "Soluciones a Medida",
    text: "Cada instalación nace de un estudio de riesgo personalizado. No creemos en paquetes genéricos cerrados ni en soluciones estándar.",
  },
  {
    icon: Users,
    title: "Equipo Propio y Cualificado",
    text: "Técnicos e ingenieros en plantilla con amplia experiencia en seguridad, formados continuamente para atenderte con nombre y apellidos.",
  },
  {
    icon: Clock,
    title: "Compromiso y Respuesta Ágil",
    text: "La seguridad es un servicio continuo. Acompañamos cada proyecto con soporte técnico 24/7 y mantenimientos preventivos rigurosos.",
  },
  {
    icon: Award,
    title: "Rigor Técnico y Calidad Certificada",
    text: "Trabajamos bajo los más altos estándares normativos e ISO (9001, 14001, 45001), empleando tecnología homologada de máxima fiabilidad.",
  },
  {
    icon: Lock,
    title: "Confidencialidad y Rigor",
    text: "Tratamos cada proyecto y sus protocolos de seguridad con la máxima discreción, rigor normativo y protección de datos.",
  },
] as const;

const commitments = [
  "Más de 20 años de experiencia técnica acumulada en protección integral.",
  "Atención directa y personalizada, sin intermediarios ni plataformas impersonales.",
  "Tecnología de vanguardia con homologación y grado de seguridad certificado.",
  "Auditoría previa y asesoramiento técnico sobre el terreno sin compromiso.",
];

function NosotrosPage() {
  return (
    <>
      <PageHero
        eyebrow="Nuestra Misión y Valores"
        title="Garantizar tu tranquilidad: la vocación que define cada uno de nuestros proyectos"
        text="Creemos en una seguridad honesta, rigurosa y cercana. Desde hace más de dos décadas protegemos empresas, instituciones y hogares en la Región de Murcia combinando tecnología de vanguardia y un equipo humano con vocación de servicio."
        image="/hero-control-room.jpg"
        imageAlt="Centro de control y monitorización de sistemas de seguridad"
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

      <section className="border-b border-border px-6 py-20" aria-labelledby="mision-vision">
        <div className="mx-auto max-w-6xl">
          <Reveal>
            <div className="max-w-2xl">
              <p className="text-xs font-semibold uppercase tracking-[0.2em] text-primary">
                Propósito
              </p>
              <h2 id="mision-vision" className="mt-3 text-3xl font-semibold tracking-tight sm:text-4xl">
                Nuestra razón de ser
              </h2>
            </div>
          </Reveal>
          <div className="mt-12 grid gap-8 md:grid-cols-2">
            {pillars.map((pillar, i) => (
              <Reveal key={pillar.title} delay={i * 0.1}>
                <div className="relative flex h-full flex-col justify-between rounded-2xl border border-border bg-gradient-to-br from-card to-card/60 p-8 shadow-sm transition-all hover:border-primary/40">
                  <div>
                    <div className="inline-flex size-12 items-center justify-center rounded-xl bg-primary/10 text-primary">
                      <pillar.icon className="size-6" aria-hidden="true" />
                    </div>
                    <h3 className="mt-6 text-xl font-semibold">{pillar.title}</h3>
                    <p className="mt-3 text-base leading-relaxed text-muted-foreground">
                      {pillar.description}
                    </p>
                  </div>
                </div>
              </Reveal>
            ))}
          </div>
        </div>
      </section>

      <section className="px-6 py-20" aria-labelledby="valores">
        <div className="mx-auto max-w-6xl">
          <Reveal>
            <div className="max-w-2xl">
              <p className="text-xs font-semibold uppercase tracking-[0.2em] text-primary">
                Nuestros Valores
              </p>
              <h2 id="valores" className="mt-3 text-3xl font-semibold tracking-tight sm:text-4xl">
                Los principios que guían cada instalación
              </h2>
              <p className="mt-4 text-muted-foreground">
                No vendemos paquetes cerrados ni contratos opacos: construimos relaciones de confianza a largo plazo
                basadas en el rigor técnico, la transparencia y el servicio constante.
              </p>
            </div>
          </Reveal>
          <ul className="mt-12 grid gap-6 sm:grid-cols-2 lg:grid-cols-3">
            {values.map((value, i) => (
              <Reveal key={value.title} delay={i * 0.06}>
                <li className="flex h-full flex-col rounded-xl border border-border bg-card p-6 transition-colors hover:border-primary/30">
                  <div className="inline-flex size-10 items-center justify-center rounded-lg bg-primary/10 text-primary">
                    <value.icon className="size-5" aria-hidden="true" />
                  </div>
                  <h3 className="mt-4 text-lg font-medium">{value.title}</h3>
                  <p className="mt-2 text-sm leading-relaxed text-muted-foreground">
                    {value.text}
                  </p>
                </li>
              </Reveal>
            ))}
          </ul>
        </div>
      </section>

      <section className="border-t border-border bg-muted/30 px-6 py-16" aria-labelledby="compromiso">
        <div className="mx-auto max-w-6xl">
          <div className="grid items-center gap-8 lg:grid-cols-2">
            <Reveal>
              <div>
                <p className="text-xs font-semibold uppercase tracking-[0.2em] text-primary">
                  Compromiso
                </p>
                <h2 id="compromiso" className="mt-2 text-2xl font-semibold tracking-tight sm:text-3xl">
                  Seguridad técnica con vocación de servicio
                </h2>
                <p className="mt-4 text-sm leading-relaxed text-muted-foreground">
                  Entendemos la seguridad como la base para vivir y trabajar con serenidad.
                  Por eso, cada uno de nuestros proyectos se ejecuta con la máxima exigencia técnica y normativa,
                  respaldado por certificaciones oficiales y un soporte humano incondicional.
                </p>
              </div>
            </Reveal>
            <Reveal delay={0.1}>
              <div className="rounded-xl border border-border bg-card p-6">
                <h3 className="text-base font-semibold">Lo que garantizamos siempre:</h3>
                <ul className="mt-4 space-y-3">
                  {commitments.map((item) => (
                    <li key={item} className="flex items-start gap-3 text-sm text-muted-foreground">
                      <CheckCircle2 className="mt-0.5 size-4 shrink-0 text-primary" aria-hidden="true" />
                      <span>{item}</span>
                    </li>
                  ))}
                </ul>
              </div>
            </Reveal>
          </div>
        </div>
      </section>

      <CtaSection
        title="¿Quieres conocer cómo podemos proteger tu espacio?"
        text="Solicita una valoración técnica gratuita. Evaluamos tus necesidades y te asesoramos sin ningún compromiso."
      />
    </>
  );
}
