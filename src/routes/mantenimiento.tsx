import { createFileRoute } from "@tanstack/react-router";
import { CalendarClock, ClipboardCheck, LifeBuoy, Timer, Wrench, Zap } from "lucide-react";

import { CtaSection } from "@/components/CtaSection";
import { FeatureGrid } from "@/components/FeatureGrid";
import { PageHero } from "@/components/PageHero";
import { pageMeta } from "@/lib/site";

export const Route = createFileRoute("/mantenimiento")({
  head: () =>
    pageMeta({
      title: "Mantenimiento de sistemas de seguridad | Control 61",
      description:
        "Contratos de mantenimiento preventivo y correctivo de alarmas, CCTV, incendio y accesos para empresas, comunidades, urbanizaciones e instituciones en Murcia.",
      path: "/mantenimiento",
    }),
  component: MantenimientoPage,
});

const items = [
  {
    icon: CalendarClock,
    title: "Mantenimiento preventivo",
    text: "Revisiones programadas de sensores, cámaras, baterías, sirenas y comunicaciones.",
  },
  {
    icon: Wrench,
    title: "Mantenimiento correctivo",
    text: "Reparación y sustitución de equipos con repuestos compatibles con tu instalación.",
  },
  {
    icon: ClipboardCheck,
    title: "Revisiones legales al día",
    text: "Actas y documentación de las revisiones obligatorias, listas para cualquier inspección.",
  },
  {
    icon: Timer,
    title: "Tiempos de respuesta acordados",
    text: "Prioridad de atención definida por contrato, sin depender de la improvisación.",
  },
  {
    icon: Zap,
    title: "Averías urgentes 24 h",
    text: "Un teléfono que responde cuando el sistema falla fuera del horario de oficina.",
  },
  {
    icon: LifeBuoy,
    title: "Nos hacemos cargo de sistemas de otros",
    text: "Auditamos la instalación existente y asumimos su mantenimiento cuando es viable.",
  },
] as const;

function MantenimientoPage() {
  return (
    <>
      <PageHero
        eyebrow="Mantenimiento"
        title="Un sistema sin mantenimiento es una falsa sensación de seguridad"
        text="Empresas, comunidades, urbanizaciones e instituciones: mantenemos la instalación operativa y la documentación en orden."
        image="/servicio-mantenimiento.jpg"
        imageAlt="Técnico revisando el cuadro de una central de alarma"
      />
      <FeatureGrid id="mantenimiento-servicios" heading="Qué cubre el contrato" items={items} />
      <CtaSection
        title="Pide una revisión de tu instalación"
        text="Te decimos en qué estado está, qué falla y qué mantenimiento necesita realmente."
      />
    </>
  );
}
