#!/bin/bash
# Install all Claude Code skills from ai4brands-design/claude-skills
set -e

SKILLS_DIR="$HOME/.claude/skills"
REPO="https://github.com/ai4brands-design/claude-skills"
TMP=$(mktemp -d)

echo "Installing Claude Code skills..."
mkdir -p "$SKILLS_DIR"

# Clone repo to temp dir
git clone --depth=1 "$REPO" "$TMP/skills" 2>&1 | tail -1

# Copy all skill folders (exclude git/readme/script files)
find "$TMP/skills" -maxdepth 1 -mindepth 1 -type d | while read dir; do
  name=$(basename "$dir")
  cp -r "$dir" "$SKILLS_DIR/"
  echo "  ✓ $name"
done

# Cleanup
rm -rf "$TMP"

COUNT=$(ls "$SKILLS_DIR" | wc -l | tr -d ' ')
echo ""
echo "Done! $COUNT skills installed to $SKILLS_DIR"
echo "Restart Claude Code to activate."
