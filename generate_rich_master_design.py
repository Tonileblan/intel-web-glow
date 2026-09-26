import json
import subprocess

# Colors
BG_DARK = "#070A11"
BG_CARD = "#0B1120"
BG_CARD_INNER = "#0F172A"
CYAN = "#06B6D4"
CYAN_LIGHT = "#22D3EE"
EMERALD = "#10B981"
EMERALD_LIGHT = "#34D399"
RED = "#EF4444"
RED_LIGHT = "#F87171"
AMBER = "#F59E0B"
BORDER_LIGHT = "#FFFFFF14"
BORDER_CYAN = "#06B6D433"
BORDER_RED = "#EF44444D"
BORDER_EMERALD = "#10B9814D"

# Photographic URLs
IMG_HERO_CONTROL_ROOM = "https://images.unsplash.com/photo-1558494949-ef010cbdcc31?auto=format&fit=crop&w=1600&q=80"
IMG_CCTV_CAMERA = "https://images.unsplash.com/photo-1557597774-9d273605dfa9?auto=format&fit=crop&w=1600&q=80"
IMG_WAREHOUSE_NIGHT = "https://images.unsplash.com/photo-1586528116311-ad8dd3c8310d?auto=format&fit=crop&w=1600&q=80"
IMG_LOGISTICS_DOCK = "https://images.unsplash.com/photo-1545324418-cc1a3fa10c00?auto=format&fit=crop&w=1600&q=80"
IMG_SERVER_CPD = "https://images.unsplash.com/photo-1558494949-ef010cbdcc31?auto=format&fit=crop&w=1600&q=80"
IMG_RESIDENTIAL_VILLA = "https://images.unsplash.com/photo-1600585154340-be6161a56a0c?auto=format&fit=crop&w=1600&q=80"
IMG_BIOMETRIC_TURNSTILE = "https://images.unsplash.com/photo-1497366216548-37526070297c?auto=format&fit=crop&w=1600&q=80"
IMG_FIRE_PROTECTION = "https://images.unsplash.com/photo-1517430816045-df4b7de01dbf?auto=format&fit=crop&w=1600&q=80"
IMG_INSTITUTION_BUILDING = "https://images.unsplash.com/photo-1486406146926-c627a92ad1ab?auto=format&fit=crop&w=1600&q=80"

def photo_fill(img_url, overlay_top="#070A1133", overlay_bot="#070A11F5"):
    return [
        {
            "type": "image",
            "url": img_url,
            "mode": "fill"
        },
        {
            "type": "gradient",
            "gradientType": "linear",
            "rotation": 180,
            "colors": [
                { "color": overlay_top, "position": 0 },
                { "color": overlay_bot, "position": 1 }
            ]
        }
    ]

def make_rich_header(page_id, active_nav):
    nav_items = [
        ("Inicio", "/"),
        ("Empresas", "/empresas"),
        ("CCTV & IA", "/cctv"),
        ("Hogar", "/hogar"),
        ("Instituciones", "/instituciones"),
        ("Mantenimiento", "/mantenimiento"),
        ("Acreditaciones", "/acreditaciones"),
        ("Nosotros", "/nosotros"),
        ("Contacto", "/contacto")
    ]
    
    links = []
    for name, path in nav_items:
        is_active = (name == active_nav)
        links.append({
            "type": "text",
            "id": f"{page_id}-nav-{name}",
            "name": name,
            "content": name,
            "fontSize": 13,
            "fontWeight": "700" if is_active else "500",
            "fill": CYAN_LIGHT if is_active else "#94A3B8"
        })
        
    return {
        "type": "frame",
        "id": f"{page_id}-navbar",
        "name": "Navbar Glassmorphism",
        "width": "fill_container",
        "height": 76,
        "fill": "#0B1120EE",
        "stroke": BORDER_LIGHT,
        "strokeWidth": { "bottom": 1 },
        "layout": "horizontal",
        "padding": [0, 48],
        "alignItems": "center",
        "justifyContent": "space_between",
        "children": [
            {
                "type": "frame",
                "id": f"{page_id}-brand",
                "name": "Brand",
                "layout": "horizontal",
                "gap": 12,
                "alignItems": "center",
                "children": [
                    {
                        "type": "frame",
                        "id": f"{page_id}-logo-box",
                        "name": "Box",
                        "width": 42,
                        "height": 42,
                        "fill": "#0891B226",
                        "stroke": CYAN,
                        "strokeWidth": 1.5,
                        "cornerRadius": 10,
                        "alignItems": "center",
                        "justifyContent": "center",
                        "children": [
                            { "type": "icon", "id": f"{page_id}-sh-ico", "name": "Ico", "library": "lucide", "icon": "shield-check", "width": 24, "height": 24, "fill": CYAN }
                        ]
                    },
                    {
                        "type": "frame",
                        "id": f"{page_id}-btexts",
                        "name": "Text",
                        "layout": "vertical",
                        "gap": 2,
                        "children": [
                            { "type": "text", "id": f"{page_id}-bname", "name": "Name", "content": "CONTROL 61", "fontSize": 19, "fontWeight": "800", "fill": "#FFFFFF", "letterSpacing": 1.5 },
                            { "type": "text", "id": f"{page_id}-bsub", "name": "Sub", "content": "SISTEMAS INTELIGENTES DE SEGURIDAD", "fontSize": 8, "fontWeight": "600", "fill": "#94A3B8", "letterSpacing": 0.8 }
                        ]
                    }
                ]
            },
            {
                "type": "frame",
                "id": f"{page_id}-navlinks",
                "name": "Links",
                "layout": "horizontal",
                "gap": 20,
                "alignItems": "center",
                "children": links
            },
            {
                "type": "frame",
                "id": f"{page_id}-navcta",
                "name": "CTAs",
                "layout": "horizontal",
                "gap": 12,
                "alignItems": "center",
                "children": [
                    {
                        "type": "frame",
                        "id": f"{page_id}-btn-ph",
                        "name": "Phone",
                        "height": 40,
                        "padding": [0, 16],
                        "fill": "#1E293B80",
                        "stroke": "#FFFFFF26",
                        "strokeWidth": 1,
                        "cornerRadius": 8,
                        "layout": "horizontal",
                        "gap": 8,
                        "alignItems": "center",
                        "children": [
                            { "type": "icon", "id": f"{page_id}-pi", "name": "I", "library": "lucide", "icon": "phone", "width": 14, "height": 14, "fill": RED },
                            { "type": "text", "id": f"{page_id}-pt", "name": "T", "content": "968 622 984", "fontSize": 12, "fontWeight": "600", "fill": "#F1F5F9" }
                        ]
                    },
                    {
                        "type": "frame",
                        "id": f"{page_id}-btn-aud",
                        "name": "Audit",
                        "height": 40,
                        "padding": [0, 18],
                        "fill": CYAN,
                        "cornerRadius": 8,
                        "alignItems": "center",
                        "justifyContent": "center",
                        "children": [
                            { "type": "text", "id": f"{page_id}-at", "name": "T", "content": "Valoración Gratuita", "fontSize": 13, "fontWeight": "700", "fill": "#070A11" }
                        ]
                    }
                ]
            }
        ]
    }

def make_rich_footer(page_id):
    return {
        "type": "frame",
        "id": f"{page_id}-footer",
        "name": "Footer Corporativo",
        "width": "fill_container",
        "height": 320,
        "fill": "#070A11",
        "layout": "vertical",
        "padding": [48, 48, 24, 48],
        "justifyContent": "space_between",
        "children": [
            {
                "type": "frame",
                "id": f"{page_id}-ft-cols",
                "name": "Columns",
                "width": "fill_container",
                "layout": "horizontal",
                "justifyContent": "space_between",
                "children": [
                    {
                        "type": "frame", "id": f"{page_id}-ft-c1", "name": "C1", "width": 420, "layout": "vertical", "gap": 12, "children": [
                            { "type": "text", "id": f"{page_id}-ft-t", "name": "T", "content": "CONTROL 61 · INGENIERÍA DE SEGURIDAD", "fontSize": 16, "fontWeight": "800", "fill": "#FFFFFF", "letterSpacing": 1.2 },
                            { "type": "text", "id": f"{page_id}-ft-d", "name": "D", "content": "Desarrollos y Sistemas Inteligentes S.L. · Inscrita en Registro DGP Nº 2341.\nEspecialistas homologados en Grado 3, CCTV con Visión Artificial y CRA 24/7.\nPol. Ind. La Polvorista, C/ Caravaca de la Cruz 13, Nave C-7, Molina de Segura (Murcia)", "fontSize": 12, "fill": "#64748B", "lineHeight": 1.6 }
                        ]
                    },
                    {
                        "type": "frame", "id": f"{page_id}-ft-c2", "name": "C2", "layout": "vertical", "gap": 10, "children": [
                            { "type": "text", "id": f"{page_id}-ft-h2", "name": "H", "content": "SOLUCIONES HOMOLOGADAS", "fontSize": 12, "fontWeight": "700", "fill": CYAN },
                            { "type": "text", "id": f"{page_id}-fl-1", "name": "L", "content": "Alarmas Homologadas Grado 3", "fontSize": 13, "fill": "#94A3B8" },
                            { "type": "text", "id": f"{page_id}-fl-2", "name": "L", "content": "CCTV Inteligente e IA Perimetral", "fontSize": 13, "fill": "#94A3B8" },
                            { "type": "text", "id": f"{page_id}-fl-3", "name": "L", "content": "Control de Accesos Biométrico 3D", "fontSize": 13, "fill": "#94A3B8" },
                            { "type": "text", "id": f"{page_id}-fl-4", "name": "L", "content": "Central Receptora CRA 24/7", "fontSize": 13, "fill": "#94A3B8" }
                        ]
                    },
                    {
                        "type": "frame", "id": f"{page_id}-ft-c3", "name": "C3", "layout": "vertical", "gap": 10, "children": [
                            { "type": "text", "id": f"{page_id}-ft-h3", "name": "H", "content": "ATENCIÓN TÉCNICA Y SEDE", "fontSize": 12, "fontWeight": "700", "fill": CYAN },
                            { "type": "text", "id": f"{page_id}-fc-1", "name": "L", "content": "📞 Centralita y Averías 24h: 968 622 984", "fontSize": 13, "fill": "#94A3B8" },
                            { "type": "text", "id": f"{page_id}-fc-2", "name": "L", "content": "✉️ info@control61.com", "fontSize": 13, "fill": "#94A3B8" },
                            { "type": "text", "id": f"{page_id}-fc-3", "name": "L", "content": "🛡️ Asistencia Técnica de Guardia en Murcia y Levante", "fontSize": 13, "fill": EMERALD }
                        ]
                    }
                ]
            },
            {
                "type": "frame",
                "id": f"{page_id}-ft-cr",
                "name": "CR Bar",
                "width": "fill_container",
                "height": 40,
                "stroke": BORDER_LIGHT,
                "strokeWidth": { "top": 1 },
                "layout": "horizontal",
                "justifyContent": "space_between",
                "alignItems": "center",
                "children": [
                    { "type": "text", "id": f"{page_id}-cr-1", "name": "C", "content": "© 2026 Desarrollos y Sistemas Inteligentes S.L. (Control 61). Todos los derechos reservados.", "fontSize": 12, "fill": "#475569" },
                    { "type": "text", "id": f"{page_id}-cr-2", "name": "L", "content": "Aviso Legal · Política de Privacidad · Normativa DGP 2341 · Certificación ISO 9001", "fontSize": 12, "fill": "#475569" }
                ]
            }
        ]
    }

# =========================================================================
# 01. FLAGSHIP LANDING PAGE (1440 x 5400)
# =========================================================================
p1_landing = {
    "type": "frame",
    "id": "screen-01-home",
    "name": "🏠 01. Inicio / Landing Principal (1440px)",
    "x": 0,
    "y": 0,
    "width": 1440,
    "height": 5200,
    "fill": BG_DARK,
    "layout": "vertical",
    "clip": True,
    "children": [
        # Emergency Top Bar
        {
            "type": "frame", "id": "p1-top-bar", "name": "Top Status", "width": "fill_container", "height": 42, "fill": BG_CARD_INNER, "stroke": BORDER_CYAN, "strokeWidth": { "bottom": 1 }, "layout": "horizontal", "padding": [0, 48], "alignItems": "center", "justifyContent": "space_between", "children": [
                { "type": "frame", "id": "p1-tb-l", "name": "L", "layout": "horizontal", "gap": 8, "alignItems": "center", "children": [
                    { "type": "ellipse", "id": "p1-dot", "name": "D", "width": 8, "height": 8, "fill": EMERALD },
                    { "type": "text", "id": "p1-st-txt", "name": "T", "content": "CENTRAL RECEPTORA DE ALARMAS 24/7/365 · HOMOLOGADA GRADO 3 · DGP Nº 2341", "fontSize": 11, "fontWeight": "bold", "fill": "#38BDF8" }
                ]},
                { "type": "text", "id": "p1-tb-r", "name": "R", "content": "🚨 Teléfono Centralita Urgencias 24h: 968 622 984", "fontSize": 12, "fontWeight": "600", "fill": "#F1F5F9" }
            ]
        },
        make_rich_header("p1", "Inicio"),
        # Hero Section with Live HUD
        {
            "type": "frame", "id": "p1-hero", "name": "Hero Section", "width": "fill_container", "height": 720, "fill": BG_DARK, "layout": "horizontal", "padding": [64, 48], "gap": 48, "alignItems": "center", "justifyContent": "space_between", "children": [
                {
                    "type": "frame", "id": "p1-h-l", "name": "Left", "width": 640, "layout": "vertical", "gap": 24, "children": [
                        { "type": "frame", "id": "p1-badge", "name": "Badge", "height": 32, "padding": [0, 14], "fill": "#0891B226", "stroke": "#06B6D466", "strokeWidth": 1, "cornerRadius": 20, "layout": "horizontal", "gap": 8, "alignItems": "center", "children": [
                            { "type": "icon", "id": "p1-b-ico", "name": "I", "library": "lucide", "icon": "shield-alert", "width": 14, "height": 14, "fill": CYAN_LIGHT },
                            { "type": "text", "id": "p1-btxt", "name": "T", "content": "HOMOLOGACIÓN NACIONAL DGP Nº 2341 · CERTIFICACIÓN GRADO 3", "fontSize": 10, "fontWeight": "700", "fill": CYAN_LIGHT }
                        ]},
                        { "type": "text", "id": "p1-h1", "name": "H1", "content": "Sistemas de Seguridad Avanzada, CCTV con IA y Protección Grado 3", "fontSize": 46, "fontWeight": "800", "fill": "#FFFFFF", "lineHeight": 1.15, "textGrowth": "fixed-width", "width": 640 },
                        { "type": "text", "id": "p1-hdesc", "name": "Desc", "content": "Ingeniería e instalación de alarmas de Grado 2 y 3, videovigilancia de alta precisión y control de accesos para industrias, naves y recintos logísticos en Murcia y Levante.", "fontSize": 16, "fill": "#94A3B8", "lineHeight": 1.6, "textGrowth": "fixed-width", "width": 620 },
                        {
                            "type": "frame", "id": "p1-h-btns", "name": "Btns", "layout": "horizontal", "gap": 16, "children": [
                                { "type": "frame", "id": "p1-btn-main", "name": "CTA", "height": 52, "padding": [0, 26], "fill": CYAN, "cornerRadius": 10, "layout": "horizontal", "gap": 10, "alignItems": "center", "children": [
                                    { "type": "text", "id": "p1-bmt", "name": "T", "content": "Solicitar Valoración Gratuita", "fontSize": 15, "fontWeight": "700", "fill": "#070A11" },
                                    { "type": "icon", "id": "p1-bmi", "name": "I", "library": "lucide", "icon": "arrow-up-right", "width": 18, "height": 18, "fill": "#070A11" }
                                ]},
                                { "type": "frame", "id": "p1-btn-sec", "name": "Phone", "height": 52, "padding": [0, 22], "fill": "#1E293B80", "stroke": "#FFFFFF26", "strokeWidth": 1, "cornerRadius": 10, "layout": "horizontal", "gap": 8, "alignItems": "center", "children": [
                                    { "type": "icon", "id": "p1-pi", "name": "I", "library": "lucide", "icon": "phone", "width": 16, "height": 16, "fill": RED },
                                    { "type": "text", "id": "p1-pst", "name": "T", "content": "968 622 984 · Averías 24h", "fontSize": 14, "fontWeight": "600", "fill": "#F1F5F9" }
                                ]}
                            ]
                        },
                        {
                            "type": "frame", "id": "p1-trust-strip", "name": "Trust", "layout": "horizontal", "gap": 28, "alignItems": "center", "children": [
                                { "type": "text", "id": "p1-t1", "name": "T1", "content": "✓ Sin Cuotas Trampa ni Permanencias", "fontSize": 13, "fontWeight": "600", "fill": EMERALD },
                                { "type": "text", "id": "p1-t2", "name": "T2", "content": "✓ Técnicos Homologados en Plantilla", "fontSize": 13, "fontWeight": "600", "fill": EMERALD },
                                { "type": "text", "id": "p1-t3", "name": "T3", "content": "✓ Respuesta CRA < 15s", "fontSize": 13, "fontWeight": "600", "fill": EMERALD }
                            ]
                        }
                    ]
                },
                # Hero Right HUD with Photo Fills
                {
                    "type": "frame", "id": "p1-hud", "name": "HUD Box", "width": 640, "height": 480, "fill": BG_CARD, "stroke": "#06B6D440", "strokeWidth": 1.5, "cornerRadius": 16, "layout": "vertical", "clip": True, "children": [
                        { "type": "frame", "id": "p1-hh", "name": "Header", "width": "fill_container", "height": 46, "fill": BG_CARD_INNER, "stroke": BORDER_LIGHT, "strokeWidth": { "bottom": 1 }, "layout": "horizontal", "padding": [0, 18], "alignItems": "center", "justifyContent": "space_between", "children": [
                            { "type": "text", "id": "p1-htitle", "name": "T", "content": "CONTROL61_SOC://MURCIA · GRADO 3 ACTIVO", "fontSize": 11, "fontWeight": "bold", "fill": "#FFFFFF" },
                            { "type": "text", "id": "p1-hlat", "name": "L", "content": "AES-256 | LATENCIA: 12ms", "fontSize": 10, "fontWeight": "bold", "fill": EMERALD }
                        ]},
                        { "type": "frame", "id": "p1-hcams", "name": "Cams", "width": "fill_container", "height": 310, "fill": "#030712", "layout": "horizontal", "gap": 12, "padding": [12, 12], "children": [
                            # CAM 01 with Photo Fill
                            { "type": "frame", "id": "p1-c1", "name": "CAM 1", "width": 302, "height": 286, "cornerRadius": 8, "clip": True, "fill": photo_fill(IMG_WAREHOUSE_NIGHT, "#070A1120", "#070A11D0"), "stroke": RED, "strokeWidth": 2, "padding": [12, 12], "layout": "vertical", "justifyContent": "space_between", "children": [
                                { "type": "frame", "id": "p1-c1-t", "name": "Top", "layout": "horizontal", "justifyContent": "space_between", "children": [
                                    { "type": "text", "id": "p1-c1-lbl", "name": "L", "content": "CAM-01 · Perímetro Norte", "fontSize": 11, "fontWeight": "bold", "fill": "#FFFFFF" },
                                    { "type": "text", "id": "p1-c1-rec", "name": "R", "content": "● REC IA", "fontSize": 11, "fontWeight": "bold", "fill": RED }
                                ]},
                                { "type": "frame", "id": "p1-c1-b", "name": "Box", "height": 120, "fill": "#EF444426", "stroke": RED, "strokeWidth": 1.5, "cornerRadius": 6, "padding": [8, 8], "children": [
                                    { "type": "text", "id": "p1-c1-txt", "name": "T", "content": "⚠️ Intrusión Detectada (99.4% Conf)\nCruce Barrera Infrarroja Sector 3", "fontSize": 10, "fontWeight": "bold", "fill": "#FCA5A5" }
                                ]},
                                { "type": "text", "id": "p1-c1-ft", "name": "F", "content": "Aviso Directo a Policía Despachado (0.8s)", "fontSize": 10, "fontWeight": "bold", "fill": RED }
                            ]},
                            # CAM 02 with Photo Fill
                            { "type": "frame", "id": "p1-c2", "name": "CAM 2", "width": 302, "height": 286, "cornerRadius": 8, "clip": True, "fill": photo_fill(IMG_LOGISTICS_DOCK, "#070A1120", "#070A11D0"), "stroke": EMERALD, "strokeWidth": 1.5, "padding": [12, 12], "layout": "vertical", "justifyContent": "space_between", "children": [
                                { "type": "frame", "id": "p1-c2-t", "name": "Top", "layout": "horizontal", "justifyContent": "space_between", "children": [
                                    { "type": "text", "id": "p1-c2-lbl", "name": "L", "content": "CAM-02 · Acceso Muelle LPR", "fontSize": 11, "fontWeight": "bold", "fill": "#FFFFFF" },
                                    { "type": "text", "id": "p1-c2-aut", "name": "A", "content": "● AUTORIZADO", "fontSize": 11, "fontWeight": "bold", "fill": EMERALD }
                                ]},
                                { "type": "frame", "id": "p1-c2-b", "name": "Box", "height": 120, "fill": "#10B9811A", "stroke": EMERALD, "strokeWidth": 1.5, "cornerRadius": 6, "padding": [8, 8], "children": [
                                    { "type": "text", "id": "p1-c2-txt", "name": "T", "content": "MATRÍCULA: 4821-LMR [Verificada]\nFlota Logística Central · Puerta Abierta", "fontSize": 10, "fontWeight": "bold", "fill": "#86EFAC" }
                                ]},
                                { "type": "text", "id": "p1-c2-ft", "name": "F", "content": "Barrera Automática Accionada", "fontSize": 10, "fontWeight": "bold", "fill": EMERALD }
                            ]}
                        ]},
                        { "type": "frame", "id": "p1-hft", "name": "Ft", "width": "fill_container", "height": 124, "fill": BG_CARD_INNER, "layout": "horizontal", "padding": [12, 20], "justifyContent": "space_between", "alignItems": "center", "children": [
                            { "type": "text", "id": "p1-hf1", "name": "T1", "content": "RED: Doble Vía Fibra+5G (12ms)", "fontSize": 11, "fontWeight": "bold", "fill": CYAN },
                            { "type": "text", "id": "p1-hf2", "name": "T2", "content": "CRA: <15s Respuesta Verificada", "fontSize": 11, "fontWeight": "bold", "fill": EMERALD },
                            { "type": "text", "id": "p1-hf3", "name": "T3", "content": "SLA: 99.999% Disponibilidad", "fontSize": 11, "fontWeight": "bold", "fill": AMBER }
                        ]}
                    ]
                }
            ]
        },
        # Bento Strip KPIs
        {
            "type": "frame", "id": "p1-kpis", "name": "KPIs", "width": "fill_container", "height": 140, "fill": BG_CARD, "stroke": BORDER_CYAN, "strokeWidth": { "top": 1, "bottom": 1 }, "layout": "horizontal", "padding": [0, 48], "alignItems": "center", "justifyContent": "space_between", "children": [
                { "type": "frame", "id": "pk-1", "name": "K1", "layout": "vertical", "gap": 4, "children": [
                    { "type": "text", "id": "pkn-1", "name": "N", "content": "+2.500", "fontSize": 36, "fontWeight": "800", "fill": CYAN },
                    { "type": "text", "id": "pkl-1", "name": "L", "content": "Clientes protegidos en Murcia y Levante", "fontSize": 13, "fill": "#94A3B8" }
                ]},
                { "type": "frame", "id": "pk-2", "name": "K2", "layout": "vertical", "gap": 4, "children": [
                    { "type": "text", "id": "pkn-2", "name": "N", "content": "< 15s", "fontSize": 36, "fontWeight": "800", "fill": EMERALD },
                    { "type": "text", "id": "pkl-2", "name": "L", "content": "Tiempo medio de respuesta SOC / CRA", "fontSize": 13, "fill": "#94A3B8" }
                ]},
                { "type": "frame", "id": "pk-3", "name": "K3", "layout": "vertical", "gap": 4, "children": [
                    { "type": "text", "id": "pkn-3", "name": "N", "content": "99.9%", "fontSize": 36, "fontWeight": "800", "fill": "#38BDF8" },
                    { "type": "text", "id": "pkl-3", "name": "L", "content": "Disponibilidad de red y polling continuo", "fontSize": 13, "fill": "#94A3B8" }
                ]},
                { "type": "frame", "id": "pk-4", "name": "K4", "layout": "vertical", "gap": 4, "children": [
                    { "type": "text", "id": "pkn-4", "name": "N", "content": "20+ Años", "fontSize": 36, "fontWeight": "800", "fill": AMBER },
                    { "type": "text", "id": "pkl-4", "name": "L", "content": "Ingeniería de seguridad homologada DGP", "fontSize": 13, "fill": "#94A3B8" }
                ]}
            ]
        },
        # 6-Pillar Rich Bento Grid with Photography Fills
        {
            "type": "frame", "id": "p1-bento", "name": "Bento Grid", "width": "fill_container", "fill": BG_DARK, "layout": "vertical", "padding": [80, 48], "gap": 36, "children": [
                { "type": "frame", "id": "pb-hdr", "name": "Hdr", "layout": "vertical", "gap": 10, "children": [
                    { "type": "text", "id": "pb-eye", "name": "Eye", "content": "SOLUCIONES DE SEGURIDAD INTEGRAL HOMOLOGADAS", "fontSize": 12, "fontWeight": "800", "fill": CYAN, "letterSpacing": 1 },
                    { "type": "text", "id": "pb-title", "name": "T", "content": "Ingeniería de Protección Sin Puntos Ciegos", "fontSize": 36, "fontWeight": "800", "fill": "#FFFFFF" },
                    { "type": "text", "id": "pb-sub", "name": "S", "content": "Diseñamos, instalamos y mantenemos ecosistemas completos donde cada cámara, sensor y acceso trabaja sincronizado.", "fontSize": 15, "fill": "#94A3B8" }
                ]},
                # Bento Row 1
                { "type": "frame", "id": "pb-r1", "name": "R1", "layout": "horizontal", "gap": 24, "children": [
                    # Card 1: CCTV IA with Camera Photo Fill
                    { "type": "frame", "id": "pbc-1", "name": "C1 CCTV", "width": 432, "height": 290, "cornerRadius": 14, "clip": True, "fill": photo_fill(IMG_CCTV_CAMERA, "#0B112044", "#0B1120F8"), "stroke": BORDER_CYAN, "strokeWidth": 1.5, "padding": [24, 24], "layout": "vertical", "justifyContent": "space_between", "children": [
                        { "type": "frame", "id": "pbc1-tags", "name": "Tags", "layout": "horizontal", "gap": 8, "children": [
                            { "type": "frame", "id": "p1-tag-1", "name": "Tag", "padding": [4, 10], "fill": "#0891B244", "stroke": CYAN, "strokeWidth": 1, "cornerRadius": 6, "children": [
                                { "type": "text", "id": "p1-t1-txt", "name": "T", "content": "4K HDR ÓPTICA IA", "fontSize": 10, "fontWeight": "bold", "fill": CYAN_LIGHT }
                            ]},
                            { "type": "frame", "id": "p1-tag-2", "name": "Tag", "padding": [4, 10], "fill": "#10B98133", "stroke": EMERALD, "strokeWidth": 1, "cornerRadius": 6, "children": [
                                { "type": "text", "id": "p1-t2-txt", "name": "T", "content": "RGPD COMPLIANT", "fontSize": 10, "fontWeight": "bold", "fill": EMERALD_LIGHT }
                            ]}
                        ]},
                        { "type": "frame", "id": "pbc1-body", "name": "Body", "layout": "vertical", "gap": 8, "children": [
                            { "type": "text", "id": "pbc1-t", "name": "T", "content": "CCTV Inteligente con Búsqueda Instantánea", "fontSize": 18, "fontWeight": "700", "fill": "#FFFFFF" },
                            { "type": "text", "id": "pbc1-d", "name": "D", "content": "Cámaras térmicas y 4K con analítica IA: detección perimetral, reconocimiento LPR y búsqueda de eventos en segundos.", "fontSize": 13, "fill": "#94A3B8", "lineHeight": 1.5 }
                        ]},
                        { "type": "text", "id": "pbc1-l", "name": "L", "content": "Explorar analítica de vídeo IA →", "fontSize": 13, "fontWeight": "700", "fill": CYAN_LIGHT }
                    ]},
                    # Card 2: Alarmas Grado 3 with Warehouse Photo Fill
                    { "type": "frame", "id": "pbc-2", "name": "C2 Grado 3", "width": 432, "height": 290, "cornerRadius": 14, "clip": True, "fill": photo_fill(IMG_WAREHOUSE_NIGHT, "#0B112044", "#0B1120F8"), "stroke": BORDER_RED, "strokeWidth": 1.5, "padding": [24, 24], "layout": "vertical", "justifyContent": "space_between", "children": [
                        { "type": "frame", "id": "pbc2-tags", "name": "Tags", "layout": "horizontal", "gap": 8, "children": [
                            { "type": "frame", "id": "p2-tag-1", "name": "Tag", "padding": [4, 10], "fill": "#EF444433", "stroke": RED, "strokeWidth": 1, "cornerRadius": 6, "children": [
                                { "type": "text", "id": "p2-t1-txt", "name": "T", "content": "GRADO 3 HOMOLOGADO", "fontSize": 10, "fontWeight": "bold", "fill": RED_LIGHT }
                            ]}
                        ]},
                        { "type": "frame", "id": "pbc2-body", "name": "Body", "layout": "vertical", "gap": 8, "children": [
                            { "type": "text", "id": "pbc2-t", "name": "T", "content": "Alarmas Grado 3 para Industria y Joyería", "fontSize": 18, "fontWeight": "700", "fill": "#FFFFFF" },
                            { "type": "text", "id": "pbc2-d", "name": "D", "content": "Obligatorio para establecimientos de riesgo. Doble vía de comunicación con polling continuo y detección de inhibición.", "fontSize": 13, "fill": "#94A3B8", "lineHeight": 1.5 }
                        ]},
                        { "type": "text", "id": "pbc2-l", "name": "L", "content": "Ver especificaciones Grado 3 →", "fontSize": 13, "fontWeight": "700", "fill": RED_LIGHT }
                    ]},
                    # Card 3: Control Biométrico with Turnstiles Photo Fill
                    { "type": "frame", "id": "pbc-3", "name": "C3 Biometria", "width": 432, "height": 290, "cornerRadius": 14, "clip": True, "fill": photo_fill(IMG_BIOMETRIC_TURNSTILE, "#0B112044", "#0B1120F8"), "stroke": "#38BDF833", "strokeWidth": 1.5, "padding": [24, 24], "layout": "vertical", "justifyContent": "space_between", "children": [
                        { "type": "frame", "id": "pbc3-tags", "name": "Tags", "layout": "horizontal", "gap": 8, "children": [
                            { "type": "frame", "id": "p3-tag-1", "name": "Tag", "padding": [4, 10], "fill": "#0284C733", "stroke": "#38BDF8", "strokeWidth": 1, "cornerRadius": 6, "children": [
                                { "type": "text", "id": "p3-t1-txt", "name": "T", "content": "BIOMETRÍA 3D CONTACTLESS", "fontSize": 10, "fontWeight": "bold", "fill": "#7DD3FC" }
                            ]}
                        ]},
                        { "type": "frame", "id": "pbc3-body", "name": "Body", "layout": "vertical", "gap": 8, "children": [
                            { "type": "text", "id": "pbc3-t", "name": "T", "content": "Control de Accesos Biométrico y Tornos", "fontSize": 18, "fontWeight": "700", "fill": "#FFFFFF" },
                            { "type": "text", "id": "pbc3-d", "name": "D", "content": "Reconocimiento facial 3D, tornos rápidos y gestión de visitas en la nube con trazabilidad total para auditorías.", "fontSize": 13, "fill": "#94A3B8", "lineHeight": 1.5 }
                        ]},
                        { "type": "text", "id": "pbc3-l", "name": "L", "content": "Configurar control de accesos →", "fontSize": 13, "fontWeight": "700", "fill": "#38BDF8" }
                    ]}
                ]},
                # Bento Row 2
                { "type": "frame", "id": "pb-r2", "name": "R2", "layout": "horizontal", "gap": 24, "children": [
                    # Card 4: CRA 24/7 with SOC Photo Fill
                    { "type": "frame", "id": "pbc-4", "name": "C4 CRA", "width": 432, "height": 290, "cornerRadius": 14, "clip": True, "fill": photo_fill(IMG_HERO_CONTROL_ROOM, "#0B112044", "#0B1120F8"), "stroke": "#F59E0B33", "strokeWidth": 1.5, "padding": [24, 24], "layout": "vertical", "justifyContent": "space_between", "children": [
                        { "type": "frame", "id": "pbc4-tags", "name": "Tags", "layout": "horizontal", "gap": 8, "children": [
                            { "type": "frame", "id": "p4-tag-1", "name": "Tag", "padding": [4, 10], "fill": "#D9770633", "stroke": AMBER, "strokeWidth": 1, "cornerRadius": 6, "children": [
                                { "type": "text", "id": "p4-t1-txt", "name": "T", "content": "CRA PROPIA 24/7/365", "fontSize": 10, "fontWeight": "bold", "fill": "#FCD34D" }
                            ]}
                        ]},
                        { "type": "frame", "id": "pbc4-body", "name": "Body", "layout": "vertical", "gap": 8, "children": [
                            { "type": "text", "id": "pbc4-t", "name": "T", "content": "CRA 24/7 con Custodia y Acuda", "fontSize": 18, "fontWeight": "700", "fill": "#FFFFFF" },
                            { "type": "text", "id": "pbc4-d", "name": "D", "content": "Verificación por vídeo en tiempo real, custodia de llaves y despacho inmediato de patrulla homologada ante saltos reales.", "fontSize": 13, "fill": "#94A3B8", "lineHeight": 1.5 }
                        ]},
                        { "type": "text", "id": "pbc4-l", "name": "L", "content": "Protocolo de intervención CRA →", "fontSize": 13, "fontWeight": "700", "fill": "#FCD34D" }
                    ]},
                    # Card 5: PCI Fire Protection Photo Fill
                    { "type": "frame", "id": "pbc-5", "name": "C5 PCI", "width": 432, "height": 290, "cornerRadius": 14, "clip": True, "fill": photo_fill(IMG_FIRE_PROTECTION, "#0B112044", "#0B1120F8"), "stroke": BORDER_RED, "strokeWidth": 1.5, "padding": [24, 24], "layout": "vertical", "justifyContent": "space_between", "children": [
                        { "type": "frame", "id": "pbc5-tags", "name": "Tags", "layout": "horizontal", "gap": 8, "children": [
                            { "type": "frame", "id": "p5-tag-1", "name": "Tag", "padding": [4, 10], "fill": "#EF444433", "stroke": RED, "strokeWidth": 1, "cornerRadius": 6, "children": [
                                { "type": "text", "id": "p5-t1-txt", "name": "T", "content": "INDUSTRIA HOMOLOGADA", "fontSize": 10, "fontWeight": "bold", "fill": RED_LIGHT }
                            ]}
                        ]},
                        { "type": "frame", "id": "pbc5-body", "name": "Body", "layout": "vertical", "gap": 8, "children": [
                            { "type": "text", "id": "pbc5-t", "name": "T", "content": "Protección Contra Incendios (PCI)", "fontSize": 18, "fontWeight": "700", "fill": "#FFFFFF" },
                            { "type": "text", "id": "pbc5-d", "name": "D", "content": "Detección precoz por aspiración láser VESDA, extinción automática en salas técnicas/CPDs y mantenimiento según RIPCI.", "fontSize": 13, "fill": "#94A3B8", "lineHeight": 1.5 }
                        ]},
                        { "type": "text", "id": "pbc5-l", "name": "L", "content": "Sistemas de extinción y PCI →", "fontSize": 13, "fontWeight": "700", "fill": RED_LIGHT }
                    ]},
                    # Card 6: Ciberseguridad OT with CPD Photo Fill
                    { "type": "frame", "id": "pbc-6", "name": "C6 Ciber", "width": 432, "height": 290, "cornerRadius": 14, "clip": True, "fill": photo_fill(IMG_SERVER_CPD, "#0B112044", "#0B1120F8"), "stroke": "#8B5CF633", "strokeWidth": 1.5, "padding": [24, 24], "layout": "vertical", "justifyContent": "space_between", "children": [
                        { "type": "frame", "id": "pbc6-tags", "name": "Tags", "layout": "horizontal", "gap": 8, "children": [
                            { "type": "frame", "id": "p6-tag-1", "name": "Tag", "padding": [4, 10], "fill": "#7C3AED33", "stroke": "#A78BFA", "strokeWidth": 1, "cornerRadius": 6, "children": [
                                { "type": "text", "id": "p6-t1-txt", "name": "T", "content": "SEGURIDAD REDES OT", "fontSize": 10, "fontWeight": "bold", "fill": "#C4B5FD" }
                            ]}
                        ]},
                        { "type": "frame", "id": "pbc6-body", "name": "Body", "layout": "vertical", "gap": 8, "children": [
                            { "type": "text", "id": "pbc6-t", "name": "T", "content": "Ciberseguridad en Redes OT y CCTV", "fontSize": 18, "fontWeight": "700", "fill": "#FFFFFF" },
                            { "type": "text", "id": "pbc6-d", "name": "D", "content": "Segmentación VLAN segura para CCTV industrial, cifrado punto a punto y protección frente a ataques de denegación.", "fontSize": 13, "fill": "#94A3B8", "lineHeight": 1.5 }
                        ]},
                        { "type": "text", "id": "pbc6-l", "name": "L", "content": "Consultoría de seguridad integral →", "fontSize": 13, "fontWeight": "700", "fill": "#C4B5FD" }
                    ]}
                ]}
            ]
        },
        # 4-Phase Defense Architecture Protocol
        {
            "type": "frame", "id": "p1-protocol", "name": "Protocolo 4 Fases", "width": "fill_container", "fill": BG_CARD, "stroke": BORDER_LIGHT, "strokeWidth": { "top": 1, "bottom": 1 }, "layout": "vertical", "padding": [80, 48], "gap": 40, "children": [
                { "type": "frame", "id": "p1-prot-hdr", "name": "Hdr", "layout": "vertical", "gap": 10, "children": [
                    { "type": "text", "id": "p1-pr-eye", "name": "Eye", "content": "PROTOCOLO DE RESPUESTA INTEGRADA", "fontSize": 12, "fontWeight": "800", "fill": RED, "letterSpacing": 1 },
                    { "type": "text", "id": "p1-pr-title", "name": "Title", "content": "Cómo Funciona el Escudo Defensivo de Control 61", "fontSize": 36, "fontWeight": "800", "fill": "#FFFFFF" }
                ]},
                { "type": "frame", "id": "p1-steps-row", "name": "Steps", "layout": "horizontal", "gap": 20, "children": [
                    { "type": "frame", "id": "ps-1", "name": "S1", "width": 320, "height": 320, "fill": BG_DARK, "stroke": BORDER_CYAN, "strokeWidth": 1, "cornerRadius": 12, "padding": [24, 20], "layout": "vertical", "justifyContent": "space_between", "children": [
                        { "type": "text", "id": "ps1-num", "name": "Num", "content": "01", "fontSize": 28, "fontWeight": "800", "fill": CYAN },
                        { "type": "frame", "id": "ps1-body", "name": "Body", "layout": "vertical", "gap": 6, "children": [
                            { "type": "text", "id": "ps1-t", "name": "T", "content": "Detección Perimetral Anticipada", "fontSize": 16, "fontWeight": "700", "fill": "#FFFFFF" },
                            { "type": "text", "id": "ps1-d", "name": "D", "content": "Barreras infrarrojas y volumétricos de triple tecnología que detectan antes de la intrusión.", "fontSize": 12, "fill": "#94A3B8", "lineHeight": 1.5 }
                        ]},
                        { "type": "text", "id": "ps1-lat", "name": "Lat", "content": "LATENCIA: < 2 SEGUNDOS", "fontSize": 11, "fontWeight": "bold", "fill": EMERALD }
                    ]},
                    { "type": "frame", "id": "ps-2", "name": "S2", "width": 320, "height": 320, "fill": BG_DARK, "stroke": BORDER_CYAN, "strokeWidth": 1, "cornerRadius": 12, "padding": [24, 20], "layout": "vertical", "justifyContent": "space_between", "children": [
                        { "type": "text", "id": "ps2-num", "name": "Num", "content": "02", "fontSize": 28, "fontWeight": "800", "fill": CYAN_LIGHT },
                        { "type": "frame", "id": "ps2-body", "name": "Body", "layout": "vertical", "gap": 6, "children": [
                            { "type": "text", "id": "ps2-t", "name": "T", "content": "Verificación de Vídeo con IA", "fontSize": 16, "fontWeight": "700", "fill": "#FFFFFF" },
                            { "type": "text", "id": "ps2-d", "name": "D", "content": "Algoritmos de visión artificial descartan el 99.8% de falsas alarmas y validan el salto real.", "fontSize": 12, "fill": "#94A3B8", "lineHeight": 1.5 }
                        ]},
                        { "type": "text", "id": "ps2-lat", "name": "Lat", "content": "LATENCIA: < 10 SEGUNDOS", "fontSize": 11, "fontWeight": "bold", "fill": EMERALD }
                    ]},
                    { "type": "frame", "id": "ps-3", "name": "S3", "width": 320, "height": 320, "fill": BG_DARK, "stroke": BORDER_RED, "strokeWidth": 1, "cornerRadius": 12, "padding": [24, 20], "layout": "vertical", "justifyContent": "space_between", "children": [
                        { "type": "text", "id": "ps3-num", "name": "Num", "content": "03", "fontSize": 28, "fontWeight": "800", "fill": RED },
                        { "type": "frame", "id": "ps3-body", "name": "Body", "layout": "vertical", "gap": 6, "children": [
                            { "type": "text", "id": "ps3-t", "name": "T", "content": "Intervención SOC & Policía", "fontSize": 16, "fontWeight": "700", "fill": "#FFFFFF" },
                            { "type": "text", "id": "ps3-d", "name": "D", "content": "Central Receptora activa aviso a Policía Nacional y Guardia Civil por canal prioritario.", "fontSize": 12, "fill": "#94A3B8", "lineHeight": 1.5 }
                        ]},
                        { "type": "text", "id": "ps3-lat", "name": "Lat", "content": "LATENCIA: < 15 SEGUNDOS", "fontSize": 11, "fontWeight": "bold", "fill": RED }
                    ]},
                    { "type": "frame", "id": "ps-4", "name": "S4", "width": 320, "height": 320, "fill": BG_DARK, "stroke": BORDER_EMERALD, "strokeWidth": 1, "cornerRadius": 12, "padding": [24, 20], "layout": "vertical", "justifyContent": "space_between", "children": [
                        { "type": "text", "id": "ps4-num", "name": "Num", "content": "04", "fontSize": 28, "fontWeight": "800", "fill": EMERALD },
                        { "type": "frame", "id": "ps4-body", "name": "Body", "layout": "vertical", "gap": 6, "children": [
                            { "type": "text", "id": "ps4-t", "name": "T", "content": "Control y Telemetría en App", "fontSize": 16, "fontWeight": "700", "fill": "#FFFFFF" },
                            { "type": "text", "id": "ps4-d", "name": "D", "content": "Armado por zonas, histórico auditable y recepción de vídeo en tiempo real en tu smartphone.", "fontSize": 12, "fill": "#94A3B8", "lineHeight": 1.5 }
                        ]},
                        { "type": "text", "id": "ps4-lat", "name": "Lat", "content": "TIEMPO REAL EN DIRECTO", "fontSize": 11, "fontWeight": "bold", "fill": EMERALD }
                    ]}
                ]}
            ]
        },
        # Audit Booking Form Card Section
        {
            "type": "frame", "id": "p1-audit-sec", "name": "Sección Auditoría", "width": "fill_container", "height": 420, "fill": BG_DARK, "layout": "horizontal", "padding": [56, 64], "alignItems": "center", "justifyContent": "space_between", "children": [
                {
                    "type": "frame", "id": "p1-aud-l", "name": "Left", "width": 640, "layout": "vertical", "gap": 16, "children": [
                        { "type": "text", "id": "p1-al-eye", "name": "Eye", "content": "AUDITORÍA IN SITU GRATUITA", "fontSize": 12, "fontWeight": "800", "fill": EMERALD, "letterSpacing": 1 },
                        { "type": "text", "id": "p1-al-title", "name": "Title", "content": "¿Cumple su empresa con la normativa de seguridad privada y grado de riesgo exigido?", "fontSize": 32, "fontWeight": "800", "fill": "#FFFFFF", "lineHeight": 1.2, "textGrowth": "fixed-width", "width": 640 },
                        { "type": "text", "id": "p1-al-desc", "name": "Desc", "content": "Nuestros ingenieros colegiados realizan un análisis integral de vulnerabilidades, perímetro, CCTV y adecuación a la Orden INT/316/2011.", "fontSize": 14, "fill": "#94A3B8", "lineHeight": 1.5, "textGrowth": "fixed-width", "width": 600 }
                    ]
                },
                {
                    "type": "frame", "id": "p1-aud-r", "name": "Form Card", "width": 500, "height": 310, "fill": "#1E293BEE", "stroke": "#06B6D466", "strokeWidth": 1.5, "cornerRadius": 14, "padding": [24, 24], "layout": "vertical", "justifyContent": "space_between", "children": [
                        { "type": "text", "id": "p1-ft-t", "name": "Title", "content": "Solicitar Diagnóstico Técnico de Seguridad", "fontSize": 16, "fontWeight": "700", "fill": "#FFFFFF" },
                        { "type": "frame", "id": "p1-f-f1", "name": "F1", "height": 44, "fill": BG_DARK, "stroke": "#FFFFFF1A", "strokeWidth": 1, "cornerRadius": 6, "padding": [0, 16], "layout": "horizontal", "alignItems": "center", "children": [
                            { "type": "text", "id": "p1-f1-ph", "name": "P", "content": "Nombre de la Empresa o Nave Industrial", "fontSize": 13, "fill": "#64748B" }
                        ]},
                        { "type": "frame", "id": "p1-f-f2", "name": "F2", "height": 44, "fill": BG_DARK, "stroke": "#FFFFFF1A", "strokeWidth": 1, "cornerRadius": 6, "padding": [0, 16], "layout": "horizontal", "alignItems": "center", "children": [
                            { "type": "text", "id": "p1-f2-ph", "name": "P", "content": "Teléfono de Contacto Directo / Email Corporativo", "fontSize": 13, "fill": "#64748B" }
                        ]},
                        { "type": "frame", "id": "p1-f-btn", "name": "Submit", "height": 48, "fill": CYAN, "cornerRadius": 8, "alignItems": "center", "justifyContent": "center", "children": [
                            { "type": "text", "id": "p1-fb-txt", "name": "T", "content": "Enviar Solicitud de Auditoría Gratuita", "fontSize": 14, "fontWeight": "800", "fill": "#070A11" }
                        ]}
                    ]
                }
            ]
        },
        make_rich_footer("p1")
    ]
}

# =========================================================================
# 02. CCTV & IA VISION DEDICATED PAGE (1440 x 3600)
# =========================================================================
p2_cctv = {
    "type": "frame",
    "id": "screen-02-cctv",
    "name": "📹 02. CCTV & Visión Artificial IA (1440px)",
    "x": 1600,
    "y": 0,
    "width": 1440,
    "height": 3600,
    "fill": BG_DARK,
    "layout": "vertical",
    "clip": True,
    "children": [
        make_rich_header("p2", "CCTV & IA"),
        # Hero with Control Room Photography Fill
        {
            "type": "frame", "id": "p2-hero", "name": "Hero CCTV", "width": "fill_container", "height": 520, "cornerRadius": 0, "clip": True, "fill": photo_fill(IMG_HERO_CONTROL_ROOM, "#070A1144", "#070A11FA"), "layout": "vertical", "padding": [80, 48], "justifyContent": "center", "gap": 20, "children": [
                { "type": "frame", "id": "p2-badge", "name": "Badge", "padding": [4, 12], "fill": "#0891B244", "stroke": CYAN, "strokeWidth": 1, "cornerRadius": 16, "layout": "horizontal", "gap": 6, "children": [
                    { "type": "text", "id": "p2-btxt", "name": "T", "content": "VIDEOVIGILANCIA DE ALTA PRECISIÓN & ANALÍTICA IA", "fontSize": 11, "fontWeight": "bold", "fill": CYAN_LIGHT }
                ]},
                { "type": "text", "id": "p2-h1", "name": "H1", "content": "CCTV que Sirve Cuando de Verdad Hace Falta", "fontSize": 44, "fontWeight": "800", "fill": "#FFFFFF" },
                { "type": "text", "id": "p2-desc", "name": "D", "content": "No basta con instalar cámaras: hay que colocarlas bien, conservar la grabación el tiempo legal correcto y poder encontrar el momento exacto en segundos sin revisar horas de vídeo.", "fontSize": 16, "fill": "#94A3B8", "lineHeight": 1.6, "textGrowth": "fixed-width", "width": 800 },
                { "type": "frame", "id": "p2-hcta", "name": "CTA", "height": 50, "padding": [0, 24], "fill": CYAN, "cornerRadius": 8, "alignItems": "center", "justifyContent": "center", "children": [
                    { "type": "text", "id": "p2-ctatxt", "name": "T", "content": "Revisar Gratis mi Instalación Actual de CCTV", "fontSize": 14, "fontWeight": "700", "fill": "#070A11" }
                ]}
            ]
        },
        # 6 Capabilities Grid
        {
            "type": "frame", "id": "p2-grid-sec", "name": "6 Capacidades", "width": "fill_container", "fill": BG_DARK, "layout": "vertical", "padding": [80, 48], "gap": 36, "children": [
                { "type": "text", "id": "p2-ghdr", "name": "Hdr", "content": "Qué Incluye una Instalación Profesional de Videovigilancia", "fontSize": 32, "fontWeight": "800", "fill": "#FFFFFF" },
                { "type": "frame", "id": "p2-r1", "name": "R1", "layout": "horizontal", "gap": 24, "children": [
                    { "type": "frame", "id": "p2-c1", "name": "C1", "width": 432, "height": 240, "fill": BG_CARD, "stroke": BORDER_LIGHT, "strokeWidth": 1, "cornerRadius": 12, "padding": [24, 24], "layout": "vertical", "justifyContent": "space_between", "children": [
                        { "type": "icon", "id": "p2-ic1", "name": "I", "library": "lucide", "icon": "camera", "width": 28, "height": 28, "fill": CYAN },
                        { "type": "frame", "id": "p2-b1", "name": "B", "layout": "vertical", "gap": 6, "children": [
                            { "type": "text", "id": "p2-t1", "name": "T", "content": "Cámaras 4K Ultra Alta Resolución", "fontSize": 17, "fontWeight": "700", "fill": "#FFFFFF" },
                            { "type": "text", "id": "p2-d1", "name": "D", "content": "Óptica y ubicación calibradas para que la imagen sirva legalmente como prueba pericial ante jueces y aseguradoras.", "fontSize": 13, "fill": "#94A3B8", "lineHeight": 1.5 }
                        ]}
                    ]},
                    { "type": "frame", "id": "p2-c2", "name": "C2", "width": 432, "height": 240, "fill": BG_CARD, "stroke": BORDER_LIGHT, "strokeWidth": 1, "cornerRadius": 12, "padding": [24, 24], "layout": "vertical", "justifyContent": "space_between", "children": [
                        { "type": "icon", "id": "p2-ic2", "name": "I", "library": "lucide", "icon": "sun", "width": 28, "height": 28, "fill": AMBER },
                        { "type": "frame", "id": "p2-b2", "name": "B", "layout": "vertical", "gap": 6, "children": [
                            { "type": "text", "id": "p2-t2", "name": "T", "content": "Visión Nocturna UltraLowLight", "fontSize": 17, "fontWeight": "700", "fill": "#FFFFFF" },
                            { "type": "text", "id": "p2-d2", "name": "D", "content": "Equipos preparados para oscuridad total, lluvia torrencial, contraluces solares intensos y el calor del sureste.", "fontSize": 13, "fill": "#94A3B8", "lineHeight": 1.5 }
                        ]}
                    ]},
                    { "type": "frame", "id": "p2-c3", "name": "C3", "width": 432, "height": 240, "fill": BG_CARD, "stroke": BORDER_LIGHT, "strokeWidth": 1, "cornerRadius": 12, "padding": [24, 24], "layout": "vertical", "justifyContent": "space_between", "children": [
                        { "type": "icon", "id": "p2-ic3", "name": "I", "library": "lucide", "icon": "scan", "width": 28, "height": 28, "fill": EMERALD },
                        { "type": "frame", "id": "p2-b3", "name": "B", "layout": "vertical", "gap": 6, "children": [
                            { "type": "text", "id": "p2-t3", "name": "T", "content": "Búsqueda Inteligente de Vídeo IA", "fontSize": 17, "fontWeight": "700", "fill": "#FFFFFF" },
                            { "type": "text", "id": "p2-d3", "name": "D", "content": "Localiza en segundos cualquier evento por cruce de línea, color de ropa o matrícula sin revisar horas de grabación.", "fontSize": 13, "fill": "#94A3B8", "lineHeight": 1.5 }
                        ]}
                    ]}
                ]}
            ]
        },
        make_rich_footer("p2")
    ]
}

# =========================================================================
# 03. SEGURIDAD EMPRESAS & GRADO 3 (1440 x 3600)
# =========================================================================
p3_empresas = {
    "type": "frame",
    "id": "screen-03-empresas",
    "name": "🏭 03. Seguridad para Empresas & Grado 3 (1440px)",
    "x": 3200,
    "y": 0,
    "width": 1440,
    "height": 3600,
    "fill": BG_DARK,
    "layout": "vertical",
    "clip": True,
    "children": [
        make_rich_header("p3", "Empresas"),
        # Hero with Warehouse Photography Fill
        {
            "type": "frame", "id": "p3-hero", "name": "Hero Empresas", "width": "fill_container", "height": 520, "cornerRadius": 0, "clip": True, "fill": photo_fill(IMG_WAREHOUSE_NIGHT, "#070A1144", "#070A11FA"), "layout": "vertical", "padding": [80, 48], "justifyContent": "center", "gap": 20, "children": [
                { "type": "frame", "id": "p3-badge", "name": "Badge", "padding": [4, 12], "fill": "#0891B244", "stroke": CYAN, "strokeWidth": 1, "cornerRadius": 16, "layout": "horizontal", "gap": 6, "children": [
                    { "type": "text", "id": "p3-btxt", "name": "T", "content": "SEGURIDAD INDUSTRIAL HOMOLOGADA · CERTIFICACIÓN GRADO 3", "fontSize": 11, "fontWeight": "bold", "fill": CYAN_LIGHT }
                ]},
                { "type": "text", "id": "p3-h1", "name": "H1", "content": "Seguridad Integral para Naves, Logística y Oficinas", "fontSize": 44, "fontWeight": "800", "fill": "#FFFFFF" },
                { "type": "text", "id": "p3-desc", "name": "D", "content": "Un solo proveedor para proyectar, legalizar, instalar y mantener toda la seguridad de tu empresa. Alarmas Grado 3, PCI Incendios, CCTV y Accesos.", "fontSize": 16, "fill": "#94A3B8", "lineHeight": 1.6, "textGrowth": "fixed-width", "width": 800 },
                { "type": "frame", "id": "p3-hcta", "name": "CTA", "height": 50, "padding": [0, 24], "fill": CYAN, "cornerRadius": 8, "alignItems": "center", "justifyContent": "center", "children": [
                    { "type": "text", "id": "p3-ctatxt", "name": "T", "content": "Solicitar Proyecto de Seguridad Grado 3", "fontSize": 14, "fontWeight": "700", "fill": "#070A11" }
                ]}
            ]
        },
        make_rich_footer("p3")
    ]
}

# =========================================================================
# 04. CONSOLA SOC & CRA 24/7 (1440 x 1024)
# =========================================================================
p4_soc = {
    "type": "frame",
    "id": "screen-04-soc-console",
    "name": "🛰️ 04. Consola de Control SOC & CRA 24/7 (1440 x 1024)",
    "x": 0,
    "y": 5400,
    "width": 1440,
    "height": 1024,
    "fill": "#030712",
    "layout": "horizontal",
    "clip": True,
    "children": [
        # Sidebar
        {
            "type": "frame", "id": "p4-sb", "name": "Sidebar", "width": 260, "height": "fill_container", "fill": BG_CARD, "stroke": BORDER_LIGHT, "strokeWidth": { "right": 1 }, "layout": "vertical", "padding": [24, 16], "justifyContent": "space_between", "children": [
                { "type": "frame", "id": "p4-sbt", "name": "Top", "layout": "vertical", "gap": 22, "children": [
                    { "type": "text", "id": "p4-bn", "name": "B", "content": "SOC CONTROL 61", "fontSize": 16, "fontWeight": "800", "fill": "#FFFFFF", "letterSpacing": 1.2 },
                    { "type": "text", "id": "p4-m1", "name": "M1", "content": "● Matriz 4K en Vivo", "fontSize": 13, "fontWeight": "700", "fill": CYAN_LIGHT },
                    { "type": "text", "id": "p4-m2", "name": "M2", "content": "Historial Alarmas CRA", "fontSize": 13, "fill": "#94A3B8" },
                    { "type": "text", "id": "p4-m3", "name": "M3", "content": "Control Accesos LPR", "fontSize": 13, "fill": "#94A3B8" },
                    { "type": "text", "id": "p4-m4", "name": "M4", "content": "Radar Perimetral 3D", "fontSize": 13, "fill": "#94A3B8" }
                ]},
                { "type": "text", "id": "p4-op", "name": "Op", "content": "Operador: Toni García #04\nLicencia DGP Activa", "fontSize": 11, "fill": "#64748B" }
            ]
        },
        # Main Feeds Area
        {
            "type": "frame", "id": "p4-main", "name": "Main", "width": 1180, "height": "fill_container", "layout": "vertical", "children": [
                { "type": "frame", "id": "p4-hdr", "name": "Header", "width": "fill_container", "height": 56, "fill": BG_CARD, "stroke": BORDER_LIGHT, "strokeWidth": { "bottom": 1 }, "layout": "horizontal", "padding": [0, 24], "alignItems": "center", "justifyContent": "space_between", "children": [
                    { "type": "text", "id": "p4-stt", "name": "T", "content": "CENTRAL RECEPTORA OPERATIVA · 2.500+ RECINTOS CONECTADOS", "fontSize": 12, "fontWeight": "bold", "fill": "#FFFFFF" },
                    { "type": "text", "id": "p4-clk", "name": "C", "content": "UTC 11:55:00 · AES-256", "fontSize": 12, "fontWeight": "bold", "fill": CYAN }
                ]},
                { "type": "frame", "id": "p4-cgrid", "name": "Grid", "width": "fill_container", "height": 968, "padding": [16, 16], "layout": "horizontal", "gap": 16, "children": [
                    # CAM 1 Night
                    { "type": "frame", "id": "p4-cm1", "name": "CAM 1", "width": 560, "height": 450, "cornerRadius": 10, "clip": True, "fill": photo_fill(IMG_WAREHOUSE_NIGHT, "#070A1120", "#070A11D0"), "stroke": RED, "strokeWidth": 2, "padding": [16, 16], "layout": "vertical", "justifyContent": "space_between", "children": [
                        { "type": "text", "id": "p4-c1t", "name": "T", "content": "CAM-01 · Perímetro Norte Logístico", "fontSize": 14, "fontWeight": "bold", "fill": "#FFFFFF" },
                        { "type": "frame", "id": "p4-bbox1", "name": "Box", "height": 140, "fill": "#EF444433", "stroke": RED, "strokeWidth": 2, "cornerRadius": 8, "padding": [10, 10], "children": [
                            { "type": "text", "id": "p4-c1st", "name": "S", "content": "⚠️ INTRUSIÓN DETECTADA (99.4%)\nCruce Línea Virtual Sector C", "fontSize": 12, "fontWeight": "bold", "fill": "#FCA5A5" }
                        ]},
                        { "type": "text", "id": "p4-c1f", "name": "F", "content": "Aviso Directo a Policía Enviado (0.8s) · Patrulla Acuda ETA: 3m 40s", "fontSize": 12, "fontWeight": "bold", "fill": RED }
                    ]},
                    # CAM 2 Logistics Dock
                    { "type": "frame", "id": "p4-cm2", "name": "CAM 2", "width": 560, "height": 450, "cornerRadius": 10, "clip": True, "fill": photo_fill(IMG_LOGISTICS_DOCK, "#070A1120", "#070A11D0"), "stroke": EMERALD, "strokeWidth": 1.5, "padding": [16, 16], "layout": "vertical", "justifyContent": "space_between", "children": [
                        { "type": "text", "id": "p4-c2t", "name": "T", "content": "CAM-02 · LPR Acceso Muelle Vehicular", "fontSize": 14, "fontWeight": "bold", "fill": "#FFFFFF" },
                        { "type": "frame", "id": "p4-bbox2", "name": "Box", "height": 140, "fill": "#10B98126", "stroke": EMERALD, "strokeWidth": 1.5, "cornerRadius": 8, "padding": [10, 10], "children": [
                            { "type": "text", "id": "p4-c2st", "name": "S", "content": "MATRÍCULA: 4821-LMR [Reconocida]\nVehículo Autorizado · Flota Central", "fontSize": 12, "fontWeight": "bold", "fill": "#86EFAC" }
                        ]},
                        { "type": "text", "id": "p4-c2f", "name": "F", "content": "● AUTORIZADO · BARRERA AUTOMÁTICA ACCIONADA", "fontSize": 12, "fontWeight": "bold", "fill": EMERALD }
                    ]}
                ]}
            ]
        }
    ]
}

# =========================================================================
# 05. HOGAR & RESIDENCIAL (1440 x 3400)
# =========================================================================
p5_hogar = {
    "type": "frame",
    "id": "screen-05-hogar",
    "name": "🏡 05. Hogar & Residencial Sin Permanencias (1440px)",
    "x": 4800,
    "y": 0,
    "width": 1440,
    "height": 3400,
    "fill": BG_DARK,
    "layout": "vertical",
    "clip": True,
    "children": [
        make_rich_header("p5", "Hogar"),
        # Hero with Residential Villa Photography Fill
        {
            "type": "frame", "id": "p5-hero", "name": "Hero Hogar", "width": "fill_container", "height": 520, "cornerRadius": 0, "clip": True, "fill": photo_fill(IMG_RESIDENTIAL_VILLA, "#070A1144", "#070A11FA"), "layout": "vertical", "padding": [80, 48], "justifyContent": "center", "gap": 20, "children": [
                { "type": "frame", "id": "p5-badge", "name": "Badge", "padding": [4, 12], "fill": "#10B98133", "stroke": EMERALD, "strokeWidth": 1, "cornerRadius": 16, "layout": "horizontal", "gap": 6, "children": [
                    { "type": "text", "id": "p5-btxt", "name": "T", "content": "PROTECCIÓN RESIDENCIAL TRANSPARENTE", "fontSize": 11, "fontWeight": "bold", "fill": EMERALD_LIGHT }
                ]},
                { "type": "text", "id": "p5-h1", "name": "H1", "content": "Alarmas para Casa Sin Cuotas Trampa ni Permanencias", "fontSize": 44, "fontWeight": "800", "fill": "#FFFFFF" },
                { "type": "text", "id": "p5-desc", "name": "D", "content": "Eres dueño de tus equipos. Seguridad Grado 2 con verificación por vídeo, control total desde la app móvil y servicio de guardia 24 horas.", "fontSize": 16, "fill": "#94A3B8", "lineHeight": 1.6, "textGrowth": "fixed-width", "width": 800 },
                { "type": "frame", "id": "p5-hcta", "name": "CTA", "height": 50, "padding": [0, 24], "fill": CYAN, "cornerRadius": 8, "alignItems": "center", "justifyContent": "center", "children": [
                    { "type": "text", "id": "p5-ctatxt", "name": "T", "content": "Calcular Presupuesto para Mi Vivienda", "fontSize": 14, "fontWeight": "700", "fill": "#070A11" }
                ]}
            ]
        },
        make_rich_footer("p5")
    ]
}

# =========================================================================
# 06. MOBILE SMARTPHONE VIEW (390 x 2800)
# =========================================================================
p6_mobile = {
    "type": "frame",
    "id": "screen-06-mobile",
    "name": "📱 06. App Móvil Smartphone (390px)",
    "x": 6400,
    "y": 0,
    "width": 390,
    "height": 2800,
    "fill": BG_DARK,
    "layout": "vertical",
    "clip": True,
    "children": [
        {
            "type": "frame", "id": "m-hdr", "name": "Hdr", "width": "fill_container", "height": 64, "fill": BG_CARD, "stroke": BORDER_LIGHT, "strokeWidth": { "bottom": 1 }, "layout": "horizontal", "padding": [0, 16], "alignItems": "center", "justifyContent": "space_between", "children": [
                { "type": "text", "id": "m-b", "name": "B", "content": "CONTROL 61", "fontSize": 15, "fontWeight": "800", "fill": "#FFFFFF" },
                { "type": "text", "id": "m-p", "name": "P", "content": "📞 968 622 984", "fontSize": 12, "fontWeight": "bold", "fill": RED }
            ]
        },
        {
            "type": "frame", "id": "m-body", "name": "Body", "width": "fill_container", "padding": [24, 16], "layout": "vertical", "gap": 18, "children": [
                { "type": "text", "id": "m-h1", "name": "H1", "content": "Seguridad Avanzada, CCTV IA y Alarmas Grado 3", "fontSize": 26, "fontWeight": "800", "fill": "#FFFFFF" },
                { "type": "text", "id": "m-sub", "name": "Sub", "content": "Ingeniería de seguridad homologada en Murcia. Conexión directa a CRA en <15s.", "fontSize": 13, "fill": "#94A3B8" },
                # Mobile Cam Card with Photo Fill
                { "type": "frame", "id": "m-cam-box", "name": "Cam Box", "width": "fill_container", "height": 220, "cornerRadius": 10, "clip": True, "fill": photo_fill(IMG_WAREHOUSE_NIGHT, "#070A1120", "#070A11D0"), "stroke": RED, "strokeWidth": 2, "padding": [12, 12], "layout": "vertical", "justifyContent": "space_between", "children": [
                    { "type": "text", "id": "m-c1-t", "name": "T", "content": "CAM-01 · Perímetro Norte (4K IA)", "fontSize": 11, "fontWeight": "bold", "fill": "#FFFFFF" },
                    { "type": "text", "id": "m-c1-s", "name": "S", "content": "⚠️ Intrusión Detectada (99.4%)\nAviso Despachado a Policía", "fontSize": 10, "fontWeight": "bold", "fill": "#FCA5A5" }
                ]},
                {
                    "type": "frame", "id": "m-btn", "name": "Btn", "height": 48, "fill": CYAN, "cornerRadius": 8, "alignItems": "center", "justifyContent": "center", "children": [
                        { "type": "text", "id": "m-btxt", "name": "T", "content": "Solicitar Valoración Gratuita", "fontSize": 14, "fontWeight": "800", "fill": "#070A11" }
                    ]
                }
            ]
        }
    ]
}

all_rich_screens = [p1_landing, p2_cctv, p3_empresas, p4_soc, p5_hogar, p6_mobile]

doc = {
    "version": "2.19",
    "children": all_rich_screens
}

with open("/Users/toni/Proyectos/Control61-Web/control61_modern_ui.pen", "w") as f:
    json.dump(doc, f, indent=2)

print("Saved 6 Master High-Fidelity Screens to control61_modern_ui.pen!")

# Sync atomically to active Pencil Desktop app window
js_code = """
let allNodes = Get((n, c) => { c.skipChildren(); return n.id; });
for (let id of allNodes) {
    try { Delete(id); } catch(e) {}
}
"""

for screen in all_rich_screens:
    js_code += f"Insert(document, {json.dumps(screen)});\n"

js_code += "Print('All 6 rich screens inserted successfully');"

cmd_input = f"""execute({{ input: {json.dumps(js_code)} }})\nsave()\nexit()\n"""

p = subprocess.run(
    ["pen", "interactive", "-a", "desktop", "-i", "/Users/toni/Proyectos/Control61-Web/control61_modern_ui.pen"],
    input=cmd_input,
    text=True,
    capture_output=True,
    env={"PEN_CLI_KEY": "pencil_cli_aebcdc64faa119be3d732b81edf1af9229f7f20f", "PATH": "/Users/toni/.npm-global/bin:/usr/local/bin:/usr/bin:/bin:/usr/sbin:/sbin"}
)

print("Pencil Desktop Sync Output:")
print(p.stdout)
