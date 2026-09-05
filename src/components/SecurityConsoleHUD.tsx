import { useState, useEffect } from "react";
import {
  Camera,
  Radar,
  Fingerprint,
  Radio,
  ShieldCheck,
  Activity,
  Maximize2,
  CheckCircle2,
  Lock,
} from "lucide-react";

type Mode = "cctv" | "radar" | "access" | "soc";

const cameras = [
  {
    id: "cam-1",
    name: "CAM-01 · Acceso Naves & Logística",
    img: "https://images.unsplash.com/photo-1557597774-9d273605dfa9?auto=format&fit=crop&w=900&q=80",
    resolution: "4K UHD 60fps",
    detection: "Persona detectada (Fiabilidad 99.4%)",
    status: "Normal · Grabación Continua",
  },
  {
    id: "cam-2",
    name: "CAM-02 · Perímetro Exterior Norte",
    img: "https://images.unsplash.com/photo-1545324418-cc1a3fa10c00?auto=format&fit=crop&w=900&q=80",
    resolution: "4K HDR Térmica",
    detection: "Barrera Infrarroja Armada",
    status: "Zona Segura · Cero Intrusión",
  },
  {
    id: "cam-3",
    name: "CAM-03 · Centro de Control & Racks",
    img: "https://images.unsplash.com/photo-1558494949-ef010cbdcc31?auto=format&fit=crop&w=900&q=80",
    resolution: "1080p UltraLowLight",
    detection: "Control Biométrico Activo",
    status: "Acceso Restringido Nivel 3",
  },
];

const accessLogs = [
  {
    time: "14:32:10",
    user: "G. Martínez (Operaciones)",
    method: "RFID Cifrado DESFire",
    zone: "Torno Acceso Norte",
    state: "Autorizado",
  },
  {
    time: "14:30:45",
    user: "M. Torres (Dirección Técnica)",
    method: "Biometría Facial IA",
    zone: "Puerta CPD Principal",
    state: "Autorizado",
  },
  {
    time: "14:28:12",
    user: "Vehículo Matrícula 4821-LMR",
    method: "LPR Lectura Automática",
    zone: "Barrera Muelle Carga",
    state: "Autorizado",
  },
  {
    time: "14:25:01",
    user: "Prueba Protocolo Anti-Sabotaje",
    method: "Test Redundancia CRA",
    zone: "Línea 4G/Fibra",
    state: "Verificado",
  },
];

export function SecurityConsoleHUD() {
  const [mode, setMode] = useState<Mode>("cctv");
  const [selectedCam, setSelectedCam] = useState(0);
  const [currentTime, setCurrentTime] = useState("");

  useEffect(() => {
    const update = () => {
      const d = new Date();
      setCurrentTime(
        `${d.toLocaleTimeString("es-ES", { hour12: false })}.${Math.floor(d.getMilliseconds() / 100)}`,
      );
    };
    update();
    const timer = setInterval(update, 100);
    return () => clearInterval(timer);
  }, []);

  return (
    <div className="relative mx-auto w-full max-w-5xl overflow-hidden rounded-2xl border border-slate-800 bg-slate-950 text-slate-100 shadow-2xl">
      {/* HUD Header Bar */}
      <div className="flex flex-wrap items-center justify-between border-b border-slate-800 bg-slate-900/90 px-4 py-2.5 text-xs font-mono text-slate-400">
        <div className="flex items-center gap-3">
          <div className="flex items-center gap-1.5">
            <span className="relative flex size-2">
              <span className="absolute inline-flex size-full animate-ping rounded-full bg-emerald-400 opacity-75"></span>
              <span className="relative inline-flex size-2 rounded-full bg-emerald-500"></span>
            </span>
            <span className="font-semibold text-slate-200">CONTROL61_SOC://MURCIA</span>
          </div>
          <span className="hidden text-slate-600 sm:inline">|</span>
          <span className="hidden text-emerald-400 sm:inline">● GRADO 3 HOMOLOGADO</span>
        </div>

        <div className="flex items-center gap-4 text-slate-400">
          <span className="hidden md:inline">ENCRIPTACIÓN: AES-256</span>
          <span className="hidden md:inline text-slate-600">|</span>
          <span className="font-mono text-slate-300">HORA_UTC: {currentTime || "12:00:00.0"}</span>
        </div>
      </div>

      {/* Mode Switcher Tabs */}
      <div className="flex border-b border-slate-800 bg-slate-900/60 p-1.5">
        <button
          onClick={() => setMode("cctv")}
          className={`flex flex-1 items-center justify-center gap-2 rounded-lg px-3 py-2 text-xs font-semibold transition-all ${
            mode === "cctv"
              ? "bg-slate-800 text-white shadow-sm ring-1 ring-slate-700"
              : "text-slate-400 hover:bg-slate-800/50 hover:text-slate-200"
          }`}
        >
          <Camera className={`size-3.5 ${mode === "cctv" ? "text-red-500" : ""}`} />
          <span>CCTV con IA</span>
        </button>

        <button
          onClick={() => setMode("radar")}
          className={`flex flex-1 items-center justify-center gap-2 rounded-lg px-3 py-2 text-xs font-semibold transition-all ${
            mode === "radar"
              ? "bg-slate-800 text-white shadow-sm ring-1 ring-slate-700"
              : "text-slate-400 hover:bg-slate-800/50 hover:text-slate-200"
          }`}
        >
          <Radar className={`size-3.5 ${mode === "radar" ? "text-emerald-400" : ""}`} />
          <span>Radar & Sensores</span>
        </button>

        <button
          onClick={() => setMode("access")}
          className={`flex flex-1 items-center justify-center gap-2 rounded-lg px-3 py-2 text-xs font-semibold transition-all ${
            mode === "access"
              ? "bg-slate-800 text-white shadow-sm ring-1 ring-slate-700"
              : "text-slate-400 hover:bg-slate-800/50 hover:text-slate-200"
          }`}
        >
          <Fingerprint className={`size-3.5 ${mode === "access" ? "text-sky-400" : ""}`} />
          <span>Control Accesos</span>
        </button>

        <button
          onClick={() => setMode("soc")}
          className={`flex flex-1 items-center justify-center gap-2 rounded-lg px-3 py-2 text-xs font-semibold transition-all ${
            mode === "soc"
              ? "bg-slate-800 text-white shadow-sm ring-1 ring-slate-700"
              : "text-slate-400 hover:bg-slate-800/50 hover:text-slate-200"
          }`}
        >
          <Radio className={`size-3.5 ${mode === "soc" ? "text-amber-400" : ""}`} />
          <span>Telemetría SOC</span>
        </button>
      </div>

      {/* Mode Content Views */}
      <div className="relative min-h-[340px] p-4 sm:p-6">
        {mode === "cctv" && (
          <div className="grid gap-4 lg:grid-cols-3">
            {/* Main Camera Screen */}
            <div className="relative overflow-hidden rounded-xl border border-slate-800 bg-black lg:col-span-2">
              <img
                src={cameras[selectedCam].img}
                alt={cameras[selectedCam].name}
                className="h-64 w-full object-cover opacity-80 transition-all duration-300 sm:h-80"
              />

              {/* HUD Screen Overlays */}
              <div className="absolute inset-0 bg-gradient-to-t from-black/80 via-transparent to-black/50 p-4">
                <div className="flex items-start justify-between">
                  <div className="flex items-center gap-2 rounded-md bg-black/60 px-2.5 py-1 text-xs font-mono text-white backdrop-blur-md">
                    <span className="size-2 rounded-full bg-red-500 animate-pulse" />
                    <span>REC ● LIVE</span>
                    <span className="text-slate-400">[{cameras[selectedCam].resolution}]</span>
                  </div>

                  <div className="rounded-md bg-black/60 px-2.5 py-1 text-xs font-mono text-emerald-400 backdrop-blur-md">
                    IA_OBJECT_TRACKING: ON
                  </div>
                </div>

                {/* AI Detection Bounding Box Visualizer */}
                <div className="absolute left-1/3 top-1/4 rounded-lg border-2 border-dashed border-emerald-400/90 bg-emerald-500/10 p-2 text-xs font-mono text-emerald-300 backdrop-blur-xs">
                  <div className="flex items-center gap-1 font-semibold">
                    <Activity className="size-3" />
                    <span>PERSONA IDENTIFICADA [0.99]</span>
                  </div>
                  <span className="text-[10px] text-slate-300">ZONA PERMITIDA · MOV. REGULAR</span>
                </div>

                {/* Bottom Screen Data */}
                <div className="absolute bottom-4 left-4 right-4 flex items-center justify-between text-xs font-mono">
                  <div>
                    <p className="font-semibold text-white">{cameras[selectedCam].name}</p>
                    <p className="text-slate-400">{cameras[selectedCam].status}</p>
                  </div>
                  <button
                    type="button"
                    className="flex size-7 items-center justify-center rounded-md bg-white/10 text-white hover:bg-white/20"
                    aria-label="Maximizar cámara"
                  >
                    <Maximize2 className="size-3.5" />
                  </button>
                </div>
              </div>
            </div>

            {/* Camera Channel Selector */}
            <div className="flex flex-col gap-2">
              <p className="font-mono text-xs font-semibold uppercase tracking-wider text-slate-400">
                Canales de Vídeo Activos (3/16)
              </p>
              {cameras.map((cam, idx) => (
                <button
                  key={cam.id}
                  onClick={() => setSelectedCam(idx)}
                  className={`flex items-start gap-3 rounded-xl border p-2.5 text-left transition-all ${
                    selectedCam === idx
                      ? "border-red-500/80 bg-red-950/20 text-white"
                      : "border-slate-800 bg-slate-900/60 text-slate-400 hover:border-slate-700 hover:bg-slate-900"
                  }`}
                >
                  <img
                    src={cam.img}
                    alt=""
                    className="size-12 rounded-lg object-cover ring-1 ring-slate-800"
                  />
                  <div className="min-w-0 flex-1">
                    <div className="flex items-center justify-between">
                      <p className="truncate text-xs font-medium text-slate-200">{cam.name}</p>
                      {selectedCam === idx ? (
                        <span className="size-2 rounded-full bg-red-500" />
                      ) : null}
                    </div>
                    <p className="mt-0.5 text-[11px] font-mono text-slate-400">{cam.resolution}</p>
                    <p className="mt-0.5 text-[10px] text-emerald-400">{cam.detection}</p>
                  </div>
                </button>
              ))}

              <div className="mt-auto rounded-lg border border-slate-800 bg-slate-900/50 p-3 text-xs text-slate-400">
                <p className="flex items-center gap-1.5 font-medium text-slate-300">
                  <ShieldCheck className="size-3.5 text-primary" />
                  Almacenamiento Conforme a RGPD
                </p>
                <p className="mt-1 text-[11px] text-slate-500">
                  Grabación continua cifrada en NVR local + copia redundante en nube de alta
                  seguridad.
                </p>
              </div>
            </div>
          </div>
        )}

        {mode === "radar" && (
          <div className="grid gap-4 md:grid-cols-2">
            <div className="relative flex min-h-[260px] flex-col items-center justify-center rounded-xl border border-slate-800 bg-slate-900/80 p-6 text-center">
              <div className="relative flex size-36 items-center justify-center rounded-full border border-emerald-500/30 bg-emerald-950/20">
                <div className="absolute size-24 rounded-full border border-emerald-500/40" />
                <div className="absolute size-12 rounded-full border border-emerald-500/60" />
                <div className="absolute size-2 rounded-full bg-emerald-400" />
                <div className="animate-radar-ping absolute size-32 rounded-full border border-emerald-400/50" />
              </div>
              <div className="mt-4 font-mono text-xs text-emerald-400">
                ● BARRIDO PERIMETRAL: ACTIVO (360°)
              </div>
              <p className="mt-1 text-xs text-slate-400">
                12 detectores perimetrales sincronizados
              </p>
            </div>

            <div className="flex flex-col justify-between space-y-3 rounded-xl border border-slate-800 bg-slate-900/60 p-5">
              <div>
                <h4 className="font-mono text-xs font-semibold text-slate-200">
                  ESTADO DE SENSORES Y GRADO DE SEGURIDAD
                </h4>
                <div className="mt-3 space-y-2.5 font-mono text-xs">
                  <div className="flex items-center justify-between rounded-lg bg-slate-950/60 p-2.5">
                    <span className="text-slate-300">Barreras Infrarrojas Exteriores</span>
                    <span className="inline-flex items-center gap-1 text-emerald-400">
                      <CheckCircle2 className="size-3" /> NORMAL
                    </span>
                  </div>
                  <div className="flex items-center justify-between rounded-lg bg-slate-950/60 p-2.5">
                    <span className="text-slate-300">Detectores Volumétricos Microondas</span>
                    <span className="inline-flex items-center gap-1 text-emerald-400">
                      <CheckCircle2 className="size-3" /> ACTIVO
                    </span>
                  </div>
                  <div className="flex items-center justify-between rounded-lg bg-slate-950/60 p-2.5">
                    <span className="text-slate-300">Sensores Sísmicos & Apertura</span>
                    <span className="inline-flex items-center gap-1 text-emerald-400">
                      <CheckCircle2 className="size-3" /> ARMADO
                    </span>
                  </div>
                  <div className="flex items-center justify-between rounded-lg bg-slate-950/60 p-2.5">
                    <span className="text-slate-300">Anti-Inhibición Doble Vía (5G/Fibra)</span>
                    <span className="inline-flex items-center gap-1 text-emerald-400">
                      <CheckCircle2 className="size-3" /> ONLINE
                    </span>
                  </div>
                </div>
              </div>
            </div>
          </div>
        )}

        {mode === "access" && (
          <div className="rounded-xl border border-slate-800 bg-slate-900/80 p-4 sm:p-5">
            <div className="flex items-center justify-between border-b border-slate-800 pb-3">
              <div className="flex items-center gap-2">
                <Lock className="size-4 text-sky-400" />
                <h4 className="font-mono text-xs font-semibold text-slate-200">
                  REGISTRO DE ACCESOS EN TIEMPO REAL
                </h4>
              </div>
              <span className="font-mono text-[11px] text-emerald-400">14 PUERTAS AUDITADAS</span>
            </div>

            <div className="mt-3 space-y-2 font-mono text-xs">
              {accessLogs.map((log, i) => (
                <div
                  key={i}
                  className="flex flex-col justify-between gap-1 rounded-lg border border-slate-800/80 bg-slate-950/60 p-2.5 sm:flex-row sm:items-center"
                >
                  <div className="flex items-center gap-2">
                    <span className="text-slate-500">{log.time}</span>
                    <span className="font-medium text-slate-200">{log.user}</span>
                  </div>
                  <div className="flex items-center gap-3 text-slate-400">
                    <span className="text-[11px] text-slate-400">{log.zone}</span>
                    <span className="rounded bg-emerald-500/10 px-2 py-0.5 text-[10px] font-semibold text-emerald-400">
                      {log.state}
                    </span>
                  </div>
                </div>
              ))}
            </div>
          </div>
        )}

        {mode === "soc" && (
          <div className="grid gap-4 sm:grid-cols-3">
            <div className="rounded-xl border border-slate-800 bg-slate-900/80 p-4 text-center">
              <p className="font-mono text-xs text-slate-400">TIEMPO DE RESPUESTA SOC</p>
              <p className="mt-2 font-mono text-3xl font-bold text-emerald-400">&lt; 15 seg</p>
              <p className="mt-1 text-xs text-slate-500">Verificación y aviso prioritario</p>
            </div>
            <div className="rounded-xl border border-slate-800 bg-slate-900/80 p-4 text-center">
              <p className="font-mono text-xs text-slate-400">DISPONIBILIDAD CONEXIÓN</p>
              <p className="mt-2 font-mono text-3xl font-bold text-sky-400">99.99%</p>
              <p className="mt-1 text-xs text-slate-500">Enlace redundante fibra + 5G</p>
            </div>
            <div className="rounded-xl border border-slate-800 bg-slate-900/80 p-4 text-center">
              <p className="font-mono text-xs text-slate-400">CERTIFICACIÓN LEGAL</p>
              <p className="mt-2 font-mono text-3xl font-bold text-primary">GRADO 2/3</p>
              <p className="mt-1 text-xs text-slate-500">Reg. Seguridad Privada Nº 4410</p>
            </div>
          </div>
        )}
      </div>

      {/* Console Footer */}
      <div className="flex flex-wrap items-center justify-between border-t border-slate-800 bg-slate-950 px-4 py-2.5 text-xs text-slate-400">
        <div className="flex items-center gap-2">
          <ShieldCheck className="size-3.5 text-primary" />
          <span>Monitorización ininterrumpida los 365 días del año</span>
        </div>
        <a
          href="/contacto"
          className="font-semibold text-slate-200 hover:text-white hover:underline"
        >
          Proteger mis instalaciones con Control 61 →
        </a>
      </div>
    </div>
  );
}
