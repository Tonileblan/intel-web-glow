import { createFileRoute } from "@tanstack/react-router";

import { PageHero } from "@/components/PageHero";
import { pageMeta, site } from "@/lib/site";

export const Route = createFileRoute("/cookies")({
  head: () =>
    pageMeta({
      title: "Política de cookies | Control 61",
      description:
        "Qué cookies utiliza el sitio web de Control 61, para qué sirven y cómo puedes configurarlas o eliminarlas desde tu navegador.",
      path: "/cookies",
    }),
  component: CookiesPage,
});

function CookiesPage() {
  return (
    <>
      <PageHero
        eyebrow="Legal"
        title="Política de cookies"
        text="Información sobre el uso de cookies y tecnologías similares en este sitio web."
      >
        <div />
      </PageHero>
      <section className="px-6 py-16">
        <div className="mx-auto max-w-3xl space-y-8 text-sm leading-relaxed text-muted-foreground">
          <div>
            <h2 className="text-xl font-medium text-foreground">Qué es una cookie</h2>
            <p className="mt-3">
              Una cookie es un pequeño archivo que se descarga en tu dispositivo al visitar una web
              y que permite almacenar y recuperar información sobre la navegación.
            </p>
          </div>
          <div>
            <h2 className="text-xl font-medium text-foreground">Cookies que usamos</h2>
            <ul className="mt-3 list-disc space-y-2 pl-5">
              <li>
                Técnicas y necesarias: imprescindibles para que el sitio funcione y se muestre
                correctamente.
              </li>
              <li>
                Analíticas: si se activan, permiten conocer de forma agregada cómo se usa el sitio
                para mejorarlo. Solo se instalan con tu consentimiento.
              </li>
            </ul>
            <p className="mt-3">
              El listado detallado de cookies y proveedores se actualizará cuando se incorporen
              herramientas de analítica o marketing a este sitio.
            </p>
          </div>
          <div>
            <h2 className="text-xl font-medium text-foreground">Cómo gestionarlas o eliminarlas</h2>
            <p className="mt-3">
              Puedes permitir, bloquear o eliminar las cookies instaladas desde la configuración de
              tu navegador (Chrome, Safari, Firefox o Edge). Bloquear las cookies técnicas puede
              afectar al funcionamiento del sitio.
            </p>
          </div>
          <div>
            <h2 className="text-xl font-medium text-foreground">Dudas</h2>
            <p className="mt-3">
              Si tienes cualquier consulta sobre esta política, escríbenos a {site.email} o llámanos
              al {site.phone}.
            </p>
          </div>
        </div>
      </section>
    </>
  );
}
