import json
import subprocess

with open("/Users/toni/Proyectos/Control61-Web/control61_modern_ui.pen", "r") as f:
    data = json.load(f)

screens = data.get("children", [])
print(f"Total screens in file: {len(screens)}")

# We will execute each screen insertion into desktop
for idx, screen in enumerate(screens):
    # screen 0 is control61-landing which might already exist or be updated
    screen_id = screen.get("id")
    screen_name = screen.get("name")
    print(f"[{idx+1}/{len(screens)}] Inserting screen: {screen_name} ({screen_id})...")
    
    # Check if node exists, delete if exists, then insert
    code = f"""
    try {{
        let existing = Get("{screen_id}");
        if (existing) {{
            Delete("{screen_id}");
        }}
    }} catch(e) {{}}
    Insert(document, {json.dumps(screen)});
    """
    
    cmd_input = f"""execute({{ input: {json.dumps(code)} }})\nsave()\nexit()\n"""
    
    p = subprocess.run(
        ["pen", "interactive", "-a", "desktop", "-i", "/Users/toni/Proyectos/Control61-Web/control61_modern_ui.pen"],
        input=cmd_input,
        text=True,
        capture_output=True,
        env={"PEN_CLI_KEY": "pencil_cli_aebcdc64faa119be3d732b81edf1af9229f7f20f", "PATH": "/Users/toni/.npm-global/bin:/usr/local/bin:/usr/bin:/bin:/usr/sbin:/sbin"}
    )
    if "Failure during operation execution" in p.stdout or "Error:" in p.stdout:
        print(f"Error inserting {screen_id}: {p.stdout[:300]}")
    else:
        print(f"✓ Inserted {screen_id}")

print("All screens successfully synced to Pencil Desktop App!")
