---
name: glm-claude-code-cheap
description: >
  Konfigurace Claude Code pro použití GLM modelů (Z.AI) místo nativního Anthropic API —
  dosažení 10x nižších nákladů při srovnatelném výkonu. Použij při nastavování Claude Code,
  řešení nákladů na API, konfiguraci ~/.claude/settings.json, nebo přepínání modelů.
  Trigger: Claude Code setup, API costs, GLM, Z.AI, settings.json konfigurace.
---

# GLM + Claude Code — 10x levnější provoz

Zdroj: Z.AI / GLM Coding Plan tutorial  
Stack: Claude Code + GLM-5.1 přes Z.AI OpenPlatform  

**Princip:** Claude Code interface zůstává stejný, ale pod kapotou běží GLM model přes Z.AI API.  
Výsledek: 3x více usage tokenů za zlomek ceny Anthropic plánů.

---

## QUICK SETUP (3 kroky)

### 1. Instalace Claude Code
```bash
npm install -g @anthropic-ai/claude-code
```
**Mac:** použij `nvm` pro Node.js, ne přímý package installer (permission issues)  
**Windows:** doinstaluj Git for Windows

### 2. Z.AI API Key
1. Jdi na z.ai → Register/Login
2. API Keys management → Create API Key
3. Zkopíruj key

### 3. Konfigurace ~/.claude/settings.json

**Automaticky (Mac/Linux):**
```bash
curl -O "https://cdn.bigmodel.cn/install/claude_code_zai_env.sh" && bash ./claude_code_zai_env.sh
```

**Manuálně:**
```json
{
  "env": {
    "ANTHROPIC_AUTH_TOKEN": "tvuj_zai_api_key",
    "ANTHROPIC_BASE_URL": "https://api.z.ai/api/anthropic",
    "API_TIMEOUT_MS": "3000000"
  }
}
```

---

## MODEL MAPPING

Default (doporuceno):

| Claude Code model | GLM model |
|---|---|
| Opus | GLM-4.7 |
| Sonnet | GLM-4.7 |
| Haiku | GLM-4.5-Air |

**Pro GLM-5.1 max vykon:**
```json
{
  "env": {
    "ANTHROPIC_AUTH_TOKEN": "tvuj_zai_api_key",
    "ANTHROPIC_BASE_URL": "https://api.z.ai/api/anthropic",
    "API_TIMEOUT_MS": "3000000",
    "ANTHROPIC_DEFAULT_HAIKU_MODEL": "glm-4.5-air",
    "ANTHROPIC_DEFAULT_SONNET_MODEL": "glm-5-turbo",
    "ANTHROPIC_DEFAULT_OPUS_MODEL": "glm-5.1"
  }
}
```

---

## OVERENI

```bash
cd tvuj-projekt
claude
/status
claude --version
claude update
```

---

## TROUBLESHOOTING

| Problem | Reseni |
|---|---|
| settings.json nema efekt | Zavri vsechna CC okna, novy terminal |
| Stale nefunguje | Smaz ~/.claude/settings.json, rekonfiguruj |
| JSON error | Validuj na jsonlint.com |
| Permission error npm Mac | Pouzij nvm |

---

## APLIKACE PRO ROSTU

| Use case | Benefit |
|---|---|
| UGC Engine development | 10x vice iteraci za stejnou cenu |
| FastAPI/Python sessions | GLM-5.1 = srovnatelny vykon se Sonnet |
| n8n debugging | Haiku GLM-4.5-Air pro rychle tasky |
| Dlouhe agentic sessions | API_TIMEOUT_MS=3000000 = 50min timeout |

---

**Zdroje:**
- Z.AI Platform: https://z.ai
- Claude Code docs: https://docs.anthropic.com/en/docs/claude-code/overview
