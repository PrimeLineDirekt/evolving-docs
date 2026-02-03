---
title: Plan Execution Workflow
type: rule
tags: []
lang: en
confidence: 100
---

# Plan Execution Workflow


## Overview

<div class="component-meta" markdown>
| Attribute | Value |
|-----------|-------|
| **Type** | Rule |
| **Purpose** | Mandatory interview before plan execution for validation |
| **Complexity** | medium |
| **Model** | sonnet |
| **Category** | rules |</div>


## What It Does

When a user approves a plan (Option 2 at ExitPlanMode), this rule mandates automatically starting a plan interview before execution. The interview identifies gaps, validates hints, checks phase boundaries, and suggests review tasks. After interview completion, the user chooses whether to clear context before execution. This prevents discovering critical issues mid-execution and ensures plans are complete before work begins.


## System Impact

**When It Triggers:**
User selects Option 2 ("Yes - continue") at ExitPlanMode

**Behavior Enforced:**
- Automatically start `/interview-plan {plan-path}` without asking
- Interview validates: gaps, delegation hints, phase boundaries, review tasks
- Suggest hint additions for tasks missing them
- Auto-generate phase boundaries if absent
- Present execution options after interview (clear context or proceed)
- Context-aware recommendation (>50% = suggest clear)

**Integration Points:**
- ExitPlanMode (plan approval)
- /interview-plan command
- Plan execution enforcement
- Context monitoring


## Architecture

**Trigger:** ExitPlanMode → User Option 2

**Dependencies:**
- /interview-plan command
- Plan file
- Context monitoring

**Workflow:**
1. **Plan Approval**: User chooses Option 2
2. **Auto-Interview**: Start interview automatically
3. **Validation**: Gaps, hints, boundaries, reviews
4. **Finalization**: Add missing components
5. **Execution Options**: Clear context or proceed
6. **Execute**: Start plan execution


## Usage

**Standard Flow:**
```
[ExitPlanMode]
Options: 1=Revise, 2=Continue, 3=Cancel

User: "2"

Claude: "Plan approved. Starting interview for finalization..."
[Runs /interview-plan automatically]

Claude: "Question 1: Tasks 2.1 and 3.2 lack delegation hints.
         Recommend: [DELEGATE] for both. Add them?"

User: "Yes"

Claude: "Question 2: Phase 2 has no review task.
         Add 'Task 2.Y: Phase 2 Review [DELEGATE:code-reviewer]'?"

User: "Yes"

Claude: "Interview complete. Plan finalized.
         Context usage: 62%
         
         Execution options:
         1. Clear Context + Execute (recommended)
         2. Execute without Clear"

User: "1"

[/clear executed, then plan execution starts]
```

**Skip Interview:**
- User says "skip interview" or "direct execution"
- Plan has "Reviewed: true" marker
- Plan is trivial (<3 tasks, no phases)


## Configuration

| Setting | Value | Description |
|---------|-------|-------------|
| Trigger | ExitPlanMode Option 2 | Automatic interview start |
| Interview Command | /interview-plan | Used for validation |
| Context Threshold (Recommend Clear) | >50% | Suggest context clear |
| Context Threshold (Mandatory Clear) | >85% | Require clear before execution |
| Skip Conditions | "skip interview", trivial plan, already reviewed | When to bypass |


## Best Practices

**Do:**
- Always run interview before execution (unless skip conditions)
- Validate all delegation hints during interview
- Generate phase boundaries if missing
- Add review tasks to each phase
- Recommend context clear when >50%
- Present clear execution options after interview

**Don't:**
- Skip interview without valid reason
- Execute without finalizing plan
- Ignore missing hints or review tasks
- Proceed with >85% context without clearing
- Ask user about interview (just start it automatically)


## Related


---

<small>Source: `.claude/rules/plan-execution-workflow.md`</small>
