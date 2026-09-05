import { Link } from "@tanstack/react-router";
import { Mail, MapPin, Phone, ShieldCheck, Clock, ArrowUpRight } from "lucide-react";

import logo from "@/assets/Logo-Limpio.png";
import selloRea from "@/assets/Registro-de-Empresas-Acreditadas.png";
import selloRina from "@/assets/Rina-Iso2-1.png";
import { site } from "@/lib/site";

export function Footer() {
  return (
    <footer className="border-t border-slate-200 bg-slate-900 text-slate-300">
      {/* Top Banner */}
      <div className="border-b border-slate-800 bg-slate-950 px-4 py-8 sm:px-6">
        <div className="mx-auto flex max-w-6xl flex-col items-center justify-between gap-4 text-center sm:flex-row sm:text-left">
          <div className="flex items-center gap-3">
            <div className="flex size-10 items-center justify-center rounded-lg bg-red-500/10 text-primary">
              <ShieldCheck className="size-5" />
            </div>
            <div>
              <p className="font-semibold text-white">Central de Asistencia y Averías 24/7</p>
              <p className="text-xs text-slate-400">
                Atención ininterrumpida para todos nuestros clientes de Murcia y Levante
              </p>
            </div>
          </div>
          <a
            href={site.phoneHref}
            className="inline-flex items-center gap-2 rounded-lg bg-primary px-4 py-2 text-sm font-semibold text-white shadow-xs transition-colors hover:bg-red-700"
          >
            <Phone className="size-4" />
            <span>{site.phone}</span>
          </a>
        </div>
      </div>

      <div className="mx-auto grid max-w-6xl gap-10 px-4 py-16 sm:px-6 lg:grid-cols-12">
        {/* Brand & Mission */}
        <div className="lg:col-span-5">
          <img
            src={logo}
            alt={site.brand}
            width={1242}
            height={496}
            loading="lazy"
            className="h-9 w-auto brightness-0 invert"
          />
          <p className="mt-4 max-w-sm text-sm leading-relaxed text-slate-400">
            {site.legalName}. Más de dos décadas desarrollando ingeniería de seguridad avanzada,
            CCTV con IA, control de accesos y alarmas conectadas a CRA en la Región de Murcia.
          </p>

          <div className="mt-6 flex flex-wrap items-center gap-3">
            <img
              src={selloRina}
              alt="Certificación ISO 9001, ISO 14001 e ISO 45001 emitida por RINA"
              width={1200}
              height={628}
              loading="lazy"
              className="h-12 w-auto rounded border border-slate-800 bg-white p-1"
            />
            <img
              src={selloRea}
              alt="Registro de Empresas Acreditadas (REA)"
              width={1080}
              height={680}
              loading="lazy"
              className="h-12 w-auto rounded border border-slate-800 bg-white p-1"
            />
          </div>

          <p className="mt-4 text-xs font-mono text-slate-500">
            Inscrita en el Registro de Seguridad Privada · Acreditada REA · Inscrita en Industria
            para PCI
          </p>
        </div>

        {/* Services Navigation */}
        <div className="lg:col-span-3">
          <h4 className="font-mono text-xs font-semibold uppercase tracking-wider text-white">
            Soluciones de Seguridad
          </h4>
          <ul className="mt-4 space-y-2.5 text-sm">
            {site.nav.map((item) => (
              <li key={item.to}>
                <Link to={item.to} className="text-slate-400 transition-colors hover:text-white">
                  {item.label}
                </Link>
              </li>
            ))}
            {site.extraNav.map((item) => (
              <li key={item.to}>
                <Link to={item.to} className="text-slate-400 transition-colors hover:text-white">
                  {item.label}
                </Link>
              </li>
            ))}
          </ul>
        </div>

        {/* Contact Info */}
        <div className="lg:col-span-4">
          <h4 className="font-mono text-xs font-semibold uppercase tracking-wider text-white">
            Oficinas Centrales & Contacto
          </h4>
          <ul className="mt-4 space-y-3 text-sm text-slate-400">
            <li className="flex items-start gap-3">
              <Phone className="mt-0.5 size-4 text-primary shrink-0" />
              <div>
                <a href={site.phoneHref} className="font-medium text-slate-200 hover:text-white">
                  {site.phone}
                </a>
                <span className="block text-xs text-slate-500">
                  Atención comercial y técnica 24h
                </span>
              </div>
            </li>
            <li className="flex items-start gap-3">
              <Mail className="mt-0.5 size-4 text-primary shrink-0" />
              <div>
                <a href={`mailto:${site.email}`} className="text-slate-200 hover:text-white">
                  {site.email}
                </a>
                <span className="block text-xs text-slate-500">Respuesta en menos de 2 horas</span>
              </div>
            </li>
            <li className="flex items-start gap-3">
              <MapPin className="mt-0.5 size-4 text-primary shrink-0" />
              <span className="text-xs leading-relaxed text-slate-400">{site.address}</span>
            </li>
            <li className="flex items-start gap-3">
              <Clock className="mt-0.5 size-4 text-primary shrink-0" />
              <span className="text-xs text-slate-400">{site.schedule}</span>
            </li>
          </ul>
        </div>
      </div>

      {/* Bottom Legal bar */}
      <div className="border-t border-slate-800 bg-slate-950 px-4 py-6 sm:px-6">
        <div className="mx-auto flex max-w-6xl flex-col items-center justify-between gap-4 text-xs text-slate-500 sm:flex-row">
          <p>
            © {new Date().getFullYear()} {site.legalName} — Todos los derechos reservados.
          </p>
          <ul className="flex flex-wrap gap-4">
            {site.legalNav.map((item) => (
              <li key={item.to}>
                <Link to={item.to} className="transition-colors hover:text-slate-300">
                  {item.label}
                </Link>
              </li>
            ))}
          </ul>
        </div>
      </div>
    </footer>
  );
}
