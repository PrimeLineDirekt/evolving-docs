# Intelligente Orchestrierung

Die Orchestrierungsebene von Evolving delegiert Aufgaben automatisch an spezialisierte Agents, kombiniert Traits für optimale Leistung und wählt das richtige Modell für jeden Job.

---

## Smart Delegation

### Was es macht

Bestimmt automatisch, ob eine Aufgabe direkt bearbeitet oder an einen spezialisierten Agent delegiert werden soll, basierend auf einem Bewertungssystem.

### Wie es funktioniert

```
User Task
    │
    ▼
┌─────────────────────────┐
│ Score Calculation       │
│                         │
│ +2  Scope > 2 files     │
│ +2  Bulk operation      │
│ +2  Research/learn      │
│ +2  Code review         │
│ +3  Exploration         │
│ -10 Critical keywords   │
│ -5  User wants to see   │
└──────────┬──────────────┘
           │
     Score ≥ 3?
      /        \
    YES         NO
     │           │
     ▼           ▼
  Delegate    Execute
             Directly
```

### Konfiguration

**Speicherort**: `_graph/cache/delegation-config.json`

```json
{
  "task_types": {
    "exploration": {
      "agent": "Explore",
      "model": "haiku",
      "auto_delegate": true
    },
    "bug_fix": {
      "traits": ["engineer", "precise", "iterative"],
      "model": "sonnet"
    }
  }
}
```

### Beispiel

```
User: "Find all uses of the auth function"

System:
  → Keywords: ["find", "search"]
  → Score: +3 (exploration)
  → Delegates to Explore Agent (haiku)
  → Completes in fresh context
```

**Relevant**: `.claude/rules/delegation.md`

---

## Agent Swarm

### Was es macht

Koordiniert mehrere spezialisierte Agents, die parallel an unabhängigen Teilaufgaben arbeiten.

### Wie es funktioniert

```
Complex Task
     │
     ▼
┌─────────────────────────────┐
│ Task Decomposition          │
│                             │
│ Task A → Agent 1 (haiku)    │
│ Task B → Agent 2 (sonnet)   │
│ Task C → Agent 3 (sonnet)   │
│   (blockedBy: [A, B])       │
└──────────┬──────────────────┘
           │
           ▼
┌─────────────────────────────┐
│ Parallel Execution          │
│                             │
│ ┌─────┐  ┌─────┐            │
│ │  A  │  │  B  │ (parallel) │
│ └──┬──┘  └──┬──┘            │
│    └────┬────┘              │
│         ▼                   │
│      ┌─────┐                │
│      │  C  │ (waits)        │
│      └─────┘                │
└──────────┬──────────────────┘
           │
           ▼
    Result Synthesis
```

### Konfiguration

Verwendet Task Tool mit Dependencies:

```javascript
// Create tasks
TaskCreate({ subject: "Analyze backend", ... })  // Task #1
TaskCreate({ subject: "Analyze frontend", ... }) // Task #2
TaskCreate({ subject: "Integration test", ... }) // Task #3

// Set dependency
TaskUpdate({ taskId: "3", addBlockedBy: ["1", "2"] })
```

### Beispiel

```
User: "Refactor the auth module"

System decomposes:
  1. Explore current implementation (haiku, parallel)
  2. Review dependencies (haiku, parallel)
  3. Generate refactor plan (sonnet, after 1+2)
  4. Execute changes (sonnet, after 3)

Result: 2x faster through parallelization
```

**Relevant**: `.claude/rules/swarm-orchestration.md`

---

## Trait Composition

### Was es macht

Erstellt spezialisierte Agent-Profile durch Kombination von 480 möglichen Trait-Kombinationen (8 Expertise × 10 Persönlichkeit × 6 Ansatz).

### Wie es funktioniert

**Trait-Kategorien**:
- **Expertise**: engineer, researcher, architect, security, analyst, etc.
- **Personality**: precise, direct, cautious, thorough, skeptical, etc.
- **Approach**: systematic, iterative, exploratory, adversarial, etc.

**Komposition**:
```
Task: Fix subtle bug
  → Traits: ["engineer", "precise", "iterative"]
  → Profile: Engineering-focused, detail-oriented, step-by-step

Task: Security audit
  → Traits: ["security", "skeptical", "adversarial"]
  → Profile: Security-focused, distrusting, attack-minded
```

### Konfiguration

**Speicherort**: `knowledge/rules/delegation/trait-system.md`

Traits werden automatisch basierend auf Task-Typ via `delegation-config.json` ausgewählt.

### Beispiel

```json
{
  "task_type": "bug_fix",
  "traits": ["engineer", "precise", "iterative"],
  "profile": {
    "focus": "Code correctness",
    "approach": "Systematic debugging",
    "mindset": "Detail-oriented"
  }
}
```

**Ausgabe**:
```
Agent behavior:
  ✓ Checks diagnostics before editing
  ✓ Tests after each change
  ✓ Documents assumptions
  ✓ Verifies with build
```

**Relevant**: `knowledge/rules/delegation/trait-system.md`

---

## Model Selection

### Was es macht

Wählt automatisch das optimale Modell (haiku/sonnet/opus) basierend auf Task-Komplexität.

### Wie es funktioniert

**Entscheidungsmatrix**:

| Komplexität | Model | Kosten | Use Case |
|------------|-------|--------|----------|
| 1-3 | Haiku | $ | Search, list, simple edits |
| 4-6 | Sonnet | $$ | Refactoring, reviews, design |
| 7+ | Opus (self) | $$$ | Architecture, complex logic |

**Komplexitätsfaktoren**:
- +1 pro beteiligter Datei
- +2 für Logik-Änderungen
- +1 für neue Patterns
- -1 für reine Read-Only-Tasks

### Konfiguration

**Speicherort**: `.claude/rules/smart-model-delegation.md`

```json
{
  "thresholds": {
    "haiku_max": 3,
    "sonnet_max": 6,
    "opus_min": 7
  }
}
```

### Beispiel

```
Task: "List all commands"
  → Complexity: 1 (read-only)
  → Model: haiku
  → Cost: $0.001

Task: "Refactor auth service"
  → Complexity: 5 (3 files + logic)
  → Model: sonnet
  → Cost: $0.015

Task: "Design new architecture"
  → Complexity: 8 (multi-system)
  → Model: opus (don't delegate)
  → Cost: $0.075
```

**Relevant**: `.claude/rules/smart-model-delegation.md`

---

## Parallel Execution

### Was es macht

Führt unabhängige Tasks gleichzeitig aus, indem mehrere Tool-Aufrufe in einer einzelnen Nachricht verwendet werden.

### Wie es funktioniert

**Sequential** (langsam):
```
Call Agent 1 → Wait → Call Agent 2 → Wait → Combine
```

**Parallel** (schnell):
```
Call Agent 1 ┐
Call Agent 2 ├─ Wait → Combine
Call Agent 3 ┘
```

### Konfiguration

Keine Konfiguration erforderlich - einfach mehrere Task Tool Calls in eine Antwort machen.

### Beispiel

**Sequential (❌ ineffizient)**:
```
Task({ prompt: "Analyze backend" })
[wait for result]
Task({ prompt: "Analyze frontend" })
[wait for result]
```

**Parallel (✅ optimal)**:
```
Task({ prompt: "Analyze backend" })
Task({ prompt: "Analyze frontend" })
Task({ prompt: "Check tests" })
[all execute simultaneously]
```

**Ergebnis**: 3x schnellere Ausführung

**Relevant**: `.claude/rules/swarm-orchestration.md`

---

## Delegation Request Pattern

### Was es macht

Ermöglicht es Layer 2 Agents (ohne Task Tool) weitere Delegation an Layer 1 Orchestrator anzufordern.

### Wie es funktioniert

**Problem**: Sub-Agents können keine weiteren Agents spawnen (kein Task Tool Zugriff).

**Lösung**: Sub-Agent gibt strukturierte JSON-Anfrage zurück.

```
Layer 1 (Orchestrator)
    │
    │ Delegates complex task
    ▼
Layer 2 (Sub-Agent)
    │
    │ Realizes needs more specialization
    │
    ▼
┌──────────────────────────┐
│ Delegation Request JSON  │
│                          │
│ {                        │
│   "delegation_request": true,
│   "reason": "...",       │
│   "recommended_tasks": [ │
│     {                    │
│       "subject": "...",  │
│       "model": "haiku",  │
│       "agent": "Explore" │
│     }                    │
│   ]                      │
│ }                        │
└──────────┬───────────────┘
           │
           ▼
Layer 1 (Orchestrator)
    │
    │ Creates & executes tasks
    │
    ▼
  Results combined
```

### Konfiguration

Keine Konfiguration - Pattern ist konventionsbasiert.

### Beispiel

**Sub-agent output**:
```json
{
  "delegation_request": true,
  "reason": "Auth module spans 3 files with complex dependencies",
  "recommended_tasks": [
    {
      "subject": "Map auth dependencies",
      "model": "haiku",
      "agent": "Explore",
      "blockedBy": []
    },
    {
      "subject": "Refactor auth.ts",
      "model": "sonnet",
      "agent": "general-purpose",
      "traits": ["engineer", "precise"],
      "blockedBy": ["Map auth dependencies"]
    }
  ]
}
```

**Layer 1 führt aus**:
1. Erstellt Task #1 (Explore)
2. Erstellt Task #2 (Engineer)
3. Setzt Task #2 blockedBy Task #1
4. Führt beide aus (sequenziell aufgrund von Abhängigkeit)
5. Kombiniert Ergebnisse

**Relevant**: `knowledge/patterns/delegation-request-pattern.md`

---

## Zusammenfassung

Intelligente Orchestrierung automatisiert:
- **Delegiert** Tasks wenn Score ≥ 3
- **Koordiniert** mehrere Agents parallel
- **Kombiniert** 480 Trait-Kombinationen
- **Wählt** optimales Modell nach Komplexität
- **Führt** unabhängige Tasks gleichzeitig aus
- **Bearbeitet** Layer 2 Delegation-Anfragen

**Ergebnis**: Schnellere Ausführung, niedrigere Kosten, bessere Spezialisierung.
