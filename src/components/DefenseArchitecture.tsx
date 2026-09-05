import { useState } from "react";
import {
  ShieldAlert,
  Cpu,
  PhoneCall,
  Smartphone,
  ChevronRight,
  CheckCircle2,
  Clock,
  Radio,
} from "lucide-react";
import { Reveal } from "./Reveal";

const layers = [
  {
    step: "01",
    name: "Detección Perimetral Anticipada",
    latency: "< 2 segundos",
    icon: ShieldAlert,
    tag: "DISUASIÓN INICIAL",
    title: "Detección antes del intento de intrusión",
    description:
      "Sensores volumétricos de triple tecnología, barreras infrarrojas activas y analítica perimetral en cámaras que detectan presencia en los límites exteriores de la finca o nave.",
    points: [
      "Inmunidad a mascotas y condiciones climáticas adversas",
      "Activación de proyectores disuasorios estroboscópicos",
      "Transmisión simultánea a CRA y canal móvil del cliente",
    ],
  },
  {
    step: "02",
    name: "Verificación de Vídeo con IA",
    latency: "< 10 segundos",
    icon: Cpu,
    tag: "FILTRO INTELIGENTE",
    title: "Cero falsas alarmas con visión artificial",
    description:
      "Algoritmos de IA analizan la escena en milisegundos para clasificar si se trata de un vehículo, una persona no autorizada o un falso positivo. Envío de clip de vídeo en alta definición a los operadores.",
    points: [
      "Clasificación instantánea de objetivos por IA",
      "Grabación continua en búfer previo al evento",
      "Certificación legal de salto real para envío a Policía",
    ],
  },
  {
    step: "03",
    name: "Intervención SOC & Fuerzas de Seguridad",
    latency: "< 15 segundos",
    icon: PhoneCall,
    tag: "RESPUESTA PRIORITARIA",
    title: "Aviso directo a Policía y patrullas de guardia",
    description:
      "Nuestra Central Receptora de Alarmas homologada confirma el incidente y activa el protocolo de emergencia con las Fuerzas y Cuerpos de Seguridad del Estado y el servicio técnico 24h.",
    points: [
      "Línea prioritaria con Policía Nacional y Guardia Civil",
      "Custodia de llaves y acudida técnica si se requiere",
      "Supervisión continua hasta el restablecimiento seguro",
    ],
  },
  {
    step: "04",
    name: "Control Total y Telemetría en App",
    latency: "En Tiempo Real",
    icon: Smartphone,
    tag: "GESTIÓN AUTÓNOMA",
    title: "Tu seguridad en la palma de tu mano",
    description:
      "Armado por zonas, histórico de eventos auditable, control de cámaras en directo y recepción de notificaciones push de incidencias con total facilidad y cifrado de grado militar.",
    points: [
      "Gestión de permisos por empleado o familiar",
      "Armado/desarmado remoto y alertas instantáneas",
      "Reportes de actividad y cumplimiento exportables",
    ],
  },
];

export function DefenseArchitecture() {
  const [activeStep, setActiveStep] = useState(0);

  return (
    <section
      className="border-y border-slate-200/80 bg-slate-50/70 px-4 py-20 sm:px-6 md:py-28"
      aria-labelledby="defense-flow"
    >
      <div className="mx-auto max-w-6xl">
        <Reveal>
          <div className="text-center">
            <p className="inline-flex items-center gap-1.5 rounded-full border border-slate-200 bg-white px-3 py-1 font-mono text-xs font-semibold text-slate-700 shadow-2xs">
              <Radio className="size-3 text-primary animate-pulse" />
              PROTOCOLO DE RESPUESTA INTEGRADA
            </p>
            <h2
              id="defense-flow"
              className="mt-3 text-3xl font-bold tracking-tight text-slate-900 sm:text-4xl"
            >
              Cómo funciona el escudo defensivo de Control 61
            </h2>
            <p className="mx-auto mt-3 max-w-2xl text-base text-slate-600">
              Un proceso milimétricamente estructurado que combina hardware homologado, inteligencia
              artificial y respuesta humana experta en segundos.
            </p>
          </div>
        </Reveal>

        {/* Interactive Step Navigator */}
        <div className="mt-12 grid grid-cols-2 gap-3 sm:grid-cols-4">
          {layers.map((layer, idx) => {
            const Icon = layer.icon;
            const isActive = activeStep === idx;
            return (
              <button
                key={layer.step}
                onClick={() => setActiveStep(idx)}
                className={`relative flex flex-col items-start rounded-xl border p-4 text-left transition-all duration-200 ${
                  isActive
                    ? "border-primary bg-white shadow-sm ring-1 ring-primary/20"
                    : "border-slate-200 bg-white/60 hover:border-slate-300 hover:bg-white"
                }`}
              >
                <div className="flex w-full items-center justify-between">
                  <span
                    className={`font-mono text-xs font-bold ${
                      isActive ? "text-primary" : "text-slate-400"
                    }`}
                  >
                    FASE {layer.step}
                  </span>
                  <Icon className={`size-4 ${isActive ? "text-primary" : "text-slate-400"}`} />
                </div>
                <p className="mt-2 text-xs font-semibold text-slate-900 sm:text-sm">{layer.name}</p>
                <span className="mt-1 flex items-center gap-1 font-mono text-[11px] text-slate-500">
                  <Clock className="size-3" />
                  {layer.latency}
                </span>
                {isActive ? (
                  <div className="absolute -bottom-[9px] left-1/2 -translate-x-1/2 rounded-full bg-primary p-1 text-white shadow-xs">
                    <ChevronRight className="size-2.5 rotate-90" />
                  </div>
                ) : null}
              </button>
            );
          })}
        </div>

        {/* Active Step Showcase Card */}
        <div className="mt-8 overflow-hidden rounded-2xl border border-slate-200 bg-white p-6 shadow-sm sm:p-10">
          <div className="grid items-center gap-8 lg:grid-cols-12">
            <div className="lg:col-span-7">
              <div className="inline-flex items-center gap-2 rounded-md border border-red-100 bg-red-50 px-2.5 py-1 text-xs font-semibold text-primary font-mono">
                <span>FASE {layers[activeStep].step}</span>
                <span>·</span>
                <span>{layers[activeStep].tag}</span>
              </div>

              <h3 className="mt-4 text-2xl font-bold tracking-tight text-slate-900 sm:text-3xl">
                {layers[activeStep].title}
              </h3>

              <p className="mt-3 text-base leading-relaxed text-slate-600">
                {layers[activeStep].description}
              </p>

              <div className="mt-6 space-y-3">
                {layers[activeStep].points.map((pt, i) => (
                  <div key={i} className="flex items-start gap-3">
                    <CheckCircle2 className="mt-0.5 size-4 text-primary shrink-0" />
                    <span className="text-sm font-medium text-slate-700">{pt}</span>
                  </div>
                ))}
              </div>
            </div>

            <div className="lg:col-span-5">
              <div className="rounded-xl border border-slate-100 bg-slate-900 p-6 text-slate-100 shadow-md">
                <div className="flex items-center justify-between border-b border-slate-800 pb-3 font-mono text-xs text-slate-400">
                  <span>TELEMETRÍA EN VIVO</span>
                  <span className="text-emerald-400">● 100% OPERATIVO</span>
                </div>

                <div className="mt-4 space-y-3 font-mono text-xs">
                  <div className="flex justify-between border-b border-slate-800/60 pb-2">
                    <span className="text-slate-400">Fase Actual:</span>
                    <span className="font-semibold text-slate-200">{layers[activeStep].name}</span>
                  </div>
                  <div className="flex justify-between border-b border-slate-800/60 pb-2">
                    <span className="text-slate-400">Tiempo de Acción:</span>
                    <span className="font-semibold text-emerald-400">
                      {layers[activeStep].latency}
                    </span>
                  </div>
                  <div className="flex justify-between border-b border-slate-800/60 pb-2">
                    <span className="text-slate-400">Canal de Transmisión:</span>
                    <span className="text-slate-200">Doble Vía 5G + Fibra Encriptada</span>
                  </div>
                  <div className="flex justify-between">
                    <span className="text-slate-400">Supervisión:</span>
                    <span className="text-slate-200">Operadores Homologados 24h</span>
                  </div>
                </div>

                <div className="mt-5 rounded-lg bg-slate-800/80 p-3 text-[11px] text-slate-300">
                  ⚡ Conexión directa y certificada según Ley 5/2014 de Seguridad Privada.
                </div>
              </div>
            </div>
          </div>
        </div>
      </div>
    </section>
  );
}
