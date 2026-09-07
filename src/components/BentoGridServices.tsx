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
      {/* Background ambient lighting */}
      <div className="pointer-events-none absolute right-1/4 top-1/2 -z-10 h-80 w-80 rounded-full bg-red-600/10 blur-[120px]" />

      <div className="mx-auto max-w-6xl">
        {/* Section Header */}
        <Reveal>
          <div className="flex flex-col items-start justify-between gap-4 md:flex-row md:items-end">
            <div>
              <p className="inline-flex items-center gap-1.5 rounded-full border border-red-500/30 bg-red-950/40 px-3.5 py-1 text-xs font-semibold uppercase tracking-wider text-red-400">
                <Sparkles className="size-3.5" />
                Soluciones de Seguridad Integral
              </p>
              <h2
                id="bento-services"
                className="mt-3 text-3xl font-bold tracking-tight text-white sm:text-4xl"
              >
                Ingeniería de protección sin puntos ciegos
              </h2>
              <p className="mt-3 max-w-2xl text-base text-slate-300">
                Diseñamos, instalamos y mantenemos ecosistemas completos de seguridad donde cada
                cámara, sensor y acceso trabaja sincronizado en tiempo real.
              </p>
            </div>
            <Link
              to="/contacto"
              className="inline-flex items-center gap-2 rounded-xl border border-slate-800 bg-slate-900/80 px-4 py-2.5 text-sm font-semibold text-slate-200 shadow-md backdrop-blur-md transition-all hover:border-slate-700 hover:bg-slate-800 hover:text-white"
            >
              <span>Ver todas las soluciones</span>
              <ArrowRight className="size-4 text-red-500" />
            </Link>
          </div>
        </Reveal>

        {/* Bento Grid Layout */}
        <div className="mt-12 grid grid-cols-1 gap-6 md:grid-cols-2 lg:grid-cols-3">
          {/* Card 1: CCTV IA (Spans 2 cols on lg) */}
          <Reveal className="lg:col-span-2">
            <div className="group relative flex h-full min-h-[380px] flex-col justify-between overflow-hidden rounded-2xl border border-slate-800 bg-slate-900/70 p-6 shadow-xl backdrop-blur-md transition-all duration-300 hover:border-red-500/40 hover:bg-slate-900 sm:p-8">
              {/* Background Image with Clean Overlays */}
              <div className="absolute inset-0 -z-10 overflow-hidden">
                <img
                  src="https://images.unsplash.com/photo-1557597774-9d273605dfa9?auto=format&fit=crop&w=1400&q=80"
                  alt="Cámara CCTV con óptica de alta resolución y sensor de visión nocturna"
                  className="size-full object-cover object-center opacity-25 transition-transform duration-700 group-hover:scale-105"
                  loading="lazy"
                />
                <div className="absolute inset-0 bg-gradient-to-t from-slate-950 via-slate-950/85 to-slate-950/40" />
              </div>

              <div>
                <div className="flex flex-wrap items-center justify-between gap-2">
                  <div className="inline-flex size-11 items-center justify-center rounded-xl bg-red-950/60 text-red-500 ring-1 ring-red-900/40">
                    <Camera className="size-5" />
                  </div>
                  <div className="flex items-center gap-2 font-mono text-xs">
                    <span className="rounded-md border border-slate-700 bg-slate-800/90 px-2.5 py-1 font-semibold text-slate-200 shadow-sm backdrop-blur-md">
                      4K HDR ÓPTICA IA
                    </span>
                    <span className="rounded-md border border-emerald-500/30 bg-emerald-950/50 px-2.5 py-1 font-semibold text-emerald-400">
                      CUMPLIMIENTO RGPD
                    </span>
                  </div>
                </div>

                <h3 className="mt-6 text-2xl font-bold tracking-tight text-white">
                  CCTV Inteligente con Búsqueda Instantánea
                </h3>
                <p className="mt-3 max-w-xl text-sm leading-relaxed text-slate-300 sm:text-base">
                  Cámaras de alta resolución con analítica de vídeo avanzada: reconocimiento de
                  matrículas (LPR), conteo perimetral y localización de eventos en segundos sin
                  tener que revisar horas de grabación.
                </p>

                <div className="mt-5 grid grid-cols-2 gap-3 sm:grid-cols-3">
                  <div className="rounded-lg border border-slate-800 bg-slate-950/60 p-2.5 backdrop-blur-sm">
                    <p className="text-xs font-semibold text-white">Visión Nocturna</p>
                    <p className="text-[11px] text-slate-400">UltraLowLight sin distorsión</p>
                  </div>
                  <div className="rounded-lg border border-slate-800 bg-slate-950/60 p-2.5 backdrop-blur-sm">
                    <p className="text-xs font-semibold text-white">Grabación Cifrada</p>
                    <p className="text-[11px] text-slate-400">Almacenamiento protegido NVR</p>
                  </div>
                  <div className="col-span-2 rounded-lg border border-slate-800 bg-slate-950/60 p-2.5 backdrop-blur-sm sm:col-span-1">
                    <p className="text-xs font-semibold text-white">Acceso Móvil</p>
                    <p className="text-[11px] text-slate-400">Visualización remota segura</p>
                  </div>
                </div>
              </div>

              <div className="mt-6 pt-4 border-t border-slate-800">
                <Link
                  to="/cctv"
                  className="group/link inline-flex items-center gap-2 text-sm font-semibold text-red-400 transition-colors hover:text-red-300"
                >
                  <span>Explorar soluciones CCTV</span>
                  <ArrowRight className="size-4 transition-transform group-hover/link:translate-x-1" />
                </Link>
              </div>
            </div>
          </Reveal>

          {/* Card 2: Alarmas Grado 2 y 3 (1 col) */}
          <Reveal delay={0.1}>
            <div className="group relative flex h-full min-h-[380px] flex-col justify-between rounded-2xl border border-slate-800 bg-slate-900/70 p-6 shadow-xl backdrop-blur-md transition-all duration-300 hover:border-red-500/40 hover:bg-slate-900 sm:p-8">
              <div>
                <div className="flex items-center justify-between">
                  <div className="inline-flex size-11 items-center justify-center rounded-xl bg-slate-800 text-slate-100 ring-1 ring-slate-700">
                    <ShieldCheck className="size-5 text-red-500" />
                  </div>
                  <span className="rounded-md border border-slate-700 bg-slate-800 px-2 py-0.5 font-mono text-xs font-semibold text-slate-200">
                    GRADO 2 & 3
                  </span>
                </div>

                <h3 className="mt-6 text-xl font-bold tracking-tight text-white">
                  Alarmas Anti-Inhibición
                </h3>
                <p className="mt-2.5 text-sm leading-relaxed text-slate-300">
                  Detección perimetral e interior con doble vía de comunicación redundante (Fibra +
                  5G). Inmune a cortes de línea e inhibidores de frecuencia.
                </p>

                <ul className="mt-5 space-y-2 text-xs text-slate-300">
                  <li className="flex items-center gap-2">
                    <CheckCircle2 className="size-3.5 text-red-500 shrink-0" />
                    <span>Verificación instantánea por vídeo</span>
                  </li>
                  <li className="flex items-center gap-2">
                    <CheckCircle2 className="size-3.5 text-red-500 shrink-0" />
                    <span>Detectores sísmicos y de rotura</span>
                  </li>
                  <li className="flex items-center gap-2">
                    <CheckCircle2 className="size-3.5 text-red-500 shrink-0" />
                    <span>Sirena disuasoria de alta potencia</span>
                  </li>
                </ul>
              </div>

              <div className="mt-6 pt-4 border-t border-slate-800">
                <Link
                  to="/empresas"
                  className="group/link inline-flex items-center gap-2 text-sm font-semibold text-slate-200 transition-colors hover:text-red-400"
                >
                  <span>Sistemas de alarma</span>
                  <ArrowRight className="size-4 transition-transform group-hover/link:translate-x-1" />
                </Link>
              </div>
            </div>
          </Reveal>

          {/* Card 3: Control de Accesos (1 col) */}
          <Reveal delay={0.15}>
            <div className="group relative flex h-full min-h-[380px] flex-col justify-between rounded-2xl border border-slate-800 bg-slate-900/70 p-6 shadow-xl backdrop-blur-md transition-all duration-300 hover:border-red-500/40 hover:bg-slate-900 sm:p-8">
              <div>
                <div className="flex items-center justify-between">
                  <div className="inline-flex size-11 items-center justify-center rounded-xl bg-slate-800 text-slate-100 ring-1 ring-slate-700">
                    <Fingerprint className="size-5 text-sky-400" />
                  </div>
                  <span className="rounded-md border border-sky-500/30 bg-sky-950/40 px-2 py-0.5 font-mono text-xs font-semibold text-sky-400">
                    BIOMETRÍA / NFC
                  </span>
                </div>

                <h3 className="mt-6 text-xl font-bold tracking-tight text-white">
                  Control de Accesos & Presencia
                </h3>
                <p className="mt-2.5 text-sm leading-relaxed text-slate-300">
                  Gestión integral de quién entra, cuándo y dónde. Lectores biométricos,
                  credenciales móviles cifradas y tornos con registro auditable.
                </p>

                <ul className="mt-5 space-y-2 text-xs text-slate-300">
                  <li className="flex items-center gap-2">
                    <CheckCircle2 className="size-3.5 text-sky-400 shrink-0" />
                    <span>Control de puertas, tornos y barreras</span>
                  </li>
                  <li className="flex items-center gap-2">
                    <CheckCircle2 className="size-3.5 text-sky-400 shrink-0" />
                    <span>Altas y bajas instantáneas sin llaves</span>
                  </li>
                  <li className="flex items-center gap-2">
                    <CheckCircle2 className="size-3.5 text-sky-400 shrink-0" />
                    <span>Software de auditoría y presencia</span>
                  </li>
                </ul>
              </div>

              <div className="mt-6 pt-4 border-t border-slate-800">
                <Link
                  to="/empresas"
                  className="group/link inline-flex items-center gap-2 text-sm font-semibold text-slate-200 transition-colors hover:text-red-400"
                >
                  <span>Control de accesos</span>
                  <ArrowRight className="size-4 transition-transform group-hover/link:translate-x-1" />
                </Link>
              </div>
            </div>
          </Reveal>

          {/* Card 4: Monitorización 24/7 y SOC (Spans 2 cols on lg) */}
          <Reveal delay={0.2} className="lg:col-span-2">
            <div className="group relative flex h-full min-h-[380px] flex-col justify-between overflow-hidden rounded-2xl border border-slate-800 bg-slate-900/70 p-6 shadow-xl backdrop-blur-md transition-all duration-300 hover:border-red-500/40 hover:bg-slate-900 sm:p-8">
              {/* Background Image with Clean Overlays */}
              <div className="absolute inset-0 -z-10 overflow-hidden">
                <img
                  src="https://images.unsplash.com/photo-1504384308090-c894fdcc538d?auto=format&fit=crop&w=1400&q=80"
                  alt="Centro de monitorización y operaciones de seguridad 24 horas"
                  className="size-full object-cover object-center opacity-25 transition-transform duration-700 group-hover:scale-105"
                  loading="lazy"
                />
                <div className="absolute inset-0 bg-gradient-to-t from-slate-950 via-slate-950/85 to-slate-950/40" />
              </div>

              <div>
                <div className="flex flex-wrap items-center justify-between gap-2">
                  <div className="inline-flex size-11 items-center justify-center rounded-xl bg-emerald-950/60 text-emerald-400 ring-1 ring-emerald-900/40">
                    <Radio className="size-5" />
                  </div>
                  <div className="flex items-center gap-2 font-mono text-xs">
                    <span className="rounded-md border border-emerald-500/30 bg-emerald-950/50 px-2.5 py-1 font-semibold text-emerald-400">
                      CONEXIÓN CRA 24/7/365
                    </span>
                    <span className="rounded-md border border-slate-700 bg-slate-800/90 px-2.5 py-1 font-semibold text-slate-200">
                      AVISO DIRECTO A POLICÍA
                    </span>
                  </div>
                </div>

                <h3 className="mt-6 text-2xl font-bold tracking-tight text-white">
                  Central Receptora & Asistencia Urgente de Averías
                </h3>
                <p className="mt-3 max-w-xl text-sm leading-relaxed text-slate-300 sm:text-base">
                  Respuesta inmediata ante cualquier salto de alarma. Verificamos la incidencia por
                  vídeo en menos de 15 segundos y activamos el protocolo con Fuerzas de Seguridad y
                  servicio técnico de guardia 24 horas.
                </p>

                <div className="mt-5 grid grid-cols-2 gap-3 sm:grid-cols-3">
                  <div className="rounded-lg border border-slate-800 bg-slate-950/60 p-2.5 backdrop-blur-sm">
                    <p className="font-mono text-base font-bold text-white">&lt; 15 seg</p>
                    <p className="text-[11px] text-slate-400">Tiempo de verificación</p>
                  </div>
                  <div className="rounded-lg border border-slate-800 bg-slate-950/60 p-2.5 backdrop-blur-sm">
                    <p className="font-mono text-base font-bold text-white">24 Horas</p>
                    <p className="text-[11px] text-slate-400">Atención técnica real</p>
                  </div>
                  <div className="col-span-2 rounded-lg border border-slate-800 bg-slate-950/60 p-2.5 backdrop-blur-sm sm:col-span-1">
                    <p className="font-mono text-base font-bold text-white">100%</p>
                    <p className="text-[11px] text-slate-400">Conexión homologada</p>
                  </div>
                </div>
              </div>

              <div className="mt-6 pt-4 border-t border-slate-800">
                <Link
                  to="/mantenimiento"
                  className="group/link inline-flex items-center gap-2 text-sm font-semibold text-red-400 transition-colors hover:text-red-300"
                >
                  <span>Mantenimiento y monitorización</span>
                  <ArrowRight className="size-4 transition-transform group-hover/link:translate-x-1" />
                </Link>
              </div>
            </div>
          </Reveal>

          {/* Card 5: Incendios (1 col) */}
          <Reveal delay={0.25}>
            <div className="group relative flex h-full min-h-[380px] flex-col justify-between rounded-2xl border border-slate-800 bg-slate-900/70 p-6 shadow-xl backdrop-blur-md transition-all duration-300 hover:border-red-500/40 hover:bg-slate-900 sm:p-8">
              <div>
                <div className="flex items-center justify-between">
                  <div className="inline-flex size-11 items-center justify-center rounded-xl bg-slate-800 text-slate-100 ring-1 ring-slate-700">
                    <Flame className="size-5 text-amber-400" />
                  </div>
                  <span className="rounded-md border border-amber-500/30 bg-amber-950/40 px-2 py-0.5 font-mono text-xs font-semibold text-amber-400">
                    REG. INDUSTRIA
                  </span>
                </div>

                <h3 className="mt-6 text-xl font-bold tracking-tight text-white">
                  Protección Contra Incendios (PCI)
                </h3>
                <p className="mt-2.5 text-sm leading-relaxed text-slate-300">
                  Detección precoz óptica y térmica, pulsadores, sirenas y extinción. Instalación y
                  mantenimiento conforme al RIPCI y normativa vigente.
                </p>

                <ul className="mt-5 space-y-2 text-xs text-slate-300">
                  <li className="flex items-center gap-2">
                    <CheckCircle2 className="size-3.5 text-amber-400 shrink-0" />
                    <span>Detección de humos convencional y analógica</span>
                  </li>
                  <li className="flex items-center gap-2">
                    <CheckCircle2 className="size-3.5 text-amber-400 shrink-0" />
                    <span>Certificados y actas oficiales de revisión</span>
                  </li>
                  <li className="flex items-center gap-2">
                    <CheckCircle2 className="size-3.5 text-amber-400 shrink-0" />
                    <span>Integración con evacuación y megafonía</span>
                  </li>
                </ul>
              </div>

              <div className="mt-6 pt-4 border-t border-slate-800">
                <Link
                  to="/empresas"
                  className="group/link inline-flex items-center gap-2 text-sm font-semibold text-slate-200 transition-colors hover:text-red-400"
                >
                  <span>Sistemas contra incendios</span>
                  <ArrowRight className="size-4 transition-transform group-hover/link:translate-x-1" />
                </Link>
              </div>
            </div>
          </Reveal>

          {/* Card 6: Ingeniería y Legalización (1 col) */}
          <Reveal delay={0.3}>
            <div className="group relative flex h-full min-h-[380px] flex-col justify-between rounded-2xl border border-slate-800 bg-slate-900/70 p-6 shadow-xl backdrop-blur-md transition-all duration-300 hover:border-red-500/40 hover:bg-slate-900 sm:p-8">
              <div>
                <div className="flex items-center justify-between">
                  <div className="inline-flex size-11 items-center justify-center rounded-xl bg-slate-800 text-slate-100 ring-1 ring-slate-700">
                    <FileCheck2 className="size-5 text-indigo-400" />
                  </div>
                  <span className="rounded-md border border-indigo-500/30 bg-indigo-950/40 px-2 py-0.5 font-mono text-xs font-semibold text-indigo-400">
                    ISO & REA
                  </span>
                </div>

                <h3 className="mt-6 text-xl font-bold tracking-tight text-white">
                  Ingeniería & Obra Nueva
                </h3>
                <p className="mt-2.5 text-sm leading-relaxed text-slate-300">
                  Proyectos técnicos desde el plano, coordinación con instaladores y legalización
                  completa para licencias de actividad y primera ocupación.
                </p>

                <ul className="mt-5 space-y-2 text-xs text-slate-300">
                  <li className="flex items-center gap-2">
                    <CheckCircle2 className="size-3.5 text-indigo-400 shrink-0" />
                    <span>Canalizaciones y cableado limpio en obra</span>
                  </li>
                  <li className="flex items-center gap-2">
                    <CheckCircle2 className="size-3.5 text-indigo-400 shrink-0" />
                    <span>Certificaciones ISO 9001, 14001, 45001</span>
                  </li>
                  <li className="flex items-center gap-2">
                    <CheckCircle2 className="size-3.5 text-indigo-400 shrink-0" />
                    <span>Acreditación REA para construcción</span>
                  </li>
                </ul>
              </div>

              <div className="mt-6 pt-4 border-t border-slate-800">
                <Link
                  to="/acreditaciones"
                  className="group/link inline-flex items-center gap-2 text-sm font-semibold text-slate-200 transition-colors hover:text-red-400"
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
