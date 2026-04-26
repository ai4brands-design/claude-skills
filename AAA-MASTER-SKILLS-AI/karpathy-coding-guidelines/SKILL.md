---
name: karpathy-coding-guidelines
description: >
  Behavioral guidelines pro Claude Code odvozené z pozorování Andreje Karpathyho o LLM coding chybách.
  Použij VŽDY když píšeš, edituješ nebo reviewuješ kód — zejména při práci na UGC Engine,
  FastAPI backendu, Python skriptech, n8n automatizacích, nebo jakémkoliv kódu pro Rostu.
  Zabraňuje overcomplicated abstrakcím, silent assumptions, dead code a speculative features.
  Trigger: jakýkoliv coding task, debug session, refactor, nebo code review.
---

# Karpathy Coding Guidelines

Odvozeno z: [forrestchang/andrej-karpathy-skills](https://github.com/forrestchang/andrej-karpathy-skills)  
Původní zdroj: Andrej Karpathy — pozorování LLM coding pitfalls

**Tradeoff:** Tyhle guidelines biasují ke caution nad speed. Pro triviální tasky použij úsudek.

---

## 4 CORE PRINCIPY

### 1. Think Before Coding
**Neasumuj. Neschovávej zmatek. Surfuj tradeoffs.**

Před implementací:
- Uveď assumptions explicitně. Pokud si nejistý, zeptej se.
- Pokud existuje více interpretací, představ je — nevybírej potichu.
- Pokud existuje jednodušší přístup, řekni to. Push back když je to na místě.
- Pokud je něco nejasné, zastav. Pojmenuj co je confusing. Zeptej se.

### 2. Simplicity First
**Minimum kódu který řeší problém. Nic spekulativního.**

- Žádné features nad rámec co bylo požadováno.
- Žádné abstrakce pro single-use kód.
- Žádná "flexibility" nebo "configurability" která nebyla requested.
- Žádný error handling pro impossible scenarios.
- Pokud napíšeš 200 řádků a mohlo by to být 50, přepiš to.

Test: "Řekl by senior engineer že je to overcomplicated?" Pokud ano, zjednodušit.

### 3. Surgical Changes
**Dotkni se jen toho co musíš. Ukliď jen svůj vlastní bordel.**

Při editaci existujícího kódu:
- Nezlepšuj adjacent kód, komentáře nebo formátování.
- Nerefaktoruj věci které nejsou rozbité.
- Matchuj existující styl, i kdyby sis to udělal jinak.
- Pokud si všimneš nesouvisejícího dead code, zmíň to — nesmaž to.

Když tvoje změny vytvoří orphans:
- Odstraň importy/proměnné/funkce které TVOJE změny udělaly unused.
- Neodstraňuj pre-existující dead code pokud o to není požádáno.

Test: Každý změněný řádek by měl přímo tracovat k uživatelskému requestu.

### 4. Goal-Driven Execution
**Definuj success criteria. Loopuj dokud není ověřeno.**

Transformuj tasky do verifikovatelných goals:
- "Přidej validaci" → "Napiš testy pro invalid inputs, pak je nech projít"
- "Oprav bug" → "Napiš test který ho reprodukuje, pak ho nech projít"
- "Refaktoruj X" → "Zajisti že testy projdou před i po"

Pro multi-step tasky, uveď brief plán:
```
1. [Krok] → verify: [check]
2. [Krok] → verify: [check]
3. [Krok] → verify: [check]
```

Silná success criteria = nezávislý loop. Slabá criteria ("ať to funguje") = nutnost neustálého upřesňování.

---

## APLIKACE NA ROSTOVY PROJEKTY

| Projekt | Jak aplikovat guidelines |
|---|---|
| UGC Engine / FastAPI | Žádné spekulativní agenty. Každý agent = jasné success criteria. |
| Python skripty (UCTENKAR) | Minimum kódu. Žádný error handling pro impossible cases. |
| n8n workflows | Surgical changes — neupravuj existující nody pokud není nutné. |
| Claude Code sessions | Think before coding — uveď assumptions před každou implementací. |

---

## ANTI-PATTERNS (co nedělat)

❌ Přidávat features "pro budoucnost" které nebyly požadovány  
❌ Mlčky vybírat mezi více interpretacemi  
❌ Refaktorovat okolní kód při opravě jednoho bugu  
❌ Psát 500 řádků abstrakce pro single-use logiku  
❌ Schovávat confusion a prostě "jet dál"  

---

## QUICK CHECK před každým commitem

1. Matchuje každý změněný řádek přímo uživatelskému requestu?
2. Bylo by to 50% kratší bez ztráty funkčnosti?
3. Jsou assumptions explicitně uvedeny?
4. Je success criteria jasná a verifikovatelná?

---

**Zdroje:**
- Repo: [github.com/forrestchang/andrej-karpathy-skills](https://github.com/forrestchang/andrej-karpathy-skills)
- Raw CLAUDE.md: [raw.githubusercontent.com/forrestchang/andrej-karpathy-skills/main/CLAUDE.md](https://raw.githubusercontent.com/forrestchang/andrej-karpathy-skills/main/CLAUDE.md)
- Autor: Jiayuan Zhang (forrestchang) — Founder @ Multica
