import re

# Update official_brand_badge in generate_three_radical_suites.py
with open("/Users/toni/Proyectos/Control61-Web/generate_three_radical_suites.py", "r") as f:
    code = f.read()

new_badge_func = '''def official_brand_badge(width=175, height=46, bg="#FFFFFF", border="#E2E8F0"):
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
                        "alignItems": "baseline",
                        "children": [
                            { "type": "text", "name": "CONTROL", "content": "CONTROL", "fontSize": 14, "fontWeight": "900", "fill": "#0F172A" },
                            { "type": "text", "name": "61", "content": "61", "fontSize": 15, "fontWeight": "900", "fill": "#DC2626" }
                        ]
                    },
                    { "type": "text", "name": "Sub", "content": "SISTEMAS DE SEGURIDAD", "fontSize": 7, "fontWeight": "700", "fill": "#64748B" }
                ]
            }
        ]
    }'''

# Replace old definition
code = re.sub(
    r'def official_brand_badge\(.*?\n\s+return \{[\s\S]*?\n\s+\}',
    new_badge_func,
    code,
    count=1
)

with open("/Users/toni/Proyectos/Control61-Web/generate_three_radical_suites.py", "w") as f:
    f.write(code)

print("Updated generate_three_radical_suites.py with vector brand badge.")
