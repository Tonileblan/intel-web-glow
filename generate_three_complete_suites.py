import json
import subprocess
import os
import base64

# =============================================================================
# ASSETS & LOGO
# =============================================================================
LOGO_PATH = "/Users/toni/Proyectos/Control61-Web/src/assets/Logo-Limpio.png"
with open(LOGO_PATH, "rb") as f:
    b64 = base64.b64encode(f.read()).decode("utf-8")
LOGO_DATA_URI = f"data:image/png;base64,{b64}"

# Photography URLs
IMG_CCTV_CAMERA = "https://images.unsplash.com/photo-1557597774-9d273605dfa9?auto=format&fit=crop&w=1600&q=80"
IMG_WAREHOUSE_NIGHT = "https://images.unsplash.com/photo-1586528116311-ad8dd3c8310d?auto=format&fit=crop&w=1600&q=80"
IMG_LOGISTICS_DOCK = "https://images.unsplash.com/photo-1545324418-cc1a3fa10c00?auto=format&fit=crop&w=1600&q=80"
IMG_CONTROL_ROOM = "https://images.unsplash.com/photo-1558494949-ef010cbdcc31?auto=format&fit=crop&w=1600&q=80"
IMG_BIOMETRIC_TURNSTILE = "https://images.unsplash.com/photo-1497366216548-37526070297c?auto=format&fit=crop&w=1600&q=80"
IMG_FIRE_PROTECTION = "https://images.unsplash.com/photo-1517430816045-df4b7de01dbf?auto=format&fit=crop&w=1600&q=80"
IMG_SOLAR_FARM = "https://images.unsplash.com/photo-1509391365360-2e959784a276?auto=format&fit=crop&w=1600&q=80"
IMG_JEWELRY_VAULT = "https://images.unsplash.com/photo-1579546929518-9e396f3cc809?auto=format&fit=crop&w=1600&q=80"
IMG_SERVER_CPD = "https://images.unsplash.com/photo-1558494949-ef010cbdcc31?auto=format&fit=crop&w=1600&q=80"
IMG_OFFICE_HQ = "https://images.unsplash.com/photo-1486406146926-c627a92ad1ab?auto=format&fit=crop&w=1600&q=80"
IMG_SECURITY_TEAM = "https://images.unsplash.com/photo-1521737604893-d14cc237f11d?auto=format&fit=crop&w=1600&q=80"

def photo_fill(img_url, overlay_top="#070A1133", overlay_bot="#070A11F8"):
    return [
        { "type": "image", "url": img_url, "mode": "fill" },
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

def logo_card(size=(140, 44), bg="#FFFFFF"):
    return {
        "type": "frame",
        "name": "Official Control61 Logo",
        "width": size[0],
        "height": size[1],
        "fill": bg,
        "cornerRadius": 6,
        "padding": [4, 8],
        "alignItems": "center",
        "justifyContent": "center",
        "children": [
            {
                "type": "frame",
                "name": "Logo Image",
                "width": "fill_container",
                "height": "fill_container",
                "fill": { "type": "image", "url": LOGO_DATA_URI, "mode": "fit" }
            }
        ]
    }

# Common constants
EMERALD = "#10B981"
EMERALD_LIGHT = "#34D399"
AMBER = "#F59E0B"
AMBER_LIGHT = "#FCD34D"

# =============================================================================
# 🔴 SUITE 1: RED INDUSTRIAL SECURITY & EMERGENCY DEFENSE (Control61.es)
# =============================================================================
RED_BG = "#08090E"
RED_SURFACE = "#11121A"
RED_CARD = "#171824"
RED_PRIMARY = "#DC2626"
RED_ACCENT = "#EF4444"
RED_LIGHT = "#F87171"
RED_BORDER = "#EF44444D"
RED_BORDER_SUBTLE = "#FFFFFF12"

def red_header(active_page="Inicio"):
    navs = ["Inicio", "Nosotros", "Servicios", "Consola CRA", "Contacto"]
    links = []
    for n in navs:
        is_a = (n == active_page)
        links.append({
            "type": "text", "name": n, "content": n,
            "fontSize": 13, "fontWeight": "700" if is_a else "500",
            "fill": RED_ACCENT if is_a else "#94A3B8"
        })
    return {
        "type": "frame", "name": "Header Red", "width": "fill_container", "layout": "vertical", "children": [
            { "type": "frame", "name": "Top Emergency Bar", "width": "fill_container", "height": 38, "fill": "#170A0C", "stroke": RED_BORDER, "strokeWidth": { "bottom": 1 }, "layout": "horizontal", "padding": [0, 48], "alignItems": "center", "justifyContent": "space_between", "children": [
                { "type": "frame", "name": "L", "layout": "horizontal", "gap": 8, "alignItems": "center", "children": [
                    { "type": "ellipse", "name": "Dot", "width": 8, "height": 8, "fill": RED_ACCENT },
                    { "type": "text", "name": "T", "content": "CRA 24/7/365 · HOMOLOGADA GRADO 3 · DGP Nº 2341", "fontSize": 11, "fontWeight": "bold", "fill": "#FCA5A5" }
                ]},
                { "type": "frame", "name": "R", "layout": "horizontal", "gap": 20, "alignItems": "center", "children": [
                    { "type": "text", "name": "P", "content": "🚨 Teléfono 24h: 968 622 984", "fontSize": 12, "fontWeight": "bold", "fill": "#FFFFFF" },
                    { "type": "text", "name": "A", "content": "Acceso Clientes CRA →", "fontSize": 12, "fontWeight": "bold", "fill": RED_ACCENT }
                ]}
            ]},
            { "type": "frame", "name": "Main Nav", "width": "fill_container", "height": 76, "fill": "#10111AEE", "stroke": RED_BORDER_SUBTLE, "strokeWidth": { "bottom": 1 }, "layout": "horizontal", "padding": [0, 48], "alignItems": "center", "justifyContent": "space_between", "children": [
                { "type": "frame", "name": "Brand", "layout": "horizontal", "gap": 12, "alignItems": "center", "children": [
                    logo_card((130, 40)),
                    { "type": "frame", "name": "Claim", "layout": "vertical", "gap": 1, "children": [
                        { "type": "text", "name": "Sub", "content": "SISTEMAS DE SEGURIDAD HOMOLOGADOS", "fontSize": 8, "fontWeight": "700", "fill": "#FCA5A5", "letterSpacing": 0.8 },
                        { "type": "text", "name": "DGP", "content": "DGP Nº 2341 · GRADO 3 UNE-EN 50131", "fontSize": 8, "fill": "#64748B" }
                    ]}
                ]},
                { "type": "frame", "name": "Nav Links", "layout": "horizontal", "gap": 24, "alignItems": "center", "children": links },
                { "type": "frame", "name": "CTA Btn", "height": 40, "padding": [0, 20], "fill": RED_PRIMARY, "cornerRadius": 8, "alignItems": "center", "justifyContent": "center", "children": [
                    { "type": "text", "name": "T", "content": "Solicitar Auditoría 24h", "fontSize": 13, "fontWeight": "700", "fill": "#FFFFFF" }
                ]}
            ]}
        ]
    }

def red_footer():
    return {
        "type": "frame", "name": "Footer Red", "width": "fill_container", "height": 260, "fill": "#06070B", "layout": "vertical", "padding": [36, 48, 16, 48], "justifyContent": "space_between", "children": [
            { "type": "frame", "name": "Cols", "width": "fill_container", "layout": "horizontal", "justifyContent": "space_between", "children": [
                { "type": "frame", "name": "C1", "width": 420, "layout": "vertical", "gap": 8, "children": [
                    logo_card((120, 36)),
                    { "type": "text", "name": "D", "content": "Desarrollos y Sistemas Inteligentes S.L. · DGP Nº 2341\nSistemas Homologados Grado 3 y Central Receptora 24h.\nSede: Pol. Ind. La Polvorista, Molina de Segura (Murcia)", "fontSize": 12, "fill": "#64748B", "lineHeight": 1.5 }
                ]},
                { "type": "frame", "name": "C2", "layout": "vertical", "gap": 6, "children": [
                    { "type": "text", "name": "T", "content": "ESPECIALIDADES", "fontSize": 11, "fontWeight": "800", "fill": RED_ACCENT },
                    { "type": "text", "name": "L1", "content": "Alarmas Homologadas Grado 3", "fontSize": 12, "fill": "#94A3B8" },
                    { "type": "text", "name": "L2", "content": "CCTV Inteligente e IA Perimetral", "fontSize": 12, "fill": "#94A3B8" },
                    { "type": "text", "name": "L3", "content": "Central CRA Propia 24/7", "fontSize": 12, "fill": "#94A3B8" }
                ]},
                { "type": "frame", "name": "C3", "layout": "vertical", "gap": 6, "children": [
                    { "type": "text", "name": "T", "content": "CONTACTO DIRECTO", "fontSize": 11, "fontWeight": "800", "fill": RED_ACCENT },
                    { "type": "text", "name": "L1", "content": "📞 Centralita 24h: 968 622 984", "fontSize": 12, "fontWeight": "bold", "fill": "#FFFFFF" },
                    { "type": "text", "name": "L2", "content": "✉️ info@control61.com", "fontSize": 12, "fill": "#94A3B8" },
                    { "type": "text", "name": "L3", "content": "📍 Molina de Segura, Murcia", "fontSize": 12, "fill": "#94A3B8" }
                ]}
            ]},
            { "type": "frame", "name": "Bot", "width": "fill_container", "layout": "horizontal", "justifyContent": "space_between", "alignItems": "center", "children": [
                { "type": "text", "name": "Copy", "content": "© 2026 Control 61 (Desarrollos y Sistemas Inteligentes S.L.). Todos los derechos reservados.", "fontSize": 11, "fill": "#475569" },
                { "type": "text", "name": "Legal", "content": "DGP 2341 · ISO 9001 / 14001 / 45001 · UNE-EN 50131", "fontSize": 11, "fill": "#475569" }
            ]}
        ]
    }

def build_s1_home(x, y):
    return {
        "type": "frame", "id": "s1-p1-home", "name": "🔴 S1.1: Home Landing (Red Security)",
        "x": x, "y": y, "width": 1440, "height": 3100, "fill": RED_BG, "layout": "vertical", "clip": True, "children": [
            red_header("Inicio"),
            { "type": "frame", "name": "Hero Section", "width": "fill_container", "height": 660, "fill": RED_BG, "layout": "horizontal", "padding": [48, 48], "gap": 40, "alignItems": "center", "justifyContent": "space_between", "children": [
                { "type": "frame", "name": "L", "width": 630, "layout": "vertical", "gap": 20, "children": [
                    { "type": "frame", "name": "Pill", "height": 30, "padding": [0, 12], "fill": "#991B1B33", "stroke": RED_BORDER, "strokeWidth": 1, "cornerRadius": 20, "layout": "horizontal", "gap": 8, "alignItems": "center", "children": [
                        { "type": "icon", "name": "I", "library": "lucide", "icon": "shield-alert", "width": 14, "height": 14, "fill": RED_ACCENT },
                        { "type": "text", "name": "T", "content": "DGP Nº 2341 · CERTIFICACIÓN GRADO 3 HOMOLOGADA", "fontSize": 10, "fontWeight": "bold", "fill": RED_ACCENT }
                    ]},
                    { "type": "text", "name": "H1", "content": "Sistemas de Seguridad Avanzada, Alarmas Grado 3 y CCTV con IA", "fontSize": 42, "fontWeight": "800", "fill": "#FFFFFF", "lineHeight": 1.15 },
                    { "type": "text", "name": "D", "content": "Protección perimetral inteligente para naves, industrias y recintos de alto riesgo en Murcia. Conexión directa con Central Receptora homologada y respuesta inmediata en menos de 15s.", "fontSize": 15, "fill": "#94A3B8", "lineHeight": 1.5 },
                    { "type": "frame", "name": "Btns", "layout": "horizontal", "gap": 16, "children": [
                        { "type": "frame", "name": "CTA", "height": 48, "padding": [0, 24], "fill": RED_PRIMARY, "cornerRadius": 8, "layout": "horizontal", "gap": 8, "alignItems": "center", "children": [
                            { "type": "text", "name": "T", "content": "Diseñar Plan de Seguridad", "fontSize": 14, "fontWeight": "700", "fill": "#FFFFFF" },
                            { "type": "icon", "name": "I", "library": "lucide", "icon": "arrow-up-right", "width": 16, "height": 16, "fill": "#FFFFFF" }
                        ]},
                        { "type": "frame", "name": "Phone", "height": 48, "padding": [0, 20], "fill": "#1E1A20", "stroke": RED_BORDER, "strokeWidth": 1, "cornerRadius": 8, "layout": "horizontal", "gap": 8, "alignItems": "center", "children": [
                            { "type": "icon", "name": "I", "library": "lucide", "icon": "phone", "width": 15, "height": 15, "fill": RED_ACCENT },
                            { "type": "text", "name": "T", "content": "968 622 984 · Averías 24h", "fontSize": 13, "fontWeight": "600", "fill": "#FFFFFF" }
                        ]}
                    ]}
                ]},
                { "type": "frame", "name": "HUD Box", "width": 640, "height": 460, "fill": RED_CARD, "stroke": RED_BORDER, "strokeWidth": 1.5, "cornerRadius": 14, "layout": "vertical", "clip": True, "children": [
                    { "type": "frame", "name": "Hdr", "width": "fill_container", "height": 42, "fill": "#1A0E10", "layout": "horizontal", "padding": [0, 16], "alignItems": "center", "justifyContent": "space_between", "children": [
                        { "type": "text", "name": "T", "content": "CONTROL61_SOC://CRA_GRADO_3 · SUPERVISIÓN ACTIVA", "fontSize": 11, "fontWeight": "bold", "fill": "#FFFFFF" },
                        { "type": "text", "name": "L", "content": "CANAL POLICIAL: 0.8s", "fontSize": 10, "fontWeight": "bold", "fill": RED_ACCENT }
                    ]},
                    { "type": "frame", "name": "Cams", "width": "fill_container", "height": 310, "fill": "#030407", "layout": "horizontal", "gap": 10, "padding": [10, 10], "children": [
                        { "type": "frame", "name": "CAM 1", "width": 305, "height": 290, "cornerRadius": 6, "fill": photo_fill(IMG_WAREHOUSE_NIGHT), "stroke": RED_PRIMARY, "strokeWidth": 2, "padding": [10, 10], "layout": "vertical", "justifyContent": "space_between", "children": [
                            { "type": "text", "name": "T", "content": "CAM-01 · Perímetro Norte [ALERTA]", "fontSize": 11, "fontWeight": "bold", "fill": RED_LIGHT },
                            { "type": "frame", "name": "Box", "height": 100, "fill": "#EF444433", "stroke": RED_PRIMARY, "strokeWidth": 2, "cornerRadius": 4, "padding": [6, 6], "children": [
                                { "type": "text", "name": "W", "content": "⚠️ INTRUSIÓN DETECTADA (99.6%)\nBarrera Láser Sector 3", "fontSize": 10, "fontWeight": "bold", "fill": "#FCA5A5" }
                            ]},
                            { "type": "text", "name": "F", "content": "Aviso a Policía · Acuda ETA: 3m 15s", "fontSize": 10, "fontWeight": "bold", "fill": RED_ACCENT }
                        ]},
                        { "type": "frame", "name": "CAM 2", "width": 305, "height": 290, "cornerRadius": 6, "fill": photo_fill(IMG_LOGISTICS_DOCK), "stroke": EMERALD, "strokeWidth": 1.5, "padding": [10, 10], "layout": "vertical", "justifyContent": "space_between", "children": [
                            { "type": "text", "name": "T", "content": "CAM-02 · Acceso LPR [AUTORIZADO]", "fontSize": 11, "fontWeight": "bold", "fill": EMERALD },
                            { "type": "frame", "name": "Box", "height": 100, "fill": "#10B9811A", "stroke": EMERALD, "strokeWidth": 1.5, "cornerRadius": 4, "padding": [6, 6], "children": [
                                { "type": "text", "name": "W", "content": "MATRÍCULA: 4821-LMR\nFlota Verificada · Barrera Abierta", "fontSize": 10, "fontWeight": "bold", "fill": "#86EFAC" }
                            ]},
                            { "type": "text", "name": "F", "content": "Paso Concedido · Registro Auditado", "fontSize": 10, "fontWeight": "bold", "fill": EMERALD }
                        ]}
                    ]},
                    { "type": "frame", "name": "Ft", "width": "fill_container", "height": 108, "fill": "#140A0C", "layout": "horizontal", "padding": [10, 18], "justifyContent": "space_between", "alignItems": "center", "children": [
                        { "type": "text", "name": "T1", "content": "DOBLE VÍA: Fibra + 5G Anti-Inhibición", "fontSize": 11, "fontWeight": "bold", "fill": RED_ACCENT },
                        { "type": "text", "name": "T2", "content": "POLLING: Cada 30 seg", "fontSize": 11, "fontWeight": "bold", "fill": EMERALD },
                        { "type": "text", "name": "T3", "content": "DGP Nº 2341", "fontSize": 11, "fontWeight": "bold", "fill": AMBER }
                    ]}
                ]}
            ]},
            { "type": "frame", "name": "KPIs", "width": "fill_container", "height": 120, "fill": RED_SURFACE, "stroke": RED_BORDER, "strokeWidth": { "top": 1, "bottom": 1 }, "layout": "horizontal", "padding": [0, 48], "alignItems": "center", "justifyContent": "space_between", "children": [
                { "type": "frame", "name": "K1", "layout": "vertical", "gap": 2, "children": [
                    { "type": "text", "name": "N", "content": "+2.500", "fontSize": 32, "fontWeight": "800", "fill": RED_ACCENT },
                    { "type": "text", "name": "L", "content": "Instalaciones protegidas en el Levante", "fontSize": 12, "fill": "#94A3B8" }
                ]},
                { "type": "frame", "name": "K2", "layout": "vertical", "gap": 2, "children": [
                    { "type": "text", "name": "N", "content": "< 15s", "fontSize": 32, "fontWeight": "800", "fill": "#FFFFFF" },
                    { "type": "text", "name": "L", "content": "Tiempo de respuesta y salto en CRA", "fontSize": 12, "fill": "#94A3B8" }
                ]},
                { "type": "frame", "name": "K3", "layout": "vertical", "gap": 2, "children": [
                    { "type": "text", "name": "N", "content": "99.8%", "fontSize": 32, "fontWeight": "800", "fill": EMERALD },
                    { "type": "text", "name": "L", "content": "Eliminación de falsas alarmas con IA", "fontSize": 12, "fill": "#94A3B8" }
                ]},
                { "type": "frame", "name": "K4", "layout": "vertical", "gap": 2, "children": [
                    { "type": "text", "name": "N", "content": "20+ Años", "fontSize": 32, "fontWeight": "800", "fill": AMBER },
                    { "type": "text", "name": "L", "content": "Líderes en seguridad privada en Murcia", "fontSize": 12, "fill": "#94A3B8" }
                ]}
            ]},
            { "type": "frame", "name": "Bento Grid", "width": "fill_container", "layout": "vertical", "padding": [56, 48], "gap": 24, "children": [
                { "type": "text", "name": "Title", "content": "Ingeniería de Seguridad de Grado 3 Sin Puntos Ciegos", "fontSize": 32, "fontWeight": "800", "fill": "#FFFFFF" },
                { "type": "frame", "name": "Row 1", "layout": "horizontal", "gap": 20, "children": [
                    { "type": "frame", "name": "C1", "width": 433, "height": 240, "cornerRadius": 12, "fill": photo_fill(IMG_WAREHOUSE_NIGHT), "stroke": RED_BORDER, "strokeWidth": 1.5, "padding": [18, 18], "layout": "vertical", "justifyContent": "space_between", "children": [
                        { "type": "text", "name": "Tag", "content": "GRADO 3 UNE-EN 50131", "fontSize": 10, "fontWeight": "bold", "fill": RED_LIGHT },
                        { "type": "text", "name": "T", "content": "Alarmas Grado 3 para Industria y Joyería", "fontSize": 16, "fontWeight": "700", "fill": "#FFFFFF" },
                        { "type": "text", "name": "L", "content": "Ver homologación oficial →", "fontSize": 12, "fontWeight": "bold", "fill": RED_LIGHT }
                    ]},
                    { "type": "frame", "name": "C2", "width": 433, "height": 240, "cornerRadius": 12, "fill": photo_fill(IMG_CCTV_CAMERA), "stroke": RED_BORDER_SUBTLE, "strokeWidth": 1, "padding": [18, 18], "layout": "vertical", "justifyContent": "space_between", "children": [
                        { "type": "text", "name": "Tag", "content": "ÓPTICA 4K IA", "fontSize": 10, "fontWeight": "bold", "fill": EMERALD },
                        { "type": "text", "name": "T", "content": "CCTV Inteligente e IA Perimetral", "fontSize": 16, "fontWeight": "700", "fill": "#FFFFFF" },
                        { "type": "text", "name": "L", "content": "Explorar analítica térmica →", "fontSize": 12, "fontWeight": "bold", "fill": RED_LIGHT }
                    ]},
                    { "type": "frame", "name": "C3", "width": 433, "height": 240, "cornerRadius": 12, "fill": photo_fill(IMG_CONTROL_ROOM), "stroke": RED_BORDER_SUBTLE, "strokeWidth": 1, "padding": [18, 18], "layout": "vertical", "justifyContent": "space_between", "children": [
                        { "type": "text", "name": "Tag", "content": "CENTRAL PROPIA 24/7", "fontSize": 10, "fontWeight": "bold", "fill": AMBER },
                        { "type": "text", "name": "T", "content": "CRA 24/7 con Custodia y Acuda", "fontSize": 16, "fontWeight": "700", "fill": "#FFFFFF" },
                        { "type": "text", "name": "L", "content": "Protocolo de intervención →", "fontSize": 12, "fontWeight": "bold", "fill": AMBER }
                    ]}
                ]}
            ]},
            { "type": "frame", "name": "Auditoría Form", "width": "fill_container", "height": 360, "fill": RED_SURFACE, "layout": "horizontal", "padding": [40, 64], "alignItems": "center", "justifyContent": "space_between", "children": [
                { "type": "frame", "name": "L", "width": 640, "layout": "vertical", "gap": 12, "children": [
                    { "type": "text", "name": "Eye", "content": "AUDITORÍA IN SITU SIN COMPROMISO", "fontSize": 11, "fontWeight": "800", "fill": RED_ACCENT },
                    { "type": "text", "name": "T", "content": "¿Cumple su empresa con la Orden INT/316/2011 y Grado 3?", "fontSize": 28, "fontWeight": "800", "fill": "#FFFFFF" },
                    { "type": "text", "name": "D", "content": "Ingenieros colegiados realizan un análisis integral de vulnerabilidades, ángulos ciegos y vías de comunicación.", "fontSize": 13, "fill": "#94A3B8" }
                ]},
                { "type": "frame", "name": "Form", "width": 460, "height": 260, "fill": "#15090C", "stroke": RED_BORDER, "strokeWidth": 1.5, "cornerRadius": 12, "padding": [20, 20], "layout": "vertical", "justifyContent": "space_between", "children": [
                    { "type": "text", "name": "T", "content": "Solicitar Diagnóstico Técnico In Situ", "fontSize": 15, "fontWeight": "bold", "fill": "#FFFFFF" },
                    { "type": "frame", "name": "F1", "height": 40, "fill": "#08090E", "stroke": RED_BORDER_SUBTLE, "strokeWidth": 1, "cornerRadius": 6, "padding": [0, 14], "layout": "horizontal", "alignItems": "center", "children": [
                        { "type": "text", "name": "P", "content": "Empresa o Nave Industrial", "fontSize": 12, "fill": "#64748B" }
                    ]},
                    { "type": "frame", "name": "F2", "height": 40, "fill": "#08090E", "stroke": RED_BORDER_SUBTLE, "strokeWidth": 1, "cornerRadius": 6, "padding": [0, 14], "layout": "horizontal", "alignItems": "center", "children": [
                        { "type": "text", "name": "P", "content": "Teléfono de Contacto Directo", "fontSize": 12, "fill": "#64748B" }
                    ]},
                    { "type": "frame", "name": "Btn", "height": 44, "fill": RED_PRIMARY, "cornerRadius": 6, "alignItems": "center", "justifyContent": "center", "children": [
                        { "type": "text", "name": "T", "content": "Enviar Solicitud de Auditoría Gratuita", "fontSize": 13, "fontWeight": "bold", "fill": "#FFFFFF" }
                    ]}
                ]}
            ]},
            red_footer()
        ]
    }

def build_s1_nosotros(x, y):
    return {
        "type": "frame", "id": "s1-p2-nosotros", "name": "🔴 S1.2: Sobre Nosotros (Red Security)",
        "x": x, "y": y, "width": 1440, "height": 2000, "fill": RED_BG, "layout": "vertical", "clip": True, "children": [
            red_header("Nosotros"),
            { "type": "frame", "name": "Hero Nosotros", "width": "fill_container", "height": 440, "fill": photo_fill(IMG_SECURITY_TEAM, "#08090E44", "#08090EF8"), "layout": "vertical", "padding": [56, 64], "justifyContent": "center", "gap": 14, "children": [
                { "type": "frame", "name": "Tag", "height": 26, "padding": [0, 12], "fill": "#991B1B4D", "stroke": RED_BORDER, "strokeWidth": 1, "cornerRadius": 14, "alignItems": "center", "children": [
                    { "type": "text", "name": "T", "content": "20+ AÑOS DE LIDERAZGO EN SEGURIDAD PRIVADA", "fontSize": 11, "fontWeight": "bold", "fill": RED_LIGHT }
                ]},
                { "type": "text", "name": "H1", "content": "Ingeniería de Seguridad en Propiedad, Sin Alquileres Ni Permanencias Ocultas", "fontSize": 36, "fontWeight": "800", "fill": "#FFFFFF", "lineHeight": 1.2, "width": 800 },
                { "type": "text", "name": "D", "content": "Desarrollos y Sistemas Inteligentes S.L. (DGP Nº 2341) nació en Molina de Segura con una misión clara: ofrecer a industrias y empresas sistemas de alta seguridad en propiedad, con soporte de ingeniería directa y Central Receptora homologada 24h.", "fontSize": 14, "fill": "#94A3B8", "lineHeight": 1.6, "width": 750 }
            ]},
            { "type": "frame", "name": "Pilares", "width": "fill_container", "layout": "horizontal", "padding": [48, 48], "gap": 24, "children": [
                { "type": "frame", "name": "P1", "width": 433, "height": 260, "fill": RED_SURFACE, "stroke": RED_BORDER, "strokeWidth": 1.5, "cornerRadius": 12, "padding": [22, 22], "layout": "vertical", "gap": 10, "children": [
                    { "type": "icon", "name": "I", "library": "lucide", "icon": "shield-check", "width": 30, "height": 30, "fill": RED_ACCENT },
                    { "type": "text", "name": "T", "content": "Homologación Oficial DGP 2341", "fontSize": 17, "fontWeight": "bold", "fill": "#FFFFFF" },
                    { "type": "text", "name": "D", "content": "Inscritos y homologados por el Ministerio del Interior para la instalación, mantenimiento y conexión a CRA de Grado 3 en todo el territorio nacional.", "fontSize": 12, "fill": "#94A3B8", "lineHeight": 1.5 }
                ]},
                { "type": "frame", "name": "P2", "width": 433, "height": 260, "fill": RED_SURFACE, "stroke": RED_BORDER_SUBTLE, "strokeWidth": 1, "cornerRadius": 12, "padding": [22, 22], "layout": "vertical", "gap": 10, "children": [
                    { "type": "icon", "name": "I", "library": "lucide", "icon": "award", "width": 30, "height": 30, "fill": AMBER },
                    { "type": "text", "name": "T", "content": "Acreditación RINA ISO Triple", "fontSize": 17, "fontWeight": "bold", "fill": "#FFFFFF" },
                    { "type": "text", "name": "D", "content": "Certificaciones ISO 9001 (Calidad), ISO 14001 (Medio Ambiente) e ISO 45001 (Seguridad Laboral) auditadas anualmente por el organismo certificador internacional RINA.", "fontSize": 12, "fill": "#94A3B8", "lineHeight": 1.5 }
                ]},
                { "type": "frame", "name": "P3", "width": 433, "height": 260, "fill": RED_SURFACE, "stroke": RED_BORDER_SUBTLE, "strokeWidth": 1, "cornerRadius": 12, "padding": [22, 22], "layout": "vertical", "gap": 10, "children": [
                    { "type": "icon", "name": "I", "library": "lucide", "icon": "building-2", "width": 30, "height": 30, "fill": EMERALD },
                    { "type": "text", "name": "T", "content": "Sede Central en La Polvorista", "fontSize": 17, "fontWeight": "bold", "fill": "#FFFFFF" },
                    { "type": "text", "name": "D", "content": "Instalaciones propias de más de 1.000m² con centro técnico de pruebas, laboratorio de telecomunicaciones y sala de control CRA 24/7 en Molina de Segura (Murcia).", "fontSize": 12, "fill": "#94A3B8", "lineHeight": 1.5 }
                ]}
            ]},
            { "type": "frame", "name": "Sede Showcase", "width": "fill_container", "height": 380, "fill": RED_SURFACE, "layout": "horizontal", "padding": [36, 48], "gap": 36, "alignItems": "center", "children": [
                { "type": "frame", "name": "Img", "width": 640, "height": 300, "cornerRadius": 12, "fill": photo_fill(IMG_OFFICE_HQ), "stroke": RED_BORDER_SUBTLE, "strokeWidth": 1 },
                { "type": "frame", "name": "Details", "width": 640, "layout": "vertical", "gap": 14, "children": [
                    { "type": "text", "name": "H2", "content": "Infraestructura Técnica Propia y Servicio de Acuda Inmediato", "fontSize": 24, "fontWeight": "800", "fill": "#FFFFFF" },
                    { "type": "text", "name": "D", "content": "A diferencia de comercializadoras que subcontratan la instalación, Control 61 cuenta con plantilla propia de ingenieros colegiados y técnicos de seguridad acreditados por el Ministerio del Interior.", "fontSize": 13, "fill": "#94A3B8", "lineHeight": 1.6 },
                    { "type": "frame", "name": "Badges", "layout": "horizontal", "gap": 16, "children": [
                        { "type": "text", "name": "B1", "content": "✓ Flota de patrullas propias", "fontSize": 12, "fontWeight": "bold", "fill": EMERALD },
                        { "type": "text", "name": "B2", "content": "✓ Custodia de llaves blindada", "fontSize": 12, "fontWeight": "bold", "fill": EMERALD }
                    ]}
                ]}
            ]},
            red_footer()
        ]
    }

def build_s1_servicios(x, y):
    return {
        "type": "frame", "id": "s1-p3-servicios", "name": "🔴 S1.3: Catálogo Servicios (Red Security)",
        "x": x, "y": y, "width": 1440, "height": 2200, "fill": RED_BG, "layout": "vertical", "clip": True, "children": [
            red_header("Servicios"),
            { "type": "frame", "name": "Sec Header", "width": "fill_container", "height": 220, "fill": RED_SURFACE, "layout": "vertical", "padding": [40, 48], "justifyContent": "center", "gap": 8, "children": [
                { "type": "text", "name": "Eye", "content": "CATÁLOGO DE INGENIERÍA Y PROTECCIÓN HOMOLOGADA", "fontSize": 12, "fontWeight": "800", "fill": RED_ACCENT },
                { "type": "text", "name": "H1", "content": "Sistemas Homologados según Normativa UNE-EN 50131", "fontSize": 34, "fontWeight": "800", "fill": "#FFFFFF" },
                { "type": "text", "name": "D", "content": "Diseñamos, instalamos y certificamos soluciones a medida con equipos propios de máxima fiabilidad.", "fontSize": 14, "fill": "#94A3B8" }
            ]},
            { "type": "frame", "name": "Services List", "width": "fill_container", "layout": "vertical", "padding": [40, 48], "gap": 24, "children": [
                { "type": "frame", "name": "S1", "width": "fill_container", "height": 200, "fill": RED_CARD, "stroke": RED_BORDER, "strokeWidth": 1.5, "cornerRadius": 12, "layout": "horizontal", "clip": True, "children": [
                    { "type": "frame", "name": "Img", "width": 320, "height": 200, "fill": photo_fill(IMG_WAREHOUSE_NIGHT) },
                    { "type": "frame", "name": "Body", "width": 970, "padding": [20, 28], "layout": "vertical", "justifyContent": "space_between", "children": [
                        { "type": "frame", "name": "Top", "layout": "horizontal", "justifyContent": "space_between", "children": [
                            { "type": "text", "name": "T", "content": "01. Alarmas Homologadas Grado 3 para Industria y Joyería", "fontSize": 18, "fontWeight": "bold", "fill": "#FFFFFF" },
                            { "type": "text", "name": "Tag", "content": "OBLIGATORIO INT/316/2011", "fontSize": 10, "fontWeight": "bold", "fill": RED_LIGHT }
                        ]},
                        { "type": "text", "name": "D", "content": "Centrales microprocesadas con doble vía de comunicación (Fibra óptica + 5G con supervisión de polling cada 30 segundos). Detección sísmica para cajas fuertes, generadores de niebla de seguridad y detectores microondas de alta inmunidad.", "fontSize": 12, "fill": "#94A3B8", "lineHeight": 1.4 },
                        { "type": "frame", "name": "Specs", "layout": "horizontal", "gap": 20, "children": [
                            { "type": "text", "name": "S1", "content": "✓ Anti-Inhibición con salto 5G", "fontSize": 12, "fontWeight": "bold", "fill": EMERALD },
                            { "type": "text", "name": "S2", "content": "✓ Conexión CRA directa 24/7", "fontSize": 12, "fontWeight": "bold", "fill": EMERALD }
                        ]}
                    ]}
                ]},
                { "type": "frame", "name": "S2", "width": "fill_container", "height": 200, "fill": RED_CARD, "stroke": RED_BORDER_SUBTLE, "strokeWidth": 1, "cornerRadius": 12, "layout": "horizontal", "clip": True, "children": [
                    { "type": "frame", "name": "Img", "width": 320, "height": 200, "fill": photo_fill(IMG_CCTV_CAMERA) },
                    { "type": "frame", "name": "Body", "width": 970, "padding": [20, 28], "layout": "vertical", "justifyContent": "space_between", "children": [
                        { "type": "frame", "name": "Top", "layout": "horizontal", "justifyContent": "space_between", "children": [
                            { "type": "text", "name": "T", "content": "02. CCTV Inteligente con Analítica de Vídeo IA y Cámaras Térmicas", "fontSize": 18, "fontWeight": "bold", "fill": "#FFFFFF" },
                            { "type": "text", "name": "Tag", "content": "ÓPTICA 4K ULTRA HD", "fontSize": 10, "fontWeight": "bold", "fill": EMERALD }
                        ]},
                        { "type": "text", "name": "D", "content": "Cámaras perimetrales térmicas de largo alcance (hasta 1.200m) y cámaras ópticas 4K con chips de inteligencia artificial dedicados a la clasificación en tiempo real de personas, turismos, camiones y lectura LPR de matrículas.", "fontSize": 12, "fill": "#94A3B8", "lineHeight": 1.4 },
                        { "type": "frame", "name": "Specs", "layout": "horizontal", "gap": 20, "children": [
                            { "type": "text", "name": "S1", "content": "✓ 0% Falsas alarmas por viento/animales", "fontSize": 12, "fontWeight": "bold", "fill": EMERALD },
                            { "type": "text", "name": "S2", "content": "✓ Grabación forense 30 días", "fontSize": 12, "fontWeight": "bold", "fill": EMERALD }
                        ]}
                    ]}
                ]},
                { "type": "frame", "name": "S3", "width": "fill_container", "height": 200, "fill": RED_CARD, "stroke": RED_BORDER_SUBTLE, "strokeWidth": 1, "cornerRadius": 12, "layout": "horizontal", "clip": True, "children": [
                    { "type": "frame", "name": "Img", "width": 320, "height": 200, "fill": photo_fill(IMG_CONTROL_ROOM) },
                    { "type": "frame", "name": "Body", "width": 970, "padding": [20, 28], "layout": "vertical", "justifyContent": "space_between", "children": [
                        { "type": "frame", "name": "Top", "layout": "horizontal", "justifyContent": "space_between", "children": [
                            { "type": "text", "name": "T", "content": "03. Central Receptora CRA 24/7 con Custodia de Llaves y Servicio Acuda", "fontSize": 18, "fontWeight": "bold", "fill": "#FFFFFF" },
                            { "type": "text", "name": "Tag", "content": "RESPUESTA < 15 SEGUNDOS", "fontSize": 10, "fontWeight": "bold", "fill": AMBER }
                        ]},
                        { "type": "text", "name": "D", "content": "Supervisión 365 días al año por operadores de seguridad acreditados. Verificación por vídeo en tiempo real y despacho inmediato de patrulla armada con custodia de llaves en caja fuerte blindada para inspección interior.", "fontSize": 12, "fill": "#94A3B8", "lineHeight": 1.4 },
                        { "type": "frame", "name": "Specs", "layout": "horizontal", "gap": 20, "children": [
                            { "type": "text", "name": "S1", "content": "✓ Canal prioritario con Policía Nacional", "fontSize": 12, "fontWeight": "bold", "fill": EMERALD },
                            { "type": "text", "name": "S2", "content": "✓ Informe pericial en cada salto", "fontSize": 12, "fontWeight": "bold", "fill": EMERALD }
                        ]}
                    ]}
                ]}
            ]},
            red_footer()
        ]
    }

def build_s1_webapp_console(x, y):
    return {
        "type": "frame", "id": "s1-p4-webapp-console", "name": "🔴 S1.4: Web App Console CRA (Red Security)",
        "x": x, "y": y, "width": 1440, "height": 1024, "fill": "#0A0B10", "layout": "horizontal", "clip": True, "children": [
            { "type": "frame", "name": "Sidebar App", "width": 240, "height": 1024, "fill": "#11121A", "stroke": RED_BORDER_SUBTLE, "strokeWidth": { "right": 1 }, "layout": "vertical", "padding": [20, 16], "justifyContent": "space_between", "children": [
                { "type": "frame", "name": "Top", "layout": "vertical", "gap": 24, "children": [
                    logo_card((160, 42)),
                    { "type": "frame", "name": "Nav Items", "layout": "vertical", "gap": 8, "children": [
                        { "type": "frame", "name": "Item 1 Active", "height": 40, "fill": "#EF444426", "stroke": RED_BORDER, "strokeWidth": 1, "cornerRadius": 8, "padding": [0, 12], "layout": "horizontal", "gap": 10, "alignItems": "center", "children": [
                            { "type": "icon", "name": "I", "library": "lucide", "icon": "layout-dashboard", "width": 18, "height": 18, "fill": RED_ACCENT },
                            { "type": "text", "name": "T", "content": "Panel Principal", "fontSize": 13, "fontWeight": "bold", "fill": "#FFFFFF" }
                        ]},
                        { "type": "frame", "name": "Item 2", "height": 40, "padding": [0, 12], "layout": "horizontal", "gap": 10, "alignItems": "center", "children": [
                            { "type": "icon", "name": "I", "library": "lucide", "icon": "video", "width": 18, "height": 18, "fill": "#64748B" },
                            { "type": "text", "name": "T", "content": "Cámaras en Directo", "fontSize": 13, "fill": "#94A3B8" }
                        ]},
                        { "type": "frame", "name": "Item 3", "height": 40, "padding": [0, 12], "layout": "horizontal", "gap": 10, "alignItems": "center", "children": [
                            { "type": "icon", "name": "I", "library": "lucide", "icon": "shield-check", "width": 18, "height": 18, "fill": "#64748B" },
                            { "type": "text", "name": "T", "content": "Zonas y Particiones", "fontSize": 13, "fill": "#94A3B8" }
                        ]},
                        { "type": "frame", "name": "Item 4", "height": 40, "padding": [0, 12], "layout": "horizontal", "gap": 10, "alignItems": "center", "children": [
                            { "type": "icon", "name": "I", "library": "lucide", "icon": "file-text", "width": 18, "height": 18, "fill": "#64748B" },
                            { "type": "text", "name": "T", "content": "Histórico de Eventos", "fontSize": 13, "fill": "#94A3B8" }
                        ]}
                    ]}
                ]},
                { "type": "frame", "name": "User Box", "height": 56, "fill": "#181924", "cornerRadius": 8, "padding": [8, 12], "layout": "horizontal", "gap": 10, "alignItems": "center", "children": [
                    { "type": "ellipse", "name": "Avatar", "width": 34, "height": 34, "fill": RED_PRIMARY },
                    { "type": "frame", "name": "Txt", "layout": "vertical", "gap": 2, "children": [
                        { "type": "text", "name": "Name", "content": "Ing. A. Martínez", "fontSize": 12, "fontWeight": "bold", "fill": "#FFFFFF" },
                        { "type": "text", "name": "Role", "content": "Dir. Seguridad (Sede A)", "fontSize": 10, "fill": "#94A3B8" }
                    ]}
                ]}
            ]},
            { "type": "frame", "name": "Main App Content", "width": 1200, "height": 1024, "layout": "vertical", "children": [
                { "type": "frame", "name": "Topbar App", "width": "fill_container", "height": 68, "fill": "#11121A", "stroke": RED_BORDER_SUBTLE, "strokeWidth": { "bottom": 1 }, "layout": "horizontal", "padding": [0, 32], "alignItems": "center", "justifyContent": "space_between", "children": [
                    { "type": "frame", "name": "Sede Selector", "layout": "horizontal", "gap": 12, "alignItems": "center", "children": [
                        { "type": "text", "name": "Sede", "content": "🏢 Sede Central - Pol. Ind. La Polvorista (Murcia)", "fontSize": 14, "fontWeight": "bold", "fill": "#FFFFFF" },
                        { "type": "frame", "name": "Status Pill", "padding": [4, 10], "fill": "#10B98126", "stroke": EMERALD, "strokeWidth": 1, "cornerRadius": 12, "children": [
                            { "type": "text", "name": "T", "content": "● CONEXIÓN CRA ACTIVA", "fontSize": 10, "fontWeight": "bold", "fill": "#86EFAC" }
                        ]}
                    ]},
                    { "type": "frame", "name": "App Actions", "layout": "horizontal", "gap": 16, "alignItems": "center", "children": [
                        { "type": "frame", "name": "Arm Button", "height": 38, "padding": [0, 16], "fill": "#EF444433", "stroke": RED_PRIMARY, "strokeWidth": 1.5, "cornerRadius": 6, "layout": "horizontal", "gap": 8, "alignItems": "center", "children": [
                            { "type": "icon", "name": "I", "library": "lucide", "icon": "shield-alert", "width": 16, "height": 16, "fill": RED_ACCENT },
                            { "type": "text", "name": "T", "content": "ARMADO TOTAL GRADO 3", "fontSize": 12, "fontWeight": "bold", "fill": "#FFFFFF" }
                        ]},
                        { "type": "frame", "name": "SOS Btn", "height": 38, "padding": [0, 16], "fill": RED_PRIMARY, "cornerRadius": 6, "alignItems": "center", "justifyContent": "center", "children": [
                            { "type": "text", "name": "T", "content": "🚨 BOTÓN SOS POLICÍA", "fontSize": 12, "fontWeight": "800", "fill": "#FFFFFF" }
                        ]}
                    ]}
                ]},
                { "type": "frame", "name": "App Workspace Grid", "width": "fill_container", "layout": "horizontal", "padding": [24, 32], "gap": 24, "children": [
                    { "type": "frame", "name": "Cam Grid 2x2", "width": 780, "height": 860, "layout": "vertical", "gap": 16, "children": [
                        { "type": "frame", "name": "Row 1", "layout": "horizontal", "gap": 16, "children": [
                            { "type": "frame", "name": "C1", "width": 382, "height": 260, "cornerRadius": 8, "fill": photo_fill(IMG_WAREHOUSE_NIGHT), "stroke": RED_PRIMARY, "strokeWidth": 2, "padding": [10, 10], "layout": "vertical", "justifyContent": "space_between", "children": [
                                { "type": "text", "name": "T", "content": "CAM-01 · Perímetro Norte [ALERTA]", "fontSize": 11, "fontWeight": "bold", "fill": RED_LIGHT },
                                { "type": "frame", "name": "Box", "height": 80, "fill": "#EF444433", "stroke": RED_PRIMARY, "strokeWidth": 1.5, "cornerRadius": 4, "padding": [6, 6], "children": [
                                    { "type": "text", "name": "W", "content": "⚠️ INTRUSIÓN 99.6% · BARRERA LÁSER", "fontSize": 9, "fontWeight": "bold", "fill": "#FCA5A5" }
                                ]},
                                { "type": "text", "name": "F", "content": "Acuda Despachado · ETA: 3m 15s", "fontSize": 10, "fontWeight": "bold", "fill": RED_ACCENT }
                            ]},
                            { "type": "frame", "name": "C2", "width": 382, "height": 260, "cornerRadius": 8, "fill": photo_fill(IMG_LOGISTICS_DOCK), "stroke": EMERALD, "strokeWidth": 1.5, "padding": [10, 10], "layout": "vertical", "justifyContent": "space_between", "children": [
                                { "type": "text", "name": "T", "content": "CAM-02 · Muelle LPR [AUTORIZADO]", "fontSize": 11, "fontWeight": "bold", "fill": EMERALD },
                                { "type": "frame", "name": "Box", "height": 80, "fill": "#10B9811A", "stroke": EMERALD, "strokeWidth": 1, "cornerRadius": 4, "padding": [6, 6], "children": [
                                    { "type": "text", "name": "W", "content": "MATRÍCULA 4821-LMR [Flota]", "fontSize": 9, "fontWeight": "bold", "fill": "#86EFAC" }
                                ]},
                                { "type": "text", "name": "F", "content": "Barrera Abierta · Registro OK", "fontSize": 10, "fontWeight": "bold", "fill": EMERALD }
                            ]}
                        ]},
                        { "type": "frame", "name": "Row 2", "layout": "horizontal", "gap": 16, "children": [
                            { "type": "frame", "name": "C3", "width": 382, "height": 260, "cornerRadius": 8, "fill": photo_fill(IMG_BIOMETRIC_TURNSTILE), "stroke": RED_BORDER_SUBTLE, "strokeWidth": 1, "padding": [10, 10], "layout": "vertical", "justifyContent": "space_between", "children": [
                                { "type": "text", "name": "T", "content": "CAM-03 · Torniquetes Entrada", "fontSize": 11, "fontWeight": "bold", "fill": "#FFFFFF" },
                                { "type": "text", "name": "F", "content": "Reconocimiento Facial 3D Activo", "fontSize": 10, "fill": "#94A3B8" }
                            ]},
                            { "type": "frame", "name": "C4", "width": 382, "height": 260, "cornerRadius": 8, "fill": photo_fill(IMG_FIRE_PROTECTION), "stroke": RED_BORDER_SUBTLE, "strokeWidth": 1, "padding": [10, 10], "layout": "vertical", "justifyContent": "space_between", "children": [
                                { "type": "text", "name": "T", "content": "CAM-04 · Sala Técnica PCI", "fontSize": 11, "fontWeight": "bold", "fill": "#FFFFFF" },
                                { "type": "text", "name": "F", "content": "Sensores Térmicos: 21°C Normal", "fontSize": 10, "fill": "#94A3B8" }
                            ]}
                        ]}
                    ]},
                    { "type": "frame", "name": "Zonas Panel", "width": 330, "height": 860, "layout": "vertical", "gap": 16, "children": [
                        { "type": "frame", "name": "Card Partitions", "width": "fill_container", "height": 280, "fill": RED_CARD, "stroke": RED_BORDER_SUBTLE, "strokeWidth": 1, "cornerRadius": 10, "padding": [16, 16], "layout": "vertical", "justifyContent": "space_between", "children": [
                            { "type": "text", "name": "T", "content": "Estado de Particiones (8 Zonas)", "fontSize": 13, "fontWeight": "bold", "fill": "#FFFFFF" },
                            { "type": "frame", "name": "Z1", "layout": "horizontal", "justifyContent": "space_between", "children": [
                                { "type": "text", "name": "L", "content": "Z1. Perímetro Exterior", "fontSize": 12, "fill": "#CBD5E1" },
                                { "type": "text", "name": "S", "content": "ARMADO", "fontSize": 11, "fontWeight": "bold", "fill": RED_ACCENT }
                            ]},
                            { "type": "frame", "name": "Z2", "layout": "horizontal", "justifyContent": "space_between", "children": [
                                { "type": "text", "name": "L", "content": "Z2. Naves Almacén A-B", "fontSize": 12, "fill": "#CBD5E1" },
                                { "type": "text", "name": "S", "content": "ARMADO", "fontSize": 11, "fontWeight": "bold", "fill": RED_ACCENT }
                            ]},
                            { "type": "frame", "name": "Z3", "layout": "horizontal", "justifyContent": "space_between", "children": [
                                { "type": "text", "name": "L", "content": "Z3. Oficinas y Administración", "fontSize": 12, "fill": "#CBD5E1" },
                                { "type": "text", "name": "S", "content": "DESARMADO", "fontSize": 11, "fontWeight": "bold", "fill": EMERALD }
                            ]},
                            { "type": "frame", "name": "Z4", "layout": "horizontal", "justifyContent": "space_between", "children": [
                                { "type": "text", "name": "L", "content": "Z4. Sala Servidores CPD", "fontSize": 12, "fill": "#CBD5E1" },
                                { "type": "text", "name": "S", "content": "24H ACTIVO", "fontSize": 11, "fontWeight": "bold", "fill": AMBER }
                            ]}
                        ]},
                        { "type": "frame", "name": "Card Event Log", "width": "fill_container", "height": 260, "fill": RED_CARD, "stroke": RED_BORDER_SUBTLE, "strokeWidth": 1, "cornerRadius": 10, "padding": [16, 16], "layout": "vertical", "justifyContent": "space_between", "children": [
                            { "type": "text", "name": "T", "content": "Log de Eventos en Tiempo Real", "fontSize": 13, "fontWeight": "bold", "fill": "#FFFFFF" },
                            { "type": "text", "name": "E1", "content": "11:58:12 · Intrusión Perímetro Norte (CAM-01)", "fontSize": 11, "fill": "#FCA5A5" },
                            { "type": "text", "name": "E2", "content": "11:55:04 · Acceso LPR Concedido (4821-LMR)", "fontSize": 11, "fill": "#86EFAC" },
                            { "type": "text", "name": "E3", "content": "11:42:19 · Test de Polling CRA OK (Doble Vía)", "fontSize": 11, "fill": "#94A3B8" }
                        ]}
                    ]}
                ]}
            ]}
        ]
    }

def build_s1_contacto(x, y):
    return {
        "type": "frame", "id": "s1-p5-contacto", "name": "🔴 S1.5: Contacto & Sede (Red Security)",
        "x": x, "y": y, "width": 1440, "height": 1400, "fill": RED_BG, "layout": "vertical", "clip": True, "children": [
            red_header("Contacto"),
            { "type": "frame", "name": "Hero Contact", "width": "fill_container", "height": 260, "fill": RED_SURFACE, "layout": "vertical", "padding": [40, 48], "justifyContent": "center", "gap": 8, "children": [
                { "type": "text", "name": "Eye", "content": "ATENCIÓN TÉCNICA Y AUDITORÍAS EN EL LEVANTE", "fontSize": 12, "fontWeight": "800", "fill": RED_ACCENT },
                { "type": "text", "name": "H1", "content": "Contacto Directo con Ingenieros Homologados", "fontSize": 34, "fontWeight": "800", "fill": "#FFFFFF" },
                { "type": "text", "name": "D", "content": "Centralita 24h para averías, asesoría técnica in situ y proyectos de ingeniería de seguridad Grado 3.", "fontSize": 14, "fill": "#94A3B8" }
            ]},
            { "type": "frame", "name": "Contact Grid", "width": "fill_container", "layout": "horizontal", "padding": [40, 48], "gap": 32, "children": [
                { "type": "frame", "name": "Cards Col", "width": 540, "layout": "vertical", "gap": 18, "children": [
                    { "type": "frame", "name": "C1 Phone", "height": 120, "fill": RED_CARD, "stroke": RED_BORDER, "strokeWidth": 1.5, "cornerRadius": 10, "padding": [18, 20], "layout": "vertical", "gap": 4, "children": [
                        { "type": "text", "name": "T", "content": "🚨 Teléfono Centralita y Averías 24 Horas", "fontSize": 13, "fontWeight": "bold", "fill": RED_ACCENT },
                        { "type": "text", "name": "P", "content": "968 622 984", "fontSize": 22, "fontWeight": "800", "fill": "#FFFFFF" },
                        { "type": "text", "name": "S", "content": "Atención inmediata por operador CRA de guardia.", "fontSize": 11, "fill": "#94A3B8" }
                    ]},
                    { "type": "frame", "name": "C2 Sede", "height": 120, "fill": RED_CARD, "stroke": RED_BORDER_SUBTLE, "strokeWidth": 1, "cornerRadius": 10, "padding": [18, 20], "layout": "vertical", "gap": 4, "children": [
                        { "type": "text", "name": "T", "content": "📍 Sede Central e Instalaciones Propias", "fontSize": 13, "fontWeight": "bold", "fill": "#FFFFFF" },
                        { "type": "text", "name": "P", "content": "Polígono Industrial La Polvorista", "fontSize": 15, "fontWeight": "700", "fill": "#FFFFFF" },
                        { "type": "text", "name": "S", "content": "30500 Molina de Segura (Murcia, España)", "fontSize": 11, "fill": "#94A3B8" }
                    ]}
                ]},
                { "type": "frame", "name": "Form Container", "width": 770, "height": 400, "fill": RED_SURFACE, "stroke": RED_BORDER, "strokeWidth": 1.5, "cornerRadius": 12, "padding": [28, 28], "layout": "vertical", "justifyContent": "space_between", "children": [
                    { "type": "text", "name": "H2", "content": "Solicitar Auditoría de Seguridad Sin Compromiso", "fontSize": 18, "fontWeight": "bold", "fill": "#FFFFFF" },
                    { "type": "frame", "name": "F1", "height": 42, "fill": RED_BG, "stroke": RED_BORDER_SUBTLE, "strokeWidth": 1, "cornerRadius": 6, "padding": [0, 16], "layout": "horizontal", "alignItems": "center", "children": [
                        { "type": "text", "name": "P", "content": "Nombre y Apellidos del Solicitante", "fontSize": 12, "fill": "#64748B" }
                    ]},
                    { "type": "frame", "name": "F2", "height": 42, "fill": RED_BG, "stroke": RED_BORDER_SUBTLE, "strokeWidth": 1, "cornerRadius": 6, "padding": [0, 16], "layout": "horizontal", "alignItems": "center", "children": [
                        { "type": "text", "name": "P", "content": "Empresa / Razón Social / Sector", "fontSize": 12, "fill": "#64748B" }
                    ]},
                    { "type": "frame", "name": "Submit", "height": 46, "fill": RED_PRIMARY, "cornerRadius": 6, "alignItems": "center", "justifyContent": "center", "children": [
                        { "type": "text", "name": "T", "content": "Enviar y Solicitar Visita Técnica Gratuita", "fontSize": 13, "fontWeight": "bold", "fill": "#FFFFFF" }
                    ]}
                ]}
            ]},
            red_footer()
        ]
    }

# =============================================================================
# 🔵 SUITE 2: CYBER SOC & AI INTELLIGENCE OPERATIONS (Cobalt Blue & Cyan)
# =============================================================================
BLUE_BG = "#030712"
BLUE_SURFACE = "#081126"
BLUE_CARD = "#0D1B3A"
BLUE_PRIMARY = "#2563EB"
BLUE_ACCENT = "#3B82F6"
BLUE_CYAN = "#06B6D4"
BLUE_CYAN_LIGHT = "#22D3EE"
BLUE_BORDER = "#3B82F64D"
BLUE_BORDER_SUBTLE = "#FFFFFF14"

def blue_header(active_page="Inicio"):
    navs = ["Inicio", "Centro SOC", "Soluciones", "SOC Portal", "Contacto"]
    links = []
    for n in navs:
        is_a = (n == active_page)
        links.append({
            "type": "text", "name": n, "content": n,
            "fontSize": 13, "fontWeight": "700" if is_a else "500",
            "fill": BLUE_CYAN if is_a else "#94A3B8"
        })
    return {
        "type": "frame", "name": "Header Blue", "width": "fill_container", "layout": "vertical", "children": [
            { "type": "frame", "name": "Top SOC Bar", "width": "fill_container", "height": 38, "fill": "#060D1E", "stroke": BLUE_BORDER, "strokeWidth": { "bottom": 1 }, "layout": "horizontal", "padding": [0, 48], "alignItems": "center", "justifyContent": "space_between", "children": [
                { "type": "frame", "name": "L", "layout": "horizontal", "gap": 8, "alignItems": "center", "children": [
                    { "type": "ellipse", "name": "Dot", "width": 8, "height": 8, "fill": BLUE_CYAN },
                    { "type": "text", "name": "T", "content": "SOC CYBER OPERATIONS · CIFRADO E2E AES-256 · DGP Nº 2341 · ENS NIVEL ALTO", "fontSize": 11, "fontWeight": "bold", "fill": BLUE_CYAN_LIGHT }
                ]},
                { "type": "frame", "name": "R", "layout": "horizontal", "gap": 20, "alignItems": "center", "children": [
                    { "type": "text", "name": "P", "content": "🛰️ Línea Directa SOC: 968 622 984", "fontSize": 12, "fontWeight": "bold", "fill": "#FFFFFF" },
                    { "type": "text", "name": "A", "content": "Portal Cyber SOC →", "fontSize": 12, "fontWeight": "bold", "fill": BLUE_CYAN }
                ]}
            ]},
            { "type": "frame", "name": "Main Nav", "width": "fill_container", "height": 76, "fill": "#081126EE", "stroke": BLUE_BORDER_SUBTLE, "strokeWidth": { "bottom": 1 }, "layout": "horizontal", "padding": [0, 48], "alignItems": "center", "justifyContent": "space_between", "children": [
                { "type": "frame", "name": "Brand", "layout": "horizontal", "gap": 12, "alignItems": "center", "children": [
                    logo_card((130, 40)),
                    { "type": "frame", "name": "Claim", "layout": "vertical", "gap": 1, "children": [
                        { "type": "text", "name": "Sub", "content": "CYBER PHYSICAL DEFENSE & SOC", "fontSize": 8, "fontWeight": "700", "fill": BLUE_CYAN, "letterSpacing": 0.8 },
                        { "type": "text", "name": "DGP", "content": "DGP Nº 2341 · ENS NIVEL ALTO CERTIFICADO", "fontSize": 8, "fill": "#64748B" }
                    ]}
                ]},
                { "type": "frame", "name": "Nav Links", "layout": "horizontal", "gap": 24, "alignItems": "center", "children": links },
                { "type": "frame", "name": "CTA Btn", "height": 40, "padding": [0, 20], "fill": BLUE_PRIMARY, "cornerRadius": 8, "alignItems": "center", "justifyContent": "center", "children": [
                    { "type": "text", "name": "T", "content": "Auditoría Tecnológica", "fontSize": 13, "fontWeight": "700", "fill": "#FFFFFF" }
                ]}
            ]}
        ]
    }

def blue_footer():
    return {
        "type": "frame", "name": "Footer Blue", "width": "fill_container", "height": 260, "fill": "#02050E", "layout": "vertical", "padding": [36, 48, 16, 48], "justifyContent": "space_between", "children": [
            { "type": "frame", "name": "Cols", "width": "fill_container", "layout": "horizontal", "justifyContent": "space_between", "children": [
                { "type": "frame", "name": "C1", "width": 420, "layout": "vertical", "gap": 8, "children": [
                    logo_card((120, 36)),
                    { "type": "text", "name": "D", "content": "Desarrollos y Sistemas Inteligentes S.L. · DGP Nº 2341\nEspecialistas en Grado 3, Visión Neural y Cyber SOC 24/7.\nSede: Pol. Ind. La Polvorista, Molina de Segura (Murcia)", "fontSize": 12, "fill": "#64748B", "lineHeight": 1.5 }
                ]},
                { "type": "frame", "name": "C2", "layout": "vertical", "gap": 6, "children": [
                    { "type": "text", "name": "T", "content": "SOLUCIONES CYBER", "fontSize": 11, "fontWeight": "800", "fill": BLUE_CYAN },
                    { "type": "text", "name": "L1", "content": "Alarmas Homologadas Grado 3", "fontSize": 12, "fill": "#94A3B8" },
                    { "type": "text", "name": "L2", "content": "CCTV con Visión Artificial Neural", "fontSize": 12, "fill": "#94A3B8" },
                    { "type": "text", "name": "L3", "content": "Central SOC 24/7 E2E", "fontSize": 12, "fill": "#94A3B8" }
                ]},
                { "type": "frame", "name": "C3", "layout": "vertical", "gap": 6, "children": [
                    { "type": "text", "name": "T", "content": "CENTRAL SOC 24H", "fontSize": 11, "fontWeight": "800", "fill": BLUE_CYAN },
                    { "type": "text", "name": "L1", "content": "📞 SOC Directo: 968 622 984", "fontSize": 12, "fontWeight": "bold", "fill": "#FFFFFF" },
                    { "type": "text", "name": "L2", "content": "✉️ info@control61.com", "fontSize": 12, "fill": "#94A3B8" }
                ]}
            ]},
            { "type": "frame", "name": "Bot", "width": "fill_container", "layout": "horizontal", "justifyContent": "space_between", "alignItems": "center", "children": [
                { "type": "text", "name": "Copy", "content": "© 2026 Control 61 Cyber Defense. Todos los derechos reservados.", "fontSize": 11, "fill": "#475569" },
                { "type": "text", "name": "Legal", "content": "DGP Nº 2341 · ISO 27001 / ISO 9001 · ENS Nivel Alto", "fontSize": 11, "fill": "#475569" }
            ]}
        ]
    }

def build_s2_home(x, y):
    return {
        "type": "frame", "id": "s2-p1-home", "name": "🔵 S2.1: Home Landing (Cobalt SOC)",
        "x": x, "y": y, "width": 1440, "height": 3100, "fill": BLUE_BG, "layout": "vertical", "clip": True, "children": [
            blue_header("Inicio"),
            { "type": "frame", "name": "Hero Section", "width": "fill_container", "height": 660, "fill": BLUE_BG, "layout": "horizontal", "padding": [48, 48], "gap": 40, "alignItems": "center", "justifyContent": "space_between", "children": [
                { "type": "frame", "name": "L", "width": 630, "layout": "vertical", "gap": 20, "children": [
                    { "type": "frame", "name": "Pill", "height": 30, "padding": [0, 12], "fill": "#1E3A8A26", "stroke": BLUE_BORDER, "strokeWidth": 1, "cornerRadius": 20, "layout": "horizontal", "gap": 8, "alignItems": "center", "children": [
                        { "type": "icon", "name": "I", "library": "lucide", "icon": "cpu", "width": 14, "height": 14, "fill": BLUE_CYAN },
                        { "type": "text", "name": "T", "content": "DEFENSA CIBER-FÍSICA DE GRADO MILITAR · DGP 2341", "fontSize": 10, "fontWeight": "bold", "fill": BLUE_CYAN }
                    ]},
                    { "type": "text", "name": "H1", "content": "Seguridad Electrónica de Grado Militar, Visión IA y Centro SOC 24/7", "fontSize": 42, "fontWeight": "800", "fill": "#FFFFFF", "lineHeight": 1.15 },
                    { "type": "text", "name": "D", "content": "Protección total para infraestructuras críticas, plantas industriales y CPDs. Doble vía cifrada AES-256, telemetría continua y resolución de alertas en tiempo real.", "fontSize": 15, "fill": "#94A3B8", "lineHeight": 1.5 },
                    { "type": "frame", "name": "Btns", "layout": "horizontal", "gap": 16, "children": [
                        { "type": "frame", "name": "CTA", "height": 48, "padding": [0, 24], "fill": BLUE_PRIMARY, "cornerRadius": 8, "layout": "horizontal", "gap": 8, "alignItems": "center", "children": [
                            { "type": "text", "name": "T", "content": "Conectar con SOC Control 61", "fontSize": 14, "fontWeight": "700", "fill": "#FFFFFF" },
                            { "type": "icon", "name": "I", "library": "lucide", "icon": "arrow-up-right", "width": 16, "height": 16, "fill": "#FFFFFF" }
                        ]},
                        { "type": "frame", "name": "Demo", "height": 48, "padding": [0, 20], "fill": "#0E1A38", "stroke": BLUE_BORDER, "strokeWidth": 1.5, "cornerRadius": 8, "layout": "horizontal", "gap": 8, "alignItems": "center", "children": [
                            { "type": "icon", "name": "I", "library": "lucide", "icon": "terminal", "width": 15, "height": 15, "fill": BLUE_CYAN },
                            { "type": "text", "name": "T", "content": "Ver Demostración SOC", "fontSize": 13, "fontWeight": "600", "fill": "#F1F5F9" }
                        ]}
                    ]}
                ]},
                { "type": "frame", "name": "HUD Box", "width": 640, "height": 460, "fill": BLUE_CARD, "stroke": BLUE_BORDER, "strokeWidth": 1.5, "cornerRadius": 14, "layout": "vertical", "clip": True, "children": [
                    { "type": "frame", "name": "Hdr", "width": "fill_container", "height": 42, "fill": "#0A1736", "layout": "horizontal", "padding": [0, 16], "alignItems": "center", "justifyContent": "space_between", "children": [
                        { "type": "text", "name": "T", "content": "CYBER_SOC://STREAM_MATRIX_4K · CIFRADO E2E", "fontSize": 11, "fontWeight": "bold", "fill": "#FFFFFF" },
                        { "type": "text", "name": "L", "content": "LATENCIA RED: 8ms (FIBRA 10Gb)", "fontSize": 10, "fontWeight": "bold", "fill": BLUE_CYAN }
                    ]},
                    { "type": "frame", "name": "Cams", "width": "fill_container", "height": 310, "fill": "#020713", "layout": "horizontal", "gap": 10, "padding": [10, 10], "children": [
                        { "type": "frame", "name": "CAM 1", "width": 305, "height": 290, "cornerRadius": 6, "fill": photo_fill(IMG_CONTROL_ROOM), "stroke": BLUE_CYAN, "strokeWidth": 2, "padding": [10, 10], "layout": "vertical", "justifyContent": "space_between", "children": [
                            { "type": "text", "name": "T", "content": "CAM-01 · Centro de Control SOC", "fontSize": 11, "fontWeight": "bold", "fill": BLUE_CYAN },
                            { "type": "frame", "name": "Box", "height": 100, "fill": "#06B6D426", "stroke": BLUE_CYAN, "strokeWidth": 1.5, "cornerRadius": 4, "padding": [6, 6], "children": [
                                { "type": "text", "name": "W", "content": "SUPERVISIÓN NEURAL ACTIVA\n2.500 Nodos Conectados", "fontSize": 10, "fontWeight": "bold", "fill": BLUE_CYAN_LIGHT }
                            ]},
                            { "type": "text", "name": "F", "content": "Operación Normal · Zero Packet Loss", "fontSize": 10, "fontWeight": "bold", "fill": EMERALD }
                        ]},
                        { "type": "frame", "name": "CAM 2", "width": 305, "height": 290, "cornerRadius": 6, "fill": photo_fill(IMG_SERVER_CPD), "stroke": BLUE_PRIMARY, "strokeWidth": 1.5, "padding": [10, 10], "layout": "vertical", "justifyContent": "space_between", "children": [
                            { "type": "text", "name": "T", "content": "CAM-02 · Sala CPD & Servidores", "fontSize": 11, "fontWeight": "bold", "fill": BLUE_CYAN_LIGHT },
                            { "type": "frame", "name": "Box", "height": 100, "fill": "#3B82F626", "stroke": BLUE_ACCENT, "strokeWidth": 1.5, "cornerRadius": 4, "padding": [6, 6], "children": [
                                { "type": "text", "name": "W", "content": "ACCESO NIVEL 3 AUTORIZADO\nTemp: 21.2°C | Gas PCI: Standby", "fontSize": 10, "fontWeight": "bold", "fill": "#93C5FD" }
                            ]},
                            { "type": "text", "name": "F", "content": "Ingeniero M. Torres Verificado", "fontSize": 10, "fontWeight": "bold", "fill": BLUE_CYAN }
                        ]}
                    ]},
                    { "type": "frame", "name": "Ft", "width": "fill_container", "height": 108, "fill": "#071026", "layout": "horizontal", "padding": [10, 18], "justifyContent": "space_between", "alignItems": "center", "children": [
                        { "type": "text", "name": "T1", "content": "ENCRIPTACIÓN: AES-256 E2E", "fontSize": 11, "fontWeight": "bold", "fill": BLUE_CYAN },
                        { "type": "text", "name": "T2", "content": "INTEGRIDAD RED: 100% OK", "fontSize": 11, "fontWeight": "bold", "fill": EMERALD },
                        { "type": "text", "name": "T3", "content": "SLA: 99.999% Certificado", "fontSize": 11, "fontWeight": "bold", "fill": AMBER }
                    ]}
                ]}
            ]},
            { "type": "frame", "name": "KPIs", "width": "fill_container", "height": 120, "fill": BLUE_SURFACE, "stroke": BLUE_BORDER, "strokeWidth": { "top": 1, "bottom": 1 }, "layout": "horizontal", "padding": [0, 48], "alignItems": "center", "justifyContent": "space_between", "children": [
                { "type": "frame", "name": "K1", "layout": "vertical", "gap": 2, "children": [
                    { "type": "text", "name": "N", "content": "+2.500", "fontSize": 32, "fontWeight": "800", "fill": BLUE_CYAN },
                    { "type": "text", "name": "L", "content": "Infraestructuras y recintos protegidos", "fontSize": 12, "fill": "#94A3B8" }
                ]},
                { "type": "frame", "name": "K2", "layout": "vertical", "gap": 2, "children": [
                    { "type": "text", "name": "N", "content": "< 15s", "fontSize": 32, "fontWeight": "800", "fill": "#FFFFFF" },
                    { "type": "text", "name": "L", "content": "Tiempo de respuesta validado por SLA", "fontSize": 12, "fill": "#94A3B8" }
                ]},
                { "type": "frame", "name": "K3", "layout": "vertical", "gap": 2, "children": [
                    { "type": "text", "name": "N", "content": "99.999%", "fontSize": 32, "fontWeight": "800", "fill": EMERALD },
                    { "type": "text", "name": "L", "content": "Disponibilidad continua de comunicaciones", "fontSize": 12, "fill": "#94A3B8" }
                ]},
                { "type": "frame", "name": "K4", "layout": "vertical", "gap": 2, "children": [
                    { "type": "text", "name": "N", "content": "20+ Años", "fontSize": 32, "fontWeight": "800", "fill": AMBER },
                    { "type": "text", "name": "L", "content": "Ingeniería de seguridad y ciberprotección", "fontSize": 12, "fill": "#94A3B8" }
                ]}
            ]},
            { "type": "frame", "name": "Bento Grid", "width": "fill_container", "layout": "vertical", "padding": [56, 48], "gap": 24, "children": [
                { "type": "text", "name": "Title", "content": "Protección Perimetral y Ciberseguridad de Alta Fidelidad", "fontSize": 32, "fontWeight": "800", "fill": "#FFFFFF" },
                { "type": "frame", "name": "Row 1", "layout": "horizontal", "gap": 20, "children": [
                    { "type": "frame", "name": "C1", "width": 433, "height": 240, "cornerRadius": 12, "fill": photo_fill(IMG_CCTV_CAMERA), "stroke": BLUE_BORDER, "strokeWidth": 1.5, "padding": [18, 18], "layout": "vertical", "justifyContent": "space_between", "children": [
                        { "type": "text", "name": "Tag", "content": "RED NEURAL 4K", "fontSize": 10, "fontWeight": "bold", "fill": BLUE_CYAN_LIGHT },
                        { "type": "text", "name": "T", "content": "CCTV con Visión Artificial y Cámaras Térmicas", "fontSize": 16, "fontWeight": "700", "fill": "#FFFFFF" },
                        { "type": "text", "name": "L", "content": "Ver analítica neural →", "fontSize": 12, "fontWeight": "bold", "fill": BLUE_CYAN }
                    ]},
                    { "type": "frame", "name": "C2", "width": 433, "height": 240, "cornerRadius": 12, "fill": photo_fill(IMG_BIOMETRIC_TURNSTILE), "stroke": BLUE_BORDER_SUBTLE, "strokeWidth": 1, "padding": [18, 18], "layout": "vertical", "justifyContent": "space_between", "children": [
                        { "type": "text", "name": "Tag", "content": "BIOMETRÍA 3D CONTACTLESS", "fontSize": 10, "fontWeight": "bold", "fill": BLUE_CYAN_LIGHT },
                        { "type": "text", "name": "T", "content": "Control de Accesos Biométrico y Tornos", "fontSize": 16, "fontWeight": "700", "fill": "#FFFFFF" },
                        { "type": "text", "name": "L", "content": "Configurar control de accesos →", "fontSize": 12, "fontWeight": "bold", "fill": BLUE_CYAN }
                    ]},
                    { "type": "frame", "name": "C3", "width": 433, "height": 240, "cornerRadius": 12, "fill": photo_fill(IMG_CONTROL_ROOM), "stroke": BLUE_BORDER_SUBTLE, "strokeWidth": 1, "padding": [18, 18], "layout": "vertical", "justifyContent": "space_between", "children": [
                        { "type": "text", "name": "Tag", "content": "SOC CYBER 24/7", "fontSize": 10, "fontWeight": "bold", "fill": AMBER },
                        { "type": "text", "name": "T", "content": "CRA 24/7/365 con Custodia y Acuda", "fontSize": 16, "fontWeight": "700", "fill": "#FFFFFF" },
                        { "type": "text", "name": "L", "content": "Protocolo SOC →", "fontSize": 12, "fontWeight": "bold", "fill": AMBER }
                    ]}
                ]}
            ]},
            blue_footer()
        ]
    }

def build_s2_nosotros(x, y):
    return {
        "type": "frame", "id": "s2-p2-nosotros", "name": "🔵 S2.2: Sobre Nosotros & SOC (Cobalt SOC)",
        "x": x, "y": y, "width": 1440, "height": 2000, "fill": BLUE_BG, "layout": "vertical", "clip": True, "children": [
            blue_header("Centro SOC"),
            { "type": "frame", "name": "Hero Nosotros", "width": "fill_container", "height": 440, "fill": photo_fill(IMG_CONTROL_ROOM, "#03071244", "#030712F8"), "layout": "vertical", "padding": [56, 64], "justifyContent": "center", "gap": 14, "children": [
                { "type": "frame", "name": "Tag", "height": 26, "padding": [0, 12], "fill": "#1E3A8A4D", "stroke": BLUE_BORDER, "strokeWidth": 1, "cornerRadius": 14, "alignItems": "center", "children": [
                    { "type": "text", "name": "T", "content": "INFRAESTRUCTURA DE CIBERDEFENSA TIER III", "fontSize": 11, "fontWeight": "bold", "fill": BLUE_CYAN_LIGHT }
                ]},
                { "type": "text", "name": "H1", "content": "Arquitectura de Defensa Ciber-Física y Centro SOC 24/7 de Alta Resiliencia", "fontSize": 36, "fontWeight": "800", "fill": "#FFFFFF", "lineHeight": 1.2, "width": 800 },
                { "type": "text", "name": "D", "content": "Control 61 integra la seguridad física de Grado 3 con la ciberseguridad industrial avanzada. Nuestro SOC monitoriza más de 2.500 nodos críticos en tiempo real con enrutamiento redundante y aislamiento automático de amenazas.", "fontSize": 14, "fill": "#94A3B8", "lineHeight": 1.6, "width": 750 }
            ]},
            { "type": "frame", "name": "Pilares SOC", "width": "fill_container", "layout": "horizontal", "padding": [48, 48], "gap": 24, "children": [
                { "type": "frame", "name": "P1", "width": 433, "height": 260, "fill": BLUE_SURFACE, "stroke": BLUE_BORDER, "strokeWidth": 1.5, "cornerRadius": 12, "padding": [22, 22], "layout": "vertical", "gap": 10, "children": [
                    { "type": "icon", "name": "I", "library": "lucide", "icon": "lock", "width": 30, "height": 30, "fill": BLUE_CYAN },
                    { "type": "text", "name": "T", "content": "Cifrado Militar AES-256 E2E", "fontSize": 17, "fontWeight": "bold", "fill": "#FFFFFF" },
                    { "type": "text", "name": "D", "content": "Toda la telemetría de sensores, ráfagas de vídeo y comandos de armado viajan a través de túneles VPN cifrados con claves rotativas de 256 bits.", "fontSize": 12, "fill": "#94A3B8", "lineHeight": 1.5 }
                ]},
                { "type": "frame", "name": "P2", "width": 433, "height": 260, "fill": BLUE_SURFACE, "stroke": BLUE_BORDER_SUBTLE, "strokeWidth": 1, "cornerRadius": 12, "padding": [22, 22], "layout": "vertical", "gap": 10, "children": [
                    { "type": "icon", "name": "I", "library": "lucide", "icon": "activity", "width": 30, "height": 30, "fill": EMERALD },
                    { "type": "text", "name": "T", "content": "Certificación ENS Nivel Alto", "fontSize": 17, "fontWeight": "bold", "fill": "#FFFFFF" },
                    { "type": "text", "name": "D", "content": "Cumplimiento auditado del Esquema Nacional de Seguridad (ENS) para la protección de infraestructuras críticas, administraciones públicas y grandes industrias.", "fontSize": 12, "fill": "#94A3B8", "lineHeight": 1.5 }
                ]},
                { "type": "frame", "name": "P3", "width": 433, "height": 260, "fill": BLUE_SURFACE, "stroke": BLUE_BORDER_SUBTLE, "strokeWidth": 1, "cornerRadius": 12, "padding": [22, 22], "layout": "vertical", "gap": 10, "children": [
                    { "type": "icon", "name": "I", "library": "lucide", "icon": "server", "width": 30, "height": 30, "fill": AMBER },
                    { "type": "text", "name": "T", "content": "SLA de Uptime 99.999%", "fontSize": 17, "fontWeight": "bold", "fill": "#FFFFFF" },
                    { "type": "text", "name": "D", "content": "Disponibilidad ininterrumpida con respaldo energético por SAI redundante y generador diésel autónomo para emergencias prolongadas.", "fontSize": 12, "fill": "#94A3B8", "lineHeight": 1.5 }
                ]}
            ]},
            blue_footer()
        ]
    }

def build_s2_soluciones(x, y):
    return {
        "type": "frame", "id": "s2-p3-soluciones", "name": "🔵 S2.3: Soluciones Ciber-Físicas (Cobalt SOC)",
        "x": x, "y": y, "width": 1440, "height": 2200, "fill": BLUE_BG, "layout": "vertical", "clip": True, "children": [
            blue_header("Soluciones"),
            { "type": "frame", "name": "Sec Header", "width": "fill_container", "height": 220, "fill": BLUE_SURFACE, "layout": "vertical", "padding": [40, 48], "justifyContent": "center", "gap": 8, "children": [
                { "type": "text", "name": "Eye", "content": "ECOSISTEMA DE CIBERSEGURIDAD, REDES OT E IA PERIMETRAL", "fontSize": 12, "fontWeight": "800", "fill": BLUE_CYAN },
                { "type": "text", "name": "H1", "content": "Soluciones Avanzadas para Infraestructuras Críticas", "fontSize": 34, "fontWeight": "800", "fill": "#FFFFFF" },
                { "type": "text", "name": "D", "content": "Integración de hardware industrial robusto con algoritmos neurales de última generación.", "fontSize": 14, "fill": "#94A3B8" }
            ]},
            { "type": "frame", "name": "Services List", "width": "fill_container", "layout": "vertical", "padding": [40, 48], "gap": 24, "children": [
                { "type": "frame", "name": "S1", "width": "fill_container", "height": 200, "fill": BLUE_CARD, "stroke": BLUE_BORDER, "strokeWidth": 1.5, "cornerRadius": 12, "layout": "horizontal", "clip": True, "children": [
                    { "type": "frame", "name": "Img", "width": 320, "height": 200, "fill": photo_fill(IMG_SERVER_CPD) },
                    { "type": "frame", "name": "Body", "width": 970, "padding": [20, 28], "layout": "vertical", "justifyContent": "space_between", "children": [
                        { "type": "frame", "name": "Top", "layout": "horizontal", "justifyContent": "space_between", "children": [
                            { "type": "text", "name": "T", "content": "01. Blindaje de CPDs & Extinción Inocua por Gas Novec 1230", "fontSize": 18, "fontWeight": "bold", "fill": "#FFFFFF" },
                            { "type": "text", "name": "Tag", "content": "ZERO DOWNTIME DATA CENTER", "fontSize": 10, "fontWeight": "bold", "fill": BLUE_CYAN_LIGHT }
                        ]},
                        { "type": "text", "name": "D", "content": "Sistemas de detección de incendios por aspiración láser de altísima sensibilidad (VESDA) y extinción automática por inundación de gas limpio inocuo para servidores y electrónica sensible.", "fontSize": 12, "fill": "#94A3B8", "lineHeight": 1.4 },
                        { "type": "frame", "name": "Specs", "layout": "horizontal", "gap": 20, "children": [
                            { "type": "text", "name": "S1", "content": "✓ No daña equipamiento informático", "fontSize": 12, "fontWeight": "bold", "fill": EMERALD },
                            { "type": "text", "name": "S2", "content": "✓ Desconexión eléctrica automática", "fontSize": 12, "fontWeight": "bold", "fill": EMERALD }
                        ]}
                    ]}
                ]},
                { "type": "frame", "name": "S2", "width": "fill_container", "height": 200, "fill": BLUE_CARD, "stroke": BLUE_BORDER_SUBTLE, "strokeWidth": 1, "cornerRadius": 12, "layout": "horizontal", "clip": True, "children": [
                    { "type": "frame", "name": "Img", "width": 320, "height": 200, "fill": photo_fill(IMG_CONTROL_ROOM) },
                    { "type": "frame", "name": "Body", "width": 970, "padding": [20, 28], "layout": "vertical", "justifyContent": "space_between", "children": [
                        { "type": "frame", "name": "Top", "layout": "horizontal", "justifyContent": "space_between", "children": [
                            { "type": "text", "name": "T", "content": "02. Microsegmentación Zero Trust en Redes OT / SCADA Industriales", "fontSize": 18, "fontWeight": "bold", "fill": "#FFFFFF" },
                            { "type": "text", "name": "Tag", "content": "PROTECCIÓN CIBER-FÍSICA", "fontSize": 10, "fontWeight": "bold", "fill": EMERALD }
                        ]},
                        { "type": "text", "name": "D", "content": "Aislamiento de la red de videovigilancia y control de accesos frente a la red corporativa mediante firewalls industriales certificados. Detección de intrusiones en bus Modbus/BACnet.", "fontSize": 12, "fill": "#94A3B8", "lineHeight": 1.4 },
                        { "type": "frame", "name": "Specs", "layout": "horizontal", "gap": 20, "children": [
                            { "type": "text", "name": "S1", "content": "✓ Inmunidad a ataques ransomware", "fontSize": 12, "fontWeight": "bold", "fill": EMERALD },
                            { "type": "text", "name": "S2", "content": "✓ Inspección profunda de paquetes DPI", "fontSize": 12, "fontWeight": "bold", "fill": EMERALD }
                        ]}
                    ]}
                ]}
            ]},
            blue_footer()
        ]
    }

def build_s2_webapp_portal(x, y):
    return {
        "type": "frame", "id": "s2-p4-webapp-portal", "name": "🔵 S2.4: Cyber SOC Portal (Cobalt SOC)",
        "x": x, "y": y, "width": 1440, "height": 1024, "fill": "#020612", "layout": "horizontal", "clip": True, "children": [
            { "type": "frame", "name": "SOC Sidebar", "width": 250, "height": 1024, "fill": "#060E24", "stroke": BLUE_BORDER_SUBTLE, "strokeWidth": { "right": 1 }, "layout": "vertical", "padding": [20, 16], "justifyContent": "space_between", "children": [
                { "type": "frame", "name": "Top", "layout": "vertical", "gap": 24, "children": [
                    logo_card((160, 42)),
                    { "type": "frame", "name": "Nav Items", "layout": "vertical", "gap": 8, "children": [
                        { "type": "frame", "name": "Item 1 Active", "height": 40, "fill": "#2563EB33", "stroke": BLUE_BORDER, "strokeWidth": 1, "cornerRadius": 8, "padding": [0, 12], "layout": "horizontal", "gap": 10, "alignItems": "center", "children": [
                            { "type": "icon", "name": "I", "library": "lucide", "icon": "activity", "width": 18, "height": 18, "fill": BLUE_CYAN },
                            { "type": "text", "name": "T", "content": "SOC Threat Matrix", "fontSize": 13, "fontWeight": "bold", "fill": "#FFFFFF" }
                        ]},
                        { "type": "frame", "name": "Item 2", "height": 40, "padding": [0, 12], "layout": "horizontal", "gap": 10, "alignItems": "center", "children": [
                            { "type": "icon", "name": "I", "library": "lucide", "icon": "eye", "width": 18, "height": 18, "fill": "#64748B" },
                            { "type": "text", "name": "T", "content": "Neural Video Streams", "fontSize": 13, "fill": "#94A3B8" }
                        ]},
                        { "type": "frame", "name": "Item 3", "height": 40, "padding": [0, 12], "layout": "horizontal", "gap": 10, "alignItems": "center", "children": [
                            { "type": "icon", "name": "I", "library": "lucide", "icon": "fingerprint", "width": 18, "height": 18, "fill": "#64748B" },
                            { "type": "text", "name": "T", "content": "Zero Trust Biometrics", "fontSize": 13, "fill": "#94A3B8" }
                        ]},
                        { "type": "frame", "name": "Item 4", "height": 40, "padding": [0, 12], "layout": "horizontal", "gap": 10, "alignItems": "center", "children": [
                            { "type": "icon", "name": "I", "library": "lucide", "icon": "terminal", "width": 18, "height": 18, "fill": "#64748B" },
                            { "type": "text", "name": "T", "content": "Terminal & Contención", "fontSize": 13, "fill": "#94A3B8" }
                        ]}
                    ]}
                ]},
                { "type": "frame", "name": "User Box", "height": 56, "fill": "#0A1535", "cornerRadius": 8, "padding": [8, 12], "layout": "horizontal", "gap": 10, "alignItems": "center", "children": [
                    { "type": "ellipse", "name": "Avatar", "width": 34, "height": 34, "fill": BLUE_CYAN },
                    { "type": "frame", "name": "Txt", "layout": "vertical", "gap": 2, "children": [
                        { "type": "text", "name": "Name", "content": "SOC Lead #084", "fontSize": 12, "fontWeight": "bold", "fill": "#FFFFFF" },
                        { "type": "text", "name": "Role", "content": "Nivel 3 - Enlace Policial", "fontSize": 10, "fill": BLUE_CYAN_LIGHT }
                    ]}
                ]}
            ]},
            { "type": "frame", "name": "Workspace", "width": 1190, "height": 1024, "layout": "vertical", "children": [
                { "type": "frame", "name": "Topbar App", "width": "fill_container", "height": 68, "fill": "#060E24", "stroke": BLUE_BORDER_SUBTLE, "strokeWidth": { "bottom": 1 }, "layout": "horizontal", "padding": [0, 32], "alignItems": "center", "justifyContent": "space_between", "children": [
                    { "type": "frame", "name": "Telemetry Bar", "layout": "horizontal", "gap": 16, "alignItems": "center", "children": [
                        { "type": "text", "name": "Lat", "content": "⚡ LATENCIA E2E: 8ms", "fontSize": 12, "fontWeight": "bold", "fill": BLUE_CYAN },
                        { "type": "text", "name": "Nodes", "content": "🛰️ 2.500 NODOS CONECTADOS", "fontSize": 12, "fontWeight": "bold", "fill": EMERALD },
                        { "type": "text", "name": "Cfr", "content": "🔒 AES-256 GCM", "fontSize": 12, "fontWeight": "bold", "fill": "#94A3B8" }
                    ]},
                    { "type": "frame", "name": "Contention Button", "height": 38, "padding": [0, 16], "fill": BLUE_PRIMARY, "cornerRadius": 6, "alignItems": "center", "justifyContent": "center", "children": [
                        { "type": "text", "name": "T", "content": "PROTOCOLOS DE CONTENCIÓN ACTIVOS", "fontSize": 12, "fontWeight": "bold", "fill": "#FFFFFF" }
                    ]}
                ]},
                { "type": "frame", "name": "Grid", "width": "fill_container", "layout": "horizontal", "padding": [24, 32], "gap": 24, "children": [
                    { "type": "frame", "name": "Main SOC Video", "width": 760, "height": 860, "layout": "vertical", "gap": 16, "children": [
                        { "type": "frame", "name": "Stream 1", "width": "fill_container", "height": 420, "cornerRadius": 10, "fill": photo_fill(IMG_CONTROL_ROOM), "stroke": BLUE_CYAN, "strokeWidth": 2, "padding": [16, 16], "layout": "vertical", "justifyContent": "space_between", "children": [
                            { "type": "frame", "name": "T", "layout": "horizontal", "justifyContent": "space_between", "children": [
                                { "type": "text", "name": "L", "content": "STREAM 4K // MATRIZ PERIMETRAL NACIONAL", "fontSize": 12, "fontWeight": "bold", "fill": "#FFFFFF" },
                                { "type": "text", "name": "R", "content": "● 60 FPS · BITRATE: 18 Mbps", "fontSize": 11, "fontWeight": "bold", "fill": BLUE_CYAN }
                            ]},
                            { "type": "frame", "name": "Box", "height": 90, "fill": "#06B6D426", "stroke": BLUE_CYAN, "strokeWidth": 1.5, "cornerRadius": 6, "padding": [8, 12], "children": [
                                { "type": "text", "name": "W", "content": "ANÁLISIS NEURAL: Perímetro 100% Despejado\nÚltimo escaneo completado hace 0.2s · Sin vectores de intrusión", "fontSize": 11, "fontWeight": "bold", "fill": BLUE_CYAN_LIGHT }
                            ]}
                        ]},
                        { "type": "frame", "name": "Stream 2", "width": "fill_container", "height": 380, "cornerRadius": 10, "fill": photo_fill(IMG_SERVER_CPD), "stroke": BLUE_BORDER_SUBTLE, "strokeWidth": 1, "padding": [16, 16], "layout": "vertical", "justifyContent": "space_between", "children": [
                            { "type": "text", "name": "T", "content": "STREAM SECUNDARIO // CPD DATA CENTER TIER III", "fontSize": 12, "fontWeight": "bold", "fill": "#FFFFFF" },
                            { "type": "text", "name": "F", "content": "Acceso Biométrico: Ingeniero M. Torres Autorizado · Puerta Esclusa Bloqueada", "fontSize": 11, "fill": "#93C5FD" }
                        ]}
                    ]},
                    { "type": "frame", "name": "Telemetry Right", "width": 340, "height": 860, "layout": "vertical", "gap": 16, "children": [
                        { "type": "frame", "name": "Card Threat Level", "width": "fill_container", "height": 280, "fill": BLUE_CARD, "stroke": BLUE_BORDER, "strokeWidth": 1.5, "cornerRadius": 10, "padding": [16, 16], "layout": "vertical", "justifyContent": "space_between", "children": [
                            { "type": "text", "name": "T", "content": "Nivel de Amenaza Global SOC", "fontSize": 13, "fontWeight": "bold", "fill": "#FFFFFF" },
                            { "type": "text", "name": "Val", "content": "NIVEL 1: NORMAL", "fontSize": 20, "fontWeight": "800", "fill": EMERALD },
                            { "type": "text", "name": "D", "content": "99.999% de paquetes verificados. Polling de alarmas Grado 3 respondiendo en < 30ms en todas las sedes.", "fontSize": 11, "fill": "#94A3B8" },
                            { "type": "frame", "name": "Btn Action", "height": 36, "fill": "#1E3A8A4D", "stroke": BLUE_CYAN, "strokeWidth": 1, "cornerRadius": 6, "alignItems": "center", "justifyContent": "center", "children": [
                                { "type": "text", "name": "T", "content": "Generar Reporte Forense E2E", "fontSize": 11, "fontWeight": "bold", "fill": BLUE_CYAN }
                            ]}
                        ]},
                        { "type": "frame", "name": "Card Incident Stream", "width": "fill_container", "height": 280, "fill": BLUE_CARD, "stroke": BLUE_BORDER_SUBTLE, "strokeWidth": 1, "cornerRadius": 10, "padding": [16, 16], "layout": "vertical", "justifyContent": "space_between", "children": [
                            { "type": "text", "name": "T", "content": "Feed de Eventos Ciber-Físicos", "fontSize": 13, "fontWeight": "bold", "fill": "#FFFFFF" },
                            { "type": "text", "name": "E1", "content": "12:04:18 · Heartbeat Polling 5G Sede 01 [OK]", "fontSize": 11, "fill": "#86EFAC" },
                            { "type": "text", "name": "E2", "content": "12:01:05 · Apertura de Esclusa CPD Nivel 3", "fontSize": 11, "fill": "#93C5FD" },
                            { "type": "text", "name": "E3", "content": "11:50:33 · Validación LPR Muelle 4 [OK]", "fontSize": 11, "fill": "#94A3B8" }
                        ]}
                    ]}
                ]}
            ]}
        ]
    }

def build_s2_contacto(x, y):
    return {
        "type": "frame", "id": "s2-p5-contacto", "name": "🔵 S2.5: Contacto & SOC (Cobalt SOC)",
        "x": x, "y": y, "width": 1440, "height": 1400, "fill": BLUE_BG, "layout": "vertical", "clip": True, "children": [
            blue_header("Contacto"),
            { "type": "frame", "name": "Hero Contact", "width": "fill_container", "height": 260, "fill": BLUE_SURFACE, "layout": "vertical", "padding": [40, 48], "justifyContent": "center", "gap": 8, "children": [
                { "type": "text", "name": "Eye", "content": "VALORACIÓN CIBER-FÍSICA Y AUDITORÍA DE REDES OT", "fontSize": 12, "fontWeight": "800", "fill": BLUE_CYAN },
                { "type": "text", "name": "H1", "content": "Conectar con el Equipo de Ingeniería SOC", "fontSize": 34, "fontWeight": "800", "fill": "#FFFFFF" },
                { "type": "text", "name": "D", "content": "Atención especializada para directores de IT, CISOs y responsables de seguridad de plantas críticas.", "fontSize": 14, "fill": "#94A3B8" }
            ]},
            { "type": "frame", "name": "Contact Grid", "width": "fill_container", "layout": "horizontal", "padding": [40, 48], "gap": 32, "children": [
                { "type": "frame", "name": "Cards Col", "width": 540, "layout": "vertical", "gap": 18, "children": [
                    { "type": "frame", "name": "C1 Phone", "height": 120, "fill": BLUE_CARD, "stroke": BLUE_BORDER, "strokeWidth": 1.5, "cornerRadius": 10, "padding": [18, 20], "layout": "vertical", "gap": 4, "children": [
                        { "type": "text", "name": "T", "content": "🛰️ Teléfono Línea Directa SOC 24h", "fontSize": 13, "fontWeight": "bold", "fill": BLUE_CYAN },
                        { "type": "text", "name": "P", "content": "968 622 984", "fontSize": 22, "fontWeight": "800", "fill": "#FFFFFF" },
                        { "type": "text", "name": "S", "content": "Canal seguro y cifrado con ingenieros de guardia.", "fontSize": 11, "fill": "#94A3B8" }
                    ]},
                    { "type": "frame", "name": "C2 Sede", "height": 120, "fill": BLUE_CARD, "stroke": BLUE_BORDER_SUBTLE, "strokeWidth": 1, "cornerRadius": 10, "padding": [18, 20], "layout": "vertical", "gap": 4, "children": [
                        { "type": "text", "name": "T", "content": "📍 SOC Command Center & Laboratorio OT", "fontSize": 13, "fontWeight": "bold", "fill": "#FFFFFF" },
                        { "type": "text", "name": "P", "content": "Pol. Ind. La Polvorista, Murcia", "fontSize": 15, "fontWeight": "700", "fill": "#FFFFFF" },
                        { "type": "text", "name": "S", "content": "Desarrollos y Sistemas Inteligentes S.L. · DGP 2341", "fontSize": 11, "fill": "#94A3B8" }
                    ]}
                ]},
                { "type": "frame", "name": "Form Container", "width": 770, "height": 400, "fill": BLUE_SURFACE, "stroke": BLUE_BORDER, "strokeWidth": 1.5, "cornerRadius": 12, "padding": [28, 28], "layout": "vertical", "justifyContent": "space_between", "children": [
                    { "type": "text", "name": "H2", "content": "Solicitar Auditoría Tecnológica de Vulnerabilidades", "fontSize": 18, "fontWeight": "bold", "fill": "#FFFFFF" },
                    { "type": "frame", "name": "F1", "height": 42, "fill": BLUE_BG, "stroke": BLUE_BORDER_SUBTLE, "strokeWidth": 1, "cornerRadius": 6, "padding": [0, 16], "layout": "horizontal", "alignItems": "center", "children": [
                        { "type": "text", "name": "P", "content": "Nombre de la Empresa o Corporación", "fontSize": 12, "fill": "#64748B" }
                    ]},
                    { "type": "frame", "name": "F2", "height": 42, "fill": BLUE_BG, "stroke": BLUE_BORDER_SUBTLE, "strokeWidth": 1, "cornerRadius": 6, "padding": [0, 16], "layout": "horizontal", "alignItems": "center", "children": [
                        { "type": "text", "name": "P", "content": "Teléfono Directo / Email Corporativo", "fontSize": 12, "fill": "#64748B" }
                    ]},
                    { "type": "frame", "name": "Submit", "height": 46, "fill": BLUE_PRIMARY, "cornerRadius": 6, "alignItems": "center", "justifyContent": "center", "children": [
                        { "type": "text", "name": "T", "content": "Solicitar Diagnóstico Ciber-Físico", "fontSize": 13, "fontWeight": "bold", "fill": "#FFFFFF" }
                    ]}
                ]}
            ]},
            blue_footer()
        ]
    }

# =============================================================================
# 🟢 SUITE 3: PLATINUM EXECUTIVE & CORPORATE DEFENSE (Titanium, Emerald & Gold)
# =============================================================================
PLAT_BG = "#0B0F19"
PLAT_SURFACE = "#111827"
PLAT_CARD = "#1F2937"
PLAT_EMERALD = "#059669"
PLAT_EMERALD_LIGHT = "#10B981"
PLAT_GOLD = "#F59E0B"
PLAT_BORDER = "#10B9814D"
PLAT_BORDER_SUBTLE = "#FFFFFF14"

def plat_header(active_page="Inicio"):
    navs = ["Inicio", "Institucional", "Sectores", "Executive Hub", "Consultoría"]
    links = []
    for n in navs:
        is_a = (n == active_page)
        links.append({
            "type": "text", "name": n, "content": n,
            "fontSize": 13, "fontWeight": "700" if is_a else "500",
            "fill": PLAT_EMERALD_LIGHT if is_a else "#94A3B8"
        })
    return {
        "type": "frame", "name": "Header Plat", "width": "fill_container", "layout": "vertical", "children": [
            { "type": "frame", "name": "Top Bar", "width": "fill_container", "height": 38, "fill": "#0F172A", "stroke": PLAT_BORDER, "strokeWidth": { "bottom": 1 }, "layout": "horizontal", "padding": [0, 48], "alignItems": "center", "justifyContent": "space_between", "children": [
                { "type": "frame", "name": "L", "layout": "horizontal", "gap": 8, "alignItems": "center", "children": [
                    { "type": "ellipse", "name": "Dot", "width": 8, "height": 8, "fill": PLAT_EMERALD_LIGHT },
                    { "type": "text", "name": "T", "content": "INGENIERÍA DE ALTA SEGURIDAD CORPORATIVA · HOMOLOGACIÓN DGP Nº 2341 · CERTIFICACIÓN UNE-EN 50131", "fontSize": 11, "fontWeight": "bold", "fill": "#E2E8F0" }
                ]},
                { "type": "frame", "name": "R", "layout": "horizontal", "gap": 20, "alignItems": "center", "children": [
                    { "type": "text", "name": "P", "content": "🏛️ Atención Ejecutiva 24h: 968 622 984", "fontSize": 12, "fontWeight": "bold", "fill": "#FFFFFF" },
                    { "type": "text", "name": "A", "content": "Executive Portal →", "fontSize": 12, "fontWeight": "bold", "fill": PLAT_EMERALD_LIGHT }
                ]}
            ]},
            { "type": "frame", "name": "Main Nav", "width": "fill_container", "height": 76, "fill": "#111827EE", "stroke": PLAT_BORDER_SUBTLE, "strokeWidth": { "bottom": 1 }, "layout": "horizontal", "padding": [0, 48], "alignItems": "center", "justifyContent": "space_between", "children": [
                { "type": "frame", "name": "Brand", "layout": "horizontal", "gap": 12, "alignItems": "center", "children": [
                    logo_card((130, 40)),
                    { "type": "frame", "name": "Claim", "layout": "vertical", "gap": 1, "children": [
                        { "type": "text", "name": "Sub", "content": "EXECUTIVE CORPORATE DEFENSE", "fontSize": 8, "fontWeight": "700", "fill": PLAT_EMERALD_LIGHT, "letterSpacing": 0.8 },
                        { "type": "text", "name": "DGP", "content": "SISTEMAS HOMOLOGADOS EN PROPIEDAD · DGP 2341", "fontSize": 8, "fill": "#64748B" }
                    ]}
                ]},
                { "type": "frame", "name": "Nav Links", "layout": "horizontal", "gap": 24, "alignItems": "center", "children": links },
                { "type": "frame", "name": "CTA Btn", "height": 40, "padding": [0, 20], "fill": PLAT_EMERALD, "cornerRadius": 8, "alignItems": "center", "justifyContent": "center", "children": [
                    { "type": "text", "name": "T", "content": "Consultoría Confidencial", "fontSize": 13, "fontWeight": "700", "fill": "#FFFFFF" }
                ]}
            ]}
        ]
    }

def plat_footer():
    return {
        "type": "frame", "name": "Footer Plat", "width": "fill_container", "height": 260, "fill": "#070B12", "layout": "vertical", "padding": [36, 48, 16, 48], "justifyContent": "space_between", "children": [
            { "type": "frame", "name": "Cols", "width": "fill_container", "layout": "horizontal", "justifyContent": "space_between", "children": [
                { "type": "frame", "name": "C1", "width": 420, "layout": "vertical", "gap": 8, "children": [
                    logo_card((120, 36)),
                    { "type": "text", "name": "D", "content": "Desarrollos y Sistemas Inteligentes S.L. · DGP Nº 2341\nSoluciones llave en mano para Grandes Corporaciones y Banca.\nSede Central: Pol. Ind. La Polvorista, Molina de Segura (Murcia)", "fontSize": 12, "fill": "#64748B", "lineHeight": 1.5 }
                ]},
                { "type": "frame", "name": "C2", "layout": "vertical", "gap": 6, "children": [
                    { "type": "text", "name": "T", "content": "SECTORES CRÍTICOS", "fontSize": 11, "fontWeight": "800", "fill": PLAT_EMERALD_LIGHT },
                    { "type": "text", "name": "L1", "content": "Banca, Joyería y Armerías (Grado 3)", "fontSize": 12, "fill": "#94A3B8" },
                    { "type": "text", "name": "L2", "content": "Plantas Fotovoltaicas & Parques Solares", "fontSize": 12, "fill": "#94A3B8" },
                    { "type": "text", "name": "L3", "content": "Sector Farmacéutico & Químico", "fontSize": 12, "fill": "#94A3B8" }
                ]},
                { "type": "frame", "name": "C3", "layout": "vertical", "gap": 6, "children": [
                    { "type": "text", "name": "T", "content": "CANAL PREFERENTE 24H", "fontSize": 11, "fontWeight": "800", "fill": PLAT_EMERALD_LIGHT },
                    { "type": "text", "name": "L1", "content": "📞 Atención VIP: 968 622 984", "fontSize": 12, "fontWeight": "bold", "fill": "#FFFFFF" },
                    { "type": "text", "name": "L2", "content": "✉️ info@control61.com", "fontSize": 12, "fill": "#94A3B8" }
                ]}
            ]},
            { "type": "frame", "name": "Bot", "width": "fill_container", "layout": "horizontal", "justifyContent": "space_between", "alignItems": "center", "children": [
                { "type": "text", "name": "Copy", "content": "© 2026 Control 61 Executive Defense. Todos los derechos reservados.", "fontSize": 11, "fill": "#475569" },
                { "type": "text", "name": "Legal", "content": "DGP 2341 · ISO 9001 / 14001 / 45001 (RINA) · UNE-EN 50131", "fontSize": 11, "fill": "#475569" }
            ]}
        ]
    }

def build_s3_home(x, y):
    return {
        "type": "frame", "id": "s3-p1-home", "name": "🟢 S3.1: Home Landing (Platinum Executive)",
        "x": x, "y": y, "width": 1440, "height": 3100, "fill": PLAT_BG, "layout": "vertical", "clip": True, "children": [
            plat_header("Inicio"),
            { "type": "frame", "name": "Hero Section", "width": "fill_container", "height": 660, "fill": PLAT_BG, "layout": "horizontal", "padding": [48, 48], "gap": 40, "alignItems": "center", "justifyContent": "space_between", "children": [
                { "type": "frame", "name": "L", "width": 630, "layout": "vertical", "gap": 20, "children": [
                    { "type": "frame", "name": "Pill", "height": 30, "padding": [0, 12], "fill": "#05966926", "stroke": PLAT_BORDER, "strokeWidth": 1, "cornerRadius": 20, "layout": "horizontal", "gap": 8, "alignItems": "center", "children": [
                        { "type": "icon", "name": "I", "library": "lucide", "icon": "shield", "width": 14, "height": 14, "fill": PLAT_EMERALD_LIGHT },
                        { "type": "text", "name": "T", "content": "HOMOLOGACIÓN MINISTERIAL DGP Nº 2341 · RINA ISO CERTIFIED", "fontSize": 10, "fontWeight": "bold", "fill": PLAT_EMERALD_LIGHT }
                    ]},
                    { "type": "text", "name": "H1", "content": "Ingeniería de Alta Seguridad para Grandes Corporaciones y Recintos Críticos", "fontSize": 40, "fontWeight": "800", "fill": "#FFFFFF", "lineHeight": 1.18 },
                    { "type": "text", "name": "D", "content": "Soluciones de seguridad integral en estricta propiedad, certificadas bajo norma UNE-EN 50131 y diseñadas para directores de seguridad que exigen máxima fiabilidad técnica sin ataduras contractuales.", "fontSize": 15, "fill": "#94A3B8", "lineHeight": 1.6 },
                    { "type": "frame", "name": "Btns", "layout": "horizontal", "gap": 16, "children": [
                        { "type": "frame", "name": "CTA", "height": 48, "padding": [0, 24], "fill": PLAT_EMERALD, "cornerRadius": 8, "layout": "horizontal", "gap": 8, "alignItems": "center", "children": [
                            { "type": "text", "name": "T", "content": "Solicitar Consultoría Técnica", "fontSize": 14, "fontWeight": "700", "fill": "#FFFFFF" },
                            { "type": "icon", "name": "I", "library": "lucide", "icon": "arrow-up-right", "width": 16, "height": 16, "fill": "#FFFFFF" }
                        ]},
                        { "type": "frame", "name": "Phone", "height": 48, "padding": [0, 20], "fill": "#1E293B", "stroke": PLAT_BORDER_SUBTLE, "strokeWidth": 1, "cornerRadius": 8, "layout": "horizontal", "gap": 8, "alignItems": "center", "children": [
                            { "type": "icon", "name": "I", "library": "lucide", "icon": "phone", "width": 15, "height": 15, "fill": PLAT_EMERALD_LIGHT },
                            { "type": "text", "name": "T", "content": "968 622 984 · Atención VIP", "fontSize": 13, "fontWeight": "600", "fill": "#FFFFFF" }
                        ]}
                    ]}
                ]},
                { "type": "frame", "name": "HUD Box", "width": 640, "height": 460, "fill": PLAT_CARD, "stroke": PLAT_BORDER, "strokeWidth": 1.5, "cornerRadius": 14, "layout": "vertical", "clip": True, "children": [
                    { "type": "frame", "name": "Hdr", "width": "fill_container", "height": 42, "fill": "#111827", "layout": "horizontal", "padding": [0, 16], "alignItems": "center", "justifyContent": "space_between", "children": [
                        { "type": "text", "name": "T", "content": "CORPORATE_DEFENSE://AUDITORIA_MULTI_SEDE", "fontSize": 11, "fontWeight": "bold", "fill": "#FFFFFF" },
                        { "type": "text", "name": "L", "content": "GRADO 3 HOMOLOGADO DGP", "fontSize": 10, "fontWeight": "bold", "fill": PLAT_EMERALD_LIGHT }
                    ]},
                    { "type": "frame", "name": "Cams", "width": "fill_container", "height": 310, "fill": "#060A10", "layout": "horizontal", "gap": 10, "padding": [10, 10], "children": [
                        { "type": "frame", "name": "CAM 1", "width": 305, "height": 290, "cornerRadius": 6, "fill": photo_fill(IMG_SOLAR_FARM), "stroke": PLAT_EMERALD, "strokeWidth": 1.5, "padding": [10, 10], "layout": "vertical", "justifyContent": "space_between", "children": [
                            { "type": "text", "name": "T", "content": "CAM-01 · Planta Solar 45 Has", "fontSize": 11, "fontWeight": "bold", "fill": PLAT_EMERALD_LIGHT },
                            { "type": "text", "name": "F", "content": "Radar Perimetral Térmico Activo", "fontSize": 10, "fill": "#CBD5E1" }
                        ]},
                        { "type": "frame", "name": "CAM 2", "width": 305, "height": 290, "cornerRadius": 6, "fill": photo_fill(IMG_JEWELRY_VAULT), "stroke": PLAT_GOLD, "strokeWidth": 1.5, "padding": [10, 10], "layout": "vertical", "justifyContent": "space_between", "children": [
                            { "type": "text", "name": "T", "content": "CAM-02 · Cámara Acorazada", "fontSize": 11, "fontWeight": "bold", "fill": PLAT_GOLD },
                            { "type": "text", "name": "F", "content": "Detección Sísmica + Niebla Standby", "fontSize": 10, "fill": "#CBD5E1" }
                        ]}
                    ]},
                    { "type": "frame", "name": "Ft", "width": "fill_container", "height": 108, "fill": "#0F172A", "layout": "horizontal", "padding": [10, 18], "justifyContent": "space_between", "alignItems": "center", "children": [
                        { "type": "text", "name": "T1", "content": "EQUIPOS EN PROPIEDAD TOTAL", "fontSize": 11, "fontWeight": "bold", "fill": PLAT_EMERALD_LIGHT },
                        { "type": "text", "name": "T2", "content": "SIN ALQUILERES NI PERMANENCIA", "fontSize": 11, "fontWeight": "bold", "fill": "#FFFFFF" },
                        { "type": "text", "name": "T3", "content": "SLA 24/7", "fontSize": 11, "fontWeight": "bold", "fill": PLAT_GOLD }
                    ]}
                ]}
            ]},
            { "type": "frame", "name": "KPIs", "width": "fill_container", "height": 120, "fill": PLAT_SURFACE, "stroke": PLAT_BORDER, "strokeWidth": { "top": 1, "bottom": 1 }, "layout": "horizontal", "padding": [0, 48], "alignItems": "center", "justifyContent": "space_between", "children": [
                { "type": "frame", "name": "K1", "layout": "vertical", "gap": 2, "children": [
                    { "type": "text", "name": "N", "content": "+2.500", "fontSize": 32, "fontWeight": "800", "fill": PLAT_EMERALD_LIGHT },
                    { "type": "text", "name": "L", "content": "Proyectos ejecutados en el Levante", "fontSize": 12, "fill": "#94A3B8" }
                ]},
                { "type": "frame", "name": "K2", "layout": "vertical", "gap": 2, "children": [
                    { "type": "text", "name": "N", "content": "100%", "fontSize": 32, "fontWeight": "800", "fill": "#FFFFFF" },
                    { "type": "text", "name": "L", "content": "Equipos en propiedad del cliente", "fontSize": 12, "fill": "#94A3B8" }
                ]},
                { "type": "frame", "name": "K3", "layout": "vertical", "gap": 2, "children": [
                    { "type": "text", "name": "N", "content": "Grado 3", "fontSize": 32, "fontWeight": "800", "fill": PLAT_GOLD },
                    { "type": "text", "name": "L", "content": "Homologación UNE-EN 50131 oficial", "fontSize": 12, "fill": "#94A3B8" }
                ]},
                { "type": "frame", "name": "K4", "layout": "vertical", "gap": 2, "children": [
                    { "type": "text", "name": "N", "content": "20+ Años", "fontSize": 32, "fontWeight": "800", "fill": "#CBD5E1" },
                    { "type": "text", "name": "L", "content": "Solvencia y trayectoria consolidada", "fontSize": 12, "fill": "#94A3B8" }
                ]}
            ]},
            { "type": "frame", "name": "Bento Grid", "width": "fill_container", "layout": "vertical", "padding": [56, 48], "gap": 24, "children": [
                { "type": "text", "name": "Title", "content": "Soluciones de Seguridad Corporativa de Alta Gama", "fontSize": 32, "fontWeight": "800", "fill": "#FFFFFF" },
                { "type": "frame", "name": "Row 1", "layout": "horizontal", "gap": 20, "children": [
                    { "type": "frame", "name": "C1", "width": 433, "height": 240, "cornerRadius": 12, "fill": photo_fill(IMG_JEWELRY_VAULT), "stroke": PLAT_BORDER, "strokeWidth": 1.5, "padding": [18, 18], "layout": "vertical", "justifyContent": "space_between", "children": [
                        { "type": "text", "name": "Tag", "content": "BANCA & JOYERÍA", "fontSize": 10, "fontWeight": "bold", "fill": PLAT_GOLD },
                        { "type": "text", "name": "T", "content": "Sistemas Grado 3 con Sísmicos y Generador de Niebla", "fontSize": 16, "fontWeight": "700", "fill": "#FFFFFF" },
                        { "type": "text", "name": "L", "content": "Ver especificaciones →", "fontSize": 12, "fontWeight": "bold", "fill": PLAT_EMERALD_LIGHT }
                    ]},
                    { "type": "frame", "name": "C2", "width": 433, "height": 240, "cornerRadius": 12, "fill": photo_fill(IMG_SOLAR_FARM), "stroke": PLAT_BORDER_SUBTLE, "strokeWidth": 1, "padding": [18, 18], "layout": "vertical", "justifyContent": "space_between", "children": [
                        { "type": "text", "name": "Tag", "content": "ENERGÍAS RENOVABLES", "fontSize": 10, "fontWeight": "bold", "fill": PLAT_EMERALD_LIGHT },
                        { "type": "text", "name": "T", "content": "Protección Perimetral para Plantas Fotovoltaicas", "fontSize": 16, "fontWeight": "700", "fill": "#FFFFFF" },
                        { "type": "text", "name": "L", "content": "Ver ingeniería perimetral →", "fontSize": 12, "fontWeight": "bold", "fill": PLAT_EMERALD_LIGHT }
                    ]},
                    { "type": "frame", "name": "C3", "width": 433, "height": 240, "cornerRadius": 12, "fill": photo_fill(IMG_CONTROL_ROOM), "stroke": PLAT_BORDER_SUBTLE, "strokeWidth": 1, "padding": [18, 18], "layout": "vertical", "justifyContent": "space_between", "children": [
                        { "type": "text", "name": "Tag", "content": "CENTRAL PROPIA 24/7", "fontSize": 10, "fontWeight": "bold", "fill": "#CBD5E1" },
                        { "type": "text", "name": "T", "content": "Custodia Blindada y Despacho Inmediato", "fontSize": 16, "fontWeight": "700", "fill": "#FFFFFF" },
                        { "type": "text", "name": "L", "content": "Protocolo de custodia →", "fontSize": 12, "fontWeight": "bold", "fill": PLAT_EMERALD_LIGHT }
                    ]}
                ]}
            ]},
            plat_footer()
        ]
    }

def build_s3_nosotros(x, y):
    return {
        "type": "frame", "id": "s3-p2-nosotros", "name": "🟢 S3.2: Identidad Institucional (Platinum Executive)",
        "x": x, "y": y, "width": 1440, "height": 2000, "fill": PLAT_BG, "layout": "vertical", "clip": True, "children": [
            plat_header("Institucional"),
            { "type": "frame", "name": "Hero Nosotros", "width": "fill_container", "height": 440, "fill": photo_fill(IMG_OFFICE_HQ, "#0B0F1944", "#0B0F19F8"), "layout": "vertical", "padding": [56, 64], "justifyContent": "center", "gap": 14, "children": [
                { "type": "frame", "name": "Tag", "height": 26, "padding": [0, 12], "fill": "#05966933", "stroke": PLAT_BORDER, "strokeWidth": 1, "cornerRadius": 14, "alignItems": "center", "children": [
                    { "type": "text", "name": "T", "content": "ÉTICA EMPRESARIAL Y TRANSPARENCIA TOTAL", "fontSize": 11, "fontWeight": "bold", "fill": PLAT_EMERALD_LIGHT }
                ]},
                { "type": "text", "name": "H1", "content": "Compromiso de Solvencia, Ingeniería Rigurosa y Equipos en Propiedad", "fontSize": 36, "fontWeight": "800", "fill": "#FFFFFF", "lineHeight": 1.2, "width": 800 },
                { "type": "text", "name": "D", "content": "Desarrollos y Sistemas Inteligentes S.L. defiende un modelo transparente: el cliente adquiere sus equipos de seguridad en propiedad y mantiene el control total de sus instalaciones sin penalizaciones abusivas ni cláusulas de rescisión ocultas.", "fontSize": 14, "fill": "#94A3B8", "lineHeight": 1.6, "width": 750 }
            ]},
            { "type": "frame", "name": "Pilares", "width": "fill_container", "layout": "horizontal", "padding": [48, 48], "gap": 24, "children": [
                { "type": "frame", "name": "P1", "width": 433, "height": 260, "fill": PLAT_SURFACE, "stroke": PLAT_BORDER, "strokeWidth": 1.5, "cornerRadius": 12, "padding": [22, 22], "layout": "vertical", "gap": 10, "children": [
                    { "type": "icon", "name": "I", "library": "lucide", "icon": "shield-check", "width": 30, "height": 30, "fill": PLAT_EMERALD_LIGHT },
                    { "type": "text", "name": "T", "content": "Propiedad Garantizada al 100%", "fontSize": 17, "fontWeight": "bold", "fill": "#FFFFFF" },
                    { "type": "text", "name": "D", "content": "Los equipos son patrimonio de su empresa. Sin cuotas de alquiler perpetuas ni costes de desinstalación forzada.", "fontSize": 12, "fill": "#94A3B8", "lineHeight": 1.5 }
                ]},
                { "type": "frame", "name": "P2", "width": 433, "height": 260, "fill": PLAT_SURFACE, "stroke": PLAT_BORDER_SUBTLE, "strokeWidth": 1, "cornerRadius": 12, "padding": [22, 22], "layout": "vertical", "gap": 10, "children": [
                    { "type": "icon", "name": "I", "library": "lucide", "icon": "award", "width": 30, "height": 30, "fill": PLAT_GOLD },
                    { "type": "text", "name": "T", "content": "Ingenieros Colegiados Sénior", "fontSize": 17, "fontWeight": "bold", "fill": "#FFFFFF" },
                    { "type": "text", "name": "D", "content": "Cada proyecto es visado y dirigido por ingenieros colegiados especialistas en seguridad física, electrónica y contra incendios.", "fontSize": 12, "fill": "#94A3B8", "lineHeight": 1.5 }
                ]},
                { "type": "frame", "name": "P3", "width": 433, "height": 260, "fill": PLAT_SURFACE, "stroke": PLAT_BORDER_SUBTLE, "strokeWidth": 1, "cornerRadius": 12, "padding": [22, 22], "layout": "vertical", "gap": 10, "children": [
                    { "type": "icon", "name": "I", "library": "lucide", "icon": "building-2", "width": 30, "height": 30, "fill": "#CBD5E1" },
                    { "type": "text", "name": "T", "content": "Sede Central en Murcia", "fontSize": 17, "fontWeight": "bold", "fill": "#FFFFFF" },
                    { "type": "text", "name": "D", "content": "Instalaciones propias en Molina de Segura con stock permanente de repuestos para garantizar asistencia técnica en menos de 2 horas.", "fontSize": 12, "fill": "#94A3B8", "lineHeight": 1.5 }
                ]}
            ]},
            plat_footer()
        ]
    }

def build_s3_sectores(x, y):
    return {
        "type": "frame", "id": "s3-p3-sectores", "name": "🟢 S3.3: Portfolio de Sectores (Platinum Executive)",
        "x": x, "y": y, "width": 1440, "height": 2200, "fill": PLAT_BG, "layout": "vertical", "clip": True, "children": [
            plat_header("Sectores"),
            { "type": "frame", "name": "Sec Header", "width": "fill_container", "height": 220, "fill": PLAT_SURFACE, "layout": "vertical", "padding": [40, 48], "justifyContent": "center", "gap": 8, "children": [
                { "type": "text", "name": "Eye", "content": "ESPECIALIZACIÓN TÉCNICA POR SECTORES DE ALTO RIESGO", "fontSize": 12, "fontWeight": "800", "fill": PLAT_EMERALD_LIGHT },
                { "type": "text", "name": "H1", "content": "Protección a Medida para Cada Actividad Económica", "fontSize": 34, "fontWeight": "800", "fill": "#FFFFFF" },
                { "type": "text", "name": "D", "content": "Adecuación integral a los requisitos específicos de las compañías aseguradoras y de la normativa de seguridad privada.", "fontSize": 14, "fill": "#94A3B8" }
            ]},
            { "type": "frame", "name": "Services List", "width": "fill_container", "layout": "vertical", "padding": [40, 48], "gap": 24, "children": [
                { "type": "frame", "name": "S1", "width": "fill_container", "height": 200, "fill": PLAT_CARD, "stroke": PLAT_BORDER, "strokeWidth": 1.5, "cornerRadius": 12, "layout": "horizontal", "clip": True, "children": [
                    { "type": "frame", "name": "Img", "width": 320, "height": 200, "fill": photo_fill(IMG_JEWELRY_VAULT) },
                    { "type": "frame", "name": "Body", "width": 970, "padding": [20, 28], "layout": "vertical", "justifyContent": "space_between", "children": [
                        { "type": "frame", "name": "Top", "layout": "horizontal", "justifyContent": "space_between", "children": [
                            { "type": "text", "name": "T", "content": "01. Joyerías, Banca, Armerías y Administraciones de Lotería", "fontSize": 18, "fontWeight": "bold", "fill": "#FFFFFF" },
                            { "type": "text", "name": "Tag", "content": "GRADO 3 OBLIGATORIO", "fontSize": 10, "fontWeight": "bold", "fill": PLAT_GOLD }
                        ]},
                        { "type": "text", "name": "D", "content": "Instalación de detectores sísmicos en recintos acorazados, generadores de niebla de disparo instantáneo que impiden la visión en 3 segundos y doble vía de comunicación supervisada con CRA.", "fontSize": 12, "fill": "#94A3B8", "lineHeight": 1.4 },
                        { "type": "frame", "name": "Specs", "layout": "horizontal", "gap": 20, "children": [
                            { "type": "text", "name": "S1", "content": "✓ Homologación ministerial DGP Nº 2341", "fontSize": 12, "fontWeight": "bold", "fill": PLAT_EMERALD_LIGHT },
                            { "type": "text", "name": "S2", "content": "✓ Certificado de conexión a CRA", "fontSize": 12, "fontWeight": "bold", "fill": PLAT_EMERALD_LIGHT }
                        ]}
                    ]}
                ]},
                { "type": "frame", "name": "S2", "width": "fill_container", "height": 200, "fill": PLAT_CARD, "stroke": PLAT_BORDER_SUBTLE, "strokeWidth": 1, "cornerRadius": 12, "layout": "horizontal", "clip": True, "children": [
                    { "type": "frame", "name": "Img", "width": 320, "height": 200, "fill": photo_fill(IMG_SOLAR_FARM) },
                    { "type": "frame", "name": "Body", "width": 970, "padding": [20, 28], "layout": "vertical", "justifyContent": "space_between", "children": [
                        { "type": "frame", "name": "Top", "layout": "horizontal", "justifyContent": "space_between", "children": [
                            { "type": "text", "name": "T", "content": "02. Parques Solares y Plantas Fotovoltaicas de Gran Extensión", "fontSize": 18, "fontWeight": "bold", "fill": "#FFFFFF" },
                            { "type": "text", "name": "Tag", "content": "PERÍMETROS DE HASTA 100 HAS", "fontSize": 10, "fontWeight": "bold", "fill": PLAT_EMERALD_LIGHT }
                        ]},
                        { "type": "text", "name": "D", "content": "Protección perimetral mediante cámaras térmicas duales, radares perimétricos y cable sensor microfónico sobre vallado con análisis de vibración para evitar el robo de cable de cobre y paneles.", "fontSize": 12, "fill": "#94A3B8", "lineHeight": 1.4 },
                        { "type": "frame", "name": "Specs", "layout": "horizontal", "gap": 20, "children": [
                            { "type": "text", "name": "S1", "content": "✓ Detección a más de 1.000m", "fontSize": 12, "fontWeight": "bold", "fill": PLAT_EMERALD_LIGHT },
                            { "type": "text", "name": "S2", "content": "✓ Inmune a condiciones meteorológicas", "fontSize": 12, "fontWeight": "bold", "fill": PLAT_EMERALD_LIGHT }
                        ]}
                    ]}
                ]}
            ]},
            plat_footer()
        ]
    }

def build_s3_webapp_hub(x, y):
    return {
        "type": "frame", "id": "s3-p4-webapp-hub", "name": "🟢 S3.4: Executive Security Hub (Platinum Executive)",
        "x": x, "y": y, "width": 1440, "height": 1024, "fill": "#0A0E17", "layout": "horizontal", "clip": True, "children": [
            { "type": "frame", "name": "Executive Sidebar", "width": 250, "height": 1024, "fill": "#111827", "stroke": PLAT_BORDER_SUBTLE, "strokeWidth": { "right": 1 }, "layout": "vertical", "padding": [20, 16], "justifyContent": "space_between", "children": [
                { "type": "frame", "name": "Top", "layout": "vertical", "gap": 24, "children": [
                    logo_card((160, 42)),
                    { "type": "frame", "name": "Nav Items", "layout": "vertical", "gap": 8, "children": [
                        { "type": "frame", "name": "Item 1 Active", "height": 40, "fill": "#05966933", "stroke": PLAT_BORDER, "strokeWidth": 1, "cornerRadius": 8, "padding": [0, 12], "layout": "horizontal", "gap": 10, "alignItems": "center", "children": [
                            { "type": "icon", "name": "I", "library": "lucide", "icon": "building", "width": 18, "height": 18, "fill": PLAT_EMERALD_LIGHT },
                            { "type": "text", "name": "T", "content": "Multi-Site Overview", "fontSize": 13, "fontWeight": "bold", "fill": "#FFFFFF" }
                        ]},
                        { "type": "frame", "name": "Item 2", "height": 40, "padding": [0, 12], "layout": "horizontal", "gap": 10, "alignItems": "center", "children": [
                            { "type": "icon", "name": "I", "library": "lucide", "icon": "file-check", "width": 18, "height": 18, "fill": "#64748B" },
                            { "type": "text", "name": "T", "content": "Auditoría de Accesos", "fontSize": 13, "fill": "#94A3B8" }
                        ]},
                        { "type": "frame", "name": "Item 3", "height": 40, "padding": [0, 12], "layout": "horizontal", "gap": 10, "alignItems": "center", "children": [
                            { "type": "icon", "name": "I", "library": "lucide", "icon": "wrench", "width": 18, "height": 18, "fill": "#64748B" },
                            { "type": "text", "name": "T", "content": "Mantenimientos SLA", "fontSize": 13, "fill": "#94A3B8" }
                        ]},
                        { "type": "frame", "name": "Item 4", "height": 40, "padding": [0, 12], "layout": "horizontal", "gap": 10, "alignItems": "center", "children": [
                            { "type": "icon", "name": "I", "library": "lucide", "icon": "file-down", "width": 18, "height": 18, "fill": "#64748B" },
                            { "type": "text", "name": "T", "content": "Informes PDF / Policía", "fontSize": 13, "fill": "#94A3B8" }
                        ]}
                    ]}
                ]},
                { "type": "frame", "name": "User Box", "height": 56, "fill": "#1F2937", "cornerRadius": 8, "padding": [8, 12], "layout": "horizontal", "gap": 10, "alignItems": "center", "children": [
                    { "type": "ellipse", "name": "Avatar", "width": 34, "height": 34, "fill": PLAT_EMERALD },
                    { "type": "frame", "name": "Txt", "layout": "vertical", "gap": 2, "children": [
                        { "type": "text", "name": "Name", "content": "D. Carlos Benítez", "fontSize": 12, "fontWeight": "bold", "fill": "#FFFFFF" },
                        { "type": "text", "name": "Role", "content": "Director de Seguridad", "fontSize": 10, "fill": PLAT_EMERALD_LIGHT }
                    ]}
                ]}
            ]},
            { "type": "frame", "name": "Workspace", "width": 1190, "height": 1024, "layout": "vertical", "children": [
                { "type": "frame", "name": "Topbar App", "width": "fill_container", "height": 68, "fill": "#111827", "stroke": PLAT_BORDER_SUBTLE, "strokeWidth": { "bottom": 1 }, "layout": "horizontal", "padding": [0, 32], "alignItems": "center", "justifyContent": "space_between", "children": [
                    { "type": "frame", "name": "Corp Selector", "layout": "horizontal", "gap": 12, "alignItems": "center", "children": [
                        { "type": "text", "name": "Corp", "content": "🏢 Grupo Corporativo Levante (14 Sedes Protegidas)", "fontSize": 14, "fontWeight": "bold", "fill": "#FFFFFF" },
                        { "type": "frame", "name": "Status Pill", "padding": [4, 10], "fill": "#05966926", "stroke": PLAT_EMERALD, "strokeWidth": 1, "cornerRadius": 12, "children": [
                            { "type": "text", "name": "T", "content": "● 100% OPERATIVO · AUDITORÍA OK", "fontSize": 10, "fontWeight": "bold", "fill": PLAT_EMERALD_LIGHT }
                        ]}
                    ]},
                    { "type": "frame", "name": "Export Report", "height": 38, "padding": [0, 16], "fill": PLAT_EMERALD, "cornerRadius": 6, "alignItems": "center", "justifyContent": "center", "children": [
                        { "type": "text", "name": "T", "content": "Descargar Informe Pericial PDF", "fontSize": 12, "fontWeight": "bold", "fill": "#FFFFFF" }
                    ]}
                ]},
                { "type": "frame", "name": "Grid", "width": "fill_container", "layout": "horizontal", "padding": [24, 32], "gap": 24, "children": [
                    { "type": "frame", "name": "Sites Table", "width": 760, "height": 860, "fill": PLAT_CARD, "stroke": PLAT_BORDER_SUBTLE, "strokeWidth": 1, "cornerRadius": 10, "padding": [20, 20], "layout": "vertical", "gap": 16, "children": [
                        { "type": "text", "name": "T", "content": "Estado de Seguridad por Sedes Corporativas", "fontSize": 15, "fontWeight": "bold", "fill": "#FFFFFF" },
                        { "type": "frame", "name": "Site 1", "height": 70, "fill": "#111827", "cornerRadius": 8, "padding": [12, 16], "layout": "horizontal", "justifyContent": "space_between", "alignItems": "center", "children": [
                            { "type": "frame", "name": "L", "layout": "vertical", "gap": 2, "children": [
                                { "type": "text", "name": "N", "content": "1. Sede Central Pol. Ind. La Polvorista (Molina)", "fontSize": 13, "fontWeight": "bold", "fill": "#FFFFFF" },
                                { "type": "text", "name": "S", "content": "Grado 3 · 24 Cámaras IA · CRA Conectada", "fontSize": 11, "fill": "#94A3B8" }
                            ]},
                            { "type": "text", "name": "St", "content": "ARMADO GRADO 3", "fontSize": 11, "fontWeight": "bold", "fill": PLAT_EMERALD_LIGHT }
                        ]},
                        { "type": "frame", "name": "Site 2", "height": 70, "fill": "#111827", "cornerRadius": 8, "padding": [12, 16], "layout": "horizontal", "justifyContent": "space_between", "alignItems": "center", "children": [
                            { "type": "frame", "name": "L", "layout": "vertical", "gap": 2, "children": [
                                { "type": "text", "name": "N", "content": "2. Plataforma Logística Puerto de Cartagena", "fontSize": 13, "fontWeight": "bold", "fill": "#FFFFFF" },
                                { "type": "text", "name": "S", "content": "Grado 3 · 16 Cámaras LPR · Barreras Activas", "fontSize": 11, "fill": "#94A3B8" }
                            ]},
                            { "type": "text", "name": "St", "content": "ARMADO GRADO 3", "fontSize": 11, "fontWeight": "bold", "fill": PLAT_EMERALD_LIGHT }
                        ]},
                        { "type": "frame", "name": "Site 3", "height": 70, "fill": "#111827", "cornerRadius": 8, "padding": [12, 16], "layout": "horizontal", "justifyContent": "space_between", "alignItems": "center", "children": [
                            { "type": "frame", "name": "L", "layout": "vertical", "gap": 2, "children": [
                                { "type": "text", "name": "N", "content": "3. Planta Solar Fortuna (40 Hectáreas)", "fontSize": 13, "fontWeight": "bold", "fill": "#FFFFFF" },
                                { "type": "text", "name": "S", "content": "Perimetral Térmico · Detección 1.200m", "fontSize": 11, "fill": "#94A3B8" }
                            ]},
                            { "type": "text", "name": "St", "content": "PERÍMETRO ACTIVO", "fontSize": 11, "fontWeight": "bold", "fill": PLAT_EMERALD_LIGHT }
                        ]}
                    ]},
                    { "type": "frame", "name": "Compliance Card", "width": 340, "height": 860, "layout": "vertical", "gap": 16, "children": [
                        { "type": "frame", "name": "Card 1", "width": "fill_container", "height": 280, "fill": PLAT_CARD, "stroke": PLAT_BORDER, "strokeWidth": 1.5, "cornerRadius": 10, "padding": [16, 16], "layout": "vertical", "justifyContent": "space_between", "children": [
                            { "type": "text", "name": "T", "content": "Cumplimiento Normativo Orden INT/316", "fontSize": 13, "fontWeight": "bold", "fill": "#FFFFFF" },
                            { "type": "text", "name": "Val", "content": "100% AUDITADO", "fontSize": 20, "fontWeight": "800", "fill": PLAT_EMERALD_LIGHT },
                            { "type": "text", "name": "D", "content": "Próxima revisión obligatoria trimestral: 14 de Noviembre de 2026. Libro de revisiones digitalizado en regla.", "fontSize": 11, "fill": "#94A3B8" }
                        ]}
                    ]}
                ]}
            ]}
        ]
    }

def build_s3_contacto(x, y):
    return {
        "type": "frame", "id": "s3-p5-contacto", "name": "🟢 S3.5: Consultoría & Sede (Platinum Executive)",
        "x": x, "y": y, "width": 1440, "height": 1400, "fill": PLAT_BG, "layout": "vertical", "clip": True, "children": [
            plat_header("Consultoría"),
            { "type": "frame", "name": "Hero Contact", "width": "fill_container", "height": 260, "fill": PLAT_SURFACE, "layout": "vertical", "padding": [40, 48], "justifyContent": "center", "gap": 8, "children": [
                { "type": "text", "name": "Eye", "content": "CANAL DE CONSULTORÍA CONFIDENCIAL", "fontSize": 12, "fontWeight": "800", "fill": PLAT_EMERALD_LIGHT },
                { "type": "text", "name": "H1", "content": "Atención Preferente a Directores de Seguridad", "fontSize": 34, "fontWeight": "800", "fill": "#FFFFFF" },
                { "type": "text", "name": "D", "content": "Agende una reunión técnica con nuestro director de ingeniería para proyectos de alta seguridad corporativa.", "fontSize": 14, "fill": "#94A3B8" }
            ]},
            { "type": "frame", "name": "Contact Grid", "width": "fill_container", "layout": "horizontal", "padding": [40, 48], "gap": 32, "children": [
                { "type": "frame", "name": "Cards Col", "width": 540, "layout": "vertical", "gap": 18, "children": [
                    { "type": "frame", "name": "C1 Phone", "height": 120, "fill": PLAT_CARD, "stroke": PLAT_BORDER, "strokeWidth": 1.5, "cornerRadius": 10, "padding": [18, 20], "layout": "vertical", "gap": 4, "children": [
                        { "type": "text", "name": "T", "content": "🏛️ Línea VIP y Dirección Técnica", "fontSize": 13, "fontWeight": "bold", "fill": PLAT_EMERALD_LIGHT },
                        { "type": "text", "name": "P", "content": "968 622 984", "fontSize": 22, "fontWeight": "800", "fill": "#FFFFFF" },
                        { "type": "text", "name": "S", "content": "Atención prioritaria y confidencial.", "fontSize": 11, "fill": "#94A3B8" }
                    ]},
                    { "type": "frame", "name": "C2 Sede", "height": 120, "fill": PLAT_CARD, "stroke": PLAT_BORDER_SUBTLE, "strokeWidth": 1, "cornerRadius": 10, "padding": [18, 20], "layout": "vertical", "gap": 4, "children": [
                        { "type": "text", "name": "T", "content": "📍 Sede Central Corporativa", "fontSize": 13, "fontWeight": "bold", "fill": "#FFFFFF" },
                        { "type": "text", "name": "P", "content": "Pol. Ind. La Polvorista, Molina de Segura", "fontSize": 15, "fontWeight": "700", "fill": "#FFFFFF" },
                        { "type": "text", "name": "S", "content": "Desarrollos y Sistemas Inteligentes S.L. · DGP 2341", "fontSize": 11, "fill": "#94A3B8" }
                    ]}
                ]},
                { "type": "frame", "name": "Form Container", "width": 770, "height": 400, "fill": PLAT_SURFACE, "stroke": PLAT_BORDER, "strokeWidth": 1.5, "cornerRadius": 12, "padding": [28, 28], "layout": "vertical", "justifyContent": "space_between", "children": [
                    { "type": "text", "name": "H2", "content": "Solicitud de Consultoría Técnica Bajo NDA", "fontSize": 18, "fontWeight": "bold", "fill": "#FFFFFF" },
                    { "type": "frame", "name": "F1", "height": 42, "fill": PLAT_BG, "stroke": PLAT_BORDER_SUBTLE, "strokeWidth": 1, "cornerRadius": 6, "padding": [0, 16], "layout": "horizontal", "alignItems": "center", "children": [
                        { "type": "text", "name": "P", "content": "Nombre y Cargo del Responsable de Seguridad", "fontSize": 12, "fill": "#64748B" }
                    ]},
                    { "type": "frame", "name": "F2", "height": 42, "fill": PLAT_BG, "stroke": PLAT_BORDER_SUBTLE, "strokeWidth": 1, "cornerRadius": 6, "padding": [0, 16], "layout": "horizontal", "alignItems": "center", "children": [
                        { "type": "text", "name": "P", "content": "Corporación / Razón Social / Actividad", "fontSize": 12, "fill": "#64748B" }
                    ]},
                    { "type": "frame", "name": "Submit", "height": 46, "fill": PLAT_EMERALD, "cornerRadius": 6, "alignItems": "center", "justifyContent": "center", "children": [
                        { "type": "text", "name": "T", "content": "Agendar Reunión Técnica Confidencial", "fontSize": 13, "fontWeight": "bold", "fill": "#FFFFFF" }
                    ]}
                ]}
            ]},
            plat_footer()
        ]
    }

def main():
    pen_path = "/Users/toni/Proyectos/Control61-Web/control61_modern_ui.pen"
    
    # Read existing pen document to preserve legacy frames
    try:
        with open(pen_path, "r", encoding="utf-8") as f:
            existing_doc = json.load(f)
    except Exception:
        existing_doc = { "version": "2.19", "children": [] }

    # Coordinates layout:
    # Suite 1 (Red Industrial): Y = 4000
    s1_screens = [
        build_s1_home(0, 4000),
        build_s1_nosotros(1550, 4000),
        build_s1_servicios(3100, 4000),
        build_s1_webapp_console(4650, 4000),
        build_s1_contacto(6200, 4000)
    ]
    
    # Suite 2 (Cyber SOC): Y = 7500
    s2_screens = [
        build_s2_home(0, 7500),
        build_s2_nosotros(1550, 7500),
        build_s2_soluciones(3100, 7500),
        build_s2_webapp_portal(4650, 7500),
        build_s2_contacto(6200, 7500)
    ]
    
    # Suite 3 (Platinum Executive): Y = 11000
    s3_screens = [
        build_s3_home(0, 11000),
        build_s3_nosotros(1550, 11000),
        build_s3_sectores(3100, 11000),
        build_s3_webapp_hub(4650, 11000),
        build_s3_contacto(6200, 11000)
    ]
    
    all_new_screens = s1_screens + s2_screens + s3_screens
    new_screen_ids = [s["id"] for s in all_new_screens]
    
    # Filter out any older duplicate screens if we re-run
    existing_children = [c for c in existing_doc.get("children", []) if c.get("id") not in new_screen_ids]
    
    combined_children = existing_children + all_new_screens
    existing_doc["children"] = combined_children
    
    with open(pen_path, "w", encoding="utf-8") as f:
        json.dump(existing_doc, f, indent=2, ensure_ascii=False)
    print(f"Updated {pen_path} with {len(combined_children)} total screens!")

    # Desktop synchronization via JS
    js_code = f"""
    const allScreens = {json.dumps(all_new_screens)};
    const insertedIds = [];
    for (const scr of allScreens) {{
        // Remove existing if any
        try {{ Delete(scr.id); }} catch(e) {{}}
        const newId = Insert(document, scr);
        insertedIds.push(newId);
    }}
    Print('Successfully inserted ' + insertedIds.length + ' screens across 3 suites into Pencil Canvas!');
    
    // Export all 15 screens to ./exports
    Export(insertedIds, 'png', './exports');
    Print('Exported all 15 screens to ./exports directory.');
    """
    
    cmd_input = f"""execute({{ input: {json.dumps(js_code)} }})\nsave()\nexit()\n"""
    
    env = os.environ.copy()
    env["PEN_CLI_KEY"] = "pencil_cli_aebcdc64faa119be3d732b81edf1af9229f7f20f"
    env["PATH"] = "/Users/toni/.npm-global/bin:/usr/local/bin:/usr/bin:/bin:/usr/sbin:/sbin"
    
    print("Syncing all 3 complete suites (15 screens) to Pencil Desktop...")
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

if __name__ == "__main__":
    main()
