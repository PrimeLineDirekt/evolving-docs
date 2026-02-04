# Knowledge Graph

The knowledge graph is a unified entity-relationship system that connects all components, patterns, and knowledge artifacts in the Evolving system.

![Knowledge Graph Architecture](../../shared/assets/infographics/knowledge-graph.png)

## Graph Structure

```mermaid
graph TB
    subgraph "Core Files"
        N[knowledge-nodes.json<br/>360+ entities]
        E[edges.json<br/>616+ relationships]
        T[taxonomy.json<br/>Unified keywords]
    end

    subgraph "Indexes"
        BT[by-type.json]
        BD[by-domain.json]
        BP[by-project.json]
    end

    subgraph "Cache"
        CR[context-router.json]
        DC[delegation-config.json]
        TT[task-types.json]
    end

    N --> BT
    N --> BD
    N --> BP
    E --> CR
    T --> CR

    CR --> |Smart Loading| App[Application]
```

## 1. Nodes (Entities)

**Location**: `_graph/knowledge-nodes.json`

Every component, pattern, and knowledge artifact is a node.

### Node Schema

```json
{
  "id": "pattern-reflection",
  "type": "pattern",
  "label": "Reflection Pattern",
  "description": "Self-critique and iterative refinement",
  "keywords": ["reflection", "critique", "iterative", "improvement"],
  "attributes": {
    "category": "reasoning",
    "complexity": 6,
    "use_cases": ["creative", "refinement", "quality"],
    "mutex_group": "A_iteration"
  },
  "metadata": {
    "created": "2026-01-05",
    "last_updated": "2026-01-08",
    "usage_count": 15,
    "success_rate": 0.87
  }
}
```

### Node Types (14 Categories)

| Type | Count | Examples |
|------|-------|----------|
| `command` | 63 | /commit, /debug, /explore |
| `agent` | 65 | Explore, debugger, code-reviewer |
| `skill` | 6 | pdf, commit, review-pr |
| `pattern` | 12 | reflection, react, tree-of-thoughts |
| `rule` | 44 | delegation, failure-recovery |
| `template` | 18 | agent-template, command-template |
| `blueprint` | 9 | memory-system, graph-system |
| `hook` | 12 | delegation-enforcer, auto-cross-reference |
| `learning` | 23 | auto-learning, staged-rules |
| `tool` | 8 | Task, Explore, Read, Write |
| `workflow` | 7 | plan-execution, interview-plan |
| `config` | 15 | context-router, delegation-config |
| `memory` | 5 | domain-memory, experience-memory |
| `documentation` | 73 | guides, references, indexes |

### Node Attributes

Different node types have specialized attributes:

**Pattern Nodes**:
```json
{
  "attributes": {
    "category": "reasoning|multi-agent|decision",
    "complexity": 1-10,
    "mutex_group": "A_iteration|B_multi_agent|C_decision",
    "compatible_with": ["other-pattern-ids"],
    "when_to_use": "Task description",
    "when_not": "Anti-pattern description"
  }
}
```

**Command Nodes**:
```json
{
  "attributes": {
    "category": "workflow|debug|memory|creation",
    "aliases": ["/alias1", "/alias2"],
    "requires_context": ["file", "project"],
    "detection_patterns": ["keyword1", "keyword2"]
  }
}
```

**Agent Nodes**:
```json
{
  "attributes": {
    "plugin": "feature-dev|pr-review-toolkit|builtin",
    "model_preference": "haiku|sonnet|opus",
    "traits": ["engineer", "precise", "iterative"],
    "specialization": "code-review|architecture|exploration"
  }
}
```

## 2. Edges (Relationships)

**Location**: `_graph/edges.json`

Relationships between nodes define how components interact.

### Edge Schema

```json
{
  "id": "edge-001",
  "source": "pattern-reflection",
  "target": "rule-metacognitive-orchestrator",
  "type": "activates",
  "weight": 0.9,
  "metadata": {
    "confidence": "high",
    "bidirectional": false,
    "context": "Pattern detection triggers orchestrator"
  }
}
```

### Edge Types

| Type | Direction | Meaning |
|------|-----------|---------|
| `uses` | A → B | A depends on B |
| `related_to` | A ↔ B | Conceptually similar |
| `activates` | A → B | A triggers B |
| `requires` | A → B | A needs B to function |
| `extends` | A → B | A builds on B |
| `implements` | A → B | A realizes B |
| `documents` | A → B | A describes B |
| `references` | A → B | A mentions B |
| `conflicts_with` | A ⊗ B | A and B are mutually exclusive |
| `part_of` | A ⊂ B | A is component of B |

### Relationship Patterns

**Pattern → Rule**:
```json
{
  "source": "pattern-react",
  "target": "rule-metacognitive-orchestrator",
  "type": "activates",
  "weight": 0.85
}
```

**Command → Agent**:
```json
{
  "source": "command-debug",
  "target": "agent-debugger",
  "type": "uses",
  "weight": 1.0
}
```

**Rule → Template**:
```json
{
  "source": "rule-delegation",
  "target": "template-delegation-prompt",
  "type": "references",
  "weight": 0.7
}
```

**Pattern → Pattern (Mutex)**:
```json
{
  "source": "pattern-reflection",
  "target": "pattern-react",
  "type": "conflicts_with",
  "weight": 1.0,
  "metadata": {
    "reason": "Both in mutex_group A_iteration"
  }
}
```

## 3. Taxonomy (Unified Keywords)

**Location**: `_graph/taxonomy.json`

Standardized keyword system for consistent routing.

### Schema

```json
{
  "version": "1.0",
  "categories": {
    "workflow": {
      "keywords": ["workflow", "process", "pipeline", "automation"],
      "aliases": ["flow", "procedure"],
      "related_types": ["command", "pattern", "rule"]
    },
    "debugging": {
      "keywords": ["debug", "error", "fix", "troubleshoot"],
      "aliases": ["bug", "issue", "problem"],
      "related_types": ["command", "agent", "pattern"]
    },
    "memory": {
      "keywords": ["memory", "context", "state", "persistence"],
      "aliases": ["recall", "storage", "cache"],
      "related_types": ["rule", "config", "memory"]
    }
  },
  "mappings": {
    "debug": "debugging",
    "bug": "debugging",
    "fix": "debugging",
    "flow": "workflow"
  }
}
```

### Keyword Normalization

```
User Input: "I need to fix this bug"
     │
     ▼
Extract: ["fix", "bug"]
     │
     ▼
Normalize via taxonomy:
  "fix" → "debugging"
  "bug" → "debugging"
     │
     ▼
Unified: ["debugging"]
     │
     ▼
Route to: debug commands, debugger agent, debugging patterns
```

## 4. Indexes

Optimized lookups for common access patterns.

### by-type.json

Groups nodes by type for fast filtering:

```json
{
  "command": ["command-commit", "command-debug", "..."],
  "agent": ["agent-explore", "agent-debugger", "..."],
  "pattern": ["pattern-reflection", "pattern-react", "..."],
  "rule": ["rule-delegation", "rule-failure-recovery", "..."]
}
```

**Use Case**: "Show me all available commands"

### by-domain.json

Groups nodes by domain/tag:

```json
{
  "debugging": [
    "command-debug",
    "agent-debugger",
    "pattern-systematic-debugging",
    "rule-observe-before-editing"
  ],
  "delegation": [
    "rule-delegation",
    "agent-explore",
    "config-delegation-config",
    "template-delegation-prompt"
  ]
}
```

**Use Case**: "Load all debugging-related context"

### by-project.json

Groups nodes by project affiliation:

```json
{
  "evolving-system": [
    "all core nodes",
    "system-specific patterns",
    "custom rules"
  ],
  "auswanderungs-ki-v2": [
    "project-specific commands",
    "domain patterns"
  ]
}
```

**Use Case**: "What tools are available for this project?"

## 5. Graph Operations

### Node Discovery

Find nodes by criteria:

```typescript
// By type
nodes.filter(n => n.type === "pattern")

// By keyword
nodes.filter(n => n.keywords.includes("debug"))

// By attribute
nodes.filter(n => n.attributes?.complexity > 7)
```

### Relationship Traversal

Follow edges from a node:

```typescript
// Direct dependencies
edges.filter(e => e.source === "pattern-reflection" && e.type === "uses")

// Related nodes (bidirectional)
edges.filter(e =>
  (e.source === nodeId || e.target === nodeId) &&
  e.type === "related_to"
)

// Conflicts (mutex)
edges.filter(e =>
  e.source === nodeId &&
  e.type === "conflicts_with"
)
```

### Path Finding

Find connection between two nodes:

```
pattern-reflection
     │ activates
     ▼
rule-metacognitive-orchestrator
     │ uses
     ▼
config-context-router
     │ references
     ▼
template-pattern-summary
```

## 6. Graph Integration

### With Memory System

Graph provides structure, Memory provides state:

```
User: "How do I delegate tasks?"
     │
     ▼
Graph: Find nodes with keywords ["delegation", "task"]
  → rule-delegation
  → config-delegation-config
  → template-delegation-prompt
     │
     ▼
Memory: Load recent delegation experiences
  → experience-delegation-success-20260108
  → failure-delegation-too-complex-20260107
     │
     ▼
Merged Context: Rules + Recent learnings
```

### With Context Router

Router uses Graph for smart loading:

```json
{
  "route": "debugging",
  "keywords": ["debug", "error", "fix"],
  "primary_nodes": [
    "command-debug",
    "agent-debugger",
    "pattern-systematic-debugging"
  ],
  "secondary_nodes": [
    "rule-observe-before-editing",
    "rule-evidence-before-claims"
  ],
  "confidence_threshold": 70
}
```

### With Agent Orchestration

Graph defines agent capabilities and relationships:

```
Task: "Review this code for type safety"
     │
     ▼
Graph lookup by keywords: ["review", "type", "safety"]
     │
     ▼
Nodes found:
  - agent-type-design-analyzer (type="agent", specialization="type-review")
  - pattern-code-review (type="pattern")
  - rule-post-todo-review (type="rule")
     │
     ▼
Orchestrator: Use agent-type-design-analyzer with pattern-code-review
```

## 7. Graph Maintenance

### Auto-Update Triggers

| Event | Action |
|-------|--------|
| New command created | Add node, update indexes |
| Agent registered | Add node, create edges to related patterns |
| Pattern documented | Add node, link to implementing rules |
| Rule created | Add node, link to activating patterns |
| Relationship discovered | Add edge |

### Consistency Checks

Automated via `scripts/graph-validator.py`:

```bash
# Check for orphan nodes (no edges)
python scripts/graph-validator.py --check orphans

# Validate edge references
python scripts/graph-validator.py --check edges

# Detect circular dependencies
python scripts/graph-validator.py --check cycles

# Verify index completeness
python scripts/graph-validator.py --check indexes
```

### Manual Updates

When to manually update:

1. **Node attributes change**: Update attributes section
2. **New relationship discovered**: Add edge
3. **Keyword refinement**: Update taxonomy
4. **Index out of sync**: Regenerate via script

## 8. Query Patterns

### Common Queries

**Find all commands in a category**:
```javascript
nodes
  .filter(n => n.type === "command" && n.attributes.category === "debugging")
  .map(n => n.label)
```

**Find related patterns for a task**:
```javascript
const taskKeywords = ["review", "code", "quality"];
nodes
  .filter(n =>
    n.type === "pattern" &&
    n.keywords.some(k => taskKeywords.includes(k))
  )
```

**Find agents that can handle a task**:
```javascript
const requiredTraits = ["engineer", "precise"];
nodes
  .filter(n =>
    n.type === "agent" &&
    requiredTraits.every(t => n.attributes.traits?.includes(t))
  )
```

**Find mutex patterns**:
```javascript
edges
  .filter(e => e.type === "conflicts_with" && e.source === "pattern-reflection")
  .map(e => e.target)
```

## 9. Graph Statistics

Current stats (as of 2026-01-08):

| Metric | Count |
|--------|-------|
| Total nodes | 360+ |
| Total edges | 616+ |
| Node types | 14 |
| Edge types | 10 |
| Avg edges per node | 1.7 |
| Max edges (hub) | 23 (rule-delegation) |
| Orphan nodes | 0 |
| Circular deps | 0 |

### Hub Nodes (Most Connected)

| Node | Type | Edge Count | Role |
|------|------|------------|------|
| rule-delegation | rule | 23 | Orchestration hub |
| config-context-router | config | 19 | Routing hub |
| pattern-reflection | pattern | 15 | Reasoning hub |
| agent-explore | agent | 14 | Discovery hub |
| template-agent-template | template | 12 | Creation hub |

## Best Practices

### DO

- Use indexes for bulk lookups (by-type, by-domain)
- Follow edges to discover related context
- Normalize keywords via taxonomy
- Maintain bidirectional edges for related_to
- Update graph when adding/removing components

### DON'T

- Query nodes.json directly without indexes
- Create edges without weight/metadata
- Use non-standard keywords (use taxonomy)
- Leave orphan nodes (all nodes need >= 1 edge)
- Forget to update indexes after changes

## Related

- [Memory System](./memory-system.md) - State management
- [Context Routing](./context-routing.md) - Smart loading via graph
- [Agent Orchestration](./agent-orchestration.md) - Agent discovery via graph
- Component inventory - See internal project system documentation
