---
title: pkm-digital-brain-pattern
type: pattern
tags: []
lang: en
confidence: 100
---

# pkm-digital-brain-pattern


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
┌─────────────────────────────────────────────────────────────┐
│                    DIGITAL BRAIN                             │
├─────────────────────────────────────────────────────────────┤
│                                                              │
│  ┌──────────┐  ┌──────────┐  ┌──────────┐  ┌──────────┐    │
│  │ IDENTITY │  │ CONTENT  │  │ KNOWLEDGE│  │ NETWORK  │    │
│  │          │  │          │  │          │  │          │    │
│  │ voice    │  │ ideas    │  │ bookmarks│  │ contacts │    │
│  │ brand    │  │ posts    │  │ research │  │ circles  │    │
│  │ values   │  │ calendar │  │ learning │  │ intros   │    │
│  └──────────┘  └──────────┘  └──────────┘  └──────────┘    │
│                                                              │
│  ┌──────────────────────────────────────┐                  │
│  │            OPERATIONS                 │                  │
│  │  todos | goals | meetings | metrics   │                  │
│  └──────────────────────────────────────┘                  │
│                                                              │
└─────────────────────────────────────────────────────────────┘
```


#### Example



**Code:**
```bash
ideas.jsonl → drafts/ → posts.jsonl
     ↓           ↓           ↓
  Capture    Develop      Log + Metrics
```


#### Example



**Code:**
```bash
SCHLECHT (Deletion):
- Verliert History
- Keine Pattern-Analyse möglich
- "Was funktioniert hat" nicht nachvollziehbar
- AI-Fehler permanent

GUT (Append-Only):
- History preserved
- "What worked" Retrospectives möglich
- Pattern-Analyse über Zeit
- AI-Fehler reversibel via Archive-Status
```


#### Example



**Code:**
```json
// Statt: Eintrag löschen
// Setze: status: "archived"

{"id": "idea_001", "status": "active", "content": "..."}
{"id": "idea_001", "status": "archived", "archived_at": "2026-01-01"}
```


#### Example



**Code:**
```json
{
  "id": "idea_YYYYMMDD_HHMMSS",
  "created": "ISO8601",
  "updated": "ISO8601",
  "status": "raw|developing|ready|published|archived",
  "content": "The idea text",
  "pillar": "ai_agents|content|personal",
  "format": "thread|post|newsletter|video",
  "source": "How you got the idea",
  "notes": "Development notes",
  "developed_to": "post_id if published"
}
```


#### Example



**Code:**
```yaml
circles:
  inner:
    description: "Close relationships - friends, advisors, confidants"
    touchpoint_frequency: "weekly"

  active:
    description: "Current collaborators, frequent interaction"
    touchpoint_frequency: "bi-weekly"

  network:
    description: "Known contacts, periodic touchpoints"
    touchpoint_frequency: "monthly"

  dormant:
    description: "Historical connections, may reactivate"
    touchpoint_frequency: "quarterly check-in"
```


#### Example



**Code:**
```python
# agents/scripts/stale_contacts.py
def find_stale_contacts(contacts: List[Contact]) -> List[Contact]:
    stale = []
    for contact in contacts:
        days_since = (now - contact.last_contact).days
        threshold = CIRCLE_THRESHOLDS[contact.circle]
        if days_since > threshold:
            stale.append(contact)
    return sorted(stale, key=lambda c: c.circle)  # inner first
```


#### Example



**Code:**
```bash
User: "Write a X post about AI agents"
           │
           ▼
┌─────────────────────────────────┐
│ L1: SKILL.md (bereits geladen)  │
│ → Erkenne: Content Creation     │
└─────────────────────────────────┘
           │
           ▼
┌─────────────────────────────────┐
│ L2: identity/IDENTITY.md        │
│     content/CONTENT.md          │
│ → Module Instructions           │
└─────────────────────────────────┘
           │
           ▼
┌─────────────────────────────────┐
│ L3: identity/voice.md (FIRST!)  │
│     identity/brand.md           │
│     content/posts.jsonl (recent)│
│ → Actual Data                   │
└─────────────────────────────────┘
           │
           ▼
┌─────────────────────────────────┐
│ Generate post with voice        │
└─────────────────────────────────┘
```


#### Example



**Code:**
```bash
Daten-Typ
    │
    ├─ Wächst über Zeit? → JSONL (append-only)
    │     (ideas, posts, contacts, interactions)
    │
    ├─ Hierarchische Struktur? → YAML
    │     (goals, values, circles, learning)
    │
    ├─ Narrative/Editierbar? → Markdown
    │     (voice, brand, todos, calendar)
    │
    └─ Komplexe Prompts? → XML
          (generation templates)
```


#### Example



**Code:**
```bash
1. Read identity/voice.md (REQUIRED!)
2. Check identity/brand.md for topic alignment
3. Reference content/posts.jsonl for successful patterns
4. Use content/templates/ as starting structure
5. Draft matching voice attributes
6. Log to posts.jsonl after publishing
```


#### Example



**Code:**
```bash
1. Look up contact: network/contacts.jsonl
2. Get history: network/interactions.jsonl
3. Check pending: operations/todos.md
4. Generate brief with context
```


#### Example



**Code:**
```bash
1. Run: python agents/scripts/weekly_review.py
2. Review metrics in operations/metrics.jsonl
3. Check stale contacts: agents/scripts/stale_contacts.py
4. Update goals progress in operations/goals.yaml
5. Plan next week in content/calendar.md
```


#### Example



**Code:**
```bash
Evolving/
├── network/                 # NEU: Personal CRM
│   ├── contacts.jsonl
│   ├── interactions.jsonl
│   └── circles.yaml
```




## Configuration



## Best Practices




## Related



---

<small>Source: `knowledge/patterns/pkm-digital-brain-pattern.md`</small>
