import json
import subprocess

def build_screens():
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

    # 1. Home
    p1 = {
        "type": "frame", "id": "screen-01-home", "name": "🏠 01. Inicio / Landing Principal (1440px)", "x": 0, "y": 0, "width": 1440, "height": 3800, "fill": c_bg_dark, "layout": "vertical", "clip": True,
        "children": [
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
            {
                "type": "frame", "id": "p1-hero", "name": "Hero", "width": "fill_container", "height": 620, "fill": c_bg_dark, "layout": "horizontal", "padding": [48, 48], "gap": 40, "alignItems": "center", "justifyContent": "space_between", "children": [
                    {
                        "type": "frame", "id": "p1-hl", "name": "Left", "width": 640, "layout": "vertical", "gap": 20, "children": [
                            { "type": "text", "id": "p1-h1", "name": "H1", "content": "Sistemas de Seguridad Avanzada, CCTV con IA y Alarmas Grado 3", "fontSize": 42, "fontWeight": "800", "fill": "#FFFFFF", "lineHeight": 1.15, "textGrowth": "fixed-width", "width": 640 },
                            { "type": "text", "id": "p1-hd", "name": "D", "content": "Ingeniería e instalación de alarmas de Grado 2 y 3, videovigilancia de alta precisión y control de accesos para empresas e instituciones en Murcia.", "fontSize": 15, "fill": "#94A3B8", "lineHeight": 1.6, "textGrowth": "fixed-width", "width": 620 },
                            {
                                "type": "frame", "id": "p1-hb", "name": "Btns", "layout": "horizontal", "gap": 16, "children": [
                                    { "type": "frame", "id": "p1-bm", "name": "CTA", "height": 48, "padding": [0, 24], "fill": c_cyan, "cornerRadius": 8, "alignItems": "center", "justifyContent": "center", "children": [
                                        { "type": "text", "id": "p1-bmt", "name": "T", "content": "Solicitar Valoración Gratuita", "fontSize": 14, "fontWeight": "700", "fill": "#070A11" }
                                    ]}
                                ]
                            }
                        ]
                    }
                ]
            },
            make_footer("p1")
        ]
    }

    # 2. CCTV
    p2 = {
        "type": "frame", "id": "screen-02-cctv", "name": "📹 02. CCTV & Visión Artificial IA (1440px)", "x": 1600, "y": 0, "width": 1440, "height": 3000, "fill": c_bg_dark, "layout": "vertical", "clip": True,
        "children": [
            make_header("p2", "CCTV & IA"),
            {
                "type": "frame", "id": "p2-hero", "name": "Hero CCTV", "width": "fill_container", "height": 420, "fill": c_card_bg, "layout": "vertical", "padding": [48, 48], "justifyContent": "center", "gap": 16, "children": [
                    { "type": "text", "id": "p2-eye", "name": "Eye", "content": "VIDEOVIGILANCIA DE ALTA PRECISIÓN", "fontSize": 11, "fontWeight": "800", "fill": c_cyan, "letterSpacing": 1 },
                    { "type": "text", "id": "p2-h1", "name": "H1", "content": "CCTV que Sirve Cuando de Verdad Hace Falta", "fontSize": 38, "fontWeight": "800", "fill": "#FFFFFF" },
                    { "type": "text", "id": "p2-desc", "name": "D", "content": "Cámaras 4K con analítica IA, visión nocturna UltraLowLight y búsqueda instantánea conforme al RGPD.", "fontSize": 15, "fill": "#94A3B8", "lineHeight": 1.6, "textGrowth": "fixed-width", "width": 780 }
                ]
            },
            make_footer("p2")
        ]
    }

    # 3. Empresas
    p3 = {
        "type": "frame", "id": "screen-03-empresas", "name": "🏭 03. Seguridad para Empresas & Grado 3 (1440px)", "x": 3200, "y": 0, "width": 1440, "height": 3000, "fill": c_bg_dark, "layout": "vertical", "clip": True,
        "children": [
            make_header("p3", "Empresas"),
            {
                "type": "frame", "id": "p3-hero", "name": "Hero Empresas", "width": "fill_container", "height": 420, "fill": c_card_bg, "layout": "vertical", "padding": [48, 48], "justifyContent": "center", "gap": 16, "children": [
                    { "type": "text", "id": "p3-eye", "name": "Eye", "content": "PROTECCIÓN INDUSTRIAL & CORPORATIVA", "fontSize": 11, "fontWeight": "800", "fill": c_cyan, "letterSpacing": 1 },
                    { "type": "text", "id": "p3-h1", "name": "H1", "content": "Seguridad Integral para Naves, Comercios y Oficinas", "fontSize": 38, "fontWeight": "800", "fill": "#FFFFFF" },
                    { "type": "text", "id": "p3-desc", "name": "D", "content": "Alarmas Grado 3 obligatorias por ley, PCI Incendios y Control de Accesos con conexión CRA.", "fontSize": 15, "fill": "#94A3B8", "lineHeight": 1.6, "textGrowth": "fixed-width", "width": 780 }
                ]
            },
            make_footer("p3")
        ]
    }

    # 4. Hogar
    p4 = {
        "type": "frame", "id": "screen-04-hogar", "name": "🏡 04. Hogar & Residencial Sin Permanencias (1440px)", "x": 4800, "y": 0, "width": 1440, "height": 2800, "fill": c_bg_dark, "layout": "vertical", "clip": True,
        "children": [
            make_header("p4", "Hogar"),
            {
                "type": "frame", "id": "p4-hero", "name": "Hero Hogar", "width": "fill_container", "height": 420, "fill": c_card_bg, "layout": "vertical", "padding": [48, 48], "justifyContent": "center", "gap": 16, "children": [
                    { "type": "text", "id": "p4-eye", "name": "Eye", "content": "PROTECCIÓN RESIDENCIAL HONESTA", "fontSize": 11, "fontWeight": "800", "fill": c_emerald, "letterSpacing": 1 },
                    { "type": "text", "id": "p4-h1", "name": "H1", "content": "Alarmas para Casa Sin Cuotas Trampa ni Permanencias", "fontSize": 38, "fontWeight": "800", "fill": "#FFFFFF" },
                    { "type": "text", "id": "p4-desc", "name": "D", "content": "Seguridad Grado 2 con verificación por vídeo, control total desde la app móvil y servicio de guardia 24h.", "fontSize": 15, "fill": "#94A3B8", "lineHeight": 1.6, "textGrowth": "fixed-width", "width": 780 }
                ]
            },
            make_footer("p4")
        ]
    }

    # 5. Instituciones
    p5 = {
        "type": "frame", "id": "screen-05-instituciones", "name": "🏛️ 05. Instituciones & Organismos Públicos (1440px)", "x": 6400, "y": 0, "width": 1440, "height": 2800, "fill": c_bg_dark, "layout": "vertical", "clip": True,
        "children": [
            make_header("p5", "Instituciones"),
            {
                "type": "frame", "id": "p5-hero", "name": "Hero Inst", "width": "fill_container", "height": 420, "fill": c_card_bg, "layout": "vertical", "padding": [48, 48], "justifyContent": "center", "gap": 16, "children": [
                    { "type": "text", "id": "p5-eye", "name": "Eye", "content": "SECTOR PÚBLICO & LICITACIONES", "fontSize": 11, "fontWeight": "800", "fill": c_amber, "letterSpacing": 1 },
                    { "type": "text", "id": "p5-h1", "name": "H1", "content": "Seguridad Homologada para Organismos Públicos", "fontSize": 38, "fontWeight": "800", "fill": "#FFFFFF" },
                    { "type": "text", "id": "p5-desc", "name": "D", "content": "Sistemas conformes al Esquema Nacional de Seguridad (ENS) y Ley de Seguridad Privada.", "fontSize": 15, "fill": "#94A3B8", "lineHeight": 1.6, "textGrowth": "fixed-width", "width": 780 }
                ]
            },
            make_footer("p5")
        ]
    }

    # 6. SOC Dashboard
    p6 = {
        "type": "frame", "id": "screen-06-soc-console", "name": "🛰️ 06. Consola de Control SOC & CRA 24/7 (1440 x 1024)", "x": 0, "y": 4000, "width": 1440, "height": 1024, "fill": "#030712", "layout": "horizontal", "clip": True,
        "children": [
            {
                "type": "frame", "id": "p6-sb", "name": "Sidebar", "width": 260, "height": "fill_container", "fill": c_card_bg, "stroke": c_border_light, "strokeWidth": { "right": 1 }, "layout": "vertical", "padding": [24, 16], "justifyContent": "space_between", "children": [
                    { "type": "frame", "id": "p6-sbt", "name": "Top", "layout": "vertical", "gap": 20, "children": [
                        { "type": "text", "id": "p6-bn", "name": "B", "content": "SOC CONTROL 61", "fontSize": 16, "fontWeight": "800", "fill": "#FFFFFF", "letterSpacing": 1 },
                        { "type": "text", "id": "p6-m1", "name": "M1", "content": "● Matriz de Cámaras CCTV", "fontSize": 13, "fontWeight": "700", "fill": c_cyan_light },
                        { "type": "text", "id": "p6-m2", "name": "M2", "content": "Historial Alarmas CRA", "fontSize": 13, "fill": "#94A3B8" },
                        { "type": "text", "id": "p6-m3", "name": "M3", "content": "Control de Accesos LPR", "fontSize": 13, "fill": "#94A3B8" }
                    ]},
                    { "type": "text", "id": "p6-op", "name": "Op", "content": "Operador: Toni García #04\nLicencia DGP Activa", "fontSize": 11, "fill": "#64748B" }
                ]
            },
            {
                "type": "frame", "id": "p6-main", "name": "Main Area", "width": 1180, "height": "fill_container", "layout": "vertical", "children": [
                    { "type": "frame", "id": "p6-hdr", "name": "Header", "width": "fill_container", "height": 56, "fill": c_card_bg, "stroke": c_border_light, "strokeWidth": { "bottom": 1 }, "layout": "horizontal", "padding": [0, 24], "alignItems": "center", "justifyContent": "space_between", "children": [
                        { "type": "text", "id": "p6-stt", "name": "T", "content": "CENTRAL RECEPTORA OPERATIVA · 2.500+ RECINTOS CONECTADOS", "fontSize": 12, "fontWeight": "bold", "fill": "#FFFFFF" },
                        { "type": "text", "id": "p6-clk", "name": "C", "content": "UTC 11:45:00 · AES-256", "fontSize": 12, "fontWeight": "bold", "fill": c_cyan }
                    ]}
                ]
            }
        ]
    }

    # 7. Mantenimiento
    p7 = {
        "type": "frame", "id": "screen-07-mantenimiento", "name": "🔧 07. Mantenimiento & Averías 24h (1440px)", "x": 1600, "y": 4000, "width": 1440, "height": 2600, "fill": c_bg_dark, "layout": "vertical", "clip": True,
        "children": [
            make_header("p7", "Mantenimiento"),
            {
                "type": "frame", "id": "p7-hero", "name": "Hero Mant", "width": "fill_container", "height": 420, "fill": c_card_bg, "layout": "vertical", "padding": [48, 48], "justifyContent": "center", "gap": 16, "children": [
                    { "type": "text", "id": "p7-eye", "name": "Eye", "content": "SERVICIO TÉCNICO & AVERÍAS", "fontSize": 11, "fontWeight": "800", "fill": c_cyan, "letterSpacing": 1 },
                    { "type": "text", "id": "p7-h1", "name": "H1", "content": "Mantenimiento Preventivo y Averías 24 Horas", "fontSize": 38, "fontWeight": "800", "fill": "#FFFFFF" },
                    { "type": "text", "id": "p7-desc", "name": "D", "content": "Revisiones obligatorias y asistencia técnica in situ cuando el sistema falla.", "fontSize": 15, "fill": "#94A3B8" }
                ]
            },
            make_footer("p7")
        ]
    }

    # 8. Acreditaciones
    p8 = {
        "type": "frame", "id": "screen-08-acreditaciones", "name": "📜 08. Acreditaciones & DGP 2341 (1440px)", "x": 3200, "y": 4000, "width": 1440, "height": 2600, "fill": c_bg_dark, "layout": "vertical", "clip": True,
        "children": [
            make_header("p8", "Acreditaciones"),
            {
                "type": "frame", "id": "p8-hero", "name": "Hero Acred", "width": "fill_container", "height": 420, "fill": c_card_bg, "layout": "vertical", "padding": [48, 48], "justifyContent": "center", "gap": 16, "children": [
                    { "type": "text", "id": "p8-eye", "name": "Eye", "content": "HOMOLOGACIÓN NACIONAL", "fontSize": 11, "fontWeight": "800", "fill": c_emerald, "letterSpacing": 1 },
                    { "type": "text", "id": "p8-h1", "name": "H1", "content": "Acreditaciones y Homologaciones Oficiales", "fontSize": 38, "fontWeight": "800", "fill": "#FFFFFF" },
                    { "type": "text", "id": "p8-desc", "name": "D", "content": "Registro DGP Nº 2341. Certificados ISO 9001 / 14001 / 45001 por RINA y Registro REA.", "fontSize": 15, "fill": "#94A3B8" }
                ]
            },
            make_footer("p8")
        ]
    }

    # 9. Nosotros
    p9 = {
        "type": "frame", "id": "screen-09-nosotros", "name": "👥 09. Nosotros & Trayectoria 20+ Años (1440px)", "x": 4800, "y": 4000, "width": 1440, "height": 2800, "fill": c_bg_dark, "layout": "vertical", "clip": True,
        "children": [
            make_header("p9", "Nosotros"),
            {
                "type": "frame", "id": "p9-hero", "name": "Hero Nosotros", "width": "fill_container", "height": 420, "fill": c_card_bg, "layout": "vertical", "padding": [48, 48], "justifyContent": "center", "gap": 16, "children": [
                    { "type": "text", "id": "p9-eye", "name": "Eye", "content": "EQUIPO & TRAYECTORIA", "fontSize": 11, "fontWeight": "800", "fill": c_cyan, "letterSpacing": 1 },
                    { "type": "text", "id": "p9-h1", "name": "H1", "content": "Más de 20 Años Protegiendo lo que Importa", "fontSize": 38, "fontWeight": "800", "fill": "#FFFFFF" },
                    { "type": "text", "id": "p9-desc", "name": "D", "content": "Empresa fundada en Molina de Segura con ingenieros y técnicos en plantilla propia.", "fontSize": 15, "fill": "#94A3B8" }
                ]
            },
            make_footer("p9")
        ]
    }

    # 10. Contacto
    p10 = {
        "type": "frame", "id": "screen-10-contacto", "name": "📍 10. Contacto & Sede Central (1440px)", "x": 6400, "y": 4000, "width": 1440, "height": 2600, "fill": c_bg_dark, "layout": "vertical", "clip": True,
        "children": [
            make_header("p10", "Contacto"),
            {
                "type": "frame", "id": "p10-hero", "name": "Hero Contacto", "width": "fill_container", "height": 420, "fill": c_card_bg, "layout": "vertical", "padding": [48, 48], "justifyContent": "center", "gap": 16, "children": [
                    { "type": "text", "id": "p10-eye", "name": "Eye", "content": "SEDE CENTRAL EN MURCIA", "fontSize": 11, "fontWeight": "800", "fill": c_cyan, "letterSpacing": 1 },
                    { "type": "text", "id": "p10-h1", "name": "H1", "content": "Contacta con Nuestro Equipo Técnico", "fontSize": 38, "fontWeight": "800", "fill": "#FFFFFF" },
                    { "type": "text", "id": "p10-desc", "name": "D", "content": "Pol. Ind. La Polvorista, Molina de Segura (Murcia). Teléfono 24h: 968 622 984.", "fontSize": 15, "fill": "#94A3B8" }
                ]
            },
            make_footer("p10")
        ]
    }

    # 11. Mobile View
    p11 = {
        "type": "frame", "id": "screen-11-mobile", "name": "📱 11. App Móvil (390px)", "x": 8000, "y": 0, "width": 390, "height": 2400, "fill": c_bg_dark, "layout": "vertical", "clip": True,
        "children": [
            {
                "type": "frame", "id": "m-hdr", "name": "Hdr", "width": "fill_container", "height": 60, "fill": c_card_bg, "stroke": c_border_light, "strokeWidth": { "bottom": 1 }, "layout": "horizontal", "padding": [0, 16], "alignItems": "center", "justifyContent": "space_between", "children": [
                    { "type": "text", "id": "m-b", "name": "B", "content": "CONTROL 61", "fontSize": 15, "fontWeight": "800", "fill": "#FFFFFF" },
                    { "type": "text", "id": "m-p", "name": "P", "content": "📞 968 622 984", "fontSize": 12, "fontWeight": "bold", "fill": c_red }
                ]
            }
        ]
    }

    screens = [p1, p2, p3, p4, p5, p6, p7, p8, p9, p10, p11]
    return screens

all_screens = build_screens()
print(f"Generated {len(all_screens)} screen structures.")

# Write full file
doc = {
    "version": "2.19",
    "children": all_screens
}
with open("/Users/toni/Proyectos/Control61-Web/control61_modern_ui.pen", "w") as f:
    json.dump(doc, f, indent=2)

print("Saved /Users/toni/Proyectos/Control61-Web/control61_modern_ui.pen with all 11 screens!")
