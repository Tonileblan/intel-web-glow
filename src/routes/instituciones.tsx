import { createFileRoute } from "@tanstack/react-router";
import { Building, CalendarCheck, FileCheck2, Landmark, Library, Users } from "lucide-react";

import { CtaSection } from "@/components/CtaSection";
import { FeatureGrid } from "@/components/FeatureGrid";
import { PageHero } from "@/components/PageHero";
import { pageMeta } from "@/lib/site";

export const Route = createFileRoute("/instituciones")({
  head: () =>
    pageMeta({
      title: "Seguridad para ayuntamientos e instituciones | Control 61",
      description:
        "Videovigilancia, control de accesos y mantenimiento para ayuntamientos, edificios públicos, instalaciones municipales y eventos en la Región de Murcia.",
      path: "/instituciones",
    }),
  component: InstitucionesPage,
});

const items = [
  {
    icon: Landmark,
    title: "Ayuntamientos y dependencias municipales",
    text: "Protección de oficinas de atención, archivos y accesos restringidos con registro auditable.",
  },
  {
    icon: Building,
    title: "Edificios e instalaciones públicas",
    text: "Polideportivos, centros culturales, almacenes municipales y naves de servicios.",
  },
  {
    icon: Library,
    title: "Patrimonio y espacios culturales",
    text: "Soluciones discretas que protegen el bien sin alterar su estética ni su conservación.",
  },
  {
    icon: CalendarCheck,
    title: "Eventos y actos públicos",
    text: "Refuerzo temporal de videovigilancia y control de aforo para fiestas y actos municipales.",
  },
  {
    icon: FileCheck2,
    title: "Cumplimiento y licitaciones",
    text: "Documentación técnica, certificados e ISO al día para presentarnos a procedimientos públicos.",
  },
  {
    icon: Users,
    title: "Formación al personal",
    text: "Dejamos a los responsables municipales operando el sistema con soltura.",
  },
] as const;

function InstitucionesPage() {
  return (
    <>
      <PageHero
        eyebrow="Instituciones y administraciones públicas"
        title="Hemos trabajado para ayuntamientos y edificios públicos"
        text="Conocemos los plazos, la documentación y las exigencias del sector público. Proyectos ejecutados con empresa acreditada y certificada."
        image="/servicio-instituciones.jpg"
        imageAlt="Fachada de un edificio municipal español iluminado al anochecer"
      />
      <FeatureGrid
        id="instituciones-servicios"
        heading="Ámbitos en los que intervenimos"
        items={items}
      />
      <CtaSection
        title="¿Preparando un pliego o una mejora de instalaciones?"
        text="Podemos ayudarte con el alcance técnico, la valoración y la documentación necesaria."
      />
    </>
  );
}
