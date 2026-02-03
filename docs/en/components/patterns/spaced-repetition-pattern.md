---
title: spaced-repetition-pattern
type: pattern
tags: []
lang: en
confidence: 100
---

# spaced-repetition-pattern


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
```json
{
  "review": {
    "next_review": "2026-02-08T00:00:00Z",
    "interval_days": 7,
    "review_count": 0,
    "last_result": null
  }
}
```


#### Example



**Code:**
```python
def calculate_next_review(current_interval: float, result: str) -> float:
    """
    Berechnet das nächste Review-Intervall basierend auf dem Ergebnis.

    Args:
        current_interval: Aktuelles Intervall in Tagen
        result: 'success' | 'practice' | 'failure' | 'skipped'

    Returns:
        Neues Intervall in Tagen
    """
    if result == 'success':
        # Exponentielles Wachstum bei vollständigem Recall
        new_interval = min(current_interval * 2.5, 90)
    elif result == 'practice':
        # Moderates Wachstum bei aktivem Wiederholen
        # User kennt das Konzept, will es aber festigen
        new_interval = min(current_interval * 2.0, 90)
    elif result == 'failure':
        # Halbierung bei Vergessen
        new_interval = max(current_interval / 2, 1)
    else:  # skipped
        # Leichte Reduktion bei Überspringen ohne Versuch
        new_interval = max(current_interval * 0.8, 1)

    return round(new_interval, 1)
```


#### Example



**Code:**
```python
def calculate_priority(item: dict, now: datetime) -> float:
    """
    Berechnet Review-Priorität für Sortierung.

    Höhere Priorität = dringender
    """
    review = item.get('review', {})
    next_review = datetime.fromisoformat(review.get('next_review', now.isoformat()))

    # Tage überfällig (negativ = noch nicht fällig)
    overdue_days = (now - next_review).days

    # Trust/Relevance berücksichtigen
    trust = item.get('scoring', {}).get('trust_level', 0.5)
    relevance = item.get('scoring', {}).get('relevance_score', 50) / 100

    # Priority-Formel
    priority = overdue_days * trust * relevance

    return priority
```


#### Example



**Code:**
```bash
Domain Memory Bootup
       │
       ▼
  Context-Scout
       │
       ▼
┌──────────────────────────────────┐
│ SPACED REP CHECK                 │
│                                  │
│ 1. Sammle due Items:             │
│    - Experiences (next_review)   │
│    - Staged Rules (trial)        │
│    - Explorations (optional)     │
│                                  │
│ 2. Sortiere nach Priority        │
│                                  │
│ 3. Zeige Top 3:                  │
│    "📚 Review-Check (3 fällig):  │
│     1. [EXP] Supabase RLS        │
│     2. [RULE] Advanced Debug     │
│     3. [EXPLORE] Hook-System"    │
│                                  │
│ 4. User-Aktion:                  │
│    confirm / practice /          │
│    skip / skip-all               │
└──────────────────────────────────┘
```


#### Example



**Code:**
```python
#!/usr/bin/env python3
"""
scripts/spaced-rep-collector.py
Collects due items for Spaced Repetition Review.
"""
import json
from datetime import datetime
from pathlib import Path
from typing import List, Dict, Any

def get_due_items(base_path: Path) -> List[Dict[str, Any]]:
    """Collect all items due for review."""
    now = datetime.now()
    due = []

    # 1. Experiences
    exp_path = base_path / "_memory/experiences"
    for exp_file in exp_path.glob("exp-*.json"):
        try:
            exp = json.loads(exp_file.read_text())
            if is_due(exp, now):
                due.append({
                    "type": "experience",
                    "id": exp.get("id"),
                    "summary": exp.get("summary"),
                    "priority": calculate_priority(exp, now),
                    "file": str(exp_file)
                })
        except (json.JSONDecodeError, KeyError):
            continue

    # 2. Staged Rules (trial status only)
    rules_index = base_path / "knowledge/rules/staging/_index.json"
    if rules_index.exists():
        try:
            index = json.loads(rules_index.read_text())
            for rule in index.get("rules", []):
                if rule.get("status") == "trial" and is_due(rule, now):
                    due.append({
                        "type": "rule",
                        "id": rule.get("id"),
                        "summary": rule.get("title"),
                        "priority": calculate_priority(rule, now),
                        "file": f"knowledge/rules/staging/{rule.get('id')}.md"
                    })
        except (json.JSONDecodeError, KeyError):
            pass

    # 3. Explorations (optional, lower priority)
    exp_index = base_path / "knowledge/explorations/_index.json"
    if exp_index.exists():
        try:
            index = json.loads(exp_index.read_text())
            for entry in index.get("entries", []):
                if is_due(entry, now):
                    due.append({
                        "type": "exploration",
                        "id": entry.get("timestamp"),
                        "summary": entry.get("task", "")[:50] + "...",
                        "priority": calculate_priority(entry, now) * 0.5,  # Lower priority
                        "file": entry.get("file")
                    })
        except (json.JSONDecodeError, KeyError):
            pass

    # Sort by priority (highest first), return top 3
    due.sort(key=lambda x: x["priority"], reverse=True)
    return due[:3]


def is_due(item: dict, now: datetime) -> bool:
    """Check if item is due for review."""
    review = item.get("review", {})
    next_review = review.get("next_review")

    if not next_review:
        return False

    try:
        review_date = datetime.fromisoformat(next_review.replace('Z', '+00:00'))
        return review_date.replace(tzinfo=None) <= now
    except (ValueError, TypeError):
        return False


def calculate_priority(item: dict, now: datetime) -> float:
    """Calculate review priority."""
    review = item.get("review", {})
    next_review = review.get("next_review")

    if not next_review:
        return 0.0

    try:
        review_date = datetime.fromisoformat(next_review.replace('Z', '+00:00'))
        overdue_days = (now - review_date.replace(tzinfo=None)).days
    except (ValueError, TypeError):
        overdue_days = 0

    # Get trust/relevance if available
    scoring = item.get("scoring", {})
    trust = scoring.get("trust_level", 0.5)
    relevance = scoring.get("relevance_score", 50) / 100

    return max(0, overdue_days) * trust * relevance + 1


if __name__ == "__main__":
    import sys
    base = Path(sys.argv[1]) if len(sys.argv) > 1 else Path.cwd()
    print(json.dumps(get_due_items(base), indent=2))
```


#### Example



**Code:**
```python
def update_review(item: dict, result: str) -> dict:
    """
    Aktualisiert Review-Felder nach User-Aktion.

    Args:
        item: Das Experience/Rule/Exploration
        result: 'success' | 'failure' | 'skipped'

    Returns:
        Aktualisiertes Item
    """
    from datetime import datetime, timedelta

    review = item.get('review', {
        'next_review': None,
        'interval_days': 7,
        'review_count': 0,
        'last_result': None
    })

    current_interval = review.get('interval_days', 7)
    new_interval = calculate_next_review(current_interval, result)

    review['interval_days'] = new_interval
    review['next_review'] = (
        datetime.now() + timedelta(days=new_interval)
    ).isoformat() + 'Z'
    review['review_count'] = review.get('review_count', 0) + 1
    review['last_result'] = result

    item['review'] = review
    return item
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

<small>Source: `knowledge/patterns/spaced-repetition-pattern.md`</small>
