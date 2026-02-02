---
title: Prompt Patterns
description: Reusable approaches for complex AI tasks
---

# Prompt Patterns

Prompt patterns are reusable approaches for solving complex problems with AI. The Evolving system includes 59 patterns that can be automatically applied based on context.

## What are Prompt Patterns?

Traditional prompt engineering focuses on single interactions. Prompt patterns are **multi-turn frameworks** that guide AI through complex reasoning:

- **Reflection** - Iterative self-critique and refinement
- **React** - Reason about the problem, then act
- **Tree of Thoughts** - Explore multiple solution paths
- **Blackboard** - Multi-agent collaboration

## Pattern Architecture

### Three-Layer Loading

```
Layer 1: Detection (Auto)
  ↓ Keywords match
Layer 2: Summary (300 tokens)
  ↓ Need more detail
Layer 3: Full Pattern (3K tokens)
```

**Result:** 90% token savings through progressive disclosure

### Pattern Structure

```markdown
---
title: Pattern Name
category: reasoning|creation|debugging|collaboration
triggers: [keywords]
---

# Pattern Name

## Core Loop
1. Step one
2. Step two
3. Repeat until done

## When to Use
- Situation A
- Situation B

## When NOT to Use
- Anti-pattern A
- Anti-pattern B

## Config
- iterations: 3
- confidence_threshold: 0.8
```

## Available Patterns

### Reasoning Patterns

#### Reflection Pattern

**Purpose:** Iterative self-improvement through critique

**Core Loop:**
1. Generate solution
2. Self-critique
3. Refine based on critique
4. Repeat 2-3 times

**When to use:**
- Creative work (prompts, content)
- Design decisions
- Optimization problems

**Example:**

```
User: "Improve this API design"

Iteration 1:
  Generate → Review endpoints
  Critique → Missing pagination, no versioning
  Refine → Add /v1/ prefix, ?page= params

Iteration 2:
  Critique → Error responses unclear
  Refine → Add error codes, descriptions

Iteration 3:
  Critique → Good enough
  Final → Ship it
```

#### React Pattern

**Purpose:** Reason before acting

**Core Loop:**
1. **Reason** - Analyze the problem
2. **Act** - Take an action
3. **Observe** - Check results
4. Repeat if needed

**When to use:**
- Debugging
- Exploratory tasks
- Multi-step problem solving

**Example:**

```
User: "Fix this login bug"

Reason: Login fails → Could be auth, DB, or session
Act: Check auth service logs
Observe: Auth succeeds, JWT valid

Reason: Auth OK → Must be session or DB
Act: Check session storage
Observe: Session not persisted

Reason: Found it! Session middleware missing
Act: Add session middleware
Observe: Login works ✓
```

#### Tree of Thoughts

**Purpose:** Explore multiple solution paths

**Core Loop:**
1. Generate 3 solution branches
2. Evaluate each branch
3. Expand most promising
4. Compare final solutions

**When to use:**
- Architecture decisions
- Multiple valid approaches
- High-stakes choices

**Example:**

```
User: "Choose database for new project"

Branch 1: PostgreSQL
  Pros: Relational, ACID, well-known
  Cons: Scaling complexity

Branch 2: MongoDB
  Pros: Flexible schema, horizontal scaling
  Cons: No ACID guarantees

Branch 3: Supabase (Postgres + APIs)
  Pros: Built-in auth, realtime, hosted
  Cons: Vendor lock-in

Evaluate: Supabase wins for MVP speed
Decision: Use Supabase, can migrate later
```

### Creation Patterns

#### Step-by-Step Refinement

**Purpose:** Build complex artifacts incrementally

**Core Loop:**
1. Draft outline
2. Fill in section by section
3. Review and refine each
4. Integrate and polish

**When to use:**
- Long documents
- Complex code modules
- System designs

**Example:**

```
User: "Write comprehensive API docs"

Step 1: Outline
  - Overview
  - Authentication
  - Endpoints
  - Error Codes

Step 2: Draft each section
Step 3: Review for clarity
Step 4: Add examples
Step 5: Final polish
```

### Debugging Patterns

#### Systematic Debugging

**Purpose:** Evidence-based bug fixing

**Core Loop:**
1. Reproduce issue
2. Gather evidence (logs, stack traces)
3. Form hypothesis
4. Test hypothesis
5. Fix if confirmed

**When to use:**
- Bug fixing
- Performance issues
- Unexpected behavior

**Example:**

```
User: "App crashes on startup"

Reproduce: Yes, crashes every time
Evidence: Stack trace points to config.load()
Hypothesis: Invalid config file
Test: Check config.json syntax
Confirm: Missing closing brace
Fix: Add closing brace
Verify: App starts ✓
```

#### Observe Before Editing

**Purpose:** Understand before changing

**Core Loop:**
1. Read relevant code
2. Identify root cause
3. Plan minimal change
4. Make change
5. Verify fix

**When to use:**
- ALWAYS before editing code
- Prevents shotgun debugging
- Reduces regressions

**Example:**

```
User: "Fix the validation error"

DON'T:
  ❌ Edit files randomly
  ❌ Try different approaches until one works

DO:
  ✅ Read validation code
  ✅ Find exact validation failure
  ✅ Understand why it fails
  ✅ Make targeted fix
  ✅ Run tests
```

### Collaboration Patterns

#### Blackboard Pattern

**Purpose:** Multi-agent problem solving

**Core Loop:**
1. Define shared workspace (blackboard)
2. Each agent contributes expertise
3. Agents read others' contributions
4. Iterate until solution emerges

**When to use:**
- Complex multi-domain problems
- Parallel exploration
- Expert coordination

**Example:**

```
Task: "Design and implement feature X"

Blackboard:
  - Requirements (from product agent)
  - Architecture (from architect agent)
  - Implementation (from engineer agent)
  - Tests (from QA agent)
  - Review (from reviewer agent)

Each agent builds on others' work
```

#### Ensemble Pattern

**Purpose:** Multiple perspectives, best answer wins

**Core Loop:**
1. Multiple agents solve independently
2. Compare solutions
3. Pick best or synthesize hybrid

**When to use:**
- High-stakes decisions
- Multiple valid approaches
- Need confidence validation

**Example:**

```
Task: "Refactor this module"

Agent A: Extract classes
Agent B: Use composition
Agent C: Apply functional approach

Compare:
  - A: More OOP, verbose
  - B: Flexible, testable ✓
  - C: Elegant but unfamiliar

Decision: Use B (composition)
```

## Pattern Detection

### Automatic Loading

The system detects patterns based on keywords:

```json
{
  "pattern": "reflection",
  "keywords": ["improve", "refine", "optimize", "better"],
  "confidence": 85,
  "action": "auto_load"
}
```

**Confidence levels:**
- **80-100%** - Auto-load summary
- **50-79%** - Ask user first
- **0-49%** - Don't load

### Manual Override

Force a pattern:

```bash
# Use reflection pattern
User: "Use reflection pattern to improve this"

# Use tree-of-thoughts
User: "Explore alternatives with tree-of-thoughts"
```

### Pattern Combination

Some patterns work well together:

```
tree-of-thoughts → reflection
  ↓ Explore options ↓ Refine winner

react → systematic-debugging
  ↓ Reason+Act ↓ With evidence
```

## Creating Custom Patterns

### Pattern Template

```markdown
---
title: My Custom Pattern
category: reasoning
triggers: [custom, pattern, keywords]
---

# My Custom Pattern

## Core Loop
1. Your step 1
2. Your step 2
3. Repeat

## When to Use
- Situation where this helps

## When NOT to Use
- When it doesn't apply

## Config
- iterations: 3
```

### Registration Steps

1. **Create pattern file**
   ```bash
   knowledge/patterns/my-pattern.md
   ```

2. **Add to knowledge graph**
   ```json
   {
     "id": "pattern-my-pattern",
     "type": "pattern",
     "tags": ["reasoning", "custom"]
   }
   ```

3. **Add context route**
   ```json
   {
     "route": "custom",
     "keywords": ["custom", "pattern"],
     "primary": ["my-pattern"]
   }
   ```

## Pattern Library

### By Category

**Reasoning:**
- Reflection
- React
- Tree of Thoughts
- Chain of Thought

**Creation:**
- Step-by-Step Refinement
- Iterative Generation
- Template Filling

**Debugging:**
- Systematic Debugging
- Observe Before Editing
- Evidence Before Claims

**Collaboration:**
- Blackboard
- Ensemble
- Delegation Request

### By Use Case

**Code Quality:**
- Code Review Pattern
- Refactoring Pattern
- Type Design Pattern

**Planning:**
- Project Planning Pattern
- Task Breakdown Pattern
- Risk Assessment Pattern

**Learning:**
- Concept Extraction Pattern
- Solution Generalization Pattern
- Failure Analysis Pattern

## Best Practices

### DO

✅ **Let the system detect patterns**
```
User: "Improve this design"
→ System loads reflection pattern automatically
```

✅ **Combine compatible patterns**
```
tree-of-thoughts (explore options)
  ↓
reflection (refine winner)
```

✅ **Override when needed**
```
User: "Use react pattern for this"
→ Forces react even if reflection would match
```

### DON'T

❌ **Force patterns that don't fit**
```
User: "Use blackboard for simple task"
→ Overkill, direct execution better
```

❌ **Combine mutex patterns**
```
reflection + react simultaneously
→ Conflicting approaches
```

❌ **Skip pattern when helpful**
```
Complex design task without reflection
→ Missing iterative refinement
```

## Pattern Configuration

### Global Config

```json
{
  "patterns": {
    "auto_detect": true,
    "confidence_threshold": 80,
    "max_iterations": 3
  }
}
```

### Per-Pattern Config

```markdown
## Config
- iterations: 5
- confidence_threshold: 0.9
- allow_backtrack: true
```

## Next Steps

- [Context Routing](../architecture/context-routing.md) - How detection works
