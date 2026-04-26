---
name: faceless-content-automation
description: >
  Strategie, taktiky a platform-specific pravidla pro automatizovanou produkci faceless video obsahu
  na YouTube, TikTok, Instagram a Facebook. Použij při práci na UGC Engine / Antigravity World,
  plánování content pipeline, nastavování multi-platform schedulingu, nebo definování content strategie
  pro velký fleet profilů. Obsahuje agnostické platform taktiky použitelné bez Syllaby —
  přímo integrovatelné do vlastního Python/FastAPI stacku.
  Trigger: faceless content, UGC pipeline, social media automatizace, video content scheduling.
---

# Faceless Content Automation

Odvozeno z: [cporter202/automate-faceless-content](https://github.com/cporter202/automate-faceless-content)  
Autor: Chris Porter (cporter202) — AI Automation Expert, ViralWaveStudio.com

> **Poznámka pro Rostu:** Původní repo je Syllaby.io marketing. Tento skill extrahuje
> **platform-agnostické taktiky** použitelné v UGC Engine bez jakékoliv SaaS závislosti.

---

## CORE PIPELINE

```
Niche/Topic → Script → Voiceover → Video → Thumbnail → Schedule → Publish → Analyze
```

Tvůj UGC Engine stack nahrazuje Syllaby na každém kroku:
- Script → Claude/GPT agent
- Voiceover → ElevenLabs / HeyGen
- Video → HeyGen / RunwayML / Sora
- Schedule → n8n / vlastní FastAPI scheduler
- Publish → Platform APIs (YouTube Data API, TikTok API, Meta Graph API)

---

## PLATFORM TAKTIKY (agnostické)

### YouTube
- **Formát:** Long-form 10-20 min + Shorts denně
- **Hook:** Prvních 3 sekundy = retention nebo smrt
- **Monetizace thresholdy:** 1,000 subscribers + 4,000 watch hours (YPP)
- **Upload timing:** Tue-Thu, 14:00-16:00 local time (peak discovery)
- **SEO:** Keyword v prvních 3 slovech titulku + v prvních 2 větách popisu
- **Shorts:** Max 60s, vertical 9:16, caption na celou délku

### TikTok
- **Optimal délka:** 7-15s (highest completion) nebo 60-90s (story format)
- **Hook:** Prvních 2 sekundy musí zodpovědět "proč bych měl dál sledovat?"
- **Posting:** 3-5x denně pro algoritmický boost v prvních 30 dnech profilu
- **Hashtags:** 3-5 relevantní (ne 30 generic)
- **Duet/Stitch:** Zvyšuje reach bez extra produkce

### Instagram Reels
- **Délka:** 15-30s pro maximum reach
- **Aspect ratio:** 9:16 (1080x1920)
- **Cover frame:** Klíčový — určuje CTR v grid
- **Timing:** 9:00-11:00 a 18:00-21:00 (vyšší engagement)
- **Stories:** 7-10 stories/den udržuje daily active status

### Facebook
- **Reels přes Facebook:** Nižší konkurence než TikTok/IG, rychlejší monetizace
- **In-stream ads:** Threshold 10,000 followers + 600,000 min watched
- **Optimal délka:** 3+ minuty pro in-stream ad eligibility

---

## NICHE STRATEGIE PRO FLEET PROFILŮ

Pro 20+ profilů (UGC Engine use case):

| Niche | CPM | Monetizace speed | Konkurence |
|---|---|---|---|
| Finance/Crypto | $15-40 | Pomalá (trust) | Vysoká |
| Tech/AI | $8-20 | Střední | Střední |
| Health/Wellness | $6-15 | Střední | Střední |
| Education | $4-10 | Rychlá | Nízká |
| Entertainment | $2-6 | Rychlá | Vysoká |

**Pro fleet:** Diverzifikuj niche mix. Ne všechny profily ve stejné niche = nižší risk.

---

## CONTENT TEMPLATES

### Hook Formula (Universal)
```
[Shocking stat / Question / Bold claim] + [Proof teaser] + [CTA to watch]
Příklad: "90% lidí dělá tuhle chybu na TikTok. Tady je proč přicházíš o reach."
```

### Script Structure (Short-form 60s)
```
0-3s:   Hook (proč sledovat)
3-15s:  Problem / Setup
15-45s: Value / Solution
45-55s: Proof / Example
55-60s: CTA (follow, like, comment)
```

### Script Structure (Long-form YouTube 10-20min)
```
0-30s:    Hook + Preview co dostaneš
30s-2min: Intro + credibility
2-8min:   Core content (3-5 main points)
8-15min:  Deep dive / Examples
15-18min: Recap
18-20min: CTA + Next video teaser
```

---

## SCHEDULING LOGIC PRO N8N / FASTAPI

```python
# Platform posting frequency doporučení
POSTING_SCHEDULE = {
    "youtube_long": {"per_week": 2-3, "times": ["14:00", "16:00"]},
    "youtube_shorts": {"per_day": 1-2, "times": ["09:00", "18:00"]},
    "tiktok": {"per_day": 3-5, "times": ["07:00", "12:00", "18:00", "21:00"]},
    "instagram_reels": {"per_day": 1-2, "times": ["09:00", "18:00"]},
    "instagram_stories": {"per_day": 7-10, "distributed": True},
    "facebook_reels": {"per_day": 1-2, "times": ["10:00", "19:00"]},
}

# Pro fleet 20+ profilů: staggered posting (ne všechny ve stejný čas)
# Interval: minimum 15 minut mezi profily na stejné platformě
```

---

## MONETIZACE STACK

### Přímá monetizace
- YouTube Partner Program → Ad revenue
- TikTok Creator Fund / TikTok Shop
- Facebook In-stream Ads
- Instagram Badges (live)

### Nepřímá monetizace (vyšší ROI)
- Affiliate marketing (Amazon, ClickBank, impact.com)
- Sponsored content (niche-specific brands)
- Digital products (kurzy, templates)
- Lead generation pro vlastní služby

### Pro UGC Engine fleet
- Prioritizuj affiliate + sponsored → nevyžaduje threshold jako ad revenue
- CPL (cost per lead) model je fastest path to revenue pro nové profily

---

## ANTI-PATTERNS

❌ Stejný obsah na všech platformách bez úpravy (každá platforma = jiný formát)  
❌ Posting bez hook v prvních 3 sekundách  
❌ Generic hashtags (#viral #fyp) bez niche-specific tagů  
❌ Ignorovat analytics — bez dat = blind posting  
❌ 100% AI generated voice bez quality check (detekce AI = penalizace dosahu)  

---

## INTEGRACE S UGC ENGINE

Chain pro tvůj stack:
```
Topic Agent → Script Agent → Voice (ElevenLabs) → Video (HeyGen) 
→ Thumbnail Agent → Metadata Agent → n8n Scheduler → Platform APIs
→ Analytics Agent → Feedback loop → Topic Agent
```

Každý krok = samostatný agent v FastAPI backendu.  
SQLite tracking: `content_id`, `platform`, `profile_id`, `status`, `posted_at`, `metrics`.

---

**Zdroje:**
- Repo: [github.com/cporter202/automate-faceless-content](https://github.com/cporter202/automate-faceless-content)
- Autor: [github.com/cporter202](https://github.com/cporter202)
- Syllaby.io (původní tool): [syllaby.io](https://syllaby.io)
- ViralWaveStudio: [viralwavestudio.com](https://viralwavestudio.com)
