import { createFileRoute } from "@tanstack/react-router";
import { AlarmSmoke, Camera, Fingerprint, Radar, ShieldCheck, Siren } from "lucide-react";

import { CtaSection } from "@/components/CtaSection";
import { FeatureGrid } from "@/components/FeatureGrid";
import { PageHero } from "@/components/PageHero";
import { pageMeta } from "@/lib/site";

export const Route = createFileRoute("/empresas")({
  head: () =>
    pageMeta({
      title: "Seguridad para empresas en Murcia | Control 61",
      description:
        "Sistemas de seguridad integrales para naves, comercios y oficinas en Murcia: intrusión, incendio, control de accesos, CCTV y monitorización 24 h.",
      path: "/empresas",
    }),
  component: EmpresasPage,
});

const items = [
  {
    icon: Siren,
    title: "Alarmas de intrusión",
    text: "Detección perimetral e interior con verificación por vídeo para evitar falsas alarmas y respuestas innecesarias.",
  },
  {
    icon: AlarmSmoke,
    title: "Protección contra incendios",
    text: "Detección temprana, sirenas y señalización instaladas por empresa inscrita en el registro de Industria.",
  },
  {
    icon: Fingerprint,
    title: "Control de accesos",
    text: "Quién entra, dónde y cuándo. Tarjetas, huella o móvil, con registro exportable para auditorías.",
  },
  {
    icon: Camera,
    title: "Videovigilancia CCTV",
    text: "Cámaras de alta resolución, grabación y búsqueda de eventos conforme al RGPD.",
  },
  {
    icon: Radar,
    title: "Monitorización remota",
    text: "Supervisión de tus instalaciones y avisos inmediatos ante cualquier incidencia.",
  },
  {
    icon: ShieldCheck,
    title: "Proyecto y legalización",
    text: "Documentación, planos y certificados para que la instalación cumpla desde el primer día.",
  },
] as const;

function EmpresasPage() {
  return (
    <>
      <PageHero
        eyebrow="Empresas"
        title="Seguridad integral para naves, comercios y oficinas"
        text="Un solo proveedor para proyectar, instalar y mantener toda la seguridad de tu empresa. Sin trucos ni contratos a largo plazo."
        image="/servicio-empresas.jpg"
        imageAlt="Nave industrial protegida con cámaras de videovigilancia al anochecer"
      />
      <FeatureGrid
        id="empresas-servicios"
        heading="Qué instalamos en tu empresa"
        intro="Diseñamos cada sistema según el riesgo real de tu actividad, tus turnos y tus procesos, no según un catálogo cerrado."
        items={items}
      />
      <section className="border-y border-border px-6 py-20" aria-labelledby="proceso">
        <div className="mx-auto max-w-6xl">
          <h2 id="proceso" className="text-3xl font-semibold tracking-tight">
            Cómo trabajamos
          </h2>
          <ol className="mt-10 grid gap-6 md:grid-cols-4">
            {[
              ["Visita y análisis", "Recorremos la instalación y detectamos puntos débiles."],
              [
                "Propuesta clara",
                "Un presupuesto sin partidas sorpresa y sin equipos innecesarios.",
              ],
              [
                "Instalación profesional",
                "Equipo propio, obra limpia y puesta en marcha con formación.",
              ],
              ["Mantenimiento", "Revisiones periódicas y asistencia ante averías durante 24 h."],
            ].map(([title, text], i) => (
              <li key={title} className="rounded-xl border border-border bg-card p-6">
                <span className="text-sm font-semibold text-primary">0{i + 1}</span>
                <h3 className="mt-3 font-medium">{title}</h3>
                <p className="mt-2 text-sm text-muted-foreground">{text}</p>
              </li>
            ))}
          </ol>
        </div>
      </section>
      <CtaSection />
    </>
  );
}
