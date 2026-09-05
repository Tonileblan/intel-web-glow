import { Link } from "@tanstack/react-router";
import {
  Camera,
  ShieldCheck,
  Fingerprint,
  Radio,
  Flame,
  FileCheck2,
  ArrowRight,
  Eye,
  CheckCircle2,
  Sparkles,
} from "lucide-react";
import { Reveal } from "./Reveal";

export function BentoGridServices() {
  return (
    <section className="relative px-4 py-20 sm:px-6 md:py-28" aria-labelledby="bento-services">
      <div className="mx-auto max-w-6xl">
        {/* Section Header */}
        <Reveal>
          <div className="flex flex-col items-start justify-between gap-4 md:flex-row md:items-end">
            <div>
              <p className="inline-flex items-center gap-1.5 rounded-full border border-red-200 bg-red-50/80 px-3 py-1 text-xs font-semibold uppercase tracking-wider text-primary">
                <Sparkles className="size-3.5" />
                Soluciones de Seguridad Integral
              </p>
              <h2
                id="bento-services"
                className="mt-3 text-3xl font-bold tracking-tight text-slate-900 sm:text-4xl"
              >
                Ingeniería de protección sin puntos ciegos
              </h2>
              <p className="mt-3 max-w-2xl text-base text-slate-600">
                Diseñamos, instalamos y mantenemos ecosistemas completos de seguridad donde cada
                cámara, sensor y acceso trabaja sincronizado en tiempo real.
              </p>
            </div>
            <Link
              to="/contacto"
              className="inline-flex items-center gap-2 rounded-lg border border-slate-200 bg-white px-4 py-2.5 text-sm font-semibold text-slate-800 shadow-xs transition-colors hover:border-slate-300 hover:bg-slate-50"
            >
              <span>Ver todas las soluciones</span>
              <ArrowRight className="size-4 text-primary" />
            </Link>
          </div>
        </Reveal>

        {/* Bento Grid Layout */}
        <div className="mt-12 grid grid-cols-1 gap-6 md:grid-cols-2 lg:grid-cols-3">
          {/* Card 1: CCTV IA (Spans 2 cols on lg) */}
          <Reveal className="lg:col-span-2">
            <div className="group relative flex h-full min-h-[380px] flex-col justify-between overflow-hidden rounded-2xl border border-slate-200/90 bg-white p-6 shadow-xs transition-all duration-300 hover:border-slate-300 hover:shadow-md sm:p-8">
              {/* Background Image with Clean Overlays */}
              <div className="absolute inset-0 -z-10 overflow-hidden">
                <img
                  src="https://images.unsplash.com/photo-1557597774-9d273605dfa9?auto=format&fit=crop&w=1400&q=80"
                  alt="Cámara CCTV con óptica de alta resolución y sensor de visión nocturna"
                  className="size-full object-cover object-center opacity-15 transition-transform duration-700 group-hover:scale-105"
                  loading="lazy"
                />
                <div className="absolute inset-0 bg-gradient-to-t from-white via-white/80 to-white/30" />
              </div>

              <div>
                <div className="flex flex-wrap items-center justify-between gap-2">
                  <div className="inline-flex size-11 items-center justify-center rounded-xl bg-red-50 text-primary ring-1 ring-red-100">
                    <Camera className="size-5" />
                  </div>
                  <div className="flex items-center gap-2 font-mono text-xs">
                    <span className="rounded-md border border-slate-200 bg-white/90 px-2.5 py-1 font-semibold text-slate-700 shadow-2xs backdrop-blur-xs">
                      4K HDR ÓPTICA IA
                    </span>
                    <span className="rounded-md border border-emerald-200 bg-emerald-50 px-2.5 py-1 font-semibold text-emerald-700">
                      CUMPLIMIENTO RGPD
                    </span>
                  </div>
                </div>

                <h3 className="mt-6 text-2xl font-bold tracking-tight text-slate-900">
                  CCTV Inteligente con Búsqueda Instantánea
                </h3>
                <p className="mt-3 max-w-xl text-sm leading-relaxed text-slate-600 sm:text-base">
                  Cámaras de alta resolución con analítica de vídeo avanzada: reconocimiento de
                  matrículas (LPR), conteo perimetral y localización de eventos en segundos sin
                  tener que revisar horas de grabación.
                </p>

                <div className="mt-5 grid grid-cols-2 gap-3 sm:grid-cols-3">
                  <div className="rounded-lg border border-slate-100 bg-slate-50/70 p-2.5">
                    <p className="text-xs font-semibold text-slate-900">Visión Nocturna</p>
                    <p className="text-[11px] text-slate-500">UltraLowLight sin distorsión</p>
                  </div>
                  <div className="rounded-lg border border-slate-100 bg-slate-50/70 p-2.5">
                    <p className="text-xs font-semibold text-slate-900">Grabación Cifrada</p>
                    <p className="text-[11px] text-slate-500">Almacenamiento protegido NVR</p>
                  </div>
                  <div className="col-span-2 rounded-lg border border-slate-100 bg-slate-50/70 p-2.5 sm:col-span-1">
                    <p className="text-xs font-semibold text-slate-900">Acceso Móvil</p>
                    <p className="text-[11px] text-slate-500">Visualización remota segura</p>
                  </div>
                </div>
              </div>

              <div className="mt-6 pt-4 border-t border-slate-100">
                <Link
                  to="/cctv"
                  className="group/link inline-flex items-center gap-2 text-sm font-semibold text-primary transition-colors hover:text-red-700"
                >
                  <span>Explorar soluciones CCTV</span>
                  <ArrowRight className="size-4 transition-transform group-hover/link:translate-x-1" />
                </Link>
              </div>
            </div>
          </Reveal>

          {/* Card 2: Alarmas Grado 2 y 3 (1 col) */}
          <Reveal delay={0.1}>
            <div className="group relative flex h-full min-h-[380px] flex-col justify-between rounded-2xl border border-slate-200/90 bg-white p-6 shadow-xs transition-all duration-300 hover:border-slate-300 hover:shadow-md sm:p-8">
              <div>
                <div className="flex items-center justify-between">
                  <div className="inline-flex size-11 items-center justify-center rounded-xl bg-slate-100 text-slate-900">
                    <ShieldCheck className="size-5 text-primary" />
                  </div>
                  <span className="rounded-md border border-slate-200 bg-slate-50 px-2 py-0.5 font-mono text-xs font-semibold text-slate-700">
                    GRADO 2 & 3
                  </span>
                </div>

                <h3 className="mt-6 text-xl font-bold tracking-tight text-slate-900">
                  Alarmas Anti-Inhibición
                </h3>
                <p className="mt-2.5 text-sm leading-relaxed text-slate-600">
                  Detección perimetral e interior con doble vía de comunicación redundante (Fibra +
                  5G). Inmune a cortes de línea e inhibidores de frecuencia.
                </p>

                <ul className="mt-5 space-y-2 text-xs text-slate-600">
                  <li className="flex items-center gap-2">
                    <CheckCircle2 className="size-3.5 text-primary shrink-0" />
                    <span>Verificación instantánea por vídeo</span>
                  </li>
                  <li className="flex items-center gap-2">
                    <CheckCircle2 className="size-3.5 text-primary shrink-0" />
                    <span>Detectores sísmicos y de rotura</span>
                  </li>
                  <li className="flex items-center gap-2">
                    <CheckCircle2 className="size-3.5 text-primary shrink-0" />
                    <span>Sirena disuasoria de alta potencia</span>
                  </li>
                </ul>
              </div>

              <div className="mt-6 pt-4 border-t border-slate-100">
                <Link
                  to="/empresas"
                  className="group/link inline-flex items-center gap-2 text-sm font-semibold text-slate-900 transition-colors hover:text-primary"
                >
                  <span>Sistemas de alarma</span>
                  <ArrowRight className="size-4 transition-transform group-hover/link:translate-x-1" />
                </Link>
              </div>
            </div>
          </Reveal>

          {/* Card 3: Control de Accesos (1 col) */}
          <Reveal delay={0.15}>
            <div className="group relative flex h-full min-h-[380px] flex-col justify-between rounded-2xl border border-slate-200/90 bg-white p-6 shadow-xs transition-all duration-300 hover:border-slate-300 hover:shadow-md sm:p-8">
              <div>
                <div className="flex items-center justify-between">
                  <div className="inline-flex size-11 items-center justify-center rounded-xl bg-slate-100 text-slate-900">
                    <Fingerprint className="size-5 text-sky-600" />
                  </div>
                  <span className="rounded-md border border-sky-100 bg-sky-50 px-2 py-0.5 font-mono text-xs font-semibold text-sky-700">
                    BIOMETRÍA / NFC
                  </span>
                </div>

                <h3 className="mt-6 text-xl font-bold tracking-tight text-slate-900">
                  Control de Accesos & Presencia
                </h3>
                <p className="mt-2.5 text-sm leading-relaxed text-slate-600">
                  Gestión integral de quién entra, cuándo y dónde. Lectores biométricos,
                  credenciales móviles cifradas y tornos con registro auditable.
                </p>

                <ul className="mt-5 space-y-2 text-xs text-slate-600">
                  <li className="flex items-center gap-2">
                    <CheckCircle2 className="size-3.5 text-sky-600 shrink-0" />
                    <span>Control de puertas, tornos y barreras</span>
                  </li>
                  <li className="flex items-center gap-2">
                    <CheckCircle2 className="size-3.5 text-sky-600 shrink-0" />
                    <span>Altas y bajas instantáneas sin llaves</span>
                  </li>
                  <li className="flex items-center gap-2">
                    <CheckCircle2 className="size-3.5 text-sky-600 shrink-0" />
                    <span>Software de auditoría y presencia</span>
                  </li>
                </ul>
              </div>

              <div className="mt-6 pt-4 border-t border-slate-100">
                <Link
                  to="/empresas"
                  className="group/link inline-flex items-center gap-2 text-sm font-semibold text-slate-900 transition-colors hover:text-primary"
                >
                  <span>Control de accesos</span>
                  <ArrowRight className="size-4 transition-transform group-hover/link:translate-x-1" />
                </Link>
              </div>
            </div>
          </Reveal>

          {/* Card 4: Monitorización 24/7 y SOC (Spans 2 cols on lg) */}
          <Reveal delay={0.2} className="lg:col-span-2">
            <div className="group relative flex h-full min-h-[380px] flex-col justify-between overflow-hidden rounded-2xl border border-slate-200/90 bg-white p-6 shadow-xs transition-all duration-300 hover:border-slate-300 hover:shadow-md sm:p-8">
              {/* Background Image with Clean Overlays */}
              <div className="absolute inset-0 -z-10 overflow-hidden">
                <img
                  src="https://images.unsplash.com/photo-1504384308090-c894fdcc538d?auto=format&fit=crop&w=1400&q=80"
                  alt="Centro de monitorización y operaciones de seguridad 24 horas"
                  className="size-full object-cover object-center opacity-15 transition-transform duration-700 group-hover:scale-105"
                  loading="lazy"
                />
                <div className="absolute inset-0 bg-gradient-to-t from-white via-white/80 to-white/30" />
              </div>

              <div>
                <div className="flex flex-wrap items-center justify-between gap-2">
                  <div className="inline-flex size-11 items-center justify-center rounded-xl bg-emerald-50 text-emerald-700 ring-1 ring-emerald-100">
                    <Radio className="size-5" />
                  </div>
                  <div className="flex items-center gap-2 font-mono text-xs">
                    <span className="rounded-md border border-emerald-200 bg-emerald-50 px-2.5 py-1 font-semibold text-emerald-700">
                      CONEXIÓN CRA 24/7/365
                    </span>
                    <span className="rounded-md border border-slate-200 bg-white/90 px-2.5 py-1 font-semibold text-slate-700">
                      AVISO DIRECTO A POLICÍA
                    </span>
                  </div>
                </div>

                <h3 className="mt-6 text-2xl font-bold tracking-tight text-slate-900">
                  Central Receptora & Asistencia Urgente de Averías
                </h3>
                <p className="mt-3 max-w-xl text-sm leading-relaxed text-slate-600 sm:text-base">
                  Respuesta inmediata ante cualquier salto de alarma. Verificamos la incidencia por
                  vídeo en menos de 15 segundos y activamos el protocolo con Fuerzas de Seguridad y
                  servicio técnico de guardia 24 horas.
                </p>

                <div className="mt-5 grid grid-cols-2 gap-3 sm:grid-cols-3">
                  <div className="rounded-lg border border-slate-100 bg-slate-50/70 p-2.5">
                    <p className="font-mono text-base font-bold text-slate-900">&lt; 15 seg</p>
                    <p className="text-[11px] text-slate-500">Tiempo de verificación</p>
                  </div>
                  <div className="rounded-lg border border-slate-100 bg-slate-50/70 p-2.5">
                    <p className="font-mono text-base font-bold text-slate-900">24 Horas</p>
                    <p className="text-[11px] text-slate-500">Atención técnica real</p>
                  </div>
                  <div className="col-span-2 rounded-lg border border-slate-100 bg-slate-50/70 p-2.5 sm:col-span-1">
                    <p className="font-mono text-base font-bold text-slate-900">100%</p>
                    <p className="text-[11px] text-slate-500">Conexión homologada</p>
                  </div>
                </div>
              </div>

              <div className="mt-6 pt-4 border-t border-slate-100">
                <Link
                  to="/mantenimiento"
                  className="group/link inline-flex items-center gap-2 text-sm font-semibold text-primary transition-colors hover:text-red-700"
                >
                  <span>Mantenimiento y monitorización</span>
                  <ArrowRight className="size-4 transition-transform group-hover/link:translate-x-1" />
                </Link>
              </div>
            </div>
          </Reveal>

          {/* Card 5: Incendios (1 col) */}
          <Reveal delay={0.25}>
            <div className="group relative flex h-full min-h-[380px] flex-col justify-between rounded-2xl border border-slate-200/90 bg-white p-6 shadow-xs transition-all duration-300 hover:border-slate-300 hover:shadow-md sm:p-8">
              <div>
                <div className="flex items-center justify-between">
                  <div className="inline-flex size-11 items-center justify-center rounded-xl bg-slate-100 text-slate-900">
                    <Flame className="size-5 text-amber-600" />
                  </div>
                  <span className="rounded-md border border-amber-200 bg-amber-50 px-2 py-0.5 font-mono text-xs font-semibold text-amber-800">
                    REG. INDUSTRIA
                  </span>
                </div>

                <h3 className="mt-6 text-xl font-bold tracking-tight text-slate-900">
                  Protección Contra Incendios (PCI)
                </h3>
                <p className="mt-2.5 text-sm leading-relaxed text-slate-600">
                  Detección precoz óptica y térmica, pulsadores, sirenas y extinción. Instalación y
                  mantenimiento conforme al RIPCI y normativa vigente.
                </p>

                <ul className="mt-5 space-y-2 text-xs text-slate-600">
                  <li className="flex items-center gap-2">
                    <CheckCircle2 className="size-3.5 text-amber-600 shrink-0" />
                    <span>Detección de humos convencional y analógica</span>
                  </li>
                  <li className="flex items-center gap-2">
                    <CheckCircle2 className="size-3.5 text-amber-600 shrink-0" />
                    <span>Certificados y actas oficiales de revisión</span>
                  </li>
                  <li className="flex items-center gap-2">
                    <CheckCircle2 className="size-3.5 text-amber-600 shrink-0" />
                    <span>Integración con evacuación y megafonía</span>
                  </li>
                </ul>
              </div>

              <div className="mt-6 pt-4 border-t border-slate-100">
                <Link
                  to="/empresas"
                  className="group/link inline-flex items-center gap-2 text-sm font-semibold text-slate-900 transition-colors hover:text-primary"
                >
                  <span>Sistemas contra incendios</span>
                  <ArrowRight className="size-4 transition-transform group-hover/link:translate-x-1" />
                </Link>
              </div>
            </div>
          </Reveal>

          {/* Card 6: Ingeniería y Legalización (1 col) */}
          <Reveal delay={0.3}>
            <div className="group relative flex h-full min-h-[380px] flex-col justify-between rounded-2xl border border-slate-200/90 bg-white p-6 shadow-xs transition-all duration-300 hover:border-slate-300 hover:shadow-md sm:p-8">
              <div>
                <div className="flex items-center justify-between">
                  <div className="inline-flex size-11 items-center justify-center rounded-xl bg-slate-100 text-slate-900">
                    <FileCheck2 className="size-5 text-indigo-600" />
                  </div>
                  <span className="rounded-md border border-indigo-200 bg-indigo-50 px-2 py-0.5 font-mono text-xs font-semibold text-indigo-800">
                    ISO & REA
                  </span>
                </div>

                <h3 className="mt-6 text-xl font-bold tracking-tight text-slate-900">
                  Ingeniería & Obra Nueva
                </h3>
                <p className="mt-2.5 text-sm leading-relaxed text-slate-600">
                  Proyectos técnicos desde el plano, coordinación con instaladores y legalización
                  completa para licencias de actividad y primera ocupación.
                </p>

                <ul className="mt-5 space-y-2 text-xs text-slate-600">
                  <li className="flex items-center gap-2">
                    <CheckCircle2 className="size-3.5 text-indigo-600 shrink-0" />
                    <span>Canalizaciones y cableado limpio en obra</span>
                  </li>
                  <li className="flex items-center gap-2">
                    <CheckCircle2 className="size-3.5 text-indigo-600 shrink-0" />
                    <span>Certificaciones ISO 9001, 14001, 45001</span>
                  </li>
                  <li className="flex items-center gap-2">
                    <CheckCircle2 className="size-3.5 text-indigo-600 shrink-0" />
                    <span>Acreditación REA para construcción</span>
                  </li>
                </ul>
              </div>

              <div className="mt-6 pt-4 border-t border-slate-100">
                <Link
                  to="/acreditaciones"
                  className="group/link inline-flex items-center gap-2 text-sm font-semibold text-slate-900 transition-colors hover:text-primary"
                >
                  <span>Ver acreditaciones y certificados</span>
                  <ArrowRight className="size-4 transition-transform group-hover/link:translate-x-1" />
                </Link>
              </div>
            </div>
          </Reveal>
        </div>
      </div>
    </section>
  );
}
