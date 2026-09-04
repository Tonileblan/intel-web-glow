import type { LucideIcon } from "lucide-react";

import { Reveal } from "./Reveal";

export type Feature = {
  icon?: LucideIcon;
  title: string;
  text: string;
};

export function FeatureGrid({
  heading,
  intro,
  items,
  id = "detalle",
}: {
  heading: string;
  intro?: string;
  items: readonly Feature[];
  id?: string;
}) {
  return (
    <section className="px-6 py-20" aria-labelledby={id}>
      <div className="mx-auto max-w-6xl">
        <Reveal>
          <h2 id={id} className="text-3xl font-semibold tracking-tight">
            {heading}
          </h2>
          {intro ? (
            <p className="mt-3 max-w-2xl text-muted-foreground">{intro}</p>
          ) : null}
        </Reveal>
        <ul className="mt-10 grid gap-6 sm:grid-cols-2 lg:grid-cols-3">
          {items.map((item, i) => (
            <Reveal key={item.title} delay={i * 0.06}>
              <li className="h-full rounded-xl border border-border bg-card p-6 transition-colors hover:border-primary">
                {item.icon ? (
                  <item.icon className="size-6 text-primary" aria-hidden="true" />
                ) : null}
                <h3 className="mt-4 text-lg font-medium">{item.title}</h3>
                <p className="mt-2 text-sm text-muted-foreground">{item.text}</p>
              </li>
            </Reveal>
          ))}
        </ul>
      </div>
    </section>
  );
}
