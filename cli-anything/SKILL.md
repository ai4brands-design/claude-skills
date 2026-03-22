---
name: cli-anything
description: "This skill should be used when the user wants to transform any application into an agent-native CLI, generate CLI interfaces automatically, create SKILL.md definitions for tools, or build automated 7-phase CLI generation pipelines inspired by CLI-Anything (HKUDS). Use when integrating professional software with AI agents via structured command-line interfaces."
version: 1.0.0
author: ai4brands-design
created: 2026-03-22
updated: 2026-03-22
platforms: [claude-code, codex, github-copilot-cli]
category: automation
tags: [cli, automation, agent-native, python, click, skill-generation, ai-agents]
risk: safe
---

# cli-anything

## Purpose

To transform any software application into an agent-native CLI interface by following the CLI-Anything methodology — a fully automated 7-phase pipeline (analysis → design → implementation → testing → documentation → SKILL.md generation → validation) that produces structured JSON output, interactive REPLs, and AI-discoverable skill definitions without requiring API modifications or GUI automation.

## When to Use This Skill

- User wants to make any desktop app or CLI tool agent-controllable
- User needs to auto-generate a CLI wrapper for professional software (Blender, GIMP, FFmpeg, LibreOffice, etc.)
- User wants to create SKILL.md files for agent-native tool discovery
- User is building an AI agent workflow that needs structured CLI output (JSON/YAML/CSV)
- User wants undo/redo, persistent state, or REPL interfaces for existing tools
- User is integrating with Claude Code, OpenClaw, Codex, or other AI agents via CLI

## Do Not Use This Skill When

- The target application already has a well-documented Python API or SDK
- The task is simple scripting with no need for agent-native discovery
- The user only needs a one-off shell script without reusability

## Instructions

1. Identify the target application and analyze its capabilities (Phase 1).
2. Design the CLI command hierarchy and output schemas (Phase 2).
3. Implement using Python + Click with JSON-first output (Phase 3).
4. Write pytest tests covering all commands (Phase 4).
5. Generate README and SKILL.md for agent discovery (Phase 5).
6. Validate the pipeline end-to-end (Phase 6).
7. Register the skill in the agent's skill index (Phase 7).

## Core Capabilities

### Phase 1: Application Analysis

Analyze the target application to discover its capabilities:

```python
# Inspect available commands, APIs, or GUI elements
import subprocess
import json

def analyze_application(app_name: str) -> dict:
    """Discover application capabilities via --help, man pages, or introspection."""
    result = subprocess.run([app_name, "--help"], capture_output=True, text=True)
    return {
        "app": app_name,
        "raw_help": result.stdout,
        "capabilities": extract_capabilities(result.stdout),
    }

def extract_capabilities(help_text: str) -> list[dict]:
    """Parse help text into structured capability list."""
    # Pattern: command name + description
    import re
    pattern = r"^\s{2,4}(\w[\w-]*)\s{2,}(.+)$"
    return [
        {"command": m.group(1), "description": m.group(2)}
        for m in re.finditer(pattern, help_text, re.MULTILINE)
    ]
```

### Phase 2: CLI Design

Design the command hierarchy using Click groups:

```python
import click
import json
import sys

@click.group()
@click.option("--output", "-o", type=click.Choice(["json", "yaml", "table", "csv"]), default="json")
@click.option("--quiet", "-q", is_flag=True)
@click.pass_context
def cli(ctx, output, quiet):
    """Agent-native CLI for <AppName>. All commands output structured JSON by default."""
    ctx.ensure_object(dict)
    ctx.obj["output"] = output
    ctx.obj["quiet"] = quiet
```

**Command naming conventions:**
- Use verb-noun format: `get-info`, `create-project`, `export-file`
- Group related commands: `cli project create`, `cli project list`
- Always support `--output json` for agent consumption

### Phase 3: Implementation Patterns

#### Structured JSON Output (Required for Agent Integration)

```python
@cli.command("get-info")
@click.argument("target")
@click.pass_context
def get_info(ctx, target: str):
    """Get structured information about target."""
    result = {
        "status": "success",
        "target": target,
        "data": {},  # application-specific data
        "metadata": {
            "command": "get-info",
            "timestamp": datetime.utcnow().isoformat(),
        }
    }
    output_result(ctx, result)

def output_result(ctx, data: dict):
    """Unified output handler supporting json/yaml/table/csv."""
    fmt = ctx.obj.get("output", "json")
    if fmt == "json":
        click.echo(json.dumps(data, indent=2))
    elif fmt == "yaml":
        import yaml
        click.echo(yaml.dump(data, default_flow_style=False))
    elif fmt == "table":
        _print_table(data)
    sys.exit(0 if data.get("status") == "success" else 1)
```

#### Undo/Redo with State Persistence

```python
import json
from pathlib import Path
from dataclasses import dataclass, field
from typing import Any

@dataclass
class StateManager:
    state_file: Path = Path(".cli-anything-state.json")
    history: list[dict] = field(default_factory=list)
    current_index: int = -1

    def save_action(self, action: str, data: Any, reverse_data: Any):
        """Record action for undo/redo."""
        self.history = self.history[:self.current_index + 1]
        self.history.append({"action": action, "data": data, "reverse": reverse_data})
        self.current_index += 1
        self._persist()

    def undo(self) -> dict | None:
        if self.current_index < 0:
            return None
        action = self.history[self.current_index]
        self.current_index -= 1
        return action

    def _persist(self):
        self.state_file.write_text(json.dumps({
            "history": self.history,
            "current_index": self.current_index,
        }))
```

#### REPL Interface

```python
import cmd

class AppREPL(cmd.Cmd):
    intro = "CLI-Anything REPL. Type 'help' for commands, 'exit' to quit."
    prompt = "cli-anything> "

    def do_run(self, arg):
        """Run a CLI command: run <command> [args...]"""
        import shlex
        args = shlex.split(arg)
        cli.main(args, standalone_mode=False)

    def do_exit(self, arg):
        """Exit REPL."""
        return True

    def do_EOF(self, arg):
        return True

@cli.command("repl")
def start_repl():
    """Start interactive REPL session."""
    AppREPL().cmdloop()
```

### Phase 4: Testing Patterns

```python
# tests/test_cli.py
import pytest
from click.testing import CliRunner
from myapp_cli import cli

@pytest.fixture
def runner():
    return CliRunner()

class TestGetInfo:
    def test_json_output(self, runner):
        result = runner.invoke(cli, ["get-info", "sample"])
        assert result.exit_code == 0
        data = json.loads(result.output)
        assert data["status"] == "success"
        assert "data" in data

    def test_yaml_output(self, runner):
        result = runner.invoke(cli, ["--output", "yaml", "get-info", "sample"])
        assert result.exit_code == 0
        import yaml
        data = yaml.safe_load(result.output)
        assert data["status"] == "success"

    def test_error_handling(self, runner):
        result = runner.invoke(cli, ["get-info", "nonexistent"])
        assert result.exit_code == 1
        data = json.loads(result.output)
        assert data["status"] == "error"

class TestUndo:
    def test_undo_last_action(self, runner, tmp_path):
        # Perform action then undo
        runner.invoke(cli, ["create", "item", "--name", "test"])
        result = runner.invoke(cli, ["undo"])
        assert result.exit_code == 0
        data = json.loads(result.output)
        assert data["undone"]["action"] == "create"
```

### Phase 5: SKILL.md Generation

Generate agent-discoverable SKILL.md automatically:

```python
SKILL_TEMPLATE = '''---
name: {skill_name}
description: "{description}"
version: {version}
platforms: [claude-code, codex, github-copilot-cli]
category: cli-automation
tags: {tags}
risk: safe
---

# {skill_name}

## Commands

{commands_section}

## Output Format

All commands return JSON by default:
```json
{{
  "status": "success|error",
  "data": {{}},
  "metadata": {{
    "command": "command-name",
    "timestamp": "ISO-8601"
  }}
}}
```

## Agent Integration

```bash
# Pipe output to other tools
{skill_name} get-info target | jq '.data'

# Use in Claude Code
claude "run {skill_name} get-info on myfile and summarize the results"
```
'''

def generate_skill_md(app_name: str, capabilities: list[dict]) -> str:
    commands_section = "\n".join([
        f"- `{c['command']}` — {c['description']}"
        for c in capabilities
    ])
    return SKILL_TEMPLATE.format(
        skill_name=app_name,
        description=f"Agent-native CLI for {app_name}. Use when automating {app_name} via AI agents.",
        version="1.0.0",
        tags=json.dumps([app_name, "cli", "automation"]),
        commands_section=commands_section,
    )
```

### Phase 6: Project Structure

Standard CLI-Anything project layout:

```
my-app-cli/
├── pyproject.toml          # uv/pip project config
├── SKILL.md                # Agent-discoverable skill definition
├── README.md               # Human-readable docs
├── src/
│   └── my_app_cli/
│       ├── __init__.py
│       ├── cli.py          # Click CLI entry point
│       ├── commands/       # One file per command group
│       │   ├── get.py
│       │   ├── create.py
│       │   └── export.py
│       ├── state.py        # StateManager for undo/redo
│       ├── output.py       # Unified output handler
│       └── repl.py         # REPL interface
├── tests/
│   ├── conftest.py
│   └── test_cli.py
└── scripts/
    └── generate_skill_md.py  # Auto-generate SKILL.md from CLI
```

### Phase 7: pyproject.toml Template

```toml
[build-system]
requires = ["hatchling"]
build-backend = "hatchling.build"

[project]
name = "my-app-cli"
version = "1.0.0"
description = "Agent-native CLI for MyApp"
requires-python = ">=3.10"
dependencies = [
    "click>=8.1",
    "pyyaml>=6.0",
    "rich>=13.0",  # optional: better table output
]

[project.scripts]
my-app-cli = "my_app_cli.cli:cli"

[tool.pytest.ini_options]
testpaths = ["tests"]

[tool.ruff]
line-length = 88
```

## Supported Application Types

### Native CLI Tools (ffmpeg, imagemagick, etc.)
Wrap existing CLI with structured JSON output and agent-friendly discovery.

### Electron Apps (Cursor, Discord, ChatGPT Desktop)
Use headless automation (playwright, pyautogui) with structured command wrappers.

### GUI Applications (Blender, GIMP, LibreOffice)
Leverage application scripting APIs (Python console in Blender, macro API in LibreOffice).

### Web Applications
Combine with browser automation skills for headless web interaction.

## Integration with AI Agents

### Claude Code Integration
```bash
# Register skill
cp SKILL.md ~/.claude/skills/my-app-cli/SKILL.md

# Use in session
claude "use my-app-cli to export the current project as PDF"
```

### OpenClaw Integration
```bash
clawhub install my-app-cli
# or manual:
cp -r . ~/.openclaw/skills/my-app-cli/
```

### Codex Integration
```bash
cp SKILL.md ~/.codex/skills/my-app-cli/SKILL.md
```

## Behavioral Traits

- Always output JSON by default for agent consumption
- Exit code 0 = success, non-zero = error (critical for agent pipelines)
- Include metadata (timestamp, command name) in every response
- Support `--output` flag: json, yaml, table, csv
- Implement `--quiet` mode that outputs only the data payload
- Every destructive action supports undo via StateManager
- REPL mode available for interactive agent sessions
- SKILL.md auto-generated from CLI introspection

## Example Interactions

- "Create an agent-native CLI for FFmpeg with JSON output"
- "Generate a SKILL.md for my existing Python CLI tool"
- "Add undo/redo support to this Click application"
- "Wrap Blender's Python API as a Claude Code skill"
- "Build a CLI-Anything pipeline for LibreOffice automation"
- "Make this CLI tool discoverable by AI agents"
- "Add structured JSON output to my existing bash scripts"
- "Create a REPL interface for this CLI tool"

## References

- CLI-Anything project: https://github.com/HKUDS/CLI-Anything
- Click documentation: https://click.palletsprojects.com/
- OpenClaw skills: https://github.com/jackwener/opencli
