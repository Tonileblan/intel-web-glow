import { Link } from "@tanstack/react-router";
import type { ReactNode } from "react";

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
    <section className="relative isolate overflow-hidden border-b border-border">
      {image ? (
        <>
          <img
            src={image}
            alt={imageAlt ?? ""}
            width={1920}
            height={1080}
            className="absolute inset-0 -z-10 size-full object-cover opacity-45"
          />
          <div
            className="absolute inset-0 -z-10 bg-gradient-to-t from-background via-background/85 to-background/55"
            aria-hidden="true"
          />
        </>
      ) : null}
      <div className="mx-auto max-w-6xl px-6 py-20 md:py-28">
        <div className="animate-in fade-in slide-in-from-bottom-4 duration-700">
          {eyebrow ? (
            <p className="text-xs font-semibold uppercase tracking-[0.2em] text-primary">
              {eyebrow}
            </p>
          ) : null}
          <h1 className="mt-4 max-w-3xl text-4xl font-semibold leading-tight tracking-tight md:text-5xl">
            {title}
          </h1>
          {text ? (
            <p className="mt-6 max-w-2xl text-lg text-muted-foreground">{text}</p>
          ) : null}
          {children ?? (
            <div className="mt-8">
              <Link
                to="/contacto"
                className="inline-flex min-h-11 items-center rounded-md bg-primary px-5 text-sm font-medium text-primary-foreground transition-colors hover:bg-primary/90"
              >
                Solicitar valoración gratuita
              </Link>
            </div>
          )}
        </div>
      </div>
    </section>
  );
}
