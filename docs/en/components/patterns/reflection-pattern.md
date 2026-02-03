---
title: reflection-pattern
type: pattern
tags: []
lang: en
confidence: 100
---

# reflection-pattern


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
│   GENERATOR     │◄──────────────┐
│  Erstellt Draft │               │
└────────┬────────┘               │
         │                        │
         ▼                        │
┌─────────────────┐               │
│    CRITIC       │               │
│ Bewertet Draft  │               │
│ Findet Probleme │               │
└────────┬────────┘               │
         │                        │
         ▼                        │
┌─────────────────┐               │
│   REFINER       │───────────────┘
│ Verbessert      │    (Loop bis akzeptabel)
│ basierend auf   │
│ Feedback        │
└────────┬────────┘
         │
         ▼
   Final Output
```


#### Example



**Code:**
```python
from pydantic import BaseModel, Field

class GeneratedDraft(BaseModel):
    content: str = Field(description="Generated content")
    reasoning: str = Field(description="Why this approach was chosen")

class CriticFeedback(BaseModel):
    issues: list[str] = Field(description="Problems identified")
    suggestions: list[str] = Field(description="Specific improvements")
    is_acceptable: bool = Field(description="Meets quality threshold?")
    quality_score: float = Field(ge=0, le=10, description="Quality 0-10")

class RefinedOutput(BaseModel):
    content: str = Field(description="Improved content")
    changes_made: list[str] = Field(description="What was changed")
```


#### Example



**Code:**
```python
from langgraph.graph import StateGraph, START, END
from typing import TypedDict

class ReflectionState(TypedDict):
    query: str
    draft: str
    feedback: CriticFeedback
    final_output: str
    iterations: int
    max_iterations: int

def generator_node(state: ReflectionState) -> dict:
    if state.get("feedback"):
        prompt = f"""
        Original query: {state['query']}
        Previous draft: {state['draft']}
        Feedback: {state['feedback'].suggestions}

        Create an improved version addressing all feedback.
        """
    else:
        prompt = f"Create a comprehensive response to: {state['query']}"

    result = llm.with_structured_output(GeneratedDraft).invoke(prompt)
    return {
        "draft": result.content,
        "iterations": state.get("iterations", 0) + 1
    }

def critic_node(state: ReflectionState) -> dict:
    prompt = f"""
    Query: {state['query']}
    Draft: {state['draft']}

    Critically evaluate this draft:
    1. Is it complete and accurate?
    2. Are there logical issues?
    3. Is the quality sufficient?

    Be constructive but thorough.
    """
    feedback = llm.with_structured_output(CriticFeedback).invoke(prompt)
    return {"feedback": feedback}

def should_continue(state: ReflectionState) -> str:
    if state["feedback"].is_acceptable:
        return "finalize"
    if state["iterations"] >= state.get("max_iterations", 3):
        return "finalize"  # Stop after max iterations
    return "refine"

def finalize_node(state: ReflectionState) -> dict:
    return {"final_output": state["draft"]}

# Build Graph
graph = StateGraph(ReflectionState)
graph.add_node("generate", generator_node)
graph.add_node("critic", critic_node)
graph.add_node("finalize", finalize_node)

graph.add_edge(START, "generate")
graph.add_edge("generate", "critic")
graph.add_conditional_edges(
    "critic",
    should_continue,
    {"refine": "generate", "finalize": "finalize"}
)
graph.add_edge("finalize", END)

reflection_chain = graph.compile()
```


#### Example



**Code:**
```python
class PromptReflectionState(TypedDict):
    user_request: str
    generated_prompt: str
    critique: CriticFeedback
    final_prompt: str

def prompt_critic(state):
    """Spezialisierter Critic für Prompts"""
    prompt = f"""
    Evaluate this prompt against best practices:

    {state['generated_prompt']}

    Check for:
    - Clear role definition
    - Structured output format
    - Edge case handling
    - Appropriate constraints
    - Claude-specific optimization
    """
    return llm.with_structured_output(CriticFeedback).invoke(prompt)
```


#### Example



**Code:**
```python
def validate_with_reflection(idea: str) -> ValidationResult:
    """Idea-Validierung mit Self-Reflection"""

    # Initial validation
    validation = idea_validator.validate(idea)

    # Critic reviews the validation
    critique = reflection_critic.evaluate(
        original=idea,
        validation=validation,
        criteria=["completeness", "bias", "assumptions"]
    )

    # Refine if needed
    if not critique.is_acceptable:
        validation = idea_validator.refine(validation, critique.suggestions)

    return validation
```


#### Example



**Code:**
```python
from pydantic import BaseModel, Field
from typing import Optional

class GleaningConfig(BaseModel):
    """Configuration for iterative output refinement."""

    num_rounds: int = Field(
        default=3,
        ge=1,
        le=5,
        description="Maximum refinement iterations"
    )

    validation_prompt: str = Field(
        description="Custom prompt to evaluate output quality"
    )

    if_condition: Optional[str] = Field(
        default=None,
        description="Condition that triggers gleaning (e.g., 'confidence < 0.8')"
    )

    quality_threshold: float = Field(
        default=0.85,
        ge=0,
        le=1,
        description="Quality score threshold to accept output"
    )
```


#### Example



**Code:**
```python
class GleaningReflectionState(TypedDict):
    query: str
    draft: str
    feedback: Optional[CriticFeedback]
    final_output: str
    iteration: int
    config: GleaningConfig

def should_glean(state: GleaningReflectionState) -> bool:
    """Evaluate if gleaning should be triggered."""
    config = state["config"]

    # Check if_condition
    if config.if_condition:
        # Evaluate condition (e.g., "confidence < 0.8")
        if not eval_condition(config.if_condition, state):
            return False

    # Check iteration limit
    if state["iteration"] >= config.num_rounds:
        return False

    # Check quality threshold
    if state.get("feedback") and state["feedback"].quality_score >= config.quality_threshold * 10:
        return False

    return True

def gleaning_critic(state: GleaningReflectionState) -> dict:
    """Critic using custom validation_prompt."""
    config = state["config"]

    prompt = f"""
    {config.validation_prompt}

    Content to evaluate:
    {state['draft']}

    Original query: {state['query']}

    Provide structured feedback with quality_score (0-10).
    """

    feedback = llm.with_structured_output(CriticFeedback).invoke(prompt)
    return {
        "feedback": feedback,
        "iteration": state["iteration"] + 1
    }
```


#### Example



**Code:**
```python
# Define gleaning config for high-stakes analysis
tax_analysis_gleaning = GleaningConfig(
    num_rounds=2,
    validation_prompt="""
    Evaluate this tax analysis for:
    1. Accuracy of legal references (§§, BMF-Schreiben)
    2. Risk zone classifications (🟢🟡🟠) are appropriate
    3. Numerical calculations are plausible
    4. No contradictory recommendations
    """,
    if_condition="model_tier == 1",  # Only for Opus agents
    quality_threshold=0.9
)

# Run with gleaning
result = reflection_chain.invoke({
    "query": "Wegzugsbesteuerung bei Umzug nach Portugal",
    "config": tax_analysis_gleaning
})
```




## Configuration



## Best Practices




## Related


---

<small>Source: `knowledge/patterns/reflection-pattern.md`</small>
