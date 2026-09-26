import json
import subprocess

# Generate the 11 screens list
from generate_and_sync_all_screens import build_screens

screens = build_screens()
print(f"Screens to insert: {len(screens)}")

# Build JS script to clear root and insert all 11 screens
js_code = """
let allNodes = Get((n, c) => { c.skipChildren(); return n.id; });
for (let id of allNodes) {
    try { Delete(id); } catch(e) {}
}
"""

for screen in screens:
    js_code += f"Insert(document, {json.dumps(screen)});\n"

js_code += "Print('All 11 screens inserted successfully');"

cmd_input = f"""execute({{ input: {json.dumps(js_code)} }})\nsave()\nexit()\n"""

p = subprocess.run(
    ["pen", "interactive", "-a", "desktop", "-i", "/Users/toni/Proyectos/Control61-Web/control61_modern_ui.pen"],
    input=cmd_input,
    text=True,
    capture_output=True,
    env={"PEN_CLI_KEY": "pencil_cli_aebcdc64faa119be3d732b81edf1af9229f7f20f", "PATH": "/Users/toni/.npm-global/bin:/usr/local/bin:/usr/bin:/bin:/usr/sbin:/sbin"}
)

print("Pencil Desktop Output:")
print(p.stdout)
if p.stderr:
    print("Stderr:", p.stderr)
