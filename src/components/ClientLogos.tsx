const modules = import.meta.glob<{ default: string }>(
  "../assets/clientes/*.png",
  { eager: true },
);

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
      className="flex shrink-0 items-center gap-6 pr-6"
      aria-hidden={ariaHidden ? "true" : undefined}
    >
      {logos.map((logo) => (
        <li key={logo.src} className="flex h-24 w-40 shrink-0 items-center justify-center rounded-lg bg-card px-4 shadow-sm">
          <img
            src={logo.src}
            alt={ariaHidden ? "" : `Logotipo de cliente de Control 61`}
            loading="lazy"
            decoding="async"
            width={300}
            height={188}
            className="h-16 w-auto max-w-full object-contain transition duration-300 hover:scale-105"
          />
        </li>
      ))}
    </ul>
  );
}

export function ClientLogos({
  title = "Empresas e instituciones que confían en nosotros",
  text,
}: {
  title?: string;
  text?: string;
}) {
  return (
    <section className="border-b border-border bg-secondary/40 py-16">
      <div className="mx-auto max-w-6xl px-6">
        <h2 className="text-2xl font-semibold tracking-tight md:text-3xl">{title}</h2>
        {text ? (
          <p className="mt-3 max-w-2xl text-muted-foreground">{text}</p>
        ) : null}
      </div>

      <div
        className="marquee-mask relative mt-10 flex overflow-hidden"
        role="region"
        aria-label="Clientes de Control 61"
      >
        <div className="marquee-track flex min-w-max">
          <Row />
          <Row ariaHidden />
        </div>
      </div>
    </section>
  );
}
