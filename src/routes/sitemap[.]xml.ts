import { createFileRoute } from "@tanstack/react-router";

const BASE_URL = "https://intel-web-glow.lovable.app";

const paths = [
  { path: "/", priority: "1.0" },
  { path: "/empresas", priority: "0.9" },
  { path: "/instituciones", priority: "0.9" },
  { path: "/hogar", priority: "0.9" },
  { path: "/cctv", priority: "0.8" },
  { path: "/obra-nueva", priority: "0.7" },
  { path: "/mantenimiento", priority: "0.8" },
  { path: "/acreditaciones", priority: "0.7" },
  { path: "/nosotros", priority: "0.6" },
  { path: "/contacto", priority: "0.8" },
  { path: "/aviso-legal", priority: "0.2" },
  { path: "/privacidad", priority: "0.2" },
  { path: "/cookies", priority: "0.2" },
];

export const Route = createFileRoute("/sitemap.xml")({
  server: {
    handlers: {
      GET: () => {
        const body = `<?xml version="1.0" encoding="UTF-8"?>
<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">
${paths
  .map(
    ({ path, priority }) =>
      `  <url>\n    <loc>${BASE_URL}${path === "/" ? "/" : path}</loc>\n    <changefreq>weekly</changefreq>\n    <priority>${priority}</priority>\n  </url>`,
  )
  .join("\n")}
</urlset>
`;
        return new Response(body, {
          headers: { "content-type": "application/xml; charset=utf-8" },
        });
      },
    },
  },
});
