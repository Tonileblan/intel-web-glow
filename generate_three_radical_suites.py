import json
import subprocess
import os

# =============================================================================
# CONSTANTS & ASSETS
# =============================================================================
OFFICIAL_LOGO_URL = "https://control61.es/wp-content/uploads/2021/03/Logo-Limpio.png"
OFFICIAL_LOGO_URL_MED = "https://control61.es/wp-content/uploads/2021/03/Logo-Limpio-300x120.png"

# Curated High-Definition Security Assets
IMG_CCTV_TACTICAL = "https://images.unsplash.com/photo-1557597774-9d273605dfa9?auto=format&fit=crop&w=1600&q=80"
IMG_WAREHOUSE_SECURITY = "https://images.unsplash.com/photo-1586528116311-ad8dd3c8310d?auto=format&fit=crop&w=1600&q=80"
IMG_LOGISTICS_DOCK = "https://images.unsplash.com/photo-1545324418-cc1a3fa10c00?auto=format&fit=crop&w=1600&q=80"
IMG_CONTROL_CENTER = "https://images.unsplash.com/photo-1558494949-ef010cbdcc31?auto=format&fit=crop&w=1600&q=80"
IMG_CORPORATE_TOWER = "https://images.unsplash.com/photo-1486406146926-c627a92ad1ab?auto=format&fit=crop&w=1600&q=80"
IMG_DATA_CENTER = "https://images.unsplash.com/photo-1558494949-ef010cbdcc31?auto=format&fit=crop&w=1600&q=80"
IMG_BIOMETRIC_TURNSTILE = "https://images.unsplash.com/photo-1497366216548-37526070297c?auto=format&fit=crop&w=1600&q=80"
IMG_TEAM_ENGINEERING = "https://images.unsplash.com/photo-1521737604893-d14cc237f11d?auto=format&fit=crop&w=1600&q=80"
IMG_FIRE_SYSTEMS = "https://images.unsplash.com/photo-1517430816045-df4b7de01dbf?auto=format&fit=crop&w=1600&q=80"
IMG_SOLAR_PLANT = "https://images.unsplash.com/photo-1509391365360-2e959784a276?auto=format&fit=crop&w=1600&q=80"
IMG_BANK_VAULT = "https://images.unsplash.com/photo-1579546929518-9e396f3cc809?auto=format&fit=crop&w=1600&q=80"

def photo_bg(img_url, top_opacity="33", bot_opacity="F5", base_color="#070A11"):
    return [
        { "type": "image", "url": img_url, "mode": "fill" },
        {
            "type": "gradient",
            "gradientType": "linear",
            "rotation": 180,
            "colors": [
                { "color": f"{base_color}{top_opacity}", "position": 0 },
                { "color": f"{base_color}{bot_opacity}", "position": 1 }
            ]
        }
    ]

def official_brand_badge(width=175, height=46, bg="#FFFFFF", border="#E2E8F0"):
    """Creates a high-contrast brand badge displaying the authentic Control 61 logo with icon and typography."""
    return {
        "type": "frame",
        "name": "Official Control 61 Brand Badge",
        "width": width,
        "height": height,
        "fill": bg,
        "cornerRadius": 8,
        "stroke": border,
        "strokeWidth": 1,
        "padding": [4, 10],
        "layout": "horizontal",
        "alignItems": "center",
        "gap": 8,
        "children": [
            {
                "type": "frame",
                "name": "Logo Icon",
                "width": 32,
                "height": 32,
                "fill": "#DC2626",
                "cornerRadius": 6,
                "alignItems": "center",
                "justifyContent": "center",
                "children": [
                    { "type": "text", "name": "61", "content": "61", "fontSize": 15, "fontWeight": "900", "fill": "#FFFFFF" }
                ]
            },
            {
                "type": "frame",
                "name": "Brand Text",
                "layout": "vertical",
                "gap": 1,
                "children": [
                    {
                        "type": "frame",
                        "name": "Wordmark Row",
                        "layout": "horizontal",
                        "gap": 4,
                        "alignItems": "center",
                        "children": [
                            { "type": "text", "name": "CONTROL", "content": "CONTROL", "fontSize": 14, "fontWeight": "900", "fill": "#0F172A" },
                            { "type": "text", "name": "61", "content": "61", "fontSize": 15, "fontWeight": "900", "fill": "#DC2626" }
                        ]
                    },
                    { "type": "text", "name": "Sub", "content": "SISTEMAS DE SEGURIDAD", "fontSize": 7, "fontWeight": "700", "fill": "#64748B" }
                ]
            }
        ]
    }


# =============================================================================
# 🟥 SUITE 1: TACTICAL INDUSTRIAL DEFENSE (Red & High-Density Grid)
# =============================================================================
R_BG = "#08090E"
R_SURFACE = "#10121B"
R_CARD = "#161925"
R_CARD_ALT = "#1E2233"
R_RED = "#DC2626"
R_RED_BRIGHT = "#EF4444"
R_RED_GLOW = "#EF444433"
R_RED_BORDER = "#EF444455"
R_BORDER = "#252B40"
R_TEXT = "#F8FAFC"
R_MUTED = "#94A3B8"
R_AMBER = "#F59E0B"
R_GREEN = "#10B981"

def suite1_header(active_nav="Inicio"):
    nav_items = ["01. INICIO", "02. NOSOTROS", "03. SISTEMAS GRADO 3", "04. CONSOLA TÁCTICA", "05. AUDITORÍA"]
    links = []
    for item in nav_items:
        is_active = (active_nav in item or (active_nav == "Inicio" and "01" in item))
        links.append({
            "type": "text", "name": item, "content": item,
            "fontSize": 12, "fontWeight": "700" if is_active else "600",
            "fill": R_RED_BRIGHT if is_active else "#94A3B8"
        })
    return {
        "type": "frame", "name": "Header Tactical Industrial", "width": "fill_container", "layout": "vertical", "children": [
            { "type": "frame", "name": "Tactical Emergency Bar", "width": "fill_container", "height": 38, "fill": "#18090C", "stroke": R_RED_BORDER, "strokeWidth": { "bottom": 1 }, "layout": "horizontal", "padding": [0, 48], "alignItems": "center", "justifyContent": "space_between", "children": [
                { "type": "frame", "name": "Status", "layout": "horizontal", "gap": 10, "alignItems": "center", "children": [
                    { "type": "ellipse", "name": "Pulse", "width": 8, "height": 8, "fill": R_RED_BRIGHT },
                    { "type": "text", "name": "CRA Status", "content": "CENTRAL RECEPTORA DE ALARMAS 24/7/365 · HOMOLOGADA GRADO 3 · DGP Nº 2341", "fontSize": 11, "fontWeight": "bold", "fill": "#FCA5A5" }
                ]},
                { "type": "frame", "name": "Direct Call", "layout": "horizontal", "gap": 20, "alignItems": "center", "children": [
                    { "type": "text", "name": "Phone", "content": "🚨 LÍNEA DIRECTA 24H: 968 622 984", "fontSize": 12, "fontWeight": "bold", "fill": "#FFFFFF" },
                    { "type": "text", "name": "Sede", "content": "Sede: Pol. Ind. La Polvorista (Murcia)", "fontSize": 11, "fontWeight": "500", "fill": "#94A3B8" }
                ]}
            ]},
            { "type": "frame", "name": "Main Bar", "width": "fill_container", "height": 80, "fill": R_SURFACE, "stroke": R_BORDER, "strokeWidth": { "bottom": 1 }, "layout": "horizontal", "padding": [0, 48], "alignItems": "center", "justifyContent": "space_between", "children": [
                { "type": "frame", "name": "Brand", "layout": "horizontal", "gap": 14, "alignItems": "center", "children": [
                    official_brand_badge(width=150, height=44, bg="#FFFFFF"),
                    { "type": "frame", "name": "Divider", "width": 1, "height": 28, "fill": R_BORDER },
                    { "type": "frame", "name": "Tag", "layout": "vertical", "gap": 2, "children": [
                        { "type": "text", "name": "Title", "content": "DIVISIÓN INDUSTRIAL & CRA", "fontSize": 11, "fontWeight": "bold", "fill": R_RED_BRIGHT },
                        { "type": "text", "name": "Sub", "content": "Desarrollos y Sistemas Inteligentes S.L.", "fontSize": 10, "fontWeight": "500", "fill": "#64748B" }
                    ]}
                ]},
                { "type": "frame", "name": "Nav Links", "layout": "horizontal", "gap": 24, "alignItems": "center", "children": links },
                { "type": "frame", "name": "CTA", "height": 44, "fill": R_RED, "cornerRadius": 6, "padding": [0, 20], "alignItems": "center", "justifyContent": "center", "children": [
                    { "type": "text", "name": "Btn", "content": "SOLICITAR INTERVENCIÓN →", "fontSize": 12, "fontWeight": "bold", "fill": "#FFFFFF" }
                ]}
            ]}
        ]
    }

def suite1_footer():
    return {
        "type": "frame", "name": "Footer Industrial", "width": "fill_container", "fill": "#06070B", "stroke": R_BORDER, "strokeWidth": { "top": 1 }, "padding": [48, 64], "layout": "vertical", "gap": 32, "children": [
            { "type": "frame", "name": "Top Row", "width": "fill_container", "layout": "horizontal", "justifyContent": "space_between", "alignItems": "flex_start", "children": [
                { "type": "frame", "name": "Col 1", "layout": "vertical", "gap": 12, "width": 340, "children": [
                    official_brand_badge(width=160, height=46, bg="#FFFFFF"),
                    { "type": "text", "name": "Desc", "content": "Empresa de Seguridad Homologada por el Ministerio del Interior. Dirección General de la Policía DGP Nº 2341. Certificaciones RINA ISO 9001, ISO 14001 y ISO 45001.", "fontSize": 12, "lineHeight": 1.6, "fill": "#64748B" }
                ]},
                { "type": "frame", "name": "Col 2", "layout": "vertical", "gap": 10, "children": [
                    { "type": "text", "name": "Head", "content": "SISTEMAS HOMOLOGADOS", "fontSize": 12, "fontWeight": "bold", "fill": "#FFFFFF" },
                    { "type": "text", "name": "L1", "content": "• Alarmas Grado 3 para Naves", "fontSize": 12, "fill": "#94A3B8" },
                    { "type": "text", "name": "L2", "content": "• CCTV con Visión Térmica IA", "fontSize": 12, "fill": "#94A3B8" },
                    { "type": "text", "name": "L3", "content": "• Cañones de Niebla Zero-Vision", "fontSize": 12, "fill": "#94A3B8" },
                    { "type": "text", "name": "L4", "content": "• Protección Contra Incendios (PCI)", "fontSize": 12, "fill": "#94A3B8" }
                ]},
                { "type": "frame", "name": "Col 3", "layout": "vertical", "gap": 10, "children": [
                    { "type": "text", "name": "Head", "content": "SEDE OPERATIVA Y CRA", "fontSize": 12, "fontWeight": "bold", "fill": "#FFFFFF" },
                    { "type": "text", "name": "L1", "content": "📍 C/ Brasil, Parcela 27, Nave 4", "fontSize": 12, "fill": "#94A3B8" },
                    { "type": "text", "name": "L2", "content": "Pol. Ind. La Polvorista, 30500", "fontSize": 12, "fill": "#94A3B8" },
                    { "type": "text", "name": "L3", "content": "Molina de Segura (Murcia)", "fontSize": 12, "fill": "#94A3B8" },
                    { "type": "text", "name": "L4", "content": "📞 Centralita 24h: 968 622 984", "fontSize": 12, "fontWeight": "bold", "fill": R_RED_BRIGHT }
                ]}
            ]},
            { "type": "frame", "name": "Bottom Bar", "width": "fill_container", "layout": "horizontal", "justifyContent": "space_between", "stroke": "#1E293B", "strokeWidth": { "top": 1 }, "padding": [20, 0, 0, 0], "children": [
                { "type": "text", "name": "Legal", "content": "© 2026 Desarrollos y Sistemas Inteligentes S.L. · Todos los derechos reservados · Aviso Legal · RGPD", "fontSize": 11, "fill": "#475569" },
                { "type": "text", "name": "Cert", "content": "HOMOLOGACIÓN DGP Nº 2341 · GRADO 3 SEGURIDAD ALTA", "fontSize": 11, "fontWeight": "bold", "fill": R_RED_BRIGHT }
            ]}
        ]
    }

# =============================================================================
# 🟦 SUITE 2: CYBER-AI SOC & NEURAL VISION (Cobalt Blue & Floating Glass Island)
# =============================================================================
B_BG = "#030712"
B_SURFACE = "#0B1120"
B_CARD = "#111A30"
B_CARD_GLASS = "#0E1830CC"
B_COBALT = "#2563EB"
B_CYAN = "#06B6D4"
B_CYAN_GLOW = "#06B6D433"
B_BORDER = "#1E2E52"
B_BORDER_CYAN = "#06B6D455"
B_TEXT = "#F8FAFC"
B_MUTED = "#94A3B8"

def suite2_header(active_nav="Capacidades IA"):
    nav_items = ["Capacidades IA", "Neural Studio", "Arquitectura Cloud", "SOC 24h", "Contacto"]
    links = []
    for item in nav_items:
        is_active = (active_nav in item)
        links.append({
            "type": "text", "name": item, "content": item,
            "fontSize": 13, "fontWeight": "600" if is_active else "500",
            "fill": B_CYAN if is_active else "#94A3B8"
        })
    return {
        "type": "frame", "name": "Header Cyber Floating", "width": "fill_container", "padding": [24, 64], "alignItems": "center", "children": [
            { "type": "frame", "name": "Floating Glass Capsule", "width": "fill_container", "height": 68, "fill": B_CARD_GLASS, "stroke": B_BORDER_CYAN, "strokeWidth": 1, "cornerRadius": 34, "padding": [0, 24], "layout": "horizontal", "alignItems": "center", "justifyContent": "space_between", "children": [
                { "type": "frame", "name": "Brand", "layout": "horizontal", "gap": 12, "alignItems": "center", "children": [
                    official_brand_badge(width=140, height=40, bg="#FFFFFF"),
                    { "type": "frame", "name": "Pill", "fill": "#06B6D422", "stroke": B_BORDER_CYAN, "strokeWidth": 1, "cornerRadius": 12, "padding": [3, 8], "children": [
                        { "type": "text", "name": "V", "content": "NEURAL SOC V4", "fontSize": 10, "fontWeight": "bold", "fill": B_CYAN }
                    ]}
                ]},
                { "type": "frame", "name": "Links", "layout": "horizontal", "gap": 28, "alignItems": "center", "children": links },
                { "type": "frame", "name": "CTA", "layout": "horizontal", "gap": 12, "alignItems": "center", "children": [
                    { "type": "frame", "name": "Pulse", "width": 8, "height": 8, "cornerRadius": 4, "fill": "#10B981" },
                    { "type": "frame", "name": "LiveBtn", "height": 40, "fill": B_COBALT, "cornerRadius": 20, "padding": [0, 18], "alignItems": "center", "justifyContent": "center", "children": [
                        { "type": "text", "name": "Txt", "content": "Acceso Neural Portal →", "fontSize": 12, "fontWeight": "bold", "fill": "#FFFFFF" }
                    ]}
                ]}
            ]}
        ]
    }

def suite2_footer():
    return {
        "type": "frame", "name": "Footer Cyber", "width": "fill_container", "fill": "#02040A", "stroke": B_BORDER, "strokeWidth": { "top": 1 }, "padding": [56, 80], "layout": "vertical", "gap": 32, "children": [
            { "type": "frame", "name": "Top", "width": "fill_container", "layout": "horizontal", "justifyContent": "space_between", "children": [
                { "type": "frame", "name": "BrandCol", "width": 380, "layout": "vertical", "gap": 16, "children": [
                    official_brand_badge(width=160, height=46, bg="#FFFFFF"),
                    { "type": "text", "name": "Tag", "content": "Plataforma de Visión Artificial, Inferencia Edge y Telemetría SOC 24h para Grandes Instalaciones.", "fontSize": 13, "lineHeight": 1.6, "fill": "#94A3B8" }
                ]},
                { "type": "frame", "name": "C1", "layout": "vertical", "gap": 10, "children": [
                    { "type": "text", "name": "H", "content": "TECNOLOGÍA IA", "fontSize": 12, "fontWeight": "bold", "fill": B_CYAN },
                    { "type": "text", "name": "1", "content": "Deep Learning CCTV", "fontSize": 12, "fill": "#94A3B8" },
                    { "type": "text", "name": "2", "content": "Reconocimiento LPR / ANPR", "fontSize": 12, "fill": "#94A3B8" },
                    { "type": "text", "name": "3", "content": "Filtro 99.4% Falsas Alarmas", "fontSize": 12, "fill": "#94A3B8" }
                ]},
                { "type": "frame", "name": "C2", "layout": "vertical", "gap": 10, "children": [
                    { "type": "text", "name": "H", "content": "INFRAESTRUCTURA", "fontSize": 12, "fontWeight": "bold", "fill": B_CYAN },
                    { "type": "text", "name": "1", "content": "Cloud Híbrido Tier IV España", "fontSize": 12, "fill": "#94A3B8" },
                    { "type": "text", "name": "2", "content": "Cifrado AES-256 E2E", "fontSize": 12, "fill": "#94A3B8" },
                    { "type": "text", "name": "3", "content": "API REST & Webhooks", "fontSize": 12, "fill": "#94A3B8" }
                ]}
            ]},
            { "type": "frame", "name": "Bot", "width": "fill_container", "layout": "horizontal", "justifyContent": "space_between", "stroke": "#111827", "strokeWidth": { "top": 1 }, "padding": [20, 0, 0, 0], "children": [
                { "type": "text", "name": "L", "content": "© 2026 Control61 Neural Vision Systems · Desarrollos y Sistemas Inteligentes S.L. · DGP 2341", "fontSize": 11, "fill": "#4B5563" },
                { "type": "text", "name": "R", "content": "SLA UPTIME 99.99% · TIEMPO REAL INFERENCIA < 40MS", "fontSize": 11, "fontWeight": "bold", "fill": B_CYAN }
            ]}
        ]
    }

# =============================================================================
# 🟩 SUITE 3: PLATINUM EXECUTIVE DEFENSE (Titanium Slate, Tactical Emerald, Gold)
# =============================================================================
P_BG = "#0A0D14"
P_SURFACE = "#121722"
P_CARD = "#171E2D"
P_BORDER = "#253047"
P_EMERALD = "#059669"
P_EMERALD_LIGHT = "#10B981"
P_GOLD = "#D97706"
P_GOLD_LIGHT = "#F59E0B"
P_GOLD_BORDER = "#D9770655"
P_TEXT = "#F8FAFC"
P_MUTED = "#94A3B8"

def suite3_header(active_nav="Grandes Cuentas"):
    nav_items = ["Grandes Cuentas", "Infraestructuras Críticas", "Gobierno Corporativo", "Executive Hub", "Contacto VIP"]
    links = []
    for item in nav_items:
        is_active = (active_nav in item)
        links.append({
            "type": "text", "name": item, "content": item,
            "fontSize": 13, "fontWeight": "700" if is_active else "500",
            "fill": P_GOLD_LIGHT if is_active else "#94A3B8"
        })
    return {
        "type": "frame", "name": "Header Platinum Executive", "width": "fill_container", "layout": "vertical", "children": [
            { "type": "frame", "name": "Top Gold Bar", "width": "fill_container", "height": 34, "fill": "#07090E", "stroke": P_GOLD_BORDER, "strokeWidth": { "bottom": 1 }, "layout": "horizontal", "padding": [0, 64], "alignItems": "center", "justifyContent": "space_between", "children": [
                { "type": "text", "name": "Label", "content": "AUDITORÍA DE SEGURIDAD PRIVADA PARA COMITÉS DE DIRECCIÓN & CONSEJOS", "fontSize": 11, "fontWeight": "bold", "fill": "#FDE68A" },
                { "type": "text", "name": "Call", "content": "LÍNEA CONFIDENCIAL DIRECTA: 968 622 984", "fontSize": 11, "fontWeight": "bold", "fill": "#FFFFFF" }
            ]},
            { "type": "frame", "name": "Main Bar", "width": "fill_container", "height": 84, "fill": P_SURFACE, "stroke": P_BORDER, "strokeWidth": { "bottom": 1 }, "layout": "horizontal", "padding": [0, 64], "alignItems": "center", "justifyContent": "space_between", "children": [
                { "type": "frame", "name": "Brand", "layout": "horizontal", "gap": 16, "alignItems": "center", "children": [
                    official_brand_badge(width=160, height=46, bg="#FFFFFF"),
                    { "type": "frame", "name": "Sep", "width": 1, "height": 32, "fill": P_BORDER },
                    { "type": "frame", "name": "Title", "layout": "vertical", "gap": 2, "children": [
                        { "type": "text", "name": "H", "content": "SEGURIDAD ESTRATÉGICA & BLINDAJE", "fontSize": 11, "fontWeight": "bold", "fill": P_GOLD_LIGHT },
                        { "type": "text", "name": "S", "content": "Homologación DGP Nº 2341 · ISO 9001/14001/45001", "fontSize": 10, "fill": "#64748B" }
                    ]}
                ]},
                { "type": "frame", "name": "Nav Links", "layout": "horizontal", "gap": 26, "alignItems": "center", "children": links },
                { "type": "frame", "name": "CTA", "height": 44, "fill": P_GOLD, "cornerRadius": 6, "padding": [0, 20], "alignItems": "center", "justifyContent": "center", "children": [
                    { "type": "text", "name": "Btn", "content": "SOLICITAR PROPUESTA PRIVADA", "fontSize": 12, "fontWeight": "bold", "fill": "#FFFFFF" }
                ]}
            ]}
        ]
    }

def suite3_footer():
    return {
        "type": "frame", "name": "Footer Executive", "width": "fill_container", "fill": "#07090F", "stroke": P_BORDER, "strokeWidth": { "top": 1 }, "padding": [56, 80], "layout": "vertical", "gap": 32, "children": [
            { "type": "frame", "name": "Top", "width": "fill_container", "layout": "horizontal", "justifyContent": "space_between", "children": [
                { "type": "frame", "name": "BrandCol", "width": 380, "layout": "vertical", "gap": 14, "children": [
                    official_brand_badge(width=160, height=46, bg="#FFFFFF"),
                    { "type": "text", "name": "Desc", "content": "Proveedor de Seguridad Integral para Infraestructuras Críticas y Corporaciones. Desarrollos y Sistemas Inteligentes S.L. DGP 2341.", "fontSize": 12, "lineHeight": 1.6, "fill": "#64748B" }
                ]},
                { "type": "frame", "name": "Col2", "layout": "vertical", "gap": 10, "children": [
                    { "type": "text", "name": "H", "content": "CERTIFICACIONES OFICIALES", "fontSize": 12, "fontWeight": "bold", "fill": P_GOLD_LIGHT },
                    { "type": "text", "name": "1", "content": "• Certificación RINA ISO 9001:2015", "fontSize": 12, "fill": "#94A3B8" },
                    { "type": "text", "name": "2", "content": "• Certificación RINA ISO 14001:2015", "fontSize": 12, "fill": "#94A3B8" },
                    { "type": "text", "name": "3", "content": "• Certificación RINA ISO 45001:2018", "fontSize": 12, "fill": "#94A3B8" },
                    { "type": "text", "name": "4", "content": "• Homologación Grado 3 UNE-EN 50131", "fontSize": 12, "fill": "#94A3B8" }
                ]},
                { "type": "frame", "name": "Col3", "layout": "vertical", "gap": 10, "children": [
                    { "type": "text", "name": "H", "content": "COMPLIANCE & CONTACTO VIP", "fontSize": 12, "fontWeight": "bold", "fill": P_GOLD_LIGHT },
                    { "type": "text", "name": "1", "content": "Acuerdo de Confidencialidad (NDA)", "fontSize": 12, "fill": "#94A3B8" },
                    { "type": "text", "name": "2", "content": "Auditorías Forenses de Seguridad", "fontSize": 12, "fill": "#94A3B8" },
                    { "type": "text", "name": "3", "content": "Centralita Directa: 968 622 984", "fontSize": 12, "fontWeight": "bold", "fill": "#FFFFFF" }
                ]}
            ]},
            { "type": "frame", "name": "Bot", "width": "fill_container", "layout": "horizontal", "justifyContent": "space_between", "stroke": "#1E293B", "strokeWidth": { "top": 1 }, "padding": [20, 0, 0, 0], "children": [
                { "type": "text", "name": "L", "content": "© 2026 Desarrollos y Sistemas Inteligentes S.L. · Todos los derechos reservados", "fontSize": 11, "fill": "#475569" },
                { "type": "text", "name": "R", "content": "SEDE: POL. IND. LA POLVORISTA, MOLINA DE SEGURA (MURCIA)", "fontSize": 11, "fontWeight": "bold", "fill": P_EMERALD_LIGHT }
            ]}
        ]
    }

print("Headers, footers and badges initialized.")
