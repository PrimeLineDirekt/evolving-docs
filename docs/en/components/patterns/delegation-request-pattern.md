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




## Architecture




## Usage


### Examples

#### Example



**Code:**
```bash
┌─────────────────────────────────────────────────────────┐
│                    LAYER 1 (Orchestrator)               │
│                                                         │
│  Empfängt Request → Validiert → Erstellt Tasks → Führt │
│  aus → Sammelt Ergebnisse → Gibt zurück an User        │
└───────────────────────┬─────────────────────────────────┘
                        │
                        │ Delegation-Request (JSON)
                        │
┌───────────────────────┴─────────────────────────────────┐
│                    LAYER 2 (Sub-Agent)                  │
│                                                         │
│  Analysiert Task → Erkennt Komplexität → Empfiehlt     │
│  weitere Agents via Delegation-Request                  │
└─────────────────────────────────────────────────────────┘
```


#### Example



**Code:**
```json
{
  "delegation_request": true,
  "reason": "Kurze Begründung für die Empfehlung",
  "recommended_tasks": [
    {
      "subject": "Prägnante Task-Beschreibung",
      "description": "Detaillierte Beschreibung (optional)",
      "model": "haiku | sonnet",
      "agent": "Explore | debugger | general-purpose | Plan",
      "traits": ["expertise", "personality", "approach"],
      "blockedBy": ["Subject eines anderen Tasks"],
      "expected_outcome": "Was soll der Task liefern"
    }
  ],
  "coordination_notes": "Optionale Hinweise für Layer 1"
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
  "reason": "Refactoring betrifft 3 Module mit klaren Dependencies",
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
  "reason": "3 unabhängige Research-Bereiche",
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




## Related



---

<small>Source: `knowledge/patterns/delegation-request-pattern.md`</small>
