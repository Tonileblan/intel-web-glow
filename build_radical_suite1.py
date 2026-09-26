import json

# =============================================================================
# SUITE 1 BUILDER: TACTICAL INDUSTRIAL DEFENSE (RED & HIGH DENSITY GRID)
# =============================================================================
from generate_three_radical_suites import (
    official_brand_badge, suite1_header, suite1_footer, photo_bg,
    R_BG, R_SURFACE, R_CARD, R_CARD_ALT, R_RED, R_RED_BRIGHT, R_RED_GLOW,
    R_RED_BORDER, R_BORDER, R_TEXT, R_MUTED, R_AMBER, R_GREEN,
    IMG_WAREHOUSE_SECURITY, IMG_CCTV_TACTICAL, IMG_LOGISTICS_DOCK, IMG_FIRE_SYSTEMS
)

def build_s1_home(y_pos=14500):
    return {
        "type": "frame",
        "name": "Suite 1: [01] Home Tactical Industrial - Control 61",
        "x": 0, "y": y_pos, "width": 1440, "height": 3300,
        "fill": R_BG, "layout": "vertical", "children": [
            suite1_header(active_nav="Inicio"),
            # Hero Asymmetric Split
            { "type": "frame", "name": "Hero Tactical", "width": "fill_container", "fill": photo_bg(IMG_WAREHOUSE_SECURITY, "40", "F0", "#08090E"), "padding": [64, 64], "layout": "horizontal", "gap": 48, "alignItems": "center", "children": [
                # Left Content
                { "type": "frame", "name": "Left Info", "width": 720, "layout": "vertical", "gap": 24, "children": [
                    { "type": "frame", "name": "Badge", "fill": "#1F0A0D", "stroke": R_RED_BORDER, "strokeWidth": 1, "cornerRadius": 4, "padding": [6, 12], "layout": "horizontal", "gap": 8, "alignItems": "center", "children": [
                        { "type": "ellipse", "name": "Dot", "width": 8, "height": 8, "fill": R_RED_BRIGHT },
                        { "type": "text", "name": "Txt", "content": "SISTEMAS HOMOLOGADOS GRADO 3 · MINISTERIO DEL INTERIOR DGP 2341", "fontSize": 11, "fontWeight": "bold", "fill": "#FCA5A5" }
                    ]},
                    { "type": "text", "name": "H1", "content": "BLINDAJE INDUSTRIAL & RESPUESTA INMEDIATA EN < 15 SEGUNDOS", "fontSize": 44, "fontWeight": "900", "lineHeight": 1.15, "fill": "#FFFFFF" },
                    { "type": "text", "name": "P", "content": "Protección física y electrónica de alta seguridad para naves logísticas, plantas industriales e instalaciones críticas. Conexión directa 24/7 con nuestra Central Receptora de Alarmas y despacho prioritario a Policía y Guardia Civil.", "fontSize": 15, "lineHeight": 1.6, "fill": "#CBD5E1" },
                    # Bullet points
                    { "type": "frame", "name": "Bullets", "layout": "vertical", "gap": 10, "children": [
                        { "type": "text", "name": "B1", "content": "✔ Doble vía de comunicación redundante (Fibra Óptica + 4G/5G Encriptado anti-inhibidores)", "fontSize": 13, "fontWeight": "600", "fill": "#F8FAFC" },
                        { "type": "text", "name": "B2", "content": "✔ Verificación de vídeo instantánea con analítica de visión térmica nocturna", "fontSize": 13, "fontWeight": "600", "fill": "#F8FAFC" },
                        { "type": "text", "name": "B3", "content": "✔ Custodia de llaves y servicio de acuda armado propio en la Región de Murcia", "fontSize": 13, "fontWeight": "600", "fill": "#F8FAFC" }
                    ]},
                    # Actions
                    { "type": "frame", "name": "Actions", "layout": "horizontal", "gap": 16, "children": [
                        { "type": "frame", "name": "Primary", "height": 50, "fill": R_RED, "cornerRadius": 6, "padding": [0, 28], "alignItems": "center", "justifyContent": "center", "children": [
                            { "type": "text", "name": "T", "content": "AUDITAR MI INSTALACIÓN EN 24H →", "fontSize": 13, "fontWeight": "bold", "fill": "#FFFFFF" }
                        ]},
                        { "type": "frame", "name": "Sec", "height": 50, "fill": R_CARD, "stroke": R_BORDER, "strokeWidth": 1, "cornerRadius": 6, "padding": [0, 24], "alignItems": "center", "justifyContent": "center", "children": [
                            { "type": "text", "name": "T", "content": "DESCARGAR HOMOLOGACIÓN DGP 2341", "fontSize": 13, "fontWeight": "600", "fill": "#CBD5E1" }
                        ]}
                    ]}
                ]},
                # Right Tactical Telemetry Box
                { "type": "frame", "name": "Right Telemetry", "width": 540, "fill": R_CARD, "stroke": R_RED_BORDER, "strokeWidth": 1, "cornerRadius": 12, "padding": [28, 28], "layout": "vertical", "gap": 20, "children": [
                    { "type": "frame", "name": "Header Box", "width": "fill_container", "layout": "horizontal", "justifyContent": "space_between", "alignItems": "center", "children": [
                        { "type": "frame", "name": "L", "layout": "horizontal", "gap": 8, "alignItems": "center", "children": [
                            { "type": "ellipse", "name": "Dot", "width": 10, "height": 10, "fill": R_GREEN },
                            { "type": "text", "name": "T", "content": "PANEL DE CONTROL CRA OPERATIVO", "fontSize": 12, "fontWeight": "bold", "fill": "#FFFFFF" }
                        ]},
                        { "type": "text", "name": "Time", "content": "SLA ACTIVO: 100%", "fontSize": 11, "fontWeight": "bold", "fill": R_GREEN }
                    ]},
                    { "type": "frame", "name": "Grid Stats", "width": "fill_container", "layout": "horizontal", "gap": 12, "children": [
                        { "type": "frame", "name": "S1", "width": "fill_container", "fill": R_SURFACE, "cornerRadius": 8, "padding": [16, 16], "layout": "vertical", "gap": 6, "children": [
                            { "type": "text", "name": "V", "content": "3.412", "fontSize": 24, "fontWeight": "bold", "fill": R_RED_BRIGHT },
                            { "type": "text", "name": "L", "content": "Naves Industriales Conectadas", "fontSize": 11, "fill": "#94A3B8" }
                        ]},
                        { "type": "frame", "name": "S2", "width": "fill_container", "fill": R_SURFACE, "cornerRadius": 8, "padding": [16, 16], "layout": "vertical", "gap": 6, "children": [
                            { "type": "text", "name": "V", "content": "12,4 seg", "fontSize": 24, "fontWeight": "bold", "fill": R_GREEN },
                            { "type": "text", "name": "L", "content": "Tiempo Medio Verificación CRA", "fontSize": 11, "fill": "#94A3B8" }
                        ]}
                    ]},
                    # Status Live Log
                    { "type": "frame", "name": "Live Log", "width": "fill_container", "fill": "#0A0C13", "cornerRadius": 8, "padding": [16, 16], "layout": "vertical", "gap": 10, "children": [
                        { "type": "text", "name": "LogH", "content": "REGISTRO DE OPERACIONES EN TIEMPO REAL:", "fontSize": 10, "fontWeight": "bold", "fill": "#64748B" },
                        { "type": "text", "name": "L1", "content": "[12:18:02] Pol. Ind. La Polvorista (Nave 14) · Test Perimetral OK", "fontSize": 11, "fontFamily": "Inter", "fill": "#10B981" },
                        { "type": "text", "name": "L2", "content": "[12:18:45] Pol. Ind. Oeste (Logística Sur) · Doble Vía Fibra Activa", "fontSize": 11, "fontFamily": "Inter", "fill": "#94A3B8" },
                        { "type": "text", "name": "L3", "content": "[12:19:10] CRA Central · 0 falsas alarmas transmitidas a Policía", "fontSize": 11, "fontFamily": "Inter", "fill": "#FCA5A5" }
                    ]},
                    # Emergency Trigger Bar
                    { "type": "frame", "name": "Panic Demo", "width": "fill_container", "height": 42, "fill": "#2A0E13", "stroke": R_RED_BORDER, "strokeWidth": 1, "cornerRadius": 6, "layout": "horizontal", "padding": [0, 16], "alignItems": "center", "justifyContent": "space_between", "children": [
                        { "type": "text", "name": "Lbl", "content": "🚨 MODO SIMULACRO DE INTRUSIÓN", "fontSize": 11, "fontWeight": "bold", "fill": "#FCA5A5" },
                        { "type": "text", "name": "Btn", "content": "PROBAR RESPUESTA CRA →", "fontSize": 11, "fontWeight": "bold", "fill": R_RED_BRIGHT }
                    ]}
                ]}
            ]},
            # Section 2: Matriz Grado 3
            { "type": "frame", "name": "Sec Matriz", "width": "fill_container", "fill": R_SURFACE, "padding": [64, 64], "layout": "vertical", "gap": 36, "children": [
                { "type": "frame", "name": "Head", "width": "fill_container", "layout": "vertical", "gap": 8, "children": [
                    { "type": "text", "name": "Tag", "content": "ESPECIFICACIONES TÉCNICAS DE MÁXIMA EXIGENCIA", "fontSize": 12, "fontWeight": "bold", "fill": R_RED_BRIGHT },
                    { "type": "text", "name": "Title", "content": "MATRIZ DE BLINDAJE INDUSTRIAL GRADO 3 UNE-EN 50131", "fontSize": 32, "fontWeight": "bold", "fill": "#FFFFFF" }
                ]},
                { "type": "frame", "name": "Grid Cards", "width": "fill_container", "layout": "horizontal", "gap": 20, "children": [
                    { "type": "frame", "name": "C1", "width": "fill_container", "fill": R_CARD, "stroke": R_RED_BORDER, "strokeWidth": { "top": 4 }, "cornerRadius": 8, "padding": [24, 20], "layout": "vertical", "gap": 12, "children": [
                        { "type": "text", "name": "Num", "content": "01", "fontSize": 28, "fontWeight": "900", "fill": R_RED_BRIGHT },
                        { "type": "text", "name": "T", "content": "Doble Vía Anti-Inhibición", "fontSize": 16, "fontWeight": "bold", "fill": "#FFFFFF" },
                        { "type": "text", "name": "P", "content": "Comunicaciones simultáneas por fibra óptica dedicada y módem 4G/5G con sondeo de línea cada 30 segundos. Si cortan la fibra, la alarma salta al instante.", "fontSize": 12, "lineHeight": 1.5, "fill": "#94A3B8" }
                    ]},
                    { "type": "frame", "name": "C2", "width": "fill_container", "fill": R_CARD, "stroke": R_RED_BORDER, "strokeWidth": { "top": 4 }, "cornerRadius": 8, "padding": [24, 20], "layout": "vertical", "gap": 12, "children": [
                        { "type": "text", "name": "Num", "content": "02", "fontSize": 28, "fontWeight": "900", "fill": R_RED_BRIGHT },
                        { "type": "text", "name": "T", "content": "Generadores de Niebla Zero-Vision", "fontSize": 16, "fontWeight": "bold", "fill": "#FFFFFF" },
                        { "type": "text", "name": "P", "content": "Descarga de 1.000 m³ de humo blanco denso e inocuo en menos de 20 segundos. Reduce la visibilidad a 10 cm impidiendo físicamente el robo.", "fontSize": 12, "lineHeight": 1.5, "fill": "#94A3B8" }
                    ]},
                    { "type": "frame", "name": "C3", "width": "fill_container", "fill": R_CARD, "stroke": R_RED_BORDER, "strokeWidth": { "top": 4 }, "cornerRadius": 8, "padding": [24, 20], "layout": "vertical", "gap": 12, "children": [
                        { "type": "text", "name": "Num", "content": "03", "fontSize": 28, "fontWeight": "900", "fill": R_RED_BRIGHT },
                        { "type": "text", "name": "T", "content": "Detección Sísmica & Térmica", "fontSize": 16, "fontWeight": "bold", "fill": "#FFFFFF" },
                        { "type": "text", "name": "P", "content": "Sensores piezoeléctricos homologados para cajas fuertes, cámaras acorazadas y cámaras térmicas perimetrales que ven en oscuridad absoluta a 300m.", "fontSize": 12, "lineHeight": 1.5, "fill": "#94A3B8" }
                    ]},
                    { "type": "frame", "name": "C4", "width": "fill_container", "fill": R_CARD, "stroke": R_RED_BORDER, "strokeWidth": { "top": 4 }, "cornerRadius": 8, "padding": [24, 20], "layout": "vertical", "gap": 12, "children": [
                        { "type": "text", "name": "Num", "content": "04", "fontSize": 28, "fontWeight": "900", "fill": R_RED_BRIGHT },
                        { "type": "text", "name": "T", "content": "Custodia y Acuda Propio 24h", "fontSize": 16, "fontWeight": "bold", "fill": "#FFFFFF" },
                        { "type": "text", "name": "P", "content": "Vigilantes de seguridad armados y habilitados con base operativa en el Polígono La Polvorista para llegar a su nave antes que nadie.", "fontSize": 12, "lineHeight": 1.5, "fill": "#94A3B8" }
                    ]}
                ]}
            ]},
            # Section 3: Protocolo Táctico
            { "type": "frame", "name": "Sec Protocolo", "width": "fill_container", "padding": [64, 64], "layout": "vertical", "gap": 32, "children": [
                { "type": "text", "name": "Title", "content": "PROTOCOLO TÁCTICO DE INTERVENCIÓN EN 4 FASES", "fontSize": 26, "fontWeight": "bold", "fill": "#FFFFFF" },
                { "type": "frame", "name": "Timeline", "width": "fill_container", "fill": R_CARD, "cornerRadius": 8, "padding": [32, 32], "layout": "horizontal", "gap": 24, "children": [
                    { "type": "frame", "name": "P1", "width": "fill_container", "layout": "vertical", "gap": 8, "children": [
                        { "type": "text", "name": "F", "content": "FASE 1 · 0.1s", "fontSize": 11, "fontWeight": "bold", "fill": R_RED_BRIGHT },
                        { "type": "text", "name": "H", "content": "Disparo de Sensor", "fontSize": 15, "fontWeight": "bold", "fill": "#FFFFFF" },
                        { "type": "text", "name": "D", "content": "Doble señal cifrada recibida en CRA central.", "fontSize": 12, "fill": "#94A3B8" }
                    ]},
                    { "type": "frame", "name": "Sep1", "width": 1, "height": 60, "fill": R_BORDER },
                    { "type": "frame", "name": "P2", "width": "fill_container", "layout": "vertical", "gap": 8, "children": [
                        { "type": "text", "name": "F", "content": "FASE 2 · < 8s", "fontSize": 11, "fontWeight": "bold", "fill": R_RED_BRIGHT },
                        { "type": "text", "name": "H", "content": "Vídeo-Verificación", "fontSize": 15, "fontWeight": "bold", "fill": "#FFFFFF" },
                        { "type": "text", "name": "D", "content": "Operador CRA valida intrusión real mediante cámaras HD.", "fontSize": 12, "fill": "#94A3B8" }
                    ]},
                    { "type": "frame", "name": "Sep2", "width": 1, "height": 60, "fill": R_BORDER },
                    { "type": "frame", "name": "P3", "width": "fill_container", "layout": "vertical", "gap": 8, "children": [
                        { "type": "text", "name": "F", "content": "FASE 3 · < 15s", "fontSize": 11, "fontWeight": "bold", "fill": R_RED_BRIGHT },
                        { "type": "text", "name": "H", "content": "Aviso Policía / GC", "fontSize": 15, "fontWeight": "bold", "fill": "#FFFFFF" },
                        { "type": "text", "name": "D", "content": "Transmisión telemática directa a Fuerzas de Seguridad.", "fontSize": 12, "fill": "#94A3B8" }
                    ]},
                    { "type": "frame", "name": "Sep3", "width": 1, "height": 60, "fill": R_BORDER },
                    { "type": "frame", "name": "P4", "width": "fill_container", "layout": "vertical", "gap": 8, "children": [
                        { "type": "text", "name": "F", "content": "FASE 4 · INMEDIATO", "fontSize": 11, "fontWeight": "bold", "fill": R_RED_BRIGHT },
                        { "type": "text", "name": "H", "content": "Despacho de Acuda", "fontSize": 15, "fontWeight": "bold", "fill": "#FFFFFF" },
                        { "type": "text", "name": "D", "content": "Patrulla armada y custodia se desplazan in-situ.", "fontSize": 12, "fill": "#94A3B8" }
                    ]}
                ]}
            ]},
            suite1_footer()
        ]
    }

print("Suite 1 Home built.")
