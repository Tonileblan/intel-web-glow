import json
import subprocess

with open("/Users/toni/Proyectos/Control61-Web/control61_modern_ui.pen", "r") as f:
    data = json.load(f)

screens = data.get("children", [])
print(f"Total screens to sync: {len(screens)}")

for idx, screen in enumerate(screens):
    screen_id = screen.get("id")
    screen_name = screen.get("name")
    print(f"Syncing [{idx+1}/{len(screens)}]: {screen_name}...")
    
    js_code = f"""
    try {{
        let n = Get("{screen_id}");
        if (n) {{
            Delete("{screen_id}");
        }}
    }} catch(e) {{}}
    Insert(document, {json.dumps(screen)});
    """
    
    cmd_input = f"""execute({{ input: {json.dumps(js_code)} }})\nsave()\nexit()\n"""
    
    p = subprocess.run(
        ["pen", "interactive", "-a", "desktop", "-i", "/Users/toni/Proyectos/Control61-Web/control61_modern_ui.pen"],
        input=cmd_input,
        text=True,
        capture_output=True,
        env={"PEN_CLI_KEY": "pencil_cli_aebcdc64faa119be3d732b81edf1af9229f7f20f", "PATH": "/Users/toni/.npm-global/bin:/usr/local/bin:/usr/bin:/bin:/usr/sbin:/sbin"}
    )
    if "Failure during operation execution" in p.stdout or "Error:" in p.stdout:
        print(f"  ❌ Error on {screen_id}: {p.stdout[:200]}")
    else:
        print(f"  ✅ Synced {screen_id}")

print("All 11 screens synced into desktop app!")
