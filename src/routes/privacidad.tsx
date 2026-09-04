import { createFileRoute } from "@tanstack/react-router";

import { PageHero } from "@/components/PageHero";
import { pageMeta, site } from "@/lib/site";

export const Route = createFileRoute("/privacidad")({
  head: () =>
    pageMeta({
      title: "Política de privacidad | Control 61",
      description:
        "Cómo trata Control 61 los datos personales de clientes y visitantes: finalidades, base jurídica, conservación y ejercicio de derechos.",
      path: "/privacidad",
    }),
  component: PrivacidadPage,
});

function PrivacidadPage() {
  return (
    <>
      <PageHero
        eyebrow="Legal"
        title="Política de privacidad"
        text="Información sobre el tratamiento de datos personales conforme al RGPD y a la LOPDGDD."
      >
        <div />
      </PageHero>
      <section className="px-6 py-16">
        <div className="mx-auto max-w-3xl space-y-8 text-sm leading-relaxed text-muted-foreground">
          <div>
            <h2 className="text-xl font-medium text-foreground">Responsable</h2>
            <p className="mt-3">
              {site.legalName} ({site.brand}), con domicilio en {site.address}. Contacto:{" "}
              {site.email} · {site.phone}.
            </p>
          </div>
          <div>
            <h2 className="text-xl font-medium text-foreground">
              Finalidades del tratamiento
            </h2>
            <ul className="mt-3 list-disc space-y-2 pl-5">
              <li>Atender solicitudes de información, presupuestos y visitas técnicas.</li>
              <li>Gestionar la relación contractual, instalaciones y mantenimientos.</li>
              <li>Cumplir obligaciones legales, fiscales y de seguridad privada.</li>
              <li>
                Enviar comunicaciones sobre nuestros servicios, cuando exista consentimiento
                o interés legítimo.
              </li>
            </ul>
          </div>
          <div>
            <h2 className="text-xl font-medium text-foreground">Base jurídica</h2>
            <p className="mt-3">
              El consentimiento del interesado, la ejecución de un contrato o
              precontractual, el cumplimiento de obligaciones legales y el interés legítimo
              del responsable, según cada finalidad.
            </p>
          </div>
          <div>
            <h2 className="text-xl font-medium text-foreground">Conservación</h2>
            <p className="mt-3">
              Los datos se conservan mientras se mantenga la relación y, después, durante
              los plazos legales de prescripción de responsabilidades. Las imágenes de
              sistemas de videovigilancia se conservan por el plazo legalmente previsto,
              salvo que deban mantenerse para acreditar un hecho.
            </p>
          </div>
          <div>
            <h2 className="text-xl font-medium text-foreground">Destinatarios</h2>
            <p className="mt-3">
              No se ceden datos a terceros salvo obligación legal o cuando sea necesario
              para prestar el servicio (por ejemplo, central receptora de alarmas o
              proveedores tecnológicos que actúan como encargados del tratamiento).
            </p>
          </div>
          <div>
            <h2 className="text-xl font-medium text-foreground">Derechos</h2>
            <p className="mt-3">
              Puedes ejercer los derechos de acceso, rectificación, supresión, limitación,
              portabilidad y oposición escribiendo a {site.email}, acreditando tu
              identidad. También puedes presentar una reclamación ante la Agencia Española
              de Protección de Datos.
            </p>
          </div>
        </div>
      </section>
    </>
  );
}
