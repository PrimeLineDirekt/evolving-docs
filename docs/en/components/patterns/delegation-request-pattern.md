---
title: delegation-request-pattern
type: pattern
tags: []
lang: en
confidence: 100
---

# delegation-request-pattern


## Overview

<div class="component-meta" markdown>
| Attribute | Value |
|-----------|-------|
| **Type** | Pattern |
| **Purpose** | Component description |
| **Complexity** | medium |
| **Model** | sonnet |
| **Category** | patterns |</div>


## What It Does




## System Impact

**Capabilities Provided:**
- Structured approach to component creation
- Automated validation and best practices
- Standardized output format
- Integration with system architecture

**When to Use:**
- Creating new system components
- Standardizing component structure
- Ensuring consistency across codebase
- Automating repetitive creation tasks



## Architecture




## Usage


### Examples

#### Example



**Code:**
```bash
┌─────────────────────────────────────────────────────────┐
│                    LAYER 1 (Orchestrator)               │
│                                                         │
│  Receives request → Validates → Creates tasks → Executes │
│  → Collects results → Returns to user        │
└───────────────────────┬─────────────────────────────────┘
                        │
                        │ Delegation-Request (JSON)
                        │
┌───────────────────────┴─────────────────────────────────┐
│                    LAYER 2 (Sub-Agent)                  │
│                                                         │
│  Analyzes task → Detects complexity → Recommends     │
│  additional agents via delegation-request                  │
└─────────────────────────────────────────────────────────┘
```


#### Example



**Code:**
```json
{
  "delegation_request": true,
  "reason": "Brief rationale for the recommendation",
  "recommended_tasks": [
    {
      "subject": "Concise task description",
      "description": "Detailed description (optional)",
      "model": "haiku | sonnet",
      "agent": "Explore | debugger | general-purpose | Plan",
      "traits": ["expertise", "personality", "approach"],
      "blockedBy": ["Subject eines anderen Tasks"],
      "expected_outcome": "Expected task output"
    }
  ],
  "coordination_notes": "Optional notes for Layer 1"
}
```


#### Example



**Code:**
```bash
Delegation-Request empfangen
         │
         ▼
┌────────────────────────────────┐
│ 1. VALIDIERUNG                 │
│                                │
│ • Alle required Felder da?     │
│ • Models valide (haiku/sonnet)?│
│ • Agents existieren?           │
│ • blockedBy referenziert       │
│   existierende Tasks?          │
└──────────────┬─────────────────┘
               │
               ▼
┌────────────────────────────────┐
│ 2. TASK CREATION               │
│                                │
│ FOR each recommended_task:     │
│   TaskCreate(subject, desc)    │
│   → Speichere Task-ID          │
└──────────────┬─────────────────┘
               │
               ▼
┌────────────────────────────────┐
│ 3. DEPENDENCIES SETZEN         │
│                                │
│ FOR each task with blockedBy:  │
│   TaskUpdate(id, addBlockedBy) │
│   → Mapping: subject → ID      │
└──────────────┬─────────────────┘
               │
               ▼
┌────────────────────────────────┐
│ 4. PARALLEL EXECUTION          │
│                                │
│ Gruppiere Tasks:               │
│ • Gruppe 0: Keine blockedBy    │
│ • Gruppe 1: blockedBy Gruppe 0 │
│ • Gruppe 2: blockedBy Gruppe 1 │
│                                │
│ Führe Gruppen sequentiell aus, │
│ Tasks innerhalb parallel       │
└──────────────┬─────────────────┘
               │
               ▼
┌────────────────────────────────┐
│ 5. RESULT AGGREGATION          │
│                                │
│ Sammle alle Task-Ergebnisse    │
│ Formatiere für User            │
└────────────────────────────────┘
```


#### Example



**Code:**
```json
{
  "delegation_request": true,
  "reason": "Refactoring affects 3 Module with clear dependencies",
  "recommended_tasks": [
    {
      "subject": "Types refactoren",
      "model": "sonnet",
      "agent": "general-purpose",
      "traits": ["engineer", "precise"],
      "blockedBy": [],
      "expected_outcome": "Neue Type-Definitionen"
    },
    {
      "subject": "Auth-Service refactoren",
      "model": "sonnet",
      "agent": "general-purpose",
      "traits": ["engineer", "iterative"],
      "blockedBy": ["Types refactoren"],
      "expected_outcome": "Aktualisierter Auth-Service"
    },
    {
      "subject": "API-Layer refactoren",
      "model": "sonnet",
      "agent": "general-purpose",
      "traits": ["engineer", "iterative"],
      "blockedBy": ["Types refactoren"],
      "expected_outcome": "Aktualisierte API-Endpoints"
    },
    {
      "subject": "Integration Tests",
      "model": "haiku",
      "agent": "general-purpose",
      "blockedBy": ["Auth-Service refactoren", "API-Layer refactoren"],
      "expected_outcome": "Passing Tests"
    }
  ],
  "coordination_notes": "Auth und API können parallel nach Types"
}
```


#### Example



**Code:**
```json
{
  "delegation_request": true,
  "reason": "3 independent Research-Bereiche",
  "recommended_tasks": [
    {
      "subject": "API Documentation recherchieren",
      "model": "haiku",
      "agent": "Explore",
      "blockedBy": []
    },
    {
      "subject": "Existing Patterns analysieren",
      "model": "haiku",
      "agent": "Explore",
      "blockedBy": []
    },
    {
      "subject": "Best Practices sammeln",
      "model": "haiku",
      "agent": "general-purpose",
      "traits": ["researcher", "thorough"],
      "blockedBy": []
    },
    {
      "subject": "Synthese erstellen",
      "model": "sonnet",
      "agent": "general-purpose",
      "traits": ["analyst", "systematic"],
      "blockedBy": [
        "API Documentation recherchieren",
        "Existing Patterns analysieren",
        "Best Practices sammeln"
      ]
    }
  ]
}
```




## Configuration



## Best Practices

**Do:**
- Use for multi-expert coordination requiring diverse perspectives
- Apply when problem benefits from iterative refinement
- Combine with proper state management and validation
- Monitor blackboard size to prevent context overflow

**Don't:**
- Use for simple single-agent tasks
- Apply to strictly sequential workflows
- Ignore controller bottleneck risks
- Forget to handle write conflicts in concurrent scenarios




## Related


---

<small>Source: `knowledge/patterns/delegation-request-pattern.md`</small>
