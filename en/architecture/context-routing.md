# Context Routing

Context routing is the intelligent system that loads only relevant documentation and patterns based on task keywords, preventing context bloat while ensuring necessary information is available.

## Core Concept

```mermaid
graph LR
    UI[User Input] --> KE[Keyword Extract]
    KE --> NM[Normalize via Taxonomy]
    NM --> RM[Route Match]
    RM --> CS[Confidence Score]

    CS --> |High 80-100%| AL[Auto Load Primary]
    CS --> |Medium 50-79%| ASK[Ask User]
    CS --> |Low 0-49%| SKIP[Skip Loading]

    AL --> PL[Progressive Load]
    PL --> S1[Layer 1: Summary 300T]
    S1 --> |If needed| S2[Layer 2: Full Doc 3000T]
```

**Problem**: Loading all rules/patterns consumes 25K+ tokens at session start.

**Solution**: Load only what's relevant based on task keywords.

## 1. Router Configuration

**Location**: `_graph/cache/context-router.json`

### Schema

```json
{
  "version": "1.2",
  "routes": [
    {
      "id": "debugging",
      "keywords": ["debug", "error", "fix", "bug", "troubleshoot"],
      "aliases": ["issue", "problem", "broken"],
      "primary_items": [
        {
          "type": "rule",
          "path": "knowledge/rules/debugging/observe-before-editing.md",
          "summary": ".claude/summaries/rules/observe-before-editing.json",
          "confidence_boost": 10
        },
        {
          "type": "pattern",
          "path": "knowledge/patterns/systematic-debugging.md",
          "summary": ".claude/summaries/patterns/systematic-debugging.json",
          "confidence_boost": 5
        }
      ],
      "secondary_items": [
        {
          "type": "rule",
          "path": "knowledge/rules/debugging/evidence-before-claims.md",
          "load_if_confidence": 70
        }
      ],
      "anti_keywords": ["create", "new", "generate"],
      "related_routes": ["testing", "failure-recovery"],
      "default_confidence": 60
    }
  ],
  "fallbacks": {
    "no_match": "ask_user",
    "ambiguous": "list_options",
    "max_routes": 3
  }
}
```

### Route Components

| Component | Purpose |
|-----------|---------|
| `keywords` | Positive signals for this route |
| `aliases` | Alternative terms (normalized via taxonomy) |
| `anti_keywords` | Negative signals (reduces confidence) |
| `primary_items` | Always load when route matches |
| `secondary_items` | Load only if confidence high enough |
| `related_routes` | Suggest if primary route weak |
| `default_confidence` | Base confidence before keyword matching |

## 2. Keyword Matching

### Extraction

```
User: "I need to debug this error in the auth service"
     │
     ▼
Extract keywords:
  - "debug" (verb)
  - "error" (noun)
  - "auth" (domain)
  - "service" (component)
```

### Normalization

```
Raw keywords: ["debug", "error", "auth", "service"]
     │
     ▼
Taxonomy lookup (_graph/taxonomy.json):
  "debug" → "debugging"
  "error" → "debugging"
  "auth" → "authentication"
  "service" → "architecture"
     │
     ▼
Normalized: ["debugging", "authentication", "architecture"]
```

### Matching Algorithm

```typescript
function calculateConfidence(route, userKeywords) {
  let confidence = route.default_confidence;

  // Positive matches
  for (const keyword of userKeywords) {
    if (route.keywords.includes(keyword)) {
      confidence += 10;
    }
    if (route.aliases.includes(keyword)) {
      confidence += 5;
    }
  }

  // Negative matches
  for (const antiKeyword of route.anti_keywords) {
    if (userKeywords.includes(antiKeyword)) {
      confidence -= 15;
    }
  }

  // Boost from primary items
  route.primary_items.forEach(item => {
    if (item.confidence_boost) {
      confidence += item.confidence_boost;
    }
  });

  return Math.min(100, Math.max(0, confidence));
}
```

### Example Scoring

```
Route: "debugging"
Default confidence: 60

User keywords: ["debug", "error", "fix"]

Matches:
  "debug" in keywords → +10
  "error" in keywords → +10
  "fix" in keywords → +10

Final: 60 + 30 = 90 (High confidence)
```

## 3. Confidence Levels

| Level | Range | Action | User Experience |
|-------|-------|--------|----------------|
| **High** | 80-100% | Auto-load primary items | Silent, seamless |
| **Medium** | 50-79% | Ask user confirmation | "Should I load debugging rules?" |
| **Low** | 0-49% | Skip loading | Normal response, no overhead |

### High Confidence (80-100%)

```
User: "Debug this authentication error"
     │
     ▼
Route: "debugging" (confidence: 92)
     │
     ▼
AUTO LOAD:
  - observe-before-editing.md (summary)
  - systematic-debugging.md (summary)
  - evidence-before-claims.md (if confidence > 70)
     │
     ▼
User sees: No interruption, rules active
```

### Medium Confidence (50-79%)

```
User: "Something is wrong with login"
     │
     ▼
Route: "debugging" (confidence: 65)
     │
     ▼
ASK USER:
  "This looks like a debugging task. Should I load
   debugging rules and patterns?"
     │
     ▼
User: "yes" → Load | "no" → Skip
```

### Low Confidence (<50%)

```
User: "Create a new component"
     │
     ▼
Route: "debugging" (confidence: 20)
     │
     ▼
SKIP: No debugging context needed
```

## 4. Progressive Loading

Three-layer approach to minimize token usage.

### Layer 1: JSON Summary (~300 tokens)

**Always loaded** when route matches.

**Location**: `.claude/summaries/{type}/{name}.json`

```json
{
  "id": "rule-observe-before-editing",
  "type": "rule",
  "title": "Observe Before Editing",
  "summary": "Always diagnose before making changes",
  "key_points": [
    "Read diagnostics first",
    "Identify root cause",
    "Verify after edit"
  ],
  "when_to_use": "Before any file edit",
  "when_not": "Trivial changes (typos)",
  "related": ["evidence-before-claims", "failure-recovery"],
  "token_estimate": 280
}
```

**Internalization**: Claude reads and understands the rule without full markdown.

### Layer 2: Full Markdown (~3000 tokens)

**Loaded on demand** when:
- User asks for "more details"
- Edge case detected
- Implementation details needed
- Summary insufficient

**Location**: Original `.md` file

### Layer 3: Related Context

**Loaded if needed** via `related` field:
- User hits edge case mentioned in related rules
- Task complexity increases
- Multi-step problem requires multiple patterns

### Loading Decision Tree

```
Route matched (confidence >= 80)
         │
         ▼
┌─────────────────────────────────┐
│ LOAD Layer 1: Summaries         │
│ (~300 tokens per item)          │
└──────────────┬──────────────────┘
               │
         Sufficient?
         /           \
       YES           NO
        │             │
        ▼             ▼
    Continue      User asks
    with task     for details
                      │
                      ▼
              ┌─────────────────────┐
              │ LOAD Layer 2: Full  │
              │ (~3000 tokens/item) │
              └──────────┬──────────┘
                         │
                   Still need more?
                         │
                         ▼
              ┌─────────────────────┐
              │ LOAD Layer 3: Related│
              │ (recursive)         │
              └─────────────────────┘
```

## 5. Multi-Route Handling

### Exact Match (Single Route)

```
User: "Debug the login error"

Routes matched:
  - debugging (95)

Action: Load debugging route
```

### Fuzzy Match (Multiple Routes)

```
User: "I need to improve this code and fix bugs"

Routes matched:
  - debugging (78)
  - refactoring (72)
  - code-quality (65)

Action: Ask user which focus
  "This could be debugging OR refactoring.
   Which should I prioritize?"
```

### Fallback

```
User: "What should I do next?"

Routes matched:
  - (none above 50)

Action: Check fallback config
  → fallbacks.no_match = "ask_user"
  → "I'm not sure what you need. Could you clarify?"
```

## 6. Context Budget Awareness

Router respects context limits.

### Budget Calculation

```typescript
const CONTEXT_LIMIT = 200000; // Opus 4.5 tokens
const CURRENT_USAGE = getCurrentUsage();
const AVAILABLE = CONTEXT_LIMIT - CURRENT_USAGE;

if (AVAILABLE < 10000) {
  // Critical: Skip all loading
  return "skip";
} else if (AVAILABLE < 30000) {
  // Tight: Summary only, no full docs
  return "summary_only";
} else {
  // Normal: Progressive loading
  return "progressive";
}
```

### Budget-Aware Loading

| Context Usage | Behavior |
|---------------|----------|
| < 70% | Normal: Summary + Full on demand |
| 70-90% | Summary only, no Full docs |
| > 90% | No loading, suggest /clear |

## 7. Integration Points

### With Memory System

```
Session Start → Bootup Ritual
     │
     ▼
Load Domain Memory (5K tokens)
     │
     ▼
User request → Context Router
     │
     ▼
Load relevant rules/patterns (3K tokens)
     │
     ▼
Total: ~8K instead of ~30K
```

### With Knowledge Graph

```
Router uses Graph for discovery:
  1. User keywords → Normalized
  2. Graph nodes filtered by keywords
  3. Edges followed for related items
  4. Router decides what to load
```

### With Metacognitive Orchestrator

```
User request
     │
     ▼
Orchestrator extracts keywords
     │
     ▼
Context Router finds matches
     │
     ▼
Orchestrator loads summaries
     │
     ▼
Pattern activated if high confidence
```

## 8. Route Examples

### Debugging Route

```json
{
  "id": "debugging",
  "keywords": ["debug", "error", "fix", "bug"],
  "primary_items": [
    "observe-before-editing",
    "evidence-before-claims",
    "systematic-debugging"
  ],
  "related_routes": ["testing", "failure-recovery"]
}
```

**Triggers**: "debug", "error", "fix the bug", "troubleshoot"

### Delegation Route

```json
{
  "id": "delegation",
  "keywords": ["delegate", "agent", "task", "sub-agent"],
  "primary_items": [
    "delegation",
    "smart-model-delegation",
    "trait-system"
  ],
  "related_routes": ["orchestration", "task-management"]
}
```

**Triggers**: "delegate this", "use agent", "spawn sub-agent"

### Creative Route

```json
{
  "id": "creative",
  "keywords": ["improve", "refine", "better", "optimize"],
  "primary_items": [
    "reflection-pattern",
    "iterative-refinement"
  ],
  "anti_keywords": ["debug", "fix", "error"],
  "related_routes": ["code-quality"]
}
```

**Triggers**: "improve this", "make it better", "refine the approach"

**Anti-triggers**: "fix error" (debugging, not creative)

## 9. Router Maintenance

### Adding a New Route

1. **Define keywords**: What user says to trigger this route?
2. **Set primary items**: What MUST load?
3. **Set secondary items**: What's optional?
4. **Define anti-keywords**: What indicates NOT this route?
5. **Link related routes**: What's similar?
6. **Test confidence scoring**: Does it trigger appropriately?

### Validating Routes

```bash
# Test route matching
python scripts/test-router.py --input "debug authentication error"

# Expected output:
# Route: debugging (confidence: 92)
# Primary items: 3
# Secondary items: 1
# Token estimate: ~900
```

### Monitoring Usage

Track which routes are used most:

```json
{
  "route_usage": {
    "debugging": {"count": 47, "avg_confidence": 85},
    "delegation": {"count": 32, "avg_confidence": 78},
    "creative": {"count": 15, "avg_confidence": 72}
  }
}
```

## 10. Performance Impact

### Before Context Router

```
Session start: Load all rules/patterns
Token usage: ~30K tokens
Time: ~2-3 seconds
Relevance: 20-30% actually needed
```

### After Context Router

```
Session start: Load only Domain Memory
Token usage: ~5K tokens
Time: ~0.5 seconds

On demand (per task):
Token usage: ~3K tokens (progressive)
Relevance: 90%+ actually needed

Total savings: ~22K tokens per session
```

## Best Practices

### DO

- Use normalized keywords via taxonomy
- Set confidence thresholds conservatively
- Provide clear anti-keywords
- Link related routes for fallback
- Monitor route usage and adjust
- Use progressive loading (summary → full)

### DON'T

- Match too broadly (low precision)
- Set confidence too low (false positives)
- Load full docs immediately
- Ignore context budget
- Create overlapping routes without distinction
- Forget to update when adding patterns/rules

## Related

- [Memory System](./memory-system.md) - Domain Memory integration
- [Knowledge Graph](./knowledge-graph.md) - Graph-based discovery
- [Agent Orchestration](./agent-orchestration.md) - Pattern activation
- Metacognitive orchestrator patterns - Implementation details in internal project documentation
