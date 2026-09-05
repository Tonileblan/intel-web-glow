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
    <section className="relative isolate overflow-hidden border-b border-slate-200/80 bg-tech-grid py-16 sm:py-20 md:py-24">
      {/* Background Image if present */}
      {image ? (
        <>
          <img
            src={image}
            alt={imageAlt ?? ""}
            width={1920}
            height={1080}
            className="absolute inset-0 -z-10 size-full object-cover opacity-15"
          />
          <div
            className="absolute inset-0 -z-10 bg-gradient-to-r from-background via-background/95 to-background/50"
            aria-hidden="true"
          />
        </>
      ) : null}

      <div className="mx-auto max-w-6xl px-4 sm:px-6">
        <div className="animate-in fade-in slide-in-from-bottom-3 duration-500">
          {eyebrow ? (
            <p className="inline-flex items-center gap-1.5 rounded-full border border-red-200 bg-white px-3 py-1 font-mono text-xs font-semibold uppercase tracking-wider text-primary shadow-2xs">
              <Sparkles className="size-3.5" />
              {eyebrow}
            </p>
          ) : null}
          <h1 className="mt-4 max-w-4xl text-3xl font-extrabold tracking-tight text-slate-900 sm:text-4xl md:text-5xl md:leading-tight">
            {title}
          </h1>
          {text ? (
            <p className="mt-4 max-w-2xl text-base text-slate-600 sm:text-lg leading-relaxed">
              {text}
            </p>
          ) : null}
          {children ?? (
            <div className="mt-8">
              <Link
                to="/contacto"
                className="inline-flex min-h-12 items-center gap-2 rounded-xl bg-primary px-6 text-sm font-semibold text-white shadow-xs transition-all hover:bg-red-700 hover:shadow-md"
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
