---
title: repo-screen
type: command
tags: []
lang: en
confidence: 100
---

# repo-screen


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
```bash
/repo-screen [URL oder Liste von URLs]
```


#### Example



**Code:**
```bash
a) README.md fetchen via WebFetch:
   https://raw.githubusercontent.com/{owner}/{repo}/main/README.md
   (Fallback: master branch)

b) Relevanz-Indikatoren checken:

   STRUKTUR (aus README oder Repo-Beschreibung):
   - .claude/ Ordner erwähnt?
   - agents/, skills/, commands/ Struktur?
   - MCP Server / .mcp.json?
   - CLAUDE.md / AGENTS.md?

   KEYWORDS (im README):
   - "Claude" / "Anthropic" / "Claude Code"
   - "Multi-Agent" / "Agent Orchestration"
   - "MCP" / "Model Context Protocol"
   - "Knowledge Base" / "Second Brain"
   - "Prompt Engineering" / "Prompts"
   - "Workflow Automation" / "n8n"
   - "AI-First" / "LLM"
   - "Skills" / "Commands" / "Hooks"

c) Relevanz-Entscheidung:
   - JA: Mindestens 2 starke Indikatoren ODER 1 sehr starker (Claude Code spezifisch)
   - NEIN: Keine oder schwache Indikatoren
```


#### Example



**Code:**
```bash
{owner}/{repo} → JA/NEIN
Grund: {1-2 Sätze warum relevant oder nicht}
---
```


#### Example



**Code:**
```bash
SCREEN ERGEBNIS:
- Relevant: X Repos
- Skip: Y Repos

Relevante Repos für Deep Analysis:
- {liste}

Nächster Schritt: /analyze-repo {url} für Details
```


#### Example



**Code:**
```bash
/repo-screen
https://github.com/anthropics/claude-code
https://github.com/random/gaming-framework
https://github.com/modelcontextprotocol/servers
```


#### Example



**Code:**
```bash
anthropics/claude-code → JA
Grund: Offizielles Claude Code CLI - direkt relevant für unser System.
---
random/gaming-framework → NEIN
Grund: Gaming Framework ohne AI/Agent Bezug.
---
modelcontextprotocol/servers → JA
Grund: MCP Server Referenz-Implementierungen - relevant für MCP Integration.
---

SCREEN ERGEBNIS:
- Relevant: 2 Repos
- Skip: 1 Repo

Relevante Repos für Deep Analysis:
- anthropics/claude-code
- modelcontextprotocol/servers
```




## Configuration



## Best Practices




## Related



---

<small>Source: `.claude/commands/repo-screen.md`</small>
