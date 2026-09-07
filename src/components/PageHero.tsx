import { Link } from "@tanstack/react-router";
import type { ReactNode } from "react";
import { ArrowUpRight, Sparkles } from "lucide-react";

export function PageHero({
  eyebrow,
  title,
  text,
  image,
  imageAlt,
  children,
}: {
  eyebrow?: string;
  title: ReactNode;
  text?: ReactNode;
  image?: string;
  imageAlt?: string;
  children?: ReactNode;
}) {
  return (
    <section className="relative isolate overflow-hidden border-b border-slate-800/80 bg-tech-grid py-16 sm:py-20 md:py-24">
      {/* Background Image if present */}
      {image ? (
        <>
          <img
            src={image}
            alt={imageAlt ?? ""}
            width={1920}
            height={1080}
            className="absolute inset-0 -z-10 size-full object-cover opacity-20"
          />
          <div
            className="absolute inset-0 -z-10 bg-gradient-to-r from-slate-950 via-slate-950/90 to-slate-950/40"
            aria-hidden="true"
          />
        </>
      ) : null}

      {/* Ambient Glow */}
      <div className="pointer-events-none absolute -top-32 left-1/3 -z-10 h-80 w-80 rounded-full bg-red-600/10 blur-[120px]" />

      <div className="mx-auto max-w-6xl px-4 sm:px-6">
        <div className="animate-in fade-in slide-in-from-bottom-3 duration-500">
          {eyebrow ? (
            <p className="inline-flex items-center gap-1.5 rounded-full border border-red-500/30 bg-red-950/40 px-3.5 py-1 font-mono text-xs font-semibold uppercase tracking-wider text-red-400 shadow-md">
              <Sparkles className="size-3.5" />
              {eyebrow}
            </p>
          ) : null}
          <h1 className="mt-4 max-w-4xl text-3xl font-extrabold tracking-tight text-white sm:text-4xl md:text-5xl md:leading-tight">
            {title}
          </h1>
          {text ? (
            <p className="mt-4 max-w-2xl text-base text-slate-300 sm:text-lg leading-relaxed">
              {text}
            </p>
          ) : null}
          {children ?? (
            <div className="mt-8">
              <Link
                to="/contacto"
                className="inline-flex min-h-12 items-center gap-2 rounded-xl bg-primary px-6 text-sm font-semibold text-white shadow-lg transition-all hover:bg-red-600 hover:shadow-red-600/30"
              >
                <span>Solicitar valoración gratuita</span>
                <ArrowUpRight className="size-4" />
              </Link>
            </div>
          )}
        </div>
      </div>
    </section>
  );
}
