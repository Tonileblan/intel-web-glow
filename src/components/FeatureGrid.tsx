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
    <section className="px-4 py-20 sm:px-6 md:py-24" aria-labelledby={id}>
      <div className="mx-auto max-w-6xl">
        <Reveal>
          <div className="max-w-2xl">
            <h2 id={id} className="text-3xl font-bold tracking-tight text-slate-900 sm:text-4xl">
              {heading}
            </h2>
            {intro ? (
              <p className="mt-3 text-base leading-relaxed text-slate-600">{intro}</p>
            ) : null}
          </div>
        </Reveal>
        <ul className="mt-12 grid gap-6 sm:grid-cols-2 lg:grid-cols-3">
          {items.map((item, i) => (
            <Reveal key={item.title} delay={i * 0.05}>
              <li className="group flex h-full flex-col justify-between rounded-2xl border border-slate-200 bg-white p-6 shadow-xs transition-all duration-300 hover:border-slate-300 hover:shadow-md sm:p-7">
                <div>
                  {item.icon ? (
                    <div className="inline-flex size-11 items-center justify-center rounded-xl bg-slate-50 text-primary ring-1 ring-slate-200 transition-colors group-hover:bg-red-50">
                      <item.icon className="size-5" aria-hidden="true" />
                    </div>
                  ) : null}
                  <h3 className="mt-5 text-lg font-bold text-slate-900">{item.title}</h3>
                  <p className="mt-2 text-sm leading-relaxed text-slate-600">{item.text}</p>
                </div>
              </li>
            </Reveal>
          ))}
        </ul>
      </div>
    </section>
  );
}
