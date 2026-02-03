---
title: Failure Recovery
type: rule
tags: []
lang: en
confidence: 100
---

# Failure Recovery


## Overview

<div class="component-meta" markdown>
| Attribute | Value |
|-----------|-------|
| **Type** | Rule |
| **Purpose** | Systematic escalation strategy for handling repeated fix failures |
| **Complexity** | medium |
| **Model** | sonnet |
| **Category** | rules |</div>


## What It Does

Failure Recovery implements a 4-stage escalation strategy when fixes fail repeatedly. After 2 failed attempts, it mandates delegating to specialized sub-agents (Explore, debugger) for systematic analysis instead of continuing to guess. This prevents infinite loops, token waste, and ensures root cause identification through evidence-based investigation.

**Escalation Stages:**
1. **Attempts 1-2**: Try fixing yourself with evidence (build, test, verify)
2. **Attempt 3**: MANDATORY sub-agent analysis (Explore + debugger for facts)
3. **Attempt 4**: Present agent findings to user with concrete options
4. **Blocked**: Document and log to memory if unresolvable


## System Impact

**When It Triggers:**
After each failed fix attempt (tracks failure counter mentally)

**Behavior Enforced:**
- Detect loop symptoms (same change reversed, contradictory info, ping-pong states)
- Stop self-fixing at attempt 3 → delegate to Explore/debugger agents
- Require evidence for all actions (diagnostics clean, exit code 0, tests pass)
- Never leave code in broken state
- Never delete tests to make them "pass"
- Don't trust handoff/memory blindly when loops detected

**Integration Points:**
- Delegation rule (sub-agent execution)
- Domain memory (failure logging)
- Evidence requirement (diagnostics, build, tests)


## Architecture

**Trigger:** After each failed fix attempt

**Dependencies:**
- Explore agent (investigation)
- debugger agent (root cause analysis)
- Domain memory (failure logging)

**Escalation Flow:**
1. **Fix 1-2**: Self-fix with evidence → verify
2. **Fix 3**: STOP → parallel sub-agents for facts
3. **Fix 4**: Present findings → user decides
4. **Blocked**: Document + memory log

**Anti-Loop Detection:**
Triggers immediate sub-agent delegation when detecting:
- Same change repeatedly reversed
- Contradictory info from different sources
- Ping-pong between two states


## Usage

**Fix Counter (Mental Model):**
```
Problem detected
  → Fix #1 (with evidence) → Success? DONE
  → Fix #2 (with evidence) → Success? DONE
  → Fix #3 = MANDATORY SUB-AGENTS
     - Explore: "What does Component A expect?"
     - Explore: "What does Component B send?"
     - debugger: "Verify E2E flow"
  → Fix #4 = Present findings to user
  → Still blocked? Document + memory log
```

**Sub-Agent Strategies:**

**Code Mismatch (Frontend ↔ Backend):**
```
Parallel:
- Explore Agent → Backend: "What fields does endpoint X expect?"
- Explore Agent → Frontend: "What fields does component Y send?"
- debugger Agent → "Verify E2E request/response"
```

**Build/Test Failures:**
```
- debugger Agent → "Analyze error stack, find root cause"
- Explore Agent → "Check dependencies and imports"
```

**Config Problems:**
```
- Explore Agent → "Analyze all relevant config files"
- debugger Agent → "Check environment and runtime"
```


## Configuration

| Stage | Action | Evidence Required |
|-------|--------|-------------------|
| Fix 1-2 | Self-fix | Diagnostics clean, build success, tests pass |
| Fix 3 | Sub-agents | Agent analysis results |
| Fix 4 | User consultation | Agent findings presented |
| Blocked | Document | Memory log + handoff entry |


## Best Practices

**Do:**
- Identify root cause, not just symptoms
- Re-verify after EVERY fix (don't batch)
- Track failure counter mentally
- Use sub-agents at attempt 3 (mandatory)
- Require evidence: diagnostics clean, build passes, tests pass
- Detect loops early (same change reversed, contradictory sources)

**Don't:**
- Leave code in broken state
- Continue guessing beyond attempt 2
- Delete tests to make them "pass"
- Trust handoff/memory blindly when loops detected
- Use shotgun debugging (random changes)
- Ignore loop symptoms and continue


## Related


---

<small>Source: `.claude/rules/failure-recovery.md`</small>
