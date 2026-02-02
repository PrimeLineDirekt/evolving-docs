---
title: Commands erstellen
description: User-aufrufbare Aktionen für das Evolving System bauen
---

# Commands erstellen

Commands sind user-aufrufbare Aktionen, die Shortcuts zu häufigen Workflows bieten. Dieser Guide zeigt dir, wie du Custom Commands erstellst, konfigurierst und integrierst.

## Was sind Commands?

Commands sind Markdown-Dateien mit YAML-Frontmatter, die definieren:

- **Name** - Wie User es aufrufen (`/command-name`)
- **Agent** - Welcher Spezialist es ausführt (optional)
- **Model** - Welches Claude-Model zu nutzen ist
- **Verhalten** - Was das Command macht

## Command-Struktur

### Basis-Template

```markdown
---
name: mein-command
description: Kurze Beschreibung was es macht
agent: spezialist-agent  # Optional
model: haiku            # Optional: haiku, sonnet, opus
---

# Command Name

Was das Command macht und wie man es nutzt.

## Parameter

- `param1`: Beschreibung
- `param2`: Beschreibung

## Beispiele

```bash
/mein-command param1 param2
```

## Verhalten

Detaillierte Anweisungen für den ausführenden Agent.
```

### Vollständiges Beispiel

```markdown
---
name: validate
description: Validiere Code, Configs und Datenstrukturen
agent: validator
model: haiku
---

# Validate

Validiert die spezifizierten Dateien auf Korrektheit mit passenden Tools.

## Parameter

- `files`: Dateipfade zu validieren (Glob-Patterns unterstützt)
- `type`: Optionaler Validierungs-Typ (code|config|data)

## Beispiele

```bash
# Spezifische Datei validieren
/validate src/auth.ts

# Mit Glob validieren
/validate "src/**/*.ts"

# Mit Type-Hint validieren
/validate config.json --type=config
```

## Verhalten

1. Dateitypen identifizieren
2. Passende Validierungs-Tools bestimmen
3. Validierung mit Confidence-Scoring ausführen
4. Findings reporten (Errors, Warnings, Suggestions)
5. Fix-Vorschläge nur auf Nachfrage

## Output-Format

```markdown
## Validierungs-Ergebnisse

**Datei**: {path}
**Status**: PASS|FAIL

### Errors
- Zeile {n}: {issue} [Confidence: {%}]

### Warnings
- Zeile {n}: {issue} [Confidence: {%}]
```
```

## Command-Typen

### 1. Direkte Commands

Sofort ausführen ohne Delegation:

```markdown
---
name: hello
description: Einfache Begrüßung
---

# Hello

Begrüße den User.

Einfach mit freundlichem Gruß antworten.
```

### 2. Agent Commands

An Spezialisten delegieren:

```markdown
---
name: explore-code
description: Codebase-Struktur analysieren
agent: Explore
model: haiku
---

# Explore Code

Nutze den Explore-Agent um die Codebase zu analysieren.
```

### 3. Workflow Commands

Multi-Step-Prozesse:

```markdown
---
name: feature-pipeline
description: Vollständige Feature-Entwicklungs-Pipeline
---

# Feature Pipeline

1. Feature-Branch erstellen
2. Implementation-Plan generieren
3. Mit code-architect ausführen
4. Mit code-reviewer reviewen
5. PR erstellen
```

## Parameter-Handling

### Einfache Parameter

```markdown
## Parameter

- `file`: Zu verarbeitende Datei
- `mode`: Operations-Modus (read|write)
```

Nutzung:
```bash
/process-file src/main.ts --mode=read
```

### Optionale Parameter

```markdown
## Parameter

- `input`: Input-Datei (erforderlich)
- `output`: Output-Datei (optional, default stdout)
- `format`: Format-Typ (optional, auto-detect)
```

Nutzung:
```bash
/convert input.json
/convert input.json --output=result.yaml
/convert input.json --output=result.yaml --format=yaml
```

### Flags

```markdown
## Parameter

- `--verbose`: Detaillierte Ausgabe zeigen
- `--dry-run`: Vorschau ohne Ausführung
- `--force`: Bestätigungen überspringen
```

Nutzung:
```bash
/migrate --dry-run
/migrate --verbose --force
```

## Agent-Integration

### Den richtigen Agent wählen

| Task-Typ | Agent | Model |
|-----------|-------|-------|
| Code-Exploration | Explore | haiku |
| Debugging | debugger | sonnet |
| Code Review | code-reviewer | sonnet |
| Architektur | code-architect | sonnet |
| General Tasks | general-purpose | sonnet |

## Plain-Text-Detection

Commands via natürliche Sprache aufrufbar machen:

### Detection Index

Zu `.claude/detection-index.json` hinzufügen:

```json
{
  "commands": [
    {
      "name": "validate",
      "triggers": [
        "validieren",
        "prüfen",
        "verifizieren",
        "lint"
      ],
      "patterns": [
        "validiere (diese|die) (datei|code)",
        "prüfe (ob|whether) .* (ist )?(gültig|korrekt)",
        "verifiziere (die )?(syntax|format)"
      ],
      "confidence_boost": 10
    }
  ]
}
```

## Registrierungs-Schritte

### 1. Command-Datei erstellen

```bash
.claude/commands/mein-command.md
```

### 2. Stats updaten

```json
// _stats.json
{
  "commands": 81  // Erhöhen
}
```

### 3. Zu Detection Index hinzufügen

```json
// .claude/detection-index.json
{
  "commands": [
    {
      "name": "mein-command",
      "triggers": ["keyword1", "keyword2"],
      "patterns": ["pattern.*regex"]
    }
  ]
}
```

### 4. Graph Node erstellen

```json
// _graph/knowledge-nodes.json
{
  "nodes": [
    {
      "id": "command-mein-command",
      "type": "command",
      "name": "mein-command",
      "description": "Was es macht",
      "domain": ["kategorie"],
      "tags": ["command", "tag1", "tag2"]
    }
  ]
}
```

### 5. SYSTEM-MAP updaten

```markdown
<!-- .claude/SYSTEM-MAP.md -->

## Commands

| Command | Agent | Zweck |
|---------|-------|-------|
| /mein-command | spezialist | Was es macht |
```

## Commands testen

### Manueller Test

```bash
# Direkter Aufruf
/mein-command param1 param2
```

### Via Plain-Text

```
User: "Führe mein Command mit diesen Params aus"
Claude: "Soll ich /mein-command ausführen?"
User: "Ja"
→ Command wird ausgeführt
```

## Best Practices

### DO

✅ **Klare, beschreibende Namen**
```markdown
---
name: validate-config
description: Konfigurations-Dateien validieren
---
```

✅ **Agent spezifizieren wenn passend**
```markdown
---
agent: validator
model: haiku
---
```

✅ **Parameter dokumentieren**
```markdown
## Parameter
- `file`: Pfad zu validieren (erforderlich)
- `strict`: Strict-Modus (optional)
```

### DON'T

❌ **Vage Namen**
```markdown
---
name: do-stuff
---
```

❌ **Fehlende Dokumentation**
```markdown
---
name: complex-command
---

# Complex Command
(keine Erklärung was es macht)
```

## Nächste Schritte

- [Agents erstellen](creating-agents.md) - Spezialisten bauen
- [Patterns nutzen](using-patterns.md) - Prompt Patterns anwenden
- [System erweitern](extending-system.md) - Volle Integration
