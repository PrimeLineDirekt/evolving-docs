---
title: idea-work
type: command
tags: []
lang: en
confidence: 100
---

# idea-work


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

Arbeite an einer Idee (Sparring Session)


## System Impact




## Architecture




## Usage


### Examples

#### Example



**Code:**
```bash
Deine Ideen:

[1] {Titel} (Potential: 8/10) - business/saas - Status: active
[2] {Titel} (Potential: 6/10) - tech/automation - Status: draft
[3] {Titel} (Potential: 9/10) - business/e-commerce - Status: active

An welcher Idee möchtest du arbeiten? (Nummer oder ID)
```


#### Example



**Code:**
```json
{
  "session_id": "idea-work-{timestamp}",
  "context_data": {
    "idea_id": "{id}",
    "idea_title": "{title}",
    "related_ideas": [],
    "related_projects": []
  },
  "agents_list": ["idea-validator", "idea-expander", "idea-connector"],
  "knowledge_base_refs": ["knowledge/prompts", "knowledge/projects"]
}
```


#### Example



**Code:**
```json
{
  "knowledge_sources": ["knowledge/prompts", "knowledge/projects", "knowledge/personal/skills.md"],
  "synthesis_depth": "standard",
  "target_domain": "{idea_category}",
  "existing_knowledge_refs": ["{related_refs}"]
}
```


#### Example



**Code:**
```bash
Session-Modus für "{Titel}":

[1] Brainstorming - Idee erweitern & neue Aspekte finden
[2] Validierung - Kritisch hinterfragen & Schwächen identifizieren
[3] Konkretisierung (PEV) - Von Idee zu konkretem Umsetzungsplan mit Plan-Execute-Verify
[4] Problemlösung - Spezifisches Problem/Blocker bearbeiten
[5] Freies Sparring - Du sagst mir was du tun willst

Wähle einen Modus:
```


#### Example



**Code:**
```bash
┌─────────────────────────────────────────────────┐
│                  PEV CYCLE                       │
│                                                  │
│  PLAN → EXECUTE → VERIFY → (REPLAN wenn nötig)  │
└─────────────────────────────────────────────────┘
```


#### Example



**Code:**
```xml
<session_plan>
  <objectives>
    <primary>Was ist das Hauptziel dieser Session?</primary>
    <secondary>Welche Nebenziele gibt es?</secondary>
  </objectives>
  <steps>
    <step id="1" agent="context-manager">Kontext laden & verifizieren</step>
    <step id="2" agent="{mode-specific}">Agent-gestützte Analyse</step>
    <step id="3" agent="idea-connector">Verbindungen prüfen</step>
    <step id="4">Session dokumentieren</step>
  </steps>
  <success_criteria>
    - Mindestens 3 neue Insights
    - Konkrete nächste Schritte definiert
    - Fortschritt dokumentiert
  </success_criteria>
</session_plan>
```


#### Example



**Code:**
```xml
<verification step="{current}">
  <expected>{step.expected_output}</expected>
  <actual>{step.actual_output}</actual>
  <check>
    - Qualität ausreichend? [ja/nein]
    - Ziel erreicht? [ja/nein]
    - Probleme aufgetreten? [beschreibung]
  </check>
  <decision>
    IF quality_ok AND goal_reached → CONTINUE to next step
    ELIF minor_issues → REFINE current step output
    ELSE → REPLAN (adjust remaining steps)
  </decision>
</verification>
```


#### Example



**Code:**
```xml
<replan trigger="{verification_failure}">
  <issue>{was ist schief gelaufen}</issue>
  <adjustment>
    - Anderen Agent hinzuziehen?
    - Schritt aufteilen?
    - Ziel anpassen?
  </adjustment>
  <new_steps>
    <!-- Aktualisierte Schritte -->
  </new_steps>
</replan>
```


#### Example



**Code:**
```json
{
  "idea_data": {idea_object},
  "expansion_dimensions": ["features", "markets", "use-cases", "integrations"],
  "constraints": {user_constraints},
  "context_refs": [context_from_step_2_5]
}
```


#### Example



**Code:**
```json
{
  "idea_data": {idea_object},
  "validation_depth": "deep",
  "validation_criteria": ["feasibility", "market", "technical", "resources"],
  "context_refs": [context_from_step_2_5]
}
```


#### Example



**Code:**
```xml
<konkretisierung_plan>
  <goal>Von Idee zu konkretem, umsetzbarem Plan</goal>
  <steps>
    <step id="1" agent="idea-validator">
      <objective>Feasibility & Resource Assessment</objective>
      <expected_output>Validation Report mit Go/No-Go Empfehlung</expected_output>
    </step>
    <step id="2" agent="idea-expander" depends_on="1">
      <objective>MVP Features & Phasen definieren</objective>
      <expected_output>Feature-Liste mit Priorisierung</expected_output>
    </step>
    <step id="3" depends_on="1,2">
      <objective>Timeline & Milestones erstellen</objective>
      <expected_output>Realistischer Zeitplan</expected_output>
    </step>
    <step id="4" depends_on="3">
      <objective>Konkrete nächste Schritte definieren</objective>
      <expected_output>Actionable Task-Liste</expected_output>
    </step>
  </steps>
  <success_criteria>
    - Feasibility Score >= 7/10
    - MVP klar definiert
    - Timeline realistisch (User bestätigt)
    - Mindestens 5 konkrete nächste Schritte
  </success_criteria>
</konkretisierung_plan>
```


#### Example



**Code:**
```json
{
  "idea_data": {idea_object},
  "validation_depth": "standard",
  "validation_criteria": ["feasibility", "resources", "timeline"],
  "context_refs": [context_from_step_2_5]
}
```


#### Example



**Code:**
```bash
Feasibility Score: {score}/10
Resources identified: [ja/nein]
Blockers: {liste}

IF score < 7 → REPLAN: Scope reduzieren oder Blocker adressieren
ELSE → CONTINUE
```


#### Example



**Code:**
```json
{
  "idea_data": {idea_object},
  "expansion_dimensions": ["mvp-features", "implementation-phases"],
  "constraints": {"focus": "concrete_plan", "feasibility_input": "{step1_output}"},
  "context_refs": [context_from_step_2_5]
}
```


#### Example



**Code:**
```bash
Features priorisiert: [ja/nein]
MVP scope klar: [ja/nein]
Passt zu Resources: [ja/nein]

IF mvp_unclear → REFINE: Feature-Scope mit User klären
ELSE → CONTINUE
```


#### Example



**Code:**
```xml
<session_verification>
  <criteria_check>
    □ Feasibility Score >= 7/10: {status}
    □ MVP klar definiert: {status}
    □ Timeline realistisch: {status}
    □ 5+ konkrete nächste Schritte: {status}
  </criteria_check>
  <overall_success>{alle_criteria_erfüllt}</overall_success>
  <if_not_success>
    <missing>{was fehlt}</missing>
    <recommendation>Nächste Session fokussieren auf: {missing}</recommendation>
  </if_not_success>
</session_verification>
```


#### Example



**Code:**
```json
{
  "research_topic": "{problem_description}",
  "research_depth": "standard",
  "source_requirements": {"minimum_sources": 3},
  "focus_areas": ["{problem_areas}"]
}
```


#### Example



**Code:**
```json
{
  "idea_data": {updated_idea_object},
  "all_ideas": [load_from_ideas_directory],
  "connection_types": ["synergy", "resource-sharing", "integration", "collaboration"],
  "context_refs": [session_insights]
}
```


#### Example



**Code:**
```bash
✓ Session gespeichert für: {Titel}

Zusammenfassung:
{Kurze Zusammenfassung der Session}

Nächste Schritte:
{Liste der neuen Todos}

Weitere Aktionen:
- /idea-work {id} - Nächste Session
- /idea-connect - Finde Synergien mit anderen Ideen
- /idea-list - Zurück zur Übersicht
```




## Configuration



## Best Practices




## Related



---

<small>Source: `.claude/commands/idea-work.md`</small>
