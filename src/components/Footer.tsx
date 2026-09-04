import { Link } from "@tanstack/react-router";
import { Mail, MapPin, Phone } from "lucide-react";

import logo from "@/assets/Logo-Limpio.png";
import selloRea from "@/assets/Registro-de-Empresas-Acreditadas.png";
import selloRina from "@/assets/Rina-Iso2-1.png";
import { site } from "@/lib/site";

export function Footer() {
  return (
    <footer className="border-t border-border bg-card">
      <div className="mx-auto grid max-w-6xl gap-10 px-6 py-14 md:grid-cols-4">
        <div className="md:col-span-2">
          <img
            src={logo}
            alt={site.brand}
            width={1242}
            height={496}
            loading="lazy"
            className="h-9 w-auto"
          />
          <p className="mt-4 max-w-sm text-sm text-muted-foreground">
            {site.legalName}. Más de 20 años protegiendo empresas, instituciones y hogares
            en la Región de Murcia.
          </p>
          <div className="mt-6 flex flex-wrap items-center gap-4">
            <img
              src={selloRina}
              alt="Certificación ISO 9001, ISO 14001 e ISO 45001 emitida por RINA"
              width={1200}
              height={628}
              loading="lazy"
              className="h-14 w-auto rounded bg-white/95 p-1"
            />
            <img
              src={selloRea}
              alt="Registro de Empresas Acreditadas (REA)"
              width={1080}
              height={680}
              loading="lazy"
              className="h-14 w-auto rounded bg-white/95 p-1"
            />
          </div>
        </div>

        <div>
          <h2 className="text-sm font-semibold uppercase tracking-widest text-muted-foreground">
            Servicios
          </h2>
          <ul className="mt-4 space-y-2 text-sm">
            {site.nav.map((item) => (
              <li key={item.to}>
                <Link
                  to={item.to}
                  className="text-muted-foreground transition-colors hover:text-foreground"
                >
                  {item.label}
                </Link>
              </li>
            ))}
          </ul>
        </div>

        <div>
          <h2 className="text-sm font-semibold uppercase tracking-widest text-muted-foreground">
            Contacto
          </h2>
          <ul className="mt-4 space-y-3 text-sm text-muted-foreground">
            <li className="flex gap-2">
              <Phone className="mt-0.5 size-4 shrink-0 text-primary" aria-hidden="true" />
              <a href={site.phoneHref} className="hover:text-foreground">
                {site.phone}
              </a>
            </li>
            <li className="flex gap-2">
              <Mail className="mt-0.5 size-4 shrink-0 text-primary" aria-hidden="true" />
              <a href={`mailto:${site.email}`} className="hover:text-foreground">
                {site.email}
              </a>
            </li>
            <li className="flex gap-2">
              <MapPin
                className="mt-0.5 size-4 shrink-0 text-primary"
                aria-hidden="true"
              />
              <span>{site.address}</span>
            </li>
          </ul>
        </div>
      </div>

      <div className="border-t border-border px-6 py-6">
        <div className="mx-auto flex max-w-6xl flex-wrap items-center justify-between gap-3 text-xs text-muted-foreground">
          <p>
            © {new Date().getFullYear()} {site.legalName}
          </p>
          <ul className="flex flex-wrap gap-4">
            {site.legalNav.map((item) => (
              <li key={item.to}>
                <Link to={item.to} className="hover:text-foreground">
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
