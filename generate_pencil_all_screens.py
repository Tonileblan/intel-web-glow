import json

def build_all_screens():
    # Common styles
    c_bg_dark = "#070A11"
    c_card_bg = "#0B1120"
    c_card_inner = "#0F172A"
    c_cyan = "#06B6D4"
    c_cyan_light = "#22D3EE"
    c_emerald = "#10B981"
    c_red = "#EF4444"
    c_amber = "#F59E0B"
    c_border_light = "#FFFFFF14"
    c_border_cyan = "#06B6D433"
    
    # Common Header Maker
    def make_header(page_id, active_nav):
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
                "fill": c_cyan_light if is_active else "#94A3B8"
            })
            
        return {
            "type": "frame",
            "id": f"{page_id}-navbar",
            "name": "Navbar Glassmorphism",
            "width": "fill_container",
            "height": 76,
            "fill": "#0B1120EE",
            "stroke": c_border_light,
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
                    "gap": 10,
                    "alignItems": "center",
                    "children": [
                        {
                            "type": "frame",
                            "id": f"{page_id}-logo-box",
                            "name": "Box",
                            "width": 40,
                            "height": 40,
                            "fill": "#0891B226",
                            "stroke": c_cyan,
                            "strokeWidth": 1.5,
                            "cornerRadius": 8,
                            "alignItems": "center",
                            "justifyContent": "center",
                            "children": [
                                { "type": "icon", "id": f"{page_id}-sh-ico", "name": "Ico", "library": "lucide", "icon": "shield-check", "width": 22, "height": 22, "fill": c_cyan }
                            ]
                        },
                        {
                            "type": "frame",
                            "id": f"{page_id}-btexts",
                            "name": "Text",
                            "layout": "vertical",
                            "gap": 2,
                            "children": [
                                { "type": "text", "id": f"{page_id}-bname", "name": "Name", "content": "CONTROL 61", "fontSize": 18, "fontWeight": "800", "fill": "#FFFFFF", "letterSpacing": 1.2 },
                                { "type": "text", "id": f"{page_id}-bsub", "name": "Sub", "content": "SISTEMAS INTELIGENTES DE SEGURIDAD", "fontSize": 8, "fontWeight": "600", "fill": "#94A3B8", "letterSpacing": 0.6 }
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
                            "height": 38,
                            "padding": [0, 14],
                            "fill": "#1E293B80",
                            "stroke": "#FFFFFF26",
                            "strokeWidth": 1,
                            "cornerRadius": 6,
                            "layout": "horizontal",
                            "gap": 6,
                            "alignItems": "center",
                            "children": [
                                { "type": "icon", "id": f"{page_id}-pi", "name": "I", "library": "lucide", "icon": "phone", "width": 13, "height": 13, "fill": c_red },
                                { "type": "text", "id": f"{page_id}-pt", "name": "T", "content": "968 622 984", "fontSize": 12, "fontWeight": "600", "fill": "#F1F5F9" }
                            ]
                        },
                        {
                            "type": "frame",
                            "id": f"{page_id}-btn-aud",
                            "name": "Audit",
                            "height": 38,
                            "padding": [0, 16],
                            "fill": c_cyan,
                            "cornerRadius": 6,
                            "alignItems": "center",
                            "justifyContent": "center",
                            "children": [
                                { "type": "text", "id": f"{page_id}-at", "name": "T", "content": "Valoración Gratuita", "fontSize": 12, "fontWeight": "700", "fill": "#070A11" }
                            ]
                        }
                    ]
                }
            ]
        }

    # Common Footer Maker
    def make_footer(page_id):
        return {
            "type": "frame",
            "id": f"{page_id}-footer",
            "name": "Footer Corporativo",
            "width": "fill_container",
            "height": 280,
            "fill": "#070A11",
            "layout": "vertical",
            "padding": [40, 48, 24, 48],
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
                            "type": "frame", "id": f"{page_id}-ft-c1", "name": "C1", "width": 400, "layout": "vertical", "gap": 10, "children": [
                                { "type": "text", "id": f"{page_id}-ft-t", "name": "T", "content": "CONTROL 61 · SISTEMAS DE SEGURIDAD", "fontSize": 15, "fontWeight": "800", "fill": "#FFFFFF", "letterSpacing": 1 },
                                { "type": "text", "id": f"{page_id}-ft-d", "name": "D", "content": "Desarrollos y Sistemas Inteligentes S.L. · DGP Nº 2341\nEspecialistas en Grado 3, CCTV IA y CRA propia 24/7.\nPol. Ind. La Polvorista, Molina de Segura (Murcia)", "fontSize": 12, "fill": "#64748B", "lineHeight": 1.6 }
                            ]
                        },
                        {
                            "type": "frame", "id": f"{page_id}-ft-c2", "name": "C2", "layout": "vertical", "gap": 8, "children": [
                                { "type": "text", "id": f"{page_id}-ft-h2", "name": "H", "content": "SERVICIOS PRINCIPALES", "fontSize": 12, "fontWeight": "700", "fill": c_cyan },
                                { "type": "text", "id": f"{page_id}-fl-1", "name": "L", "content": "Alarmas Homologadas Grado 3", "fontSize": 13, "fill": "#94A3B8" },
                                { "type": "text", "id": f"{page_id}-fl-2", "name": "L", "content": "CCTV Inteligente e IA Perimetral", "fontSize": 13, "fill": "#94A3B8" },
                                { "type": "text", "id": f"{page_id}-fl-3", "name": "L", "content": "Control de Accesos Biométrico 3D", "fontSize": 13, "fill": "#94A3B8" }
                            ]
                        },
                        {
                            "type": "frame", "id": f"{page_id}-ft-c3", "name": "C3", "layout": "vertical", "gap": 8, "children": [
                                { "type": "text", "id": f"{page_id}-ft-h3", "name": "H", "content": "CONTACTO DIRECTO", "fontSize": 12, "fontWeight": "700", "fill": c_cyan },
                                { "type": "text", "id": f"{page_id}-fc-1", "name": "L", "content": "📞 Centralita y Averías 24h: 968 622 984", "fontSize": 13, "fill": "#94A3B8" },
                                { "type": "text", "id": f"{page_id}-fc-2", "name": "L", "content": "✉️ info@control61.com", "fontSize": 13, "fill": "#94A3B8" },
                                { "type": "text", "id": f"{page_id}-fc-3", "name": "L", "content": "🛡️ Asistencia Inmediata en Región de Murcia", "fontSize": 13, "fill": "#10B981" }
                            ]
                        }
                    ]
                },
                {
                    "type": "frame",
                    "id": f"{page_id}-ft-cr",
                    "name": "CR Bar",
                    "width": "fill_container",
                    "height": 36,
                    "stroke": c_border_light,
                    "strokeWidth": { "top": 1 },
                    "layout": "horizontal",
                    "justifyContent": "space_between",
                    "alignItems": "center",
                    "children": [
                        { "type": "text", "id": f"{page_id}-cr-1", "name": "C", "content": "© 2026 Control 61. By Toni.", "fontSize": 12, "fill": "#475569" },
                        { "type": "text", "id": f"{page_id}-cr-2", "name": "L", "content": "Aviso Legal · Privacidad · Normativa DGP 2341 · ISO 9001", "fontSize": 12, "fill": "#475569" }
                    ]
                }
            ]
        }

    # =========================================================================
    # 01. SCREEN: HOME / LANDING (1440 x 4800)
    # =========================================================================
    p1_landing = {
        "type": "frame",
        "id": "screen-01-home",
        "name": "🏠 01. Inicio / Landing Principal (1440px)",
        "x": 0,
        "y": 0,
        "width": 1440,
        "height": 4600,
        "fill": c_bg_dark,
        "layout": "vertical",
        "clip": True,
        "children": [
            # Top Bar
            {
                "type": "frame", "id": "p1-top-bar", "name": "Top Status", "width": "fill_container", "height": 40, "fill": c_card_inner, "stroke": c_border_cyan, "strokeWidth": { "bottom": 1 }, "layout": "horizontal", "padding": [0, 48], "alignItems": "center", "justifyContent": "space_between", "children": [
                    { "type": "frame", "id": "p1-tb-l", "name": "L", "layout": "horizontal", "gap": 8, "alignItems": "center", "children": [
                        { "type": "ellipse", "id": "p1-dot", "name": "D", "width": 8, "height": 8, "fill": c_emerald },
                        { "type": "text", "id": "p1-st-txt", "name": "T", "content": "CENTRAL RECEPTORA DE ALARMAS 24/7/365 · HOMOLOGADA GRADO 3 · DGP Nº 2341", "fontSize": 11, "fontWeight": "bold", "fill": "#38BDF8" }
                    ]},
                    { "type": "text", "id": "p1-tb-r", "name": "R", "content": "🚨 Teléfono Centralita Urgencias 24h: 968 622 984", "fontSize": 12, "fontWeight": "600", "fill": "#F1F5F9" }
                ]
            },
            make_header("p1", "Inicio"),
            # Hero Section
            {
                "type": "frame", "id": "p1-hero", "name": "Hero Section", "width": "fill_container", "height": 680, "fill": c_bg_dark, "layout": "horizontal", "padding": [56, 48], "gap": 48, "alignItems": "center", "justifyContent": "space_between", "children": [
                    {
                        "type": "frame", "id": "p1-h-l", "name": "Left", "width": 640, "layout": "vertical", "gap": 22, "children": [
                            { "type": "frame", "id": "p1-badge", "name": "Badge", "height": 30, "padding": [0, 12], "fill": "#0891B226", "stroke": "#06B6D466", "strokeWidth": 1, "cornerRadius": 16, "layout": "horizontal", "gap": 6, "alignItems": "center", "children": [
                                { "type": "text", "id": "p1-btxt", "name": "T", "content": "HOMOLOGACIÓN NACIONAL DGP Nº 2341 · CERTIFICACIÓN GRADO 3", "fontSize": 10, "fontWeight": "700", "fill": c_cyan_light }
                            ]},
                            { "type": "text", "id": "p1-h1", "name": "H1", "content": "Sistemas de Seguridad Avanzada, CCTV con IA y Alarmas de Grado 3", "fontSize": 44, "fontWeight": "800", "fill": "#FFFFFF", "lineHeight": 1.15, "textGrowth": "fixed-width", "width": 640 },
                            { "type": "text", "id": "p1-hdesc", "name": "Desc", "content": "Ingeniería e instalación de alarmas de Grado 2 y 3, videovigilancia de alta precisión y control de accesos para empresas, instituciones y hogares en Murcia y Levante.", "fontSize": 15, "fill": "#94A3B8", "lineHeight": 1.6, "textGrowth": "fixed-width", "width": 620 },
                            {
                                "type": "frame", "id": "p1-h-btns", "name": "Btns", "layout": "horizontal", "gap": 16, "children": [
                                    { "type": "frame", "id": "p1-btn-main", "name": "CTA", "height": 50, "padding": [0, 24], "fill": c_cyan, "cornerRadius": 8, "alignItems": "center", "justifyContent": "center", "children": [
                                        { "type": "text", "id": "p1-bmt", "name": "T", "content": "Solicitar Valoración Gratuita", "fontSize": 14, "fontWeight": "700", "fill": "#070A11" }
                                    ]},
                                    { "type": "frame", "id": "p1-btn-sec", "name": "Phone", "height": 50, "padding": [0, 20], "fill": "#1E293B80", "stroke": "#FFFFFF26", "strokeWidth": 1, "cornerRadius": 8, "layout": "horizontal", "gap": 8, "alignItems": "center", "children": [
                                        { "type": "icon", "id": "p1-pi", "name": "I", "library": "lucide", "icon": "phone", "width": 16, "height": 16, "fill": c_red },
                                        { "type": "text", "id": "p1-pst", "name": "T", "content": "968 622 984 · Averías 24h", "fontSize": 13, "fontWeight": "600", "fill": "#F1F5F9" }
                                    ]}
                                ]
                            }
                        ]
                    },
                    # Hero Right HUD
                    {
                        "type": "frame", "id": "p1-hud", "name": "HUD Box", "width": 640, "height": 450, "fill": c_card_bg, "stroke": "#06B6D440", "strokeWidth": 1.5, "cornerRadius": 14, "layout": "vertical", "clip": True, "children": [
                            { "type": "frame", "id": "p1-hh", "name": "Header", "width": "fill_container", "height": 44, "fill": c_card_inner, "stroke": c_border_light, "strokeWidth": { "bottom": 1 }, "layout": "horizontal", "padding": [0, 16], "alignItems": "center", "justifyContent": "space_between", "children": [
                                { "type": "text", "id": "p1-htitle", "name": "T", "content": "CONTROL61_SOC://MURCIA · GRADO 3 ACTIVO", "fontSize": 11, "fontWeight": "bold", "fill": "#FFFFFF" },
                                { "type": "text", "id": "p1-hlat", "name": "L", "content": "AES-256 | LATENCIA: 12ms", "fontSize": 10, "fontWeight": "bold", "fill": c_emerald }
                            ]},
                            { "type": "frame", "id": "p1-hcams", "name": "Cams", "width": "fill_container", "height": 290, "fill": "#030712", "layout": "horizontal", "gap": 10, "padding": [10, 10], "children": [
                                { "type": "frame", "id": "p1-c1", "name": "CAM 1", "width": 305, "height": 270, "fill": c_card_inner, "stroke": c_red, "strokeWidth": 2, "cornerRadius": 8, "padding": [10, 10], "layout": "vertical", "justifyContent": "space_between", "children": [
                                    { "type": "text", "id": "p1-c1-t", "name": "T", "content": "CAM-01 · Perímetro Norte (4K IA)", "fontSize": 11, "fontWeight": "bold", "fill": "#FFFFFF" },
                                    { "type": "frame", "id": "p1-c1-b", "name": "Box", "height": 110, "fill": "#EF44441F", "stroke": c_red, "strokeWidth": 1, "cornerRadius": 6, "padding": [8, 8], "children": [
                                        { "type": "text", "id": "p1-c1-txt", "name": "T", "content": "⚠️ Intrusión Detectada (99.4%)\nCruce Línea Virtual Sector C", "fontSize": 10, "fontWeight": "bold", "fill": "#FCA5A5" }
                                    ]},
                                    { "type": "text", "id": "p1-c1-ft", "name": "F", "content": "Aviso Directo a Policía Despachado", "fontSize": 10, "fontWeight": "bold", "fill": c_red }
                                ]},
                                { "type": "frame", "id": "p1-c2", "name": "CAM 2", "width": 305, "height": 270, "fill": c_card_inner, "stroke": c_emerald, "strokeWidth": 1.5, "cornerRadius": 8, "padding": [10, 10], "layout": "vertical", "justifyContent": "space_between", "children": [
                                    { "type": "text", "id": "p1-c2-t", "name": "T", "content": "CAM-02 · Acceso Muelle LPR", "fontSize": 11, "fontWeight": "bold", "fill": "#FFFFFF" },
                                    { "type": "frame", "id": "p1-c2-b", "name": "Box", "height": 110, "fill": "#10B9811A", "stroke": c_emerald, "strokeWidth": 1, "cornerRadius": 6, "padding": [8, 8], "children": [
                                        { "type": "text", "id": "p1-c2-txt", "name": "T", "content": "MATRÍCULA: 4821-LMR\nVehículo Autorizado · Flota Central", "fontSize": 10, "fontWeight": "bold", "fill": "#86EFAC" }
                                    ]},
                                    { "type": "text", "id": "p1-c2-ft", "name": "F", "content": "Barrera Automática Accionada", "fontSize": 10, "fontWeight": "bold", "fill": c_emerald }
                                ]}
                            ]},
                            { "type": "frame", "id": "p1-hft", "name": "Ft", "width": "fill_container", "height": 116, "fill": c_card_inner, "layout": "horizontal", "padding": [10, 16], "justifyContent": "space_between", "alignItems": "center", "children": [
                                { "type": "text", "id": "p1-hf1", "name": "T1", "content": "RED: Doble Vía Fibra+5G", "fontSize": 11, "fontWeight": "bold", "fill": c_cyan },
                                { "type": "text", "id": "p1-hf2", "name": "T2", "content": "CRA: <15s Respuesta", "fontSize": 11, "fontWeight": "bold", "fill": c_emerald },
                                { "type": "text", "id": "p1-hf3", "name": "T3", "content": "SLA: 99.9% Operativo", "fontSize": 11, "fontWeight": "bold", "fill": c_amber }
                            ]}
                        ]
                    }
                ]
            },
            # Bento Strip
            {
                "type": "frame", "id": "p1-kpis", "name": "KPIs", "width": "fill_container", "height": 130, "fill": c_card_bg, "stroke": c_border_cyan, "strokeWidth": { "top": 1, "bottom": 1 }, "layout": "horizontal", "padding": [0, 48], "alignItems": "center", "justifyContent": "space_between", "children": [
                    { "type": "frame", "id": "pk-1", "name": "K1", "layout": "vertical", "gap": 2, "children": [
                        { "type": "text", "id": "pkn-1", "name": "N", "content": "+2.500", "fontSize": 32, "fontWeight": "800", "fill": c_cyan },
                        { "type": "text", "id": "pkl-1", "name": "L", "content": "Clientes protegidos en Murcia", "fontSize": 12, "fill": "#94A3B8" }
                    ]},
                    { "type": "frame", "id": "pk-2", "name": "K2", "layout": "vertical", "gap": 2, "children": [
                        { "type": "text", "id": "pkn-2", "name": "N", "content": "< 15s", "fontSize": 32, "fontWeight": "800", "fill": c_emerald },
                        { "type": "text", "id": "pkl-2", "name": "L", "content": "Respuesta inmediata CRA", "fontSize": 12, "fill": "#94A3B8" }
                    ]},
                    { "type": "frame", "id": "pk-3", "name": "K3", "layout": "vertical", "gap": 2, "children": [
                        { "type": "text", "id": "pkn-3", "name": "N", "content": "99.9%", "fontSize": 32, "fontWeight": "800", "fill": "#38BDF8" },
                        { "type": "text", "id": "pkl-3", "name": "L", "content": "Disponibilidad de red", "fontSize": 12, "fill": "#94A3B8" }
                    ]},
                    { "type": "frame", "id": "pk-4", "name": "K4", "layout": "vertical", "gap": 2, "children": [
                        { "type": "text", "id": "pkn-4", "name": "N", "content": "20+ Años", "fontSize": 32, "fontWeight": "800", "fill": c_amber },
                        { "type": "text", "id": "pkl-4", "name": "L", "content": "Trayectoria homologada", "fontSize": 12, "fill": "#94A3B8" }
                    ]}
                ]
            },
            # 6 Bento Services
            {
                "type": "frame", "id": "p1-bento", "name": "Bento Grid", "width": "fill_container", "fill": c_bg_dark, "layout": "vertical", "padding": [64, 48], "gap": 32, "children": [
                    { "type": "frame", "id": "pb-hdr", "name": "Hdr", "layout": "vertical", "gap": 8, "children": [
                        { "type": "text", "id": "pb-eye", "name": "Eye", "content": "SOLUCIONES DE SEGURIDAD INTEGRAL", "fontSize": 11, "fontWeight": "800", "fill": c_cyan, "letterSpacing": 1 },
                        { "type": "text", "id": "pb-title", "name": "T", "content": "Ingeniería de Protección Sin Puntos Ciegos", "fontSize": 32, "fontWeight": "800", "fill": "#FFFFFF" }
                    ]},
                    { "type": "frame", "id": "pb-r1", "name": "R1", "layout": "horizontal", "gap": 20, "children": [
                        { "type": "frame", "id": "pbc-1", "name": "C1", "width": 433, "height": 220, "fill": c_card_bg, "stroke": c_border_cyan, "strokeWidth": 1, "cornerRadius": 12, "padding": [22, 22], "layout": "vertical", "justifyContent": "space_between", "children": [
                            { "type": "text", "id": "pbc1-t", "name": "T", "content": "Alarmas Homologadas Grado 3", "fontSize": 16, "fontWeight": "700", "fill": "#FFFFFF" },
                            { "type": "text", "id": "pbc1-d", "name": "D", "content": "Obligatorio para establecimientos de riesgo. Doble vía de comunicación con supervisión por polling y detección de inhibición.", "fontSize": 12, "fill": "#94A3B8", "lineHeight": 1.5 },
                            { "type": "text", "id": "pbc1-l", "name": "L", "content": "Ver normativa Grado 3 →", "fontSize": 12, "fontWeight": "700", "fill": c_cyan_light }
                        ]},
                        { "type": "frame", "id": "pbc-2", "name": "C2", "width": 433, "height": 220, "fill": c_card_bg, "stroke": "#10B98133", "strokeWidth": 1, "cornerRadius": 12, "padding": [22, 22], "layout": "vertical", "justifyContent": "space_between", "children": [
                            { "type": "text", "id": "pbc2-t", "name": "T", "content": "CCTV Inteligente e IA Térmica", "fontSize": 16, "fontWeight": "700", "fill": "#FFFFFF" },
                            { "type": "text", "id": "pbc2-d", "name": "D", "content": "Detección térmica perimetral, radar perimétrico integrado y clasificación automática de humanos y vehículos.", "fontSize": 12, "fill": "#94A3B8", "lineHeight": 1.5 },
                            { "type": "text", "id": "pbc2-l", "name": "L", "content": "Explorar analítica IA →", "fontSize": 12, "fontWeight": "700", "fill": "#34D399" }
                        ]},
                        { "type": "frame", "id": "pbc-3", "name": "C3", "width": 433, "height": 220, "fill": c_card_bg, "stroke": "#38BDF833", "strokeWidth": 1, "cornerRadius": 12, "padding": [22, 22], "layout": "vertical", "justifyContent": "space_between", "children": [
                            { "type": "text", "id": "pbc3-t", "name": "T", "content": "Control de Accesos Biométrico", "fontSize": 16, "fontWeight": "700", "fill": "#FFFFFF" },
                            { "type": "text", "id": "pbc3-d", "name": "D", "content": "Reconocimiento facial 3D contactless, lectores de matrícula LPR y gestión de visitas en la nube con trazabilidad total.", "fontSize": 12, "fill": "#94A3B8", "lineHeight": 1.5 },
                            { "type": "text", "id": "pbc3-l", "name": "L", "content": "Configurar accesos →", "fontSize": 12, "fontWeight": "700", "fill": "#38BDF8" }
                        ]}
                    ]}
                ]
            },
            make_footer("p1")
        ]
    }

    # =========================================================================
    # 02. SCREEN: CCTV & IA VISION (1440 x 3000)
    # =========================================================================
    p2_cctv = {
        "type": "frame",
        "id": "screen-02-cctv",
        "name": "📹 02. CCTV & Visión Artificial IA (1440px)",
        "x": 1600,
        "y": 0,
        "width": 1440,
        "height": 3000,
        "fill": c_bg_dark,
        "layout": "vertical",
        "clip": True,
        "children": [
            make_header("p2", "CCTV & IA"),
            # Hero CCTV
            {
                "type": "frame", "id": "p2-hero", "name": "Hero CCTV", "width": "fill_container", "height": 480, "fill": c_card_bg, "layout": "vertical", "padding": [64, 48], "justifyContent": "center", "gap": 18, "children": [
                    { "type": "text", "id": "p2-eye", "name": "Eye", "content": "VIDEOVIGILANCIA DE ALTA PRECISIÓN", "fontSize": 11, "fontWeight": "800", "fill": c_cyan, "letterSpacing": 1 },
                    { "type": "text", "id": "p2-h1", "name": "H1", "content": "CCTV que Sirve Cuando de Verdad Hace Falta", "fontSize": 40, "fontWeight": "800", "fill": "#FFFFFF" },
                    { "type": "text", "id": "p2-desc", "name": "D", "content": "No basta con instalar cámaras: hay que colocarlas bien, conservar la grabación el tiempo correcto y poder encontrar el momento exacto en segundos sin revisar horas de vídeo.", "fontSize": 16, "fill": "#94A3B8", "lineHeight": 1.6, "textGrowth": "fixed-width", "width": 800 },
                    {
                        "type": "frame", "id": "p2-cta-row", "name": "CTA", "layout": "horizontal", "gap": 16, "children": [
                            { "type": "frame", "id": "p2-btn1", "name": "B1", "height": 46, "padding": [0, 22], "fill": c_cyan, "cornerRadius": 8, "alignItems": "center", "justifyContent": "center", "children": [
                                { "type": "text", "id": "p2-b1t", "name": "T", "content": "Solicitar Estudio de Cámaras", "fontSize": 13, "fontWeight": "700", "fill": "#070A11" }
                            ]}
                        ]
                    }
                ]
            },
            # Feature Grid 6 items
            {
                "type": "frame", "id": "p2-grid-sec", "name": "6 Features", "width": "fill_container", "fill": c_bg_dark, "layout": "vertical", "padding": [64, 48], "gap": 32, "children": [
                    { "type": "text", "id": "p2-ghdr", "name": "Hdr", "content": "Qué Incluye una Instalación Profesional de CCTV", "fontSize": 28, "fontWeight": "800", "fill": "#FFFFFF" },
                    { "type": "frame", "id": "p2-r1", "name": "R1", "layout": "horizontal", "gap": 20, "children": [
                        { "type": "frame", "id": "p2-c1", "name": "F1", "width": 433, "height": 180, "fill": c_card_bg, "stroke": c_border_light, "strokeWidth": 1, "cornerRadius": 10, "padding": [20, 20], "layout": "vertical", "gap": 8, "children": [
                            { "type": "text", "id": "p2c1-t", "name": "T", "content": "Cámaras 4K Ultra Alta Resolución", "fontSize": 16, "fontWeight": "700", "fill": "#FFFFFF" },
                            { "type": "text", "id": "p2c1-d", "name": "D", "content": "Óptica y ubicación elegidas milimétricamente para que la imagen sirva legalmente como prueba pericial.", "fontSize": 13, "fill": "#94A3B8", "lineHeight": 1.5 }
                        ]},
                        { "type": "frame", "id": "p2-c2", "name": "F2", "width": 433, "height": 180, "fill": c_card_bg, "stroke": c_border_light, "strokeWidth": 1, "cornerRadius": 10, "padding": [20, 20], "layout": "vertical", "gap": 8, "children": [
                            { "type": "text", "id": "p2c2-t", "name": "T", "content": "Visión Nocturna UltraLowLight", "fontSize": 16, "fontWeight": "700", "fill": "#FFFFFF" },
                            { "type": "text", "id": "p2c2-d", "name": "D", "content": "Equipos preparados para oscuridad total, contraluces solares intensos y el clima del sureste.", "fontSize": 13, "fill": "#94A3B8", "lineHeight": 1.5 }
                        ]},
                        { "type": "frame", "id": "p2-c3", "name": "F3", "width": 433, "height": 180, "fill": c_card_bg, "stroke": c_border_light, "strokeWidth": 1, "cornerRadius": 10, "padding": [20, 20], "layout": "vertical", "gap": 8, "children": [
                            { "type": "text", "id": "p2c3-t", "name": "T", "content": "Búsqueda Inteligente de Vídeo IA", "fontSize": 16, "fontWeight": "700", "fill": "#FFFFFF" },
                            { "type": "text", "id": "p2c3-d", "name": "D", "content": "Localiza en segundos un evento por zona, cruce de línea o matrícula sin revisar horas de grabación.", "fontSize": 13, "fill": "#94A3B8", "lineHeight": 1.5 }
                        ]}
                    ]},
                    { "type": "frame", "id": "p2-r2", "name": "R2", "layout": "horizontal", "gap": 20, "children": [
                        { "type": "frame", "id": "p2-c4", "name": "F4", "width": 433, "height": 180, "fill": c_card_bg, "stroke": c_border_light, "strokeWidth": 1, "cornerRadius": 10, "padding": [20, 20], "layout": "vertical", "gap": 8, "children": [
                            { "type": "text", "id": "p2c4-t", "name": "T", "content": "Grabación y Retención NVR Cifrada", "fontSize": 16, "fontWeight": "700", "fill": "#FFFFFF" },
                            { "type": "text", "id": "p2c4-d", "name": "D", "content": "Almacenamiento dimensionado al plazo de conservación de 30 días exigido por ley con discos de grado videovigilancia.", "fontSize": 13, "fill": "#94A3B8", "lineHeight": 1.5 }
                        ]},
                        { "type": "frame", "id": "p2-c5", "name": "F5", "width": 433, "height": 180, "fill": c_card_bg, "stroke": c_border_light, "strokeWidth": 1, "cornerRadius": 10, "padding": [20, 20], "layout": "vertical", "gap": 8, "children": [
                            { "type": "text", "id": "p2c5-t", "name": "T", "content": "Acceso Remoto Seguro Multiplataforma", "fontSize": 16, "fontWeight": "700", "fill": "#FFFFFF" },
                            { "type": "text", "id": "p2c5-d", "name": "D", "content": "Visualización cifrada punto a punto desde móvil o PC con permisos por usuario y doble factor.", "fontSize": 13, "fill": "#94A3B8", "lineHeight": 1.5 }
                        ]},
                        { "type": "frame", "id": "p2-c6", "name": "F6", "width": 433, "height": 180, "fill": c_card_bg, "stroke": c_border_light, "strokeWidth": 1, "cornerRadius": 10, "padding": [20, 20], "layout": "vertical", "gap": 8, "children": [
                            { "type": "text", "id": "p2c6-t", "name": "T", "content": "Cumplimiento Estricto del RGPD", "fontSize": 16, "fontWeight": "700", "fill": "#FFFFFF" },
                            { "type": "text", "id": "p2c6-d", "name": "D", "content": "Cartelería homologada, delimitación de zonas públicas y registro de actividades de tratamiento legal.", "fontSize": 13, "fill": "#94A3B8", "lineHeight": 1.5 }
                        ]}
                    ]}
                ]
            },
            make_footer("p2")
        ]
    }

    # =========================================================================
    # 03. SCREEN: SEGURIDAD EMPRESAS (1440 x 3000)
    # =========================================================================
    p3_empresas = {
        "type": "frame",
        "id": "screen-03-empresas",
        "name": "🏭 03. Seguridad para Empresas & Grado 3 (1440px)",
        "x": 3200,
        "y": 0,
        "width": 1440,
        "height": 3000,
        "fill": c_bg_dark,
        "layout": "vertical",
        "clip": True,
        "children": [
            make_header("p3", "Empresas"),
            {
                "type": "frame", "id": "p3-hero", "name": "Hero Empresas", "width": "fill_container", "height": 480, "fill": c_card_bg, "layout": "vertical", "padding": [64, 48], "justifyContent": "center", "gap": 18, "children": [
                    { "type": "text", "id": "p3-eye", "name": "Eye", "content": "PROTECCIÓN CORPORATIVA & INDUSTRIAL", "fontSize": 11, "fontWeight": "800", "fill": c_cyan, "letterSpacing": 1 },
                    { "type": "text", "id": "p3-h1", "name": "H1", "content": "Seguridad Integral para Naves, Comercios y Oficinas", "fontSize": 40, "fontWeight": "800", "fill": "#FFFFFF" },
                    { "type": "text", "id": "p3-desc", "name": "D", "content": "Un solo proveedor para proyectar, instalar y mantener toda la seguridad de tu empresa. Alarmas Grado 3, PCI Incendios, CCTV y Control de Accesos con conexión CRA.", "fontSize": 16, "fill": "#94A3B8", "lineHeight": 1.6, "textGrowth": "fixed-width", "width": 800 }
                ]
            },
            make_footer("p3")
        ]
    }

    # =========================================================================
    # 04. SCREEN: HOGAR & RESIDENCIAL (1440 x 2800)
    # =========================================================================
    p4_hogar = {
        "type": "frame",
        "id": "screen-04-hogar",
        "name": "🏡 04. Hogar & Residencial Sin Permanencias (1440px)",
        "x": 4800,
        "y": 0,
        "width": 1440,
        "height": 2800,
        "fill": c_bg_dark,
        "layout": "vertical",
        "clip": True,
        "children": [
            make_header("p4", "Hogar"),
            {
                "type": "frame", "id": "p4-hero", "name": "Hero Hogar", "width": "fill_container", "height": 480, "fill": c_card_bg, "layout": "vertical", "padding": [64, 48], "justifyContent": "center", "gap": 18, "children": [
                    { "type": "text", "id": "p4-eye", "name": "Eye", "content": "PROTECCIÓN RESIDENCIAL HONESTA", "fontSize": 11, "fontWeight": "800", "fill": c_emerald, "letterSpacing": 1 },
                    { "type": "text", "id": "p4-h1", "name": "H1", "content": "Alarmas para Casa Sin Cuotas Trampa ni Permanencias", "fontSize": 40, "fontWeight": "800", "fill": "#FFFFFF" },
                    { "type": "text", "id": "p4-desc", "name": "D", "content": "Eres dueño de tus equipos. Seguridad Grado 2 con verificación por vídeo, control total desde la app móvil y asistencia de guardia 24 horas.", "fontSize": 16, "fill": "#94A3B8", "lineHeight": 1.6, "textGrowth": "fixed-width", "width": 800 }
                ]
            },
            make_footer("p4")
        ]
    }

    # =========================================================================
    # 05. SCREEN: INSTITUCIONES & ORGANISMOS PÚBLICOS (1440 x 2800)
    # =========================================================================
    p5_inst = {
        "type": "frame",
        "id": "screen-05-instituciones",
        "name": "🏛️ 05. Instituciones & Organismos Públicos (1440px)",
        "x": 6400,
        "y": 0,
        "width": 1440,
        "height": 2800,
        "fill": c_bg_dark,
        "layout": "vertical",
        "clip": True,
        "children": [
            make_header("p5", "Instituciones"),
            {
                "type": "frame", "id": "p5-hero", "name": "Hero Inst", "width": "fill_container", "height": 480, "fill": c_card_bg, "layout": "vertical", "padding": [64, 48], "justifyContent": "center", "gap": 18, "children": [
                    { "type": "text", "id": "p5-eye", "name": "Eye", "content": "SECTOR PÚBLICO & LICITACIONES", "fontSize": 11, "fontWeight": "800", "fill": c_amber, "letterSpacing": 1 },
                    { "type": "text", "id": "p5-h1", "name": "H1", "content": "Seguridad Homologada para Organismos Públicos", "fontSize": 40, "fontWeight": "800", "fill": "#FFFFFF" },
                    { "type": "text", "id": "p5-desc", "name": "D", "content": "Soluciones de seguridad para ayuntamientos, centros educativos, juzgados y dependencias oficiales conforme al Esquema Nacional de Seguridad (ENS) y Ley de Seguridad Privada.", "fontSize": 16, "fill": "#94A3B8", "lineHeight": 1.6, "textGrowth": "fixed-width", "width": 800 }
                ]
            },
            make_footer("p5")
        ]
    }

    # =========================================================================
    # 06. SCREEN: SOC DASHBOARD CONSOLE (1440 x 1024)
    # =========================================================================
    p6_soc = {
        "type": "frame",
        "id": "screen-06-soc-console",
        "name": "🛰️ 06. Consola de Control SOC & CRA 24/7 (1440 x 1024)",
        "x": 0,
        "y": 5000,
        "width": 1440,
        "height": 1024,
        "fill": "#030712",
        "layout": "horizontal",
        "clip": True,
        "children": [
            # Left Sidebar
            {
                "type": "frame", "id": "p6-sb", "name": "Sidebar", "width": 260, "height": "fill_container", "fill": c_card_bg, "stroke": c_border_light, "strokeWidth": { "right": 1 }, "layout": "vertical", "padding": [24, 16], "justifyContent": "space_between", "children": [
                    { "type": "frame", "id": "p6-sb-t", "name": "Top", "layout": "vertical", "gap": 24, "children": [
                        { "type": "text", "id": "p6-bname", "name": "B", "content": "SOC CONTROL 61", "fontSize": 16, "fontWeight": "800", "fill": "#FFFFFF", "letterSpacing": 1 },
                        { "type": "text", "id": "p6-m1", "name": "M1", "content": "● Matriz de Cámaras CCTV", "fontSize": 13, "fontWeight": "700", "fill": c_cyan_light },
                        { "type": "text", "id": "p6-m2", "name": "M2", "content": "Historial Alarmas CRA", "fontSize": 13, "fill": "#94A3B8" },
                        { "type": "text", "id": "p6-m3", "name": "M3", "content": "Control de Accesos LPR", "fontSize": 13, "fill": "#94A3B8" },
                        { "type": "text", "id": "p6-m4", "name": "M4", "content": "Radar Perimetral 3D", "fontSize": 13, "fill": "#94A3B8" }
                    ]},
                    { "type": "text", "id": "p6-op", "name": "Op", "content": "Operador: Toni García #04\nLicencia DGP Activa", "fontSize": 11, "fill": "#64748B" }
                ]
            },
            # Main Area
            {
                "type": "frame", "id": "p6-main", "name": "Main", "width": 1180, "height": "fill_container", "layout": "vertical", "children": [
                    { "type": "frame", "id": "p6-thdr", "name": "Hdr", "width": "fill_container", "height": 56, "fill": c_card_bg, "stroke": c_border_light, "strokeWidth": { "bottom": 1 }, "layout": "horizontal", "padding": [0, 24], "alignItems": "center", "justifyContent": "space_between", "children": [
                        { "type": "text", "id": "p6-htxt", "name": "T", "content": "CENTRAL RECEPTORA OPERATIVA · 2.500+ RECINTOS CONECTADOS", "fontSize": 12, "fontWeight": "bold", "fill": "#FFFFFF" },
                        { "type": "text", "id": "p6-hclk", "name": "C", "content": "UTC 11:45:00 · AES-256", "fontSize": 12, "fontWeight": "bold", "fill": c_cyan }
                    ]},
                    { "type": "frame", "id": "p6-cgrid", "name": "Grid", "width": "fill_container", "height": 968, "padding": [16, 16], "layout": "horizontal", "gap": 16, "children": [
                        { "type": "frame", "id": "p6-cm1", "name": "CAM 1", "width": 560, "height": 450, "fill": c_card_inner, "stroke": c_red, "strokeWidth": 2, "cornerRadius": 8, "padding": [16, 16], "layout": "vertical", "justifyContent": "space_between", "children": [
                            { "type": "text", "id": "p6-c1t", "name": "T", "content": "CAM-01 · Perímetro Norte (Intrusión Detectada)", "fontSize": 14, "fontWeight": "bold", "fill": "#FFFFFF" },
                            { "type": "text", "id": "p6-c1st", "name": "S", "content": "⚠️ INTRUSIÓN 99.4% · AVISO POLICÍA ENVIADO", "fontSize": 12, "fontWeight": "bold", "fill": c_red }
                        ]},
                        { "type": "frame", "id": "p6-cm2", "name": "CAM 2", "width": 560, "height": 450, "fill": c_card_inner, "stroke": c_emerald, "strokeWidth": 1.5, "cornerRadius": 8, "padding": [16, 16], "layout": "vertical", "justifyContent": "space_between", "children": [
                            { "type": "text", "id": "p6-c2t", "name": "T", "content": "CAM-02 · LPR Acceso Muelle (4821-LMR)", "fontSize": 14, "fontWeight": "bold", "fill": "#FFFFFF" },
                            { "type": "text", "id": "p6-c2st", "name": "S", "content": "● AUTORIZADO · BARRERA ACCIONADA", "fontSize": 12, "fontWeight": "bold", "fill": c_emerald }
                        ]}
                    ]}
                ]
            }
        ]
    }

    # =========================================================================
    # 07. SCREEN: MANTENIMIENTO & AVERÍAS 24H (1440 x 2600)
    # =========================================================================
    p7_mant = {
        "type": "frame",
        "id": "screen-07-mantenimiento",
        "name": "🔧 07. Mantenimiento Preventivo & Averías 24h (1440px)",
        "x": 1600,
        "y": 5000,
        "width": 1440,
        "height": 2600,
        "fill": c_bg_dark,
        "layout": "vertical",
        "clip": True,
        "children": [
            make_header("p7", "Mantenimiento"),
            {
                "type": "frame", "id": "p7-hero", "name": "Hero Mant", "width": "fill_container", "height": 440, "fill": c_card_bg, "layout": "vertical", "padding": [64, 48], "justifyContent": "center", "gap": 16, "children": [
                    { "type": "text", "id": "p7-eye", "name": "Eye", "content": "SERVICIO TÉCNICO & ASISTENCIA URGENTE", "fontSize": 11, "fontWeight": "800", "fill": c_cyan, "letterSpacing": 1 },
                    { "type": "text", "id": "p7-h1", "name": "H1", "content": "Mantenimiento y Averías 24 Horas en Murcia", "fontSize": 38, "fontWeight": "800", "fill": "#FFFFFF" },
                    { "type": "text", "id": "p7-desc", "name": "D", "content": "Revisiones preventivas obligatorias por ley y asistencia de urgencia con técnicos cualificados en plantilla propia.", "fontSize": 15, "fill": "#94A3B8" }
                ]
            },
            make_footer("p7")
        ]
    }

    # =========================================================================
    # 08. SCREEN: ACREDITACIONES & NORMATIVA (1440 x 2600)
    # =========================================================================
    p8_acred = {
        "type": "frame",
        "id": "screen-08-acreditaciones",
        "name": "📜 08. Acreditaciones, Normativa & DGP 2341 (1440px)",
        "x": 3200,
        "y": 5000,
        "width": 1440,
        "height": 2600,
        "fill": c_bg_dark,
        "layout": "vertical",
        "clip": True,
        "children": [
            make_header("p8", "Acreditaciones"),
            {
                "type": "frame", "id": "p8-hero", "name": "Hero Acred", "width": "fill_container", "height": 440, "fill": c_card_bg, "layout": "vertical", "padding": [64, 48], "justifyContent": "center", "gap": 16, "children": [
                    { "type": "text", "id": "p8-eye", "name": "Eye", "content": "HOMOLOGACIÓN NACIONAL & CALIDAD", "fontSize": 11, "fontWeight": "800", "fill": c_emerald, "letterSpacing": 1 },
                    { "type": "text", "id": "p8-h1", "name": "H1", "content": "Acreditaciones y Homologaciones Oficiales", "fontSize": 38, "fontWeight": "800", "fill": "#FFFFFF" },
                    { "type": "text", "id": "p8-desc", "name": "D", "content": "Inscritos en el Registro de Empresas de Seguridad de la DGP con el Nº 2341. Certificados ISO 9001, ISO 14001 e ISO 45001 emitidos por RINA.", "fontSize": 15, "fill": "#94A3B8" }
                ]
            },
            make_footer("p8")
        ]
    }

    # =========================================================================
    # 09. SCREEN: NOSOTROS & EQUIPO (1440 x 2800)
    # =========================================================================
    p9_nosotros = {
        "type": "frame",
        "id": "screen-09-nosotros",
        "name": "👥 09. Nosotros & Trayectoria 20+ Años (1440px)",
        "x": 4800,
        "y": 5000,
        "width": 1440,
        "height": 2800,
        "fill": c_bg_dark,
        "layout": "vertical",
        "clip": True,
        "children": [
            make_header("p9", "Nosotros"),
            {
                "type": "frame", "id": "p9-hero", "name": "Hero Nosotros", "width": "fill_container", "height": 440, "fill": c_card_bg, "layout": "vertical", "padding": [64, 48], "justifyContent": "center", "gap": 16, "children": [
                    { "type": "text", "id": "p9-eye", "name": "Eye", "content": "TRAYECTORIA & EQUIPO", "fontSize": 11, "fontWeight": "800", "fill": c_cyan, "letterSpacing": 1 },
                    { "type": "text", "id": "p9-h1", "name": "H1", "content": "Más de 20 Años Protegiendo lo que Importa", "fontSize": 38, "fontWeight": "800", "fill": "#FFFFFF" },
                    { "type": "text", "id": "p9-desc", "name": "D", "content": "Desarrollos y Sistemas Inteligentes S.L. nació en Murcia para ofrecer ingeniería de seguridad seria, sin subcontratas y con atención técnica real.", "fontSize": 15, "fill": "#94A3B8" }
                ]
            },
            make_footer("p9")
        ]
    }

    # =========================================================================
    # 10. SCREEN: CONTACTO & SEDE (1440 x 2600)
    # =========================================================================
    p10_contacto = {
        "type": "frame",
        "id": "screen-10-contacto",
        "name": "📍 10. Contacto, Sede Central & Valoración (1440px)",
        "x": 6400,
        "y": 5000,
        "width": 1440,
        "height": 2600,
        "fill": c_bg_dark,
        "layout": "vertical",
        "clip": True,
        "children": [
            make_header("p10", "Contacto"),
            {
                "type": "frame", "id": "p10-hero", "name": "Hero Contacto", "width": "fill_container", "height": 440, "fill": c_card_bg, "layout": "vertical", "padding": [64, 48], "justifyContent": "center", "gap": 16, "children": [
                    { "type": "text", "id": "p10-eye", "name": "Eye", "content": "SEDE CENTRAL EN MOLINA DE SEGURA", "fontSize": 11, "fontWeight": "800", "fill": c_cyan, "letterSpacing": 1 },
                    { "type": "text", "id": "p10-h1", "name": "H1", "content": "Contacta con Nuestro Equipo Técnico", "fontSize": 38, "fontWeight": "800", "fill": "#FFFFFF" },
                    { "type": "text", "id": "p10-desc", "name": "D", "content": "Pol. Ind. La Polvorista, C/ Caravaca de la Cruz 13, Nave C-7, Molina de Segura (Murcia). Tel: 968 622 984.", "fontSize": 15, "fill": "#94A3B8" }
                ]
            },
            make_footer("p10")
        ]
    }

    # =========================================================================
    # 11. SCREEN: MOBILE VIEW (390 x 2600)
    # =========================================================================
    p11_mobile = {
        "type": "frame",
        "id": "screen-11-mobile",
        "name": "📱 11. App Móvil / Vista Smartphone (390px)",
        "x": 8000,
        "y": 0,
        "width": 390,
        "height": 2600,
        "fill": c_bg_dark,
        "layout": "vertical",
        "clip": True,
        "children": [
            {
                "type": "frame", "id": "m-hdr", "name": "Hdr", "width": "fill_container", "height": 60, "fill": c_card_bg, "stroke": c_border_light, "strokeWidth": { "bottom": 1 }, "layout": "horizontal", "padding": [0, 16], "alignItems": "center", "justifyContent": "space_between", "children": [
                    { "type": "text", "id": "m-b", "name": "B", "content": "CONTROL 61", "fontSize": 15, "fontWeight": "800", "fill": "#FFFFFF" },
                    { "type": "text", "id": "m-p", "name": "P", "content": "📞 968 622 984", "fontSize": 12, "fontWeight": "bold", "fill": c_red }
                ]
            },
            {
                "type": "frame", "id": "m-body", "name": "Body", "width": "fill_container", "padding": [24, 16], "layout": "vertical", "gap": 16, "children": [
                    { "type": "text", "id": "m-h1", "name": "H1", "content": "Seguridad Avanzada, CCTV IA y Alarmas Grado 3", "fontSize": 24, "fontWeight": "800", "fill": "#FFFFFF" },
                    { "type": "text", "id": "m-sub", "name": "Sub", "content": "Ingeniería de seguridad homologada en Murcia. Conexión directa a CRA en <15s.", "fontSize": 13, "fill": "#94A3B8" },
                    {
                        "type": "frame", "id": "m-btn", "name": "Btn", "height": 46, "fill": c_cyan, "cornerRadius": 8, "alignItems": "center", "justifyContent": "center", "children": [
                            { "type": "text", "id": "m-btxt", "name": "T", "content": "Solicitar Valoración Gratuita", "fontSize": 13, "fontWeight": "800", "fill": "#070A11" }
                        ]
                    }
                ]
            }
        ]
    }

    all_screens = [
        p1_landing,
        p2_cctv,
        p3_empresas,
        p4_hogar,
        p5_inst,
        p6_soc,
        p7_mant,
        p8_acred,
        p9_nosotros,
        p10_contacto,
        p11_mobile
    ]

    return {
        "version": "2.19",
        "children": all_screens
    }

doc = build_all_screens()
with open("/Users/toni/Proyectos/Control61-Web/control61_modern_ui.pen", "w") as f:
    json.dump(doc, f, indent=2)

print("Successfully written 11 complete screens to control61_modern_ui.pen!")
