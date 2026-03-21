
import os
import sys
from pathlib import Path

# Reuse logic from bulk_upload_skills if possible, or duplicate for independence
# Duplicating logic to ensure standalone execution without dependency issues

def get_skill_content(skill_dir):
    """Aggregate SKILL.md and scripts from a skill directory"""
    skill_path = Path(skill_dir)
    skill_name = skill_path.name
    
    content = []
    content.append(f"# Skill: {skill_name}\n")
    
    # 1. Read SKILL.md
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
    
    # 2. Read Scripts
    scripts_dir = skill_path / "scripts"
    if scripts_dir.exists():
        content.append(f"## Scripts ({skill_name}/scripts)\n")
        
        # Get all .py and .ps1 files
        script_files = list(scripts_dir.glob("*.py")) + list(scripts_dir.glob("*.ps1"))
        
        for script in script_files:
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
            content.append("\n```\n")
            
    return "\n".join(content)

def main():
    # Hardcoded target for this task
    target_dir = Path(r"C:\Users\Rosta\Desktop\antigravity skills upload")
    
    if not target_dir.exists():
        print(f"❌ Target directory does not exist: {target_dir}")
        return

    print(f"🚀 Exporting skills to: {target_dir}")
    
    # Iterate Skills
    # specific structure: ../../../skills relative to this script in skills/notebooklm/scripts
    skills_base = Path(__file__).parent.parent.parent 
    
    if not skills_base.exists():
        # Fallback if running from a different cwd
         skills_base = Path(r"C:\Users\Rosta\ANTIGRAVITY MASTER FOLDER\notebooklm_context\skills")
    
    print(f"📂 Skills base: {skills_base}")
    
    skill_dirs = [d for d in skills_base.iterdir() if d.is_dir()]
    
    for skill in skill_dirs:
        if skill.name.startswith("__") or skill.name.startswith("."):
            continue
            
        print(f"📦 Processing Skill: {skill.name}")
        content = get_skill_content(skill)
        
        if len(content) < 100:
            print(f"  ⚠️ Skipping {skill.name} (insufficient content)")
            continue
            
        output_file = target_dir / f"{skill.name}.txt"
        
        try:
            with open(output_file, 'w', encoding='utf-8') as f:
                f.write(content)
            print(f"  ✅ Saved {output_file.name}")
        except Exception as e:
            print(f"  ❌ Failed to save {skill.name}: {e}")

if __name__ == "__main__":
    main()
