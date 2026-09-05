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
          ? "border-b border-slate-200/80 bg-white/90 shadow-xs backdrop-blur-md"
          : "border-b border-transparent bg-background/80 backdrop-blur-xs"
      }`}
    >
      {/* Top micro-bar for emergency & 24h assistance */}
      <div className="border-b border-slate-100 bg-slate-50/80 px-4 py-1.5 text-xs text-muted-foreground sm:px-6">
        <div className="mx-auto flex max-w-6xl items-center justify-between">
          <div className="flex items-center gap-2 font-mono">
            <span className="relative flex size-2">
              <span className="absolute inline-flex size-full animate-ping rounded-full bg-emerald-400 opacity-75"></span>
              <span className="relative inline-flex size-2 rounded-full bg-emerald-500"></span>
            </span>
            <span className="font-medium text-slate-700">CENTRAL 24/7 OPERATIVA</span>
            <span className="hidden text-slate-300 sm:inline">|</span>
            <span className="hidden sm:inline">Murcia & Levante</span>
          </div>
          <div className="flex items-center gap-4">
            <span className="hidden text-slate-500 md:inline">
              Instalador Homologado REA & RINA ISO
            </span>
            <a
              href={site.phoneHref}
              className="flex items-center gap-1.5 font-semibold text-slate-900 transition-colors hover:text-primary"
            >
              <Phone className="size-3 text-primary" />
              <span>Averías 24h: {site.phone}</span>
            </a>
          </div>
        </div>
      </div>

      <div className="mx-auto flex max-w-6xl items-center justify-between gap-4 px-4 py-3 sm:px-6">
        <Link to="/" className="group flex items-center gap-3" onClick={() => setOpen(false)}>
          <img
            src={logo}
            alt={`${site.brand} — ${site.claim}`}
            width={1242}
            height={496}
            className="h-9 w-auto transition-transform duration-200 group-hover:scale-102"
          />
        </Link>

        {/* Desktop Navigation */}
        <nav aria-label="Principal" className="hidden items-center gap-1 lg:flex">
          {site.nav.map((item) => (
            <Link
              key={item.to}
              to={item.to}
              className="rounded-lg px-3 py-1.5 text-sm font-medium text-slate-600 transition-colors hover:bg-slate-100/80 hover:text-slate-900"
              activeProps={{ className: "text-slate-900 font-semibold bg-slate-100" }}
            >
              {item.label}
            </Link>
          ))}
        </nav>

        {/* Action CTAs */}
        <div className="flex items-center gap-2.5">
          <Link
            to="/contacto"
            className="group relative inline-flex min-h-10 items-center justify-center gap-1.5 overflow-hidden rounded-lg bg-primary px-4 py-2 text-sm font-semibold text-white shadow-xs transition-all duration-200 hover:bg-red-700 hover:shadow-md"
          >
            <span>Estudio Gratuito</span>
            <ArrowUpRight className="size-4 transition-transform duration-200 group-hover:translate-x-0.5 group-hover:-translate-y-0.5" />
          </Link>

          <button
            type="button"
            aria-label={open ? "Cerrar menú" : "Abrir menú"}
            aria-expanded={open}
            onClick={() => setOpen((v) => !v)}
            className="inline-flex size-10 items-center justify-center rounded-lg border border-slate-200 bg-white text-slate-700 hover:bg-slate-50 lg:hidden"
          >
            {open ? <X className="size-5" /> : <Menu className="size-5" />}
          </button>
        </div>
      </div>

      {/* Mobile Drawer */}
      {open ? (
        <nav
          aria-label="Menú móvil"
          className="border-t border-slate-200 bg-white/95 px-6 py-5 backdrop-blur-xl lg:hidden"
        >
          <ul className="flex flex-col space-y-1">
            {site.nav.map((item) => (
              <li key={item.to}>
                <Link
                  to={item.to}
                  onClick={() => setOpen(false)}
                  className="flex items-center justify-between rounded-lg px-3 py-2.5 text-base font-medium text-slate-700 transition-colors hover:bg-slate-50 hover:text-slate-900"
                  activeProps={{ className: "text-primary font-semibold bg-red-50/50" }}
                >
                  <span>{item.label}</span>
                </Link>
              </li>
            ))}
            <li className="pt-2">
              <Link
                to="/contacto"
                onClick={() => setOpen(false)}
                className="flex min-h-11 w-full items-center justify-center gap-2 rounded-lg bg-primary px-4 text-sm font-semibold text-white shadow-sm"
              >
                <ShieldCheck className="size-4" />
                <span>Solicitar Auditoría de Seguridad</span>
              </Link>
            </li>
            <li className="pt-1">
              <a
                href={site.phoneHref}
                className="flex min-h-11 w-full items-center justify-center gap-2 rounded-lg border border-slate-200 bg-slate-50 px-4 text-sm font-medium text-slate-800"
              >
                <Phone className="size-4 text-primary" />
                <span>Llamar ahora: {site.phone}</span>
              </a>
            </li>
          </ul>
        </nav>
      ) : null}
    </header>
  );
}
