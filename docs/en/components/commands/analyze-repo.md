---
title: analyze-repo
type: command
tags: []
lang: en
confidence: 100
---

# analyze-repo


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

5-Phasen Repository-Analyse mit Rel-Extraktion + Tpl-Abstraktion


## System Impact




## Architecture




## Usage


### Examples

#### Example



**Code:**
```bash
P1: Relevanz-Check (Remote)
├── README.md via WebFetch
├── Struktur via GitHub Page
├── Relevanz-Score (0-10)
└── Output: RELEVANT / NICHT RELEVANT
     │
     ▼ (Wenn RELEVANT + User OK)
P2: Deep Dive (Local Clone)
├── git clone → /tmp/{repo}
├── Glob/Read/Grep auf echtem Code
├── Funktionssignaturen extrahieren
└── Mapping gegen Evolving
     │
     ▼
P3: REL-EXTRAKTION (Kernlogik!)
├── Rel? → .claude/*/external/{repo}/
├── Interessant? → .claude/templates/{tpl}.md
└── Irrelevant? → Skip-Notes
     │
     ▼
P4: Archivierung
└── /tmp/{repo} → _archive/repos/{date}-{name}/
     │
     ▼
P5: Integration
└── Findings → knowledge/, .claude/SYSTEM-MAP.md
```


#### Example



**Code:**
```python
# README + Struktur fetchen
readme = WebFetch(f"{raw_url}/README.md")
structure = WebFetch(github_url, prompt="Ordnerstruktur")
```


#### Example



**Code:**
```bash
Score < 4  → NICHT RELEVANT (Report + Ende)
Score 4-5  → GRENZWERTIG (User entscheiden lassen)
Score >= 6 → RELEVANT (Deep Dive anbieten)
```


#### Example



**Code:**
```markdown
## Phase 1: Relevanz-Check

| Metric | Value |
|--------|-------|
| Repo | {name} |
| Score | {X}/10 |
| Indikatoren | {liste} |

**Fazit**: {RELEVANT/NICHT RELEVANT}

{Wenn RELEVANT}:
Für Code-Level Analyse muss ich clonen.
Soll ich Deep Dive starten?
```


#### Example



**Code:**
```bash
git clone {url} /tmp/{repo-name}
```


#### Example



**Code:**
```bash
Grep "^(class |def |@dataclass)" **/*.py
Read pyproject.toml, requirements.txt
```


#### Example



**Code:**
```bash
Grep "^(export |interface |type )" **/*.ts
Read package.json
```


#### Example



**Code:**
```bash
Glob .claude/agents/*.md
Glob .claude/commands/*.md
Glob .claude/skills/*
```


#### Example



**Code:**
```markdown
---
tags: [memory, persistence, context-management]
---
# {Finding Title}
```


#### Example



**Code:**
```bash
Komponente gefunden
       │
       ▼
┌──────────────────┐
│ Für UNS nutzbar? │
└────────┬─────────┘
    Ja   │   Nein
    ▼    │    ▼
   EXT   │  ┌──────────────────┐
         │  │ Framework        │
         │  │ interessant?     │
         │  └────────┬─────────┘
         │      Ja   │   Nein
         │      ▼    │    ▼
         │    TPL    │  SKIP
```


#### Example



**Code:**
```bash
.claude/{type}/external/{repo}/
├── {komponente}.md          # Vollständiger Inhalt
└── _index.json              # Tags + Beschreibungen
```


#### Example



**Code:**
```json
{
  "source": "{github-url}",
  "extracted": "{date}",
  "components": [
    {
      "name": "{name}",
      "type": "agent|skill|command|hook",
      "tags": ["tag1", "tag2"],
      "status": "extracted|adapted|integrated"
    }
  ]
}
```


#### Example



**Code:**
```bash
.claude/templates/{abstrahierter-name}.md
```


#### Example



**Code:**
```bash
knowledge/learnings/{repo}-skip-notes.md
```


#### Example



**Code:**
```markdown
# {Repo} Skip Notes

| Komponente | Grund |
|------------|-------|
| discord-bot | Discord-spezifisch |
| aws-lambda | AWS, kein neues Framework |
```


#### Example



**Code:**
```markdown
## Phase 3: Rel-Extraktion

| Komponente | Entscheidung | Aktion |
|------------|--------------|--------|
| context-mgr-agent | EXT | → agents/external/{repo}/ |
| k8s-validator | TPL | → templates/validation-checklist.md |
| discord-bot | SKIP | → {repo}-skip-notes.md |

Extrahiert: {X} | Templates: {Y} | Skipped: {Z}
```


#### Example



**Code:**
```bash
EXT-Finding identifiziert
       │
       ▼
@compatibility-checker-agent invoken
       │
       ├─ Check 1: Tool-Mutex Konflikte
       ├─ Check 2: Naming-Kollisionen
       ├─ Check 3: Pattern-Overlap
       └─ Check 4: Sub-Agent Nutzung
           │
           ▼
       Severity?
       /    |    \
    🟢     🟡     🔴
   CLEAN FIXABLE NON-FIX
     │      │       │
     │   Warnung  Blocking
     │   + Fix?   + Optionen
     │      │       │
     └──────┴───────┘
             │
             ▼
       Weiter zu Phase 4
```


#### Example



**Code:**
```bash
@compatibility-checker-agent
{
  "finding": {
    "name": "{FINDING_NAME}",
    "type": "{agent|command|skill|hook}",
    "source_repo": "{REPO_URL}",
    "content": "{FINDING_CONTENT}",
    "extracted_tools": [...],
    "extracted_keywords": [...]
  }
}
```


#### Example



**Code:**
```bash
"✅ Kompatibilitäts-Check bestanden. Weiter mit Integration."
→ Automatisch zu Phase 4
```


#### Example



**Code:**
```bash
"⚠️ Warnungen gefunden:
1. Naming: Ähnlich zu 'X' → Auto-Fix: Rename zu 'Y'
2. Sub-Agent: Score 4/10 → Optimierung möglich

Soll ich Auto-Fixes anwenden? [y/N]"

→ Bei "y": Fixes anwenden, dann Phase 4
→ Bei "n": Warnung dokumentieren, Phase 4
```


#### Example



**Code:**
```bash
"❌ Kritischer Konflikt!

Tool-Mutex: puppeteer vs claude-in-chrome
Beide steuern Browser - können nicht koexistieren.

Optionen:
1. Finding ablehnen (nicht integrieren)
2. Als Template abstrahieren (nur Konzept)
3. Manuell lösen (eigene Anpassungen)

Wähle: [1/2/3]"

→ 1: Finding zu SKIP ändern
→ 2: Finding zu TPL ändern
→ 3: User löst manuell, dann Phase 4
```


#### Example



**Code:**
```bash
# Verschieben
mv /tmp/{repo-name} _archive/repos/{YYYY-MM-DD}-{repo-name}/

# Summary erstellen
Write _archive/repos/{date}-{repo-name}/_analysis.md
```


#### Example



**Code:**
```markdown
## Integration

Ich habe folgende Findings identifiziert:

| # | Finding | Type | Kategorie | Integrieren? |
|---|---------|------|-----------|--------------|
| 1 | {name} | template | 🟢 NEU | ☐ |
| 2 | {name} | pattern | 🟡 BESSER | ☐ |
| 3 | {name} | learning | 🔵 ANDERS | ☐ Evaluieren |

Welche soll ich integrieren? (Alle NEU / Alle NEU+BESSER / Spezifische / Keine)
```


#### Example



**Code:**
```bash
Read _stats.json
# Erhöhe den passenden Counter:
# - templates +1 bei type=template
# - patterns +1 bei type=pattern
# - learnings +1 bei type=learning
# - commands +1 bei type=command
# - agents +1 bei type=agent
Edit _stats.json → Counter erhöhen
```


#### Example



**Code:**
```bash
Read _graph/cache/context-router.json

# Option A: Bestehende Route erweitern (wenn Keywords 50%+ überlappen)
# → Finding zu "primary" Array hinzufügen
# → Neue Keywords zu "keywords" Array hinzufügen

# Option B: Neue Route erstellen
{
  "routes": {
    "{route-name}": {
      "keywords": ["{kw1}", "{kw2}", "{kw3}"],
      "primary": ["{type}-{name}"],
      "secondary": [],
      "context_files": ["{path-to-file}"]
    }
  }
}

Edit _graph/cache/context-router.json
```


#### Example



**Code:**
```bash
# Nur wenn type=command:
Read .claude/detection-index.json

# Neuen Command-Eintrag hinzufügen:
"/{command-name}": {
  "kw": ["{keyword1}", "{keyword2}"],
  "patterns": ["{pattern1}"],
  "anti": [],
  "conf": "high"
}

Edit .claude/detection-index.json
```


#### Example



**Code:**
```bash
Read _graph/knowledge-nodes.json

# Neuen Node hinzufügen:
{
  "id": "{type}-{name}",
  "type": "{template|pattern|learning|command|agent|rule}",
  "name": "{Display Name}",
  "path": "{relative/path/to/file.md}",
  "domain": ["{domain1}", "{domain2}"],
  "description": "{Kurzbeschreibung}"
}

# count erhöhen!
Edit _graph/knowledge-nodes.json
```


#### Example



**Code:**
```bash
Read _graph/edges.json

# Edges zu verwandten Nodes hinzufügen:
{
  "source": "{type}-{name}",
  "target": "{related-node-id}",
  "relation": "related_to",
  "weight": 1,
  "created": "{YYYY-MM-DD}"
}

# Finde verwandte Nodes über:
# - Gleiche Tags/Domains
# - Gleicher Typ
# - Thematische Nähe

# count erhöhen!
Edit _graph/edges.json
```


#### Example



**Code:**
```bash
Read .claude/SYSTEM-MAP.md

# Je nach Typ:
# - Command → Commands-Tabelle erweitern
# - Agent → Agents-Tabelle erweitern
# - Template → Templates-Tabelle erweitern
# - Pattern/Learning → Changelog-Eintrag

# Changelog am Ende hinzufügen:
| {date} | {finding} from {repo} | {path} | integrated |

Edit .claude/SYSTEM-MAP.md
```


#### Example



**Code:**
```bash
# Nur wenn type in [template, pattern, learning, prompt]:
Read knowledge/index.md

# Link zum neuen File hinzufügen in passender Sektion:
# - Templates → ### 📐 Templates
# - Patterns → ### 🔧 Patterns
# - Learnings → ### 📖 Learnings

Edit knowledge/index.md
```


#### Example



**Code:**
```markdown
## Integration Verifikation für: {name}

| Schritt | Datei | Status |
|---------|-------|--------|
| 1 | _stats.json | ☐ Count erhöht |
| 2 | context-router.json | ☐ Route vorhanden |
| 3 | detection-index.json | ☐ (nur Commands) |
| 4 | knowledge-nodes.json | ☐ Node existiert |
| 5 | edges.json | ☐ Edges erstellt |
| 6 | SYSTEM-MAP.md | ☐ Tabelle/Changelog |
| 7 | knowledge/index.md | ☐ (nur KB-Types) |

Alle ☑? → Commit erstellen
```


#### Example



**Code:**
```bash
git add _stats.json _graph/ .claude/SYSTEM-MAP.md knowledge/index.md
# + weitere geänderte Dateien

git commit -m "$(cat <<'EOF'
integrate: {name} from {repo}

- Added {type} to system
- Context Router: {route-name} route
- Graph: +1 node, +{n} edges
- Stats: {type}s now at {new-count}

Co-Authored-By: Claude Opus 4.5 <noreply@anthropic.com>
EOF
)"
```


#### Example



**Code:**
```markdown
## ✅ Integration Complete: {name}

| Registrierung | Status | Details |
|---------------|--------|---------|
| _stats.json | ✅ | {type}s: {old} → {new} |
| Context Router | ✅ | Route: {route-name} |
| Detection Index | ✅/⏭️ | {status} |
| Knowledge Node | ✅ | ID: {type}-{name} |
| Graph Edges | ✅ | +{n} edges |
| SYSTEM-MAP | ✅ | Changelog updated |
| knowledge/index | ✅/⏭️ | {status} |

**Commit**: `integrate: {name} from {repo}`

Das Finding ist jetzt vollständig ins System integriert und über
Keywords "{kw1}, {kw2}" im Context Router findbar.
```


#### Example



**Code:**
```markdown
# {Repo} Analysis

**Datum**: {date}
**URL**: {url}
**Score**: {X}/10

## Extrahierte Patterns

| Pattern | Code | Integration |
|---------|------|-------------|
| {name} | `{signature}` | patterns/{file} |

## Integration Status

| Finding | Integriert | Location |
|---------|------------|----------|
| {name} | ✓/✗ | {path} |

## Quick Access

`cd _archive/repos/{date}-{name}/`
```


#### Example



**Code:**
```markdown
# {REPO_NAME} Deep Dive

## Summary

| Metric | Value |
|--------|-------|
| Score | {X}/10 |
| Tech Stack | {stack} |
| Code Files | {count} |
| Extrahierte Patterns | {count} |

## 🟢 NEU (Code-Level)

### Pattern: {name}
**Datei**: `{path}`
**Code**:
```


#### Example



**Code:**
```bash
**Integration**: → knowledge/patterns/{name}.md
**Tags**: {auto-tags}

## 🟡 BESSER (vs. unsere Version)

| Finding | Unser Code | Ihr Code | Verbesserung |
|---------|-----------|----------|--------------|
| {name} | {ours} | {theirs} | {improvement} |

## 🔵 ANDERS

{alternative approaches}

## Archiv

Repo archiviert: `_archive/repos/{date}-{name}/`
Für Details: Dort reinschauen.

## SYSTEM-MAP Update

| Datum | Finding | Integration | Status |
|-------|---------|-------------|--------|
| {date} | {finding} | {location} | Pending |
```


#### Example



**Code:**
```bash
User: "Schau dir mal https://github.com/some/claude-tools an"

Claude:
## Phase 1: Relevanz-Check

| Metric | Value |
|--------|-------|
| Repo | claude-tools |
| Score | 8/10 |
| Indikatoren | .claude/ ✓, MCP ✓, Hooks ✓ |

**Fazit**: RELEVANT

Für Code-Level Analyse muss ich clonen.
Deep Dive starten?

User: Ja

Claude:
Cloning...
Analysiere Code...
Extrahiere Patterns...

[Deep Dive Report mit Code-Level Details]

✓ Archiviert: _archive/repos/2025-12-27-claude-tools/
```


#### Example



**Code:**
```bash
⚠ Konnte docs/architecture.md nicht lesen (404)

Das könnte relevante Patterns enthalten.
Alternativen:
1. Lokal clonen und dann lesen
2. Ähnliche Dateien suchen (docs/*.md)
3. Überspringen (mit Vermerk im Report)

Wie soll ich vorgehen?
```


#### Example



**Code:**
```markdown
## Nicht gelesene Dateien

| Datei | Grund | Potentielle Relevanz |
|-------|-------|---------------------|
| docs/architecture.md | 404 | Hoch (Architecture Patterns) |
| src/internal/ | Private | Mittel |
```


#### Example



**Code:**
```bash
❌ Repo nicht erreichbar

Optionen:
1. Lokal klonen: git clone {url}
2. Dann: "Analysiere /path/to/repo"
```


#### Example



**Code:**
```bash
Score: 2/10

Keine Claude Code Relevanz erkannt.
Analyse beenden.
```


#### Example



**Code:**
```bash
⚠ {datei} nicht lesbar

Nicht überspringen! Alternativen versuchen oder User fragen.
```




## Configuration



## Best Practices




## Related



---

<small>Source: `.claude/commands/analyze-repo.md`</small>
