const modules = import.meta.glob<{ default: string }>("../assets/clientes/*.png", { eager: true });

const logos = Object.entries(modules)
  .sort(([a], [b]) => a.localeCompare(b))
  .map(([path, mod]) => ({
    src: mod.default,
    name:
      path
        .split("/")
        .pop()
        ?.replace(/\.png$/, "")
        .replace(/-/g, " ") ?? "cliente",
  }));

function Row({ ariaHidden }: { ariaHidden?: boolean }) {
  return (
    <ul
      className="flex shrink-0 items-center gap-4 pr-4"
      aria-hidden={ariaHidden ? "true" : undefined}
    >
      {logos.map((logo) => (
        <li
          key={logo.src}
          className="group flex h-20 w-36 shrink-0 items-center justify-center rounded-xl border border-slate-200 bg-white px-4 shadow-2xs transition-all duration-300 hover:border-slate-300 hover:shadow-sm"
        >
          <img
            src={logo.src}
            alt={ariaHidden ? "" : `Logotipo de ${logo.name}`}
            loading="lazy"
            decoding="async"
            width={300}
            height={188}
            className="max-h-12 w-auto max-w-full object-contain grayscale opacity-75 transition duration-300 group-hover:grayscale-0 group-hover:opacity-100 group-hover:scale-105"
          />
        </li>
      ))}
    </ul>
  );
}

export function ClientLogos({
  title = "Empresas e instituciones que confían en Control 61",
  text,
}: {
  title?: string;
  text?: string;
}) {
  return (
    <section
      className="border-b border-slate-200/80 bg-slate-50/50 py-16"
      aria-labelledby="clients-heading"
    >
      <div className="mx-auto max-w-6xl px-4 sm:px-6">
        <div className="flex flex-col items-center text-center">
          <p className="font-mono text-xs font-semibold uppercase tracking-wider text-slate-500">
            PROTECCIÓN CORPORATIVA COMPROBADA
          </p>
          <h2
            id="clients-heading"
            className="mt-2 text-2xl font-bold tracking-tight text-slate-900 sm:text-3xl"
          >
            {title}
          </h2>
          {text ? <p className="mt-2.5 max-w-2xl text-sm text-slate-600">{text}</p> : null}
        </div>
      </div>

      <div
        className="marquee-mask relative mt-8 flex overflow-hidden"
        role="region"
        aria-label="Clientes protegidos por Control 61"
      >
        <div className="marquee-track flex min-w-max">
          <Row />
          <Row ariaHidden />
        </div>
      </div>
    </section>
  );
}
