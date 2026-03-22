# cli-anything

**Transform any application into an agent-native CLI using the CLI-Anything methodology.**

Inspired by [CLI-Anything (HKUDS)](https://github.com/HKUDS/CLI-Anything) — a 7-phase automated pipeline that generates complete, testable, AI-discoverable CLI interfaces for any software without touching the original application's source code.

## What It Does

- Wraps any desktop app, GUI tool, or existing CLI into a structured command-line interface
- Outputs JSON/YAML/table/CSV for seamless AI agent consumption
- Generates SKILL.md definitions for Claude Code, OpenClaw, and Codex discovery
- Adds undo/redo state management and interactive REPL mode
- Produces pytest test suites with 90%+ coverage targets

## When to Use

Use this skill when you want to:
- Make Blender, GIMP, LibreOffice, FFmpeg, or any tool agent-controllable
- Auto-generate a CLI with structured JSON output for AI pipelines
- Create SKILL.md definitions so Claude Code can discover your tools
- Add undo/redo and REPL interfaces to existing CLI tools
- Build reproducible automation pipelines for professional software

## Quick Start

```bash
# Analyze target application
claude "use cli-anything to create an agent-native CLI for ffmpeg"

# The skill will generate:
# - src/ffmpeg_cli/cli.py   (Click CLI with JSON output)
# - tests/test_cli.py       (pytest test suite)
# - SKILL.md                (agent-discoverable definition)
# - README.md               (human docs)
```

## Usage Examples

### Wrap an existing CLI tool

```bash
# Ask Claude to generate a CLI-Anything wrapper
claude "create a cli-anything wrapper for imagemagick with commands: convert, resize, crop, info"
```

### Generate SKILL.md for an existing tool

```bash
claude "generate a SKILL.md for my python CLI at ./myapp/cli.py"
```

### Add JSON output to existing Click app

```bash
claude "add structured JSON output and undo/redo to this Click CLI"
```

## Output Format

All generated CLIs return structured JSON:

```json
{
  "status": "success",
  "data": { "...": "application-specific result" },
  "metadata": {
    "command": "convert",
    "timestamp": "2026-03-22T10:00:00Z"
  }
}
```

Exit code `0` = success, non-zero = error — compatible with agent pipelines and shell scripting.

## Tech Stack

- **Python 3.10+** with Click 8.1+
- **pytest** for auto-generated test suites
- **PyYAML** for YAML output mode
- **rich** (optional) for table output
- **uv** for fast dependency management

## File Structure Generated

```
my-app-cli/
├── SKILL.md                # Agent-discoverable definition
├── README.md
├── pyproject.toml
├── src/my_app_cli/
│   ├── cli.py              # Main Click entrypoint
│   ├── commands/           # One file per command group
│   ├── state.py            # Undo/redo state manager
│   ├── output.py           # JSON/YAML/table/CSV output
│   └── repl.py             # Interactive REPL
└── tests/
    └── test_cli.py
```

## Supported Application Types

| Type | Examples | Method |
|------|----------|--------|
| Native CLI | ffmpeg, imagemagick, git | Subprocess wrapper + JSON output |
| Electron Apps | Cursor, Discord, ChatGPT | Headless automation layer |
| GUI Apps | Blender, GIMP, LibreOffice | Application scripting APIs |
| Web Apps | Any website | Browser automation |

## Agent Integration

After generation, register with your AI agent:

```bash
# Claude Code
cp SKILL.md ~/.claude/skills/my-app-cli/SKILL.md

# OpenClaw
cp -r . ~/.openclaw/skills/my-app-cli/

# Codex
cp SKILL.md ~/.codex/skills/my-app-cli/SKILL.md
```

---

**Version:** 1.0.0
**Platform:** Claude Code, Codex, GitHub Copilot CLI
**Reference:** https://github.com/HKUDS/CLI-Anything
