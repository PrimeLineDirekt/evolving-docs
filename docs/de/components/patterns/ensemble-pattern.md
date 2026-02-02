---
title: ensemble-pattern
type: pattern
tags: []
lang: en
confidence: 100
---

# ensemble-pattern


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
User Query
    │
    ▼
┌─────────────────┐
│   DISPATCHER    │
│ Verteilt Query  │
│ an Agent Pool   │
└────────┬────────┘
         │
    ┌────┴────┬────────┬────────┐
    ▼         ▼        ▼        ▼
┌───────┐ ┌───────┐ ┌───────┐ ┌───────┐
│Agent 1│ │Agent 2│ │Agent 3│ │Agent N│
│Expert │ │Skeptic│ │Risk   │ │Domain │
└───┬───┘ └───┬───┘ └───┬───┘ └───┬───┘
    │         │        │        │
    └────┬────┴────────┴────────┘
         │
         ▼
┌─────────────────┐
│   AGGREGATOR    │
│ Voting/Konsens  │
│ Conflict Res.   │
└────────┬────────┘
         │
         ▼
┌─────────────────┐
│    DECIDER      │
│ Finale Antwort  │
│ + Confidence    │
└────────┬────────┘
         │
         ▼
   Final Output
```


#### Example



**Code:**
```python
from pydantic import BaseModel, Field
from typing import Optional
from enum import Enum

class VotingStrategy(str, Enum):
    MAJORITY = "majority"
    UNANIMOUS = "unanimous"
    WEIGHTED = "weighted"
    THRESHOLD = "threshold"

class AgentVote(BaseModel):
    agent_id: str
    agent_role: str
    decision: str = Field(description="The agent's decision/answer")
    confidence: float = Field(ge=0, le=1)
    reasoning: str = Field(description="Why this decision")
    concerns: list[str] = Field(default_factory=list)
    weight: float = Field(default=1.0, description="Agent expertise weight")

class EnsembleResult(BaseModel):
    final_decision: str
    consensus_level: float = Field(ge=0, le=1)
    voting_breakdown: dict[str, int]
    dissenting_views: list[str]
    aggregate_confidence: float
    recommendation: str

class ConflictResolution(BaseModel):
    conflict_type: str
    resolution_strategy: str
    additional_agents_needed: bool
    escalate_to_human: bool
```


#### Example



**Code:**
```python
def majority_vote(votes: list[AgentVote]) -> str:
    """Simple majority wins (>50%)."""
    decision_counts = Counter(v.decision for v in votes)
    winner, count = decision_counts.most_common(1)[0]

    if count > len(votes) / 2:
        return winner
    return "NO_CONSENSUS"

def unanimous_vote(votes: list[AgentVote]) -> str:
    """All agents must agree."""
    decisions = set(v.decision for v in votes)

    if len(decisions) == 1:
        return decisions.pop()
    return "NO_CONSENSUS"

def weighted_vote(votes: list[AgentVote]) -> str:
    """Weighted by agent expertise and confidence."""
    weighted_scores = defaultdict(float)

    for vote in votes:
        score = vote.weight * vote.confidence
        weighted_scores[vote.decision] += score

    winner = max(weighted_scores, key=weighted_scores.get)
    total_weight = sum(weighted_scores.values())

    if weighted_scores[winner] / total_weight >= 0.6:
        return winner
    return "NO_CONSENSUS"

def threshold_vote(votes: list[AgentVote], threshold: float = 0.7) -> str:
    """Decision needs minimum confidence threshold."""
    avg_confidence = {}

    for decision in set(v.decision for v in votes):
        relevant_votes = [v for v in votes if v.decision == decision]
        avg_confidence[decision] = sum(v.confidence for v in relevant_votes) / len(relevant_votes)

    for decision, conf in avg_confidence.items():
        if conf >= threshold:
            return decision

    return "BELOW_THRESHOLD"
```


#### Example



**Code:**
```python
from langgraph.graph import StateGraph, START, END
from typing import TypedDict

class EnsembleState(TypedDict):
    query: str
    context: dict
    agent_configs: list[dict]
    votes: list[dict]
    voting_strategy: str
    result: dict
    needs_resolution: bool

def dispatch_node(state: EnsembleState) -> dict:
    """Prepare query for parallel agent execution."""
    return {
        "dispatch_ready": True,
        "agent_count": len(state['agent_configs'])
    }

def create_agent_node(agent_config: dict):
    """Factory for agent evaluation nodes."""

    def agent_node(state: EnsembleState) -> dict:
        prompt = f"""
        You are: {agent_config['role']}
        Perspective: {agent_config['perspective']}

        Query: {state['query']}
        Context: {state['context']}

        Evaluate this from your perspective:
        1. What is your decision/recommendation?
        2. How confident are you? (0-1)
        3. What is your reasoning?
        4. What concerns do you have?
        """

        vote = llm.with_structured_output(AgentVote).invoke(prompt)
        vote.agent_id = agent_config['id']
        vote.agent_role = agent_config['role']
        vote.weight = agent_config.get('weight', 1.0)

        return {"votes": state['votes'] + [vote.dict()]}

    return agent_node

def aggregate_node(state: EnsembleState) -> dict:
    """Aggregate votes using configured strategy."""

    votes = [AgentVote(**v) for v in state['votes']]
    strategy = state['voting_strategy']

    if strategy == "majority":
        decision = majority_vote(votes)
    elif strategy == "unanimous":
        decision = unanimous_vote(votes)
    elif strategy == "weighted":
        decision = weighted_vote(votes)
    else:
        decision = threshold_vote(votes)

    needs_resolution = decision in ["NO_CONSENSUS", "BELOW_THRESHOLD"]

    return {
        "result": {
            "decision": decision,
            "votes": state['votes'],
            "consensus": not needs_resolution
        },
        "needs_resolution": needs_resolution
    }

def resolve_conflict_node(state: EnsembleState) -> dict:
    """Handle cases without clear consensus."""

    prompt = f"""
    The ensemble did not reach consensus.

    Votes:
    {format_votes(state['votes'])}

    Analyze the disagreement:
    1. What is the core conflict?
    2. Which perspective has stronger evidence?
    3. Should we escalate to human?
    4. Can we synthesize a middle ground?
    """

    resolution = llm.with_structured_output(ConflictResolution).invoke(prompt)

    return {
        "result": {
            **state['result'],
            "resolution": resolution.dict()
        }
    }

def finalize_node(state: EnsembleState) -> dict:
    """Create final ensemble result."""

    votes = [AgentVote(**v) for v in state['votes']]

    return {
        "result": EnsembleResult(
            final_decision=state['result']['decision'],
            consensus_level=calculate_consensus(votes),
            voting_breakdown=Counter(v.decision for v in votes),
            dissenting_views=[v.reasoning for v in votes if v.decision != state['result']['decision']],
            aggregate_confidence=sum(v.confidence for v in votes) / len(votes),
            recommendation=generate_recommendation(state['result'])
        ).dict()
    }

# Build Graph with parallel agent execution
graph = StateGraph(EnsembleState)
graph.add_node("dispatch", dispatch_node)
graph.add_node("aggregate", aggregate_node)
graph.add_node("resolve", resolve_conflict_node)
graph.add_node("finalize", finalize_node)

# Add agent nodes dynamically
for config in DEFAULT_AGENT_CONFIGS:
    graph.add_node(f"agent_{config['id']}", create_agent_node(config))

graph.add_edge(START, "dispatch")
# Parallel execution to all agents
for config in DEFAULT_AGENT_CONFIGS:
    graph.add_edge("dispatch", f"agent_{config['id']}")
    graph.add_edge(f"agent_{config['id']}", "aggregate")

graph.add_conditional_edges(
    "aggregate",
    lambda s: "resolve" if s['needs_resolution'] else "finalize",
    {"resolve": "resolve", "finalize": "finalize"}
)
graph.add_edge("resolve", "finalize")
graph.add_edge("finalize", END)

ensemble_chain = graph.compile()
```


#### Example



**Code:**
```python
SECURITY_ENSEMBLE = [
    {
        "id": "security_expert",
        "role": "Security Expert",
        "perspective": "Focus on vulnerabilities, attack vectors, data exposure",
        "weight": 1.5
    },
    {
        "id": "skeptic",
        "role": "Devil's Advocate",
        "perspective": "Challenge assumptions, find edge cases, worst-case scenarios",
        "weight": 1.0
    },
    {
        "id": "domain_expert",
        "role": "Domain Expert",
        "perspective": "Business logic correctness, compliance requirements",
        "weight": 1.2
    },
    {
        "id": "pragmatist",
        "role": "Pragmatic Engineer",
        "perspective": "Feasibility, maintenance burden, real-world tradeoffs",
        "weight": 1.0
    },
    {
        "id": "risk_assessor",
        "role": "Risk Analyst",
        "perspective": "Probability and impact of failures, mitigation options",
        "weight": 1.3
    }
]
```


#### Example



**Code:**
```python
VALIDATION_ENSEMBLE = [
    {
        "id": "fact_checker",
        "role": "Fact Checker",
        "perspective": "Verify claims against known facts and sources",
        "weight": 1.5
    },
    {
        "id": "logic_checker",
        "role": "Logic Validator",
        "perspective": "Check for logical consistency and sound reasoning",
        "weight": 1.3
    },
    {
        "id": "completeness_checker",
        "role": "Completeness Auditor",
        "perspective": "Identify gaps, missing considerations, blind spots",
        "weight": 1.0
    }
]
```


#### Example



**Code:**
```python
def validate_critical_decision(
    decision: str,
    context: dict,
    ensemble_type: str = "security"
) -> EnsembleResult:
    """Use ensemble for critical decisions."""

    configs = {
        "security": SECURITY_ENSEMBLE,
        "validation": VALIDATION_ENSEMBLE
    }

    result = ensemble_chain.invoke({
        "query": f"Evaluate this decision: {decision}",
        "context": context,
        "agent_configs": configs[ensemble_type],
        "votes": [],
        "voting_strategy": "weighted"
    })

    return EnsembleResult(**result['result'])
```


#### Example



**Code:**
```json
{
  "min_agents": 3,
  "recommended_agents": 5,
  "max_agents": 7,
  "default_strategy": "weighted",
  "confidence_threshold": 0.7,
  "require_unanimous_for": ["security", "legal", "financial"]
}
```




## Configuration



## Best Practices




## Related



---

<small>Source: `knowledge/patterns/ensemble-pattern.md`</small>
