# Knowledge Management

Die Knowledge-Ebene von Evolving bietet persistentes Gedächtnis über Sessions hinweg, Decay-bewusste Experience-Abfrage, Entity-Graphen und intelligentes Context Routing.

---

## Domain Memory

### Was es macht

Verwaltet persistenten Projektzustand über Sessions hinweg, einschließlich Ziele, Progress-Verlauf und bekannte Fehler.

### Wie es funktioniert

```
Session Start
     │
     ▼
┌──────────────────────────┐
│ 1. Read _memory/index.json│
│    → active_project       │
└──────────┬───────────────┘
           │
           ▼
┌──────────────────────────┐
│ 2. Load Project Memory   │
│    _memory/projects/     │
│    {active}.json         │
│                          │
│    Contains:             │
│    • Goals               │
│    • Current State       │
│    • Progress History    │
│    • Known Failures      │
└──────────┬───────────────┘
           │
           ▼
┌──────────────────────────┐
│ 3. Orient & Announce     │
│    "Working on X"        │
│    "Last: Y"             │
│    "Next: Z"             │
└──────────────────────────┘
```

### Konfiguration

**Index-Speicherort**: `_memory/index.json`

```json
{
  "active_context": {
    "project": "evolving-system",
    "workflow": null
  },
  "recent_projects": [
    "evolving-system",
    "auswanderungs-ki-v2"
  ]
}
```

**Projekt-Speicherort**: `_memory/projects/{project}.json`

```json
{
  "name": "evolving-system",
  "goals": ["Self-improving AI system"],
  "state": {
    "current_phase": "Knowledge Management v3.3",
    "features": {
      "domain_memory": "passing",
      "experience_memory": "in_progress"
    }
  },
  "progress": [
    {
      "date": "2026-02-03",
      "action": "Created feature documentation",
      "result": "5 pages written",
      "next": "Review and deploy"
    }
  ],
  "failures": [
    {
      "date": "2026-02-01",
      "what": "Context overflow during review",
      "why": "Loaded all rules at once",
      "learned": "Use progressive loading"
    }
  ]
}
```

### Beispiel

```
Session 1:
  → Write: Feature X implemented
  → Memory: {"action": "Feature X", "result": "OK", "next": "Tests"}

Session 2 (next day):
  → Load Memory
  → Announce: "Last: Feature X. Next: Tests"
  → Continue seamlessly
```

**Relevant**: `.claude/rules/domain-memory-bootup.md`

---

## Experience Memory

### Was es macht

Speichert Lösungen, Patterns und Entscheidungen mit Decay-bewusster Relevanz-Bewertung und Vertrauensstufen.

### Wie es funktioniert

**Decay-Formel**:
```
effective_relevance = base_relevance × decay_factor × trust_level

decay_factor = 0.9^(days_since_created / 30)
trust_level = 1.0 (verified) | 0.7 (successful) | 0.3 (untested)
```

**Lebenszyklus**:
```
Solution Found
     │
     ▼
┌──────────────────────────┐
│ Create Experience        │
│ • base_relevance: 100    │
│ • trust_level: 0.3       │
│ • decay starts           │
└──────────┬───────────────┘
           │
      Time passes...
           │
           ▼
┌──────────────────────────┐
│ Decay Calculation        │
│                          │
│ Day 0:  100 × 1.0 × 0.3 = 30
│ Day 30: 100 × 0.9 × 0.3 = 27
│ Day 60: 100 × 0.8 × 0.3 = 24
│ Day 90: 100 × 0.7 × 0.3 = 21
└──────────┬───────────────┘
           │
   effective < 30?
           │
           ▼
      Archive/Delete
```

### Konfiguration

**Speicherort**: `_memory/experiences/*.json`

**Schema**:
```json
{
  "id": "exp_2026_02_03_001",
  "type": "solution",
  "summary": "Fixed context overflow with progressive loading",
  "content": "...",
  "tags": ["context", "optimization"],
  "projects": ["evolving-system"],
  "metadata": {
    "base_relevance": 100,
    "trust_level": 0.7,
    "valid_until": null,
    "verification_count": 1
  },
  "created": "2026-02-03T10:00:00Z"
}
```

### Beispiel

**Experience erstellen**:
```
User: "That solution worked great!"

System:
  → Extracts solution from conversation
  → Creates experience with trust_level: 0.7
  → Tags: ["auth", "security", "bug-fix"]
  → Stores in _memory/experiences/
```

**Experience abrufen**:
```
Session Start → Hydrate Pattern:
  → Query experiences WHERE project = active
  → Filter by effective_relevance > 30
  → Sort by effective_relevance DESC
  → Load Top 3

Result: Only relevant, recent, trusted experiences
```

**Relevant**: `_memory/experiences/SCHEMA.md`

---

## Knowledge Graph

### Was es macht

Modelliert Entities (Commands, Agents, Patterns, etc.) und ihre Beziehungen als verbundener Graph.

### Wie es funktioniert

```
┌─────────────┐
│   Nodes     │  150+ Entities
│             │
│ • Commands  │  e.g., "command:explore"
│ • Agents    │  e.g., "agent:debugger"
│ • Patterns  │  e.g., "pattern:delegation-request"
│ • Templates │  e.g., "template:agent"
│ • Rules     │  e.g., "rule:failure-recovery"
└──────┬──────┘
       │
       │ Connected by
       │
       ▼
┌─────────────┐
│   Edges     │  200+ Relationships
│             │
│ • uses      │  Command uses Agent
│ • extends   │  Pattern extends Pattern
│ • related   │  Rule related to Rule
│ • implements│  Agent implements Pattern
└─────────────┘
```

### Konfiguration

**Kern-Dateien**:
- `_graph/nodes.json` - Alle Entities
- `_graph/edges.json` - Alle Beziehungen
- `_graph/taxonomy.json` - Vereinigte Keywords

**Indizes** (auto-generiert):
- `_graph/index/by-type.json` - Gruppiert nach Entity-Typ
- `_graph/index/by-domain.json` - Gruppiert nach Domain
- `_graph/index/by-project.json` - Gruppiert nach Projekt

### Beispiel

**Abfrage**: "Zeige alle Agents die das Explore Pattern nutzen"

```javascript
// 1. Find pattern node
pattern = nodes.find(n => n.id === "pattern:explore")

// 2. Find edges TO pattern
edges = edges.filter(e => e.to === pattern.id && e.type === "uses")

// 3. Get agent nodes
agents = edges.map(e => nodes.find(n => n.id === e.from))

// Result: [agent:Explore, agent:code-explorer, ...]
```

**Visualisierung**:
```
agent:Explore
     │
     │ uses
     ▼
pattern:exploration
     │
     │ implements
     ▼
rule:explore-index-check
```

**Relevant**: `_graph/README.md`

---

## Context Router

### Was es macht

Mapped User-Keywords auf relevante Knowledge-Nodes und ermöglicht Just-in-Time Context-Laden.

### Wie es funktioniert

```
User Input: "I need to debug this"
     │
     ▼
┌──────────────────────────┐
│ 1. Extract Keywords      │
│    ["debug", "problem"]  │
└──────────┬───────────────┘
           │
           ▼
┌──────────────────────────┐
│ 2. Query Router          │
│    _graph/cache/         │
│    context-router.json   │
│                          │
│    Match: "debugging"    │
└──────────┬───────────────┘
           │
           ▼
┌──────────────────────────┐
│ 3. Load Primary Nodes    │
│                          │
│    • rule:observe-before-│
│      editing             │
│    • rule:failure-       │
│      recovery            │
│    • agent:debugger      │
└──────────┬───────────────┘
           │
           ▼
┌──────────────────────────┐
│ 4. Context Available     │
│    (Just-in-Time)        │
└──────────────────────────┘
```

### Konfiguration

**Speicherort**: `_graph/cache/context-router.json`

```json
{
  "routes": {
    "debugging": {
      "keywords": ["debug", "error", "fix", "problem"],
      "primary_nodes": [
        "rule:observe-before-editing",
        "rule:failure-recovery",
        "agent:debugger"
      ],
      "secondary_nodes": [
        "pattern:systematic-debugging",
        "rule:evidence-before-claims"
      ],
      "confidence_boost": 10
    }
  }
}
```

### Beispiel

**Ohne Router** (alter Weg):
```
Session Start → Load ALL rules → 34K tokens
```

**Mit Router** (optimiert):
```
Session Start → Load only core rules → 2K tokens
User: "debug this" → Router loads debug rules → +3K tokens
Total: 5K tokens (85% savings)
```

**Relevant**: `_graph/cache/context-router.json`

---

## Exploration Index

### Was es macht

Cached Findings von Explore Agents um redundante Explorationen zu vermeiden.

### Wie es funktioniert

```
User: "How does hook system work?"
     │
     ▼
┌──────────────────────────┐
│ 1. Check Index           │
│    knowledge/explorations│
│    /_index.json          │
│                          │
│    Keywords: ["hook",    │
│               "system"]  │
└──────────┬───────────────┘
           │
     Match found?
      /         \
    YES          NO
     │            │
     ▼            ▼
┌─────────┐  ┌─────────┐
│ Ask User│  │ Explore │
│ "Load   │  │ (new)   │
│  cached │  │         │
│  or re- │  │         │
│  explore?"│  │         │
└────┬────┘  └────┬────┘
     │            │
     │            ▼
     │       ┌─────────┐
     │       │ Cache   │
     │       │ Result  │
     │       └────┬────┘
     │            │
     └────────────┘
          │
          ▼
    Use Findings
```

### Konfiguration

**Index-Speicherort**: `knowledge/explorations/_index.json`

```json
{
  "entries": [
    {
      "id": "explore_2026_01_09_hooks",
      "date": "2026-01-09",
      "keywords": ["hook", "system", "subagent", "routing"],
      "summary": "Found 22 hooks in 4 categories",
      "file": "knowledge/explorations/2026-01-09-hook-system.md",
      "agent": "Explore",
      "model": "haiku"
    }
  ]
}
```

### Beispiel

**Erstes Mal**:
```
User: "Explain hook system"
  → No index entry
  → Explore Agent runs (costs tokens)
  → Findings cached in _index.json + .md file
```

**Zweites Mal**:
```
User: "How do hooks work again?"
  → Index match found (2026-01-09)
  → Ask: "Found cached exploration from Jan 9. Load or re-explore?"
  → User: "Load"
  → Read cached .md (much cheaper)
```

**Relevant**: `.claude/rules/explore-index-check.md`

---

## Session Handoffs

### Was es macht

Verbindet Sessions durch Dokumentation abgeschlossener Arbeit und offener Tasks für die nächste Session.

### Wie es funktioniert

```
Session Ending
     │
     ▼
┌──────────────────────────┐
│ 1. Handoff Creation      │
│    _handoffs/            │
│    YYYY-MM-DD-topic.md   │
│                          │
│    Contains:             │
│    • What was done       │
│    • What's pending      │
│    • Known blockers      │
│    • Next steps          │
└──────────┬───────────────┘
           │
           ▼
┌──────────────────────────┐
│ 2. Update Project Memory │
│    _memory/projects/     │
│    {active}.json         │
│                          │
│    Add progress entry    │
└──────────┬───────────────┘
           │
           ▼
      Session Ends

Next Session
     │
     ▼
┌──────────────────────────┐
│ 3. Bootup Reads Handoff  │
│    (most recent)         │
│                          │
│    Extracts open tasks   │
└──────────┬───────────────┘
           │
           ▼
┌──────────────────────────┐
│ 4. Continue Seamlessly   │
│    "Last session: X"     │
│    "Pending: Y, Z"       │
│    "Starting with Y..."  │
└──────────────────────────┘
```

### Konfiguration

**Speicherort**: `_handoffs/YYYY-MM-DD-topic.md`

**Template**:
```markdown
# Handoff: [Topic]

**Date**: YYYY-MM-DD
**Project**: {project-name}

## Completed
- Task A (commit: abc123)
- Task B (commit: def456)

## Pending
- [ ] Task C (blocked by: external API)
- [ ] Task D (ready to start)

## Blockers
- External API not responding (since 2026-02-02)

## Next Steps
1. Start with Task D (no blockers)
2. Monitor API for Task C
3. Consider fallback if API still down

## Context for Next Session
- Feature X is 80% complete
- Tests passing except integration test
- User wants deployment by Friday
```

### Beispiel

**Session 1 Ende**:
```
System creates handoff:
  → _handoffs/2026-02-03-feature-x.md
  → Documents completed tasks (A, B)
  → Lists pending tasks (C, D)
  → Notes blocker (API down)
```

**Session 2 Start**:
```
System reads handoff:
  → "Working on Feature X"
  → "Completed: A, B"
  → "Pending: C (blocked), D (ready)"
  → "Starting with D..."

→ Immediately continues work (no re-explanation needed)
```

**Relevant**: `knowledge/workflows/handoff-protocol.md`

---

## Zusammenfassung

Knowledge Management bietet:
- **Persistenter Zustand**: Domain Memory über Sessions
- **Intelligentes Abrufen**: Experience Memory mit Decay
- **Verbundene Entities**: Knowledge Graph mit 150+ Knoten
- **Just-in-Time Laden**: Context Router spart 85% Tokens
- **Gecachte Findings**: Exploration Index vermeidet Redundanz
- **Nahtlose Kontinuität**: Session Handoffs überbrücken Arbeit

**Ergebnis**: System merkt sich, lernt und wird mit der Zeit smarter.
