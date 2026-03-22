#!/bin/bash
# Session start hook for ai4brands-design/claude-skills
# Updates CLAUDE.md with current skill count and optionally fetches org info from GitHub

set -euo pipefail

REPO_DIR="${CLAUDE_PROJECT_DIR:-$(git rev-parse --show-toplevel 2>/dev/null || pwd)}"
CLAUDE_MD="$REPO_DIR/CLAUDE.md"

# Count skills (subdirectories in repo root, excluding hidden dirs and files)
SKILL_COUNT=$(find "$REPO_DIR" -maxdepth 1 -mindepth 1 -type d ! -name '.*' | wc -l | tr -d ' ')

# Update skill count in CLAUDE.md
if [ -f "$CLAUDE_MD" ]; then
  sed -i "s/Total skills in this repo: [0-9]*/Total skills in this repo: $SKILL_COUNT/" "$CLAUDE_MD"
fi

# Optionally fetch org info from GitHub API (requires GITHUB_TOKEN)
if [ -n "${GITHUB_TOKEN:-}" ]; then
  ORG_INFO=$(curl -sf -H "Authorization: token $GITHUB_TOKEN" \
    "https://api.github.com/orgs/ai4brands-design" 2>/dev/null || echo "")

  if [ -n "$ORG_INFO" ]; then
    REPO_COUNT=$(echo "$ORG_INFO" | grep -o '"public_repos":[0-9]*' | grep -o '[0-9]*' || echo "")
    if [ -n "$REPO_COUNT" ] && [ -f "$CLAUDE_MD" ]; then
      # Append or update org repo count section
      if grep -q "GITHUB_ORG_REPOS" "$CLAUDE_MD"; then
        sed -i "s/GitHub org repos: [0-9]*/GitHub org repos: $REPO_COUNT/" "$CLAUDE_MD"
      else
        echo "" >> "$CLAUDE_MD"
        echo "<!-- GITHUB_ORG_REPOS: $REPO_COUNT repositories in ai4brands-design org -->" >> "$CLAUDE_MD"
      fi
    fi
  fi
fi

echo "Session start: $SKILL_COUNT skills found in claude-skills repo" >&2
