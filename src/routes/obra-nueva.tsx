import { createFileRoute } from "@tanstack/react-router";
import { Cable, FileCheck2, HardHat, Layers, Ruler, Wrench } from "lucide-react";

import { CtaSection } from "@/components/CtaSection";
import { FeatureGrid } from "@/components/FeatureGrid";
import { PageHero } from "@/components/PageHero";
import { pageMeta } from "@/lib/site";

export const Route = createFileRoute("/obra-nueva")({
  head: () =>
    pageMeta({
      title: "Seguridad en obra nueva y reformas | Control 61",
      description:
        "Proyecto e instalación de seguridad en obra nueva y renovaciones: previsión de canalizaciones, protección de obra y legalización de la instalación.",
      path: "/obra-nueva",
    }),
  component: ObraNuevaPage,
});

const items = [
  {
    icon: Ruler,
    title: "Proyecto desde el plano",
    text: "Definimos ubicaciones y necesidades antes de cerrar tabiques y falsos techos.",
  },
  {
    icon: Cable,
    title: "Previsión de canalizaciones",
    text: "Tubos y cableado previstos en obra: menos coste y ninguna instalación a la vista.",
  },
  {
    icon: HardHat,
    title: "Protección durante la obra",
    text: "Videovigilancia temporal frente a robos de material y cobre en fase de ejecución.",
  },
  {
    icon: Layers,
    title: "Coordinación con oficios",
    text: "Trabajamos junto a electricista, climatización y telecomunicaciones sin pisar plazos.",
  },
  {
    icon: FileCheck2,
    title: "Legalización y certificados",
    text: "Entregamos la documentación necesaria para licencias y primera ocupación.",
  },
  {
    icon: Wrench,
    title: "Mantenimiento desde el día uno",
    text: "La instalación entra directamente en plan de revisiones al entregar la obra.",
  },
] as const;

function ObraNuevaPage() {
  return (
    <>
      <PageHero
        eyebrow="Obra nueva y reformas"
        title="La seguridad sale mucho mejor si se piensa en obra"
        text="Intervenir en fase de proyecto evita rozas posteriores, cables vistos y sistemas mal ubicados."
        image="/servicio-obra.jpg"
        imageAlt="Edificio en construcción iluminado al anochecer"
      />
      <FeatureGrid id="obra-servicios" heading="Cómo intervenimos en obra" items={items} />
      <CtaSection
        title="¿Tienes una obra en marcha?"
        text="Revisamos el proyecto y te decimos qué prever ahora para no pagarlo el doble después."
      />
    </>
  );
}
