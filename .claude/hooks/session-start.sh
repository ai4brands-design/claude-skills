#!/bin/bash
# Session start hook for ai4brands-design/claude-skills
# Pulls latest skills from GitHub and updates CLAUDE.md

set -euo pipefail

REPO_DIR="${CLAUDE_PROJECT_DIR:-$(git rev-parse --show-toplevel 2>/dev/null || pwd)}"
CLAUDE_MD="$REPO_DIR/CLAUDE.md"

# Pull latest skills from GitHub
echo "Pulling latest skills from GitHub..." >&2
git -C "$REPO_DIR" pull origin master --ff-only 2>&1 | tail -1 >&2 || true

# Count skills
SKILL_COUNT=$(find "$REPO_DIR" -maxdepth 1 -mindepth 1 -type d ! -name '.*' | wc -l | tr -d ' ')

# List all skill names
SKILL_LIST=$(find "$REPO_DIR" -maxdepth 1 -mindepth 1 -type d ! -name '.*' -exec basename {} \; | sort | sed 's/^/- /')

# Rewrite CLAUDE.md with current data
cat > "$CLAUDE_MD" << EOF
# ai4brands-design / claude-skills

GitHub org: https://github.com/ai4brands-design
Repo: https://github.com/ai4brands-design/claude-skills

## Skills (${SKILL_COUNT} celkem)

${SKILL_LIST}
EOF

echo "Session start: ${SKILL_COUNT} skills načteno z GitHubu" >&2
