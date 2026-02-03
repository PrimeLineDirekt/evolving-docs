# Knowledge Management

Evolving's knowledge layer provides persistent memory across sessions, decay-aware experience retrieval, entity graphs, and intelligent context routing.

![Knowledge Management Architecture](/shared/assets/infographics/knowledge-management.png)

---

## Domain Memory

### What It Does

Maintains persistent project state across sessions, including goals, progress history, and known failures.

### How It Works

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

### Configuration

**Index Location**: `_memory/index.json`

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

**Project Location**: `_memory/projects/{project}.json`

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

### Example

```
Session 1:
  → Write: Feature X implemented
  → Memory: {"action": "Feature X", "result": "OK", "next": "Tests"}

Session 2 (next day):
  → Load Memory
  → Announce: "Last: Feature X. Next: Tests"
  → Continue seamlessly
```

**Related**: `.claude/rules/domain-memory-bootup.md`

---

## Experience Memory

### What It Does

Stores solutions, patterns, and decisions with decay-aware relevance scoring and trust levels.

### How It Works

**Decay Formula**:
```
effective_relevance = base_relevance × decay_factor × trust_level

decay_factor = 0.9^(days_since_created / 30)
trust_level = 1.0 (verified) | 0.7 (successful) | 0.3 (untested)
```

**Lifecycle**:
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

### Configuration

**Location**: `_memory/experiences/*.json`

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

### Example

**Creating Experience**:
```
User: "That solution worked great!"

System:
  → Extracts solution from conversation
  → Creates experience with trust_level: 0.7
  → Tags: ["auth", "security", "bug-fix"]
  → Stores in _memory/experiences/
```

**Retrieving Experience**:
```
Session Start → Hydrate Pattern:
  → Query experiences WHERE project = active
  → Filter by effective_relevance > 30
  → Sort by effective_relevance DESC
  → Load Top 3

Result: Only relevant, recent, trusted experiences
```

**Related**: `_memory/experiences/SCHEMA.md`

---

## Knowledge Graph

### What It Does

Models entities (commands, agents, patterns, etc.) and their relationships as a connected graph.

### How It Works

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

### Configuration

**Core Files**:
- `_graph/nodes.json` - All entities
- `_graph/edges.json` - All relationships
- `_graph/taxonomy.json` - Unified keywords

**Indexes** (auto-generated):
- `_graph/index/by-type.json` - Grouped by entity type
- `_graph/index/by-domain.json` - Grouped by domain
- `_graph/index/by-project.json` - Grouped by project

### Example

**Query**: "Show me all agents that use the Explore pattern"

```javascript
// 1. Find pattern node
pattern = nodes.find(n => n.id === "pattern:explore")

// 2. Find edges TO pattern
edges = edges.filter(e => e.to === pattern.id && e.type === "uses")

// 3. Get agent nodes
agents = edges.map(e => nodes.find(n => n.id === e.from))

// Result: [agent:Explore, agent:code-explorer, ...]
```

**Visualization**:
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

**Related**: `_graph/README.md`

---

## Context Router

### What It Does

Maps user keywords to relevant knowledge nodes, enabling just-in-time context loading.

### How It Works

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

### Configuration

**Location**: `_graph/cache/context-router.json`

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

### Example

**Without Router** (old way):
```
Session Start → Load ALL rules → 34K tokens
```

**With Router** (optimized):
```
Session Start → Load only core rules → 2K tokens
User: "debug this" → Router loads debug rules → +3K tokens
Total: 5K tokens (85% savings)
```

**Related**: `_graph/cache/context-router.json`

---

## Exploration Index

### What It Does

Caches findings from Explore agents to avoid redundant explorations.

### How It Works

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

### Configuration

**Index Location**: `knowledge/explorations/_index.json`

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

### Example

**First Time**:
```
User: "Explain hook system"
  → No index entry
  → Explore Agent runs (costs tokens)
  → Findings cached in _index.json + .md file
```

**Second Time**:
```
User: "How do hooks work again?"
  → Index match found (2026-01-09)
  → Ask: "Found cached exploration from Jan 9. Load or re-explore?"
  → User: "Load"
  → Read cached .md (much cheaper)
```

**Related**: `.claude/rules/explore-index-check.md`

---

## Session Handoffs

### What It Does

Bridges sessions by documenting completed work and open tasks for the next session.

### How It Works

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

### Configuration

**Location**: `_handoffs/YYYY-MM-DD-topic.md`

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

### Example

**Session 1 End**:
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

**Related**: `knowledge/workflows/handoff-protocol.md`

---

## Summary

Knowledge Management provides:
- **Persistent State**: Domain Memory across sessions
- **Smart Retrieval**: Experience Memory with decay
- **Connected Entities**: Knowledge Graph with 150+ nodes
- **Just-in-Time Loading**: Context Router saves 85% tokens
- **Cached Findings**: Exploration Index avoids redundancy
- **Seamless Continuity**: Session Handoffs bridge work

**Result**: System remembers, learns, and gets smarter over time.
