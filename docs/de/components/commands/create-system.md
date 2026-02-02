---
title: create-system
type: command
tags: []
lang: en
confidence: 100
---

# create-system


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

Generiert ein komplettes Multi-Agent System in einem Ziel-Ordner


## System Impact




## Architecture




## Usage


### Examples

#### Example



**Code:**
```bash
/create-system ~/projects/steuer-system
/create-system ~/projects/legal-advisor --blueprint multi-agent-advisory
```


#### Example



**Code:**
```bash
Starte Task-Agent mit:
- subagent_type: "general-purpose"
- prompt: Lade @.claude/agents/system-analyzer-agent.md und analysiere:
  - User Request: "{user_description}"
  - Target Path: "{target_path}"
  - Available Blueprints: Lade .claude/blueprints/index.json
```


#### Example



**Code:**
```bash
Analysiere deine Anforderung...

Erkannt:
- Domain: {detected_domain}
- Komplexität: {complexity}
- Geschätzte Agents: {agent_count}

Blueprint-Matches:
┌────────────────────────────┬───────┬─────────────────────────────┐
│ Blueprint                  │ Match │ Grund                       │
├────────────────────────────┼───────┼─────────────────────────────┤
│ 1. Multi-Agent Advisory    │  95%  │ Keywords: experten, team    │
│ 2. Autonomous Research     │  40%  │ Nur partial match           │
│ 3. Simple Workflow         │  25%  │ Zu einfach für Anforderung  │
└────────────────────────────┴───────┴─────────────────────────────┘

Empfehlung: Multi-Agent Advisory (95% Match)

[1] Empfehlung akzeptieren
[2] Anderen Blueprint wählen
[3] Custom System (ohne Blueprint)
```


#### Example



**Code:**
```bash
Starte Task-Agent mit:
- subagent_type: "general-purpose"
- model: "opus"
- prompt: Lade @.claude/agents/system-architect-agent.md und designe:
  - Blueprint: {selected_blueprint}
  - Domain: {domain}
  - Target: {target_path}
  - User Customization: {customization_answers}
```


#### Example



**Code:**
```bash
Konfiguration für Multi-Agent Advisory:

1. Domain-Name: steuer
2. Projekt-Name: Steuer-Beratungs-System [Enter für Default]
3. Anzahl Spezialisten (2-4): 3

Optionale Features:
[x] Validator-Agent für Risiko-Assessment
[x] Knowledge Base Struktur
[ ] Memory-System

Welche Spezialisten-Rollen?
1. Steuerberater (Hauptexperte) [Opus]
2. Steueranwalt (Rechtssicherheit) [Opus]
3. Software-Experte (Tool-Bedienung) [Sonnet]

Proceed? (Y/n)
```


#### Example



**Code:**
```bash
Architektur-Design:

System: Steuer-Beratungs-System
Domain: steuer
Pattern: multi-agent-advisory

Agents (5):
┌─────────────────────────────────────────────────────────────────┐
│                     steuer-koordinator                          │
│                        (Sonnet)                                 │
└───────────────────────────┬─────────────────────────────────────┘
                            │
        ┌───────────────────┼───────────────────┐
        │                   │                   │
        ▼                   ▼                   ▼
┌───────────────┐   ┌───────────────┐   ┌───────────────┐
│ steuerberater │   │ steueranwalt  │   │ software-     │
│    (Opus)     │   │    (Opus)     │   │ experte       │
│               │   │               │   │  (Sonnet)     │
└───────┬───────┘   └───────┬───────┘   └───────────────┘
        │                   │
        └─────────┬─────────┘
                  │
                  ▼
          ┌───────────────┐
          │    reporter   │
          │   (Haiku)     │
          └───────────────┘

Commands (2):
- /steuer-beratung → Umfassende Team-Beratung (Opus)
- /steuer-check → Schnelle Prüfung (Haiku)

Knowledge Injection:
- multi-agent-orchestration.md (Pattern)
- confidence-scoring.md (Pattern)
- ki-auswanderungs-berater-learnings.md (Reference)

Model-Verteilung:
- Opus: 2 Agents (kritische Analyse)
- Sonnet: 2 Agents (Koordination)
- Haiku: 1 Agent (Reporting)

Proceed mit Generation? (Y/n)
```


#### Example



**Code:**
```bash
Starte Task-Agent mit:
- subagent_type: "general-purpose"
- prompt: Lade @.claude/agents/system-generator-agent.md und generiere:
  - Architecture: {architecture_json}
  - Target Path: {target_path}
  - Templates: .claude/templates/generated-system/
```


#### Example



**Code:**
```bash
Generiere System...

[1/8] Verzeichnisstruktur erstellen... ✓
[2/8] CLAUDE.md generieren... ✓
[3/8] README.md generieren... ✓
[4/8] scenario.json generieren... ✓
[5/8] Agents erstellen (5)... ✓
[6/8] Commands erstellen (2)... ✓
[7/8] Knowledge Injection... ✓
[8/8] Memory Bootstrap... ✓

Generation abgeschlossen!
```


#### Example



**Code:**
```bash
Starte Task-Agent mit:
- subagent_type: "general-purpose"
- model: "haiku"
- prompt: Lade @.claude/agents/system-validator-agent.md und validiere:
  - Target Path: {target_path}
  - Architecture: {architecture_json}
```


#### Example



**Code:**
```bash
Validierung...

✓ Verzeichnisstruktur (5/5 Ordner)
✓ Required Files (3/3 Dateien)
✓ Agent Files (5/5 Agents)
✓ Command Files (2/2 Commands)
✓ Placeholder Check (0 verbleibend)
✓ CLAUDE.md Quality (156 Zeilen)
⚠ Reference Integrity (7/8 - 1 optionale Warnung)

Score: 95/100 - PASS

1 Warnung:
- Optional pattern 'reflection-pattern.md' nicht gefunden
  → Kann ignoriert oder später hinzugefügt werden
```


#### Example



**Code:**
```bash
System erfolgreich generiert!

Pfad: ~/projects/steuer-system/

Dateien erstellt:
├── .claude/
│   ├── CLAUDE.md
│   ├── scenario.json
│   ├── agents/
│   │   ├── steuer-koordinator-agent.md
│   │   ├── steuerberater-agent.md
│   │   ├── steueranwalt-agent.md
│   │   ├── software-experte-agent.md
│   │   └── steuer-reporter-agent.md
│   └── commands/
│       ├── steuer-beratung.md
│       └── steuer-check.md
├── knowledge/
│   └── patterns/
│       ├── multi-agent-orchestration.md
│       └── confidence-scoring.md
├── _memory/
│   └── index.json
└── README.md

Total: 14 Dateien, 5 Agents, 2 Commands

Nächste Schritte:
1. cd ~/projects/steuer-system
2. claude code (startet Claude Code im Projekt)
3. /steuer-beratung für umfassende Beratung
4. /steuer-check für schnelle Prüfungen

Optional:
- Füge Domain-Wissen zu knowledge/ hinzu
- Passe Agents in .claude/agents/ an
- Erweitere mit eigenen Commands
```


#### Example



**Code:**
```bash
IF path_not_writable:
  "Fehler: Keine Schreibrechte für {path}
   Versuche einen anderen Pfad oder führe mit sudo aus."
```


#### Example



**Code:**
```bash
IF blueprint_not_found:
  "Blueprint '{id}' nicht gefunden.
   Verfügbare Blueprints:"
   → Liste alle aus index.json
```


#### Example



**Code:**
```bash
IF generation_failed:
  "Generation fehlgeschlagen bei: {step}
   Fehler: {error}

   Bereits erstellte Dateien wurden beibehalten.
   Retry mit: /create-system {path} --resume"
```


#### Example



**Code:**
```bash
IF validation_failed:
  "System generiert aber Validation fehlgeschlagen:
   {issues}

   Das System ist möglicherweise nicht vollständig nutzbar.
   Bitte manuell prüfen oder mit --force überspringen."
```


#### Example



**Code:**
```bash
/create-system ~/projects/tax-advisor
```


#### Example



**Code:**
```bash
/create-system ~/projects/legal-system --blueprint multi-agent-advisory --domain legal
```


#### Example



**Code:**
```bash
/create-system ~/projects/quick-test --blueprint simple-workflow --auto
```


#### Example



**Code:**
```bash
/create-system ~/projects/preview --dry-run
```




## Configuration



## Best Practices




## Related



---

<small>Source: `.claude/commands/create-system.md`</small>
