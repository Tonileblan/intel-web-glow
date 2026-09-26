import json
import subprocess
import os

# =============================================================================
# COLOR PALETTES
# =============================================================================

# Option A: Signature Red (Control61.es Authentic Brand)
RED_BG = "#08090E"
RED_SURFACE = "#11121A"
RED_CARD = "#171824"
RED_CARD_ALT = "#13141F"
RED_PRIMARY = "#DC2626"
RED_ACCENT = "#EF4444"
RED_LIGHT = "#F87171"
RED_GLOW = "#7F1D1D"
RED_BORDER = "#EF44444D"
RED_BORDER_SUBTLE = "#FFFFFF12"

# Option B: Strong Cobalt Blue (Cyber SOC Edition)
BLUE_BG = "#030712"
BLUE_SURFACE = "#0B1329"
BLUE_CARD = "#0F1E3D"
BLUE_CARD_ALT = "#0A152E"
BLUE_PRIMARY = "#2563EB"
BLUE_ACCENT = "#3B82F6"
BLUE_CYAN = "#06B6D4"
BLUE_CYAN_LIGHT = "#22D3EE"
BLUE_BORDER = "#3B82F64D"
BLUE_BORDER_SUBTLE = "#FFFFFF14"

# Common Accents
EMERALD = "#10B981"
EMERALD_LIGHT = "#34D399"
AMBER = "#F59E0B"
AMBER_LIGHT = "#FCD34D"

# Image URLs
IMG_CCTV_CAMERA = "https://images.unsplash.com/photo-1557597774-9d273605dfa9?auto=format&fit=crop&w=1600&q=80"
IMG_WAREHOUSE_NIGHT = "https://images.unsplash.com/photo-1586528116311-ad8dd3c8310d?auto=format&fit=crop&w=1600&q=80"
IMG_LOGISTICS_DOCK = "https://images.unsplash.com/photo-1545324418-cc1a3fa10c00?auto=format&fit=crop&w=1600&q=80"
IMG_CONTROL_ROOM = "https://images.unsplash.com/photo-1558494949-ef010cbdcc31?auto=format&fit=crop&w=1600&q=80"
IMG_BIOMETRIC_TURNSTILE = "https://images.unsplash.com/photo-1497366216548-37526070297c?auto=format&fit=crop&w=1600&q=80"
IMG_FIRE_PROTECTION = "https://images.unsplash.com/photo-1517430816045-df4b7de01dbf?auto=format&fit=crop&w=1600&q=80"
IMG_SOLAR_FARM = "https://images.unsplash.com/photo-1509391365360-2e959784a276?auto=format&fit=crop&w=1600&q=80"
IMG_JEWELRY_VAULT = "https://images.unsplash.com/photo-1579546929518-9e396f3cc809?auto=format&fit=crop&w=1600&q=80"
IMG_SERVER_CPD = "https://images.unsplash.com/photo-1558494949-ef010cbdcc31?auto=format&fit=crop&w=1600&q=80"

def photo_fill(img_url, overlay_top="#070A1133", overlay_bot="#070A11F8"):
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

# =============================================================================
# 🔴 OPTION A: SIGNATURE RED (Control61.es Authentic Identity)
# =============================================================================
def build_option_a_red():
    nav_links = [
        ("Inicio", True),
        ("Alarmas Grado 3", False),
        ("CCTV & Visión IA", False),
        ("Control de Accesos", False),
        ("CRA 24/7", False),
        ("Incendios PCI", False),
        ("Acreditaciones", False),
        ("Nosotros", False),
        ("Contacto", False)
    ]
    
    header_links = []
    for name, is_active in nav_links:
        header_links.append({
            "type": "text",
            "id": f"red-nav-{name}",
            "name": name,
            "content": name,
            "fontSize": 13,
            "fontWeight": "700" if is_active else "500",
            "fill": RED_ACCENT if is_active else "#94A3B8"
        })
        
    return {
        "type": "frame",
        "id": "OoFpg",
        "name": "🔴 Opción A: Control 61 - Red Security Edition (Web Oficial Style)",
        "x": 0,
        "y": 0,
        "width": 1440,
        "height": 3480,
        "fill": RED_BG,
        "layout": "vertical",
        "clip": True,
        "children": [
            # 1. Top Emergency Bar Red
            {
                "type": "frame", "id": "red-top-bar", "name": "Top Emergency Bar", "width": "fill_container", "height": 42, "fill": "#170A0C", "stroke": RED_BORDER, "strokeWidth": { "bottom": 1 }, "layout": "horizontal", "padding": [0, 48], "alignItems": "center", "justifyContent": "space_between", "children": [
                    { "type": "frame", "id": "red-tb-l", "name": "L", "layout": "horizontal", "gap": 8, "alignItems": "center", "children": [
                        { "type": "ellipse", "id": "red-dot-live", "name": "Live Red Dot", "width": 8, "height": 8, "fill": RED_ACCENT },
                        { "type": "text", "id": "red-st-txt", "name": "T", "content": "CENTRAL RECEPTORA DE ALARMAS 24/7/365 · HOMOLOGADA GRADO 3 · DGP Nº 2341", "fontSize": 11, "fontWeight": "bold", "fill": "#FCA5A5" }
                    ]},
                    { "type": "frame", "id": "red-tb-r", "name": "R", "layout": "horizontal", "gap": 20, "alignItems": "center", "children": [
                        { "type": "text", "id": "red-phone-24", "name": "Phone", "content": "🚨 Centralita Urgencias 24h: 968 622 984", "fontSize": 12, "fontWeight": "bold", "fill": "#FFFFFF" },
                        { "type": "text", "id": "red-cra-portal", "name": "Portal", "content": "Acceso Clientes CRA →", "fontSize": 12, "fontWeight": "bold", "fill": RED_ACCENT }
                    ]}
                ]
            },
            # 2. Navbar Red
            {
                "type": "frame", "id": "red-navbar", "name": "Navbar Glass", "width": "fill_container", "height": 78, "fill": "#10111AEE", "stroke": RED_BORDER_SUBTLE, "strokeWidth": { "bottom": 1 }, "layout": "horizontal", "padding": [0, 48], "alignItems": "center", "justifyContent": "space_between", "children": [
                    { "type": "frame", "id": "red-brand", "name": "Brand", "layout": "horizontal", "gap": 12, "alignItems": "center", "children": [
                        { "type": "frame", "id": "red-logo-box", "name": "Shield Box", "width": 44, "height": 44, "fill": "#991B1B33", "stroke": RED_PRIMARY, "strokeWidth": 1.5, "cornerRadius": 10, "alignItems": "center", "justifyContent": "center", "children": [
                            { "type": "icon", "id": "red-sh-ico", "name": "Ico", "library": "lucide", "icon": "shield-alert", "width": 24, "height": 24, "fill": RED_ACCENT }
                        ]},
                        { "type": "frame", "id": "red-btexts", "name": "Text", "layout": "vertical", "gap": 2, "children": [
                            { "type": "text", "id": "red-bname", "name": "Name", "content": "CONTROL 61", "fontSize": 20, "fontWeight": "800", "fill": "#FFFFFF", "letterSpacing": 1.5 },
                            { "type": "text", "id": "red-bsub", "name": "Sub", "content": "SISTEMAS DE SEGURIDAD HOMOLOGADOS", "fontSize": 8, "fontWeight": "700", "fill": "#FCA5A5", "letterSpacing": 0.8 }
                        ]}
                    ]},
                    { "type": "frame", "id": "red-navlinks", "name": "Links", "layout": "horizontal", "gap": 20, "alignItems": "center", "children": header_links },
                    { "type": "frame", "id": "red-navctas", "name": "CTAs", "layout": "horizontal", "gap": 12, "alignItems": "center", "children": [
                        { "type": "frame", "id": "red-btn-ph", "name": "Phone", "height": 40, "padding": [0, 16], "fill": "#1E1A20", "stroke": RED_BORDER, "strokeWidth": 1, "cornerRadius": 8, "layout": "horizontal", "gap": 8, "alignItems": "center", "children": [
                            { "type": "icon", "id": "red-pico", "name": "P", "library": "lucide", "icon": "phone", "width": 14, "height": 14, "fill": RED_ACCENT },
                            { "type": "text", "id": "red-ptxt", "name": "T", "content": "968 622 984", "fontSize": 12, "fontWeight": "bold", "fill": "#FFFFFF" }
                        ]},
                        { "type": "frame", "id": "red-btn-cta", "name": "CTA", "height": 40, "padding": [0, 18], "fill": RED_PRIMARY, "cornerRadius": 8, "alignItems": "center", "justifyContent": "center", "children": [
                            { "type": "text", "id": "red-ctatxt", "name": "T", "content": "Solicitar Valoración", "fontSize": 13, "fontWeight": "700", "fill": "#FFFFFF" }
                        ]}
                    ]}
                ]
            },
            # 3. Hero Section Red with Night Perimeter HUD
            {
                "type": "frame", "id": "red-hero-sec", "name": "Hero Section", "width": "fill_container", "height": 680, "fill": RED_BG, "layout": "horizontal", "padding": [56, 48], "gap": 40, "alignItems": "center", "justifyContent": "space_between", "children": [
                    { "type": "frame", "id": "red-h-l", "name": "Left", "width": 630, "layout": "vertical", "gap": 22, "children": [
                        { "type": "frame", "id": "red-badge-pill", "name": "Badge", "height": 32, "padding": [0, 14], "fill": "#991B1B26", "stroke": RED_BORDER, "strokeWidth": 1, "cornerRadius": 20, "layout": "horizontal", "gap": 8, "alignItems": "center", "children": [
                            { "type": "icon", "id": "red-bico", "name": "I", "library": "lucide", "icon": "shield-check", "width": 14, "height": 14, "fill": RED_ACCENT },
                            { "type": "text", "id": "red-btxt", "name": "T", "content": "HOMOLOGACIÓN DGP Nº 2341 · CERTIFICACIÓN GRADO 3 OFICIAL", "fontSize": 10, "fontWeight": "700", "fill": RED_ACCENT }
                        ]},
                        { "type": "text", "id": "red-h1", "name": "H1", "content": "Sistemas de Seguridad Avanzada, Alarmas Grado 3 y CCTV con IA", "fontSize": 44, "fontWeight": "800", "fill": "#FFFFFF", "lineHeight": 1.15, "textGrowth": "fixed-width", "width": 630 },
                        { "type": "text", "id": "red-hdesc", "name": "Desc", "content": "Protección perimetral inteligente para industrias, naves y recintos de alto riesgo en Murcia y Levante. Conexión directa a Central Receptora homologada Grado 3 con respuesta inmediata en < 15s.", "fontSize": 15, "fill": "#94A3B8", "lineHeight": 1.6, "textGrowth": "fixed-width", "width": 610 },
                        { "type": "frame", "id": "red-h-btns", "name": "Btns", "layout": "horizontal", "gap": 16, "children": [
                            { "type": "frame", "id": "red-bm", "name": "CTA", "height": 50, "padding": [0, 24], "fill": RED_PRIMARY, "cornerRadius": 10, "layout": "horizontal", "gap": 10, "alignItems": "center", "children": [
                                { "type": "text", "id": "red-bmt", "name": "T", "content": "Diseñar Plan de Seguridad", "fontSize": 14, "fontWeight": "700", "fill": "#FFFFFF" },
                                { "type": "icon", "id": "red-bmi", "name": "I", "library": "lucide", "icon": "arrow-up-right", "width": 16, "height": 16, "fill": "#FFFFFF" }
                            ]},
                            { "type": "frame", "id": "red-bs", "name": "Phone", "height": 50, "padding": [0, 20], "fill": "#1E1A20", "stroke": RED_BORDER, "strokeWidth": 1.5, "cornerRadius": 10, "layout": "horizontal", "gap": 8, "alignItems": "center", "children": [
                                { "type": "icon", "id": "red-psi", "name": "P", "library": "lucide", "icon": "phone", "width": 15, "height": 15, "fill": RED_ACCENT },
                                { "type": "text", "id": "red-pst", "name": "T", "content": "968 622 984 · Averías 24h", "fontSize": 13, "fontWeight": "600", "fill": "#F1F5F9" }
                            ]}
                        ]},
                        { "type": "frame", "id": "red-trust-strip", "name": "Trust", "layout": "horizontal", "gap": 24, "alignItems": "center", "children": [
                            { "type": "text", "id": "red-t1", "name": "T1", "content": "✓ Sin Permanencias Ocultas", "fontSize": 12, "fontWeight": "600", "fill": EMERALD },
                            { "type": "text", "id": "red-t2", "name": "T2", "content": "✓ Equipos Propios en Propiedad", "fontSize": 12, "fontWeight": "600", "fill": EMERALD },
                            { "type": "text", "id": "red-t3", "name": "T3", "content": "✓ Verificación Policial < 15s", "fontSize": 12, "fontWeight": "600", "fill": EMERALD }
                        ]}
                    ]},
                    # Hero Right HUD Simulator (Red Aesthetic)
                    { "type": "frame", "id": "red-hud-box", "name": "HUD Simulator", "width": 640, "height": 470, "fill": RED_CARD, "stroke": RED_BORDER, "strokeWidth": 1.5, "cornerRadius": 16, "layout": "vertical", "clip": True, "children": [
                        { "type": "frame", "id": "red-hh", "name": "Header", "width": "fill_container", "height": 44, "fill": "#1A0E10", "stroke": RED_BORDER_SUBTLE, "strokeWidth": { "bottom": 1 }, "layout": "horizontal", "padding": [0, 18], "alignItems": "center", "justifyContent": "space_between", "children": [
                            { "type": "text", "id": "red-htitle", "name": "T", "content": "CONTROL61_SOC://CRA_GRADO_3 · SUPERVISIÓN ACTIVA", "fontSize": 11, "fontWeight": "bold", "fill": "#FFFFFF" },
                            { "type": "text", "id": "red-hlat", "name": "L", "content": "CANAL POLICIAL DIRECTO: 0.8s", "fontSize": 10, "fontWeight": "bold", "fill": RED_ACCENT }
                        ]},
                        { "type": "frame", "id": "red-hcams", "name": "Cams", "width": "fill_container", "height": 310, "fill": "#030407", "layout": "horizontal", "gap": 12, "padding": [12, 12], "children": [
                            # CAM 1
                            { "type": "frame", "id": "red-c1", "name": "CAM 1", "width": 302, "height": 286, "cornerRadius": 8, "clip": True, "fill": photo_fill(IMG_WAREHOUSE_NIGHT, "#0E040620", "#0E0406E0"), "stroke": RED_PRIMARY, "strokeWidth": 2, "padding": [12, 12], "layout": "vertical", "justifyContent": "space_between", "children": [
                                { "type": "frame", "id": "red-c1t", "name": "Top", "layout": "horizontal", "justifyContent": "space_between", "children": [
                                    { "type": "text", "id": "red-c1l", "name": "L", "content": "CAM-01 · Perímetro Norte", "fontSize": 11, "fontWeight": "bold", "fill": "#FFFFFF" },
                                    { "type": "text", "id": "red-c1r", "name": "R", "content": "● ALERTA ROJA", "fontSize": 11, "fontWeight": "bold", "fill": RED_ACCENT }
                                ]},
                                { "type": "frame", "id": "red-c1b", "name": "Box", "height": 110, "fill": "#EF444433", "stroke": RED_PRIMARY, "strokeWidth": 2, "cornerRadius": 6, "padding": [8, 8], "children": [
                                    { "type": "text", "id": "red-c1txt", "name": "T", "content": "⚠️ INTRUSIÓN DETECTADA (99.6%)\nCruce Barrera Láser Sector 3", "fontSize": 10, "fontWeight": "bold", "fill": "#FCA5A5" }
                                ]},
                                { "type": "text", "id": "red-c1f", "name": "F", "content": "Aviso Enviado a Policía · Acuda ETA: 3m 15s", "fontSize": 10, "fontWeight": "bold", "fill": RED_ACCENT }
                            ]},
                            # CAM 2
                            { "type": "frame", "id": "red-c2", "name": "CAM 2", "width": 302, "height": 286, "cornerRadius": 8, "clip": True, "fill": photo_fill(IMG_LOGISTICS_DOCK, "#0E040620", "#0E0406E0"), "stroke": EMERALD, "strokeWidth": 1.5, "padding": [12, 12], "layout": "vertical", "justifyContent": "space_between", "children": [
                                { "type": "frame", "id": "red-c2t", "name": "Top", "layout": "horizontal", "justifyContent": "space_between", "children": [
                                    { "type": "text", "id": "red-c2l", "name": "L", "content": "CAM-02 · Acceso Muelle LPR", "fontSize": 11, "fontWeight": "bold", "fill": "#FFFFFF" },
                                    { "type": "text", "id": "red-c2r", "name": "R", "content": "● AUTORIZADO", "fontSize": 11, "fontWeight": "bold", "fill": EMERALD }
                                ]},
                                { "type": "frame", "id": "red-c2b", "name": "Box", "height": 110, "fill": "#10B9811A", "stroke": EMERALD, "strokeWidth": 1.5, "cornerRadius": 6, "padding": [8, 8], "children": [
                                    { "type": "text", "id": "red-c2txt", "name": "T", "content": "MATRÍCULA: 4821-LMR [Verificada]\nFlota Autorizada · Barrera Abierta", "fontSize": 10, "fontWeight": "bold", "fill": "#86EFAC" }
                                ]},
                                { "type": "text", "id": "red-c2f", "name": "F", "content": "Paso Concedido · Registro Auditado", "fontSize": 10, "fontWeight": "bold", "fill": EMERALD }
                            ]}
                        ]},
                        { "type": "frame", "id": "red-hft", "name": "Ft", "width": "fill_container", "height": 114, "fill": "#140A0C", "layout": "horizontal", "padding": [10, 20], "justifyContent": "space_between", "alignItems": "center", "children": [
                            { "type": "text", "id": "red-hf1", "name": "T1", "content": "DOBLE VÍA: Fibra + 5G Anti-Inhibición", "fontSize": 11, "fontWeight": "bold", "fill": RED_ACCENT },
                            { "type": "text", "id": "red-hf2", "name": "T2", "content": "POLLING: Supervisión cada 30 seg", "fontSize": 11, "fontWeight": "bold", "fill": EMERALD },
                            { "type": "text", "id": "red-hf3", "name": "T3", "content": "DGP: Nº 2341 Homologada", "fontSize": 11, "fontWeight": "bold", "fill": AMBER }
                        ]}
                    ]}
                ]
            },
            # 4. Red Stats Bento
            {
                "type": "frame", "id": "red-kpis", "name": "KPIs", "width": "fill_container", "height": 130, "fill": RED_SURFACE, "stroke": RED_BORDER, "strokeWidth": { "top": 1, "bottom": 1 }, "layout": "horizontal", "padding": [0, 48], "alignItems": "center", "justifyContent": "space_between", "children": [
                    { "type": "frame", "id": "rk-1", "name": "K1", "layout": "vertical", "gap": 4, "children": [
                        { "type": "text", "id": "rkn-1", "name": "N", "content": "+2.500", "fontSize": 34, "fontWeight": "800", "fill": RED_ACCENT },
                        { "type": "text", "id": "rkl-1", "name": "L", "content": "Instalaciones protegidas en el Levante", "fontSize": 13, "fill": "#94A3B8" }
                    ]},
                    { "type": "frame", "id": "rk-2", "name": "K2", "layout": "vertical", "gap": 4, "children": [
                        { "type": "text", "id": "rkn-2", "name": "N", "content": "< 15s", "fontSize": 34, "fontWeight": "800", "fill": "#FFFFFF" },
                        { "type": "text", "id": "rkl-2", "name": "L", "content": "Tiempo de respuesta y salto en CRA", "fontSize": 13, "fill": "#94A3B8" }
                    ]},
                    { "type": "frame", "id": "rk-3", "name": "K3", "layout": "vertical", "gap": 4, "children": [
                        { "type": "text", "id": "rkn-3", "name": "N", "content": "99.8%", "fontSize": 34, "fontWeight": "800", "fill": EMERALD },
                        { "type": "text", "id": "rkl-3", "name": "L", "content": "Eliminación de falsas alarmas con IA", "fontSize": 13, "fill": "#94A3B8" }
                    ]},
                    { "type": "frame", "id": "rk-4", "name": "K4", "layout": "vertical", "gap": 4, "children": [
                        { "type": "text", "id": "rkn-4", "name": "N", "content": "20+ Años", "fontSize": 34, "fontWeight": "800", "fill": AMBER },
                        { "type": "text", "id": "rkl-4", "name": "L", "content": "Liderando seguridad privada en Murcia", "fontSize": 13, "fill": "#94A3B8" }
                    ]}
                ]
            },
            # 5. Bento Grid Red Style (6 Cards: 2 rows of 3)
            {
                "type": "frame", "id": "red-bento", "name": "Bento Grid", "width": "fill_container", "fill": RED_BG, "layout": "vertical", "padding": [64, 48], "gap": 32, "children": [
                    { "type": "frame", "id": "rb-hdr", "name": "Hdr", "layout": "vertical", "gap": 8, "children": [
                        { "type": "text", "id": "rb-eye", "name": "Eye", "content": "SOLUCIONES INDUSTRIALES HOMOLOGADAS", "fontSize": 12, "fontWeight": "800", "fill": RED_ACCENT, "letterSpacing": 1 },
                        { "type": "text", "id": "rb-title", "name": "T", "content": "Ingeniería de Seguridad de Grado 3 Sin Puntos Ciegos", "fontSize": 34, "fontWeight": "800", "fill": "#FFFFFF" }
                    ]},
                    # Row 1
                    { "type": "frame", "id": "rb-r1", "name": "R1", "layout": "horizontal", "gap": 24, "children": [
                        # Card 1: Alarmas Grado 3
                        { "type": "frame", "id": "rbc-1", "name": "C1 Grado 3", "width": 432, "height": 260, "cornerRadius": 14, "clip": True, "fill": photo_fill(IMG_WAREHOUSE_NIGHT, "#15080A55", "#15080AF8"), "stroke": RED_BORDER, "strokeWidth": 1.5, "padding": [22, 22], "layout": "vertical", "justifyContent": "space_between", "children": [
                            { "type": "frame", "id": "rb1-tags", "name": "Tags", "layout": "horizontal", "gap": 8, "children": [
                                { "type": "frame", "id": "rt1", "name": "Tag", "padding": [4, 10], "fill": "#EF444433", "stroke": RED_PRIMARY, "strokeWidth": 1, "cornerRadius": 6, "children": [
                                    { "type": "text", "id": "rt1t", "name": "T", "content": "GRADO 3 UNE-EN 50131", "fontSize": 10, "fontWeight": "bold", "fill": RED_LIGHT }
                                ]}
                            ]},
                            { "type": "frame", "id": "rb1-b", "name": "Body", "layout": "vertical", "gap": 6, "children": [
                                { "type": "text", "id": "rb1-t", "name": "T", "content": "Alarmas Grado 3 para Industria y Joyería", "fontSize": 17, "fontWeight": "700", "fill": "#FFFFFF" },
                                { "type": "text", "id": "rb1-d", "name": "D", "content": "Obligatorio para recintos de alto riesgo. Doble vía de comunicación con polling continuo y anti-inhibición.", "fontSize": 12, "fill": "#94A3B8", "lineHeight": 1.4 }
                            ]},
                            { "type": "text", "id": "rb1-l", "name": "L", "content": "Ver detalles de homologación →", "fontSize": 12, "fontWeight": "700", "fill": RED_LIGHT }
                        ]},
                        # Card 2: CCTV
                        { "type": "frame", "id": "rbc-2", "name": "C2 CCTV", "width": 432, "height": 260, "cornerRadius": 14, "clip": True, "fill": photo_fill(IMG_CCTV_CAMERA, "#15080A55", "#15080AF8"), "stroke": RED_BORDER_SUBTLE, "strokeWidth": 1.5, "padding": [22, 22], "layout": "vertical", "justifyContent": "space_between", "children": [
                            { "type": "frame", "id": "rb2-tags", "name": "Tags", "layout": "horizontal", "gap": 8, "children": [
                                { "type": "frame", "id": "rt2", "name": "Tag", "padding": [4, 10], "fill": "#10B98133", "stroke": EMERALD, "strokeWidth": 1, "cornerRadius": 6, "children": [
                                    { "type": "text", "id": "rt2t", "name": "T", "content": "ÓPTICA 4K IA", "fontSize": 10, "fontWeight": "bold", "fill": EMERALD_LIGHT }
                                ]}
                            ]},
                            { "type": "frame", "id": "rb2-b", "name": "Body", "layout": "vertical", "gap": 6, "children": [
                                { "type": "text", "id": "rb2-t", "name": "T", "content": "CCTV Inteligente e IA Perimetral", "fontSize": 17, "fontWeight": "700", "fill": "#FFFFFF" },
                                { "type": "text", "id": "rb2-d", "name": "D", "content": "Cámaras térmicas, cruce de línea y clasificación de personas y vehículos sin falsos positivos.", "fontSize": 12, "fill": "#94A3B8", "lineHeight": 1.4 }
                            ]},
                            { "type": "text", "id": "rb2-l", "name": "L", "content": "Explorar analítica IA →", "fontSize": 12, "fontWeight": "700", "fill": RED_LIGHT }
                        ]},
                        # Card 3: CRA 24h
                        { "type": "frame", "id": "rbc-3", "name": "C3 CRA", "width": 432, "height": 260, "cornerRadius": 14, "clip": True, "fill": photo_fill(IMG_CONTROL_ROOM, "#15080A55", "#15080AF8"), "stroke": RED_BORDER_SUBTLE, "strokeWidth": 1.5, "padding": [22, 22], "layout": "vertical", "justifyContent": "space_between", "children": [
                            { "type": "frame", "id": "rb3-tags", "name": "Tags", "layout": "horizontal", "gap": 8, "children": [
                                { "type": "frame", "id": "rt3", "name": "Tag", "padding": [4, 10], "fill": "#D9770633", "stroke": AMBER, "strokeWidth": 1, "cornerRadius": 6, "children": [
                                    { "type": "text", "id": "rt3t", "name": "T", "content": "CENTRAL PROPIA 24/7", "fontSize": 10, "fontWeight": "bold", "fill": AMBER_LIGHT }
                                ]}
                            ]},
                            { "type": "frame", "id": "rb3-b", "name": "Body", "layout": "vertical", "gap": 6, "children": [
                                { "type": "text", "id": "rb3-t", "name": "T", "content": "CRA 24/7 con Custodia y Acuda", "fontSize": 17, "fontWeight": "700", "fill": "#FFFFFF" },
                                { "type": "text", "id": "rb3-d", "name": "D", "content": "Verificación por vídeo en tiempo real, custodia de llaves y despacho inmediato de patrulla armada.", "fontSize": 12, "fill": "#94A3B8", "lineHeight": 1.4 }
                            ]},
                            { "type": "text", "id": "rb3-l", "name": "L", "content": "Protocolo de intervención →", "fontSize": 12, "fontWeight": "700", "fill": AMBER_LIGHT }
                        ]}
                    ]},
                    # Row 2 (Accesos, PCI, Ciberseguridad)
                    { "type": "frame", "id": "rb-r2", "name": "R2", "layout": "horizontal", "gap": 24, "children": [
                        # Card 4: Control de Accesos
                        { "type": "frame", "id": "rbc-4", "name": "C4 Accesos", "width": 432, "height": 260, "cornerRadius": 14, "clip": True, "fill": photo_fill(IMG_BIOMETRIC_TURNSTILE, "#15080A55", "#15080AF8"), "stroke": RED_BORDER_SUBTLE, "strokeWidth": 1.5, "padding": [22, 22], "layout": "vertical", "justifyContent": "space_between", "children": [
                            { "type": "frame", "id": "rb4-tags", "name": "Tags", "layout": "horizontal", "gap": 8, "children": [
                                { "type": "frame", "id": "rt4", "name": "Tag", "padding": [4, 10], "fill": "#3B82F633", "stroke": BLUE_ACCENT, "strokeWidth": 1, "cornerRadius": 6, "children": [
                                    { "type": "text", "id": "rt4t", "name": "T", "content": "BIOMETRÍA 3D", "fontSize": 10, "fontWeight": "bold", "fill": BLUE_CYAN_LIGHT }
                                ]}
                            ]},
                            { "type": "frame", "id": "rb4-b", "name": "Body", "layout": "vertical", "gap": 6, "children": [
                                { "type": "text", "id": "rb4-t", "name": "T", "content": "Control de Accesos y Torniquetes", "fontSize": 17, "fontWeight": "700", "fill": "#FFFFFF" },
                                { "type": "text", "id": "rb4-d", "name": "D", "content": "Reconocimiento facial sin contacto, lectores LPR para matrículas y control horario de empleados.", "fontSize": 12, "fill": "#94A3B8", "lineHeight": 1.4 }
                            ]},
                            { "type": "text", "id": "rb4-l", "name": "L", "content": "Configurar accesos →", "fontSize": 12, "fontWeight": "700", "fill": RED_LIGHT }
                        ]},
                        # Card 5: Incendios PCI
                        { "type": "frame", "id": "rbc-5", "name": "C5 Incendios", "width": 432, "height": 260, "cornerRadius": 14, "clip": True, "fill": photo_fill(IMG_FIRE_PROTECTION, "#15080A55", "#15080AF8"), "stroke": RED_BORDER_SUBTLE, "strokeWidth": 1.5, "padding": [22, 22], "layout": "vertical", "justifyContent": "space_between", "children": [
                            { "type": "frame", "id": "rb5-tags", "name": "Tags", "layout": "horizontal", "gap": 8, "children": [
                                { "type": "frame", "id": "rt5", "name": "Tag", "padding": [4, 10], "fill": "#EF444433", "stroke": RED_PRIMARY, "strokeWidth": 1, "cornerRadius": 6, "children": [
                                    { "type": "text", "id": "rt5t", "name": "T", "content": "RIPCI REGISTRADO", "fontSize": 10, "fontWeight": "bold", "fill": RED_LIGHT }
                                ]}
                            ]},
                            { "type": "frame", "id": "rb5-b", "name": "Body", "layout": "vertical", "gap": 6, "children": [
                                { "type": "text", "id": "rb5-t", "name": "T", "content": "Protección Contra Incendios PCI", "fontSize": 17, "fontWeight": "700", "fill": "#FFFFFF" },
                                { "type": "text", "id": "rb5-d", "name": "D", "content": "Detección precoz óptica y por aspiración, extinción por gas en salas técnicas y mantenimiento certificado.", "fontSize": 12, "fill": "#94A3B8", "lineHeight": 1.4 }
                            ]},
                            { "type": "text", "id": "rb5-l", "name": "L", "content": "Normativa y mantenimiento →", "fontSize": 12, "fontWeight": "700", "fill": RED_LIGHT }
                        ]},
                        # Card 6: Ciberseguridad
                        { "type": "frame", "id": "rbc-6", "name": "C6 Ciberseguridad", "width": 432, "height": 260, "cornerRadius": 14, "clip": True, "fill": photo_fill(IMG_CONTROL_ROOM, "#15080A55", "#15080AF8"), "stroke": RED_BORDER_SUBTLE, "strokeWidth": 1.5, "padding": [22, 22], "layout": "vertical", "justifyContent": "space_between", "children": [
                            { "type": "frame", "id": "rb6-tags", "name": "Tags", "layout": "horizontal", "gap": 8, "children": [
                                { "type": "frame", "id": "rt6", "name": "Tag", "padding": [4, 10], "fill": "#10B98133", "stroke": EMERALD, "strokeWidth": 1, "cornerRadius": 6, "children": [
                                    { "type": "text", "id": "rt6t", "name": "T", "content": "ENS NIVEL ALTO", "fontSize": 10, "fontWeight": "bold", "fill": EMERALD_LIGHT }
                                ]}
                            ]},
                            { "type": "frame", "id": "rb6-b", "name": "Body", "layout": "vertical", "gap": 6, "children": [
                                { "type": "text", "id": "rb6-t", "name": "T", "content": "Ciberseguridad y Redes OT", "fontSize": 17, "fontWeight": "700", "fill": "#FFFFFF" },
                                { "type": "text", "id": "rb6-d", "name": "D", "content": "Segmentación de redes industriales, firewalls de grado militar y protección contra ciberataques.", "fontSize": 12, "fill": "#94A3B8", "lineHeight": 1.4 }
                            ]},
                            { "type": "text", "id": "rb6-l", "name": "L", "content": "Auditoría de ciberseguridad →", "fontSize": 12, "fontWeight": "700", "fill": RED_LIGHT }
                        ]}
                    ]}
                ]
            },
            # 6. Protocolo de Defensa 4 Fases (Red Workflow)
            {
                "type": "frame", "id": "red-protocol-sec", "name": "Protocolo de Defensa", "width": "fill_container", "height": 340, "fill": RED_SURFACE, "stroke": RED_BORDER, "strokeWidth": { "top": 1, "bottom": 1 }, "layout": "vertical", "padding": [48, 48], "gap": 28, "children": [
                    { "type": "frame", "id": "rp-hdr", "name": "Hdr", "layout": "horizontal", "justifyContent": "space_between", "alignItems": "center", "children": [
                        { "type": "frame", "id": "rph-l", "name": "L", "layout": "vertical", "gap": 4, "children": [
                            { "type": "text", "id": "rph-eye", "name": "Eye", "content": "OPERATIVA DE RESPUESTA EN TIEMPO REAL", "fontSize": 11, "fontWeight": "800", "fill": RED_ACCENT },
                            { "type": "text", "id": "rph-title", "name": "Title", "content": "Protocolo de Neutralización en 4 Fases Homologadas", "fontSize": 24, "fontWeight": "800", "fill": "#FFFFFF" }
                        ]},
                        { "type": "text", "id": "rph-time", "name": "Time", "content": "⏱ TIEMPO TOTAL MEDIO: < 15 SEGUNDOS", "fontSize": 12, "fontWeight": "bold", "fill": EMERALD }
                    ]},
                    { "type": "frame", "id": "rp-steps", "name": "Steps", "width": "fill_container", "layout": "horizontal", "gap": 16, "children": [
                        # Step 1
                        { "type": "frame", "id": "rps-1", "name": "S1", "width": 320, "height": 160, "fill": "#181014", "stroke": RED_BORDER, "strokeWidth": 1, "cornerRadius": 10, "padding": [16, 16], "layout": "vertical", "justifyContent": "space_between", "children": [
                            { "type": "frame", "id": "rs1-t", "name": "Top", "width": "fill_container", "layout": "horizontal", "justifyContent": "space_between", "alignItems": "center", "children": [
                                { "type": "text", "id": "rs1-num", "name": "Num", "content": "FASE 01", "fontSize": 11, "fontWeight": "800", "fill": RED_ACCENT },
                                { "type": "text", "id": "rs1-ms", "name": "Ms", "content": "0.1s", "fontSize": 11, "fontWeight": "bold", "fill": "#94A3B8" }
                            ]},
                            { "type": "text", "id": "rs1-h", "name": "H", "content": "Detección Perimetral", "fontSize": 15, "fontWeight": "700", "fill": "#FFFFFF" },
                            { "type": "text", "id": "rs1-d", "name": "D", "content": "Barreras infrarrojas y radar térmico captan la intrusión en el perímetro exterior.", "fontSize": 11, "fill": "#94A3B8", "lineHeight": 1.4 }
                        ]},
                        # Step 2
                        { "type": "frame", "id": "rps-2", "name": "S2", "width": 320, "height": 160, "fill": "#181014", "stroke": RED_BORDER_SUBTLE, "strokeWidth": 1, "cornerRadius": 10, "padding": [16, 16], "layout": "vertical", "justifyContent": "space_between", "children": [
                            { "type": "frame", "id": "rs2-t", "name": "Top", "width": "fill_container", "layout": "horizontal", "justifyContent": "space_between", "alignItems": "center", "children": [
                                { "type": "text", "id": "rs2-num", "name": "Num", "content": "FASE 02", "fontSize": 11, "fontWeight": "800", "fill": RED_ACCENT },
                                { "type": "text", "id": "rs2-ms", "name": "Ms", "content": "0.8s", "fontSize": 11, "fontWeight": "bold", "fill": "#94A3B8" }
                            ]},
                            { "type": "text", "id": "rs2-h", "name": "H", "content": "Filtrado IA Neural", "fontSize": 15, "fontWeight": "700", "fill": "#FFFFFF" },
                            { "type": "text", "id": "rs2-d", "name": "D", "content": "Algoritmos descartan animales, vegetación y lluvia, confirmando amenaza real.", "fontSize": 11, "fill": "#94A3B8", "lineHeight": 1.4 }
                        ]},
                        # Step 3
                        { "type": "frame", "id": "rps-3", "name": "S3", "width": 320, "height": 160, "fill": "#181014", "stroke": RED_BORDER_SUBTLE, "strokeWidth": 1, "cornerRadius": 10, "padding": [16, 16], "layout": "vertical", "justifyContent": "space_between", "children": [
                            { "type": "frame", "id": "rs3-t", "name": "Top", "width": "fill_container", "layout": "horizontal", "justifyContent": "space_between", "alignItems": "center", "children": [
                                { "type": "text", "id": "rs3-num", "name": "Num", "content": "FASE 03", "fontSize": 11, "fontWeight": "800", "fill": RED_ACCENT },
                                { "type": "text", "id": "rs3-ms", "name": "Ms", "content": "4.2s", "fontSize": 11, "fontWeight": "bold", "fill": "#94A3B8" }
                            ]},
                            { "type": "text", "id": "rs3-h", "name": "H", "content": "Verificación CRA 24/7", "fontSize": 15, "fontWeight": "700", "fill": "#FFFFFF" },
                            { "type": "text", "id": "rs3-d", "name": "D", "content": "Operadores especializados visualizan ráfagas de vídeo y despachan patrulla Acuda.", "fontSize": 11, "fill": "#94A3B8", "lineHeight": 1.4 }
                        ]},
                        # Step 4
                        { "type": "frame", "id": "rps-4", "name": "S4", "width": 320, "height": 160, "fill": "#181014", "stroke": RED_PRIMARY, "strokeWidth": 1.5, "cornerRadius": 10, "padding": [16, 16], "layout": "vertical", "justifyContent": "space_between", "children": [
                            { "type": "frame", "id": "rs4-t", "name": "Top", "width": "fill_container", "layout": "horizontal", "justifyContent": "space_between", "alignItems": "center", "children": [
                                { "type": "text", "id": "rs4-num", "name": "Num", "content": "FASE 04", "fontSize": 11, "fontWeight": "800", "fill": RED_LIGHT },
                                { "type": "text", "id": "rs4-ms", "name": "Ms", "content": "< 15s", "fontSize": 11, "fontWeight": "bold", "fill": EMERALD }
                            ]},
                            { "type": "text", "id": "rs4-h", "name": "H", "content": "Intervención Policial", "fontSize": 15, "fontWeight": "700", "fill": "#FFFFFF" },
                            { "type": "text", "id": "rs4-d", "name": "D", "content": "Transmisión telemática prioritaria a Policía Nacional y Guardia Civil.", "fontSize": 11, "fill": "#94A3B8", "lineHeight": 1.4 }
                        ]}
                    ]}
                ]
            },
            # 7. Free Audit CTA Form Card Red
            {
                "type": "frame", "id": "red-audit-sec", "name": "Sección Auditoría", "width": "fill_container", "height": 380, "fill": RED_BG, "layout": "horizontal", "padding": [48, 64], "alignItems": "center", "justifyContent": "space_between", "children": [
                    { "type": "frame", "id": "red-aud-l", "name": "Left", "width": 640, "layout": "vertical", "gap": 16, "children": [
                        { "type": "text", "id": "red-al-eye", "name": "Eye", "content": "AUDITORÍA IN SITU SIN COMPROMISO", "fontSize": 12, "fontWeight": "800", "fill": RED_ACCENT, "letterSpacing": 1 },
                        { "type": "text", "id": "red-al-title", "name": "Title", "content": "¿Cumple su empresa con la normativa de seguridad privada y grado de riesgo exigido?", "fontSize": 30, "fontWeight": "800", "fill": "#FFFFFF", "lineHeight": 1.2, "textGrowth": "fixed-width", "width": 640 },
                        { "type": "text", "id": "red-al-desc", "name": "Desc", "content": "Nuestros ingenieros colegiados realizan un análisis integral de adecuación a la Orden INT/316/2011, inspeccionando ángulos ciegos, coberturas y vías de comunicación.", "fontSize": 14, "fill": "#94A3B8", "lineHeight": 1.5, "textGrowth": "fixed-width", "width": 600 }
                    ]},
                    { "type": "frame", "id": "red-aud-r", "name": "Form Card", "width": 480, "height": 290, "fill": "#15090C", "stroke": RED_BORDER, "strokeWidth": 1.5, "cornerRadius": 14, "padding": [22, 22], "layout": "vertical", "justifyContent": "space_between", "children": [
                        { "type": "text", "id": "red-ft-t", "name": "Title", "content": "Solicitar Diagnóstico Técnico de Seguridad", "fontSize": 16, "fontWeight": "700", "fill": "#FFFFFF" },
                        { "type": "frame", "id": "red-f-f1", "name": "F1", "height": 42, "fill": "#08090E", "stroke": RED_BORDER_SUBTLE, "strokeWidth": 1, "cornerRadius": 6, "padding": [0, 16], "layout": "horizontal", "alignItems": "center", "children": [
                            { "type": "text", "id": "red-f1-ph", "name": "P", "content": "Nombre de la Empresa o Nave Industrial", "fontSize": 13, "fill": "#64748B" }
                        ]},
                        { "type": "frame", "id": "red-f-f2", "name": "F2", "height": 42, "fill": "#08090E", "stroke": RED_BORDER_SUBTLE, "strokeWidth": 1, "cornerRadius": 6, "padding": [0, 16], "layout": "horizontal", "alignItems": "center", "children": [
                            { "type": "text", "id": "red-f2-ph", "name": "P", "content": "Teléfono de Contacto Directo / Email", "fontSize": 13, "fill": "#64748B" }
                        ]},
                        { "type": "frame", "id": "red-f-btn", "name": "Submit", "height": 46, "fill": RED_PRIMARY, "cornerRadius": 8, "alignItems": "center", "justifyContent": "center", "children": [
                            { "type": "text", "id": "red-fb-txt", "name": "T", "content": "Enviar Solicitud de Auditoría Gratuita", "fontSize": 14, "fontWeight": "800", "fill": "#FFFFFF" }
                        ]}
                    ]}
                ]
            },
            # 8. Certifications Strip Red
            {
                "type": "frame", "id": "red-certs", "name": "Acreditaciones", "width": "fill_container", "height": 100, "fill": "#0A0B12", "stroke": RED_BORDER_SUBTLE, "strokeWidth": { "top": 1, "bottom": 1 }, "layout": "horizontal", "padding": [0, 48], "alignItems": "center", "justifyContent": "space_between", "children": [
                    { "type": "text", "id": "rc-t1", "name": "C1", "content": "🏛 DGP Nº 2341 (MINISTERIO DEL INTERIOR)", "fontSize": 12, "fontWeight": "bold", "fill": "#94A3B8" },
                    { "type": "text", "id": "rc-t2", "name": "C2", "content": "🛡 GRADO 3 (UNE-EN 50131)", "fontSize": 12, "fontWeight": "bold", "fill": "#94A3B8" },
                    { "type": "text", "id": "rc-t3", "name": "C3", "content": "🏅 ISO 9001 / 14001 / 45001 (RINA)", "fontSize": 12, "fontWeight": "bold", "fill": "#94A3B8" },
                    { "type": "text", "id": "rc-t4", "name": "C4", "content": "🔒 ENS NIVEL ALTO CERTIFICADO", "fontSize": 12, "fontWeight": "bold", "fill": "#94A3B8" }
                ]
            },
            # 9. Footer Red
            {
                "type": "frame", "id": "red-footer", "name": "Footer", "width": "fill_container", "height": 280, "fill": "#06070B", "layout": "vertical", "padding": [40, 48, 20, 48], "justifyContent": "space_between", "children": [
                    { "type": "frame", "id": "red-ft-cols", "name": "Cols", "width": "fill_container", "layout": "horizontal", "justifyContent": "space_between", "children": [
                        { "type": "frame", "id": "red-fc1", "name": "C1", "width": 420, "layout": "vertical", "gap": 10, "children": [
                            { "type": "text", "id": "red-ftt", "name": "T", "content": "CONTROL 61 · INGENIERÍA DE SEGURIDAD", "fontSize": 15, "fontWeight": "800", "fill": "#FFFFFF", "letterSpacing": 1.2 },
                            { "type": "text", "id": "red-ftd", "name": "D", "content": "Desarrollos y Sistemas Inteligentes S.L. · DGP Nº 2341\nSistemas Homologados Grado 3 y CRA 24h.\nPol. Ind. La Polvorista, Molina de Segura (Murcia)", "fontSize": 12, "fill": "#64748B", "lineHeight": 1.6 }
                        ]},
                        { "type": "frame", "id": "red-fc2", "name": "C2", "layout": "vertical", "gap": 6, "children": [
                            { "type": "text", "id": "red-fc2t", "name": "T", "content": "SERVICIOS", "fontSize": 11, "fontWeight": "800", "fill": RED_ACCENT },
                            { "type": "text", "id": "red-fc2l1", "name": "L1", "content": "Alarmas Homologadas Grado 3", "fontSize": 12, "fill": "#94A3B8" },
                            { "type": "text", "id": "red-fc2l2", "name": "L2", "content": "CCTV Inteligente e IA Perimetral", "fontSize": 12, "fill": "#94A3B8" },
                            { "type": "text", "id": "red-fc2l3", "name": "L3", "content": "Central Receptora CRA 24/7", "fontSize": 12, "fill": "#94A3B8" }
                        ]},
                        { "type": "frame", "id": "red-fc3", "name": "C3", "layout": "vertical", "gap": 6, "children": [
                            { "type": "text", "id": "red-fc3t", "name": "T", "content": "CONTACTO 24H", "fontSize": 11, "fontWeight": "800", "fill": RED_ACCENT },
                            { "type": "text", "id": "red-fc3l1", "name": "L1", "content": "📞 Centralita y Averías: 968 622 984", "fontSize": 12, "fill": "#FFFFFF", "fontWeight": "bold" },
                            { "type": "text", "id": "red-fc3l2", "name": "L2", "content": "✉️ info@control61.com", "fontSize": 12, "fill": "#94A3B8" },
                            { "type": "text", "id": "red-fc3l3", "name": "L3", "content": "📍 Molina de Segura, Murcia", "fontSize": 12, "fill": "#94A3B8" }
                        ]}
                    ]},
                    { "type": "frame", "id": "red-ft-bot", "name": "Bot", "width": "fill_container", "layout": "horizontal", "justifyContent": "space_between", "alignItems": "center", "children": [
                        { "type": "text", "id": "red-copy", "name": "Copy", "content": "© 2026 Control 61 (Desarrollos y Sistemas Inteligentes S.L.). Todos los derechos reservados.", "fontSize": 11, "fill": "#475569" },
                        { "type": "text", "id": "red-legal", "name": "Legal", "content": "Aviso Legal · Privacidad · DGP 2341 · ISO 9001", "fontSize": 11, "fill": "#475569" }
                    ]}
                ]
            }
        ]
    }

# =============================================================================
# 🔵 OPTION B: STRONG COBALT BLUE (Cyber SOC & Defence Edition)
# =============================================================================
def build_option_b_blue():
    nav_links = [
        ("Inicio", True),
        ("Cyber CCTV IA", False),
        ("Central SOC 24/7", False),
        ("Biometría 3D", False),
        ("Sistemas Grado 3", False),
        ("Redes OT & Ciber", False),
        ("Normativa ENS", False),
        ("Contacto", False)
    ]
    
    header_links = []
    for name, is_active in nav_links:
        header_links.append({
            "type": "text",
            "id": f"blue-nav-{name}",
            "name": name,
            "content": name,
            "fontSize": 13,
            "fontWeight": "700" if is_active else "500",
            "fill": BLUE_CYAN if is_active else "#94A3B8"
        })
        
    return {
        "type": "frame",
        "id": "x6zQ8",
        "name": "🔵 Opción B: Control 61 - Cobalt Cyber SOC Edition (Electric Blue Style)",
        "x": 1600,
        "y": 0,
        "width": 1440,
        "height": 3480,
        "fill": BLUE_BG,
        "layout": "vertical",
        "clip": True,
        "children": [
            # 1. Top SOC Status Bar Blue
            {
                "type": "frame", "id": "blue-top-bar", "name": "Top SOC Bar", "width": "fill_container", "height": 42, "fill": "#060D1E", "stroke": BLUE_BORDER, "strokeWidth": { "bottom": 1 }, "layout": "horizontal", "padding": [0, 48], "alignItems": "center", "justifyContent": "space_between", "children": [
                    { "type": "frame", "id": "blue-tb-l", "name": "L", "layout": "horizontal", "gap": 8, "alignItems": "center", "children": [
                        { "type": "ellipse", "id": "blue-dot-live", "name": "Live Blue Dot", "width": 8, "height": 8, "fill": BLUE_CYAN },
                        { "type": "text", "id": "blue-st-txt", "name": "T", "content": "SOC CYBER OPERATIONS · CONEXIÓN CIFRADA E2E · DGP Nº 2341 · ENS NIVEL ALTO", "fontSize": 11, "fontWeight": "bold", "fill": BLUE_CYAN_LIGHT }
                    ]},
                    { "type": "frame", "id": "blue-tb-r", "name": "R", "layout": "horizontal", "gap": 20, "alignItems": "center", "children": [
                        { "type": "text", "id": "blue-phone-24", "name": "Phone", "content": "🛰️ Línea Directa SOC 24h: 968 622 984", "fontSize": 12, "fontWeight": "bold", "fill": "#FFFFFF" },
                        { "type": "text", "id": "blue-soc-portal", "name": "Portal", "content": "Portal Cyber SOC →", "fontSize": 12, "fontWeight": "bold", "fill": BLUE_CYAN }
                    ]}
                ]
            },
            # 2. Navbar Blue
            {
                "type": "frame", "id": "blue-navbar", "name": "Navbar Glass", "width": "fill_container", "height": 78, "fill": "#081126EE", "stroke": BLUE_BORDER_SUBTLE, "strokeWidth": { "bottom": 1 }, "layout": "horizontal", "padding": [0, 48], "alignItems": "center", "justifyContent": "space_between", "children": [
                    { "type": "frame", "id": "blue-brand", "name": "Brand", "layout": "horizontal", "gap": 12, "alignItems": "center", "children": [
                        { "type": "frame", "id": "blue-logo-box", "name": "Shield Box", "width": 44, "height": 44, "fill": "#1E3A8A33", "stroke": BLUE_PRIMARY, "strokeWidth": 1.5, "cornerRadius": 10, "alignItems": "center", "justifyContent": "center", "children": [
                            { "type": "icon", "id": "blue-sh-ico", "name": "Ico", "library": "lucide", "icon": "shield-check", "width": 24, "height": 24, "fill": BLUE_CYAN }
                        ]},
                        { "type": "frame", "id": "blue-btexts", "name": "Text", "layout": "vertical", "gap": 2, "children": [
                            { "type": "text", "id": "blue-bname", "name": "Name", "content": "CONTROL 61", "fontSize": 20, "fontWeight": "800", "fill": "#FFFFFF", "letterSpacing": 1.5 },
                            { "type": "text", "id": "blue-bsub", "name": "Sub", "content": "CYBER PHYSICAL DEFENSE & SOC", "fontSize": 8, "fontWeight": "700", "fill": BLUE_CYAN, "letterSpacing": 0.8 }
                        ]}
                    ]},
                    { "type": "frame", "id": "blue-navlinks", "name": "Links", "layout": "horizontal", "gap": 20, "alignItems": "center", "children": header_links },
                    { "type": "frame", "id": "blue-navctas", "name": "CTAs", "layout": "horizontal", "gap": 12, "alignItems": "center", "children": [
                        { "type": "frame", "id": "blue-btn-ph", "name": "Phone", "height": 40, "padding": [0, 16], "fill": "#0E1A38", "stroke": BLUE_BORDER, "strokeWidth": 1, "cornerRadius": 8, "layout": "horizontal", "gap": 8, "alignItems": "center", "children": [
                            { "type": "icon", "id": "blue-pico", "name": "P", "library": "lucide", "icon": "phone", "width": 14, "height": 14, "fill": BLUE_CYAN },
                            { "type": "text", "id": "blue-ptxt", "name": "T", "content": "968 622 984", "fontSize": 12, "fontWeight": "bold", "fill": "#FFFFFF" }
                        ]},
                        { "type": "frame", "id": "blue-btn-cta", "name": "CTA", "height": 40, "padding": [0, 18], "fill": BLUE_PRIMARY, "cornerRadius": 8, "alignItems": "center", "justifyContent": "center", "children": [
                            { "type": "text", "id": "blue-ctatxt", "name": "T", "content": "Auditoría Tecnológica", "fontSize": 13, "fontWeight": "700", "fill": "#FFFFFF" }
                        ]}
                    ]}
                ]
            },
            # 3. Hero Section Blue with Military SOC HUD
            {
                "type": "frame", "id": "blue-hero-sec", "name": "Hero Section", "width": "fill_container", "height": 680, "fill": BLUE_BG, "layout": "horizontal", "padding": [56, 48], "gap": 40, "alignItems": "center", "justifyContent": "space_between", "children": [
                    { "type": "frame", "id": "blue-h-l", "name": "Left", "width": 630, "layout": "vertical", "gap": 22, "children": [
                        { "type": "frame", "id": "blue-badge-pill", "name": "Badge", "height": 32, "padding": [0, 14], "fill": "#1E3A8A26", "stroke": BLUE_BORDER, "strokeWidth": 1, "cornerRadius": 20, "layout": "horizontal", "gap": 8, "alignItems": "center", "children": [
                            { "type": "icon", "id": "blue-bico", "name": "I", "library": "lucide", "icon": "cpu", "width": 14, "height": 14, "fill": BLUE_CYAN },
                            { "type": "text", "id": "blue-btxt", "name": "T", "content": "INGENIERÍA DE SEGURIDAD FÍSICA & CIBERNÉTICA · DGP 2341", "fontSize": 10, "fontWeight": "700", "fill": BLUE_CYAN }
                        ]},
                        { "type": "text", "id": "blue-h1", "name": "H1", "content": "Seguridad Electrónica de Grado Militar, Visión IA y Centro SOC 24/7", "fontSize": 44, "fontWeight": "800", "fill": "#FFFFFF", "lineHeight": 1.15, "textGrowth": "fixed-width", "width": 630 },
                        { "type": "text", "id": "blue-hdesc", "name": "Desc", "content": "Protección total para infraestructuras críticas, plantas industriales y plataformas logísticas. Doble vía cifrada AES-256, telemetría perimetral continua y resolución de alertas en tiempo real.", "fontSize": 15, "fill": "#94A3B8", "lineHeight": 1.6, "textGrowth": "fixed-width", "width": 610 },
                        { "type": "frame", "id": "blue-h-btns", "name": "Btns", "layout": "horizontal", "gap": 16, "children": [
                            { "type": "frame", "id": "blue-bm", "name": "CTA", "height": 50, "padding": [0, 24], "fill": BLUE_PRIMARY, "cornerRadius": 10, "layout": "horizontal", "gap": 10, "alignItems": "center", "children": [
                                { "type": "text", "id": "blue-bmt", "name": "T", "content": "Conectar con SOC Control 61", "fontSize": 14, "fontWeight": "700", "fill": "#FFFFFF" },
                                { "type": "icon", "id": "blue-bmi", "name": "I", "library": "lucide", "icon": "arrow-up-right", "width": 16, "height": 16, "fill": "#FFFFFF" }
                            ]},
                            { "type": "frame", "id": "blue-bs", "name": "Demo", "height": 50, "padding": [0, 20], "fill": "#0E1A38", "stroke": BLUE_BORDER, "strokeWidth": 1.5, "cornerRadius": 10, "layout": "horizontal", "gap": 8, "alignItems": "center", "children": [
                                { "type": "icon", "id": "blue-psi", "name": "P", "library": "lucide", "icon": "terminal", "width": 15, "height": 15, "fill": BLUE_CYAN },
                                { "type": "text", "id": "blue-pst", "name": "T", "content": "Ver Demostración SOC", "fontSize": 13, "fontWeight": "600", "fill": "#F1F5F9" }
                            ]}
                        ]},
                        { "type": "frame", "id": "blue-trust-strip", "name": "Trust", "layout": "horizontal", "gap": 24, "alignItems": "center", "children": [
                            { "type": "text", "id": "blue-t1", "name": "T1", "content": "✓ Encriptación Militar AES-256", "fontSize": 12, "fontWeight": "600", "fill": BLUE_CYAN },
                            { "type": "text", "id": "blue-t2", "name": "T2", "content": "✓ Homologación Grado 3 DGP", "fontSize": 12, "fontWeight": "600", "fill": BLUE_CYAN },
                            { "type": "text", "id": "blue-t3", "name": "T3", "content": "✓ SLA Uptime 99.999%", "fontSize": 12, "fontWeight": "600", "fill": BLUE_CYAN }
                        ]}
                    ]},
                    # Hero Right HUD Simulator (Blue Cyber Style)
                    { "type": "frame", "id": "blue-hud-box", "name": "HUD Simulator", "width": 640, "height": 470, "fill": BLUE_CARD, "stroke": BLUE_BORDER, "strokeWidth": 1.5, "cornerRadius": 16, "layout": "vertical", "clip": True, "children": [
                        { "type": "frame", "id": "blue-hh", "name": "Header", "width": "fill_container", "height": 44, "fill": "#0A1736", "stroke": BLUE_BORDER_SUBTLE, "strokeWidth": { "bottom": 1 }, "layout": "horizontal", "padding": [0, 18], "alignItems": "center", "justifyContent": "space_between", "children": [
                            { "type": "text", "id": "blue-htitle", "name": "T", "content": "CYBER_SOC://STREAM_MATRIX_4K · CIFRADO E2E", "fontSize": 11, "fontWeight": "bold", "fill": "#FFFFFF" },
                            { "type": "text", "id": "blue-hlat", "name": "L", "content": "LATENCIA RED: 8ms (FIBRA 10Gb)", "fontSize": 10, "fontWeight": "bold", "fill": BLUE_CYAN }
                        ]},
                        { "type": "frame", "id": "blue-hcams", "name": "Cams", "width": "fill_container", "height": 310, "fill": "#020713", "layout": "horizontal", "gap": 12, "padding": [12, 12], "children": [
                            # CAM 1 SOC
                            { "type": "frame", "id": "blue-c1", "name": "CAM 1", "width": 302, "height": 286, "cornerRadius": 8, "clip": True, "fill": photo_fill(IMG_CONTROL_ROOM, "#06132D20", "#06132DE0"), "stroke": BLUE_CYAN, "strokeWidth": 2, "padding": [12, 12], "layout": "vertical", "justifyContent": "space_between", "children": [
                                { "type": "frame", "id": "blue-c1t", "name": "Top", "layout": "horizontal", "justifyContent": "space_between", "children": [
                                    { "type": "text", "id": "blue-c1l", "name": "L", "content": "CAM-01 · Centro de Control SOC", "fontSize": 11, "fontWeight": "bold", "fill": "#FFFFFF" },
                                    { "type": "text", "id": "blue-c1r", "name": "R", "content": "● 4K 60FPS", "fontSize": 11, "fontWeight": "bold", "fill": BLUE_CYAN }
                                ]},
                                { "type": "frame", "id": "blue-c1b", "name": "Box", "height": 110, "fill": "#06B6D426", "stroke": BLUE_CYAN, "strokeWidth": 1.5, "cornerRadius": 6, "padding": [8, 8], "children": [
                                    { "type": "text", "id": "blue-c1txt", "name": "T", "content": "SUPERVISIÓN NEURAL ACTIVA\n2.500 Nodos Conectados en Línea", "fontSize": 10, "fontWeight": "bold", "fill": BLUE_CYAN_LIGHT }
                                ]},
                                { "type": "text", "id": "blue-c1f", "name": "F", "content": "Operación Normal · Zero Packet Loss", "fontSize": 10, "fontWeight": "bold", "fill": EMERALD }
                            ]},
                            # CAM 2 CPD
                            { "type": "frame", "id": "blue-c2", "name": "CAM 2", "width": 302, "height": 286, "cornerRadius": 8, "clip": True, "fill": photo_fill(IMG_SERVER_CPD, "#06132D20", "#06132DE0"), "stroke": BLUE_PRIMARY, "strokeWidth": 1.5, "padding": [12, 12], "layout": "vertical", "justifyContent": "space_between", "children": [
                                { "type": "frame", "id": "blue-c2t", "name": "Top", "layout": "horizontal", "justifyContent": "space_between", "children": [
                                    { "type": "text", "id": "blue-c2l", "name": "L", "content": "CAM-02 · Sala CPD & Servidores", "fontSize": 11, "fontWeight": "bold", "fill": "#FFFFFF" },
                                    { "type": "text", "id": "blue-c2r", "name": "R", "content": "● BIOMETRÍA", "fontSize": 11, "fontWeight": "bold", "fill": BLUE_CYAN_LIGHT }
                                ]},
                                { "type": "frame", "id": "blue-c2b", "name": "Box", "height": 110, "fill": "#3B82F626", "stroke": BLUE_ACCENT, "strokeWidth": 1.5, "cornerRadius": 6, "padding": [8, 8], "children": [
                                    { "type": "text", "id": "blue-c2txt", "name": "T", "content": "ACCESO NIVEL 3 AUTORIZADO\nTemp: 21.2°C | Gas PCI: Standby", "fontSize": 10, "fontWeight": "bold", "fill": "#93C5FD" }
                                ]},
                                { "type": "text", "id": "blue-c2f", "name": "F", "content": "Ingeniero M. Torres Verificado", "fontSize": 10, "fontWeight": "bold", "fill": BLUE_CYAN }
                            ]}
                        ]},
                        { "type": "frame", "id": "blue-hft", "name": "Ft", "width": "fill_container", "height": 114, "fill": "#071026", "layout": "horizontal", "padding": [10, 20], "justifyContent": "space_between", "alignItems": "center", "children": [
                            { "type": "text", "id": "blue-hf1", "name": "T1", "content": "ENCRIPTACIÓN: AES-256 E2E", "fontSize": 11, "fontWeight": "bold", "fill": BLUE_CYAN },
                            { "type": "text", "id": "blue-hf2", "name": "T2", "content": "INTEGRIDAD RED: 100% OK", "fontSize": 11, "fontWeight": "bold", "fill": EMERALD },
                            { "type": "text", "id": "blue-hf3", "name": "T3", "content": "SLA: 99.999% Certificado", "fontSize": 11, "fontWeight": "bold", "fill": AMBER }
                        ]}
                    ]}
                ]
            },
            # 4. Blue Stats Bento
            {
                "type": "frame", "id": "blue-kpis", "name": "KPIs", "width": "fill_container", "height": 130, "fill": BLUE_SURFACE, "stroke": BLUE_BORDER, "strokeWidth": { "top": 1, "bottom": 1 }, "layout": "horizontal", "padding": [0, 48], "alignItems": "center", "justifyContent": "space_between", "children": [
                    { "type": "frame", "id": "bk-1", "name": "K1", "layout": "vertical", "gap": 4, "children": [
                        { "type": "text", "id": "bkn-1", "name": "N", "content": "+2.500", "fontSize": 34, "fontWeight": "800", "fill": BLUE_CYAN },
                        { "type": "text", "id": "bkl-1", "name": "L", "content": "Infraestructuras y recintos protegidos", "fontSize": 13, "fill": "#94A3B8" }
                    ]},
                    { "type": "frame", "id": "bk-2", "name": "K2", "layout": "vertical", "gap": 4, "children": [
                        { "type": "text", "id": "bkn-2", "name": "N", "content": "< 15s", "fontSize": 34, "fontWeight": "800", "fill": "#FFFFFF" },
                        { "type": "text", "id": "bkl-2", "name": "L", "content": "Tiempo de respuesta validado por SLA", "fontSize": 13, "fill": "#94A3B8" }
                    ]},
                    { "type": "frame", "id": "bk-3", "name": "K3", "layout": "vertical", "gap": 4, "children": [
                        { "type": "text", "id": "bkn-3", "name": "N", "content": "99.999%", "fontSize": 34, "fontWeight": "800", "fill": EMERALD },
                        { "type": "text", "id": "bkl-3", "name": "L", "content": "Disponibilidad continua de comunicaciones", "fontSize": 13, "fill": "#94A3B8" }
                    ]},
                    { "type": "frame", "id": "bk-4", "name": "K4", "layout": "vertical", "gap": 4, "children": [
                        { "type": "text", "id": "bkn-4", "name": "N", "content": "20+ Años", "fontSize": 34, "fontWeight": "800", "fill": AMBER },
                        { "type": "text", "id": "bkl-4", "name": "L", "content": "Ingeniería de seguridad y ciberprotección", "fontSize": 13, "fill": "#94A3B8" }
                    ]}
                ]
            },
            # 5. Bento Grid Blue Cyber (6 Cards: 2 rows of 3)
            {
                "type": "frame", "id": "blue-bento", "name": "Bento Grid", "width": "fill_container", "fill": BLUE_BG, "layout": "vertical", "padding": [64, 48], "gap": 32, "children": [
                    { "type": "frame", "id": "bb-hdr", "name": "Hdr", "layout": "vertical", "gap": 8, "children": [
                        { "type": "text", "id": "bb-eye", "name": "Eye", "content": "CYBER-PHYSICAL SECURITY PILLARS", "fontSize": 12, "fontWeight": "800", "fill": BLUE_CYAN, "letterSpacing": 1 },
                        { "type": "text", "id": "bb-title", "name": "T", "content": "Protección Perimetral y Ciberseguridad de Alta Fidelidad", "fontSize": 34, "fontWeight": "800", "fill": "#FFFFFF" }
                    ]},
                    # Row 1
                    { "type": "frame", "id": "bb-r1", "name": "R1", "layout": "horizontal", "gap": 24, "children": [
                        # Card 1: CCTV
                        { "type": "frame", "id": "bbc-1", "name": "C1 CCTV", "width": 432, "height": 260, "cornerRadius": 14, "clip": True, "fill": photo_fill(IMG_CCTV_CAMERA, "#09173855", "#091738F8"), "stroke": BLUE_BORDER, "strokeWidth": 1.5, "padding": [22, 22], "layout": "vertical", "justifyContent": "space_between", "children": [
                            { "type": "frame", "id": "bb1-tags", "name": "Tags", "layout": "horizontal", "gap": 8, "children": [
                                { "type": "frame", "id": "bt1", "name": "Tag", "padding": [4, 10], "fill": "#2563EB33", "stroke": BLUE_PRIMARY, "strokeWidth": 1, "cornerRadius": 6, "children": [
                                    { "type": "text", "id": "bt1t", "name": "T", "content": "RED NEURAL 4K", "fontSize": 10, "fontWeight": "bold", "fill": BLUE_CYAN_LIGHT }
                                ]}
                            ]},
                            { "type": "frame", "id": "bb1-b", "name": "Body", "layout": "vertical", "gap": 6, "children": [
                                { "type": "text", "id": "bb1-t", "name": "T", "content": "CCTV con Visión Artificial y Cámaras Térmicas", "fontSize": 17, "fontWeight": "700", "fill": "#FFFFFF" },
                                { "type": "text", "id": "bb1-d", "name": "D", "content": "Detección térmica perimetral, radar perimétrico integrado y clasificación de amenazas en microsegundos.", "fontSize": 12, "fill": "#94A3B8", "lineHeight": 1.4 }
                            ]},
                            { "type": "text", "id": "bb1-l", "name": "L", "content": "Ver analítica de vídeo neural →", "fontSize": 12, "fontWeight": "700", "fill": BLUE_CYAN }
                        ]},
                        # Card 2: Biometría & Torniquetes
                        { "type": "frame", "id": "bbc-2", "name": "C2 Biometria", "width": 432, "height": 260, "cornerRadius": 14, "clip": True, "fill": photo_fill(IMG_BIOMETRIC_TURNSTILE, "#09173855", "#091738F8"), "stroke": BLUE_BORDER_SUBTLE, "strokeWidth": 1.5, "padding": [22, 22], "layout": "vertical", "justifyContent": "space_between", "children": [
                            { "type": "frame", "id": "bb2-tags", "name": "Tags", "layout": "horizontal", "gap": 8, "children": [
                                { "type": "frame", "id": "bt2", "name": "Tag", "padding": [4, 10], "fill": "#06B6D433", "stroke": BLUE_CYAN, "strokeWidth": 1, "cornerRadius": 6, "children": [
                                    { "type": "text", "id": "bt2t", "name": "T", "content": "BIOMETRÍA 3D CONTACTLESS", "fontSize": 10, "fontWeight": "bold", "fill": BLUE_CYAN_LIGHT }
                                ]}
                            ]},
                            { "type": "frame", "id": "bb2-b", "name": "Body", "layout": "vertical", "gap": 6, "children": [
                                { "type": "text", "id": "bb2-t", "name": "T", "content": "Control de Accesos Biométrico y Tornos", "fontSize": 17, "fontWeight": "700", "fill": "#FFFFFF" },
                                { "type": "text", "id": "bb2-d", "name": "D", "content": "Reconocimiento facial 3D, lectores de matrícula LPR y gestión de visitas totalmente automatizada.", "fontSize": 12, "fill": "#94A3B8", "lineHeight": 1.4 }
                            ]},
                            { "type": "text", "id": "bb2-l", "name": "L", "content": "Configurar control de accesos →", "fontSize": 12, "fontWeight": "700", "fill": BLUE_CYAN }
                        ]},
                        # Card 3: CRA SOC
                        { "type": "frame", "id": "bbc-3", "name": "C3 SOC", "width": 432, "height": 260, "cornerRadius": 14, "clip": True, "fill": photo_fill(IMG_CONTROL_ROOM, "#09173855", "#091738F8"), "stroke": BLUE_BORDER_SUBTLE, "strokeWidth": 1.5, "padding": [22, 22], "layout": "vertical", "justifyContent": "space_between", "children": [
                            { "type": "frame", "id": "bb3-tags", "name": "Tags", "layout": "horizontal", "gap": 8, "children": [
                                { "type": "frame", "id": "bt3", "name": "Tag", "padding": [4, 10], "fill": "#D9770633", "stroke": AMBER, "strokeWidth": 1, "cornerRadius": 6, "children": [
                                    { "type": "text", "id": "bt3t", "name": "T", "content": "SOC CYBER 24/7", "fontSize": 10, "fontWeight": "bold", "fill": AMBER_LIGHT }
                                ]}
                            ]},
                            { "type": "frame", "id": "bb3-b", "name": "Body", "layout": "vertical", "gap": 6, "children": [
                                { "type": "text", "id": "bb3-t", "name": "T", "content": "CRA 24/7/365 con Custodia y Acuda", "fontSize": 17, "fontWeight": "700", "fill": "#FFFFFF" },
                                { "type": "text", "id": "bb3-d", "name": "D", "content": "Verificación por vídeo en tiempo real, custodia de llaves y despacho prioritario de patrullas armadas.", "fontSize": 12, "fill": "#94A3B8", "lineHeight": 1.4 }
                            ]},
                            { "type": "text", "id": "bb3-l", "name": "L", "content": "Protocolo de intervención SOC →", "fontSize": 12, "fontWeight": "700", "fill": AMBER_LIGHT }
                        ]}
                    ]},
                    # Row 2 (Grado 3, PCI Servidores, Redes OT)
                    { "type": "frame", "id": "bb-r2", "name": "R2", "layout": "horizontal", "gap": 24, "children": [
                        # Card 4: Grado 3
                        { "type": "frame", "id": "bbc-4", "name": "C4 Grado 3", "width": 432, "height": 260, "cornerRadius": 14, "clip": True, "fill": photo_fill(IMG_WAREHOUSE_NIGHT, "#09173855", "#091738F8"), "stroke": BLUE_BORDER_SUBTLE, "strokeWidth": 1.5, "padding": [22, 22], "layout": "vertical", "justifyContent": "space_between", "children": [
                            { "type": "frame", "id": "bb4-tags", "name": "Tags", "layout": "horizontal", "gap": 8, "children": [
                                { "type": "frame", "id": "bt4", "name": "Tag", "padding": [4, 10], "fill": "#EF444433", "stroke": RED_PRIMARY, "strokeWidth": 1, "cornerRadius": 6, "children": [
                                    { "type": "text", "id": "bt4t", "name": "T", "content": "GRADO 3 HOMOLOGADO", "fontSize": 10, "fontWeight": "bold", "fill": RED_LIGHT }
                                ]}
                            ]},
                            { "type": "frame", "id": "bb4-b", "name": "Body", "layout": "vertical", "gap": 6, "children": [
                                { "type": "text", "id": "bb4-t", "name": "T", "content": "Alarmas Grado 3 e Intrusión Crítica", "fontSize": 17, "fontWeight": "700", "fill": "#FFFFFF" },
                                { "type": "text", "id": "bb4-d", "name": "D", "content": "Sistemas de máxima exigencia legal para joyerías, gasolineras, farmacias y plantas químicas.", "fontSize": 12, "fill": "#94A3B8", "lineHeight": 1.4 }
                            ]},
                            { "type": "text", "id": "bb4-l", "name": "L", "content": "Homologación UNE-EN 50131 →", "fontSize": 12, "fontWeight": "700", "fill": BLUE_CYAN }
                        ]},
                        # Card 5: CPD & PCI
                        { "type": "frame", "id": "bbc-5", "name": "C5 CPD PCI", "width": 432, "height": 260, "cornerRadius": 14, "clip": True, "fill": photo_fill(IMG_SERVER_CPD, "#09173855", "#091738F8"), "stroke": BLUE_BORDER_SUBTLE, "strokeWidth": 1.5, "padding": [22, 22], "layout": "vertical", "justifyContent": "space_between", "children": [
                            { "type": "frame", "id": "bb5-tags", "name": "Tags", "layout": "horizontal", "gap": 8, "children": [
                                { "type": "frame", "id": "bt5", "name": "Tag", "padding": [4, 10], "fill": "#06B6D433", "stroke": BLUE_CYAN, "strokeWidth": 1, "cornerRadius": 6, "children": [
                                    { "type": "text", "id": "bt5t", "name": "T", "content": "PROTECCIÓN DATA CENTER", "fontSize": 10, "fontWeight": "bold", "fill": BLUE_CYAN_LIGHT }
                                ]}
                            ]},
                            { "type": "frame", "id": "bb5-b", "name": "Body", "layout": "vertical", "gap": 6, "children": [
                                { "type": "text", "id": "bb5-t", "name": "T", "content": "Extinción Inocua & PCI para CPDs", "fontSize": 17, "fontWeight": "700", "fill": "#FFFFFF" },
                                { "type": "text", "id": "bb5-d", "name": "D", "content": "Sistemas de extinción mediante gas Novec 1230 / Inergen sin residuo ni daño a la electrónica crítica.", "fontSize": 12, "fill": "#94A3B8", "lineHeight": 1.4 }
                            ]},
                            { "type": "text", "id": "bb5-l", "name": "L", "content": "Soluciones para CPD →", "fontSize": 12, "fontWeight": "700", "fill": BLUE_CYAN }
                        ]},
                        # Card 6: Ciberseguridad OT
                        { "type": "frame", "id": "bbc-6", "name": "C6 Ciber OT", "width": 432, "height": 260, "cornerRadius": 14, "clip": True, "fill": photo_fill(IMG_CONTROL_ROOM, "#09173855", "#091738F8"), "stroke": BLUE_BORDER_SUBTLE, "strokeWidth": 1.5, "padding": [22, 22], "layout": "vertical", "justifyContent": "space_between", "children": [
                            { "type": "frame", "id": "bb6-tags", "name": "Tags", "layout": "horizontal", "gap": 8, "children": [
                                { "type": "frame", "id": "bt6", "name": "Tag", "padding": [4, 10], "fill": "#10B98133", "stroke": EMERALD, "strokeWidth": 1, "cornerRadius": 6, "children": [
                                    { "type": "text", "id": "bt6t", "name": "T", "content": "CIBERSEGURIDAD OT / SCADA", "fontSize": 10, "fontWeight": "bold", "fill": EMERALD_LIGHT }
                                ]}
                            ]},
                            { "type": "frame", "id": "bb6-b", "name": "Body", "layout": "vertical", "gap": 6, "children": [
                                { "type": "text", "id": "bb6-t", "name": "T", "content": "Defensa de Redes Industriales OT", "fontSize": 17, "fontWeight": "700", "fill": "#FFFFFF" },
                                { "type": "text", "id": "bb6-d", "name": "D", "content": "Microsegmentación Zero Trust, detección de intrusiones en bus industrial y blindaje cibernético.", "fontSize": 12, "fill": "#94A3B8", "lineHeight": 1.4 }
                            ]},
                            { "type": "text", "id": "bb6-l", "name": "L", "content": "Consultar arquitectura Zero Trust →", "fontSize": 12, "fontWeight": "700", "fill": BLUE_CYAN }
                        ]}
                    ]}
                ]
            },
            # 6. Protocolo SOC 4 Fases (Blue Workflow)
            {
                "type": "frame", "id": "blue-protocol-sec", "name": "Protocolo de Defensa SOC", "width": "fill_container", "height": 340, "fill": BLUE_SURFACE, "stroke": BLUE_BORDER, "strokeWidth": { "top": 1, "bottom": 1 }, "layout": "vertical", "padding": [48, 48], "gap": 28, "children": [
                    { "type": "frame", "id": "bp-hdr", "name": "Hdr", "layout": "horizontal", "justifyContent": "space_between", "alignItems": "center", "children": [
                        { "type": "frame", "id": "bph-l", "name": "L", "layout": "vertical", "gap": 4, "children": [
                            { "type": "text", "id": "bph-eye", "name": "Eye", "content": "AUTOMATIZACIÓN & RESOLUCIÓN TELEMÁTICA", "fontSize": 11, "fontWeight": "800", "fill": BLUE_CYAN },
                            { "type": "text", "id": "bph-title", "name": "Title", "content": "Pipeline de Detección y Respuesta SOC Ciber-Física", "fontSize": 24, "fontWeight": "800", "fill": "#FFFFFF" }
                        ]},
                        { "type": "text", "id": "bph-time", "name": "Time", "content": "⏱ RESPUESTA SLA PROMETIDA: < 15 SEGUNDOS", "fontSize": 12, "fontWeight": "bold", "fill": BLUE_CYAN_LIGHT }
                    ]},
                    { "type": "frame", "id": "bp-steps", "name": "Steps", "width": "fill_container", "layout": "horizontal", "gap": 16, "children": [
                        # Step 1
                        { "type": "frame", "id": "bps-1", "name": "S1", "width": 320, "height": 160, "fill": "#0B1530", "stroke": BLUE_BORDER, "strokeWidth": 1, "cornerRadius": 10, "padding": [16, 16], "layout": "vertical", "justifyContent": "space_between", "children": [
                            { "type": "frame", "id": "bs1-t", "name": "Top", "width": "fill_container", "layout": "horizontal", "justifyContent": "space_between", "alignItems": "center", "children": [
                                { "type": "text", "id": "bs1-num", "name": "Num", "content": "NIVEL 01", "fontSize": 11, "fontWeight": "800", "fill": BLUE_CYAN },
                                { "type": "text", "id": "bs1-ms", "name": "Ms", "content": "10ms", "fontSize": 11, "fontWeight": "bold", "fill": "#94A3B8" }
                            ]},
                            { "type": "text", "id": "bs1-h", "name": "H", "content": "Telemetría IoT & Sensores", "fontSize": 15, "fontWeight": "700", "fill": "#FFFFFF" },
                            { "type": "text", "id": "bs1-d", "name": "D", "content": "Recopilación de señales en tiempo real desde radares perimetrales, cámaras y lazos inductivos.", "fontSize": 11, "fill": "#94A3B8", "lineHeight": 1.4 }
                        ]},
                        # Step 2
                        { "type": "frame", "id": "bps-2", "name": "S2", "width": 320, "height": 160, "fill": "#0B1530", "stroke": BLUE_BORDER_SUBTLE, "strokeWidth": 1, "cornerRadius": 10, "padding": [16, 16], "layout": "vertical", "justifyContent": "space_between", "children": [
                            { "type": "frame", "id": "bs2-t", "name": "Top", "width": "fill_container", "layout": "horizontal", "justifyContent": "space_between", "alignItems": "center", "children": [
                                { "type": "text", "id": "bs2-num", "name": "Num", "content": "NIVEL 02", "fontSize": 11, "fontWeight": "800", "fill": BLUE_CYAN },
                                { "type": "text", "id": "bs2-ms", "name": "Ms", "content": "0.5s", "fontSize": 11, "fontWeight": "bold", "fill": "#94A3B8" }
                            ]},
                            { "type": "text", "id": "bs2-h", "name": "H", "content": "Inferencia de Visión Neural", "fontSize": 15, "fontWeight": "700", "fill": "#FFFFFF" },
                            { "type": "text", "id": "bs2-d", "name": "D", "content": "Modelos de visión por computador identifican vectores de intrusión y trayectorias críticas.", "fontSize": 11, "fill": "#94A3B8", "lineHeight": 1.4 }
                        ]},
                        # Step 3
                        { "type": "frame", "id": "bps-3", "name": "S3", "width": 320, "height": 160, "fill": "#0B1530", "stroke": BLUE_BORDER_SUBTLE, "strokeWidth": 1, "cornerRadius": 10, "padding": [16, 16], "layout": "vertical", "justifyContent": "space_between", "children": [
                            { "type": "frame", "id": "bs3-t", "name": "Top", "width": "fill_container", "layout": "horizontal", "justifyContent": "space_between", "alignItems": "center", "children": [
                                { "type": "text", "id": "bs3-num", "name": "Num", "content": "NIVEL 03", "fontSize": 11, "fontWeight": "800", "fill": BLUE_CYAN },
                                { "type": "text", "id": "bs3-ms", "name": "Ms", "content": "3.8s", "fontSize": 11, "fontWeight": "bold", "fill": "#94A3B8" }
                            ]},
                            { "type": "text", "id": "bs3-h", "name": "H", "content": "Verificación SOC 24/7", "fontSize": 15, "fontWeight": "700", "fill": "#FFFFFF" },
                            { "type": "text", "id": "bs3-d", "name": "D", "content": "Analistas del SOC confirman vector de ataque y ejecutan medidas de contención automatizadas.", "fontSize": 11, "fill": "#94A3B8", "lineHeight": 1.4 }
                        ]},
                        # Step 4
                        { "type": "frame", "id": "bps-4", "name": "S4", "width": 320, "height": 160, "fill": "#0B1530", "stroke": BLUE_PRIMARY, "strokeWidth": 1.5, "cornerRadius": 10, "padding": [16, 16], "layout": "vertical", "justifyContent": "space_between", "children": [
                            { "type": "frame", "id": "bs4-t", "name": "Top", "width": "fill_container", "layout": "horizontal", "justifyContent": "space_between", "alignItems": "center", "children": [
                                { "type": "text", "id": "bs4-num", "name": "Num", "content": "NIVEL 04", "fontSize": 11, "fontWeight": "800", "fill": BLUE_CYAN_LIGHT },
                                { "type": "text", "id": "bs4-ms", "name": "Ms", "content": "< 15s", "fontSize": 11, "fontWeight": "bold", "fill": EMERALD }
                            ]},
                            { "type": "text", "id": "bs4-h", "name": "H", "content": "Respuesta Policial y Acuda", "fontSize": 15, "fontWeight": "700", "fill": "#FFFFFF" },
                            { "type": "text", "id": "bs4-d", "name": "D", "content": "Despacho inmediato de unidad móvil táctica y canal directo con Fuerzas y Cuerpos de Seguridad.", "fontSize": 11, "fill": "#94A3B8", "lineHeight": 1.4 }
                        ]}
                    ]}
                ]
            },
            # 7. Free Audit CTA Form Card Blue
            {
                "type": "frame", "id": "blue-audit-sec", "name": "Sección Auditoría", "width": "fill_container", "height": 380, "fill": BLUE_BG, "layout": "horizontal", "padding": [48, 64], "alignItems": "center", "justifyContent": "space_between", "children": [
                    { "type": "frame", "id": "blue-aud-l", "name": "Left", "width": 640, "layout": "vertical", "gap": 16, "children": [
                        { "type": "text", "id": "blue-al-eye", "name": "Eye", "content": "VALORACIÓN TECNOLÓGICA Y AUDITORÍA", "fontSize": 12, "fontWeight": "800", "fill": BLUE_CYAN, "letterSpacing": 1 },
                        { "type": "text", "id": "blue-al-title", "name": "Title", "content": "¿Cumple su empresa con el Esquema Nacional de Seguridad y Grado 3 exigido?", "fontSize": 30, "fontWeight": "800", "fill": "#FFFFFF", "lineHeight": 1.2, "textGrowth": "fixed-width", "width": 640 },
                        { "type": "text", "id": "blue-al-desc", "name": "Desc", "content": "Ingenieros de seguridad colegiados realizan un análisis integral de vulnerabilidades, redes OT y cobertura perimetral de CCTV para blindar su empresa.", "fontSize": 14, "fill": "#94A3B8", "lineHeight": 1.5, "textGrowth": "fixed-width", "width": 600 }
                    ]},
                    { "type": "frame", "id": "blue-aud-r", "name": "Form Card", "width": 480, "height": 290, "fill": "#0A142E", "stroke": BLUE_BORDER, "strokeWidth": 1.5, "cornerRadius": 14, "padding": [22, 22], "layout": "vertical", "justifyContent": "space_between", "children": [
                        { "type": "text", "id": "blue-ft-t", "name": "Title", "content": "Solicitar Auditoría Tecnológica de Seguridad", "fontSize": 16, "fontWeight": "700", "fill": "#FFFFFF" },
                        { "type": "frame", "id": "blue-f-f1", "name": "F1", "height": 42, "fill": "#050B1A", "stroke": BLUE_BORDER_SUBTLE, "strokeWidth": 1, "cornerRadius": 6, "padding": [0, 16], "layout": "horizontal", "alignItems": "center", "children": [
                            { "type": "text", "id": "blue-f1-ph", "name": "P", "content": "Nombre de la Empresa o Corporación", "fontSize": 13, "fill": "#64748B" }
                        ]},
                        { "type": "frame", "id": "blue-f-f2", "name": "F2", "height": 42, "fill": "#050B1A", "stroke": BLUE_BORDER_SUBTLE, "strokeWidth": 1, "cornerRadius": 6, "padding": [0, 16], "layout": "horizontal", "alignItems": "center", "children": [
                            { "type": "text", "id": "blue-f2-ph", "name": "P", "content": "Teléfono Directo / Email Corporativo", "fontSize": 13, "fill": "#64748B" }
                        ]},
                        { "type": "frame", "id": "blue-f-btn", "name": "Submit", "height": 46, "fill": BLUE_PRIMARY, "cornerRadius": 8, "alignItems": "center", "justifyContent": "center", "children": [
                            { "type": "text", "id": "blue-fb-txt", "name": "T", "content": "Enviar Solicitud de Auditoría", "fontSize": 14, "fontWeight": "800", "fill": "#FFFFFF" }
                        ]}
                    ]}
                ]
            },
            # 8. Certifications Strip Blue
            {
                "type": "frame", "id": "blue-certs", "name": "Acreditaciones", "width": "fill_container", "height": 100, "fill": "#060D20", "stroke": BLUE_BORDER_SUBTLE, "strokeWidth": { "top": 1, "bottom": 1 }, "layout": "horizontal", "padding": [0, 48], "alignItems": "center", "justifyContent": "space_between", "children": [
                    { "type": "text", "id": "bc-t1", "name": "C1", "content": "🏛 DGP Nº 2341 (MINISTERIO DEL INTERIOR)", "fontSize": 12, "fontWeight": "bold", "fill": "#94A3B8" },
                    { "type": "text", "id": "bc-t2", "name": "C2", "content": "🛡 GRADO 3 (UNE-EN 50131)", "fontSize": 12, "fontWeight": "bold", "fill": "#94A3B8" },
                    { "type": "text", "id": "bc-t3", "name": "C3", "content": "🏅 ISO 27001 / 9001 / 14001 (RINA)", "fontSize": 12, "fontWeight": "bold", "fill": "#94A3B8" },
                    { "type": "text", "id": "bc-t4", "name": "C4", "content": "🔒 ENS NIVEL ALTO CERTIFICADO", "fontSize": 12, "fontWeight": "bold", "fill": "#94A3B8" }
                ]
            },
            # 9. Footer Blue
            {
                "type": "frame", "id": "blue-footer", "name": "Footer", "width": "fill_container", "height": 280, "fill": "#02050E", "layout": "vertical", "padding": [40, 48, 20, 48], "justifyContent": "space_between", "children": [
                    { "type": "frame", "id": "blue-ft-cols", "name": "Cols", "width": "fill_container", "layout": "horizontal", "justifyContent": "space_between", "children": [
                        { "type": "frame", "id": "blue-fc1", "name": "C1", "width": 420, "layout": "vertical", "gap": 10, "children": [
                            { "type": "text", "id": "blue-ftt", "name": "T", "content": "CONTROL 61 · CYBER PHYSICAL DEFENSE", "fontSize": 15, "fontWeight": "800", "fill": "#FFFFFF", "letterSpacing": 1.2 },
                            { "type": "text", "id": "blue-ftd", "name": "D", "content": "Desarrollos y Sistemas Inteligentes S.L. · DGP Nº 2341\nEspecialistas en Grado 3, Visión IA y Cyber SOC 24/7.\nPol. Ind. La Polvorista, Molina de Segura (Murcia)", "fontSize": 12, "fill": "#64748B", "lineHeight": 1.6 }
                        ]},
                        { "type": "frame", "id": "blue-fc2", "name": "C2", "layout": "vertical", "gap": 6, "children": [
                            { "type": "text", "id": "blue-fc2t", "name": "T", "content": "SOLUCIONES CYBER", "fontSize": 11, "fontWeight": "800", "fill": BLUE_CYAN },
                            { "type": "text", "id": "blue-fc2l1", "name": "L1", "content": "Alarmas Homologadas Grado 3", "fontSize": 12, "fill": "#94A3B8" },
                            { "type": "text", "id": "blue-fc2l2", "name": "L2", "content": "CCTV con Visión Artificial Neural", "fontSize": 12, "fill": "#94A3B8" },
                            { "type": "text", "id": "blue-fc2l3", "name": "L3", "content": "Central SOC 24/7", "fontSize": 12, "fill": "#94A3B8" }
                        ]},
                        { "type": "frame", "id": "blue-fc3", "name": "C3", "layout": "vertical", "gap": 6, "children": [
                            { "type": "text", "id": "blue-fc3t", "name": "T", "content": "CENTRAL SOC 24H", "fontSize": 11, "fontWeight": "800", "fill": BLUE_CYAN },
                            { "type": "text", "id": "blue-fc3l1", "name": "L1", "content": "📞 SOC 24h: 968 622 984", "fontSize": 12, "fill": "#FFFFFF", "fontWeight": "bold" },
                            { "type": "text", "id": "blue-fc3l2", "name": "L2", "content": "✉️ info@control61.com", "fontSize": 12, "fill": "#94A3B8" },
                            { "type": "text", "id": "blue-fc3l3", "name": "L3", "content": "📍 Molina de Segura, Murcia", "fontSize": 12, "fill": "#94A3B8" }
                        ]}
                    ]},
                    { "type": "frame", "id": "blue-ft-bot", "name": "Bot", "width": "fill_container", "layout": "horizontal", "justifyContent": "space_between", "alignItems": "center", "children": [
                        { "type": "text", "id": "blue-copy", "name": "Copy", "content": "© 2026 Control 61 Cyber Defense. Todos los derechos reservados.", "fontSize": 11, "fill": "#475569" },
                        { "type": "text", "id": "blue-legal", "name": "Legal", "content": "Aviso Legal · Privacidad · DGP 2341 · ISO 27001", "fontSize": 11, "fill": "#475569" }
                    ]}
                ]
            }
        ]
    }

def main():
    red_frame = build_option_a_red()
    blue_frame = build_option_b_blue()
    
    pen_doc = {
        "version": "2.19",
        "children": [
            red_frame,
            blue_frame
        ]
    }
    
    pen_path = "/Users/toni/Proyectos/Control61-Web/control61_modern_ui.pen"
    with open(pen_path, "w", encoding="utf-8") as f:
        json.dump(pen_doc, f, indent=2, ensure_ascii=False)
    print(f"Written updated pen document to {pen_path}")

    # Now let's sync to Desktop app
    js_code = f"""
    const redNode = {json.dumps(red_frame)};
    const blueNode = {json.dumps(blue_frame)};
    
    // Replace children in canvas
    root.children = [redNode, blueNode];
    Print('Synced both Option A (Red) and Option B (Blue) to Pencil Desktop successfully');
    
    // Export high-res PNGs
    const exp = Export(['OoFpg', 'x6zQ8'], 'png', './exports');
    Print('Exported both frames to ./exports');
    """
    
    cmd_input = f"""execute({{ input: {json.dumps(js_code)} }})\nsave()\nexit()\n"""
    
    env = os.environ.copy()
    env["PEN_CLI_KEY"] = "pencil_cli_aebcdc64faa119be3d732b81edf1af9229f7f20f"
    env["PATH"] = "/Users/toni/.npm-global/bin:/usr/local/bin:/usr/bin:/bin:/usr/sbin:/sbin"
    
    print("Sending live update to Pencil Desktop...")
    try:
        p = subprocess.run(
            ["pen", "interactive", "-a", "desktop", "-i", pen_path],
            input=cmd_input,
            text=True,
            capture_output=True,
            env=env
        )
        print("Desktop Sync STDOUT:", p.stdout)
        print("Desktop Sync STDERR:", p.stderr)
    except Exception as e:
        print("Desktop sync exception:", e)
        
    print("Running headless export to ensure exports directory is fully updated...")
    p_head = subprocess.run(
        ["pen", "interactive", "-i", pen_path, "-o", pen_path],
        input=cmd_input,
        text=True,
        capture_output=True,
        env=env
    )
    print("Headless Export STDOUT:", p_head.stdout)

if __name__ == "__main__":
    main()
