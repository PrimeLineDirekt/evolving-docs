---
title: domain-memory-bootup
type: rule
tags: []
lang: en
confidence: 100
---

# domain-memory-bootup


## Overview

<div class="component-meta" markdown>
| Attribute | Value |
|-----------|-------|
| **Type** | Rule |
| **Purpose** | Component description |
| **Complexity** | medium |
| **Model** | sonnet |
| **Category** | rules |</div>


## What It Does




## System Impact




## Architecture




## Usage


### Examples

#### Example



**Code:**
```bash
Lies in dieser Reihenfolge:

1. _memory/index.json
   → Welches Projekt ist aktiv?
   → Welcher Workflow läuft?

2. _memory/projects/{active}.json
   → Goals & Features
   → Current State
   → Recent Progress
   → Known Failures

3. _memory/workflows/active.json (falls vorhanden)
   → Current Step
   → Checklist Status
```


#### Example



**Code:**
```bash
"Ich sehe wir arbeiten an [Projekt].
 Letzter Stand: [Progress].
 Nächster Schritt wäre: [Next].
 Soll ich damit weitermachen?"
```


#### Example



**Code:**
```bash
Lies _memory/system-updates.json
    │
    ├─ last_check < 7 Tage? → Skip, weiter mit Task
    │
    └─ last_check >= 7 Tage?
        │
        ▼
    KURZER Check (max 2K Tokens):
    - WebSearch: "Claude Code changelog 2026"
    - Diff gegen known_features
    - Neue Features? → Learning erstellen
    - Timestamp aktualisieren
        │
        ▼
    Kurze Info an User:
    "ℹ️ Update-Check: [X neue Features gefunden / Alles aktuell]"
```


#### Example



**Code:**
```bash
User sagt "continue" (oder Variante)
    │
    ▼
1. HANDOFF LADEN
   ls -t _handoffs/*.md | head -1
   → Neuesten Handoff lesen
   → Offene Punkte extrahieren
    │
    ▼
2. PLAN LADEN (falls referenziert)
   → Plan-Datei aus Handoff lesen
   → Offene Phasen/Tasks identifizieren
    │
    ▼
3. SOFORT WEITERMACHEN
   → Keine Rückfragen
   → Ersten offenen Task starten
   → TodoWrite mit offenen Tasks
```


#### Example



**Code:**
```bash
User: "continue"

Claude:
  [Liest _handoffs/2026-01-03-v3.3.0-intelligence-system.md]
  [Liest Plan falls vorhanden]

  "Fortsetze v3.3.0 Plan. Offene Punkte:
   - Blueprints Index aktualisieren
   - Broken References fixen
   - domain-memory-bootup erweitern

   Starte mit Blueprints Index..."

  [Beginnt sofort mit Arbeit]
```


#### Example



**Code:**
```bash
User sagt "resume mcp-phase-4" (oder /resume mcp-phase-4)
    │
    ▼
1. NAMED SESSION SUCHEN
   Lies _memory/sessions/index.json
   → Finde Session mit name = "mcp-phase-4"
   → Extrahiere handoff_file + project
    │
    ▼
2. SESSION LADEN
   Falls handoff_file existiert:
   → Handoff lesen
   → Offene Punkte extrahieren
   Falls nicht:
   → Projekt-Memory laden (_memory/projects/{project}.json)
    │
    ▼
3. CONTEXT WIEDERHERSTELLEN
   → Projekt aktivieren (falls anders als aktuell)
   → last_accessed in Session updaten
   → SOFORT mit Arbeit beginnen
```


#### Example



**Code:**
```bash
User: "resume mcp-phase-4"

Claude:
  [Liest _memory/sessions/index.json]
  [Findet: {name: "mcp-phase-4", handoff: "_handoffs/2026-01-08-mcp-phase-4.md"}]
  [Liest Handoff]

  "Fortsetze Session 'mcp-phase-4'. Offene Punkte:
   - Tests für neue Tools
   - Dokumentation aktualisieren

   Starte mit Tests..."

  [Beginnt sofort mit Arbeit]
```


#### Example



**Code:**
```bash
User: "/rename mcp-phase-4"

Claude:
  → Speichert in _memory/sessions/index.json:
    {
      "name": "mcp-phase-4",
      "created": "2026-01-08T14:30:00Z",
      "last_accessed": "2026-01-08T14:30:00Z",
      "project": "evolving-system",
      "handoff_file": "_handoffs/2026-01-08-mcp-phase-4.md",
      "status": "paused"
    }
  → Bestätigt: "Session als 'mcp-phase-4' gespeichert. Später mit /resume mcp-phase-4 fortsetzen."
```


#### Example



**Code:**
```json
{
  "date": "YYYY-MM-DD",
  "action": "Was wurde getan",
  "result": "Ergebnis",
  "next": "Vorgeschlagener nächster Schritt"
}
```


#### Example



**Code:**
```json
{
  "date": "YYYY-MM-DD",
  "what": "Was ging schief",
  "why": "Root Cause",
  "learned": "Lesson Learned"
}
```


#### Example



**Code:**
```bash
_memory/
├── index.json              # Aktiver Context
├── projects/
│   ├── evolving-system.json
│   ├── auswanderungs-ki-v2.json
│   └── thrive-vibes-art.json
├── workflows/
│   └── active.json         # Laufender Workflow
└── sessions/
    └── context.json        # Session-spezifisch
```


#### Example



**Code:**
```bash
_graph/
├── nodes.json              # Alle Entities (~150)
├── edges.json              # Beziehungen (~200)
├── taxonomy.json           # Unified Keywords
├── index/
│   ├── by-type.json        # Nach Entity-Typ
│   ├── by-domain.json      # Nach Domain/Tag
│   └── by-project.json     # Nach Projekt
└── cache/
    └── context-router.json # Keyword → Nodes
```


#### Example



**Code:**
```bash
[Session Start]

Claude liest _memory/index.json:
  → active_context.project = "evolving-system"

Claude liest _memory/projects/evolving-system.json:
  → current_phase = "Domain Memory Implementation"
  → last_progress = "Schema erstellt"
  → next = "Workflows anpassen"

Claude sagt:
  "Wir arbeiten am Evolving System.
   Letzter Stand: Domain Memory Schema erstellt.
   Features: 6/8 passing, Domain Memory in_progress.
   Nächster Schritt: Workflows für Memory-Integration anpassen.
   Soll ich damit weitermachen?"
```


#### Example



**Code:**
```bash
HYDRATE bei Session-Start:
                    ┌─────────────┐
                    │   Session   │
                    │    Start    │
                    └──────┬──────┘
                           │
           ┌───────────────┼───────────────┐
           ▼               ▼               ▼
    ┌─────────────┐ ┌─────────────┐ ┌─────────────┐
    │   DOMAIN    │ │ EXPERIENCE  │ │    GRAPH    │
    │   MEMORY    │ │   MEMORY    │ │   CONTEXT   │
    └──────┬──────┘ └──────┬──────┘ └──────┬──────┘
           │               │               │
           ▼               ▼               ▼
    _memory/index    Decay-Filtered    context-router
    + project.json   Experiences       Primary Nodes
           │               │               │
           └───────────────┼───────────────┘
                           ▼
                  ┌─────────────────┐
                  │  MERGED CONTEXT │
                  │  für Session    │
                  └─────────────────┘
```


#### Example



**Code:**
```bash
effective_relevance = base * decay_factor * trust_level
WHERE effective_relevance > 30
  AND (valid_until IS NULL OR valid_until > NOW())
```


#### Example



**Code:**
```bash
1. PARALLEL HYDRATE (Single-Call-Konzept):
   │
   ├─ _memory/index.json
   │   └─ Extrahiere: active_project, active_workflow
   │
   ├─ _memory/projects/{active}.json
   │   └─ Extrahiere: goals, state, progress, failures
   │
   ├─ _memory/experiences/ (decay-filtered)
   │   └─ Relevante Solutions, Patterns, Decisions
   │   └─ Filter: project-match OR high-relevance
   │
   └─ _graph/cache/context-router.json
       └─ Extrahiere: Routes für aktiven Projekt-Domain

2. MERGE & PRIORITIZE:
   │
   ├─ Domain Memory → Höchste Priorität (aktueller State)
   ├─ Recent Failures → Warnung bei bekannten Issues
   ├─ High-Trust Experiences → Relevante Lösungen
   └─ Graph Nodes → Verfügbare Patterns/Templates

3. ANNOUNCE (wie gehabt):
   "Projekt: {name} | Phase: {phase}
    Letzter Stand: {progress}
    Bekannte Issues: {failures count}
    Relevante Erfahrungen: {experiences count}
    Nächster Schritt: {next}"
```


#### Example



**Code:**
```bash
User-Input empfangen
         │
         ▼
┌────────────────────────┐
│ 1. KEYWORDS EXTRAHIEREN │
│    (aus User-Anfrage)   │
└──────────┬─────────────┘
           │
           ▼
┌────────────────────────────────┐
│ 2. COMMAND-DETECTION           │
│    .claude/detection-index.json │
│    → Match? Confidence?         │
└──────────┬─────────────────────┘
           │
           ▼
┌────────────────────────────────┐
│ 3. CONTEXT-ROUTER MATCH        │
│    _graph/cache/context-router  │
│    → Relevante Patterns/Rules   │
└──────────┬─────────────────────┘
           │
           ▼
┌────────────────────────────────┐
│ 4. SUMMARY-LAYER CHECK         │
│    .claude/summaries/{type}/    │
│    → Kompakte JSON statt MD     │
└──────────┬─────────────────────┘
           │
           ▼
      CONFIDENCE?
      /    |    \
    HIGH  MED   LOW
     │     │     │
     ▼     ▼     ▼
   LOAD  FRAGEN  SKIP
           │
           ▼
┌────────────────────────────────┐
│ 5. DELEGATION CHECK            │
│    (siehe auto-delegation.md)  │
│                                │
│    Task delegierbar?           │
│    → Agent Selection           │
│    → Model Selection           │
│    → Execute oder selbst       │
└────────────────────────────────┘
```


#### Example



**Code:**
```json
{
  "match_type": "exact|fuzzy|fallback",
  "confidence": 85,
  "primary_route": "debugging",
  "secondary_routes": [{"route": "testing", "conf": 45}],
  "load_items": {
    "patterns": ["systematic-debugging"],
    "rules": ["observe-before-editing"],
    "commands": ["/debug"]
  },
  "suggested_command": "/debug",
  "full_docs_needed": false
}
```


#### Example



**Code:**
```bash
Bei HIGH Confidence:
1. Lies .claude/summaries/{type}/{name}.json (300 Tokens)
2. Verstehe key_points, when_to_use, related
3. NUR bei Bedarf: Volle MD laden (3000 Tokens)

Effekt: ~90% Token-Ersparnis durch Summary-Layer
```


#### Example



**Code:**
```bash
IF no_route_match OR confidence < 50:
   │
   ├─ Fallback 1: detection-index.json Keywords prüfen
   │   → Vielleicht Command-Match ohne Route?
   │
   ├─ Fallback 2: User fragen
   │   "Ich bin nicht sicher was du meinst.
   │    Meinst du X, Y, oder Z?"
   │
   └─ Max-Depth: 1
       → KEIN rekursives Fallback!
       → Lieber fragen als raten
```


#### Example



**Code:**
```bash
Context < 60%?
     │
     ├─ NEIN → Skip Spaced Rep
     │
     └─ JA
         │
         ▼
┌────────────────────────────────┐
│ 1. COLLECTOR AUFRUFEN          │
│    scripts/spaced-rep-collector│
│    .py                         │
└──────────┬─────────────────────┘
           │
           ▼
┌────────────────────────────────┐
│ 2. DUE ITEMS PRÄSENTIEREN      │
│                                │
│ "📚 Review-Check (3 fällig):   │
│  1. [EXP] Supabase RLS         │
│  2. [RULE] Advanced Debug      │
│  3. [EXPLORE] Hook-System"     │
│                                │
│ [C]onfirm / [S]kip / Details   │
└──────────┬─────────────────────┘
           │
           ▼
┌────────────────────────────────┐
│ 3. INTERVALLE AKTUALISIEREN    │
│                                │
│ confirm → interval *= 2.5      │
│ skip → interval *= 0.8         │
└────────────────────────────────┘
```


#### Example



**Code:**
```bash
Session-Start
     │
     ▼
┌────────────────────────────────┐
│ 1. STAGING-INDEX LADEN         │
│    knowledge/rules/staging/    │
│    _index.json                 │
└──────────┬─────────────────────┘
           │
           ▼
┌────────────────────────────────┐
│ 2. TRIAL-RULES IDENTIFIZIEREN  │
│                                │
│ Für jede Rule mit status:      │
│ "trial" → laden und tracken    │
└──────────┬─────────────────────┘
           │
           ▼
┌────────────────────────────────┐
│ 3. PASSIVE TRACKING            │
│                                │
│ Bei User-Input Keywords match: │
│ → applied_count++              │
│ → applied_sessions[]           │
│                                │
│ Bei Erfolg (kein Rollback):    │
│ → success_count++              │
└──────────┬─────────────────────┘
           │
           ▼
┌────────────────────────────────┐
│ 4. PROMOTION CHECK             │
│                                │
│ IF success_count >= 3          │
│    AND no corrections:         │
│    → Status: trial → stable    │
│    → Move to production        │
└────────────────────────────────┘
```


#### Example



**Code:**
```bash
candidate (inactive)
     │
     ├─ Manual: User sagt "teste diese Rule"
     │  OR Auto: Learning mit high confidence
     │
     ▼
trial (loaded bei Session-Start)
     │
     ├─ Nach jeder Session:
     │  • success_count++ wenn keine Korrektur
     │  • applied_count++ wenn Keywords gematcht
     │
     ├─ IF success_count >= 3:
     │  → Status: stable
     │
     ├─ IF corrections > 2:
     │  → Status: candidate (zurück)
     │  → Reason geloggt
     │
     ▼
stable (Production)
     │
     └─ Move nach knowledge/rules/{category}/
        (kein Staging mehr)
```


#### Example



**Code:**
```bash
Domain Memory Bootup
         │
         ▼
    HYDRATE Memory
         │
         ▼
    Context-Scout
         │
         ▼
┌─────────────────────────────────┐
│ STAGED RULES VALIDATION         │
│                                 │
│ 1. Lies staging/_index.json    │
│ 2. Lade trial-Rules             │
│ 3. Track intern (nicht explizit)│
└──────────┬──────────────────────┘
           │
           ▼
    Task-Arbeit beginnen
```


#### Example



**Code:**
```bash
User-Input: "Ich muss das debuggen"
     │
     ▼
Keywords: ["debug", "problem"]
     │
     ▼
staging/_index.json prüfen:
  → Rule "advanced-debugging-v2" (trial)
  → Keywords: ["debug", "systematic", "evidence"]
     │
     ▼
Match gefunden!
  → Rule laden (silent, kein User-Feedback)
  → applied_count++
  → applied_sessions.append("2026-02-01")
     │
     ▼
Task wird ausgeführt...
     │
     ├─ User korrigiert nichts? → success_count++
     │
     └─ User korrigiert? → Tracking ohne success++
```


#### Example



**Code:**
```bash
Session-Ende
     │
     ▼
Für jede trial-Rule prüfen:
     │
     ├─ success_count >= 3?
     │  AND no_corrections?
     │  → PROMOTE zu stable
     │  → Move File zu knowledge/rules/{category}/
     │  → Update _index.json
     │
     ├─ corrections > 2?
     │  → DEMOTE zu candidate
     │  → Log reason
     │
     └─ Sonst: Status bleibt trial
```


#### Example



**Code:**
```json
{
  "rules": [
    {
      "id": "advanced-debugging-v2",
      "status": "trial",
      "keywords": ["debug", "systematic", "evidence"],
      "applied_count": 5,
      "success_count": 3,
      "corrections": 0,
      "applied_sessions": ["2026-01-28", "2026-01-29", "2026-02-01"],
      "last_applied": "2026-02-01T14:30:00Z",
      "created": "2026-01-15T10:00:00Z"
    }
  ]
}
```


#### Example



**Code:**
```bash
HYDRATE mit Budget-Awareness:

1. ESTIMATE Session-Komplexität:
   - Einfacher Task → Budget: 50K tokens
   - Komplexer Task → Budget: 100K tokens
   - Multi-Step → Budget: 150K tokens

2. BUDGET für Memory reservieren:
   - Domain Memory: max 5K tokens (kompakt halten!)
   - Experiences: max 3K tokens (nur Top-3 relevant)
   - Graph Context: max 2K tokens (Primary Nodes only)
   - REST für Task-Arbeit!

3. Bei BUDGET-Überschreitung:
   - Nur NEUESTE Failures laden (nicht alle)
   - Experiences auf Top-1 reduzieren
   - Graph-Kontext skippen
```


#### Example



**Code:**
```json
// SCHLECHT (zu lang):
{"date": "2025-12-27", "action": "Ich habe das Feature X implementiert mit den folgenden Schritten...", "result": "Das Feature funktioniert jetzt komplett..."}

// GUT (kompakt):
{"d": "12-27", "a": "Feature X impl", "r": "OK", "n": "Tests"}
```


#### Example



**Code:**
```bash
// SCHLECHT: Alle 50 Experiences laden
// GUT: Top-3 nach effective_relevance, projekt-gefiltert
```


#### Example



**Code:**
```bash
Session 1                     Session 2
─────────────────────────────────────────────────
┌─────────────┐               ┌─────────────┐
│ Task 1 ✅   │               │ (leer oder  │
│ Task 2 ✅   │  ──Sync──►    │  persistent │
│ Task 3 🔄   │               │  via ID)    │
└─────────────┘               └─────────────┘
       │
       ▼
┌─────────────┐
│ Memory      │  ◄── Completed Tasks werden
│ Progress    │      zu Memory-Entries
└─────────────┘
```


#### Example



**Code:**
```bash
1. TaskList abrufen
2. Completed Tasks extrahieren
3. Progress-Entry generieren:
   {
     "date": "YYYY-MM-DD",
     "action": "Session completed",
     "tasks_done": ["Task 1", "Task 2"],
     "result": "Summary",
     "next": "Offene Tasks"
   }
4. In _memory/projects/{active}.json schreiben
5. Optional: Tasks löschen wenn sync complete
```


#### Example



**Code:**
```bash
TaskList lesen
    │
    ├─ Keine Tasks? → Normal fortfahren
    │
    └─ Tasks vorhanden?
        │
        ├─ Completed Tasks → Zu Memory syncen, dann löschen
        │
        └─ Offene Tasks → User fragen:
           "Es gibt offene Tasks von letzter Session:
            - Task A (in_progress)
            - Task B (pending)
            Fortsetzen oder verwerfen?"
```




## Configuration



## Best Practices




## Related



---

<small>Source: `.claude/rules/domain-memory-bootup.md`</small>
