# Using Patterns

Patterns are proven problem-solving approaches that help you tackle complex tasks systematically. This guide shows you when and how to apply patterns effectively.

## What Are Patterns?

Patterns are reusable mental models for approaching different types of problems:

- **Reflection Pattern**: Iterative self-improvement through critique
- **ReAct Pattern**: Reasoning + Acting in cycles
- **Tree of Thoughts**: Explore multiple solution paths
- **Chain of Thought**: Step-by-step reasoning
- **Ensemble Pattern**: Multiple agents, different perspectives
- **Blackboard Pattern**: Shared workspace for collaboration

**Location**: `knowledge/patterns/`

## Finding the Right Pattern

### By Problem Type

| Problem Type | Recommended Pattern |
|--------------|-------------------|
| **Improve existing solution** | Reflection |
| **Debug complex issue** | ReAct |
| **Critical decision** | Tree of Thoughts |
| **Multi-perspective analysis** | Ensemble |
| **Complex reasoning** | Chain of Thought |
| **Team coordination** | Blackboard |

### By Task Characteristics

```
Need iteration/refinement? → Reflection
Need exploration/experimentation? → ReAct
Need to evaluate options? → Tree of Thoughts
Need multiple viewpoints? → Ensemble
Need to break down complexity? → Chain of Thought
Need agent coordination? → Blackboard
```

### Via Context Router

The system can auto-suggest patterns:

```
User: "Improve this code"
→ Context Scout detects "improve"
→ Loads reflection pattern (confidence: 85%)
→ Applies iterative refinement
```

**Config**: `_graph/cache/context-router.json`

## Pattern Structure

Each pattern follows this format:

```markdown
# {Pattern Name}

## Core Loop
{The fundamental iteration cycle}

## When to Use
{Situations where this pattern excels}

## When NOT to Use
{Anti-patterns and wrong situations}

## Steps
1. {Phase 1}
2. {Phase 2}
...

## Example
{Concrete application}

## Related
{Links to similar patterns}
```

## Applying Patterns Step by Step

### 1. Identify Your Problem

```markdown
Problem: "My API design is functional but feels clunky"

Characteristics:
- Existing solution ✓
- Need refinement ✓
- No clear bugs ✓
- Want improvement ✓

→ Pattern: Reflection
```

### 2. Load Pattern Context

```bash
# Manual
Read knowledge/patterns/reflection-pattern.md

# Auto (via Context Scout)
User: "Refine this API design"
→ System loads reflection pattern summary
```

### 3. Follow Pattern Steps

**Reflection Pattern Example:**

```markdown
## Step 1: Initial State
Current API:
```typescript
class UserAPI {
  getUser(id: string): Promise<User>
  updateUser(id: string, data: Partial<User>): Promise<User>
  deleteUser(id: string): Promise<void>
}
```

## Step 2: Self-Critique
Issues:
- Inconsistent error handling (throws vs returns null)
- No input validation
- Missing batch operations
- No caching strategy

## Step 3: Refinement
```typescript
class UserAPI {
  // Consistent Result<T, E> return type
  async getUser(id: string): Promise<Result<User, APIError>>

  // Input validation via schema
  async updateUser(
    id: string,
    data: UpdateUserSchema
  ): Promise<Result<User, ValidationError>>

  // Soft delete with reason
  async deleteUser(
    id: string,
    reason: string
  ): Promise<Result<void, APIError>>

  // New: Batch operations
  async getUsers(ids: string[]): Promise<Result<User[], APIError>>
}
```

## Step 4: Re-Evaluate
Improvements:
✅ Consistent error handling
✅ Input validation
✅ Batch operations
✅ Better type safety

Remaining issues:
- Caching strategy still undefined
- Rate limiting not addressed

## Step 5: Iterate (if needed)
Continue refining...
```

### 4. Know When to Stop

Stop iterating when:
- ✅ Core issues addressed
- ✅ Diminishing returns (< 10% improvement per cycle)
- ✅ Time/context budget exceeded
- ✅ User satisfied with result

## Combining Patterns

Patterns can be used together:

### Sequential Combination

```
Tree of Thoughts → Reflection
(Explore options) → (Refine chosen option)

ReAct → Reflection
(Explore problem) → (Refine solution)
```

### Parallel Combination

```
Ensemble + Chain of Thought
(Multiple agents each use structured reasoning)

Blackboard + ReAct
(Shared workspace where agents explore)
```

### Example: Complex Feature Design

```markdown
## Phase 1: Exploration (Tree of Thoughts)
Generate 3 design approaches:
1. Event-driven architecture
2. Microservices
3. Monolithic with modules

Evaluate each against criteria...
Choose: Modular monolith

## Phase 2: Refinement (Reflection)
Initial design:
{modules, APIs, data flow}

Critique → Refine → Re-evaluate
Iterate 3 times until solid

## Phase 3: Implementation (ReAct)
Reasoning: "Start with core module"
Action: Implement core
Observation: Works but coupling tight
Reasoning: "Introduce interfaces"
Action: Add abstraction layer
...
```

## When NOT to Use Patterns

### Anti-Patterns

❌ **Over-engineering simple tasks**
```
User: "Fix this typo"
Wrong: Apply reflection pattern (3 iterations on a typo!)
Right: Just fix it directly
```

❌ **Pattern for pattern's sake**
```
User: "Read this file"
Wrong: Tree of Thoughts (explore 5 ways to read!)
Right: Direct Read tool
```

❌ **Ignoring context budget**
```
Context: 85% full
Wrong: Start ensemble pattern (spawn 5 agents)
Right: Single-agent with clear constraint
```

### Decision Matrix

| Task Complexity | Pattern? | Why |
|----------------|----------|-----|
| Trivial (1-2 steps) | ❌ No | Overhead > value |
| Simple (3-5 steps) | ❌ No | Direct approach faster |
| Moderate (6-10 steps) | ✅ Maybe | If uncertainty/ambiguity |
| Complex (10+ steps) | ✅ Yes | Structure prevents chaos |

## Practical Examples

### Example 1: Reflection Pattern for Code Review

```markdown
**Problem**: Review auth service implementation

**Pattern**: Reflection

**Application**:

Cycle 1:
- Read code
- Critique: Missing input validation
- Refine: Add Zod schemas
- Re-evaluate: Better, but error handling weak

Cycle 2:
- Critique: Generic error messages
- Refine: Add specific error types
- Re-evaluate: Good, but no logging

Cycle 3:
- Critique: No audit trail
- Refine: Add structured logging
- Re-evaluate: Solid! Ship it.
```

### Example 2: ReAct Pattern for Debugging

```markdown
**Problem**: API returns 500 error intermittently

**Pattern**: ReAct

**Application**:

Thought: "Check server logs"
Action: Read logs/error.log
Observation: "Database timeout errors"

Thought: "Check DB connection pool"
Action: Read config/database.ts
Observation: "Pool size = 5, likely too small"

Thought: "Check concurrent request count"
Action: Bash: grep "concurrent" logs/access.log
Observation: "Peak = 50 requests/sec"

Thought: "5 connections for 50 req/sec = bottleneck"
Action: Update pool size to 20
Observation: "Error rate drops to near zero"

Result: Problem identified and fixed
```

### Example 3: Tree of Thoughts for Architecture

```markdown
**Problem**: Design authentication system

**Pattern**: Tree of Thoughts

**Application**:

Branch 1: JWT-based
- Pros: Stateless, scalable
- Cons: Hard to revoke, token size
- Score: 7/10

Branch 2: Session-based
- Pros: Easy revocation, small cookies
- Cons: Server state, Redis dependency
- Score: 6/10

Branch 3: Hybrid (JWT + refresh tokens)
- Pros: Best of both, revocable
- Cons: More complex
- Score: 9/10

Decision: Choose Branch 3 (Hybrid)

Next: Apply Reflection to refine the hybrid design
```

## Pattern Discovery

### Via Auto-Detection

```
User input → Keywords extracted → Context Router match → Pattern loaded

Example:
"How can I improve this?"
→ Keywords: ["improve", "refine"]
→ Match: reflection pattern (confidence: 90%)
→ Auto-load summary
```

### Via Manual Selection

```bash
# List available patterns
/list-patterns

# Apply specific pattern
"Use reflection pattern to improve this code"

# Or reference directly
Read knowledge/patterns/reflection-pattern.md
```

### Via Agent Recommendation

Agents can suggest patterns:

```
Explorer Agent: "This problem has multiple valid approaches.
                 Consider using Tree of Thoughts pattern."
```

## Related

- [Pattern Catalog](../architecture/context-routing.md) - All available patterns
- [Context Router](../architecture/context-routing.md) - Auto-detection
- [Writing Commands](writing-commands.md) - Use patterns in commands
- [Creating Agents](creating-agents.md) - Agents that apply patterns
