---
title: run-workflow
type: command
tags: []
lang: en
confidence: 100
---

# run-workflow


## Overview

<div class="component-meta" markdown>
| Attribute | Value |
|-----------|-------|
| **Type** | Command |
| **Purpose** | Component description |
| **Complexity** | medium |
| **Model** | sonnet |
| **Category** | commands |</div>


## What It Does




## System Impact




## Architecture




## Usage


### Examples

#### Example



**Code:**
```python
from workflows.engine import load_workflow, list_workflows

# Zeige verfügbare Workflows wenn keiner angegeben
if not workflow_name:
    available = list_workflows()
    print("Verfügbare Workflows:")
    for name in available:
        workflow = load_workflow(name)
        print(f"  - {name}: {workflow.description}")
    return

# Lade Workflow
workflow = load_workflow(workflow_name)
```


#### Example



**Code:**
```bash
Workflow: {workflow.name} (v{workflow.version})
Beschreibung: {workflow.description}

Permissions: {workflow.permissions_profile}
Preferences: {workflow.preferences_profile}

Steps:
1. {step.name} [{step.get_execution_type()}] - {step.model}
2. ...

Variablen:
- {var.name}: {var.default or "(required)"}
...

Geschätzte Kosten: ~${estimated_cost}
Geschätzte Dauer: ~{estimated_duration}
```


#### Example



**Code:**
```python
from workflows.engine import WorkflowRunner

runner = WorkflowRunner()

if dry_run:
    result = await runner.dry_run(workflow_name, variables=parsed_variables)
else:
    result = await runner.run(
        workflow_name,
        variables=parsed_variables,
        resume_from=resume_id
    )
```


#### Example



**Code:**
```bash
═══════════════════════════════════════════════════════
Workflow Complete: {workflow.name}
═══════════════════════════════════════════════════════

Status: {result.status}
Dauer: {result.duration_seconds}s
Tokens: {result.total_tokens}
Kosten: ${result.total_cost:.4f}

Steps:
✓ Step 1: Erfasse Idee (success)
✓ Step 2: Validiere Idee (success)
⚠ Step 3: Expandiere (skipped - condition not met)
✓ Step 4: Dokumentation (success)

Logs: workflows/logs/{workflow.name}-{result.run_id}.json
```


#### Example



**Code:**
```bash
✗ Workflow Failed: {error}

Fehlgeschlagener Step: {step_name}
Fehler: {error_message}

Checkpoint: {checkpoint_path}
Fortsetzen mit: /run-workflow {name} --resume {run_id}
```




## Configuration



## Best Practices




## Related



---

<small>Source: `.claude/commands/run-workflow.md`</small>
