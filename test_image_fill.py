import json
import subprocess

test_screen = {
    "type": "frame",
    "id": "test-img-screen",
    "name": "Test Image Screen",
    "x": 0,
    "y": 0,
    "width": 600,
    "height": 400,
    "cornerRadius": 12,
    "clip": True,
    "fill": [
        {
            "type": "image",
            "url": "https://images.unsplash.com/photo-1557597774-9d273605dfa9?auto=format&fit=crop&w=1200&q=80",
            "mode": "fill"
        },
        {
            "type": "gradient",
            "gradientType": "linear",
            "rotation": 180,
            "colors": [
                { "color": "#070A1100", "position": 0 },
                { "color": "#070A11F0", "position": 1 }
            ]
        }
    ],
    "children": [
        {
            "type": "text",
            "id": "test-img-t",
            "name": "Text",
            "content": "CCTV IA 4K ULTRA HD",
            "fontSize": 24,
            "fontWeight": "800",
            "fill": "#FFFFFF",
            "x": 24,
            "y": 320
        }
    ]
}

js = f"Insert(document, {json.dumps(test_screen)});"
cmd = f"execute({{ input: {json.dumps(js)} }})\nsave()\nexit()\n"

p = subprocess.run(
    ["pen", "interactive", "-i", "/Users/toni/Proyectos/Control61-Web/control61_modern_ui.pen", "-o", "/Users/toni/Proyectos/Control61-Web/control61_modern_ui.pen"],
    input=cmd,
    text=True, capture_output=True,
    env={"PEN_CLI_KEY": "pencil_cli_aebcdc64faa119be3d732b81edf1af9229f7f20f", "PATH": "/Users/toni/.npm-global/bin:/usr/local/bin:/usr/bin:/bin:/usr/sbin:/sbin"}
)
print("Output:", p.stdout)
