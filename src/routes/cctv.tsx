import { createFileRoute } from "@tanstack/react-router";
import { Camera, Eye, HardDrive, ScanSearch, Scale, Sun } from "lucide-react";

import { CtaSection } from "@/components/CtaSection";
import { FeatureGrid } from "@/components/FeatureGrid";
import { PageHero } from "@/components/PageHero";
import { pageMeta } from "@/lib/site";

export const Route = createFileRoute("/cctv")({
  head: () =>
    pageMeta({
      title: "CCTV y videovigilancia en Murcia | Control 61",
      description:
        "Instalación de CCTV en Murcia: cámaras de alta resolución, grabación segura, búsqueda inteligente de vídeo y cumplimiento del RGPD.",
      path: "/cctv",
    }),
  component: CctvPage,
});

const items = [
  {
    icon: Camera,
    title: "Cámaras de alta resolución",
    text: "Óptica y ubicación elegidas para que la imagen sirva realmente como prueba.",
  },
  {
    icon: Sun,
    title: "Visión nocturna y exteriores",
    text: "Equipos preparados para contraluces, lluvia y las temperaturas del sureste.",
  },
  {
    icon: ScanSearch,
    title: "Búsqueda inteligente de vídeo",
    text: "Localiza en segundos un evento por zona, movimiento o intervalo, sin revisar horas de grabación.",
  },
  {
    icon: HardDrive,
    title: "Grabación y retención segura",
    text: "Almacenamiento dimensionado al plazo de conservación que necesitas.",
  },
  {
    icon: Eye,
    title: "Acceso remoto controlado",
    text: "Visualización desde móvil u ordenador con permisos por usuario.",
  },
  {
    icon: Scale,
    title: "Cumplimiento RGPD",
    text: "Cartelería, zonas permitidas y registro de tratamiento para que la instalación sea legal.",
  },
] as const;

function CctvPage() {
  return (
    <>
      <PageHero
        eyebrow="Videovigilancia"
        title="CCTV que sirve cuando de verdad hace falta"
        text="No basta con instalar cámaras: hay que colocarlas bien, conservar la grabación el tiempo correcto y poder encontrar el momento exacto."
        image="/hero-control-room.jpg"
        imageAlt="Centro de control con múltiples monitores de videovigilancia"
      />
      <FeatureGrid id="cctv-servicios" heading="Qué incluye una instalación bien hecha" items={items} />
      <CtaSection
        title="Revisamos gratis tu instalación actual"
        text="Si ya tienes cámaras, comprobamos cobertura, calidad de imagen, retención y cumplimiento legal."
      />
    </>
  );
}
