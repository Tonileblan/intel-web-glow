import json
from generate_three_radical_suites import (
    official_brand_badge, suite1_header, suite1_footer, photo_bg,
    R_BG, R_SURFACE, R_CARD, R_CARD_ALT, R_RED, R_RED_BRIGHT, R_RED_GLOW,
    R_RED_BORDER, R_BORDER, R_TEXT, R_MUTED, R_AMBER, R_GREEN,
    IMG_WAREHOUSE_SECURITY, IMG_CCTV_TACTICAL, IMG_LOGISTICS_DOCK, IMG_FIRE_SYSTEMS,
    IMG_TEAM_ENGINEERING, IMG_CONTROL_CENTER
)
from build_radical_suite1 import build_s1_home

def build_s1_nosotros(y_pos=14500):
    return {
        "type": "frame",
        "name": "Suite 1: [02] Sobre Nosotros - Base Operativa La Polvorista",
        "x": 1500, "y": y_pos, "width": 1440, "height": 2300,
        "fill": R_BG, "layout": "vertical", "children": [
            suite1_header(active_nav="NOSOTROS"),
            # Hero Dossier
            { "type": "frame", "name": "Hero Dossier", "width": "fill_container", "fill": R_SURFACE, "padding": [56, 64], "layout": "vertical", "gap": 24, "children": [
                { "type": "frame", "name": "Dossier Tag", "fill": "#1F0A0D", "stroke": R_RED_BORDER, "strokeWidth": 1, "cornerRadius": 4, "padding": [4, 10], "layout": "horizontal", "gap": 6, "children": [
                    { "type": "text", "name": "T", "content": "DOSSIER OPERATIVO · REGISTRO DGP Nº 2341", "fontSize": 11, "fontWeight": "bold", "fill": R_RED_BRIGHT }
                ]},
                { "type": "text", "name": "H1", "content": "MANDO OPERATIVO & BASE DE OPERACIONES EN MURCIA", "fontSize": 38, "fontWeight": "900", "fill": "#FFFFFF" },
                { "type": "text", "name": "P", "content": "Control 61 (Desarrollos y Sistemas Inteligentes S.L.) opera desde su sede central en el Polígono Industrial La Polvorista de Molina de Segura, prestando servicios de seguridad física, ingeniería electrónica, conexión CRA y custodia armada para las principales empresas de la Región de Murcia y el arco mediterráneo.", "fontSize": 14, "lineHeight": 1.6, "fill": "#CBD5E1" }
            ]},
            # Section 1: Headquarters Details
            { "type": "frame", "name": "HQ Section", "width": "fill_container", "padding": [56, 64], "layout": "horizontal", "gap": 40, "children": [
                { "type": "frame", "name": "Left HQ Box", "width": 640, "fill": photo_bg(IMG_CONTROL_CENTER, "30", "F0"), "cornerRadius": 12, "padding": [36, 36], "layout": "vertical", "gap": 16, "children": [
                    { "type": "text", "name": "H", "content": "CENTRAL RECEPTORA DE ALARMAS PROPIA", "fontSize": 20, "fontWeight": "bold", "fill": "#FFFFFF" },
                    { "type": "text", "name": "T1", "content": "📍 C/ Brasil, Parcela 27, Nave 4 · Pol. Ind. La Polvorista", "fontSize": 13, "fontWeight": "600", "fill": R_RED_BRIGHT },
                    { "type": "text", "name": "D", "content": "Instalaciones blindadas con búnker de comunicaciones clase Grado 3, triple acometida eléctrica y enlace satelital ininterrumpido.", "fontSize": 13, "lineHeight": 1.5, "fill": "#CBD5E1" },
                    { "type": "frame", "name": "BadgeRow", "layout": "horizontal", "gap": 12, "children": [
                        { "type": "frame", "name": "B1", "fill": R_CARD, "cornerRadius": 4, "padding": [6, 10], "children": [{ "type": "text", "name": "t", "content": "24/7/365 Activo", "fontSize": 11, "fill": R_GREEN }] },
                        { "type": "frame", "name": "B2", "fill": R_CARD, "cornerRadius": 4, "padding": [6, 10], "children": [{ "type": "text", "name": "t", "content": "Homologación Interior", "fontSize": 11, "fill": "#FFFFFF" }] }
                    ]}
                ]},
                { "type": "frame", "name": "Right Team Grid", "width": 640, "layout": "vertical", "gap": 16, "children": [
                    { "type": "frame", "name": "Team 1", "fill": R_CARD, "stroke": R_BORDER, "strokeWidth": 1, "cornerRadius": 8, "padding": [20, 20], "layout": "horizontal", "gap": 16, "alignItems": "center", "children": [
                        { "type": "ellipse", "name": "Av", "width": 48, "height": 48, "fill": "#2A1215" },
                        { "type": "frame", "name": "Inf", "layout": "vertical", "gap": 4, "children": [
                            { "type": "text", "name": "N", "content": "Dirección Técnica de Seguridad", "fontSize": 15, "fontWeight": "bold", "fill": "#FFFFFF" },
                            { "type": "text", "name": "R", "content": "Director de Seguridad Privada Habilitado (DGP Nº 2341)", "fontSize": 12, "fill": R_RED_BRIGHT }
                        ]}
                    ]},
                    { "type": "frame", "name": "Team 2", "fill": R_CARD, "stroke": R_BORDER, "strokeWidth": 1, "cornerRadius": 8, "padding": [20, 20], "layout": "horizontal", "gap": 16, "alignItems": "center", "children": [
                        { "type": "ellipse", "name": "Av", "width": 48, "height": 48, "fill": "#2A1215" },
                        { "type": "frame", "name": "Inf", "layout": "vertical", "gap": 4, "children": [
                            { "type": "text", "name": "N", "content": "Ingeniería de Sistemas & Redes", "fontSize": 15, "fontWeight": "bold", "fill": "#FFFFFF" },
                            { "type": "text", "name": "R", "content": "Especialistas en CCTV Térmico, Fibra Óptica y Control de Accesos", "fontSize": 12, "fill": "#94A3B8" }
                        ]}
                    ]},
                    { "type": "frame", "name": "Team 3", "fill": R_CARD, "stroke": R_BORDER, "strokeWidth": 1, "cornerRadius": 8, "padding": [20, 20], "layout": "horizontal", "gap": 16, "alignItems": "center", "children": [
                        { "type": "ellipse", "name": "Av", "width": 48, "height": 48, "fill": "#2A1215" },
                        { "type": "frame", "name": "Inf", "layout": "vertical", "gap": 4, "children": [
                            { "type": "text", "name": "N", "content": "Operadores de CRA & Despacho Táctico", "fontSize": 15, "fontWeight": "bold", "fill": "#FFFFFF" },
                            { "type": "text", "name": "R", "content": "Personal acreditado con formación continua en gestión de crisis", "fontSize": 12, "fill": "#94A3B8" }
                        ]}
                    ]}
                ]}
            ]},
            suite1_footer()
        ]
    }

def build_s1_servicios(y_pos=14500):
    return {
        "type": "frame",
        "name": "Suite 1: [03] Servicios y Sistemas Grado 3 - Control 61",
        "x": 3000, "y": y_pos, "width": 1440, "height": 2500,
        "fill": R_BG, "layout": "vertical", "children": [
            suite1_header(active_nav="SISTEMAS"),
            # Hero
            { "type": "frame", "name": "Hero", "width": "fill_container", "fill": R_SURFACE, "padding": [56, 64], "layout": "vertical", "gap": 16, "children": [
                { "type": "text", "name": "T", "content": "CATÁLOGO TÉCNICO DE SISTEMAS HOMOLOGADOS", "fontSize": 36, "fontWeight": "900", "fill": "#FFFFFF" },
                { "type": "text", "name": "Sub", "content": "Equipos certificados según la normativa UNE-EN 50131 para establecimientos obligados y naves de alto riesgo.", "fontSize": 14, "fill": "#94A3B8" }
            ]},
            # Table Specification Matrix
            { "type": "frame", "name": "Spec Table Frame", "width": "fill_container", "padding": [48, 64], "layout": "vertical", "gap": 24, "children": [
                { "type": "text", "name": "H", "content": "COMPARATIVA NORMATIVA: GRADO 2 VS GRADO 3 OBLIGATORIO", "fontSize": 20, "fontWeight": "bold", "fill": R_RED_BRIGHT },
                # Table
                { "type": "frame", "name": "Table", "width": "fill_container", "fill": R_CARD, "stroke": R_BORDER, "strokeWidth": 1, "cornerRadius": 8, "layout": "vertical", "children": [
                    # Header Row
                    { "type": "frame", "name": "TR Head", "width": "fill_container", "height": 48, "fill": R_SURFACE, "layout": "horizontal", "padding": [0, 24], "alignItems": "center", "children": [
                        { "type": "text", "name": "C1", "content": "REQUISITO TÉCNICO / NORMATIVO", "width": 450, "fontSize": 11, "fontWeight": "bold", "fill": "#64748B" },
                        { "type": "text", "name": "C2", "content": "GRADO 2 (Comercio Estándar)", "width": 380, "fontSize": 11, "fontWeight": "bold", "fill": "#94A3B8" },
                        { "type": "text", "name": "C3", "content": "GRADO 3 (Naves / Joyerías / Obligados)", "width": 400, "fontSize": 11, "fontWeight": "bold", "fill": R_RED_BRIGHT }
                    ]},
                    # Rows
                    { "type": "frame", "name": "R1", "width": "fill_container", "height": 52, "stroke": R_BORDER, "strokeWidth": { "top": 1 }, "layout": "horizontal", "padding": [0, 24], "alignItems": "center", "children": [
                        { "type": "text", "name": "c1", "content": "Vías de Comunicación con CRA", "width": 450, "fontSize": 13, "fontWeight": "bold", "fill": "#FFFFFF" },
                        { "type": "text", "name": "c2", "content": "1 sola vía (IP o GSM estándar)", "width": 380, "fontSize": 13, "fill": "#94A3B8" },
                        { "type": "text", "name": "c3", "content": "Doble vía supervisada (Fibra + 4G con polling <30s)", "width": 400, "fontSize": 13, "fontWeight": "bold", "fill": "#10B981" }
                    ]},
                    { "type": "frame", "name": "R2", "width": "fill_container", "height": 52, "stroke": R_BORDER, "strokeWidth": { "top": 1 }, "layout": "horizontal", "padding": [0, 24], "alignItems": "center", "children": [
                        { "type": "text", "name": "c1", "content": "Anti-Sabotaje / Anti-Enmascaramiento", "width": 450, "fontSize": 13, "fontWeight": "bold", "fill": "#FFFFFF" },
                        { "type": "text", "name": "c2", "content": "Opcional / Básico", "width": 380, "fontSize": 13, "fill": "#94A3B8" },
                        { "type": "text", "name": "c3", "content": "Obligatorio Grado 3 en todos los volumétricos", "width": 400, "fontSize": 13, "fontWeight": "bold", "fill": "#10B981" }
                    ]},
                    { "type": "frame", "name": "R3", "width": "fill_container", "height": 52, "stroke": R_BORDER, "strokeWidth": { "top": 1 }, "layout": "horizontal", "padding": [0, 24], "alignItems": "center", "children": [
                        { "type": "text", "name": "c1", "content": "Detectores Sísmicos en Bóvedas / Cajas", "width": 450, "fontSize": 13, "fontWeight": "bold", "fill": "#FFFFFF" },
                        { "type": "text", "name": "c2", "content": "No requerido", "width": 380, "fontSize": 13, "fill": "#94A3B8" },
                        { "type": "text", "name": "c3", "content": "Sensor piezoeléctrico homologado por norma", "width": 400, "fontSize": 13, "fontWeight": "bold", "fill": "#10B981" }
                    ]},
                    { "type": "frame", "name": "R4", "width": "fill_container", "height": 52, "stroke": R_BORDER, "strokeWidth": { "top": 1 }, "layout": "horizontal", "padding": [0, 24], "alignItems": "center", "children": [
                        { "type": "text", "name": "c1", "content": "Inspección y Mantenimiento Obligatorio", "width": 450, "fontSize": 13, "fontWeight": "bold", "fill": "#FFFFFF" },
                        { "type": "text", "name": "c2", "content": "Anual", "width": 380, "fontSize": 13, "fill": "#94A3B8" },
                        { "type": "text", "name": "c3", "content": "Trimestral con emisión de certificado oficial", "width": 400, "fontSize": 13, "fontWeight": "bold", "fill": "#10B981" }
                    ]}
                ]}
            ]},
            suite1_footer()
        ]
    }

def build_s1_webapp(y_pos=14500):
    """Real CAD/Blueprint floorplan interactive dispatch console."""
    return {
        "type": "frame",
        "name": "Suite 1: [04] Web App - Consola Táctica CAD Dispatcher",
        "x": 4500, "y": y_pos, "width": 1440, "height": 1024,
        "fill": "#0A0D15", "layout": "horizontal", "children": [
            # Left Tactical Sidebar
            { "type": "frame", "name": "Sidebar", "width": 280, "height": 1024, "fill": R_SURFACE, "stroke": R_BORDER, "strokeWidth": { "right": 1 }, "padding": [24, 20], "layout": "vertical", "justifyContent": "space_between", "children": [
                { "type": "frame", "name": "Top Part", "layout": "vertical", "gap": 20, "width": "fill_container", "children": [
                    official_brand_badge(width=180, height=44, bg="#FFFFFF"),
                    { "type": "frame", "name": "Facility Card", "fill": R_CARD, "stroke": R_RED_BORDER, "strokeWidth": 1, "cornerRadius": 6, "padding": [12, 12], "layout": "vertical", "gap": 4, "width": "fill_container", "children": [
                        { "type": "text", "name": "Lbl", "content": "INSTALACIÓN SELECCIONADA:", "fontSize": 10, "fontWeight": "bold", "fill": "#64748B" },
                        { "type": "text", "name": "Name", "content": "Nave Logística Polvorista 4", "fontSize": 13, "fontWeight": "bold", "fill": "#FFFFFF" },
                        { "type": "frame", "name": "StatusRow", "layout": "horizontal", "gap": 6, "alignItems": "center", "children": [
                            { "type": "ellipse", "name": "Dot", "width": 8, "height": 8, "fill": R_RED_BRIGHT },
                            { "type": "text", "name": "Arm", "content": "ESTADO: ARMADO TOTAL (GRADO 3)", "fontSize": 10, "fontWeight": "bold", "fill": "#FCA5A5" }
                        ]}
                    ]},
                    # Zone Selector
                    { "type": "frame", "name": "Zone Selector", "layout": "vertical", "gap": 6, "width": "fill_container", "children": [
                        { "type": "text", "name": "H", "content": "PARTICIONES Y ZONAS", "fontSize": 11, "fontWeight": "bold", "fill": "#64748B" },
                        { "type": "frame", "name": "Z1", "fill": R_CARD, "cornerRadius": 6, "padding": [10, 12], "layout": "horizontal", "justifyContent": "space_between", "width": "fill_container", "children": [
                            { "type": "text", "name": "T", "content": "Zona 1 · Oficinas / Dirección", "fontSize": 12, "fill": "#E2E8F0" },
                            { "type": "text", "name": "S", "content": "ARMADA", "fontSize": 11, "fontWeight": "bold", "fill": R_GREEN }
                        ]},
                        { "type": "frame", "name": "Z2", "fill": R_CARD, "cornerRadius": 6, "padding": [10, 12], "layout": "horizontal", "justifyContent": "space_between", "width": "fill_container", "children": [
                            { "type": "text", "name": "T", "content": "Zona 2 · Muelle de Carga Sur", "fontSize": 12, "fill": "#E2E8F0" },
                            { "type": "text", "name": "S", "content": "ARMADA", "fontSize": 11, "fontWeight": "bold", "fill": R_GREEN }
                        ]},
                        { "type": "frame", "name": "Z3", "fill": "#2D1217", "stroke": R_RED_BORDER, "strokeWidth": 1, "cornerRadius": 6, "padding": [10, 12], "layout": "horizontal", "justifyContent": "space_between", "width": "fill_container", "children": [
                            { "type": "text", "name": "T", "content": "Zona 3 · Perímetro Exterior", "fontSize": 12, "fontWeight": "bold", "fill": "#FCA5A5" },
                            { "type": "text", "name": "S", "content": "DISPARO", "fontSize": 11, "fontWeight": "bold", "fill": R_RED_BRIGHT }
                        ]}
                    ]}
                ]},
                # Bottom Panic Action
                { "type": "frame", "name": "Bot Panic", "width": "fill_container", "layout": "vertical", "gap": 10, "children": [
                    { "type": "frame", "name": "SmokeBtn", "height": 44, "fill": R_RED, "cornerRadius": 6, "alignItems": "center", "justifyContent": "center", "children": [
                        { "type": "text", "name": "T", "content": "⚡ DISPARAR NIEBLA ZONA 3", "fontSize": 12, "fontWeight": "bold", "fill": "#FFFFFF" }
                    ]},
                    { "type": "frame", "name": "PoliceBtn", "height": 40, "fill": "#1F2438", "stroke": R_BORDER, "strokeWidth": 1, "cornerRadius": 6, "alignItems": "center", "justifyContent": "center", "children": [
                        { "type": "text", "name": "T", "content": "🚨 AVISO POLICIAL URGENTE", "fontSize": 12, "fontWeight": "bold", "fill": "#F87171" }
                    ]}
                ]}
            ]},
            # Right CAD Workspace Area
            { "type": "frame", "name": "CAD Workspace", "width": 1160, "height": 1024, "layout": "vertical", "children": [
                # Top CAD Status Bar
                { "type": "frame", "name": "Top CAD Bar", "width": "fill_container", "height": 64, "fill": R_SURFACE, "stroke": R_BORDER, "strokeWidth": { "bottom": 1 }, "layout": "horizontal", "padding": [0, 32], "alignItems": "center", "justifyContent": "space_between", "children": [
                    { "type": "frame", "name": "Metrics", "layout": "horizontal", "gap": 24, "alignItems": "center", "children": [
                        { "type": "text", "name": "T1", "content": "📶 FIBRA PRIMARIA: 4ms", "fontSize": 11, "fontWeight": "bold", "fill": R_GREEN },
                        { "type": "text", "name": "T2", "content": "📡 BACKUP 4G: 100% COBERTURA", "fontSize": 11, "fontWeight": "bold", "fill": R_GREEN },
                        { "type": "text", "name": "T3", "content": "🔋 BATERÍAS PANEL: 99.8%", "fontSize": 11, "fontWeight": "bold", "fill": "#94A3B8" }
                    ]},
                    { "type": "frame", "name": "Op", "layout": "horizontal", "gap": 12, "alignItems": "center", "children": [
                        { "type": "ellipse", "name": "D", "width": 8, "height": 8, "fill": R_GREEN },
                        { "type": "text", "name": "N", "content": "Operador CRA: M. García (ID #412)", "fontSize": 12, "fontWeight": "600", "fill": "#FFFFFF" }
                    ]}
                ]},
                # Main Blueprint & Live Feed Split
                { "type": "frame", "name": "Blueprint View Area", "width": "fill_container", "height": 960, "padding": [24, 24], "layout": "horizontal", "gap": 20, "children": [
                    # 2D Floorplan CAD Canvas (Left 700px)
                    { "type": "frame", "name": "CAD Canvas", "width": 720, "height": 880, "fill": "#070B14", "stroke": "#1E293B", "strokeWidth": 2, "cornerRadius": 8, "padding": [24, 24], "layout": "vertical", "justifyContent": "space_between", "children": [
                        { "type": "frame", "name": "CAD Top", "width": "fill_container", "layout": "horizontal", "justifyContent": "space_between", "children": [
                            { "type": "text", "name": "CAD Title", "content": "PLANO ESQUEMÁTICO PLANTA BAJA (NAVE 4) · SENSORES ACTIVOS", "fontSize": 11, "fontWeight": "bold", "fill": "#64748B" },
                            { "type": "text", "name": "Scale", "content": "ESCALA 1:100", "fontSize": 11, "fill": "#475569" }
                        ]},
                        # Blueprint Schematic Box
                        { "type": "frame", "name": "Blueprint Box", "width": "fill_container", "height": 720, "fill": "#0A1020", "stroke": "#1E3A8A", "strokeWidth": 1, "cornerRadius": 6, "padding": [24, 24], "layout": "vertical", "justifyContent": "space_between", "children": [
                            # Top Warehouse Area
                            { "type": "frame", "name": "Area Norte", "width": "fill_container", "height": 200, "fill": "#0E1A33", "stroke": "#2563EB", "strokeWidth": 1, "padding": [16, 16], "layout": "horizontal", "justifyContent": "space_between", "children": [
                                { "type": "text", "name": "T", "content": "ZONA 1: ALMACÉN PALETS Y CÁMARA FRÍO", "fontSize": 12, "fontWeight": "bold", "fill": "#93C5FD" },
                                { "type": "frame", "name": "Sensor 1", "fill": "#064E3B", "cornerRadius": 4, "padding": [4, 8], "children": [{ "type": "text", "name": "t", "content": "PIR-01: OK", "fontSize": 10, "fill": "#34D399" }] }
                            ]},
                            # Middle Breach Area
                            { "type": "frame", "name": "Area Breach", "width": "fill_container", "height": 220, "fill": "#2E0E14", "stroke": R_RED_BRIGHT, "strokeWidth": 2, "padding": [16, 16], "layout": "vertical", "justifyContent": "space_between", "children": [
                                { "type": "frame", "name": "H", "width": "fill_container", "layout": "horizontal", "justifyContent": "space_between", "children": [
                                    { "type": "text", "name": "T", "content": "🚨 ZONA 3: PERÍMETRO VALLA ESTE (DISPARO ACTIVO)", "fontSize": 13, "fontWeight": "900", "fill": "#FCA5A5" },
                                    { "type": "frame", "name": "Badge", "fill": R_RED, "cornerRadius": 4, "padding": [4, 8], "children": [{ "type": "text", "name": "t", "content": "INTRUSIÓN EN CURSO", "fontSize": 10, "fontWeight": "bold", "fill": "#FFFFFF" }] }
                                ]},
                                { "type": "text", "name": "Desc", "content": "Barrera Infrarroja BI-03 cortada + Detección Térmica CAM-04 (Silueta Humana Confirmada)", "fontSize": 12, "fill": "#FECACA" },
                                { "type": "frame", "name": "Cam Cone", "fill": "#450A0A", "cornerRadius": 4, "padding": [8, 12], "layout": "horizontal", "gap": 8, "alignItems": "center", "children": [
                                    { "type": "text", "name": "c", "content": "📹 CAM-04 APUNTANDO A COORDENADA X:42 Y:18", "fontSize": 11, "fontWeight": "bold", "fill": "#FCA5A5" }
                                ]}
                            ]},
                            # Bottom Dock Area
                            { "type": "frame", "name": "Area Muelle", "width": "fill_container", "height": 180, "fill": "#0E1A33", "stroke": "#2563EB", "strokeWidth": 1, "padding": [16, 16], "layout": "horizontal", "justifyContent": "space_between", "children": [
                                { "type": "text", "name": "T", "content": "ZONA 2: MUELLES DE CARGA 1-4 (PUERTAS CERRADAS)", "fontSize": 12, "fontWeight": "bold", "fill": "#93C5FD" },
                                { "type": "frame", "name": "Mag", "fill": "#064E3B", "cornerRadius": 4, "padding": [4, 8], "children": [{ "type": "text", "name": "t", "content": "CONTACTOS: CERRADOS", "fontSize": 10, "fill": "#34D399" }] }
                            ]}
                        ]},
                        { "type": "text", "name": "B", "content": "Desarrollos y Sistemas Inteligentes S.L. · Telemetría Grado 3 en Vivo", "fontSize": 10, "fill": "#475569" }
                    ]},
                    # Right Incident Log & Patrol Dispatch (380px)
                    { "type": "frame", "name": "Incident Log Panel", "width": 380, "height": 880, "fill": R_CARD, "stroke": R_BORDER, "strokeWidth": 1, "cornerRadius": 8, "padding": [20, 20], "layout": "vertical", "gap": 16, "children": [
                        { "type": "text", "name": "Title", "content": "TERMINAL DE DESPACHO & EVENTOS", "fontSize": 14, "fontWeight": "bold", "fill": "#FFFFFF" },
                        # Patrol Map Card
                        { "type": "frame", "name": "Patrol Card", "width": "fill_container", "fill": R_SURFACE, "stroke": R_RED_BORDER, "strokeWidth": 1, "cornerRadius": 6, "padding": [14, 14], "layout": "vertical", "gap": 8, "children": [
                            { "type": "frame", "name": "H", "layout": "horizontal", "justifyContent": "space_between", "children": [
                                { "type": "text", "name": "p", "content": "🚔 PATRULLA ACUDA ASIGNADA", "fontSize": 11, "fontWeight": "bold", "fill": R_RED_BRIGHT },
                                { "type": "text", "name": "id", "content": "Unidad #P-04", "fontSize": 11, "fontWeight": "bold", "fill": "#FFFFFF" }
                            ]},
                            { "type": "text", "name": "Loc", "content": "Posición GPS: Avda. Principal La Polvorista", "fontSize": 12, "fill": "#CBD5E1" },
                            { "type": "text", "name": "ETA", "content": "Llegada Estimada: 2 min 45 seg (1.8 km)", "fontSize": 12, "fontWeight": "bold", "fill": R_GREEN }
                        ]},
                        # Live Log Events
                        { "type": "frame", "name": "Log Items", "width": "fill_container", "layout": "vertical", "gap": 8, "children": [
                            { "type": "frame", "name": "E1", "fill": "#2A0E13", "cornerRadius": 4, "padding": [8, 10], "layout": "vertical", "gap": 2, "children": [
                                { "type": "text", "name": "t", "content": "12:21:40 · Disparo Barrera BI-03", "fontSize": 11, "fontWeight": "bold", "fill": R_RED_BRIGHT },
                                { "type": "text", "name": "d", "content": "Corte de haz exterior. Verificación visual iniciada.", "fontSize": 11, "fill": "#E2E8F0" }
                            ]},
                            { "type": "frame", "name": "E2", "fill": R_SURFACE, "cornerRadius": 4, "padding": [8, 10], "layout": "vertical", "gap": 2, "children": [
                                { "type": "text", "name": "t", "content": "12:21:48 · Vídeo Confirmado Operador CRA", "fontSize": 11, "fontWeight": "bold", "fill": "#F59E0B" },
                                { "type": "text", "name": "d", "content": "Intruso intentando forzar puerta lateral.", "fontSize": 11, "fill": "#94A3B8" }
                            ]},
                            { "type": "frame", "name": "E3", "fill": R_SURFACE, "cornerRadius": 4, "padding": [8, 10], "layout": "vertical", "gap": 2, "children": [
                                { "type": "text", "name": "t", "content": "12:21:55 · Transmisión a 091 / 062", "fontSize": 11, "fontWeight": "bold", "fill": R_GREEN },
                                { "type": "text", "name": "d", "content": "Aviso con código de prioridad policial Grado 3.", "fontSize": 11, "fill": "#94A3B8" }
                            ]}
                        ]}
                    ]}
                ]}
            ]}
        ]
    }

def build_s1_contacto(y_pos=14500):
    return {
        "type": "frame",
        "name": "Suite 1: [05] Contacto y Auditoría Técnica - Control 61",
        "x": 6000, "y": y_pos, "width": 1440, "height": 1600,
        "fill": R_BG, "layout": "vertical", "children": [
            suite1_header(active_nav="AUDITORÍA"),
            # Main Form Section
            { "type": "frame", "name": "Form Section", "width": "fill_container", "padding": [64, 80], "layout": "horizontal", "gap": 64, "children": [
                { "type": "frame", "name": "Left Info", "width": 540, "layout": "vertical", "gap": 24, "children": [
                    official_brand_badge(width=160, height=48, bg="#FFFFFF"),
                    { "type": "text", "name": "H", "content": "AUDITORÍA DE SEGURIDAD IN-SITU EN MENOS DE 24 HORAS", "fontSize": 34, "fontWeight": "900", "fill": "#FFFFFF" },
                    { "type": "text", "name": "P", "content": "Un ingeniero colegiado de Control 61 visitará su instalación para evaluar vulnerabilidades perimetrales, puntos ciegos de CCTV y requisitos de homologación Grado 3.", "fontSize": 14, "lineHeight": 1.6, "fill": "#94A3B8" },
                    { "type": "frame", "name": "Direct Call", "fill": R_SURFACE, "stroke": R_RED_BORDER, "strokeWidth": 1, "cornerRadius": 8, "padding": [20, 20], "layout": "vertical", "gap": 6, "children": [
                        { "type": "text", "name": "T", "content": "TELÉFONO DE ATENCIÓN DIRECTA A EMPRESAS:", "fontSize": 11, "fontWeight": "bold", "fill": R_RED_BRIGHT },
                        { "type": "text", "name": "P", "content": "968 622 984", "fontSize": 24, "fontWeight": "900", "fill": "#FFFFFF" },
                        { "type": "text", "name": "H", "content": "Sede: Pol. Ind. La Polvorista, Molina de Segura", "fontSize": 12, "fill": "#64748B" }
                    ]}
                ]},
                # Form Card
                { "type": "frame", "name": "Form Card", "width": 640, "fill": R_CARD, "stroke": R_BORDER, "strokeWidth": 1, "cornerRadius": 12, "padding": [36, 36], "layout": "vertical", "gap": 20, "children": [
                    { "type": "text", "name": "Title", "content": "SOLICITUD DE AUDITORÍA Y PRESUPUESTO", "fontSize": 18, "fontWeight": "bold", "fill": "#FFFFFF" },
                    # Field 1
                    { "type": "frame", "name": "F1", "layout": "vertical", "gap": 6, "children": [
                        { "type": "text", "name": "L", "content": "Nombre de la Empresa / Razón Social", "fontSize": 12, "fontWeight": "600", "fill": "#CBD5E1" },
                        { "type": "frame", "name": "Input", "height": 46, "fill": R_SURFACE, "stroke": R_BORDER, "strokeWidth": 1, "cornerRadius": 6, "padding": [0, 16], "justifyContent": "center", "children": [
                            { "type": "text", "name": "p", "content": "Ej. Logística Levante S.L.", "fontSize": 13, "fill": "#475569" }
                        ]}
                    ]},
                    # Field 2
                    { "type": "frame", "name": "F2", "layout": "vertical", "gap": 6, "children": [
                        { "type": "text", "name": "L", "content": "Ubicación / Polígono Industrial", "fontSize": 12, "fontWeight": "600", "fill": "#CBD5E1" },
                        { "type": "frame", "name": "Input", "height": 46, "fill": R_SURFACE, "stroke": R_BORDER, "strokeWidth": 1, "cornerRadius": 6, "padding": [0, 16], "justifyContent": "center", "children": [
                            { "type": "text", "name": "p", "content": "Ej. Pol. Ind. La Polvorista, Parcela 12", "fontSize": 13, "fill": "#475569" }
                        ]}
                    ]},
                    # Field 3: Type of Facility
                    { "type": "frame", "name": "F3", "layout": "vertical", "gap": 6, "children": [
                        { "type": "text", "name": "L", "content": "Tipo de Instalación y Grado Requerido", "fontSize": 12, "fontWeight": "600", "fill": "#CBD5E1" },
                        { "type": "frame", "name": "Row", "layout": "horizontal", "gap": 10, "children": [
                            { "type": "frame", "name": "O1", "fill": R_SURFACE, "stroke": R_RED_BORDER, "strokeWidth": 1, "cornerRadius": 6, "padding": [10, 14], "children": [{ "type": "text", "name": "t", "content": "Nave Grado 3", "fontSize": 12, "fontWeight": "bold", "fill": R_RED_BRIGHT }] },
                            { "type": "frame", "name": "O2", "fill": R_SURFACE, "stroke": R_BORDER, "strokeWidth": 1, "cornerRadius": 6, "padding": [10, 14], "children": [{ "type": "text", "name": "t", "content": "Planta Solar", "fontSize": 12, "fill": "#94A3B8" }] },
                            { "type": "frame", "name": "O3", "fill": R_SURFACE, "stroke": R_BORDER, "strokeWidth": 1, "cornerRadius": 6, "padding": [10, 14], "children": [{ "type": "text", "name": "t", "content": "Joyería / Bancario", "fontSize": 12, "fill": "#94A3B8" }] }
                        ]}
                    ]},
                    # Submit
                    { "type": "frame", "name": "Submit", "height": 50, "fill": R_RED, "cornerRadius": 6, "alignItems": "center", "justifyContent": "center", "children": [
                        { "type": "text", "name": "t", "content": "SOLICITAR VISITA TÉCNICA INGENIERO →", "fontSize": 13, "fontWeight": "bold", "fill": "#FFFFFF" }
                    ]}
                ]}
            ]},
            suite1_footer()
        ]
    }

print("Suite 1 all 5 frames defined.")
