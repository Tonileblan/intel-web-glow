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

# 1. Build dictionary of 15 frames
frames_data = [
    # Suite 1 (Red Industrial Tactical) Y = 14500
    ("v2_s1_01_home_red", build_s1_home(14500)),
    ("v2_s1_02_nosotros_red", build_s1_nosotros(14500)),
    ("v2_s1_03_servicios_red", build_s1_servicios(14500)),
    ("v2_s1_04_webapp_cad_red", build_s1_webapp(14500)),
    ("v2_s1_05_contacto_red", build_s1_contacto(14500)),

    # Suite 2 (Cyber-AI SOC Neural Vision) Y = 18500
    ("v2_s2_01_home_blue", build_s2_home(18500)),
    ("v2_s2_02_nosotros_blue", build_s2_nosotros(18500)),
    ("v2_s2_03_soluciones_blue", build_s2_soluciones(18500)),
    ("v2_s2_04_webapp_studio_blue", build_s2_webapp(18500)),
    ("v2_s2_05_contacto_blue", build_s2_contacto(18500)),

    # Suite 3 (Platinum Executive Governance) Y = 22500
    ("v2_s3_01_home_plat", build_s3_home(22500)),
    ("v2_s3_02_nosotros_plat", build_s3_nosotros(22500)),
    ("v2_s3_03_sectores_plat", build_s3_sectores(22500)),
    ("v2_s3_04_webapp_hub_plat", build_s3_webapp(22500)),
    ("v2_s3_05_contacto_plat", build_s3_contacto(22500)),
]

print(f"Total new radical frames generated: {len(frames_data)}")

# 2. Update .pen file
with open(PEN_FILE, "r") as f:
    doc = json.load(f)

# Keep track of existing node IDs and root children
existing_children = list(doc.get("children", []))
existing_keys = set(doc.keys())

# We want to insert each frame properly into doc
id_counter = 100
for name, frame_node in frames_data:
    # Assign unique top ID
    frame_id = f"rad_{name}"
    frame_node["id"] = frame_id
    
    # Recursive helper to assign unique IDs to all sub-nodes
    def assign_ids(node, parent_id):
        global id_counter
        id_counter += 1
        n_id = f"{parent_id}_{id_counter}"
        node["id"] = n_id
        if "children" in node and isinstance(node["children"], list):
            for child in node["children"]:
                if isinstance(child, dict):
                    assign_ids(child, n_id)
    
    if "children" in frame_node and isinstance(frame_node["children"], list):
        for child in frame_node["children"]:
            if isinstance(child, dict):
                assign_ids(child, frame_id)
                
    # Add to doc children if not already present
    if frame_id not in doc.get("children", []):
        doc["children"].append(frame_id)
    doc[frame_id] = frame_node

with open(PEN_FILE, "w") as f:
    json.dump(doc, f, indent=2)

print(f"Saved master .pen file: {PEN_FILE} with {len(doc.get('children', []))} total frames on canvas.")

# 3. Push to Desktop via pen interactive
env = os.environ.copy()
env["PEN_CLI_KEY"] = "pencil_cli_aebcdc64faa119be3d732b81edf1af9229f7f20f"
push_cmd = f"pen interactive -a desktop -i '{PEN_FILE}'"
try:
    res = subprocess.run(push_cmd, shell=True, env=env, capture_output=True, text=True, timeout=20)
    print("Desktop push output:", res.stdout[:300])
except Exception as e:
    print("Desktop push exception:", e)

# 4. Export each frame to PNG
print("\nExporting 15 frames to PNG...")
for name, _ in frames_data:
    frame_id = f"rad_{name}"
    out_png = os.path.join(EXPORTS_DIR, f"{name}.png")
    export_cmd = f"pen --in '{PEN_FILE}' --out '{PEN_FILE}' --export '{out_png}' --export-type png --export-scale 1 --export-target '{frame_id}'"
    try:
        sub = subprocess.run(export_cmd, shell=True, env=env, capture_output=True, text=True, timeout=25)
        if os.path.exists(out_png):
            art_png = os.path.join(ARTIFACTS_DIR, f"{name}.png")
            shutil.copy(out_png, art_png)
            print(f"✓ Exported {name}.png ({os.path.getsize(out_png)} bytes)")
        else:
            print(f"✗ Failed to export {name}: {sub.stderr[:200]}")
    except Exception as ex:
        print(f"Export error for {name}: {ex}")

print("\nMaster update complete!")
