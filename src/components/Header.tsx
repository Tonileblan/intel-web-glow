import { Link } from "@tanstack/react-router";
import { Menu, Phone, ShieldCheck, X, ArrowUpRight } from "lucide-react";
import { useEffect, useState } from "react";

import logo from "@/assets/Logo-Limpio.png";
import { site } from "@/lib/site";

export function Header() {
  const [open, setOpen] = useState(false);
  const [scrolled, setScrolled] = useState(false);

  useEffect(() => {
    const onScroll = () => setScrolled(window.scrollY > 12);
    onScroll();
    window.addEventListener("scroll", onScroll, { passive: true });
    return () => window.removeEventListener("scroll", onScroll);
  }, []);

  return (
    <header
      className={`sticky top-0 z-50 transition-all duration-300 ${
        scrolled
          ? "border-b border-slate-800/80 bg-slate-950/90 shadow-2xl backdrop-blur-xl"
          : "border-b border-white/[0.05] bg-slate-950/75 backdrop-blur-md"
      }`}
    >
      {/* Top micro-bar for emergency & 24h assistance */}
      <div className="border-b border-slate-800/60 bg-slate-900/50 px-4 py-1.5 text-xs text-slate-400 sm:px-6">
        <div className="mx-auto flex max-w-6xl items-center justify-between">
          <div className="flex items-center gap-2 font-mono">
            <span className="relative flex size-2">
              <span className="absolute inline-flex size-full animate-ping rounded-full bg-emerald-400 opacity-75"></span>
              <span className="relative inline-flex size-2 rounded-full bg-emerald-500"></span>
            </span>
            <span className="font-medium text-slate-200">CENTRAL 24/7 OPERATIVA</span>
            <span className="hidden text-slate-700 sm:inline">|</span>
            <span className="hidden text-slate-400 sm:inline">Murcia & Levante</span>
          </div>
          <div className="flex items-center gap-4">
            <span className="hidden text-slate-400 md:inline">
              Instalador Homologado REA & RINA ISO
            </span>
            <a
              href={site.phoneHref}
              className="flex items-center gap-1.5 font-semibold text-slate-200 transition-colors hover:text-red-400"
            >
              <Phone className="size-3 text-red-500" />
              <span>Averías 24h: {site.phone}</span>
            </a>
          </div>
        </div>
      </div>

      <div className="mx-auto flex max-w-6xl items-center justify-between gap-4 px-4 py-3 sm:px-6">
        <Link to="/" className="group flex items-center gap-3" onClick={() => setOpen(false)}>
          <div className="rounded-lg bg-white/95 p-1 transition-all duration-200 group-hover:bg-white group-hover:shadow-md">
            <img
              src={logo}
              alt={`${site.brand} — ${site.claim}`}
              width={1242}
              height={496}
              className="h-8 w-auto"
            />
          </div>
        </Link>

        {/* Desktop Navigation */}
        <nav aria-label="Principal" className="hidden items-center gap-1 lg:flex">
          {site.nav.map((item) => (
            <Link
              key={item.to}
              to={item.to}
              className="rounded-lg px-3 py-1.5 text-sm font-medium text-slate-300 transition-colors hover:bg-slate-800/80 hover:text-white"
              activeProps={{
                className: "text-white font-semibold bg-slate-800 ring-1 ring-slate-700",
              }}
            >
              {item.label}
            </Link>
          ))}
        </nav>

        {/* Action CTAs */}
        <div className="flex items-center gap-2.5">
          <Link
            to="/contacto"
            className="group relative inline-flex min-h-10 items-center justify-center gap-1.5 overflow-hidden rounded-lg bg-primary px-4 py-2 text-sm font-semibold text-white shadow-lg transition-all duration-200 hover:bg-red-600 hover:shadow-red-600/30"
          >
            <span>Estudio Gratuito</span>
            <ArrowUpRight className="size-4 transition-transform duration-200 group-hover:translate-x-0.5 group-hover:-translate-y-0.5" />
          </Link>

          <button
            type="button"
            aria-label={open ? "Cerrar menú" : "Abrir menú"}
            aria-expanded={open}
            onClick={() => setOpen((v) => !v)}
            className="inline-flex size-10 items-center justify-center rounded-lg border border-slate-800 bg-slate-900 text-slate-200 hover:bg-slate-800 lg:hidden"
          >
            {open ? <X className="size-5" /> : <Menu className="size-5" />}
          </button>
        </div>
      </div>

      {/* Mobile Drawer */}
      {open ? (
        <nav
          aria-label="Menú móvil"
          className="border-t border-slate-800 bg-slate-950/95 px-6 py-5 backdrop-blur-2xl lg:hidden"
        >
          <ul className="flex flex-col space-y-1">
            {site.nav.map((item) => (
              <li key={item.to}>
                <Link
                  to={item.to}
                  onClick={() => setOpen(false)}
                  className="flex items-center justify-between rounded-lg px-3 py-2.5 text-base font-medium text-slate-300 transition-colors hover:bg-slate-900 hover:text-white"
                  activeProps={{
                    className: "text-red-400 font-semibold bg-red-950/30 ring-1 ring-red-900/40",
                  }}
                >
                  <span>{item.label}</span>
                </Link>
              </li>
            ))}
            <li className="pt-3">
              <Link
                to="/contacto"
                onClick={() => setOpen(false)}
                className="flex min-h-11 w-full items-center justify-center gap-2 rounded-lg bg-primary px-4 text-sm font-semibold text-white shadow-md hover:bg-red-600"
              >
                <ShieldCheck className="size-4" />
                <span>Solicitar Auditoría de Seguridad</span>
              </Link>
            </li>
            <li className="pt-1.5">
              <a
                href={site.phoneHref}
                className="flex min-h-11 w-full items-center justify-center gap-2 rounded-lg border border-slate-800 bg-slate-900 px-4 text-sm font-medium text-slate-200 hover:bg-slate-800"
              >
                <Phone className="size-4 text-red-500" />
                <span>Llamar ahora: {site.phone}</span>
              </a>
            </li>
          </ul>
        </nav>
      ) : null}
    </header>
  );
}
