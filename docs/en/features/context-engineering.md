# Context Engineering

Evolving optimizes context window usage through progressive loading, summary layers, budget awareness, and strategic memory patterns.

![Context Engineering Architecture](/shared/assets/infographics/context-engineering.png)

---

## Progressive Loading

### What It Does

Loads knowledge in three stages (JSON config → Summary → Full docs) based on need, preventing context bloat.

### How It Works

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

### Configuration

**Layer 1 Location**: `_graph/cache/task-types.json`
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

**Layer 2 Location**: `.claude/summaries/patterns/systematic-debugging.json`
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

**Layer 3 Location**: `knowledge/patterns/systematic-debugging-pattern.md`

### Example

**Without Progressive Loading**:
```
Session Start:
  → Load ALL patterns → 30K tokens
  → Load ALL rules → 25K tokens
  → Total: 55K tokens used
  → Available for work: 145K tokens
```

**With Progressive Loading**:
```
Session Start:
  → Load configs → 2K tokens

User: "debug this error"
  → Load debug summary → 300 tokens
  → Apply pattern
  → Total: 2.3K tokens used
  → Available for work: 197.7K tokens
```

**Savings**: 96% reduction in startup cost

**Related**: `.claude/rules/metacognitive-orchestrator.md`

---

## Summary Layer

### What It Does

Provides compact JSON summaries of markdown docs, enabling quick understanding without loading full content.

### How It Works

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

### Configuration

**Summary Structure**:
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

### Example

**Query**: "How does delegation request work?"

**Without Summary**:
```
→ Load full MD (2800 tokens)
→ Parse entire document
→ Extract relevant parts
→ Answer question
```

**With Summary**:
```
→ Load summary (300 tokens)
→ Read core_loop: "Sub-agent → JSON → Layer 1"
→ Read when_to_use
→ Answer question (10x faster)
```

**Follow-up**: "Show me implementation details"
```
→ NOW load full MD (2800 tokens)
→ Deep dive into specifics
```

**Related**: `.claude/summaries/README.md`

---

## Budget Awareness

### What It Does

Monitors context usage and prevents degradation by adapting behavior at defined thresholds.

### How It Works

**Model-Specific Degradation Points**:

| Model | Degradation Starts | Severe Degradation |
|-------|-------------------|-------------------|
| Opus 4.5 | ~100K tokens | ~180K tokens |
| Sonnet 4.5 | ~80K tokens | ~150K tokens |

**Threshold Actions**:
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

### Configuration

**Location**: `_graph/cache/orchestration-config.json`

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

### Example

**Session at 65% context**:
```
User: "Apply reflection pattern"
  → Load summary (300 tokens) ✓
  → Apply pattern
  → Context: 65% → 67%
```

**Session at 75% context**:
```
User: "Apply reflection pattern"
  → Load summary only (300 tokens) ✓
  → Skip full MD ✗
  → Warn: "High context - summary mode active"
  → Context: 75% → 76%
```

**Session at 92% context**:
```
User: "Apply reflection pattern"
  → Skip all pattern loading ✗
  → Suggest: "Context at 92%. Run /clear for optimal performance."
  → Offer: "Create handoff and continue in fresh session?"
```

**Related**: `.claude/rules/clear-dont-compact.md`

---

## Hydration Pattern

### What It Does

Loads all memory types (domain, experience, graph) in a single optimized call at session start.

### How It Works

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

### Configuration

**Hydrate Filters**:
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

### Example

**Session Start with Hydration**:
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
- Savings: 75% faster bootup

**Related**: `.claude/rules/domain-memory-bootup.md`

---

## Staged Rules

### What It Does

Validates new rules through a trial period before promoting them to production.

### How It Works

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

### Configuration

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

### Example

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

**Related**: `.claude/rules/domain-memory-bootup.md` (Phase 4b)

---

## Clear > Compact

### What It Does

Recommends starting fresh sessions instead of trying to compress context when limits are reached.

### How It Works

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

### Configuration

**Threshold**: When to suggest clear

```json
{
  "context_thresholds": {
    "warn": 0.70,
    "recommend_clear": 0.85,
    "force_handoff": 0.95
  }
}
```

### Example

**At 85% context**:
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

**Why Clear > Compact**:
- Maintains full context fidelity
- No information loss
- Better performance
- Seamless via handoffs
- Models designed for fresh context

**Related**: `.claude/rules/clear-dont-compact.md`

---

## Summary

Context Engineering provides:
- **Progressive Loading**: 3-layer loading saves 96% startup cost
- **Summary Layer**: 300-token JSON vs 3000-token MD
- **Budget Awareness**: Adapts at 70%/90%/95% thresholds
- **Hydration**: Single-call parallel loading (75% faster)
- **Staged Rules**: Trial → stable validation
- **Clear > Compact**: Fresh sessions maintain quality

**Result**: 200K context used optimally, no degradation, seamless scaling.
