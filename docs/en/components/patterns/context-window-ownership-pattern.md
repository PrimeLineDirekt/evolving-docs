---
title: context-window-ownership-pattern
type: pattern
tags: []
lang: en
confidence: 100
---

# context-window-ownership-pattern


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

Standard LLM Message-Formate (OpenAI-Style `role: user/assistant/system`) sind:

- Token-ineffizient (viel Overhead)
- Nicht optimiert für spezifische Use Cases
- Starr und unflexibel
- Keine Kontrolle über Information Density

**Solution**: **Aktive Context-Kontrolle**: Statt Standard-Formate zu akzeptieren, Context explizit für den spezifischen Use Case strukturieren.

```
┌─────────────────────────────────────┐
│         Context Components          │
├─────────────────────────────────────┤
│  • System Prompts & Instructions    │
│  • Retrieved Data (RAG)             │
│  • Historical State & Tool Results  │
│  • Memory (Past Conversations)      │
│  • Structured Output Specs          │
└─────────────────────────────────────┘
                 │
                 ▼
┌─────────────────────────────────────┐
│    Custom Context Engineering       │
│  ┌─────────────────────────────┐   │
│  │  Transform to Optimal Format │   │
│  │  (XML, YAML, Compact JSON)   │   │
│  └─────────────────────────────┘   │
└─────────────────────────────────────┘
                 │
                 ▼
┌─────────────────────────────────────┐
│         LLM Processing              │
│   (Stateless: Input → Output)       │
└─────────────────────────────────────┘
```

**Core Principle**: "Everything is context engineering. LLMs are stateless functions that turn inputs into outputs."



## System Impact

**When to Apply:**
- **YES**: Multi-Turn Agents, RAG Systems, Tool-Heavy Workflows
- **NO**: Simple Single-Turn Calls, Bereits optimierte Pipelines

**Integration Points:**
- Can be combined with multi-agent orchestration patterns
- Integrates with task coordination systems
- Requires proper state management




## Architecture

**Key Components:**

```
from typing import Literal, Union, List
from dataclasses import dataclass

@dataclass
class Event:
    """Single event in the context thread."""
    type: str  # e.g., "user_query", "tool_result", "error"
    data: Union[dict, str]

@dataclass
class Thread:
    """Complete context thread."""
    events: List[Event]


def event_to_prompt(event: Event) -> str:
    """Convert event to XML-tagged prompt section."""
    if isinstance(event.data, dict):
        # YAML for structured data (more token-efficient than JSON)
        import yaml
        data_str = yaml.dump(event.data, default_flow_style=False)
    else:
        data_str = str(event.data)

    return f"<{event.type}>\n{data_str}</{event.type}>"


def thread_to_prompt(thread: Thread) -> str:
    """Convert entire thread to LLM prompt."""
    return '\n\n'.join(
        event_to_prompt(event) for event in thread.events
    )
```

**Data Flow:**
1. Controller analyzes current state
2. Selects appropriate agent based on context
3. Agent processes and contributes to shared state
4. Iterate until completion criteria met




## Usage


### Examples

#### Example



**Code:**
```bash
┌─────────────────────────────────────┐
│         Context Components          │
├─────────────────────────────────────┤
│  • System Prompts & Instructions    │
│  • Retrieved Data (RAG)             │
│  • Historical State & Tool Results  │
│  • Memory (Past Conversations)      │
│  • Structured Output Specs          │
└─────────────────────────────────────┘
                 │
                 ▼
┌─────────────────────────────────────┐
│    Custom Context Engineering       │
│  ┌─────────────────────────────┐   │
│  │  Transform to Optimal Format │   │
│  │  (XML, YAML, Compact JSON)   │   │
│  └─────────────────────────────┘   │
└─────────────────────────────────────┘
                 │
                 ▼
┌─────────────────────────────────────┐
│         LLM Processing              │
│   (Stateless: Input → Output)       │
└─────────────────────────────────────┘
```


#### Example



**Code:**
```python
from typing import Literal, Union, List
from dataclasses import dataclass

@dataclass
class Event:
    """Single event in the context thread."""
    type: str  # e.g., "user_query", "tool_result", "error"
    data: Union[dict, str]

@dataclass
class Thread:
    """Complete context thread."""
    events: List[Event]


def event_to_prompt(event: Event) -> str:
    """Convert event to XML-tagged prompt section."""
    if isinstance(event.data, dict):
        # YAML for structured data (more token-efficient than JSON)
        import yaml
        data_str = yaml.dump(event.data, default_flow_style=False)
    else:
        data_str = str(event.data)

    return f"<{event.type}>\n{data_str}</{event.type}>"


def thread_to_prompt(thread: Thread) -> str:
    """Convert entire thread to LLM prompt."""
    return '\n\n'.join(
        event_to_prompt(event) for event in thread.events
    )
```


#### Example



**Code:**
```json
{
  "messages": [
    {"role": "system", "content": "You are a deployment assistant..."},
    {"role": "user", "content": "Deploy the latest backend"},
    {"role": "assistant", "content": null, "tool_calls": [...]},
    {"role": "tool", "tool_call_id": "...", "content": "{\"tags\": [...]}"}
  ]
}
```


#### Example



**Code:**
```xml
<slack_message>
From: @alex
Channel: #deployments
Text: Can you deploy the latest backend?
</slack_message>

<list_git_tags_result>
tags:
  - name: v1.2.3
    commit: abc123
    date: 2024-03-15
</list_git_tags_result>

<deploy_backend>
intent: deploy_backend
tag: v1.2.3
</deploy_backend>
```


#### Example



**Code:**
```python
class ContextBuilder:
    """Builds optimized context for LLM calls."""

    def __init__(self, max_tokens: int = 8000):
        self.max_tokens = max_tokens
        self.events: List[Event] = []

    def add_system_context(self, instructions: str) -> 'ContextBuilder':
        """Add system instructions."""
        self.events.insert(0, Event(
            type="system",
            data=instructions
        ))
        return self

    def add_user_input(self, input_data: dict) -> 'ContextBuilder':
        """Add user input with relevant metadata."""
        self.events.append(Event(
            type="user_input",
            data=input_data
        ))
        return self

    def add_tool_result(self, tool_name: str, result: dict) -> 'ContextBuilder':
        """Add tool execution result."""
        self.events.append(Event(
            type=f"{tool_name}_result",
            data=result
        ))
        return self

    def add_retrieved_context(self, docs: List[str], source: str) -> 'ContextBuilder':
        """Add RAG-retrieved documents."""
        self.events.append(Event(
            type=f"retrieved_{source}",
            data={"documents": docs}
        ))
        return self

    def build(self) -> str:
        """Build final context string."""
        return thread_to_prompt(Thread(events=self.events))

    def build_with_truncation(self) -> str:
        """Build with intelligent truncation if needed."""
        full_context = self.build()

        # Simple token estimation (4 chars ≈ 1 token)
        estimated_tokens = len(full_context) // 4

        if estimated_tokens <= self.max_tokens:
            return full_context

        # Truncate older events (keep system + recent)
        system_events = [e for e in self.events if e.type == "system"]
        other_events = [e for e in self.events if e.type != "system"]

        # Keep most recent events
        while estimated_tokens > self.max_tokens and len(other_events) > 1:
            other_events.pop(0)  # Remove oldest
            truncated = Thread(events=system_events + other_events)
            estimated_tokens = len(thread_to_prompt(truncated)) // 4

        return thread_to_prompt(Thread(events=system_events + other_events))
```


#### Example



**Code:**
```python
# In resilient_orchestrator.py
context = (
    ContextBuilder(max_tokens=6000)
    .add_system_context(agent.system_prompt)
    .add_user_input({"profile": profile.summary, "query": query})
    .add_retrieved_context(kb_results, source="tax_knowledge")
    .build()
)
```


#### Example



**Code:**
```bash
┌─────────┐    ┌──────────┐    ┌──────────┐    ┌──────────┐
│  WRITE  │ →  │  SELECT  │ →  │ COMPRESS │ →  │ ISOLATE  │
│         │    │          │    │          │    │          │
│ Bessere │    │ Richtige │    │ Weniger  │    │ Saubere  │
│ Inputs  │    │ Auswahl  │    │ Tokens   │    │ Trennung │
└─────────┘    └──────────┘    └──────────┘    └──────────┘
```


#### Example



**Code:**
```bash
┌─────────────────────────────────────────────────┐
│              Total Token Budget                  │
│                (z.B. 100K)                       │
└─────────────────────────────────────────────────┘
                      │
    ┌─────────────────┼─────────────────┐
    │                 │                 │
    ▼                 ▼                 ▼
┌────────┐      ┌──────────┐      ┌──────────┐
│ System │      │ Critical │      │ History  │
│  10%   │      │ Context  │      │   40%    │
│        │      │   15%    │      │          │
└────────┘      └──────────┘      └──────────┘
    │                 │                 │
    ▼                 ▼                 ▼
┌────────┐                        ┌──────────┐
│ Query  │                        │ Response │
│  10%   │                        │   25%    │
└────────┘                        └──────────┘
```


#### Example



**Code:**
```python
def allocate_budget(total_tokens: int) -> dict:
    """
    Allocate token budget across context components.
    Based on empirical testing with Claude and GPT models.
    """
    return {
        "system": int(total_tokens * 0.10),           # 10%
        "critical_context": int(total_tokens * 0.15), # 15%
        "history": int(total_tokens * 0.40),          # 40%
        "query": int(total_tokens * 0.10),            # 10%
        "response": int(total_tokens * 0.25),         # 25%
    }

# Example: 100K model
budget = allocate_budget(100_000)
# → system: 10K, critical: 15K, history: 40K, query: 10K, response: 25K
```


#### Example



**Code:**
```python
used = sum([system_tokens, critical_tokens, query_tokens])
remaining = total_tokens - used - budget["response"]

if remaining > 0:
    # Extra zu History (most valuable for conversation)
    budget["history"] += remaining
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

<small>Source: `knowledge/patterns/context-window-ownership-pattern.md`</small>
