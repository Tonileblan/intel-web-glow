import json
import os
import shutil
import subprocess

from build_suite1_all import (
    build_s1_home, build_s1_nosotros, build_s1_servicios, build_s1_webapp, build_s1_contacto
)
from build_suite2_all import (
    build_s2_home, build_s2_nosotros, build_s2_soluciones, build_s2_webapp, build_s2_contacto
)
from build_suite3_all import (
    build_s3_home, build_s3_nosotros, build_s3_sectores, build_s3_webapp, build_s3_contacto
)

PEN_FILE = "/Users/toni/Proyectos/Control61-Web/control61_modern_ui.pen"
EXPORTS_DIR = "/Users/toni/Proyectos/Control61-Web/exports"
ARTIFACTS_DIR = "/Users/toni/.gemini/antigravity-ide/brain/0fd50a11-6b5f-44b2-9e53-8b92848e2ae2"

os.makedirs(EXPORTS_DIR, exist_ok=True)
os.makedirs(ARTIFACTS_DIR, exist_ok=True)

# Build the 15 radical frames
s1_screens = [
    build_s1_home(14500),
    build_s1_nosotros(14500),
    build_s1_servicios(14500),
    build_s1_webapp(14500),
    build_s1_contacto(14500)
]
s1_screens[0]["id"] = "rad_s1_01_home_red"
s1_screens[1]["id"] = "rad_s1_02_nosotros_red"
s1_screens[2]["id"] = "rad_s1_03_servicios_red"
s1_screens[3]["id"] = "rad_s1_04_webapp_cad_red"
s1_screens[4]["id"] = "rad_s1_05_contacto_red"

s2_screens = [
    build_s2_home(18500),
    build_s2_nosotros(18500),
    build_s2_soluciones(18500),
    build_s2_webapp(18500),
    build_s2_contacto(18500)
]
s2_screens[0]["id"] = "rad_s2_01_home_blue"
s2_screens[1]["id"] = "rad_s2_02_nosotros_blue"
s2_screens[2]["id"] = "rad_s2_03_soluciones_blue"
s2_screens[3]["id"] = "rad_s2_04_webapp_studio_blue"
s2_screens[4]["id"] = "rad_s2_05_contacto_blue"

s3_screens = [
    build_s3_home(22500),
    build_s3_nosotros(22500),
    build_s3_sectores(22500),
    build_s3_webapp(22500),
    build_s3_contacto(22500)
]
s3_screens[0]["id"] = "rad_s3_01_home_plat"
s3_screens[1]["id"] = "rad_s3_02_nosotros_plat"
s3_screens[2]["id"] = "rad_s3_03_sectores_plat"
s3_screens[3]["id"] = "rad_s3_04_webapp_hub_plat"
s3_screens[4]["id"] = "rad_s3_05_contacto_plat"

# Offset X coordinates for each suite's 5 pages
for suite in [s1_screens, s2_screens, s3_screens]:
    for i, scr in enumerate(suite):
        scr["x"] = i * 1550

all_15_screens = s1_screens + s2_screens + s3_screens
all_15_ids = [s["id"] for s in all_15_screens]

# Load existing doc
try:
    with open(PEN_FILE, "r", encoding="utf-8") as f:
        doc = json.load(f)
except Exception:
    doc = { "version": "2.19", "children": [] }

# Filter children list (ensure children is list of dicts)
existing_children = []
if "children" in doc and isinstance(doc["children"], list):
    for c in doc["children"]:
        if isinstance(c, dict) and c.get("id") not in all_15_ids:
            existing_children.append(c)

doc["children"] = existing_children + all_15_screens

with open(PEN_FILE, "w", encoding="utf-8") as f:
    json.dump(doc, f, indent=2, ensure_ascii=False)

print(f"Updated {PEN_FILE} with {len(doc['children'])} total screens on canvas!")

# Live sync & export via Pencil JS runtime
js_code = f"""
const screens = {json.dumps(all_15_screens)};
const ids = [];
for (const s of screens) {{
    try {{ Delete(s.id); }} catch(e) {{}}
    const newId = Insert(document, s);
    ids.push(newId);
}}
Print('Inserted ' + ids.length + ' radical screens into Canvas.');
Export(ids, 'png', './exports');
Print('Exported all ' + ids.length + ' screens to ./exports');
"""

cmd_input = f"""execute({{ input: {json.dumps(js_code)} }})\nsave()\nexit()\n"""

env = os.environ.copy()
env["PEN_CLI_KEY"] = "pencil_cli_aebcdc64faa119be3d732b81edf1af9229f7f20f"
env["PATH"] = "/Users/toni/.npm-global/bin:/usr/local/bin:/usr/bin:/bin:/usr/sbin:/sbin"

print("Syncing with Pencil Desktop and exporting PNGs...")
p = subprocess.run(
    ["pen", "interactive", "-a", "desktop", "-i", PEN_FILE],
    input=cmd_input,
    text=True,
    capture_output=True,
    env=env,
    timeout=60
)
print("STDOUT:", p.stdout)
print("STDERR:", p.stderr)

# Copy exported PNGs to artifacts directory
exported_files = [f for f in os.listdir(EXPORTS_DIR) if f.endswith(".png")]
print(f"Total exported PNGs in {EXPORTS_DIR}: {len(exported_files)}")
for f in exported_files:
    src_p = os.path.join(EXPORTS_DIR, f)
    dst_p = os.path.join(ARTIFACTS_DIR, f)
    shutil.copy(src_p, dst_p)

print("Export and artifact copy complete!")
