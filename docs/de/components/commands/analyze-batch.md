---
title: analyze-batch
type: command
tags: []
lang: en
confidence: 100
---

# analyze-batch


## Overview

<div class="component-meta" markdown>
| Attribute | Value |
|-----------|-------|
| **Type** | Command |
| **Purpose** | Component description |
| **Complexity** | medium |
| **Model** | sonnet |
| **Category** | commands |</div>


## What It Does




## System Impact




## Architecture




## Usage


### Examples

#### Example



**Code:**
```bash
Lese: /Users/neoforce/Buisiness/Projects/Macro-Analyse/data/inbox/index.json

Filter: has_deep_analysis == false OR has_deep_analysis nicht vorhanden

Output:
- Liste der pending doc_ids
- Anzahl: X Dokumente warten auf Analyse
```


#### Example



**Code:**
```bash
1. Lese das Document:
   /Users/neoforce/Buisiness/Projects/Macro-Analyse/data/inbox/{file_path}

2. Analysiere mit WZRD Intelligence Prompt:

   === WZRD INTELLIGENCE ANALYSIS ===

   Analysiere diesen Artikel mit dem WZRD Framework:

   TITLE: {title}
   SOURCE: {source}
   CONTENT: {content}

   Antworte NUR mit diesem JSON (keine andere Ausgabe):
   {
     "msm_narrative": "Was will das Mainstream-Narrativ, dass ich glaube?",
     "reality_check": "Was ist wahrscheinlich wirklich los? (Folge dem Geld)",
     "signal_strength": 0.0-1.0,
     "narrative_contradiction_score": 0.0-1.0,
     "cui_bono": [{"who": "...", "how": "...", "confidence": 0.0-1.0}],
     "bullish_for": ["BTC", ...],
     "bearish_for": ["USD", ...],
     "hidden_connections": "Verborgene Zusammenhänge",
     "auto_tags": ["tag1", "tag2"],
     "wzrd_assessment": "1-2 Sätze Gesamtbewertung"
   }

3. Update Document File:
   - intelligence = parsed JSON
   - has_deep_analysis = true
   - signal_strength = aus analysis
   - narrative_gap = narrative_contradiction_score

4. Update Index Entry
```


#### Example



**Code:**
```bash
[X/N] Analysiert: {title}
      Signal: {signal_strength}% | Gap: {narrative_gap}%
      Tags: {auto_tags}
```


#### Example



**Code:**
```bash
Batch-Analyse abgeschlossen!

Analysiert: N Dokumente
- High Signal (>70%): X
- High Gap (>50%): Y
- Bullish Signals: Z
- Bearish Signals: W

Nächste Schritte:
- Dashboard unter http://localhost:3000 zeigt aktualisierte Daten
- /inbox/high-signal für kritische Artikel
```


#### Example



**Code:**
```bash
/analyze-batch              # Standard: bis zu 20
/analyze-batch 5            # Nur 5 analysieren
/analyze-batch --high-prio  # Nur actionable=true zuerst
```


#### Example



**Code:**
```bash
Index:     /Users/neoforce/Buisiness/Projects/Macro-Analyse/data/inbox/index.json
Documents: /Users/neoforce/Buisiness/Projects/Macro-Analyse/data/inbox/{category}/{doc_id}.json
```


#### Example



**Code:**
```bash
User: /analyze-batch

Claude:
  📊 Scanning inbox...
  Found: 50 documents pending analysis

  Analyzing batch of 20...

  [1/20] "Fed signals rate pause in 2025"
         Signal: 78% | Gap: 65% | Tags: fed, rates, policy

  [2/20] "Bitcoin ETF inflows reach $2B"
         Signal: 85% | Gap: 42% | Tags: btc, etf, institutional

  ...

  ✅ Batch complete!

  Summary:
  - Analyzed: 20 documents
  - High Signal (>70%): 8
  - High Gap (>50%): 5
  - Remaining: 30 documents

  Run /analyze-batch again for next batch.
```




## Configuration



## Best Practices




## Related



---

<small>Source: `.claude/commands/analyze-batch.md`</small>
