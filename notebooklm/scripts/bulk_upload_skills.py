
import os
import sys
import glob
from pathlib import Path
import subprocess
import argparse

# Add parent directory to path
sys.path.insert(0, str(Path(__file__).parent))

from notebook_manager import NotebookLibrary

def get_skill_content(skill_dir):
    """Aggregate SKILL.md and scripts from a skill directory"""
    skill_path = Path(skill_dir)
    skill_name = skill_path.name
    
    content = []
    content.append(f"# Skill: {skill_name}\n")
    
    # 1. Read SKILL.md (The most important part)
    skill_md = skill_path / "SKILL.md"
    if skill_md.exists():
        content.append(f"## Documentation ({skill_name}/SKILL.md)\n")
        try:
            with open(skill_md, 'r', encoding='utf-8') as f:
                content.append(f.read())
        except Exception as e:
            content.append(f"[Error reading SKILL.md: {e}]")
    else:
        print(f"⚠️ {skill_name}: No SKILL.md found")
    
    content.append("\n---\n")
    
    # 2. Read Scripts (briefly)
    scripts_dir = skill_path / "scripts"
    if scripts_dir.exists():
        content.append(f"## Scripts ({skill_name}/scripts)\n")
        
        # Get all .py and .ps1 files
        script_files = list(scripts_dir.glob("*.py")) + list(scripts_dir.glob("*.ps1"))
        
        for script in script_files:
            # Skip large files or certain types if needed
            if script.stat().st_size > 50000: # Skip > 50KB
                content.append(f"\n### {script.name} (Skipped - too large)\n")
                continue
                
            content.append(f"\n### {script.name}\n")
            content.append("```python" if script.suffix == ".py" else "```powershell")
            try:
                with open(script, 'r', encoding='utf-8') as f:
                    content.append(f.read())
            except Exception as e:
                content.append(f"[Error reading script: {e}]")
            content.append("```\n")
            
    return "\n".join(content)

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--notebook-id", help="Target notebook ID")
    parser.add_argument("--notebook-url", help="Target notebook URL (overrides ID)")
    parser.add_argument("--create-new", action="store_true", help="Create a new notebook 'Antigravity Skills Library'")
    args = parser.parse_args()
    
    library = NotebookLibrary()
    
    # 1. Determine Target Notebook
    notebook_id = args.notebook_id
    notebook_url = args.notebook_url
    
    if args.create_new and not notebook_url:
        print("🆕 Requesting creation of new 'Antigravity Skills Library' notebook...")
        # (This would use create_notebook.py logic, but for simplicity let's rely on finding one or URL)
        # Assuming we can't easily CREATE and GET URL in one step without calling create_notebook.py
        # Let's use subprocess to call create_notebook.py if needed, or ask user to provide URL if manual.
        # For now, let's limit to existing notebooks or URL.
        pass

    if not notebook_id and not notebook_url:
        # Try to find "Antigravity Skills Library"
        for nb in library.notebooks.values():
            if "skills" in nb.get('name', '').lower() or "library" in nb.get('name', '').lower():
                notebook_id = nb['id']
                notebook_url = f"https://notebooklm.google.com/notebook/{notebook_id}"
                print(f"🎯 Found existing skills notebook: {nb.get('title')} ({notebook_id})")
                break
    
    if not notebook_url and notebook_id:
         notebook_url = f"https://notebooklm.google.com/notebook/{notebook_id}"
         
    if not notebook_url:
        print("❌ No target notebook found. Please create one named 'Antigravity Skills Library' or provide --notebook-id")
        # Optional: Call create_notebook.py
        return

    print(f"🚀 Uploading skills to: {notebook_url}")
    
    # 2. Iterate Skills
    skills_base = Path(__file__).parent.parent.parent # /skills
    skill_dirs = [d for d in skills_base.iterdir() if d.is_dir()]
    
    temp_file = Path("temp_upload_content.txt")
    
    for skill in skill_dirs:
        if skill.name.startswith("__") or skill.name.startswith("."):
            continue
            
        print(f"\n📦 Processing Skill: {skill.name}")
        content = get_skill_content(skill)
        
        # Brief check if content is meaningful
        if len(content) < 100:
            print(f"  ⚠️ Skipping {skill.name} (insufficient content)")
            continue
            
        # Write to temp file for upload script
        with open(temp_file, 'w', encoding='utf-8') as f:
            f.write(content)
            
        # Call upload_text_source.py
        title = f"Skill: {skill.name}"
        
        cmd = [
            sys.executable,
            str(Path(__file__).parent / "run.py"),
            str(Path(__file__).parent / "upload_text_source.py"),
            "--url", notebook_url,
            "--title", title,
            "--content-file", str(temp_file)
        ]
        
        try:
            subprocess.run(cmd, check=True)
            print(f"  ✅ Uploaded {skill.name}")
        except subprocess.CalledProcessError as e:
            print(f"  ❌ Failed to upload {skill.name}")
        
    if temp_file.exists():
        temp_file.unlink()

if __name__ == "__main__":
    main()
