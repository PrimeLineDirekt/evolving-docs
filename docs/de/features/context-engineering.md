# Context Engineering

Evolving optimiert Context Window Nutzung durch Progressive Loading, Summary Layers, Budget-Bewusstsein und strategische Memory Patterns.

---

## Progressive Loading

### Was es macht

Lädt Knowledge in drei Stufen (JSON Config → Summary → Volle Docs) basierend auf Bedarf und verhindert Context-Bloat.

### Wie es funktioniert

```
User Request
     │
     ▼
┌──────────────────────────┐
│ Layer 1: JSON Config     │
│ (~500 tokens)            │
│                          │
│ • task-types.json        │
│ • pattern-mutex.json     │
│ • orchestration-config   │
│                          │
│ → Enables detection      │
└──────────┬───────────────┘
           │
     Match found?
           │
           ▼
┌──────────────────────────┐
│ Layer 2: Summary         │
│ (~300 tokens)            │
│                          │
│ .claude/summaries/       │
│ {type}/{name}.json       │
│                          │
│ • core_loop              │
│ • when_to_use            │
│ • config                 │
│                          │
│ → Apply pattern          │
└──────────┬───────────────┘
           │
     Need details?
           │
           ▼
┌──────────────────────────┐
│ Layer 3: Full Markdown   │
│ (~3000 tokens)           │
│                          │
│ knowledge/patterns/      │
│ {name}-pattern.md        │
│                          │
│ • Full documentation     │
│ • Edge cases             │
│ • Examples               │
└──────────────────────────┘
```

### Konfiguration

**Layer 1 Speicherort**: `_graph/cache/task-types.json`
```json
{
  "task_types": {
    "debugging": {
      "keywords": ["debug", "error", "fix"],
      "confidence_boost": 10,
      "recommended_pattern": "systematic-debugging"
    }
  }
}
```

**Layer 2 Speicherort**: `.claude/summaries/patterns/systematic-debugging.json`
```json
{
  "name": "Systematic Debugging",
  "core_loop": "Observe → Diagnose → Fix → Verify",
  "when_to_use": "Bug reports, test failures, unexpected behavior",
  "when_not": "Feature requests, known issues",
  "key_points": [
    "Never edit without diagnostics",
    "Evidence before claims",
    "Re-verify after each fix"
  ]
}
```

**Layer 3 Speicherort**: `knowledge/patterns/systematic-debugging-pattern.md`

### Beispiel

**Ohne Progressive Loading**:
```
Session Start:
  → Load ALL patterns → 30K tokens
  → Load ALL rules → 25K tokens
  → Total: 55K tokens used
  → Available for work: 145K tokens
```

**Mit Progressive Loading**:
```
Session Start:
  → Load configs → 2K tokens

User: "debug this error"
  → Load debug summary → 300 tokens
  → Apply pattern
  → Total: 2.3K tokens used
  → Available for work: 197.7K tokens
```

**Ersparnis**: 96% Reduktion in Startup-Kosten

**Relevant**: `.claude/rules/metacognitive-orchestrator.md`

---

## Summary Layer

### Was es macht

Bietet kompakte JSON-Zusammenfassungen von Markdown-Docs und ermöglicht schnelles Verständnis ohne volle Inhalte zu laden.

### Wie es funktioniert

```
Full Markdown (3000 tokens)
     │
     │ Summarized to
     ▼
JSON Summary (300 tokens)
     │
     │ Contains
     ▼
┌──────────────────────────┐
│ Key Information:         │
│                          │
│ • Core concept (1-2 lines)│
│ • When to use            │
│ • When NOT to use        │
│ • Config needed          │
│ • Related items          │
│                          │
│ → 90% of cases covered   │
└──────────────────────────┘
```

### Konfiguration

**Summary Struktur**:
```json
{
  "id": "pattern:delegation-request",
  "type": "pattern",
  "name": "Delegation Request Pattern",
  "summary": "Layer 2 agents request delegation back to Layer 1",
  "core_loop": "Sub-agent → JSON Request → Layer 1 executes",
  "when_to_use": "Complex tasks discovered during delegation",
  "when_not": "Simple tasks, Layer 1 already",
  "key_points": [
    "Sub-agents have no Task Tool",
    "Return structured JSON",
    "Layer 1 creates & executes tasks"
  ],
  "config": {
    "location": null,
    "required_fields": ["delegation_request", "recommended_tasks"]
  },
  "related": [
    "rule:delegation",
    "rule:swarm-orchestration"
  ],
  "token_estimate": {
    "summary": 300,
    "full_doc": 2800
  }
}
```

### Beispiel

**Abfrage**: "Wie funktioniert Delegation Request?"

**Ohne Summary**:
```
→ Load full MD (2800 tokens)
→ Parse entire document
→ Extract relevant parts
→ Answer question
```

**Mit Summary**:
```
→ Load summary (300 tokens)
→ Read core_loop: "Sub-agent → JSON → Layer 1"
→ Read when_to_use
→ Answer question (10x faster)
```

**Nachfrage**: "Zeig mir Implementation Details"
```
→ NOW load full MD (2800 tokens)
→ Deep dive into specifics
```

**Relevant**: `.claude/summaries/README.md`

---

## Budget Awareness

### Was es macht

Überwacht Context-Nutzung und verhindert Degradation durch Verhalten-Anpassung bei definierten Schwellwerten.

### Wie es funktioniert

**Modell-spezifische Degradationspunkte**:

| Model | Degradation startet | Schwere Degradation |
|-------|-------------------|-------------------|
| Opus 4.5 | ~100K tokens | ~180K tokens |
| Sonnet 4.5 | ~80K tokens | ~150K tokens |

**Threshold-Aktionen**:
```
Context Usage
     │
     ▼
┌──────────────────────────┐
│ < 70% (~140K)            │
│ → Normal operation       │
│ → Full progressive load  │
└──────────┬───────────────┘
           │
           ▼
┌──────────────────────────┐
│ 70-90% (~140-180K)       │
│ → Compressed mode        │
│ → Summary only (no full) │
│ → Reduce parallel agents │
└──────────┬───────────────┘
           │
           ▼
┌──────────────────────────┐
│ > 90% (~180K+)           │
│ → Critical mode          │
│ → No pattern loading     │
│ → Suggest /clear         │
│ → Handoff if needed      │
└──────────────────────────┘
```

### Konfiguration

**Speicherort**: `_graph/cache/orchestration-config.json`

```json
{
  "context_budget": {
    "thresholds": {
      "normal": 0.70,
      "compressed": 0.90,
      "critical": 0.95
    },
    "actions": {
      "normal": {
        "load_full_docs": true,
        "parallel_agents": 5
      },
      "compressed": {
        "load_full_docs": false,
        "parallel_agents": 2,
        "summary_only": true
      },
      "critical": {
        "load_full_docs": false,
        "parallel_agents": 0,
        "suggest_clear": true
      }
    }
  }
}
```

### Beispiel

**Session bei 65% Context**:
```
User: "Apply reflection pattern"
  → Load summary (300 tokens) ✓
  → Apply pattern
  → Context: 65% → 67%
```

**Session bei 75% Context**:
```
User: "Apply reflection pattern"
  → Load summary only (300 tokens) ✓
  → Skip full MD ✗
  → Warn: "High context - summary mode active"
  → Context: 75% → 76%
```

**Session bei 92% Context**:
```
User: "Apply reflection pattern"
  → Skip all pattern loading ✗
  → Suggest: "Context at 92%. Run /clear for optimal performance."
  → Offer: "Create handoff and continue in fresh session?"
```

**Relevant**: `.claude/rules/clear-dont-compact.md`

---

## Hydration Pattern

### Was es macht

Lädt alle Memory-Typen (Domain, Experience, Graph) in einem einzelnen optimierten Call beim Session-Start.

### Wie es funktioniert

**Sequential (Old)**:
```
Read _memory/index.json
  → Wait
Read _memory/projects/{active}.json
  → Wait
Query experiences
  → Wait
Read context-router.json
  → Wait

Total: 4 sequential calls
```

**Hydration (Optimized)**:
```
┌─────────────────────────┐
│ Single Hydrate Call     │
│                         │
│ Parallel reads:         │
│ • Domain Memory         │
│ • Experience Memory     │
│ • Graph Context         │
│ • Workflow State        │
│                         │
│ → All at once           │
└────────┬────────────────┘
         │
         ▼
┌─────────────────────────┐
│ Merge & Prioritize      │
│                         │
│ 1. Domain (highest)     │
│ 2. Recent Failures      │
│ 3. High-trust Experiences│
│ 4. Graph Nodes          │
└─────────────────────────┘
```

### Konfiguration

**Hydrate Filter**:
```javascript
// Domain Memory
SELECT * FROM active_project

// Experience Memory (decay-aware)
SELECT *
FROM experiences
WHERE effective_relevance > 30
  AND (valid_until IS NULL OR valid_until > NOW())
ORDER BY effective_relevance DESC
LIMIT 3

// Graph Context
SELECT primary_nodes
FROM context_router
WHERE keywords MATCH user_intent
```

### Beispiel

**Session-Start mit Hydration**:
```
1. Trigger Hydrate:
   → _memory/index.json (active project)
   → _memory/projects/evolving-system.json
   → _memory/experiences/*.json (filtered by decay)
   → _graph/cache/context-router.json

2. Merge Results:
   Domain: {goals, state, progress}
   Experiences: [3 relevant solutions]
   Graph: [primary nodes for "evolving-system"]

3. Announce:
   "Project: Evolving System
    Phase: Knowledge Management v3.3
    Last: Created feature docs
    Relevant experiences: 2
    Next: Review and deploy"
```

**Performance**:
- Old: 4 sequential calls (~2 seconds)
- Hydrated: 1 parallel call (~0.5 seconds)
- Ersparnis: 75% schneller Bootup

**Relevant**: `.claude/rules/domain-memory-bootup.md`

---

## Staged Rules

### Was es macht

Validiert neue Rules durch eine Testphase bevor sie in Produktion gehen.

### Wie es funktioniert

```
New Rule Created
     │
     ▼
┌──────────────────────────┐
│ Status: CANDIDATE        │
│                          │
│ • Not loaded by default  │
│ • Manual review needed   │
└──────────┬───────────────┘
           │
     User promotes
           │
           ▼
┌──────────────────────────┐
│ Status: TRIAL            │
│                          │
│ • Loaded at session start│
│ • Passive tracking       │
│ • No user feedback       │
│                          │
│ Metrics:                 │
│ • applied_count          │
│ • success_count          │
│ • corrections            │
└──────────┬───────────────┘
           │
   Success ≥ 3 sessions?
   No corrections?
           │
           ▼
┌──────────────────────────┐
│ Status: STABLE           │
│                          │
│ • Moved to production    │
│ • Always loaded          │
│ • Part of core system    │
└──────────────────────────┘
```

### Konfiguration

**Staging Index**: `knowledge/rules/staging/_index.json`

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
      "applied_sessions": [
        "2026-01-28",
        "2026-01-29",
        "2026-02-01"
      ],
      "last_applied": "2026-02-01T14:30:00Z",
      "created": "2026-01-15T10:00:00Z"
    }
  ]
}
```

### Beispiel

**Candidate → Trial**:
```
User: "Test this new rule"
  → Status: candidate → trial
  → Rule now loaded at session start
  → Tracking begins
```

**Trial Usage** (Session 1):
```
User: "Debug this error"
  → Keywords: ["debug"]
  → Rule matches, applied silently
  → applied_count++ (1)
  → User doesn't correct
  → success_count++ (1)
```

**Trial Usage** (Sessions 2-3):
```
Similar pattern, no corrections
  → applied_count: 3
  → success_count: 3
  → corrections: 0
```

**Trial → Stable**:
```
Session end check:
  → success_count >= 3? ✓
  → corrections == 0? ✓
  → Promote to stable
  → Move to knowledge/rules/{category}/
  → Now part of core system
```

**Relevant**: `.claude/rules/domain-memory-bootup.md` (Phase 4b)

---

## Clear > Compact

### Was es macht

Empfiehlt frische Sessions zu starten statt Context zu komprimieren wenn Limits erreicht sind.

### Wie es funktioniert

**Compact (Anti-Pattern)**:
```
Context at 90%
     │
     ▼
Try to compress:
• Summarize conversations ✗
• Remove "unnecessary" context ✗
• Truncate history ✗

Problems:
• Loses nuance
• Breaks references
• Causes confusion
• Degrades performance
```

**Clear (Best Practice)**:
```
Context at 90%
     │
     ▼
Create handoff:
• What was done ✓
• What's pending ✓
• Context for next session ✓
     │
     ▼
Run /clear
     │
     ▼
New session:
• Fresh 200K context ✓
• Load handoff ✓
• Continue seamlessly ✓
```

### Konfiguration

**Threshold**: Wann zu Clear raten

```json
{
  "context_thresholds": {
    "warn": 0.70,
    "recommend_clear": 0.85,
    "force_handoff": 0.95
  }
}
```

### Beispiel

**Bei 85% Context**:
```
System: "⚠️ Context at 85% (170K/200K).

         Recommend /clear for optimal performance.

         Options:
         1. Continue (may degrade)
         2. Create handoff + /clear (recommended)
         3. Create handoff only (continue later)"

User: "2"

System:
  → Creates handoff in _handoffs/
  → Runs /clear
  → New session starts
  → Reads handoff automatically
  → Continues where left off (but with 200K available)
```

**Warum Clear > Compact**:
- Erhält volle Context-Treue
- Kein Informationsverlust
- Bessere Leistung
- Nahtlos über Handoffs
- Modelle sind für frischen Context ausgelegt

**Relevant**: `.claude/rules/clear-dont-compact.md`

---

## Zusammenfassung

Context Engineering bietet:
- **Progressive Loading**: 3-layer loading spart 96% Startup-Kosten
- **Summary Layer**: 300-token JSON vs 3000-token MD
- **Budget Awareness**: Passt sich bei 70%/90%/95% Schwellen an
- **Hydration**: Single-call paralleles Laden (75% schneller)
- **Staged Rules**: Trial → Stable Validierung
- **Clear > Compact**: Frische Sessions bewahren Qualität

**Ergebnis**: 200K Context optimal genutzt, keine Degradation, nahtloses Skalieren.
