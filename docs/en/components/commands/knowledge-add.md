---
title: knowledge-add
type: command
tags: []
lang: en
confidence: 100
---

# knowledge-add


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

Füge Wissen zur Knowledge Base hinzu


## System Impact




## Architecture




## Usage


### Examples

#### Example



**Code:**
```bash
Was für Wissen möchtest du hinzufügen?

[1] Prompt - Wiederverwendbarer Prompt/Template
[2] Learning - Erkenntnis aus einem Projekt/Erfahrung
[3] Resource - Nützliche Ressource (Link, Tool, Methode)
[4] Note - Allgemeine Notiz/Wissen
[5] Import - Bestehende Datei importieren

Wähle eine Option:
```


#### Example



**Code:**
```yaml
---
title: "{Titel}"
type: {prompt|learning|resource|note}
tags: [{tag1, tag2, tag3}]
topics: [{thema1, thema2}]
skills: [{skill1, skill2}]
created: {datum}
updated: {datum}
related_ideas: [{idea-ids}]
related_projects: [{project-names}]
source: {optional: woher stammt das Wissen}
---
```


#### Example



**Code:**
```markdown
---
{frontmatter}
---

# {Titel}

## Zweck
{Wofür ist dieser Prompt}

## Prompt
\`\`\`
{Der eigentliche Prompt}
\`\`\`

## Verwendung
{Wie/wann nutzen}

## Varianten
{Optional: Anpassungen für verschiedene Use-Cases}

## Beispiele
{Optional: Beispiel-Outputs}
```


#### Example



**Code:**
```markdown
---
{frontmatter}
---

# {Titel}

## Kontext
{Wo/wie wurde das gelernt}

## Learning
{Die eigentliche Erkenntnis}

## Anwendung
{Wie kann das wiederverwendet werden}

## Verbindungen
{Links zu verwandten Themen}
```


#### Example



**Code:**
```markdown
---
{frontmatter}
---

# {Titel}

## Beschreibung
{Was ist die Ressource}

## Warum nützlich
{Value Proposition}

## Verwendung
{Wie nutzen}

## Links
{URLs, Referenzen}
```


#### Example



**Code:**
```markdown
---
{frontmatter}
---

# {Titel}

{Freier Content - strukturiert nach Bedarf}
```


#### Example



**Code:**
```bash
✓ Wissen hinzugefügt: {Titel}
  Type: {type}
  Kategorie: {kategorie}

Key Insights:
- {Insight 1}
- {Insight 2}
- {Insight 3}

Skills: {skills}

Verbindungen:
{Liste verwandter Ideen/Projekte}

Gespeichert unter: knowledge/{pfad}

Weitere Aktionen:
- /knowledge-search {topic} - Verwandtes Wissen finden
- /idea-new - Neue Idee basierend auf diesem Wissen
```




## Configuration



## Best Practices




## Related



---

<small>Source: `.claude/commands/knowledge-add.md`</small>
