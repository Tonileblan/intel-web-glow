import { createFileRoute } from "@tanstack/react-router";
import { Bell, DoorOpen, Home, KeyRound, Smartphone, Trees } from "lucide-react";

import { CtaSection } from "@/components/CtaSection";
import { FeatureGrid } from "@/components/FeatureGrid";
import { PageHero } from "@/components/PageHero";
import { Reveal } from "@/components/Reveal";
import { pageMeta } from "@/lib/site";

export const Route = createFileRoute("/hogar")({
  head: () =>
    pageMeta({
      title: "Alarmas para viviendas y urbanizaciones | Control 61",
      description:
        "Alarmas conectadas, videovigilancia y control de accesos para viviendas, comunidades y urbanizaciones en Murcia. Sin contratos abusivos.",
      path: "/hogar",
    }),
  component: HogarPage,
});

const items = [
  {
    icon: Home,
    title: "Alarma para vivienda",
    text: "Detección de intrusión con verificación, avisos al móvil y sirena interior y exterior.",
  },
  {
    icon: Smartphone,
    title: "Control desde el móvil",
    text: "Arma, desarma y consulta el estado de tu casa desde cualquier lugar.",
  },
  {
    icon: Trees,
    title: "Urbanizaciones y comunidades",
    text: "Videovigilancia de accesos, zonas comunes, piscina y aparcamiento con uso conforme al RGPD.",
  },
  {
    icon: KeyRound,
    title: "Control de accesos comunitario",
    text: "Mandos, tarjetas o móvil para vecinos, con altas y bajas gestionadas sin cambiar cerraduras.",
  },
  {
    icon: DoorOpen,
    title: "Videoportero y automatismos",
    text: "Puertas de garaje y accesos peatonales integrados con el sistema de seguridad.",
  },
  {
    icon: Bell,
    title: "Aviso de averías 24 h",
    text: "Si algo falla, atendemos la incidencia sin esperar al horario de oficina.",
  },
] as const;

function HogarPage() {
  return (
    <>
      <PageHero
        eyebrow="Hogar y urbanizaciones"
        title="Tranquilidad en casa y en tu comunidad"
        text="Instalaciones honestas y dimensionadas: pagas por lo que realmente protege tu vivienda o tu urbanización."
        image="/servicio-hogar.jpg"
        imageAlt="Salón de una vivienda al atardecer con teclado de alarma integrado"
      />
      <FeatureGrid
        id="hogar-servicios"
        heading="Soluciones para particulares y comunidades"
        items={items}
      />
      <section className="border-y border-border px-6 py-20" aria-labelledby="urbanizaciones">
        <div className="mx-auto grid max-w-6xl items-center gap-10 md:grid-cols-2">
          <Reveal>
            <img
              src="/servicio-urbanizaciones.jpg"
              alt="Acceso controlado de una urbanización al atardecer"
              width={1920}
              height={1080}
              loading="lazy"
              className="rounded-2xl border border-border object-cover"
            />
          </Reveal>
          <Reveal delay={0.1}>
            <h2 id="urbanizaciones" className="text-3xl font-semibold tracking-tight">
              Urbanizaciones sin sorpresas en la junta
            </h2>
            <p className="mt-4 text-muted-foreground">
              Preparamos propuestas comprensibles para presentar a los vecinos, con el alcance, el
              coste de mantenimiento y las obligaciones legales de la videovigilancia explicadas en
              lenguaje claro.
            </p>
            <ul className="mt-6 space-y-2 text-sm text-muted-foreground">
              <li>· Cartelería y registro de tratamiento conforme al RGPD.</li>
              <li>· Cámaras orientadas solo a zonas comunes de la comunidad.</li>
              <li>· Gestión de accesos con altas y bajas de vecinos.</li>
              <li>· Contrato de mantenimiento con revisiones programadas.</li>
            </ul>
          </Reveal>
        </div>
      </section>
      <CtaSection />
    </>
  );
}
