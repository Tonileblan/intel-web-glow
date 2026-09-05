import { useState, type FormEvent } from "react";
import { ShieldCheck, Phone, CheckCircle2, ArrowRight, Clock, Send, Lock } from "lucide-react";
import { toast } from "sonner";
import { site } from "@/lib/site";

const types = [
  { id: "empresa", label: "Empresa / Nave Industrial" },
  { id: "comunidad", label: "Comunidad / Urbanización" },
  { id: "hogar", label: "Vivienda / Particular" },
  { id: "institucion", label: "Institución / Organismo" },
  { id: "cctv", label: "Revisión CCTV Existente" },
];

export function QuickAuditForm() {
  const [selectedType, setSelectedType] = useState("empresa");
  const [submitted, setSubmitted] = useState(false);
  const [loading, setLoading] = useState(false);

  const handleSubmit = (e: FormEvent<HTMLFormElement>) => {
    e.preventDefault();
    setLoading(true);

    setTimeout(() => {
      setLoading(false);
      setSubmitted(true);
      toast.success("¡Solicitud recibida correctamente!", {
        description:
          "Un ingeniero de seguridad de Control 61 revisará tus necesidades y te contactará en menos de 2 horas laborales.",
        duration: 6000,
      });
    }, 600);
  };

  return (
    <div className="mx-auto w-full max-w-4xl overflow-hidden rounded-2xl border border-slate-200 bg-white shadow-xl">
      <div className="grid gap-0 md:grid-cols-12">
        {/* Left Side: Value & Guarantee */}
        <div className="flex flex-col justify-between border-b border-slate-200 bg-slate-900 p-6 text-slate-100 sm:p-8 md:col-span-5 md:border-b-0 md:border-r">
          <div>
            <div className="inline-flex items-center gap-1.5 rounded-full bg-red-500/20 px-3 py-1 font-mono text-xs font-semibold text-red-400">
              <ShieldCheck className="size-3.5" />
              VALORACIÓN GRATUITA SIN COMPROMISO
            </div>
            <h3 className="mt-4 text-2xl font-bold tracking-tight text-white">
              Diseñamos la protección exacta que necesitas
            </h3>
            <p className="mt-2.5 text-sm leading-relaxed text-slate-300">
              Analizamos los puntos vulnerables sobre el terreno y te entregamos un presupuesto cerrado sin letra pequeña ni contratos abusivos.
            </p>

            <div className="mt-6 space-y-3">
              <div className="flex items-start gap-2.5 text-xs text-slate-300">
                <CheckCircle2 className="mt-0.5 size-4 text-emerald-400 shrink-0" />
                <span>Estudio de riesgo personalizado en 24/48h</span>
              </div>
              <div className="flex items-start gap-2.5 text-xs text-slate-300">
                <CheckCircle2 className="mt-0.5 size-4 text-emerald-400 shrink-0" />
                <span>Equipos homologados Grado 2 y 3</span>
              </div>
              <div className="flex items-start gap-2.5 text-xs text-slate-300">
                <CheckCircle2 className="mt-0.5 size-4 text-emerald-400 shrink-0" />
                <span>Técnicos propios certificados en plantilla</span>
              </div>
            </div>
          </div>

          <div className="mt-8 rounded-xl border border-slate-800 bg-slate-950/70 p-4">
            <p className="text-xs text-slate-400">¿Tienes una avería urgente o consulta directa?</p>
            <a
              href={site.phoneHref}
              className="mt-2 flex items-center gap-2 font-bold text-white transition-colors hover:text-red-400"
            >
              <Phone className="size-4 text-primary" />
              <span>{site.phone} · Atención 24h</span>
            </a>
          </div>
        </div>

        {/* Right Side: Fast 1-Step Form */}
        <div className="p-6 sm:p-8 md:col-span-7">
          {submitted ? (
            <div className="flex min-h-[360px] flex-col items-center justify-center text-center">
              <div className="flex size-14 items-center justify-center rounded-full bg-emerald-100 text-emerald-600">
                <CheckCircle2 className="size-8" />
              </div>
              <h4 className="mt-4 text-xl font-bold text-slate-900">
                ¡Gracias por contactar con Control 61!
              </h4>
              <p className="mt-2 max-w-md text-sm text-slate-600">
                Hemos registrado tu solicitud. Nos pondremos en contacto contigo en breve para coordinar la visita técnica gratuita.
              </p>
              <button
                type="button"
                onClick={() => setSubmitted(false)}
                className="mt-6 inline-flex items-center rounded-lg border border-slate-300 px-4 py-2 text-xs font-semibold text-slate-700 hover:bg-slate-50"
              >
                Enviar otra solicitud
              </button>
            </div>
          ) : (
            <form onSubmit={handleSubmit} className="space-y-4">
              <div>
                <label className="block text-xs font-bold uppercase tracking-wider text-slate-700">
                  1. ¿Qué tipo de instalación quieres proteger?
                </label>
                <div className="mt-2 flex flex-wrap gap-2">
                  {types.map((t) => (
                    <button
                      key={t.id}
                      type="button"
                      onClick={() => setSelectedType(t.id)}
                      className={`rounded-lg px-3 py-1.5 text-xs font-medium transition-all ${
                        selectedType === t.id
                          ? "bg-primary font-semibold text-white shadow-xs"
                          : "border border-slate-200 bg-slate-50 text-slate-700 hover:border-slate-300 hover:bg-slate-100"
                      }`}
                    >
                      {t.label}
                    </button>
                  ))}
                </div>
              </div>

              <div className="grid gap-3 sm:grid-cols-2">
                <div>
                  <label htmlFor="audit-name" className="block text-xs font-medium text-slate-700">
                    Nombre o Empresa *
                  </label>
                  <input
                    id="audit-name"
                    required
                    placeholder="Ej. Juan Gómez / Transportes SL"
                    className="mt-1 h-10 w-full rounded-lg border border-slate-300 bg-white px-3 text-sm text-slate-900 placeholder:text-slate-400 outline-none transition-all focus:border-primary focus:ring-2 focus:ring-red-100"
                  />
                </div>

                <div>
                  <label htmlFor="audit-phone" className="block text-xs font-medium text-slate-700">
                    Teléfono de contacto *
                  </label>
                  <input
                    id="audit-phone"
                    type="tel"
                    required
                    placeholder="Ej. 600 000 000"
                    className="mt-1 h-10 w-full rounded-lg border border-slate-300 bg-white px-3 text-sm text-slate-900 placeholder:text-slate-400 outline-none transition-all focus:border-primary focus:ring-2 focus:ring-red-100"
                  />
                </div>
              </div>

              <div className="grid gap-3 sm:grid-cols-2">
                <div>
                  <label htmlFor="audit-email" className="block text-xs font-medium text-slate-700">
                    Email
                  </label>
                  <input
                    id="audit-email"
                    type="email"
                    placeholder="ejemplo@correo.com"
                    className="mt-1 h-10 w-full rounded-lg border border-slate-300 bg-white px-3 text-sm text-slate-900 placeholder:text-slate-400 outline-none transition-all focus:border-primary focus:ring-2 focus:ring-red-100"
                  />
                </div>

                <div>
                  <label htmlFor="audit-location" className="block text-xs font-medium text-slate-700">
                    Municipio / Ubicación en Murcia
                  </label>
                  <input
                    id="audit-location"
                    placeholder="Ej. Molina de Segura, Murcia..."
                    className="mt-1 h-10 w-full rounded-lg border border-slate-300 bg-white px-3 text-sm text-slate-900 placeholder:text-slate-400 outline-none transition-all focus:border-primary focus:ring-2 focus:ring-red-100"
                  />
                </div>
              </div>

              <div>
                <label htmlFor="audit-notes" className="block text-xs font-medium text-slate-700">
                  Detalles adicionales (opcional)
                </label>
                <textarea
                  id="audit-notes"
                  rows={2}
                  placeholder="Superficie aproximada, cámaras necesarias, dudas específicas..."
                  className="mt-1 w-full rounded-lg border border-slate-300 bg-white p-2.5 text-sm text-slate-900 placeholder:text-slate-400 outline-none transition-all focus:border-primary focus:ring-2 focus:ring-red-100"
                />
              </div>

              <button
                type="submit"
                disabled={loading}
                className="inline-flex min-h-11 w-full items-center justify-center gap-2 rounded-lg bg-primary px-6 text-sm font-semibold text-white shadow-xs transition-all hover:bg-red-700 hover:shadow-md disabled:opacity-50"
              >
                {loading ? (
                  <span>Procesando...</span>
                ) : (
                  <>
                    <span>Solicitar Estudio y Presupuesto Gratuito</span>
                    <ArrowRight className="size-4" />
                  </>
                )}
              </button>

              <p className="flex items-center justify-center gap-1 text-[11px] text-slate-500">
                <Lock className="size-3 text-slate-400" />
                <span>Datos protegidos bajo secreto profesional y normativa RGPD. Sin spam.</span>
              </p>
            </form>
          )}
        </div>
      </div>
    </div>
  );
}
