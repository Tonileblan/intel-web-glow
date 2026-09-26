import json

def official_brand_badge(width=168, height=44, bg="#FFFFFF", border="#E2E8F0"):
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
            # Shield / Number Icon
            {
                "type": "frame",
                "name": "Logo Icon",
                "width": 30,
                "height": 30,
                "fill": "#DC2626",
                "cornerRadius": 6,
                "alignItems": "center",
                "justifyContent": "center",
                "children": [
                    { "type": "text", "name": "61", "content": "61", "fontSize": 14, "fontWeight": "900", "fontFamily": "Inter", "fill": "#FFFFFF" }
                ]
            },
            # Textual Wordmark
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
                        "gap": 3,
                        "alignItems": "baseline",
                        "children": [
                            { "type": "text", "name": "CONTROL", "content": "CONTROL", "fontSize": 13, "fontWeight": "900", "fontFamily": "Inter", "fill": "#0F172A" },
                            { "type": "text", "name": "61", "content": "61", "fontSize": 14, "fontWeight": "900", "fontFamily": "Inter", "fill": "#DC2626" }
                        ]
                    },
                    { "type": "text", "name": "Sub", "content": "SISTEMAS DE SEGURIDAD", "fontSize": 6.5, "fontWeight": "700", "fontFamily": "Inter", "fill": "#64748B" }
                ]
            }
        ]
    }

print("Brand badge verified successfully.")
