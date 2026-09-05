import { createFileRoute } from "@tanstack/react-router";

import { CtaSection } from "@/components/CtaSection";
import { PageHero } from "@/components/PageHero";
import { Reveal } from "@/components/Reveal";
import selloRea from "@/assets/Registro-de-Empresas-Acreditadas.png";
import selloRina from "@/assets/Rina-Iso2-1.png";
import { pageMeta } from "@/lib/site";

export const Route = createFileRoute("/acreditaciones")({
  head: () =>
    pageMeta({
      title: "Certificaciones y acreditaciones | Control 61",
      description:
        "Empresa certificada en ISO 9001, ISO 14001 e ISO 45001 por RINA, acreditada en el REA, inscrita en Industria y en el Registro de Seguridad Privada.",
      path: "/acreditaciones",
    }),
  component: AcreditacionesPage,
});

const blocks = [
  {
    title: "ISO 9001, ISO 14001 e ISO 45001",
    issuer: "RINA — miembro de CISQ Federation y de la red IQNet",
    benefit:
      "Procesos auditados por una entidad independiente en calidad, gestión ambiental y seguridad y salud laboral. Para ti significa instalaciones trazables, incidencias registradas y un equipo que trabaja con procedimientos escritos.",
    image: selloRina,
    imageAlt: "Sello de certificación RINA para ISO 9001, ISO 14001 e ISO 45001",
  },
  {
    title: "Empresa acreditada en el REA",
    issuer: "Registro de Empresas Acreditadas — Ministerio de Trabajo",
    benefit:
      "Podemos ejecutar trabajos en obras de construcción cumpliendo la ley de subcontratación. Es requisito habitual para contratistas, promotoras y administraciones.",
    image: selloRea,
    imageAlt: "Sello del Registro de Empresas Acreditadas del Gobierno de España",
  },
  {
    title: "Inscripción en Industria",
    issuer: "Registro de empresas instaladoras y mantenedoras",
    benefit:
      "Habilitación para instalar y mantener sistemas de protección contra incendios, con la documentación y los certificados que exige la normativa.",
  },
  {
    title: "Registro de Seguridad Privada",
    issuer: "Ministerio del Interior",
    benefit:
      "Empresa inscrita para el ejercicio de actividades de seguridad privada, con las obligaciones y controles que ello implica.",
  },
] as const;

function AcreditacionesPage() {
  return (
    <>
      <PageHero
        eyebrow="Acreditaciones"
        title="Certificados que puedes comprobar antes de contratarnos"
        text="No son adornos: cada acreditación habilita trabajos concretos y garantiza cómo los ejecutamos."
      />

      <section className="px-6 py-20" aria-labelledby="acreditaciones-detalle">
        <div className="mx-auto max-w-6xl">
          <h2 id="acreditaciones-detalle" className="sr-only">
            Detalle de certificaciones y registros
          </h2>
          <ul className="grid gap-6 md:grid-cols-2">
            {blocks.map((block, i) => (
              <Reveal key={block.title} delay={i * 0.06}>
                <li className="flex h-full flex-col rounded-xl border border-border bg-card p-6">
                  {"image" in block && block.image ? (
                    <img
                      src={block.image}
                      alt={block.imageAlt}
                      loading="lazy"
                      className="mb-5 h-24 w-auto self-start rounded bg-white/95 p-2"
                    />
                  ) : null}
                  <h3 className="text-lg font-medium">{block.title}</h3>
                  <p className="mt-1 text-sm font-medium text-primary">{block.issuer}</p>
                  <p className="mt-3 text-sm text-muted-foreground">{block.benefit}</p>
                </li>
              </Reveal>
            ))}
          </ul>
          <p className="mt-10 text-sm text-muted-foreground">
            Números de certificado, alcance exacto y fechas de vigencia se facilitan a petición,
            junto con el documento original emitido por cada organismo.
          </p>
        </div>
      </section>

      <CtaSection
        title="¿Necesitas nuestra documentación para un expediente?"
        text="Te enviamos certificados, seguros y alta en registros en el formato que necesites."
      />
    </>
  );
}
