import json
from generate_three_radical_suites import (
    IMG_LOGISTICS_DOCK,
    official_brand_badge, suite2_header, suite2_footer, photo_bg,
    B_BG, B_SURFACE, B_CARD, B_CARD_GLASS, B_COBALT, B_CYAN, B_CYAN_GLOW,
    B_BORDER, B_BORDER_CYAN, B_TEXT, B_MUTED,
    IMG_CCTV_TACTICAL, IMG_DATA_CENTER, IMG_CONTROL_CENTER, IMG_WAREHOUSE_SECURITY
)

def build_s2_home(y_pos=18500):
    return {
        "type": "frame",
        "name": "Suite 2: [01] Home Cyber-AI Neural Vision - Control 61",
        "x": 0, "y": y_pos, "width": 1440, "height": 3300,
        "fill": B_BG, "layout": "vertical", "children": [
            suite2_header(active_nav="Capacidades IA"),
            # Centered Hero with Prompt Simulator
            { "type": "frame", "name": "Hero Centered", "width": "fill_container", "padding": [64, 120], "layout": "vertical", "alignItems": "center", "gap": 28, "children": [
                { "type": "frame", "name": "Glow Tag", "fill": "#06B6D41A", "stroke": B_BORDER_CYAN, "strokeWidth": 1, "cornerRadius": 20, "padding": [6, 16], "layout": "horizontal", "gap": 8, "alignItems": "center", "children": [
                    { "type": "ellipse", "name": "Pulse", "width": 8, "height": 8, "fill": B_CYAN },
                    { "type": "text", "name": "T", "content": "MOTOR DE INFERENCIA NEURONAL V4.2 ACTIVADO EN TIEMPO REAL", "fontSize": 11, "fontWeight": "bold", "fill": B_CYAN }
                ]},
                { "type": "text", "name": "H1", "content": "La Inteligencia Artificial que Ve lo que el Ojo Humano Pasa por Alto", "fontSize": 48, "fontWeight": "900", "textAlign": "center", "lineHeight": 1.15, "fill": "#FFFFFF" },
                { "type": "text", "name": "P", "content": "Transforme su red de cámaras CCTV en un sistema autónomo de detección de amenazas. Clasificación instantánea de personas, vehículos y matrículas con reducción del 99.4% de falsas alarmas.", "fontSize": 16, "textAlign": "center", "lineHeight": 1.6, "fill": "#94A3B8" },
                # Interactive AI Natural Language Search Simulator
                { "type": "frame", "name": "AI Search Simulator", "width": 800, "fill": B_CARD, "stroke": B_BORDER_CYAN, "strokeWidth": 1, "cornerRadius": 16, "padding": [16, 20], "layout": "vertical", "gap": 12, "children": [
                    { "type": "frame", "name": "Input Bar", "width": "fill_container", "layout": "horizontal", "gap": 12, "alignItems": "center", "children": [
                        { "type": "text", "name": "Icon", "content": "🔍", "fontSize": 18 },
                        { "type": "text", "name": "Prompt", "content": "Buscar: \"Persona con chaleco reflectante cerca del muelle norte entre 02:00 y 04:00\"", "fontSize": 13, "fontWeight": "600", "fill": "#F8FAFC" },
                        { "type": "frame", "name": "Tag", "fill": B_COBALT, "cornerRadius": 6, "padding": [4, 10], "children": [{ "type": "text", "name": "t", "content": "Inferencia 32ms", "fontSize": 10, "fontWeight": "bold", "fill": "#FFFFFF" }] }
                    ]},
                    { "type": "frame", "name": "Result Pill", "fill": "#06B6D415", "cornerRadius": 8, "padding": [10, 14], "layout": "horizontal", "justifyContent": "space_between", "alignItems": "center", "children": [
                        { "type": "text", "name": "T", "content": "✓ 1 Coincidencia detectada en Cámara #04 (Muelle Norte) · Confianza 99.7%", "fontSize": 12, "fontWeight": "bold", "fill": B_CYAN },
                        { "type": "text", "name": "Clip", "content": "Reproducir Clip 5s →", "fontSize": 11, "fontWeight": "bold", "fill": "#FFFFFF" }
                    ]}
                ]}
            ]},
            # Section 2: 6-Tile Futuristic Bento Grid
            { "type": "frame", "name": "Bento Section", "width": "fill_container", "padding": [64, 80], "layout": "vertical", "gap": 32, "children": [
                { "type": "frame", "name": "H", "layout": "vertical", "gap": 6, "children": [
                    { "type": "text", "name": "Tag", "content": "CAPACIDADES TECNOLÓGICAS DE NUEVA GENERACIÓN", "fontSize": 12, "fontWeight": "bold", "fill": B_CYAN },
                    { "type": "text", "name": "Title", "content": "BENTO SUITE DE INTELIGENCIA DE SEGURIDAD", "fontSize": 32, "fontWeight": "bold", "fill": "#FFFFFF" }
                ]},
                # Bento Row 1
                { "type": "frame", "name": "Row 1", "width": "fill_container", "layout": "horizontal", "gap": 20, "children": [
                    # Large Tile 1 (LPR / Vision)
                    { "type": "frame", "name": "Tile 1", "width": 800, "height": 300, "fill": photo_bg(IMG_CCTV_TACTICAL, "20", "F0", "#030712"), "stroke": B_BORDER_CYAN, "strokeWidth": 1, "cornerRadius": 16, "padding": [28, 28], "layout": "vertical", "justifyContent": "space_between", "children": [
                        { "type": "frame", "name": "Top", "layout": "horizontal", "justifyContent": "space_between", "children": [
                            { "type": "frame", "name": "Badge", "fill": "#06B6D422", "cornerRadius": 6, "padding": [4, 10], "children": [{ "type": "text", "name": "t", "content": "VISIÓN COMPUTACIONAL DEEP LEARNING", "fontSize": 10, "fontWeight": "bold", "fill": B_CYAN }] },
                            { "type": "text", "name": "FPS", "content": "60 FPS REAL-TIME", "fontSize": 11, "fontWeight": "bold", "fill": "#10B981" }
                        ]},
                        { "type": "frame", "name": "Bot", "layout": "vertical", "gap": 8, "children": [
                            { "type": "text", "name": "T", "content": "Reconocimiento LPR / ANPR y Bounding Boxes Inteligentes", "fontSize": 20, "fontWeight": "bold", "fill": "#FFFFFF" },
                            { "type": "text", "name": "P", "content": "Lectura automática de matrículas a velocidades de hasta 160 km/h y tracking simultáneo de múltiples personas y vehículos en alta definición.", "fontSize": 13, "fill": "#CBD5E1" }
                        ]}
                    ]},
                    # Tile 2 (Anti-False Alarms)
                    { "type": "frame", "name": "Tile 2", "width": 460, "height": 300, "fill": B_CARD, "stroke": B_BORDER, "strokeWidth": 1, "cornerRadius": 16, "padding": [28, 28], "layout": "vertical", "justifyContent": "space_between", "children": [
                        { "type": "text", "name": "Stat", "content": "99.4%", "fontSize": 48, "fontWeight": "900", "fill": B_CYAN },
                        { "type": "frame", "name": "Bot", "layout": "vertical", "gap": 8, "children": [
                            { "type": "text", "name": "T", "content": "Filtro de Falsas Alarmas", "fontSize": 18, "fontWeight": "bold", "fill": "#FFFFFF" },
                            { "type": "text", "name": "P", "content": "Eliminación algorítmica de falsos positivos provocados por lluvia, ramas, sombras o pequeños animales.", "fontSize": 13, "fill": "#94A3B8" }
                        ]}
                    ]}
                ]},
                # Bento Row 2
                { "type": "frame", "name": "Row 2", "width": "fill_container", "layout": "horizontal", "gap": 20, "children": [
                    { "type": "frame", "name": "Tile 3", "width": "fill_container", "height": 220, "fill": B_CARD, "stroke": B_BORDER, "strokeWidth": 1, "cornerRadius": 16, "padding": [24, 24], "layout": "vertical", "gap": 10, "children": [
                        { "type": "text", "name": "H", "content": "⚡ Latencia Ultra Baja (<80ms)", "fontSize": 16, "fontWeight": "bold", "fill": "#FFFFFF" },
                        { "type": "text", "name": "P", "content": "Streaming directo a CRA y dispositivos móviles mediante códecs WebRTC y H.265+ de compresión eficiente.", "fontSize": 12, "fill": "#94A3B8" }
                    ]},
                    { "type": "frame", "name": "Tile 4", "width": "fill_container", "height": 220, "fill": B_CARD, "stroke": B_BORDER, "strokeWidth": 1, "cornerRadius": 16, "padding": [24, 24], "layout": "vertical", "gap": 10, "children": [
                        { "type": "text", "name": "H", "content": "🔒 Cloud Cifrado Tier IV España", "fontSize": 16, "fontWeight": "bold", "fill": "#FFFFFF" },
                        { "type": "text", "name": "P", "content": "Grabación continua y eventos archivados en centros de datos con cifrado de extremo a extremo AES-256.", "fontSize": 12, "fill": "#94A3B8" }
                    ]},
                    { "type": "frame", "name": "Tile 5", "width": "fill_container", "height": 220, "fill": B_CARD, "stroke": B_BORDER, "strokeWidth": 1, "cornerRadius": 16, "padding": [24, 24], "layout": "vertical", "gap": 10, "children": [
                        { "type": "text", "name": "H", "content": "🌐 API REST & Webhooks", "fontSize": 16, "fontWeight": "bold", "fill": "#FFFFFF" },
                        { "type": "text", "name": "P", "content": "Integración nativa con sistemas ERP, SAP, control de accesos y software de terceros mediante webhooks seguros.", "fontSize": 12, "fill": "#94A3B8" }
                    ]}
                ]}
            ]},
            suite2_footer()
        ]
    }

def build_s2_nosotros(y_pos=18500):
    return {
        "type": "frame",
        "name": "Suite 2: [02] Sobre Nosotros - Tech Innovation Hub",
        "x": 1500, "y": y_pos, "width": 1440, "height": 2300,
        "fill": B_BG, "layout": "vertical", "children": [
            suite2_header(active_nav="Neural Studio"),
            # Hero
            { "type": "frame", "name": "Hero", "width": "fill_container", "padding": [64, 80], "layout": "vertical", "gap": 16, "children": [
                { "type": "text", "name": "Tag", "content": "LABORATORIO DE SEGURIDAD COMPUTACIONAL", "fontSize": 12, "fontWeight": "bold", "fill": B_CYAN },
                { "type": "text", "name": "H1", "content": "I+D EN VISIÓN ARTIFICIAL & INFRAESTRUCTURA CLOUD", "fontSize": 40, "fontWeight": "900", "fill": "#FFFFFF" },
                { "type": "text", "name": "P", "content": "En Control 61 combinamos la experiencia de más de 20 años como empresa de seguridad homologada DGP 2341 con un equipo especializado en aprendizaje profundo y desarrollo de software para proteger activos de alto valor.", "fontSize": 15, "fill": "#94A3B8" }
            ]},
            # Infrastructure Grid
            { "type": "frame", "name": "Infra Grid", "width": "fill_container", "padding": [32, 80], "layout": "horizontal", "gap": 24, "children": [
                { "type": "frame", "name": "Cluster", "width": "fill_container", "fill": photo_bg(IMG_DATA_CENTER, "30", "F0", "#030712"), "stroke": B_BORDER_CYAN, "strokeWidth": 1, "cornerRadius": 12, "padding": [32, 32], "layout": "vertical", "gap": 16, "children": [
                    { "type": "text", "name": "T", "content": "CLUSTERS DE INFERENCIA GPU DEDICADOS", "fontSize": 18, "fontWeight": "bold", "fill": "#FFFFFF" },
                    { "type": "text", "name": "P", "content": "Procesamiento de cientos de canales de vídeo simultáneos sin latencia ni cuellos de botella.", "fontSize": 13, "fill": "#CBD5E1" }
                ]},
                { "type": "frame", "name": "Researchers", "width": "fill_container", "fill": B_CARD, "stroke": B_BORDER, "strokeWidth": 1, "cornerRadius": 12, "padding": [32, 32], "layout": "vertical", "gap": 16, "children": [
                    { "type": "text", "name": "T", "content": "EQUIPO MULTIDISCIPLINAR DE INGENIERÍA", "fontSize": 18, "fontWeight": "bold", "fill": B_CYAN },
                    { "type": "text", "name": "P", "content": "Científicos de datos, ingenieros de telecomunicaciones y operadores de CRA trabajando en estrecha sinergia.", "fontSize": 13, "fill": "#94A3B8" }
                ]}
            ]},
            suite2_footer()
        ]
    }

def build_s2_soluciones(y_pos=18500):
    return {
        "type": "frame",
        "name": "Suite 2: [03] Soluciones y Analítica IA - Control 61",
        "x": 3000, "y": y_pos, "width": 1440, "height": 2400,
        "fill": B_BG, "layout": "vertical", "children": [
            suite2_header(active_nav="Arquitectura Cloud"),
            { "type": "frame", "name": "Hero", "width": "fill_container", "padding": [64, 80], "layout": "vertical", "gap": 16, "children": [
                { "type": "text", "name": "H", "content": "CATÁLOGO DE MODELOS NEURONALES DE SEGURIDAD", "fontSize": 36, "fontWeight": "900", "fill": "#FFFFFF" },
                { "type": "text", "name": "P", "content": "Modelos entrenados para identificar riesgos con precisión quirúrgica en condiciones climatológicas adversas y oscuridad total.", "fontSize": 14, "fill": "#94A3B8" }
            ]},
            { "type": "frame", "name": "Models Grid", "width": "fill_container", "padding": [32, 80], "layout": "horizontal", "gap": 20, "children": [
                { "type": "frame", "name": "M1", "width": "fill_container", "fill": B_CARD, "stroke": B_BORDER_CYAN, "strokeWidth": 1, "cornerRadius": 12, "padding": [24, 24], "layout": "vertical", "gap": 12, "children": [
                    { "type": "text", "name": "Icon", "content": "🚗", "fontSize": 28 },
                    { "type": "text", "name": "T", "content": "Control de Matrículas LPR", "fontSize": 16, "fontWeight": "bold", "fill": "#FFFFFF" },
                    { "type": "text", "name": "P", "content": "Identificación de vehículos, listas blancas/negras y apertura automática de barreras.", "fontSize": 12, "fill": "#94A3B8" }
                ]},
                { "type": "frame", "name": "M2", "width": "fill_container", "fill": B_CARD, "stroke": B_BORDER_CYAN, "strokeWidth": 1, "cornerRadius": 12, "padding": [24, 24], "layout": "vertical", "gap": 12, "children": [
                    { "type": "text", "name": "Icon", "content": "🚶", "fontSize": 28 },
                    { "type": "text", "name": "T", "content": "Detección Perimetral Humana", "fontSize": 16, "fontWeight": "bold", "fill": "#FFFFFF" },
                    { "type": "text", "name": "P", "content": "Cruce de línea virtual, merodeo no autorizado (Loitering) y permanencia indebida.", "fontSize": 12, "fill": "#94A3B8" }
                ]},
                { "type": "frame", "name": "M3", "width": "fill_container", "fill": B_CARD, "stroke": B_BORDER_CYAN, "strokeWidth": 1, "cornerRadius": 12, "padding": [24, 24], "layout": "vertical", "gap": 12, "children": [
                    { "type": "text", "name": "Icon", "content": "🔥", "fontSize": 28 },
                    { "type": "text", "name": "T", "content": "Detección Térmica de Fuego", "fontSize": 16, "fontWeight": "bold", "fill": "#FFFFFF" },
                    { "type": "text", "name": "P", "content": "Alerta temprana ante gradientes anómalos de temperatura antes de la aparición de llama.", "fontSize": 12, "fill": "#94A3B8" }
                ]}
            ]},
            suite2_footer()
        ]
    }

def build_s2_webapp(y_pos=18500):
    """Modern Dark SaaS Studio with slim nav, camera tree, and 3 live camera feeds with AI bounding boxes."""
    return {
        "type": "frame",
        "name": "Suite 2: [04] Web App - Neural Vision Studio SaaS",
        "x": 4500, "y": y_pos, "width": 1440, "height": 1024,
        "fill": "#020617", "layout": "horizontal", "children": [
            # Slim Left Nav (72px)
            { "type": "frame", "name": "Slim Nav", "width": 72, "height": 1024, "fill": "#070D1F", "stroke": B_BORDER, "strokeWidth": { "right": 1 }, "padding": [20, 0], "layout": "vertical", "alignItems": "center", "justifyContent": "space_between", "children": [
                { "type": "frame", "name": "Top Icons", "layout": "vertical", "gap": 24, "alignItems": "center", "children": [
                    { "type": "ellipse", "name": "LogoDot", "width": 36, "height": 36, "fill": B_COBALT },
                    { "type": "text", "name": "I1", "content": "📹", "fontSize": 18 },
                    { "type": "text", "name": "I2", "content": "📊", "fontSize": 18 },
                    { "type": "text", "name": "I3", "content": "🧠", "fontSize": 18 },
                    { "type": "text", "name": "I4", "content": "🔍", "fontSize": 18 }
                ]},
                { "type": "text", "name": "Set", "content": "⚙️", "fontSize": 18 }
            ]},
            # Camera Tree Sidebar (240px)
            { "type": "frame", "name": "Camera Tree", "width": 240, "height": 1024, "fill": B_SURFACE, "stroke": B_BORDER, "strokeWidth": { "right": 1 }, "padding": [20, 16], "layout": "vertical", "gap": 16, "children": [
                official_brand_badge(width=160, height=40, bg="#FFFFFF"),
                { "type": "text", "name": "Head", "content": "ÁRBOL DE DISPOSITIVOS IA", "fontSize": 11, "fontWeight": "bold", "fill": "#64748B" },
                { "type": "frame", "name": "Tree List", "layout": "vertical", "gap": 6, "width": "fill_container", "children": [
                    { "type": "frame", "name": "G1", "fill": "#06B6D415", "stroke": B_BORDER_CYAN, "strokeWidth": 1, "cornerRadius": 6, "padding": [8, 10], "layout": "horizontal", "justifyContent": "space_between", "width": "fill_container", "children": [
                        { "type": "text", "name": "T", "content": "Campus Principal (Sede)", "fontSize": 12, "fontWeight": "bold", "fill": B_CYAN },
                        { "type": "text", "name": "c", "content": "4/4", "fontSize": 10, "fill": "#10B981" }
                    ]},
                    { "type": "frame", "name": "C1", "padding": [4, 12], "children": [{ "type": "text", "name": "t", "content": "• Cam 01: Acceso Norte", "fontSize": 11, "fill": "#E2E8F0" }] },
                    { "type": "frame", "name": "C2", "padding": [4, 12], "children": [{ "type": "text", "name": "t", "content": "• Cam 02: Perímetro Este (ALERTA)", "fontSize": 11, "fontWeight": "bold", "fill": "#F87171" }] },
                    { "type": "frame", "name": "C3", "padding": [4, 12], "children": [{ "type": "text", "name": "t", "content": "• Cam 03: Muelle Descarga", "fontSize": 11, "fill": "#94A3B8" }] },
                    { "type": "frame", "name": "G2", "fill": B_CARD, "cornerRadius": 6, "padding": [8, 10], "layout": "horizontal", "justifyContent": "space_between", "width": "fill_container", "children": [
                        { "type": "text", "name": "T", "content": "Parque Fotovoltaico", "fontSize": 12, "fill": "#94A3B8" },
                        { "type": "text", "name": "c", "content": "8/8", "fontSize": 10, "fill": "#94A3B8" }
                    ]}
                ]}
            ]},
            # Main Studio Workspace (1128px)
            { "type": "frame", "name": "Studio Canvas", "width": 1128, "height": 1024, "layout": "vertical", "children": [
                # Top Search & Layout Bar
                { "type": "frame", "name": "Top Bar", "width": "fill_container", "height": 64, "fill": B_SURFACE, "stroke": B_BORDER, "strokeWidth": { "bottom": 1 }, "layout": "horizontal", "padding": [0, 24], "alignItems": "center", "justifyContent": "space_between", "children": [
                    { "type": "frame", "name": "Search", "width": 480, "height": 38, "fill": B_CARD, "stroke": B_BORDER, "strokeWidth": 1, "cornerRadius": 19, "padding": [0, 16], "layout": "horizontal", "gap": 8, "alignItems": "center", "children": [
                        { "type": "text", "name": "i", "content": "🔍", "fontSize": 12 },
                        { "type": "text", "name": "p", "content": "Búsqueda semántica por lenguaje natural...", "fontSize": 12, "fill": "#64748B" }
                    ]},
                    { "type": "frame", "name": "Controls", "layout": "horizontal", "gap": 12, "children": [
                        { "type": "frame", "name": "Grid 2x2", "fill": B_COBALT, "cornerRadius": 6, "padding": [6, 12], "children": [{ "type": "text", "name": "t", "content": "Grid 2x2", "fontSize": 11, "fontWeight": "bold", "fill": "#FFFFFF" }] },
                        { "type": "frame", "name": "HD", "fill": B_CARD, "cornerRadius": 6, "padding": [6, 12], "children": [{ "type": "text", "name": "t", "content": "4K Ultra-HD", "fontSize": 11, "fill": "#94A3B8" }] }
                    ]}
                ]},
                # 2x2 Live Video Matrix Area
                { "type": "frame", "name": "Video Matrix Area", "width": "fill_container", "height": 960, "padding": [20, 20], "layout": "vertical", "gap": 16, "children": [
                    # Row 1 of feeds
                    { "type": "frame", "name": "Video Row 1", "width": "fill_container", "height": 440, "layout": "horizontal", "gap": 16, "children": [
                        # Feed 1 (Vehicle / LPR)
                        { "type": "frame", "name": "Cam 01 Feed", "width": "fill_container", "fill": photo_bg(IMG_LOGISTICS_DOCK, "20", "80"), "stroke": B_BORDER_CYAN, "strokeWidth": 1, "cornerRadius": 8, "padding": [16, 16], "layout": "vertical", "justifyContent": "space_between", "children": [
                            { "type": "frame", "name": "Info", "layout": "horizontal", "justifyContent": "space_between", "children": [
                                { "type": "text", "name": "N", "content": "CAM-01 · Acceso Norte (LPR)", "fontSize": 12, "fontWeight": "bold", "fill": "#FFFFFF" },
                                { "type": "text", "name": "R", "content": "● REC 4K", "fontSize": 11, "fontWeight": "bold", "fill": "#EF4444" }
                            ]},
                            # Bounding Box Simulation
                            { "type": "frame", "name": "Bounding Box LPR", "width": 260, "height": 100, "fill": "#06B6D418", "stroke": B_CYAN, "strokeWidth": 2, "cornerRadius": 4, "padding": [8, 8], "layout": "vertical", "justifyContent": "space_between", "children": [
                                { "type": "text", "name": "Tag", "content": "VEHÍCULO AUTORIZADO (99.8%)", "fontSize": 10, "fontWeight": "bold", "fill": B_CYAN },
                                { "type": "text", "name": "Plate", "content": "MATRÍCULA: 4821-KTY", "fontSize": 12, "fontWeight": "bold", "fill": "#FFFFFF" }
                            ]}
                        ]},
                        # Feed 2 (Breach Alert)
                        { "type": "frame", "name": "Cam 02 Feed", "width": "fill_container", "fill": photo_bg(IMG_WAREHOUSE_SECURITY, "20", "80"), "stroke": "#EF4444", "strokeWidth": 2, "cornerRadius": 8, "padding": [16, 16], "layout": "vertical", "justifyContent": "space_between", "children": [
                            { "type": "frame", "name": "Info", "layout": "horizontal", "justifyContent": "space_between", "children": [
                                { "type": "text", "name": "N", "content": "🚨 CAM-02 · Perímetro Este", "fontSize": 12, "fontWeight": "bold", "fill": "#FCA5A5" },
                                { "type": "text", "name": "R", "content": "ALERTA SOC", "fontSize": 11, "fontWeight": "bold", "fill": "#EF4444" }
                            ]},
                            # Bounding Box Intruder
                            { "type": "frame", "name": "Bounding Box Intrusion", "width": 220, "height": 140, "fill": "#EF444422", "stroke": "#EF4444", "strokeWidth": 2, "cornerRadius": 4, "padding": [8, 8], "layout": "vertical", "justifyContent": "space_between", "children": [
                                { "type": "text", "name": "Tag", "content": "INTRUSO HUMANO (98.6%)", "fontSize": 10, "fontWeight": "bold", "fill": "#FCA5A5" },
                                { "type": "text", "name": "Act", "content": "DISPARO ALARMA CRA", "fontSize": 11, "fontWeight": "bold", "fill": "#FFFFFF" }
                            ]}
                        ]}
                    ]},
                    # Row 2 (Telemetry & Analytics)
                    { "type": "frame", "name": "Video Row 2", "width": "fill_container", "height": 440, "layout": "horizontal", "gap": 16, "children": [
                        # Feed 3
                        { "type": "frame", "name": "Cam 03 Feed", "width": "fill_container", "fill": photo_bg(IMG_CCTV_TACTICAL, "20", "80"), "stroke": B_BORDER, "strokeWidth": 1, "cornerRadius": 8, "padding": [16, 16], "layout": "vertical", "justifyContent": "space_between", "children": [
                            { "type": "text", "name": "N", "content": "CAM-03 · Muelle Descarga", "fontSize": 12, "fontWeight": "bold", "fill": "#FFFFFF" },
                            { "type": "text", "name": "S", "content": "Seguimiento de Carretilla Elevadora Activo", "fontSize": 11, "fill": "#94A3B8" }
                        ]},
                        # Panel 4: Telemetry Graphs
                        { "type": "frame", "name": "Telemetry Graph Card", "width": "fill_container", "fill": B_CARD, "stroke": B_BORDER, "strokeWidth": 1, "cornerRadius": 8, "padding": [20, 20], "layout": "vertical", "justifyContent": "space_between", "children": [
                            { "type": "text", "name": "H", "content": "TELEMETRÍA DE INFERENCIA EN TIEMPO REAL", "fontSize": 12, "fontWeight": "bold", "fill": B_CYAN },
                            { "type": "frame", "name": "Stats Row", "layout": "horizontal", "gap": 20, "children": [
                                { "type": "frame", "name": "S1", "layout": "vertical", "gap": 4, "children": [
                                    { "type": "text", "name": "v", "content": "58.4 FPS", "fontSize": 20, "fontWeight": "bold", "fill": "#10B981" },
                                    { "type": "text", "name": "l", "content": "Velocidad Inferencia", "fontSize": 10, "fill": "#94A3B8" }
                                ]},
                                { "type": "frame", "name": "S2", "layout": "vertical", "gap": 4, "children": [
                                    { "type": "text", "name": "v", "content": "34 ms", "fontSize": 20, "fontWeight": "bold", "fill": B_CYAN },
                                    { "type": "text", "name": "l", "content": "Latencia Red Cloud", "fontSize": 10, "fill": "#94A3B8" }
                                ]}
                            ]},
                            { "type": "text", "name": "Log", "content": "Control61 Neural Vision Engine v4.2 · Licencia Corporativa Activa", "fontSize": 10, "fill": "#475569" }
                        ]}
                    ]}
                ]}
            ]}
        ]
    }

def build_s2_contacto(y_pos=18500):
    return {
        "type": "frame",
        "name": "Suite 2: [05] Contacto y Despliegue Piloto IA - Control 61",
        "x": 6000, "y": y_pos, "width": 1440, "height": 1600,
        "fill": B_BG, "layout": "vertical", "children": [
            suite2_header(active_nav="Contacto"),
            { "type": "frame", "name": "Main", "width": "fill_container", "padding": [64, 100], "layout": "horizontal", "gap": 64, "children": [
                { "type": "frame", "name": "Left", "width": 500, "layout": "vertical", "gap": 20, "children": [
                    official_brand_badge(width=160, height=48, bg="#FFFFFF"),
                    { "type": "text", "name": "H", "content": "SOLICITAR PILOTO TÉCNICO DE VISIÓN ARTIFICIAL", "fontSize": 34, "fontWeight": "900", "fill": "#FFFFFF" },
                    { "type": "text", "name": "P", "content": "Conectamos hasta 8 cámaras existentes de su instalación a nuestro motor de IA durante 14 días sin coste para auditar la reducción de falsas alarmas.", "fontSize": 14, "lineHeight": 1.6, "fill": "#94A3B8" }
                ]},
                { "type": "frame", "name": "Form", "width": 640, "fill": B_CARD, "stroke": B_BORDER_CYAN, "strokeWidth": 1, "cornerRadius": 16, "padding": [36, 36], "layout": "vertical", "gap": 20, "children": [
                    { "type": "text", "name": "T", "content": "CONFIGURADOR DE PROYECTO IA", "fontSize": 18, "fontWeight": "bold", "fill": B_CYAN },
                    { "type": "frame", "name": "F1", "layout": "vertical", "gap": 6, "children": [
                        { "type": "text", "name": "L", "content": "Número de Canales CCTV a Monitorizar", "fontSize": 12, "fill": "#CBD5E1" },
                        { "type": "frame", "name": "In", "height": 46, "fill": B_SURFACE, "stroke": B_BORDER, "strokeWidth": 1, "cornerRadius": 8, "padding": [0, 16], "justifyContent": "center", "children": [
                            { "type": "text", "name": "p", "content": "Ej. 16 cámaras IP / Térmicas", "fontSize": 13, "fill": "#475569" }
                        ]}
                    ]},
                    { "type": "frame", "name": "F2", "layout": "vertical", "gap": 6, "children": [
                        { "type": "text", "name": "L", "content": "Email Corporativo", "fontSize": 12, "fill": "#CBD5E1" },
                        { "type": "frame", "name": "In", "height": 46, "fill": B_SURFACE, "stroke": B_BORDER, "strokeWidth": 1, "cornerRadius": 8, "padding": [0, 16], "justifyContent": "center", "children": [
                            { "type": "text", "name": "p", "content": "seguridad@empresa.com", "fontSize": 13, "fill": "#475569" }
                        ]}
                    ]},
                    { "type": "frame", "name": "Btn", "height": 50, "fill": B_COBALT, "cornerRadius": 8, "alignItems": "center", "justifyContent": "center", "children": [
                        { "type": "text", "name": "t", "content": "INICIAR PILOTO IA EN 48H →", "fontSize": 13, "fontWeight": "bold", "fill": "#FFFFFF" }
                    ]}
                ]}
            ]},
            suite2_footer()
        ]
    }

print("Suite 2 all 5 frames defined.")
