---
title: multi-agent-orchestration
type: pattern
tags: ["[multi-agent", " orchestration", " n8n", " langgraph", " performance", " scalability", " resilient]"]
lang: en
confidence: 100
---

# multi-agent-orchestration


## Overview

<div class="component-meta" markdown>
| Attribute | Value |
|-----------|-------|
| **Type** | Pattern |
| **Purpose** | Component description |
| **Complexity** | medium |
| **Model** | sonnet |
| **Category** | patterns || **Created** | 2024-11-22 |</div>

<div class="component-tags">
<span class="tag tag-[multi-agent">[multi-agent</span>
<span class="tag tag--orchestration"> orchestration</span>
<span class="tag tag--n8n"> n8n</span>
<span class="tag tag--langgraph"> langgraph</span>
<span class="tag tag--performance"> performance</span>
<span class="tag tag--scalability"> scalability</span>
<span class="tag tag--resilient]"> resilient]</span>
</div>

## What It Does




## System Impact




## Architecture




## Usage


### Examples

#### Example



**Code:**
```bash
┌─────────────────────────────┐
│   Master Orchestrator       │
│   (Koordination + Routing)  │
└──────────┬──────────────────┘
           │
    ┌──────┴────────┬──────────────┬──────────────┐
    │               │              │              │
┌───▼────┐    ┌────▼───┐    ┌────▼───┐    ┌────▼───┐
│Agent 1 │    │Agent 2 │    │Agent 3 │... │Agent N │
│Steuer  │    │Familie │    │Logistik│    │Report  │
└────┬───┘    └────┬───┘    └────┬───┘    └────┬───┘
     │             │              │              │
     └─────────────┴──────────────┴──────────────┘
                   │
            ┌──────▼───────┐
            │  Aggregation  │
            │    & Report   │
            └──────────────┘
```


#### Example



**Code:**
```javascript
if (profile.hasChildren) {
  agents.push('familie-kinder')
}

if (profile.hasPets) {
  agents.push('tierverlagerung')
}

if (profile.isEntrepreneur) {
  agents.push('unternehmens-verlagerung')
}

// Result: 8-15 agents per user (not 29)
```


#### Example



**Code:**
```bash
Auswanderung →
  - Steuerliche Aspekte
  - Finanzplanung
  - Logistik (Umzug, Versand)
  - Familie (Kinder, Schule)
  - Rechtliches (Verträge, Versicherung)
  - Integration (Sprache, Kultur)
```


#### Example



**Code:**
```markdown
# Agent: {Name}

## Identity
Du bist ein {Domain} Experte mit {Credentials}

## Input
- User Profile (126 Felder)
- Dependencies von: {Other Agents}

## Output Format
Strukturiert (JSON/Markdown):
- EXECUTIVE SUMMARY
- DETAILLIERTE ANALYSE
- ACTION ITEMS
- DEPENDENCIES (für andere Agents)

## Quality Criteria
- Mindestens 3 konkrete Action Items
- Alle kritischen Punkte adressiert
- Keine Widersprüche mit Dependencies
```


#### Example



**Code:**
```bash
Agent: Krankenversicherung
Dependencies:
  - Profil-Analyse (Familiensituation)
  - Steueroptimierung (Ansässigkeits-Status)

Output für:
  - Reporter (Health Section)
  - Finanzplanung (Insurance Costs)
```


#### Example



**Code:**
```javascript
// 1. Profile Analysis
const relevantAgents = selectAgents(profile)

// 2. Dependency Graph
const graph = buildDependencyGraph(relevantAgents)

// 3. Parallel Batches
const batches = [
  [agents with no dependencies],
  [agents depending on batch 1],
  ...
]

// 4. Execute
for (const batch of batches) {
  await Promise.all(batch.map(agent => execute(agent)))
}

// 5. Aggregate
const report = await reporter.aggregate(allOutputs)
```


#### Example



**Code:**
```javascript
try {
  output = await agent.execute()
} catch (error) {
  // Fallback to simpler agent or graceful degradation
  output = await fallbackAgent.execute()

  // Log for review
  logAgentFailure(agent, error)
}
```


#### Example



**Code:**
```bash
Webhook Trigger →
  Profile Parse →
    Conditional Branches (if hasChildren, if hasPets) →
      Parallel Agent Execution →
        Aggregation →
          Reporter →
            Response
```


#### Example



**Code:**
```bash
Sub-Agent: "Der DBA-Artikel 5 Abs. 2 lit. a findet Anwendung..."
     ↓
Supervisor (paraphrasiert): "Es gibt steuerliche Regelungen..."
     ↓
User erhält: Vereinfachte, unpräzise Antwort
```


#### Example



**Code:**
```python
def forward_message(message: str, to_user: bool = True) -> dict:
    """
    Forward sub-agent response directly to user without supervisor synthesis.

    Use when:
    - Sub-agent response is final and complete
    - Supervisor synthesis would lose important details
    - Response format must be preserved exactly
    """
    if to_user:
        return {"type": "direct_response", "content": message}
    return {"type": "supervisor_input", "content": message}
```


#### Example



**Code:**
```python
# In Agent-Output-Handling
if agent.output.is_final and not needs_aggregation:
    return forward_message(agent.output.content, to_user=True)
else:
    return {"type": "supervisor_input", "content": agent.output.summary}
```


#### Example



**Code:**
```python
# Checkpoint-based Crash Recovery
class ResilientOrchestrator:
    def run_with_checkpoints(self, profile):
        # Checkpoint after each phase
        self.save_checkpoint("agent_selection", selected_agents)
        self.save_checkpoint("batch_1_complete", batch_1_results)
        # ...

        # On crash: Resume from last checkpoint
        if self.has_checkpoint():
            return self.resume_from_checkpoint()
```


#### Example



**Code:**
```python
score = 20  # Base
if income > 120k: score += 15
if net_worth > 500k: score += 20
if has_business: score += 15
score += num_children * 5
if age > 60: score += 10
# ... max 100
```


#### Example



**Code:**
```bash
🟢 GRÜN (Sicher) - Standard-Verfahren, etabliert
🟡 GELB (Moderat) - Legal aber nicht Standard, Dokumentation nötig
🟠 ORANGE (Aggressiv) - Am Limit, Expertenberatung zwingend
❌ VERBOTEN - Niemals empfehlen
```


#### Example



**Code:**
```bash
confidence = base_score × aktualität × konsistenz + vollständigkeit_bonus

KB-Quellen:
- Primary (Tier 1): 1.0 Basisfaktor
- Secondary (Tier 2): 0.8 Basisfaktor
- Tertiary (Tier 3): 0.6 Basisfaktor

Thresholds:
- < 0.50: Nicht publishen
- < 0.75: HITL Review
- ≥ 0.85: Premium Quality
```




## Configuration



## Best Practices




## Related



---

<small>Source: `knowledge/patterns/multi-agent-orchestration.md`</small>
