import { Star, ShieldCheck, Quote, Building, Award } from "lucide-react";
import { Reveal } from "./Reveal";
import selloRea from "@/assets/Registro-de-Empresas-Acreditadas.png";
import selloRina from "@/assets/Rina-Iso2-1.png";
import { Link } from "@tanstack/react-router";

const testimonials = [
  {
    quote:
      "La analítica de CCTV con IA y el control perimetral redujeron a cero los conatos de intrusión en nuestras naves de Molina de Segura. Saber que detrás hay un equipo técnico que atiende las averías 24h nos da una tranquilidad total.",
    author: "Javier M. Rocamora",
    role: "Director de Operaciones y Logística",
    sector: "Sector Industrial & Transporte",
    stars: 5,
    highlight: "Cero incidentes en 3 años",
  },
  {
    quote:
      "Gestionamos más de 30 comunidades de propietarios en Murcia y siempre recomendamos Control 61. Sus presupuestos son 100% transparentes, sin contratos trampa, y la gestión de accesos y cámaras cumple escrupulosamente con el RGPD.",
    author: "Carmen Balsalobre",
    role: "Administradora de Fincas Colegiada",
    sector: "Residencial & Urbanizaciones",
    stars: 5,
    highlight: "Más de 30 fincas protegidas",
  },
  {
    quote:
      "En proyectos para dependencias municipales necesitamos empresas que acrediten homologación oficial, REA y normativas ISO. Control 61 ejecutó el despliegue técnico con una profesionalidad y rapidez intachable.",
    author: "Francisco J. Navarro",
    role: "Responsable Técnico de Infraestructuras",
    sector: "Administración e Instituciones",
    stars: 5,
    highlight: "Cumplimiento normativo 100%",
  },
];

export function TestimonialsSection() {
  return (
    <section className="px-4 py-20 sm:px-6 md:py-28" aria-labelledby="testimonios">
      <div className="mx-auto max-w-6xl">
        {/* Header */}
        <Reveal>
          <div className="text-center">
            <p className="inline-flex items-center gap-1.5 rounded-full border border-slate-800 bg-slate-900 px-3.5 py-1 text-xs font-semibold uppercase tracking-wider text-slate-300">
              <ShieldCheck className="size-3.5 text-red-500" />
              Confianza & Experiencia Acreditada
            </p>
            <h2
              id="testimonios"
              className="mt-3 text-3xl font-bold tracking-tight text-white sm:text-4xl"
            >
              Más de 20 años protegiendo lo que más importa
            </h2>
            <p className="mx-auto mt-3 max-w-2xl text-base text-slate-300">
              La satisfacción de más de 2.500 empresas, comunidades y particulares en la Región de
              Murcia es nuestro mejor aval.
            </p>
          </div>
        </Reveal>

        {/* Testimonials Grid */}
        <div className="mt-14 grid gap-6 md:grid-cols-3">
          {testimonials.map((item, i) => (
            <Reveal key={item.author} delay={i * 0.08}>
              <div className="relative flex h-full flex-col justify-between rounded-2xl border border-slate-800 bg-slate-900/70 p-6 shadow-xl backdrop-blur-md transition-all duration-300 hover:border-red-500/40 hover:bg-slate-900 sm:p-8">
                <div>
                  <div className="flex items-center justify-between">
                    <div className="flex text-amber-400">
                      {[...Array(item.stars)].map((_, idx) => (
                        <Star key={idx} className="size-4 fill-amber-400" />
                      ))}
                    </div>
                    <span className="rounded-md border border-slate-700 bg-slate-800 px-2 py-0.5 font-mono text-[11px] font-semibold text-slate-300">
                      {item.highlight}
                    </span>
                  </div>

                  <Quote className="mt-4 size-6 text-red-500/40" />

                  <p className="mt-2 text-sm leading-relaxed text-slate-200">"{item.quote}"</p>
                </div>

                <div className="mt-6 border-t border-slate-800 pt-4">
                  <p className="font-semibold text-white">{item.author}</p>
                  <p className="text-xs text-slate-400">{item.role}</p>
                  <p className="mt-0.5 text-[11px] font-medium text-red-400">{item.sector}</p>
                </div>
              </div>
            </Reveal>
          ))}
        </div>

        {/* Official Certifications Banner */}
        <Reveal delay={0.25}>
          <div className="mt-14 rounded-2xl border border-slate-800 bg-slate-900/80 p-6 shadow-xl backdrop-blur-md sm:p-8">
            <div className="flex flex-col items-center justify-between gap-6 lg:flex-row">
              <div className="max-w-xl text-center lg:text-left">
                <div className="inline-flex items-center gap-1.5 font-mono text-xs font-semibold uppercase text-slate-300">
                  <Award className="size-4 text-red-500" />
                  Garantía de Calidad y Cumplimiento Normativo
                </div>
                <h3 className="mt-2 text-xl font-bold text-white">
                  Empresa Homologada y Certificada por Organismos Oficiales
                </h3>
                <p className="mt-2 text-sm text-slate-300">
                  Contamos con las certificaciones RINA ISO 9001, ISO 14001, ISO 45001, acreditación
                  REA e inscripción oficial en el Registro de Seguridad Privada.
                </p>
              </div>

              <div className="flex flex-wrap items-center justify-center gap-4">
                <img
                  src={selloRina}
                  alt="Certificación ISO 9001, ISO 14001 e ISO 45001 emitida por RINA"
                  width={1200}
                  height={628}
                  loading="lazy"
                  className="h-14 w-auto rounded-lg border border-slate-700 bg-white/95 p-1.5 shadow-md"
                />
                <img
                  src={selloRea}
                  alt="Registro de Empresas Acreditadas (REA) Ministerio de Trabajo"
                  width={1080}
                  height={680}
                  loading="lazy"
                  className="h-14 w-auto rounded-lg border border-slate-700 bg-white/95 p-1.5 shadow-md"
                />
                <Link
                  to="/acreditaciones"
                  className="inline-flex items-center gap-1.5 rounded-xl border border-slate-700 bg-slate-800 px-4 py-2.5 text-xs font-semibold text-white shadow-md transition-colors hover:bg-slate-700 hover:text-red-300"
                >
                  <span>Ver todas las acreditaciones</span>
                  <span>→</span>
                </Link>
              </div>
            </div>
          </div>
        </Reveal>
      </div>
    </section>
  );
}
