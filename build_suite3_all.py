import json
from generate_three_radical_suites import (
    official_brand_badge, suite3_header, suite3_footer, photo_bg,
    P_BG, P_SURFACE, P_CARD, P_BORDER, P_EMERALD, P_EMERALD_LIGHT,
    P_GOLD, P_GOLD_LIGHT, P_GOLD_BORDER, P_TEXT, P_MUTED,
    IMG_CORPORATE_TOWER, IMG_BANK_VAULT, IMG_DATA_CENTER, IMG_CONTROL_CENTER
)

def build_s3_home(y_pos=22500):
    return {
        "type": "frame",
        "name": "Suite 3: [01] Home Platinum Executive - Control 61",
        "x": 0, "y": y_pos, "width": 1440, "height": 3300,
        "fill": P_BG, "layout": "vertical", "children": [
            suite3_header(active_nav="Grandes Cuentas"),
            # Split Narrative Editorial Hero
            { "type": "frame", "name": "Hero Split", "width": "fill_container", "fill": photo_bg(IMG_CORPORATE_TOWER, "40", "F0", "#0A0D14"), "padding": [64, 80], "layout": "horizontal", "gap": 64, "alignItems": "center", "children": [
                # Left 55%
                { "type": "frame", "name": "Left Narrative", "width": 680, "layout": "vertical", "gap": 24, "children": [
                    { "type": "frame", "name": "Gold Badge", "fill": "#1F160A", "stroke": P_GOLD_BORDER, "strokeWidth": 1, "cornerRadius": 4, "padding": [6, 14], "layout": "horizontal", "gap": 8, "children": [
                        { "type": "text", "name": "t", "content": "AUDITORÍA & BLINDAJE PARA CONSEJOS DE ADMINISTRACIÓN", "fontSize": 11, "fontWeight": "bold", "fill": P_GOLD_LIGHT }
                    ]},
                    { "type": "text", "name": "H1", "content": "Blindaje de Activos Estratégicos & Continuidad de Negocio", "fontSize": 44, "fontWeight": "900", "lineHeight": 1.15, "fill": "#FFFFFF" },
                    { "type": "text", "name": "P", "content": "Protegemos el patrimonio, las infraestructuras críticas y la reputación corporativa de las organizaciones más exigentes de España mediante soluciones de seguridad física convergente, cumplimiento estricto de la Directiva NIS2 y supervisión CRA de máxima homologación.", "fontSize": 15, "lineHeight": 1.6, "fill": "#CBD5E1" },
                    # Cert seals row
                    { "type": "frame", "name": "Seals Row", "layout": "horizontal", "gap": 16, "children": [
                        { "type": "frame", "name": "S1", "fill": P_SURFACE, "stroke": P_BORDER, "strokeWidth": 1, "cornerRadius": 6, "padding": [8, 14], "children": [{ "type": "text", "name": "t", "content": "RINA ISO 9001/14001/45001", "fontSize": 11, "fontWeight": "bold", "fill": P_GOLD_LIGHT }] },
                        { "type": "frame", "name": "S2", "fill": P_SURFACE, "stroke": P_BORDER, "strokeWidth": 1, "cornerRadius": 6, "padding": [8, 14], "children": [{ "type": "text", "name": "t", "content": "MINISTERIO INTERIOR DGP 2341", "fontSize": 11, "fontWeight": "bold", "fill": "#FFFFFF" }] }
                    ]},
                    { "type": "frame", "name": "CTA", "layout": "horizontal", "gap": 16, "children": [
                        { "type": "frame", "name": "Primary", "height": 48, "fill": P_GOLD, "cornerRadius": 6, "padding": [0, 24], "alignItems": "center", "justifyContent": "center", "children": [
                            { "type": "text", "name": "t", "content": "SOLICITAR AUDITORÍA PRIVADA →", "fontSize": 13, "fontWeight": "bold", "fill": "#FFFFFF" }
                        ]},
                        { "type": "frame", "name": "Sec", "height": 48, "fill": P_CARD, "stroke": P_BORDER, "strokeWidth": 1, "cornerRadius": 6, "padding": [0, 20], "alignItems": "center", "justifyContent": "center", "children": [
                            { "type": "text", "name": "t", "content": "DOSSIER CORPORATIVO PDF", "fontSize": 13, "fontWeight": "600", "fill": "#CBD5E1" }
                        ]}
                    ]}
                ]},
                # Right Risk Dashboard Box
                { "type": "frame", "name": "Right Risk Box", "width": 520, "fill": P_CARD, "stroke": P_BORDER, "strokeWidth": 1, "cornerRadius": 12, "padding": [32, 32], "layout": "vertical", "gap": 20, "children": [
                    { "type": "text", "name": "H", "content": "ÍNDICES DE MITIGACIÓN DE RIESGO CORPORATIVO", "fontSize": 12, "fontWeight": "bold", "fill": P_GOLD_LIGHT },
                    { "type": "frame", "name": "M1", "fill": P_SURFACE, "cornerRadius": 8, "padding": [16, 16], "layout": "horizontal", "justifyContent": "space_between", "alignItems": "center", "children": [
                        { "type": "frame", "name": "L", "layout": "vertical", "gap": 2, "children": [
                            { "type": "text", "name": "T", "content": "Disponibilidad CRA & SLA Contractual", "fontSize": 13, "fontWeight": "bold", "fill": "#FFFFFF" },
                            { "type": "text", "name": "S", "content": "Compromiso de respuesta penalizado", "fontSize": 11, "fill": "#64748B" }
                        ]},
                        { "type": "text", "name": "Val", "content": "99.999%", "fontSize": 18, "fontWeight": "900", "fill": P_EMERALD_LIGHT }
                    ]},
                    { "type": "frame", "name": "M2", "fill": P_SURFACE, "cornerRadius": 8, "padding": [16, 16], "layout": "horizontal", "justifyContent": "space_between", "alignItems": "center", "children": [
                        { "type": "frame", "name": "L", "layout": "vertical", "gap": 2, "children": [
                            { "type": "text", "name": "T", "content": "Adecuación Normativa Directiva NIS2", "fontSize": 13, "fontWeight": "bold", "fill": "#FFFFFF" },
                            { "type": "text", "name": "S", "content": "Convergencia física y ciberseguridad", "fontSize": 11, "fill": "#64748B" }
                        ]},
                        { "type": "text", "name": "Val", "content": "100%", "fontSize": 18, "fontWeight": "900", "fill": P_GOLD_LIGHT }
                    ]},
                    { "type": "frame", "name": "M3", "fill": P_SURFACE, "cornerRadius": 8, "padding": [16, 16], "layout": "horizontal", "justifyContent": "space_between", "alignItems": "center", "children": [
                        { "type": "frame", "name": "L", "layout": "vertical", "gap": 2, "children": [
                            { "type": "text", "name": "T", "content": "Póliza Responsabilidad Civil", "fontSize": 13, "fontWeight": "bold", "fill": "#FFFFFF" },
                            { "type": "text", "name": "S", "content": "Cobertura integral de operaciones", "fontSize": 11, "fill": "#64748B" }
                        ]},
                        { "type": "text", "name": "Val", "content": "MÁXIMA", "fontSize": 14, "fontWeight": "bold", "fill": "#CBD5E1" }
                    ]}
                ]}
            ]},
            # Section 2: 4 Strategic Pillars
            { "type": "frame", "name": "Sec Pillars", "width": "fill_container", "padding": [64, 80], "layout": "vertical", "gap": 32, "children": [
                { "type": "text", "name": "H", "content": "LOS 4 PILARES DEL BLINDAJE INSTITUCIONAL", "fontSize": 26, "fontWeight": "bold", "fill": "#FFFFFF" },
                { "type": "frame", "name": "Grid", "width": "fill_container", "layout": "horizontal", "gap": 20, "children": [
                    { "type": "frame", "name": "P1", "width": "fill_container", "fill": P_CARD, "stroke": P_BORDER, "strokeWidth": 1, "cornerRadius": 8, "padding": [24, 20], "layout": "vertical", "gap": 10, "children": [
                        { "type": "text", "name": "N", "content": "01 · PERÍMETROS", "fontSize": 11, "fontWeight": "bold", "fill": P_GOLD_LIGHT },
                        { "type": "text", "name": "T", "content": "Defensa en Profundidad", "fontSize": 16, "fontWeight": "bold", "fill": "#FFFFFF" },
                        { "type": "text", "name": "P", "content": "Detección concéntrica multicapa desde el límite de propiedad hasta las zonas de máxima restricción.", "fontSize": 12, "fill": "#94A3B8" }
                    ]},
                    { "type": "frame", "name": "P2", "width": "fill_container", "fill": P_CARD, "stroke": P_BORDER, "strokeWidth": 1, "cornerRadius": 8, "padding": [24, 20], "layout": "vertical", "gap": 10, "children": [
                        { "type": "text", "name": "N", "content": "02 · SECRETO", "fontSize": 11, "fontWeight": "bold", "fill": P_GOLD_LIGHT },
                        { "type": "text", "name": "T", "content": "Custodia de Información", "fontSize": 16, "fontWeight": "bold", "fill": "#FFFFFF" },
                        { "type": "text", "name": "P", "content": "Canales de comunicación privados con aislamiento de red para evitar fuga de imágenes y planos.", "fontSize": 12, "fill": "#94A3B8" }
                    ]},
                    { "type": "frame", "name": "P3", "width": "fill_container", "fill": P_CARD, "stroke": P_BORDER, "strokeWidth": 1, "cornerRadius": 8, "padding": [24, 20], "layout": "vertical", "gap": 10, "children": [
                        { "type": "text", "name": "N", "content": "03 · ACCESOS", "fontSize": 11, "fontWeight": "bold", "fill": P_GOLD_LIGHT },
                        { "type": "text", "name": "T", "content": "Biometría y Esclusas", "fontSize": 16, "fontWeight": "bold", "fill": "#FFFFFF" },
                        { "type": "text", "name": "P", "content": "Control de personal de alta dirección y zonas restringidas mediante reconocimiento multimodal.", "fontSize": 12, "fill": "#94A3B8" }
                    ]},
                    { "type": "frame", "name": "P4", "width": "fill_container", "fill": P_CARD, "stroke": P_BORDER, "strokeWidth": 1, "cornerRadius": 8, "padding": [24, 20], "layout": "vertical", "gap": 10, "children": [
                        { "type": "text", "name": "N", "content": "04 · GOBIERNO", "fontSize": 11, "fontWeight": "bold", "fill": P_GOLD_LIGHT },
                        { "type": "text", "name": "T", "content": "Informes para el Consejo", "fontSize": 16, "fontWeight": "bold", "fill": "#FFFFFF" },
                        { "type": "text", "name": "P", "content": "Auditorías periódicas trimestrales con actas oficiales para auditores externos y aseguradoras.", "fontSize": 12, "fill": "#94A3B8" }
                    ]}
                ]}
            ]},
            suite3_footer()
        ]
    }

def build_s3_nosotros(y_pos=22500):
    return {
        "type": "frame",
        "name": "Suite 3: [02] Sobre Nosotros - Gobierno Corporativo & Calidad",
        "x": 1500, "y": y_pos, "width": 1440, "height": 2200,
        "fill": P_BG, "layout": "vertical", "children": [
            suite3_header(active_nav="Gobierno Corporativo"),
            { "type": "frame", "name": "Hero", "width": "fill_container", "padding": [64, 80], "layout": "vertical", "gap": 16, "children": [
                { "type": "text", "name": "Tag", "content": "VOCACIÓN DE EXCELENCIA Y RIGOR TÉCNICO", "fontSize": 12, "fontWeight": "bold", "fill": P_GOLD_LIGHT },
                { "type": "text", "name": "H", "content": "MÁS DE DOS DÉCADAS VELANDO POR LA SEGURIDAD", "fontSize": 38, "fontWeight": "900", "fill": "#FFFFFF" },
                { "type": "text", "name": "P", "content": "Control 61 (Desarrollos y Sistemas Inteligentes S.L.) mantiene un compromiso inquebrantable con la confidencialidad, la ética profesional y el cumplimiento de las normativas más estrictas del sector de la seguridad privada.", "fontSize": 15, "fill": "#94A3B8" }
            ]},
            { "type": "frame", "name": "Cert Section", "width": "fill_container", "padding": [32, 80], "layout": "horizontal", "gap": 24, "children": [
                { "type": "frame", "name": "C1", "width": "fill_container", "fill": P_CARD, "stroke": P_BORDER, "strokeWidth": 1, "cornerRadius": 8, "padding": [28, 28], "layout": "vertical", "gap": 12, "children": [
                    { "type": "text", "name": "H", "content": "SISTEMA INTEGRADO DE GESTIÓN RINA", "fontSize": 16, "fontWeight": "bold", "fill": P_GOLD_LIGHT },
                    { "type": "text", "name": "P", "content": "Certificaciones ISO 9001 (Calidad), ISO 14001 (Medio Ambiente) e ISO 45001 (Seguridad y Salud en el Trabajo) auditadas anualmente.", "fontSize": 13, "fill": "#CBD5E1" }
                ]},
                { "type": "frame", "name": "C2", "width": "fill_container", "fill": P_CARD, "stroke": P_BORDER, "strokeWidth": 1, "cornerRadius": 8, "padding": [28, 28], "layout": "vertical", "gap": 12, "children": [
                    { "type": "text", "name": "H", "content": "HABILITACIÓN LEGAL DEL ESTADO", "fontSize": 16, "fontWeight": "bold", "fill": P_EMERALD_LIGHT },
                    { "type": "text", "name": "P", "content": "Empresa inscrita en el Registro Nacional de Seguridad Privada con el Nº 2341 y autorizada para instalación y mantenimiento en toda España.", "fontSize": 13, "fill": "#CBD5E1" }
                ]}
            ]},
            suite3_footer()
        ]
    }

def build_s3_sectores(y_pos=22500):
    return {
        "type": "frame",
        "name": "Suite 3: [03] Sectores Críticos & Compliance - Control 61",
        "x": 3000, "y": y_pos, "width": 1440, "height": 2400,
        "fill": P_BG, "layout": "vertical", "children": [
            suite3_header(active_nav="Infraestructuras Críticas"),
            { "type": "frame", "name": "Hero", "width": "fill_container", "padding": [64, 80], "layout": "vertical", "gap": 16, "children": [
                { "type": "text", "name": "H", "content": "DOSSIER DE SECTORES ESTRATÉGICOS & BLINDAJE NORMATIVO", "fontSize": 36, "fontWeight": "900", "fill": "#FFFFFF" },
                { "type": "text", "name": "P", "content": "Soluciones adaptadas a la legislación específica de cada sector obligado por la Orden Ministerial INT/317/2011.", "fontSize": 14, "fill": "#94A3B8" }
            ]},
            { "type": "frame", "name": "Sectors", "width": "fill_container", "padding": [32, 80], "layout": "horizontal", "gap": 20, "children": [
                { "type": "frame", "name": "S1", "width": "fill_container", "fill": photo_bg(IMG_BANK_VAULT, "30", "F0", "#0A0D14"), "stroke": P_BORDER, "strokeWidth": 1, "cornerRadius": 8, "padding": [28, 24], "layout": "vertical", "gap": 12, "children": [
                    { "type": "text", "name": "Tag", "content": "ORDEN INT/317/2011", "fontSize": 10, "fontWeight": "bold", "fill": P_GOLD_LIGHT },
                    { "type": "text", "name": "T", "content": "Banca & Joyerías", "fontSize": 18, "fontWeight": "bold", "fill": "#FFFFFF" },
                    { "type": "text", "name": "P", "content": "Grado 3 obligatorio, detectores sísmicos, pulsadores de atraco y doble vía supervisada.", "fontSize": 12, "fill": "#CBD5E1" }
                ]},
                { "type": "frame", "name": "S2", "width": "fill_container", "fill": photo_bg(IMG_DATA_CENTER, "30", "F0", "#0A0D14"), "stroke": P_BORDER, "strokeWidth": 1, "cornerRadius": 8, "padding": [28, 24], "layout": "vertical", "gap": 12, "children": [
                    { "type": "text", "name": "Tag", "content": "DIRECTIVA NIS2", "fontSize": 10, "fontWeight": "bold", "fill": P_EMERALD_LIGHT },
                    { "type": "text", "name": "T", "content": "Centros de Datos & Telco", "fontSize": 18, "fontWeight": "bold", "fill": "#FFFFFF" },
                    { "type": "text", "name": "P", "content": "Control biométrico estricto, extinción automática por gas y monitorización ambiental.", "fontSize": 12, "fill": "#CBD5E1" }
                ]},
                { "type": "frame", "name": "S3", "width": "fill_container", "fill": photo_bg(IMG_CONTROL_CENTER, "30", "F0", "#0A0D14"), "stroke": P_BORDER, "strokeWidth": 1, "cornerRadius": 8, "padding": [28, 24], "layout": "vertical", "gap": 12, "children": [
                    { "type": "text", "name": "Tag", "content": "LEY PIC", "fontSize": 10, "fontWeight": "bold", "fill": P_GOLD_LIGHT },
                    { "type": "text", "name": "T", "content": "Energía & Puertos", "fontSize": 18, "fontWeight": "bold", "fill": "#FFFFFF" },
                    { "type": "text", "name": "P", "content": "Protección de infraestructuras críticas con radar perimetral y cámaras térmicas de largo alcance.", "fontSize": 12, "fill": "#CBD5E1" }
                ]}
            ]},
            suite3_footer()
        ]
    }

def build_s3_webapp(y_pos=22500):
    """Executive Multi-Site Command Hub for CISO / CSO with Spain Multi-Site map and compliance status matrix."""
    return {
        "type": "frame",
        "name": "Suite 3: [04] Web App - Executive Multi-Site Command Hub",
        "x": 4500, "y": y_pos, "width": 1440, "height": 1024,
        "fill": "#080B11", "layout": "vertical", "children": [
            # Top Executive Header Bar
            { "type": "frame", "name": "Top Bar", "width": "fill_container", "height": 72, "fill": P_SURFACE, "stroke": P_BORDER, "strokeWidth": { "bottom": 1 }, "layout": "horizontal", "padding": [0, 32], "alignItems": "center", "justifyContent": "space_between", "children": [
                { "type": "frame", "name": "Brand", "layout": "horizontal", "gap": 16, "alignItems": "center", "children": [
                    official_brand_badge(width=160, height=44, bg="#FFFFFF"),
                    { "type": "frame", "name": "Company Selector", "fill": P_CARD, "stroke": P_BORDER, "strokeWidth": 1, "cornerRadius": 6, "padding": [8, 14], "layout": "horizontal", "gap": 8, "alignItems": "center", "children": [
                        { "type": "text", "name": "c", "content": "🏢 Grupo Corporativo Levante S.A. (14 Sedes)", "fontSize": 12, "fontWeight": "bold", "fill": "#FFFFFF" }
                    ]}
                ]},
                { "type": "frame", "name": "Right Actions", "layout": "horizontal", "gap": 16, "children": [
                    { "type": "frame", "name": "Export PDF", "fill": P_CARD, "stroke": P_GOLD_BORDER, "strokeWidth": 1, "cornerRadius": 6, "padding": [8, 16], "children": [
                        { "type": "text", "name": "t", "content": "📄 Exportar Informe Consejo PDF", "fontSize": 12, "fontWeight": "bold", "fill": P_GOLD_LIGHT }
                    ]},
                    { "type": "frame", "name": "User", "fill": P_SURFACE, "cornerRadius": 6, "padding": [8, 12], "children": [
                        { "type": "text", "name": "u", "content": "CSO: D. Alejandro Ruiz", "fontSize": 12, "fill": "#CBD5E1" }
                    ]}
                ]}
            ]},
            # Main Dashboard Split
            { "type": "frame", "name": "Main Dashboard", "width": "fill_container", "height": 952, "layout": "horizontal", "children": [
                # Left Governance Sidebar (280px)
                { "type": "frame", "name": "Gov Sidebar", "width": 280, "height": 952, "fill": P_SURFACE, "stroke": P_BORDER, "strokeWidth": { "right": 1 }, "padding": [24, 20], "layout": "vertical", "gap": 20, "children": [
                    { "type": "text", "name": "Head", "content": "GOBERNANZA & CUMPLIMIENTO", "fontSize": 11, "fontWeight": "bold", "fill": "#64748B" },
                    { "type": "frame", "name": "Score Card", "fill": P_CARD, "stroke": P_BORDER, "strokeWidth": 1, "cornerRadius": 8, "padding": [16, 16], "layout": "vertical", "gap": 6, "children": [
                        { "type": "text", "name": "Lbl", "content": "SCORE DE SEGURIDAD GLOBAL", "fontSize": 10, "fontWeight": "bold", "fill": P_GOLD_LIGHT },
                        { "type": "text", "name": "Val", "content": "98.4 / 100", "fontSize": 28, "fontWeight": "900", "fill": P_EMERALD_LIGHT },
                        { "type": "text", "name": "Sub", "content": "Excelente · 0 vulnerabilidades críticas", "fontSize": 11, "fill": "#94A3B8" }
                    ]},
                    { "type": "frame", "name": "Metrics List", "layout": "vertical", "gap": 10, "children": [
                        { "type": "frame", "name": "Item 1", "layout": "vertical", "gap": 2, "children": [
                            { "type": "text", "name": "t", "content": "SLA CRA Promedio Trimestral", "fontSize": 12, "fill": "#CBD5E1" },
                            { "type": "text", "name": "v", "content": "11.8 segundos (< 15s objetivo)", "fontSize": 13, "fontWeight": "bold", "fill": P_EMERALD_LIGHT }
                        ]},
                        { "type": "frame", "name": "Item 2", "layout": "vertical", "gap": 2, "children": [
                            { "type": "text", "name": "t", "content": "Revisiones Trimestrales", "fontSize": 12, "fill": "#CBD5E1" },
                            { "type": "text", "name": "v", "content": "14/14 Realizadas (100%)", "fontSize": 13, "fontWeight": "bold", "fill": "#FFFFFF" }
                        ]}
                    ]}
                ]},
                # Center-Right Multi-Site & Compliance Matrix Area (1160px)
                { "type": "frame", "name": "Content Area", "width": 1160, "height": 952, "padding": [24, 28], "layout": "vertical", "gap": 20, "children": [
                    # Top Map & Status Highlights (Height 380px)
                    { "type": "frame", "name": "Map & Highlight Row", "width": "fill_container", "height": 360, "layout": "horizontal", "gap": 20, "children": [
                        # Geographic Map Card (700px)
                        { "type": "frame", "name": "Spain Map Card", "width": 700, "height": "fill_container", "fill": P_CARD, "stroke": P_BORDER, "strokeWidth": 1, "cornerRadius": 8, "padding": [20, 20], "layout": "vertical", "justifyContent": "space_between", "children": [
                            { "type": "frame", "name": "Map Head", "layout": "horizontal", "justifyContent": "space_between", "children": [
                                { "type": "text", "name": "t", "content": "MAPA DE DESPLIEGUE MULTI-SEDE (SISTEMA CONVERGENTE)", "fontSize": 12, "fontWeight": "bold", "fill": P_GOLD_LIGHT },
                                { "type": "text", "name": "s", "content": "14 SEDES CONECTADAS 24/7", "fontSize": 11, "fontWeight": "bold", "fill": P_EMERALD_LIGHT }
                            ]},
                            # Nodes representation
                            { "type": "frame", "name": "Nodes Container", "width": "fill_container", "height": 240, "fill": "#0D131F", "cornerRadius": 6, "padding": [20, 24], "layout": "horizontal", "justifyContent": "space_between", "alignItems": "center", "children": [
                                { "type": "frame", "name": "Node Murcia", "layout": "vertical", "gap": 4, "alignItems": "center", "children": [
                                    { "type": "ellipse", "name": "Dot", "width": 14, "height": 14, "fill": P_EMERALD_LIGHT },
                                    { "type": "text", "name": "N", "content": "Murcia HQ (La Polvorista)", "fontSize": 11, "fontWeight": "bold", "fill": "#FFFFFF" },
                                    { "type": "text", "name": "s", "content": "Grado 3 · OK", "fontSize": 10, "fill": P_EMERALD_LIGHT }
                                ]},
                                { "type": "frame", "name": "Node Cartagena", "layout": "vertical", "gap": 4, "alignItems": "center", "children": [
                                    { "type": "ellipse", "name": "Dot", "width": 14, "height": 14, "fill": P_EMERALD_LIGHT },
                                    { "type": "text", "name": "N", "content": "Cartagena (Planta Química)", "fontSize": 11, "fontWeight": "bold", "fill": "#FFFFFF" },
                                    { "type": "text", "name": "s", "content": "CCTV IA · OK", "fontSize": 10, "fill": P_EMERALD_LIGHT }
                                ]},
                                { "type": "frame", "name": "Node Valencia", "layout": "vertical", "gap": 4, "alignItems": "center", "children": [
                                    { "type": "ellipse", "name": "Dot", "width": 14, "height": 14, "fill": P_EMERALD_LIGHT },
                                    { "type": "text", "name": "N", "content": "Valencia (Hub Logístico)", "fontSize": 11, "fontWeight": "bold", "fill": "#FFFFFF" },
                                    { "type": "text", "name": "s", "content": "Grado 3 · OK", "fontSize": 10, "fill": P_EMERALD_LIGHT }
                                ]},
                                { "type": "frame", "name": "Node Alicante", "layout": "vertical", "gap": 4, "alignItems": "center", "children": [
                                    { "type": "ellipse", "name": "Dot", "width": 14, "height": 14, "fill": P_EMERALD_LIGHT },
                                    { "type": "text", "name": "N", "content": "Alicante (Oficinas)", "fontSize": 11, "fontWeight": "bold", "fill": "#FFFFFF" },
                                    { "type": "text", "name": "s", "content": "Accesos · OK", "fontSize": 10, "fill": P_EMERALD_LIGHT }
                                ]}
                            ]},
                            { "type": "text", "name": "Foot", "content": "Conexión encriptada directa con CRA Central Control 61", "fontSize": 10, "fill": "#64748B" }
                        ]},
                        # Summary Card (400px)
                        { "type": "frame", "name": "Audit Summary Card", "width": 400, "height": "fill_container", "fill": P_CARD, "stroke": P_BORDER, "strokeWidth": 1, "cornerRadius": 8, "padding": [20, 20], "layout": "vertical", "justifyContent": "space_between", "children": [
                            { "type": "text", "name": "H", "content": "CERTIFICADOS & ACTAS DISPONIBLES", "fontSize": 12, "fontWeight": "bold", "fill": P_GOLD_LIGHT },
                            { "type": "frame", "name": "List", "layout": "vertical", "gap": 8, "children": [
                                { "type": "text", "name": "A1", "content": "• Acta Revisión Trimestral Q3 (Firmada)", "fontSize": 12, "fill": "#CBD5E1" },
                                { "type": "text", "name": "A2", "content": "• Certificado Homologación Grado 3", "fontSize": 12, "fill": "#CBD5E1" },
                                { "type": "text", "name": "A3", "content": "• Póliza de Seguro Vigor 2026", "fontSize": 12, "fill": "#CBD5E1" }
                            ]},
                            { "type": "frame", "name": "DownloadAll", "height": 38, "fill": P_GOLD, "cornerRadius": 6, "alignItems": "center", "justifyContent": "center", "children": [
                                { "type": "text", "name": "t", "content": "Descargar Todo el Expediente (ZIP)", "fontSize": 12, "fontWeight": "bold", "fill": "#FFFFFF" }
                            ]}
                        ]}
                    ]},
                    # Bottom Facility Compliance Table (Height 480px)
                    { "type": "frame", "name": "Compliance Table Card", "width": "fill_container", "height": 480, "fill": P_CARD, "stroke": P_BORDER, "strokeWidth": 1, "cornerRadius": 8, "layout": "vertical", "children": [
                        # Table Header
                        { "type": "frame", "name": "TH", "width": "fill_container", "height": 44, "fill": P_SURFACE, "layout": "horizontal", "padding": [0, 20], "alignItems": "center", "children": [
                            { "type": "text", "name": "c1", "content": "INSTALACIÓN", "width": 280, "fontSize": 11, "fontWeight": "bold", "fill": "#64748B" },
                            { "type": "text", "name": "c2", "content": "NIVEL DE RIESGO", "width": 180, "fontSize": 11, "fontWeight": "bold", "fill": "#64748B" },
                            { "type": "text", "name": "c3", "content": "ESTADO CRA", "width": 180, "fontSize": 11, "fontWeight": "bold", "fill": "#64748B" },
                            { "type": "text", "name": "c4", "content": "ÚLTIMA INSPECCIÓN", "width": 220, "fontSize": 11, "fontWeight": "bold", "fill": "#64748B" },
                            { "type": "text", "name": "c5", "content": "CERTIFICADO", "width": 200, "fontSize": 11, "fontWeight": "bold", "fill": "#64748B" }
                        ]},
                        # Row 1
                        { "type": "frame", "name": "TR 1", "width": "fill_container", "height": 52, "stroke": P_BORDER, "strokeWidth": { "top": 1 }, "layout": "horizontal", "padding": [0, 20], "alignItems": "center", "children": [
                            { "type": "text", "name": "c1", "content": "Sede Corporativa Central (Murcia)", "width": 280, "fontSize": 12, "fontWeight": "bold", "fill": "#FFFFFF" },
                            { "type": "text", "name": "c2", "content": "Grado 3 (Alto Riesgo)", "width": 180, "fontSize": 12, "fill": P_GOLD_LIGHT },
                            { "type": "text", "name": "c3", "content": "● Conectado 100%", "width": 180, "fontSize": 12, "fontWeight": "bold", "fill": P_EMERALD_LIGHT },
                            { "type": "text", "name": "c4", "content": "15 Sep 2026 (Superada)", "width": 220, "fontSize": 12, "fill": "#CBD5E1" },
                            { "type": "text", "name": "c5", "content": "Descargar PDF →", "width": 200, "fontSize": 12, "fontWeight": "bold", "fill": P_GOLD_LIGHT }
                        ]},
                        # Row 2
                        { "type": "frame", "name": "TR 2", "width": "fill_container", "height": 52, "stroke": P_BORDER, "strokeWidth": { "top": 1 }, "layout": "horizontal", "padding": [0, 20], "alignItems": "center", "children": [
                            { "type": "text", "name": "c1", "content": "Planta Química Cartagena", "width": 280, "fontSize": 12, "fontWeight": "bold", "fill": "#FFFFFF" },
                            { "type": "text", "name": "c2", "content": "Infraestructura Crítica", "width": 180, "fontSize": 12, "fill": "#93C5FD" },
                            { "type": "text", "name": "c3", "content": "● Conectado 100%", "width": 180, "fontSize": 12, "fontWeight": "bold", "fill": P_EMERALD_LIGHT },
                            { "type": "text", "name": "c4", "content": "02 Sep 2026 (Superada)", "width": 220, "fontSize": 12, "fill": "#CBD5E1" },
                            { "type": "text", "name": "c5", "content": "Descargar PDF →", "width": 200, "fontSize": 12, "fontWeight": "bold", "fill": P_GOLD_LIGHT }
                        ]},
                        # Row 3
                        { "type": "frame", "name": "TR 3", "width": "fill_container", "height": 52, "stroke": P_BORDER, "strokeWidth": { "top": 1 }, "layout": "horizontal", "padding": [0, 20], "alignItems": "center", "children": [
                            { "type": "text", "name": "c1", "content": "Hub Logístico Valencia", "width": 280, "fontSize": 12, "fontWeight": "bold", "fill": "#FFFFFF" },
                            { "type": "text", "name": "c2", "content": "Grado 3 (Naves 1-4)", "width": 180, "fontSize": 12, "fill": P_GOLD_LIGHT },
                            { "type": "text", "name": "c3", "content": "● Conectado 100%", "width": 180, "fontSize": 12, "fontWeight": "bold", "fill": P_EMERALD_LIGHT },
                            { "type": "text", "name": "c4", "content": "28 Ago 2026 (Superada)", "width": 220, "fontSize": 12, "fill": "#CBD5E1" },
                            { "type": "text", "name": "c5", "content": "Descargar PDF →", "width": 200, "fontSize": 12, "fontWeight": "bold", "fill": P_GOLD_LIGHT }
                        ]}
                    ]}
                ]}
            ]}
        ]
    }

def build_s3_contacto(y_pos=22500):
    return {
        "type": "frame",
        "name": "Suite 3: [05] Contacto VIP & Asesoría Confidencial - Control 61",
        "x": 6000, "y": y_pos, "width": 1440, "height": 1600,
        "fill": P_BG, "layout": "vertical", "children": [
            suite3_header(active_nav="Contacto VIP"),
            { "type": "frame", "name": "Main", "width": "fill_container", "padding": [64, 100], "layout": "horizontal", "gap": 64, "children": [
                { "type": "frame", "name": "Left", "width": 500, "layout": "vertical", "gap": 20, "children": [
                    official_brand_badge(width=160, height=48, bg="#FFFFFF"),
                    { "type": "text", "name": "H", "content": "CANAL CONFIDENCIAL PARA COMITÉS DE DIRECCIÓN", "fontSize": 34, "fontWeight": "900", "fill": "#FFFFFF" },
                    { "type": "text", "name": "P", "content": "Si su corporación requiere una evaluación de seguridad de alta discreción con firma previa de acuerdo de confidencialidad (NDA), contacte directamente con nuestra Dirección de Seguridad.", "fontSize": 14, "lineHeight": 1.6, "fill": "#94A3B8" }
                ]},
                { "type": "frame", "name": "Form", "width": 640, "fill": P_CARD, "stroke": P_BORDER, "strokeWidth": 1, "cornerRadius": 12, "padding": [36, 36], "layout": "vertical", "gap": 20, "children": [
                    { "type": "text", "name": "T", "content": "SOLICITUD DE REUNIÓN PRIVADA (CON NDA)", "fontSize": 18, "fontWeight": "bold", "fill": P_GOLD_LIGHT },
                    { "type": "frame", "name": "F1", "layout": "vertical", "gap": 6, "children": [
                        { "type": "text", "name": "L", "content": "Representante del Comité de Seguridad / CISO", "fontSize": 12, "fill": "#CBD5E1" },
                        { "type": "frame", "name": "In", "height": 46, "fill": P_SURFACE, "stroke": P_BORDER, "strokeWidth": 1, "cornerRadius": 6, "padding": [0, 16], "justifyContent": "center", "children": [
                            { "type": "text", "name": "p", "content": "Nombre y cargo", "fontSize": 13, "fill": "#475569" }
                        ]}
                    ]},
                    { "type": "frame", "name": "F2", "layout": "vertical", "gap": 6, "children": [
                        { "type": "text", "name": "L", "content": "Teléfono de Contacto Confidencial", "fontSize": 12, "fill": "#CBD5E1" },
                        { "type": "frame", "name": "In", "height": 46, "fill": P_SURFACE, "stroke": P_BORDER, "strokeWidth": 1, "cornerRadius": 6, "padding": [0, 16], "justifyContent": "center", "children": [
                            { "type": "text", "name": "p", "content": "+34 600 000 000", "fontSize": 13, "fill": "#475569" }
                        ]}
                    ]},
                    { "type": "frame", "name": "Btn", "height": 50, "fill": P_GOLD, "cornerRadius": 6, "alignItems": "center", "justifyContent": "center", "children": [
                        { "type": "text", "name": "t", "content": "CONCERTAR REUNIÓN PRIVADA CON DIRECCIÓN →", "fontSize": 13, "fontWeight": "bold", "fill": "#FFFFFF" }
                    ]}
                ]}
            ]},
            suite3_footer()
        ]
    }

print("Suite 3 all 5 frames defined.")
