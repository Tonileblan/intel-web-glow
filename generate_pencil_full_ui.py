import json

def make_doc():
    doc = {
        "version": "2.19",
        "children": []
    }

    # =========================================================================
    # SCREEN 1: FULL DESKTOP HOMEPAGE & INDUSTRIAL PORTAL (1440 x 4900)
    # =========================================================================
    landing = {
        "type": "frame",
        "id": "control61-landing",
        "name": "🖥️ 01. Landing Page Corporativa & Industrial (1440px)",
        "x": 0,
        "y": 0,
        "width": 1440,
        "height": 4900,
        "fill": "#070A11",
        "layout": "vertical",
        "clip": True,
        "children": [
            # 1.1 Emergency Top Bar
            {
                "type": "frame",
                "id": "l-emergency-bar",
                "name": "Barra de Alerta y Estado CRA",
                "width": "fill_container",
                "height": 42,
                "fill": "#0F172A",
                "stroke": "#06B6D433",
                "strokeWidth": { "bottom": 1 },
                "layout": "horizontal",
                "padding": [0, 48],
                "alignItems": "center",
                "justifyContent": "space_between",
                "children": [
                    {
                        "type": "frame",
                        "id": "l-cra-badge",
                        "name": "CRA Status",
                        "layout": "horizontal",
                        "gap": 8,
                        "alignItems": "center",
                        "children": [
                            {
                                "type": "ellipse",
                                "id": "l-dot-live",
                                "name": "Pulsing Dot",
                                "width": 8,
                                "height": 8,
                                "fill": "#10B981"
                            },
                            {
                                "type": "text",
                                "id": "l-cra-status-t",
                                "name": "Text",
                                "content": "CENTRAL RECEPTORA DE ALARMAS 24/7/365 · HOMOLOGACIÓN DGP Nº 2341 · GRADO 3",
                                "fontSize": 11,
                                "fontWeight": "bold",
                                "fill": "#38BDF8",
                                "letterSpacing": 0.5
                            }
                        ]
                    },
                    {
                        "type": "frame",
                        "id": "l-top-links",
                        "name": "Direct Contacts",
                        "layout": "horizontal",
                        "gap": 24,
                        "alignItems": "center",
                        "children": [
                            {
                                "type": "text",
                                "id": "l-phone-24h",
                                "name": "Phone",
                                "content": "🚨 Teléfono Centralita Urgencias: 968 622 984",
                                "fontSize": 12,
                                "fontWeight": "600",
                                "fill": "#F1F5F9"
                            },
                            {
                                "type": "text",
                                "id": "l-portal-link",
                                "name": "Link",
                                "content": "Acceso Clientes CRA →",
                                "fontSize": 12,
                                "fontWeight": "bold",
                                "fill": "#22D3EE"
                            }
                        ]
                    }
                ]
            },
            # 1.2 Main Navbar
            {
                "type": "frame",
                "id": "l-navbar",
                "name": "Navbar Principal Glassmorphism",
                "width": "fill_container",
                "height": 80,
                "fill": "#0B1120EE",
                "stroke": "#FFFFFF14",
                "strokeWidth": { "bottom": 1 },
                "layout": "horizontal",
                "padding": [0, 48],
                "alignItems": "center",
                "justifyContent": "space_between",
                "children": [
                    {
                        "type": "frame",
                        "id": "l-brand-group",
                        "name": "Brand Identity",
                        "layout": "horizontal",
                        "gap": 12,
                        "alignItems": "center",
                        "children": [
                            {
                                "type": "frame",
                                "id": "l-logo-box",
                                "name": "Shield Box",
                                "width": 46,
                                "height": 46,
                                "fill": "#0891B226",
                                "stroke": "#06B6D4",
                                "strokeWidth": 1.5,
                                "cornerRadius": 10,
                                "alignItems": "center",
                                "justifyContent": "center",
                                "children": [
                                    {
                                        "type": "icon",
                                        "id": "l-shield-ico",
                                        "name": "Shield Icon",
                                        "library": "lucide",
                                        "icon": "shield-check",
                                        "width": 26,
                                        "height": 26,
                                        "fill": "#06B6D4"
                                    }
                                ]
                            },
                            {
                                "type": "frame",
                                "id": "l-brand-texts",
                                "name": "Brand Text",
                                "layout": "vertical",
                                "gap": 2,
                                "children": [
                                    {
                                        "type": "text",
                                        "id": "l-brand-name",
                                        "name": "Name",
                                        "content": "CONTROL 61",
                                        "fontSize": 20,
                                        "fontWeight": "800",
                                        "fill": "#FFFFFF",
                                        "letterSpacing": 1.5
                                    },
                                    {
                                        "type": "text",
                                        "id": "l-brand-sub",
                                        "name": "Sub",
                                        "content": "SISTEMAS INTELIGENTES DE SEGURIDAD",
                                        "fontSize": 9,
                                        "fontWeight": "600",
                                        "fill": "#94A3B8",
                                        "letterSpacing": 0.8
                                    }
                                ]
                            }
                        ]
                    },
                    {
                        "type": "frame",
                        "id": "l-nav-links",
                        "name": "Menu Links",
                        "layout": "horizontal",
                        "gap": 28,
                        "alignItems": "center",
                        "children": [
                            { "type": "text", "id": "nl-1", "name": "Item", "content": "Alarmas Grado 3", "fontSize": 14, "fontWeight": "600", "fill": "#F1F5F9" },
                            { "type": "text", "id": "nl-2", "name": "Item", "content": "CCTV & Visión IA", "fontSize": 14, "fontWeight": "500", "fill": "#94A3B8" },
                            { "type": "text", "id": "nl-3", "name": "Item", "content": "Control de Accesos", "fontSize": 14, "fontWeight": "500", "fill": "#94A3B8" },
                            { "type": "text", "id": "nl-4", "name": "Item", "content": "Central Receptora 24h", "fontSize": 14, "fontWeight": "500", "fill": "#94A3B8" },
                            { "type": "text", "id": "nl-5", "name": "Item", "content": "Sistemas PCI", "fontSize": 14, "fontWeight": "500", "fill": "#94A3B8" },
                            { "type": "text", "id": "nl-6", "name": "Item", "content": "Acreditaciones", "fontSize": 14, "fontWeight": "500", "fill": "#94A3B8" }
                        ]
                    },
                    {
                        "type": "frame",
                        "id": "l-nav-ctas",
                        "name": "CTA Actions",
                        "layout": "horizontal",
                        "gap": 16,
                        "alignItems": "center",
                        "children": [
                            {
                                "type": "frame",
                                "id": "l-btn-phone",
                                "name": "Phone CTA",
                                "height": 42,
                                "padding": [0, 16],
                                "fill": "#1E293B80",
                                "stroke": "#FFFFFF26",
                                "strokeWidth": 1,
                                "cornerRadius": 8,
                                "layout": "horizontal",
                                "gap": 8,
                                "alignItems": "center",
                                "children": [
                                    { "type": "icon", "id": "l-ico-ph", "name": "Phone", "library": "lucide", "icon": "phone", "width": 14, "height": 14, "fill": "#EF4444" },
                                    { "type": "text", "id": "l-ph-txt", "name": "Txt", "content": "968 622 984", "fontSize": 13, "fontWeight": "600", "fill": "#F1F5F9" }
                                ]
                            },
                            {
                                "type": "frame",
                                "id": "l-btn-audit",
                                "name": "Primary CTA",
                                "height": 42,
                                "padding": [0, 20],
                                "fill": "#06B6D4",
                                "cornerRadius": 8,
                                "alignItems": "center",
                                "justifyContent": "center",
                                "children": [
                                    { "type": "text", "id": "l-audit-txt", "name": "Txt", "content": "Solicitar Valoración Gratuita", "fontSize": 13, "fontWeight": "700", "fill": "#070A11" }
                                ]
                            }
                        ]
                    }
                ]
            },
            # 1.3 Hero Section
            {
                "type": "frame",
                "id": "l-hero-section",
                "name": "Hero Section Industrial",
                "width": "fill_container",
                "height": 720,
                "fill": "#070A11",
                "layout": "horizontal",
                "padding": [64, 48],
                "gap": 48,
                "alignItems": "center",
                "justifyContent": "space_between",
                "children": [
                    {
                        "type": "frame",
                        "id": "l-hero-left",
                        "name": "Hero Left Content",
                        "width": 640,
                        "layout": "vertical",
                        "gap": 24,
                        "children": [
                            {
                                "type": "frame",
                                "id": "l-hero-badge",
                                "name": "Badge",
                                "height": 32,
                                "padding": [0, 14],
                                "fill": "#0891B226",
                                "stroke": "#06B6D466",
                                "strokeWidth": 1,
                                "cornerRadius": 20,
                                "layout": "horizontal",
                                "gap": 8,
                                "alignItems": "center",
                                "children": [
                                    { "type": "icon", "id": "l-h-ico", "name": "Ico", "library": "lucide", "icon": "shield-alert", "width": 14, "height": 14, "fill": "#22D3EE" },
                                    { "type": "text", "id": "l-h-btxt", "name": "Txt", "content": "HOMOLOGACIÓN NACIONAL DGP Nº 2341 · CERTIFICACIÓN GRADO 3", "fontSize": 11, "fontWeight": "700", "fill": "#22D3EE", "letterSpacing": 0.5 }
                                ]
                            },
                            {
                                "type": "text",
                                "id": "l-hero-h1",
                                "name": "Headline",
                                "content": "Sistemas de Seguridad Avanzada, CCTV con IA y Alarmas de Grado 3",
                                "fontSize": 46,
                                "fontWeight": "800",
                                "fill": "#FFFFFF",
                                "lineHeight": 1.15,
                                "textGrowth": "fixed-width",
                                "width": 640
                            },
                            {
                                "type": "text",
                                "id": "l-hero-desc",
                                "name": "Description",
                                "content": "Ingeniería e instalación homologada de alarmas de Grado 2 y 3, videovigilancia perimetral de alta precisión y control de accesos para industrias, recintos logísticos e instituciones en Murcia y todo el Levante.",
                                "fontSize": 16,
                                "fontWeight": "400",
                                "fill": "#94A3B8",
                                "lineHeight": 1.6,
                                "textGrowth": "fixed-width",
                                "width": 620
                            },
                            {
                                "type": "frame",
                                "id": "l-hero-cta-group",
                                "name": "CTA Row",
                                "layout": "horizontal",
                                "gap": 16,
                                "alignItems": "center",
                                "children": [
                                    {
                                        "type": "frame",
                                        "id": "l-h-pbtn",
                                        "name": "Main CTA",
                                        "height": 52,
                                        "padding": [0, 26],
                                        "fill": "#06B6D4",
                                        "cornerRadius": 10,
                                        "layout": "horizontal",
                                        "gap": 10,
                                        "alignItems": "center",
                                        "children": [
                                            { "type": "text", "id": "l-hpb-txt", "name": "Txt", "content": "Solicitar Valoración Gratuita", "fontSize": 15, "fontWeight": "700", "fill": "#070A11" },
                                            { "type": "icon", "id": "l-hpb-ico", "name": "Arrow", "library": "lucide", "icon": "arrow-up-right", "width": 18, "height": 18, "fill": "#070A11" }
                                        ]
                                    },
                                    {
                                        "type": "frame",
                                        "id": "l-h-sbtn",
                                        "name": "Secondary CTA",
                                        "height": 52,
                                        "padding": [0, 22],
                                        "fill": "#1E293B66",
                                        "stroke": "#38BDF84D",
                                        "strokeWidth": 1.5,
                                        "cornerRadius": 10,
                                        "layout": "horizontal",
                                        "gap": 10,
                                        "alignItems": "center",
                                        "children": [
                                            { "type": "icon", "id": "l-hsb-ico", "name": "Play", "library": "lucide", "icon": "phone", "width": 18, "height": 18, "fill": "#EF4444" },
                                            { "type": "text", "id": "l-hsb-txt", "name": "Txt", "content": "968 622 984 · Averías 24h", "fontSize": 14, "fontWeight": "600", "fill": "#F1F5F9" }
                                        ]
                                    }
                                ]
                            },
                            {
                                "type": "frame",
                                "id": "l-hero-badges",
                                "name": "Trust Badges",
                                "layout": "horizontal",
                                "gap": 28,
                                "alignItems": "center",
                                "children": [
                                    { "type": "text", "id": "l-tb-1", "name": "B1", "content": "✓ Sin Permanencias Ocultas", "fontSize": 13, "fontWeight": "600", "fill": "#10B981" },
                                    { "type": "text", "id": "l-tb-2", "name": "B2", "content": "✓ Técnicos Propios Homologados", "fontSize": 13, "fontWeight": "600", "fill": "#10B981" },
                                    { "type": "text", "id": "l-tb-3", "name": "B3", "content": "✓ Respuesta CRA < 15s", "fontSize": 13, "fontWeight": "600", "fill": "#10B981" }
                                ]
                            }
                        ]
                    },
                    {
                        "type": "frame",
                        "id": "l-hero-hud",
                        "name": "Live Console HUD Visual",
                        "width": 640,
                        "height": 480,
                        "fill": "#0B1120EE",
                        "stroke": "#06B6D440",
                        "strokeWidth": 1.5,
                        "cornerRadius": 16,
                        "layout": "vertical",
                        "clip": True,
                        "children": [
                            {
                                "type": "frame",
                                "id": "l-hud-hdr",
                                "name": "HUD Header",
                                "width": "fill_container",
                                "height": 46,
                                "fill": "#0F172A",
                                "stroke": "#FFFFFF14",
                                "strokeWidth": { "bottom": 1 },
                                "layout": "horizontal",
                                "padding": [0, 18],
                                "alignItems": "center",
                                "justifyContent": "space_between",
                                "children": [
                                    {
                                        "type": "frame",
                                        "id": "l-hud-tt",
                                        "name": "Title Box",
                                        "layout": "horizontal",
                                        "gap": 8,
                                        "alignItems": "center",
                                        "children": [
                                            { "type": "icon", "id": "l-hh-ico", "name": "Ico", "library": "lucide", "icon": "video", "width": 16, "height": 16, "fill": "#06B6D4" },
                                            { "type": "text", "id": "l-hh-txt", "name": "Txt", "content": "CONTROL61_SOC://MURCIA · GRADO 3 ACTIVO", "fontSize": 11, "fontWeight": "700", "fill": "#F1F5F9" }
                                        ]
                                    },
                                    {
                                        "type": "text",
                                        "id": "l-hud-enc",
                                        "name": "Enc",
                                        "content": "ENCRIPTACIÓN: AES-256 | LATENCIA: 12ms",
                                        "fontSize": 10,
                                        "fontWeight": "bold",
                                        "fill": "#34D399"
                                    }
                                ]
                            },
                            {
                                "type": "frame",
                                "id": "l-hud-cams",
                                "name": "Camera Feeds",
                                "width": "fill_container",
                                "height": 310,
                                "fill": "#030712",
                                "layout": "horizontal",
                                "gap": 12,
                                "padding": [12, 12],
                                "children": [
                                    {
                                        "type": "frame",
                                        "id": "l-cfeed-1",
                                        "name": "CAM 01 Intrusion",
                                        "width": 302,
                                        "height": 286,
                                        "fill": "#0F172A",
                                        "stroke": "#EF444499",
                                        "strokeWidth": 2,
                                        "cornerRadius": 8,
                                        "layout": "vertical",
                                        "justifyContent": "space_between",
                                        "padding": [12, 12],
                                        "children": [
                                            {
                                                "type": "frame",
                                                "id": "l-cf1-t",
                                                "name": "Top",
                                                "layout": "horizontal",
                                                "justifyContent": "space_between",
                                                "children": [
                                                    { "type": "text", "id": "l-cf1-lbl", "name": "Lbl", "content": "CAM-01 · Perímetro Norte", "fontSize": 11, "fontWeight": "bold", "fill": "#FFFFFF" },
                                                    { "type": "text", "id": "l-cf1-rec", "name": "Rec", "content": "● REC IA", "fontSize": 11, "fontWeight": "bold", "fill": "#EF4444" }
                                                ]
                                            },
                                            {
                                                "type": "frame",
                                                "id": "l-cf1-box",
                                                "name": "BBox",
                                                "height": 130,
                                                "fill": "#EF44441A",
                                                "stroke": "#EF4444",
                                                "strokeWidth": 1.5,
                                                "cornerRadius": 6,
                                                "padding": [8, 8],
                                                "layout": "vertical",
                                                "justifyContent": "start",
                                                "children": [
                                                    { "type": "text", "id": "l-cf1-b1", "name": "B1", "content": "⚠️ INTRUSIÓN DETECTADA (99.4% Conf)", "fontSize": 10, "fontWeight": "bold", "fill": "#FCA5A5" },
                                                    { "type": "text", "id": "l-cf1-b2", "name": "B2", "content": "Cruce Barrera Infrarroja Sector 3", "fontSize": 9, "fontWeight": "500", "fill": "#F87171" }
                                                ]
                                            },
                                            {
                                                "type": "frame",
                                                "id": "l-cf1-ft",
                                                "name": "Status",
                                                "fill": "#EF444433",
                                                "padding": [6, 10],
                                                "cornerRadius": 4,
                                                "children": [
                                                    { "type": "text", "id": "l-cf1-stxt", "name": "Txt", "content": "AVISO DIRECTO A POLICÍA ENVIADO", "fontSize": 10, "fontWeight": "bold", "fill": "#FCA5A5" }
                                                ]
                                            }
                                        ]
                                    },
                                    {
                                        "type": "frame",
                                        "id": "l-cfeed-2",
                                        "name": "CAM 02 LPR",
                                        "width": 302,
                                        "height": 286,
                                        "fill": "#0F172A",
                                        "stroke": "#10B98188",
                                        "strokeWidth": 1.5,
                                        "cornerRadius": 8,
                                        "layout": "vertical",
                                        "justifyContent": "space_between",
                                        "padding": [12, 12],
                                        "children": [
                                            {
                                                "type": "frame",
                                                "id": "l-cf2-t",
                                                "name": "Top",
                                                "layout": "horizontal",
                                                "justifyContent": "space_between",
                                                "children": [
                                                    { "type": "text", "id": "l-cf2-lbl", "name": "Lbl", "content": "CAM-02 · Acceso Muelle LPR", "fontSize": 11, "fontWeight": "bold", "fill": "#FFFFFF" },
                                                    { "type": "text", "id": "l-cf2-aut", "name": "Aut", "content": "● AUTORIZADO", "fontSize": 11, "fontWeight": "bold", "fill": "#10B981" }
                                                ]
                                            },
                                            {
                                                "type": "frame",
                                                "id": "l-cf2-box",
                                                "name": "BBox",
                                                "height": 130,
                                                "fill": "#10B9811A",
                                                "stroke": "#10B981",
                                                "strokeWidth": 1.5,
                                                "cornerRadius": 6,
                                                "padding": [8, 8],
                                                "layout": "vertical",
                                                "justifyContent": "start",
                                                "children": [
                                                    { "type": "text", "id": "l-cf2-b1", "name": "B1", "content": "MATRÍCULA: 4821-LMR [Reconocida]", "fontSize": 10, "fontWeight": "bold", "fill": "#86EFAC" },
                                                    { "type": "text", "id": "l-cf2-b2", "name": "B2", "content": "Flota Logística Central · Puerta Abierta", "fontSize": 9, "fontWeight": "500", "fill": "#4ADE80" }
                                                ]
                                            },
                                            {
                                                "type": "frame",
                                                "id": "l-cf2-ft",
                                                "name": "Status",
                                                "fill": "#10B98133",
                                                "padding": [6, 10],
                                                "cornerRadius": 4,
                                                "children": [
                                                    { "type": "text", "id": "l-cf2-stxt", "name": "Txt", "content": "BARRERA AUTOMÁTICA ACCIONADA", "fontSize": 10, "fontWeight": "bold", "fill": "#86EFAC" }
                                                ]
                                            }
                                        ]
                                    }
                                ]
                            },
                            {
                                "type": "frame",
                                "id": "l-hud-ft",
                                "name": "Telemetry Bar",
                                "width": "fill_container",
                                "height": 124,
                                "fill": "#0F172A",
                                "stroke": "#FFFFFF14",
                                "strokeWidth": { "top": 1 },
                                "layout": "horizontal",
                                "padding": [12, 20],
                                "justifyContent": "space_between",
                                "alignItems": "center",
                                "children": [
                                    {
                                        "type": "frame", "id": "l-tel-1", "name": "T1", "layout": "vertical", "gap": 2, "children": [
                                            { "type": "text", "id": "l-t1-l", "name": "L", "content": "TRANSMISIÓN RED", "fontSize": 10, "fontWeight": "bold", "fill": "#64748B" },
                                            { "type": "text", "id": "l-t1-v", "name": "V", "content": "Doble Vía Fibra + 5G", "fontSize": 13, "fontWeight": "700", "fill": "#06B6D4" }
                                        ]
                                    },
                                    {
                                        "type": "frame", "id": "l-tel-2", "name": "T2", "layout": "vertical", "gap": 2, "children": [
                                            { "type": "text", "id": "l-t2-l", "name": "L", "content": "TEST POLICÍA", "fontSize": 10, "fontWeight": "bold", "fill": "#64748B" },
                                            { "type": "text", "id": "l-t2-v", "name": "V", "content": "Conexión Inmediata <15s", "fontSize": 13, "fontWeight": "700", "fill": "#10B981" }
                                        ]
                                    },
                                    {
                                        "type": "frame", "id": "l-tel-3", "name": "T3", "layout": "vertical", "gap": 2, "children": [
                                            { "type": "text", "id": "l-t3-l", "name": "L", "content": "SLA DISPONIBILIDAD", "fontSize": 10, "fontWeight": "bold", "fill": "#64748B" },
                                            { "type": "text", "id": "l-t3-v", "name": "V", "content": "99.9% Operativo", "fontSize": 13, "fontWeight": "700", "fill": "#F59E0B" }
                                        ]
                                    }
                                ]
                            }
                        ]
                    }
                ]
            },
            # 1.4 Stats Bento Strip
            {
                "type": "frame",
                "id": "l-stats-strip",
                "name": "KPIs Strip",
                "width": "fill_container",
                "height": 140,
                "fill": "#0B1120",
                "stroke": "#06B6D426",
                "strokeWidth": { "top": 1, "bottom": 1 },
                "layout": "horizontal",
                "padding": [0, 48],
                "alignItems": "center",
                "justifyContent": "space_between",
                "children": [
                    {
                        "type": "frame", "id": "l-sb-1", "name": "K1", "layout": "vertical", "gap": 4, "children": [
                            { "type": "text", "id": "l-sk-1", "name": "N", "content": "+2.500", "fontSize": 34, "fontWeight": "800", "fill": "#06B6D4" },
                            { "type": "text", "id": "l-sl-1", "name": "D", "content": "Clientes protegidos en Murcia y Levante", "fontSize": 12, "fontWeight": "500", "fill": "#94A3B8" }
                        ]
                    },
                    {
                        "type": "frame", "id": "l-sb-2", "name": "K2", "layout": "vertical", "gap": 4, "children": [
                            { "type": "text", "id": "l-sk-2", "name": "N", "content": "< 15s", "fontSize": 34, "fontWeight": "800", "fill": "#10B981" },
                            { "type": "text", "id": "l-sl-2", "name": "D", "content": "Respuesta inmediata SOC / CRA", "fontSize": 12, "fontWeight": "500", "fill": "#94A3B8" }
                        ]
                    },
                    {
                        "type": "frame", "id": "l-sb-3", "name": "K3", "layout": "vertical", "gap": 4, "children": [
                            { "type": "text", "id": "l-sk-3", "name": "N", "content": "99.9%", "fontSize": 34, "fontWeight": "800", "fill": "#38BDF8" },
                            { "type": "text", "id": "l-sl-3", "name": "D", "content": "Disponibilidad de red y comunicaciones", "fontSize": 12, "fontWeight": "500", "fill": "#94A3B8" }
                        ]
                    },
                    {
                        "type": "frame", "id": "l-sb-4", "name": "K4", "layout": "vertical", "gap": 4, "children": [
                            { "type": "text", "id": "l-sk-4", "name": "N", "content": "20+ Años", "fontSize": 34, "fontWeight": "800", "fill": "#F59E0B" },
                            { "type": "text", "id": "l-sl-4", "name": "D", "content": "Ingeniería de seguridad homologada", "fontSize": 12, "fontWeight": "500", "fill": "#94A3B8" }
                        ]
                    }
                ]
            },
            # 1.5 4-Step Defense Architecture Flow
            {
                "type": "frame",
                "id": "l-defense-arch",
                "name": "Protocolo de Respuesta 4 Pasos",
                "width": "fill_container",
                "fill": "#070A11",
                "layout": "vertical",
                "padding": [80, 48],
                "gap": 40,
                "children": [
                    {
                        "type": "frame",
                        "id": "l-da-hdr",
                        "name": "Header",
                        "layout": "vertical",
                        "gap": 10,
                        "children": [
                            { "type": "text", "id": "l-da-eyebrow", "name": "Eye", "content": "PROTOCOLO DE RESPUESTA INTEGRADA", "fontSize": 12, "fontWeight": "800", "fill": "#EF4444", "letterSpacing": 1 },
                            { "type": "text", "id": "l-da-title", "name": "Title", "content": "Cómo Funciona el Escudo Defensivo de Control 61", "fontSize": 36, "fontWeight": "800", "fill": "#FFFFFF" },
                            { "type": "text", "id": "l-da-sub", "name": "Sub", "content": "Un proceso milimétricamente estructurado que combina hardware homologado, inteligencia artificial y respuesta humana experta en segundos.", "fontSize": 15, "fill": "#94A3B8" }
                        ]
                    },
                    {
                        "type": "frame",
                        "id": "l-da-grid",
                        "name": "4 Steps Row",
                        "layout": "horizontal",
                        "gap": 20,
                        "children": [
                            {
                                "type": "frame", "id": "l-step-1", "name": "Paso 1", "width": 320, "height": 340, "fill": "#0B1120", "stroke": "#38BDF833", "strokeWidth": 1, "cornerRadius": 12, "padding": [24, 20], "layout": "vertical", "justifyContent": "space_between", "children": [
                                    { "type": "frame", "id": "l-st1-top", "name": "Top", "layout": "horizontal", "justifyContent": "space_between", "children": [
                                        { "type": "text", "id": "l-st1-num", "name": "Num", "content": "01", "fontSize": 28, "fontWeight": "800", "fill": "#38BDF8" },
                                        { "type": "text", "id": "l-st1-lat", "name": "Lat", "content": "< 2 seg", "fontSize": 11, "fontWeight": "bold", "fill": "#10B981" }
                                    ]},
                                    { "type": "frame", "id": "l-st1-body", "name": "Body", "layout": "vertical", "gap": 8, "children": [
                                        { "type": "text", "id": "l-st1-t", "name": "T", "content": "Detección Perimetral Anticipada", "fontSize": 16, "fontWeight": "700", "fill": "#FFFFFF" },
                                        { "type": "text", "id": "l-st1-d", "name": "D", "content": "Sensores volumétricos de triple tecnología, barreras infrarrojas y analítica perimetral antes del intento de intrusión.", "fontSize": 12, "fill": "#94A3B8", "lineHeight": 1.5 }
                                    ]},
                                    { "type": "text", "id": "l-st1-ft", "name": "Ft", "content": "● Inmunidad a clima y mascotas", "fontSize": 11, "fontWeight": "600", "fill": "#38BDF8" }
                                ]
                            },
                            {
                                "type": "frame", "id": "l-step-2", "name": "Paso 2", "width": 320, "height": 340, "fill": "#0B1120", "stroke": "#06B6D433", "strokeWidth": 1, "cornerRadius": 12, "padding": [24, 20], "layout": "vertical", "justifyContent": "space_between", "children": [
                                    { "type": "frame", "id": "l-st2-top", "name": "Top", "layout": "horizontal", "justifyContent": "space_between", "children": [
                                        { "type": "text", "id": "l-st2-num", "name": "Num", "content": "02", "fontSize": 28, "fontWeight": "800", "fill": "#06B6D4" },
                                        { "type": "text", "id": "l-st2-lat", "name": "Lat", "content": "< 10 seg", "fontSize": 11, "fontWeight": "bold", "fill": "#10B981" }
                                    ]},
                                    { "type": "frame", "id": "l-st2-body", "name": "Body", "layout": "vertical", "gap": 8, "children": [
                                        { "type": "text", "id": "l-st2-t", "name": "T", "content": "Verificación de Vídeo con IA", "fontSize": 16, "fontWeight": "700", "fill": "#FFFFFF" },
                                        { "type": "text", "id": "l-st2-d", "name": "D", "content": "Algoritmos de visión artificial clasifican objetivos en milisegundos y descartan el 99.8% de falsas alarmas.", "fontSize": 12, "fill": "#94A3B8", "lineHeight": 1.5 }
                                    ]},
                                    { "type": "text", "id": "l-st2-ft", "name": "Ft", "content": "● Búfer HD previo a la alarma", "fontSize": 11, "fontWeight": "600", "fill": "#06B6D4" }
                                ]
                            },
                            {
                                "type": "frame", "id": "l-step-3", "name": "Paso 3", "width": 320, "height": 340, "fill": "#0B1120", "stroke": "#EF444433", "strokeWidth": 1, "cornerRadius": 12, "padding": [24, 20], "layout": "vertical", "justifyContent": "space_between", "children": [
                                    { "type": "frame", "id": "l-st3-top", "name": "Top", "layout": "horizontal", "justifyContent": "space_between", "children": [
                                        { "type": "text", "id": "l-st3-num", "name": "Num", "content": "03", "fontSize": 28, "fontWeight": "800", "fill": "#EF4444" },
                                        { "type": "text", "id": "l-st3-lat", "name": "Lat", "content": "< 15 seg", "fontSize": 11, "fontWeight": "bold", "fill": "#EF4444" }
                                    ]},
                                    { "type": "frame", "id": "l-st3-body", "name": "Body", "layout": "vertical", "gap": 8, "children": [
                                        { "type": "text", "id": "l-st3-t", "name": "T", "content": "Intervención SOC & Policía", "fontSize": 16, "fontWeight": "700", "fill": "#FFFFFF" },
                                        { "type": "text", "id": "l-st3-d", "name": "D", "content": "Central Receptora confirma el incidente y activa el protocolo de emergencia con Policía Nacional y Guardia Civil.", "fontSize": 12, "fill": "#94A3B8", "lineHeight": 1.5 }
                                    ]},
                                    { "type": "text", "id": "l-st3-ft", "name": "Ft", "content": "● Canal prioritario policial", "fontSize": 11, "fontWeight": "600", "fill": "#EF4444" }
                                ]
                            },
                            {
                                "type": "frame", "id": "l-step-4", "name": "Paso 4", "width": 320, "height": 340, "fill": "#0B1120", "stroke": "#10B98133", "strokeWidth": 1, "cornerRadius": 12, "padding": [24, 20], "layout": "vertical", "justifyContent": "space_between", "children": [
                                    { "type": "frame", "id": "l-st4-top", "name": "Top", "layout": "horizontal", "justifyContent": "space_between", "children": [
                                        { "type": "text", "id": "l-st4-num", "name": "Num", "content": "04", "fontSize": 28, "fontWeight": "800", "fill": "#10B981" },
                                        { "type": "text", "id": "l-st4-lat", "name": "Lat", "content": "En Vivo", "fontSize": 11, "fontWeight": "bold", "fill": "#10B981" }
                                    ]},
                                    { "type": "frame", "id": "l-st4-body", "name": "Body", "layout": "vertical", "gap": 8, "children": [
                                        { "type": "text", "id": "l-st4-t", "name": "T", "content": "Control y Telemetría Móvil", "fontSize": 16, "fontWeight": "700", "fill": "#FFFFFF" },
                                        { "type": "text", "id": "l-st4-d", "name": "D", "content": "Armado por zonas, histórico auditable de accesos y visualización de cámaras en tiempo real desde la app.", "fontSize": 12, "fill": "#94A3B8", "lineHeight": 1.5 }
                                    ]},
                                    { "type": "text", "id": "l-st4-ft", "name": "Ft", "content": "● Notificaciones push instantáneas", "fontSize": 11, "fontWeight": "600", "fill": "#10B981" }
                                ]
                            }
                        ]
                    }
                ]
            },
            # 1.6 Why Choose Control 61 Section
            {
                "type": "frame",
                "id": "l-why-section",
                "name": "Por Qué Elegir Control 61",
                "width": "fill_container",
                "fill": "#0B1120",
                "stroke": "#FFFFFF0F",
                "strokeWidth": { "top": 1, "bottom": 1 },
                "layout": "horizontal",
                "padding": [80, 48],
                "gap": 48,
                "alignItems": "center",
                "justifyContent": "space_between",
                "children": [
                    {
                        "type": "frame",
                        "id": "l-why-left",
                        "name": "Left",
                        "width": 500,
                        "layout": "vertical",
                        "gap": 20,
                        "children": [
                            { "type": "text", "id": "l-why-eyebrow", "name": "Eye", "content": "VALOR DIFERENCIAL", "fontSize": 12, "fontWeight": "800", "fill": "#06B6D4", "letterSpacing": 1 },
                            { "type": "text", "id": "l-why-h2", "name": "H2", "content": "Por Qué las Empresas Eligen Control 61", "fontSize": 34, "fontWeight": "800", "fill": "#FFFFFF" },
                            { "type": "text", "id": "l-why-p", "name": "P", "content": "Nacimos con amplia experiencia técnica y operativa en el sector de la seguridad privada. Nuestro trabajo es implementar sistemas fiables que funcionen sin fallos para que dejes de preocuparte por la seguridad de tus instalaciones.", "fontSize": 14, "fill": "#94A3B8", "lineHeight": 1.6 },
                            {
                                "type": "frame", "id": "l-why-certs", "name": "Certs Row", "layout": "horizontal", "gap": 16, "alignItems": "center", "children": [
                                    { "type": "frame", "id": "c-box-1", "name": "RINA", "padding": [8, 14], "fill": "#1E293B", "stroke": "#FFFFFF1A", "strokeWidth": 1, "cornerRadius": 6, "children": [
                                        { "type": "text", "id": "c-t1", "name": "T", "content": "ISO 9001 / 14001 / 45001", "fontSize": 11, "fontWeight": "bold", "fill": "#38BDF8" }
                                    ]},
                                    { "type": "frame", "id": "c-box-2", "name": "REA", "padding": [8, 14], "fill": "#1E293B", "stroke": "#FFFFFF1A", "strokeWidth": 1, "cornerRadius": 6, "children": [
                                        { "type": "text", "id": "c-t2", "name": "T", "content": "Registro REA Acreditado", "fontSize": 11, "fontWeight": "bold", "fill": "#10B981" }
                                    ]}
                                ]
                            }
                        ]
                    },
                    {
                        "type": "frame",
                        "id": "l-why-grid",
                        "name": "4 Reasons Grid",
                        "width": 780,
                        "layout": "vertical",
                        "gap": 16,
                        "children": [
                            {
                                "type": "frame", "id": "l-wg-r1", "name": "Row 1", "layout": "horizontal", "gap": 16, "children": [
                                    { "type": "frame", "id": "l-wcard-1", "name": "Card 1", "width": 382, "height": 130, "fill": "#070A11", "stroke": "#06B6D426", "strokeWidth": 1, "cornerRadius": 10, "padding": [16, 18], "layout": "vertical", "gap": 6, "children": [
                                        { "type": "text", "id": "l-wt-1", "name": "T", "content": "Sin cuotas trampa ni permanencias", "fontSize": 14, "fontWeight": "700", "fill": "#FFFFFF" },
                                        { "type": "text", "id": "l-wd-1", "name": "D", "content": "Presupuestos cerrados y transparentes. Eres dueño de tus equipos sin cláusulas de rescisión ocultas.", "fontSize": 12, "fill": "#94A3B8", "lineHeight": 1.4 }
                                    ]},
                                    { "type": "frame", "id": "l-wcard-2", "name": "Card 2", "width": 382, "height": 130, "fill": "#070A11", "stroke": "#06B6D426", "strokeWidth": 1, "cornerRadius": 10, "padding": [16, 18], "layout": "vertical", "gap": 6, "children": [
                                        { "type": "text", "id": "l-wt-2", "name": "T", "content": "Auditoría previa sobre el terreno", "fontSize": 14, "fontWeight": "700", "fill": "#FFFFFF" },
                                        { "type": "text", "id": "l-wd-2", "name": "D", "content": "Analizamos los accesos y riesgos reales de tu instalación antes de redactar cualquier propuesta técnica.", "fontSize": 12, "fill": "#94A3B8", "lineHeight": 1.4 }
                                    ]}
                                ]
                            },
                            {
                                "type": "frame", "id": "l-wg-r2", "name": "Row 2", "layout": "horizontal", "gap": 16, "children": [
                                    { "type": "frame", "id": "l-wcard-3", "name": "Card 3", "width": 382, "height": 130, "fill": "#070A11", "stroke": "#06B6D426", "strokeWidth": 1, "cornerRadius": 10, "padding": [16, 18], "layout": "vertical", "gap": 6, "children": [
                                        { "type": "text", "id": "l-wt-3", "name": "T", "content": "Técnicos e ingenieros en plantilla", "fontSize": 14, "fontWeight": "700", "fill": "#FFFFFF" },
                                        { "type": "text", "id": "l-wd-3", "name": "D", "content": "Equipo propio homologado con formación continua. Cero subcontratación de calidad cuestionable.", "fontSize": 12, "fill": "#94A3B8", "lineHeight": 1.4 }
                                    ]},
                                    { "type": "frame", "id": "l-wcard-4", "name": "Card 4", "width": 382, "height": 130, "fill": "#070A11", "stroke": "#06B6D426", "strokeWidth": 1, "cornerRadius": 10, "padding": [16, 18], "layout": "vertical", "gap": 6, "children": [
                                        { "type": "text", "id": "l-wt-4", "name": "T", "content": "Servicio de guardia y averías 24h", "fontSize": 14, "fontWeight": "700", "fill": "#FFFFFF" },
                                        { "type": "text", "id": "l-wd-4", "name": "D", "content": "Teléfono atendido por personal técnico de guardia que responde y actúa cuando el sistema falla.", "fontSize": 12, "fill": "#94A3B8", "lineHeight": 1.4 }
                                    ]}
                                ]
                            }
                        ]
                    }
                ]
            },
            # 1.7 Quick Audit Conversion Form Section
            {
                "type": "frame",
                "id": "l-audit-section",
                "name": "Sección de Contacto y Valoración Gratuita",
                "width": "fill_container",
                "height": 400,
                "fill": "#0F172A",
                "stroke": "#06B6D440",
                "strokeWidth": { "top": 1, "bottom": 1 },
                "layout": "horizontal",
                "padding": [48, 64],
                "alignItems": "center",
                "justifyContent": "space_between",
                "children": [
                    {
                        "type": "frame",
                        "id": "l-aud-info",
                        "name": "Info",
                        "width": 620,
                        "layout": "vertical",
                        "gap": 16,
                        "children": [
                            { "type": "text", "id": "l-aud-eyebrow", "name": "Eye", "content": "VALORACIÓN TÉCNICA IN SITU SIN COMPROMISO", "fontSize": 12, "fontWeight": "800", "fill": "#10B981", "letterSpacing": 1 },
                            { "type": "text", "id": "l-aud-title", "name": "Title", "content": "¿Cumple su empresa con la normativa de seguridad privada y grado de riesgo exigido?", "fontSize": 32, "fontWeight": "800", "fill": "#FFFFFF", "lineHeight": 1.2, "textGrowth": "fixed-width", "width": 620 },
                            { "type": "text", "id": "l-aud-desc", "name": "Desc", "content": "Nuestros ingenieros de seguridad realizan un análisis de vulnerabilidades, perímetro, CCTV y adecuación a la Orden INT/316/2011.", "fontSize": 14, "fill": "#94A3B8", "lineHeight": 1.5, "textGrowth": "fixed-width", "width": 600 }
                        ]
                    },
                    {
                        "type": "frame",
                        "id": "l-aud-form",
                        "name": "Form Card",
                        "width": 500,
                        "height": 300,
                        "fill": "#1E293BCC",
                        "stroke": "#06B6D44D",
                        "strokeWidth": 1.5,
                        "cornerRadius": 12,
                        "padding": [24, 24],
                        "layout": "vertical",
                        "justifyContent": "space_between",
                        "children": [
                            { "type": "text", "id": "l-f-title", "name": "Title", "content": "Solicitar Diagnóstico Técnico de Seguridad", "fontSize": 16, "fontWeight": "700", "fill": "#FFFFFF" },
                            { "type": "frame", "id": "l-f-f1", "name": "Field 1", "height": 44, "fill": "#0B1120", "stroke": "#FFFFFF1A", "strokeWidth": 1, "cornerRadius": 6, "padding": [0, 16], "layout": "horizontal", "alignItems": "center", "children": [
                                { "type": "text", "id": "l-f1-ph", "name": "PH", "content": "Nombre de la Empresa o Nave Industrial", "fontSize": 13, "fill": "#64748B" }
                            ]},
                            { "type": "frame", "id": "l-f-f2", "name": "Field 2", "height": 44, "fill": "#0B1120", "stroke": "#FFFFFF1A", "strokeWidth": 1, "cornerRadius": 6, "padding": [0, 16], "layout": "horizontal", "alignItems": "center", "children": [
                                { "type": "text", "id": "l-f2-ph", "name": "PH", "content": "Teléfono de Contacto Directo / Email Corporativo", "fontSize": 13, "fill": "#64748B" }
                            ]},
                            { "type": "frame", "id": "l-f-btn", "name": "Submit", "height": 48, "fill": "#06B6D4", "cornerRadius": 8, "alignItems": "center", "justifyContent": "center", "children": [
                                { "type": "text", "id": "l-f-btxt", "name": "Txt", "content": "Enviar Solicitud de Auditoría Gratuita", "fontSize": 14, "fontWeight": "800", "fill": "#070A11" }
                            ]}
                        ]
                    }
                ]
            },
            # 1.8 Footer
            {
                "type": "frame",
                "id": "l-footer",
                "name": "Footer Corporativo",
                "width": "fill_container",
                "height": 340,
                "fill": "#070A11",
                "layout": "vertical",
                "padding": [48, 48, 32, 48],
                "justifyContent": "space_between",
                "children": [
                    {
                        "type": "frame",
                        "id": "l-ft-cols",
                        "name": "Columns",
                        "width": "fill_container",
                        "layout": "horizontal",
                        "justifyContent": "space_between",
                        "children": [
                            {
                                "type": "frame", "id": "l-ft-c1", "name": "C1", "width": 400, "layout": "vertical", "gap": 12, "children": [
                                    { "type": "text", "id": "l-ft-t", "name": "T", "content": "CONTROL 61 · SISTEMAS DE SEGURIDAD", "fontSize": 16, "fontWeight": "800", "fill": "#FFFFFF", "letterSpacing": 1 },
                                    { "type": "text", "id": "l-ft-d", "name": "D", "content": "Desarrollos y Sistemas Inteligentes S.L.\nEmpresa de Seguridad Privada Homologada DGP Nº 2341.\nEspecialistas en Grado 3, CCTV con Visión Artificial y CRA propia 24/7.", "fontSize": 12, "fill": "#64748B", "lineHeight": 1.6 }
                                ]
                            },
                            {
                                "type": "frame", "id": "l-ft-c2", "name": "C2", "layout": "vertical", "gap": 10, "children": [
                                    { "type": "text", "id": "l-ft-h2", "name": "H", "content": "SOLUCIONES", "fontSize": 12, "fontWeight": "700", "fill": "#06B6D4" },
                                    { "type": "text", "id": "l-fl-1", "name": "L", "content": "Alarmas Homologadas Grado 3", "fontSize": 13, "fill": "#94A3B8" },
                                    { "type": "text", "id": "l-fl-2", "name": "L", "content": "CCTV Inteligente e IA Perimetral", "fontSize": 13, "fill": "#94A3B8" },
                                    { "type": "text", "id": "l-fl-3", "name": "L", "content": "Control de Accesos Biométrico 3D", "fontSize": 13, "fill": "#94A3B8" },
                                    { "type": "text", "id": "l-fl-4", "name": "L", "content": "Central Receptora CRA 24/7", "fontSize": 13, "fill": "#94A3B8" }
                                ]
                            },
                            {
                                "type": "frame", "id": "l-ft-c3", "name": "C3", "layout": "vertical", "gap": 10, "children": [
                                    { "type": "text", "id": "l-ft-h3", "name": "H", "content": "SEDE Y CONTACTO", "fontSize": 12, "fontWeight": "700", "fill": "#06B6D4" },
                                    { "type": "text", "id": "l-fc-1", "name": "L", "content": "📍 Pol. Ind. La Polvorista, Molina de Segura (Murcia)", "fontSize": 13, "fill": "#94A3B8" },
                                    { "type": "text", "id": "l-fc-2", "name": "L", "content": "📞 Centralita y Averías 24h: 968 622 984", "fontSize": 13, "fill": "#94A3B8" },
                                    { "type": "text", "id": "l-fc-3", "name": "L", "content": "✉️ info@control61.com", "fontSize": 13, "fill": "#94A3B8" }
                                ]
                            }
                        ]
                    },
                    {
                        "type": "frame",
                        "id": "l-ft-cr",
                        "name": "Copyright",
                        "width": "fill_container",
                        "height": 40,
                        "stroke": "#FFFFFF0F",
                        "strokeWidth": { "top": 1 },
                        "layout": "horizontal",
                        "justifyContent": "space_between",
                        "alignItems": "center",
                        "children": [
                            { "type": "text", "id": "l-cr-1", "name": "C", "content": "© 2026 Desarrollos y Sistemas Inteligentes S.L. (Control 61). By Toni.", "fontSize": 12, "fill": "#475569" },
                            { "type": "text", "id": "l-cr-2", "name": "L", "content": "Aviso Legal · Privacidad · Normativa DGP 2341 · Esquema Nacional de Seguridad", "fontSize": 12, "fill": "#475569" }
                        ]
                    }
                ]
            }
        ]
    }

    # =========================================================================
    # SCREEN 2: LIVE SOC SECURITY CONSOLE DASHBOARD (1440 x 1024)
    # =========================================================================
    soc_dashboard = {
        "type": "frame",
        "id": "control61-soc-dashboard",
        "name": "🛰️ 02. Consola de Control SOC & CRA 24/7 (1440 x 1024)",
        "x": 1540,
        "y": 0,
        "width": 1440,
        "height": 1024,
        "fill": "#030712",
        "layout": "horizontal",
        "clip": True,
        "children": [
            # Left Navigation Sidebar
            {
                "type": "frame",
                "id": "soc-sidebar",
                "name": "Sidebar",
                "width": 260,
                "height": "fill_container",
                "fill": "#0B1120",
                "stroke": "#FFFFFF14",
                "strokeWidth": { "right": 1 },
                "layout": "vertical",
                "padding": [24, 16],
                "justifyContent": "space_between",
                "children": [
                    {
                        "type": "frame",
                        "id": "soc-sb-top",
                        "name": "Top",
                        "layout": "vertical",
                        "gap": 28,
                        "children": [
                            {
                                "type": "frame",
                                "id": "soc-brand",
                                "name": "Brand",
                                "layout": "horizontal",
                                "gap": 10,
                                "alignItems": "center",
                                "children": [
                                    {
                                        "type": "frame", "id": "soc-b-ico", "name": "Box", "width": 36, "height": 36, "fill": "#0891B226", "stroke": "#06B6D4", "strokeWidth": 1.5, "cornerRadius": 8, "alignItems": "center", "justifyContent": "center", "children": [
                                            { "type": "icon", "id": "sb-ic", "name": "Ico", "library": "lucide", "icon": "shield-check", "width": 20, "height": 20, "fill": "#06B6D4" }
                                        ]
                                    },
                                    { "type": "text", "id": "soc-b-t", "name": "T", "content": "SOC CONTROL 61", "fontSize": 15, "fontWeight": "800", "fill": "#FFFFFF", "letterSpacing": 1 }
                                ]
                            },
                            {
                                "type": "frame",
                                "id": "soc-menu-list",
                                "name": "Menu",
                                "layout": "vertical",
                                "gap": 6,
                                "children": [
                                    {
                                        "type": "frame", "id": "sm-1", "name": "Item Active", "height": 40, "fill": "#0891B233", "stroke": "#06B6D466", "strokeWidth": 1, "cornerRadius": 8, "padding": [0, 12], "layout": "horizontal", "gap": 10, "alignItems": "center", "children": [
                                            { "type": "icon", "id": "smi-1", "name": "Ico", "library": "lucide", "icon": "video", "width": 16, "height": 16, "fill": "#22D3EE" },
                                            { "type": "text", "id": "smt-1", "name": "Txt", "content": "Matriz de Cámaras CCTV", "fontSize": 13, "fontWeight": "700", "fill": "#22D3EE" }
                                        ]
                                    },
                                    {
                                        "type": "frame", "id": "sm-2", "name": "Item", "height": 40, "padding": [0, 12], "layout": "horizontal", "gap": 10, "alignItems": "center", "children": [
                                            { "type": "icon", "id": "smi-2", "name": "Ico", "library": "lucide", "icon": "activity", "width": 16, "height": 16, "fill": "#64748B" },
                                            { "type": "text", "id": "smt-2", "name": "Txt", "content": "Historial de Alarmas (CRA)", "fontSize": 13, "fontWeight": "500", "fill": "#94A3B8" }
                                        ]
                                    },
                                    {
                                        "type": "frame", "id": "sm-3", "name": "Item", "height": 40, "padding": [0, 12], "layout": "horizontal", "gap": 10, "alignItems": "center", "children": [
                                            { "type": "icon", "id": "smi-3", "name": "Ico", "library": "lucide", "icon": "fingerprint", "width": 16, "height": 16, "fill": "#64748B" },
                                            { "type": "text", "id": "smt-3", "name": "Txt", "content": "Control de Accesos LPR", "fontSize": 13, "fontWeight": "500", "fill": "#94A3B8" }
                                        ]
                                    },
                                    {
                                        "type": "frame", "id": "sm-4", "name": "Item", "height": 40, "padding": [0, 12], "layout": "horizontal", "gap": 10, "alignItems": "center", "children": [
                                            { "type": "icon", "id": "smi-4", "name": "Ico", "library": "lucide", "icon": "radio", "width": 16, "height": 16, "fill": "#64748B" },
                                            { "type": "text", "id": "smt-4", "name": "Txt", "content": "Radar y Perímetro 3D", "fontSize": 13, "fontWeight": "500", "fill": "#94A3B8" }
                                        ]
                                    },
                                    {
                                        "type": "frame", "id": "sm-5", "name": "Item", "height": 40, "padding": [0, 12], "layout": "horizontal", "gap": 10, "alignItems": "center", "children": [
                                            { "type": "icon", "id": "smi-5", "name": "Ico", "library": "lucide", "icon": "lock", "width": 16, "height": 16, "fill": "#64748B" },
                                            { "type": "text", "id": "smt-5", "name": "Txt", "content": "Supervisión Grado 3", "fontSize": 13, "fontWeight": "500", "fill": "#94A3B8" }
                                        ]
                                    }
                                ]
                            }
                        ]
                    },
                    {
                        "type": "frame",
                        "id": "soc-sb-bot",
                        "name": "Operator Card",
                        "padding": [12, 12],
                        "fill": "#0F172A",
                        "stroke": "#FFFFFF1A",
                        "strokeWidth": 1,
                        "cornerRadius": 10,
                        "layout": "vertical",
                        "gap": 4,
                        "children": [
                            { "type": "text", "id": "soc-op-name", "name": "Op", "content": "Operador: Toni García", "fontSize": 12, "fontWeight": "700", "fill": "#FFFFFF" },
                            { "type": "text", "id": "soc-op-rank", "name": "Rank", "content": "Licencia DGP: #2341-OP", "fontSize": 10, "fill": "#38BDF8" }
                        ]
                    }
                ]
            },
            # Center & Right Main Console
            {
                "type": "frame",
                "id": "soc-main-area",
                "name": "Main Console Area",
                "width": 1180,
                "height": "fill_container",
                "layout": "vertical",
                "children": [
                    # Top Console Bar
                    {
                        "type": "frame",
                        "id": "soc-topbar",
                        "name": "Top Header",
                        "width": "fill_container",
                        "height": 60,
                        "fill": "#0B1120",
                        "stroke": "#FFFFFF14",
                        "strokeWidth": { "bottom": 1 },
                        "layout": "horizontal",
                        "padding": [0, 24],
                        "alignItems": "center",
                        "justifyContent": "space_between",
                        "children": [
                            {
                                "type": "frame",
                                "id": "soc-t-status",
                                "name": "Status",
                                "layout": "horizontal",
                                "gap": 12,
                                "alignItems": "center",
                                "children": [
                                    { "type": "ellipse", "id": "soc-live-dot", "name": "Dot", "width": 10, "height": 10, "fill": "#10B981" },
                                    { "type": "text", "id": "soc-st-txt", "name": "Txt", "content": "CENTRAL RECEPTORA OPERATIVA · 2.500+ RECINTOS CONECTADOS", "fontSize": 12, "fontWeight": "bold", "fill": "#F1F5F9" }
                                ]
                            },
                            {
                                "type": "frame",
                                "id": "soc-t-actions",
                                "name": "Actions",
                                "layout": "horizontal",
                                "gap": 16,
                                "alignItems": "center",
                                "children": [
                                    { "type": "text", "id": "soc-clock", "name": "Clock", "content": "UTC 11:35:42 · AES-256", "fontSize": 12, "fontWeight": "bold", "fill": "#06B6D4" },
                                    {
                                        "type": "frame", "id": "soc-panic-btn", "name": "Panic", "height": 36, "padding": [0, 16], "fill": "#EF4444", "cornerRadius": 6, "alignItems": "center", "justifyContent": "center", "children": [
                                            { "type": "text", "id": "soc-pb-t", "name": "T", "content": "🚨 AVISO POLICIAL DIRECTO", "fontSize": 11, "fontWeight": "bold", "fill": "#FFFFFF" }
                                        ]
                                    }
                                ]
                            }
                        ]
                    },
                    # 4 Camera Matrix + Right Event Log
                    {
                        "type": "frame",
                        "id": "soc-body-split",
                        "name": "Feeds & Telemetry Split",
                        "width": "fill_container",
                        "height": 964,
                        "layout": "horizontal",
                        "children": [
                            # 2x2 Matrix Video Feeds
                            {
                                "type": "frame",
                                "id": "soc-cam-matrix",
                                "name": "2x2 Camera Grid",
                                "width": 840,
                                "height": "fill_container",
                                "padding": [16, 16],
                                "layout": "vertical",
                                "gap": 12,
                                "children": [
                                    {
                                        "type": "frame", "id": "soc-row-c1", "name": "Row 1", "layout": "horizontal", "gap": 12, "children": [
                                            {
                                                "type": "frame", "id": "scam-1", "name": "CAM 01", "width": 398, "height": 260, "fill": "#0F172A", "stroke": "#EF4444", "strokeWidth": 2, "cornerRadius": 8, "padding": [12, 12], "layout": "vertical", "justifyContent": "space_between", "children": [
                                                    { "type": "frame", "id": "sc1-h", "name": "H", "layout": "horizontal", "justifyContent": "space_between", "children": [
                                                        { "type": "text", "id": "sc1-t", "name": "T", "content": "CAM-01 · Acceso Naves & Logística", "fontSize": 11, "fontWeight": "bold", "fill": "#FFFFFF" },
                                                        { "type": "text", "id": "sc1-r", "name": "R", "content": "● 4K 60FPS IA", "fontSize": 11, "fontWeight": "bold", "fill": "#EF4444" }
                                                    ]},
                                                    { "type": "frame", "id": "sc1-box", "name": "BBox", "height": 110, "fill": "#EF444426", "stroke": "#EF4444", "strokeWidth": 1.5, "cornerRadius": 6, "padding": [8, 8], "children": [
                                                        { "type": "text", "id": "sc1-txt", "name": "Txt", "content": "Persona No Autorizada (99.4% Conf)\nZona Restringida Muelle 4", "fontSize": 10, "fontWeight": "bold", "fill": "#FCA5A5" }
                                                    ]},
                                                    { "type": "text", "id": "sc1-ft", "name": "F", "content": "Despacho Acuda Solicitado (ETA: 3m 40s)", "fontSize": 10, "fontWeight": "bold", "fill": "#EF4444" }
                                                ]
                                            },
                                            {
                                                "type": "frame", "id": "scam-2", "name": "CAM 02", "width": 398, "height": 260, "fill": "#0F172A", "stroke": "#10B98188", "strokeWidth": 1.5, "cornerRadius": 8, "padding": [12, 12], "layout": "vertical", "justifyContent": "space_between", "children": [
                                                    { "type": "frame", "id": "sc2-h", "name": "H", "layout": "horizontal", "justifyContent": "space_between", "children": [
                                                        { "type": "text", "id": "sc2-t", "name": "T", "content": "CAM-02 · Perímetro Exterior Térmico", "fontSize": 11, "fontWeight": "bold", "fill": "#FFFFFF" },
                                                        { "type": "text", "id": "sc2-r", "name": "R", "content": "● TÉRMICA", "fontSize": 11, "fontWeight": "bold", "fill": "#10B981" }
                                                    ]},
                                                    { "type": "frame", "id": "sc2-box", "name": "BBox", "height": 110, "fill": "#10B9811A", "stroke": "#10B981", "strokeWidth": 1, "cornerRadius": 6, "padding": [8, 8], "children": [
                                                        { "type": "text", "id": "sc2-txt", "name": "Txt", "content": "Barrera Infrarroja Armada\nPerímetro Asegurado · Cero Cruces", "fontSize": 10, "fontWeight": "bold", "fill": "#86EFAC" }
                                                    ]},
                                                    { "type": "text", "id": "sc2-ft", "name": "F", "content": "Estado: Seguro · Polling 500ms OK", "fontSize": 10, "fontWeight": "bold", "fill": "#10B981" }
                                                ]
                                            }
                                        ]
                                    },
                                    {
                                        "type": "frame", "id": "soc-row-c2", "name": "Row 2", "layout": "horizontal", "gap": 12, "children": [
                                            {
                                                "type": "frame", "id": "scam-3", "name": "CAM 03", "width": 398, "height": 260, "fill": "#0F172A", "stroke": "#06B6D466", "strokeWidth": 1.5, "cornerRadius": 8, "padding": [12, 12], "layout": "vertical", "justifyContent": "space_between", "children": [
                                                    { "type": "frame", "id": "sc3-h", "name": "H", "layout": "horizontal", "justifyContent": "space_between", "children": [
                                                        { "type": "text", "id": "sc3-t", "name": "T", "content": "CAM-03 · Sala CPD & Servidores", "fontSize": 11, "fontWeight": "bold", "fill": "#FFFFFF" },
                                                        { "type": "text", "id": "sc3-r", "name": "R", "content": "● BIOMETRÍA", "fontSize": 11, "fontWeight": "bold", "fill": "#06B6D4" }
                                                    ]},
                                                    { "type": "frame", "id": "sc3-box", "name": "BBox", "height": 110, "fill": "#0891B226", "stroke": "#06B6D4", "strokeWidth": 1, "cornerRadius": 6, "padding": [8, 8], "children": [
                                                        { "type": "text", "id": "sc3-txt", "name": "Txt", "content": "Acceso Restringido Nivel 3\nTemperatura Rack: 21.4°C | Gas PCI: OK", "fontSize": 10, "fontWeight": "bold", "fill": "#67E8F9" }
                                                    ]},
                                                    { "type": "text", "id": "sc3-ft", "name": "F", "content": "Último Acceso: M. Torres (Ingeniero)", "fontSize": 10, "fontWeight": "bold", "fill": "#06B6D4" }
                                                ]
                                            },
                                            {
                                                "type": "frame", "id": "scam-4", "name": "CAM 04", "width": 398, "height": 260, "fill": "#0F172A", "stroke": "#F59E0B66", "strokeWidth": 1.5, "cornerRadius": 8, "padding": [12, 12], "layout": "vertical", "justifyContent": "space_between", "children": [
                                                    { "type": "frame", "id": "sc4-h", "name": "H", "layout": "horizontal", "justifyContent": "space_between", "children": [
                                                        { "type": "text", "id": "sc4-t", "name": "T", "content": "CAM-04 · LPR Barrera Vehicular", "fontSize": 11, "fontWeight": "bold", "fill": "#FFFFFF" },
                                                        { "type": "text", "id": "sc4-r", "name": "R", "content": "● LPR OK", "fontSize": 11, "fontWeight": "bold", "fill": "#F59E0B" }
                                                    ]},
                                                    { "type": "frame", "id": "sc4-box", "name": "BBox", "height": 110, "fill": "#F59E0B1A", "stroke": "#F59E0B", "strokeWidth": 1, "cornerRadius": 6, "padding": [8, 8], "children": [
                                                        { "type": "text", "id": "sc4-txt", "name": "Txt", "content": "Matrícula: 4821-LMR\nVehículo de Reparto Autorizado", "fontSize": 10, "fontWeight": "bold", "fill": "#FCD34D" }
                                                    ]},
                                                    { "type": "text", "id": "sc4-ft", "name": "F", "content": "Apertura Automática Concedida", "fontSize": 10, "fontWeight": "bold", "fill": "#F59E0B" }
                                                ]
                                            }
                                        ]
                                    }
                                ]
                            },
                            # Right Event Logs & Incident Telemetry
                            {
                                "type": "frame",
                                "id": "soc-event-panel",
                                "name": "Event Stream Log",
                                "width": 340,
                                "height": "fill_container",
                                "fill": "#0B1120",
                                "stroke": "#FFFFFF14",
                                "strokeWidth": { "left": 1 },
                                "padding": [16, 16],
                                "layout": "vertical",
                                "gap": 16,
                                "children": [
                                    { "type": "text", "id": "el-title", "name": "T", "content": "REGISTRO DE INCIDENCIAS EN VIVO", "fontSize": 12, "fontWeight": "800", "fill": "#06B6D4", "letterSpacing": 0.5 },
                                    {
                                        "type": "frame", "id": "el-card-1", "name": "Log 1", "fill": "#EF44441F", "stroke": "#EF444466", "strokeWidth": 1, "cornerRadius": 8, "padding": [10, 12], "layout": "vertical", "gap": 4, "children": [
                                            { "type": "text", "id": "lc1-t", "name": "Time", "content": "11:34:10 · ALERTA GRADO 3", "fontSize": 10, "fontWeight": "bold", "fill": "#EF4444" },
                                            { "type": "text", "id": "lc1-d", "name": "Desc", "content": "Salto Perimetral Nave C-7\nVerificación vídeo confirmada por CRA.", "fontSize": 11, "fontWeight": "600", "fill": "#FFFFFF" }
                                        ]
                                    },
                                    {
                                        "type": "frame", "id": "el-card-2", "name": "Log 2", "fill": "#10B9811A", "stroke": "#10B98144", "strokeWidth": 1, "cornerRadius": 8, "padding": [10, 12], "layout": "vertical", "gap": 4, "children": [
                                            { "type": "text", "id": "lc2-t", "name": "Time", "content": "11:32:05 · ACCESO AUTORIZADO", "fontSize": 10, "fontWeight": "bold", "fill": "#10B981" },
                                            { "type": "text", "id": "lc2-d", "name": "Desc", "content": "Torno 2: G. Martínez (Operaciones RFID)", "fontSize": 11, "fill": "#94A3B8" }
                                        ]
                                    },
                                    {
                                        "type": "frame", "id": "el-card-3", "name": "Log 3", "fill": "#0891B21A", "stroke": "#06B6D444", "strokeWidth": 1, "cornerRadius": 8, "padding": [10, 12], "layout": "vertical", "gap": 4, "children": [
                                            { "type": "text", "id": "lc3-t", "name": "Time", "content": "11:28:50 · TEST REDUNDANCIA", "fontSize": 10, "fontWeight": "bold", "fill": "#06B6D4" },
                                            { "type": "text", "id": "lc3-d", "name": "Desc", "content": "Supervisión Polling Fibra + 5G: OK", "fontSize": 11, "fill": "#94A3B8" }
                                        ]
                                    }
                                ]
                            }
                        ]
                    }
                ]
            }
        ]
    }

    # =========================================================================
    # SCREEN 3: MOBILE INTERFACE VIEW (390 x 2400)
    # =========================================================================
    mobile_view = {
        "type": "frame",
        "id": "control61-mobile-view",
        "name": "📱 03. Vista Móvil Responsiva (390 x 2400)",
        "x": 3080,
        "y": 0,
        "width": 390,
        "height": 2400,
        "fill": "#070A11",
        "layout": "vertical",
        "clip": True,
        "children": [
            # Mobile Header
            {
                "type": "frame",
                "id": "m-navbar",
                "name": "Mobile Header",
                "width": "fill_container",
                "height": 64,
                "fill": "#0B1120EE",
                "stroke": "#FFFFFF14",
                "strokeWidth": { "bottom": 1 },
                "layout": "horizontal",
                "padding": [0, 16],
                "alignItems": "center",
                "justifyContent": "space_between",
                "children": [
                    {
                        "type": "frame",
                        "id": "m-logo-grp",
                        "name": "Logo",
                        "layout": "horizontal",
                        "gap": 8,
                        "alignItems": "center",
                        "children": [
                            {
                                "type": "frame", "id": "m-lbox", "name": "Ico", "width": 32, "height": 32, "fill": "#0891B226", "stroke": "#06B6D4", "strokeWidth": 1, "cornerRadius": 6, "alignItems": "center", "justifyContent": "center", "children": [
                                    { "type": "icon", "id": "m-sh", "name": "I", "library": "lucide", "icon": "shield-check", "width": 18, "height": 18, "fill": "#06B6D4" }
                                ]
                            },
                            { "type": "text", "id": "m-bname", "name": "T", "content": "CONTROL 61", "fontSize": 15, "fontWeight": "800", "fill": "#FFFFFF", "letterSpacing": 1 }
                        ]
                    },
                    {
                        "type": "frame",
                        "id": "m-call-btn",
                        "name": "Call",
                        "height": 36,
                        "padding": [0, 12],
                        "fill": "#EF4444",
                        "cornerRadius": 6,
                        "layout": "horizontal",
                        "gap": 6,
                        "alignItems": "center",
                        "children": [
                            { "type": "icon", "id": "m-ph-i", "name": "P", "library": "lucide", "icon": "phone", "width": 14, "height": 14, "fill": "#FFFFFF" },
                            { "type": "text", "id": "m-ph-t", "name": "T", "content": "Llamar 24h", "fontSize": 12, "fontWeight": "bold", "fill": "#FFFFFF" }
                        ]
                    }
                ]
            },
            # Mobile Hero
            {
                "type": "frame",
                "id": "m-hero",
                "name": "Mobile Hero",
                "width": "fill_container",
                "padding": [32, 20],
                "layout": "vertical",
                "gap": 18,
                "children": [
                    {
                        "type": "frame", "id": "m-badge", "name": "Badge", "padding": [4, 10], "fill": "#0891B226", "stroke": "#06B6D466", "strokeWidth": 1, "cornerRadius": 16, "layout": "horizontal", "gap": 6, "children": [
                            { "type": "text", "id": "m-btxt", "name": "T", "content": "● HOMOLOGACIÓN DGP Nº 2341 · GRADO 3", "fontSize": 10, "fontWeight": "bold", "fill": "#22D3EE" }
                        ]
                    },
                    { "type": "text", "id": "m-h1", "name": "H1", "content": "Seguridad Avanzada, CCTV con IA y Alarmas", "fontSize": 28, "fontWeight": "800", "fill": "#FFFFFF", "lineHeight": 1.2 },
                    { "type": "text", "id": "m-sub", "name": "Sub", "content": "Instalación homologada de Grado 2 y 3 en Murcia. Conexión directa a CRA en <15s.", "fontSize": 14, "fill": "#94A3B8", "lineHeight": 1.5 },
                    {
                        "type": "frame", "id": "m-cta-btn", "name": "CTA", "height": 48, "width": "fill_container", "fill": "#06B6D4", "cornerRadius": 8, "alignItems": "center", "justifyContent": "center", "children": [
                            { "type": "text", "id": "m-cta-t", "name": "T", "content": "Solicitar Valoración Gratuita", "fontSize": 14, "fontWeight": "800", "fill": "#070A11" }
                        ]
                    }
                ]
            },
            # Mobile Cam HUD Card
            {
                "type": "frame",
                "id": "m-cam-card",
                "name": "Mobile Cam Stream Card",
                "width": "fill_container",
                "padding": [0, 20],
                "children": [
                    {
                        "type": "frame", "id": "m-hud-box", "name": "HUD", "width": "fill_container", "height": 220, "fill": "#0F172A", "stroke": "#EF444499", "strokeWidth": 2, "cornerRadius": 12, "padding": [12, 12], "layout": "vertical", "justifyContent": "space_between", "children": [
                            { "type": "frame", "id": "mh-t", "name": "Top", "layout": "horizontal", "justifyContent": "space_between", "children": [
                                { "type": "text", "id": "mh-l", "name": "L", "content": "CAM-01 · Perímetro Norte", "fontSize": 11, "fontWeight": "bold", "fill": "#FFFFFF" },
                                { "type": "text", "id": "mh-r", "name": "R", "content": "● EN VIVO IA", "fontSize": 11, "fontWeight": "bold", "fill": "#EF4444" }
                            ]},
                            { "type": "frame", "id": "mh-box", "name": "BBox", "height": 90, "fill": "#EF44441A", "stroke": "#EF4444", "strokeWidth": 1.5, "cornerRadius": 6, "padding": [8, 8], "children": [
                                { "type": "text", "id": "mh-btxt", "name": "T", "content": "⚠️ Intrusión Detectada (99.4%)\nAviso Despachado a Policía", "fontSize": 10, "fontWeight": "bold", "fill": "#FCA5A5" }
                            ]},
                            { "type": "text", "id": "mh-f", "name": "F", "content": "Latencia: 12ms · Doble Vía Fibra+5G", "fontSize": 10, "fontWeight": "bold", "fill": "#10B981" }
                        ]
                    }
                ]
            },
            # Mobile Stats Strip
            {
                "type": "frame",
                "id": "m-stats-grid",
                "name": "Stats 2x2",
                "width": "fill_container",
                "padding": [24, 20],
                "layout": "vertical",
                "gap": 12,
                "children": [
                    {
                        "type": "frame", "id": "ms-r1", "name": "R1", "layout": "horizontal", "gap": 12, "children": [
                            { "type": "frame", "id": "ms-c1", "name": "C1", "width": 169, "height": 80, "fill": "#0B1120", "stroke": "#06B6D433", "strokeWidth": 1, "cornerRadius": 8, "padding": [12, 12], "layout": "vertical", "gap": 2, "children": [
                                { "type": "text", "id": "ms-v1", "name": "V", "content": "+2.500", "fontSize": 20, "fontWeight": "800", "fill": "#06B6D4" },
                                { "type": "text", "id": "ms-l1", "name": "L", "content": "Clientes protegidos", "fontSize": 11, "fill": "#94A3B8" }
                            ]},
                            { "type": "frame", "id": "ms-c2", "name": "C2", "width": 169, "height": 80, "fill": "#0B1120", "stroke": "#10B98133", "strokeWidth": 1, "cornerRadius": 8, "padding": [12, 12], "layout": "vertical", "gap": 2, "children": [
                                { "type": "text", "id": "ms-v2", "name": "V", "content": "< 15s", "fontSize": 20, "fontWeight": "800", "fill": "#10B981" },
                                { "type": "text", "id": "ms-l2", "name": "L", "content": "Respuesta CRA", "fontSize": 11, "fill": "#94A3B8" }
                            ]}
                        ]
                    },
                    {
                        "type": "frame", "id": "ms-r2", "name": "R2", "layout": "horizontal", "gap": 12, "children": [
                            { "type": "frame", "id": "ms-c3", "name": "C3", "width": 169, "height": 80, "fill": "#0B1120", "stroke": "#38BDF833", "strokeWidth": 1, "cornerRadius": 8, "padding": [12, 12], "layout": "vertical", "gap": 2, "children": [
                                { "type": "text", "id": "ms-v3", "name": "V", "content": "99.9%", "fontSize": 20, "fontWeight": "800", "fill": "#38BDF8" },
                                { "type": "text", "id": "ms-l3", "name": "L", "content": "Disponibilidad", "fontSize": 11, "fill": "#94A3B8" }
                            ]},
                            { "type": "frame", "id": "ms-c4", "name": "C4", "width": 169, "height": 80, "fill": "#0B1120", "stroke": "#F59E0B33", "strokeWidth": 1, "cornerRadius": 8, "padding": [12, 12], "layout": "vertical", "gap": 2, "children": [
                                { "type": "text", "id": "ms-v4", "name": "V", "content": "20+ Años", "fontSize": 20, "fontWeight": "800", "fill": "#F59E0B" },
                                { "type": "text", "id": "ms-l4", "name": "L", "content": "Experiencia", "fontSize": 11, "fill": "#94A3B8" }
                            ]}
                        ]
                    }
                ]
            },
            # Mobile Contact Footer
            {
                "type": "frame",
                "id": "m-footer",
                "name": "Mobile Footer",
                "width": "fill_container",
                "padding": [32, 20],
                "layout": "vertical",
                "gap": 12,
                "children": [
                    { "type": "text", "id": "mf-t", "name": "T", "content": "CONTROL 61 · MURCIA", "fontSize": 14, "fontWeight": "800", "fill": "#FFFFFF" },
                    { "type": "text", "id": "mf-d", "name": "D", "content": "Sistemas Homologados DGP Nº 2341 · Tel: 968 622 984", "fontSize": 12, "fill": "#94A3B8" }
                ]
            }
        ]
    }

    doc["children"] = [landing, soc_dashboard, mobile_view]
    return doc

full_doc = make_doc()
with open("/Users/toni/Proyectos/Control61-Web/control61_modern_ui.pen", "w") as f:
    json.dump(full_doc, f, indent=2)

print("Successfully generated complete multi-screen .pen file!")
