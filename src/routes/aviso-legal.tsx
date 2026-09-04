import { createFileRoute } from "@tanstack/react-router";

import { PageHero } from "@/components/PageHero";
import { pageMeta, site } from "@/lib/site";

export const Route = createFileRoute("/aviso-legal")({
  head: () =>
    pageMeta({
      title: "Aviso legal | Control 61",
      description:
        "Información legal y condiciones de uso del sitio web de Control 61 (Desarrollos y Sistemas Inteligentes S.L.).",
      path: "/aviso-legal",
    }),
  component: AvisoLegalPage,
});

function AvisoLegalPage() {
  return (
    <>
      <PageHero
        eyebrow="Legal"
        title="Aviso legal"
        text="Información sobre el titular de este sitio web y las condiciones de uso."
      >
        <div />
      </PageHero>
      <section className="px-6 py-16">
        <div className="mx-auto max-w-3xl space-y-8 text-sm leading-relaxed text-muted-foreground">
          <div>
            <h2 className="text-xl font-medium text-foreground">Titular del sitio</h2>
            <p className="mt-3">
              Denominación social: {site.legalName}, que opera comercialmente como{" "}
              {site.brand}.
            </p>
            <p className="mt-2">Domicilio: {site.address}</p>
            <p className="mt-2">
              Teléfono: {site.phone} · Email: {site.email}
            </p>
            <p className="mt-2">
              CIF y datos de inscripción en el Registro Mercantil: pendientes de
              confirmación por el titular antes de la publicación definitiva.
            </p>
          </div>
          <div>
            <h2 className="text-xl font-medium text-foreground">Objeto</h2>
            <p className="mt-3">
              Este sitio web tiene por finalidad informar sobre los servicios de
              instalación y mantenimiento de sistemas de seguridad que presta el titular,
              así como facilitar el contacto con clientes actuales y potenciales.
            </p>
          </div>
          <div>
            <h2 className="text-xl font-medium text-foreground">Condiciones de uso</h2>
            <p className="mt-3">
              El acceso a este sitio es gratuito y supone la aceptación de este aviso
              legal. El usuario se compromete a utilizar el sitio y sus contenidos de forma
              conforme a la ley, la buena fe y el orden público, y a no emplearlos con
              fines ilícitos o que puedan dañar los derechos del titular o de terceros.
            </p>
          </div>
          <div>
            <h2 className="text-xl font-medium text-foreground">Propiedad intelectual</h2>
            <p className="mt-3">
              Los textos, marcas, logotipos, imágenes y demás elementos de este sitio son
              titularidad del titular o de sus legítimos propietarios y están protegidos
              por la normativa de propiedad intelectual e industrial. No se permite su
              reproducción, distribución o transformación sin autorización expresa.
            </p>
          </div>
          <div>
            <h2 className="text-xl font-medium text-foreground">Responsabilidad</h2>
            <p className="mt-3">
              El titular procura que la información publicada sea correcta y actualizada,
              pero no garantiza la ausencia de errores ni la disponibilidad ininterrumpida
              del servicio. Los enlaces a sitios de terceros se ofrecen únicamente a título
              informativo.
            </p>
          </div>
          <div>
            <h2 className="text-xl font-medium text-foreground">
              Legislación aplicable
            </h2>
            <p className="mt-3">
              Este aviso legal se rige por la legislación española. Para cualquier
              controversia serán competentes los juzgados y tribunales que correspondan
              conforme a la normativa vigente.
            </p>
          </div>
        </div>
      </section>
    </>
  );
}
