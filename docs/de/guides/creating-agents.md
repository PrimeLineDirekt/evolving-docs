# Agents erstellen

Agents sind spezialisierte KI-Mitarbeiter, die spezifische Aufgaben innerhalb des Evolving-Systems bewältigen. Diese Anleitung zeigt dir, wie du benutzerdefinierte Agents erstellst, konfigurierst und integrierst.

## Agent-Dateistruktur

Agents befinden sich in `.claude/agents/` und verwenden Markdown-Format mit YAML-Frontmatter:

```markdown
---
name: validator
description: Validates code, configs, and data structures
model: haiku
capabilities:
  - code_validation
  - schema_checking
  - format_verification
tools:
  - Read
  - Bash
  - Grep
---

# Validator Agent

## Role
You are a validation specialist. Your job is to verify correctness, not to fix issues.

## Approach
1. Check against known standards
2. Report violations clearly
3. Suggest fixes only when asked
4. Use confidence levels for findings

## Capabilities
- **Code Validation**: Syntax, style, conventions
- **Schema Checking**: JSON Schema, TypeScript types
- **Format Verification**: YAML, TOML, Markdown
```

## Erforderliche Felder

| Feld | Typ | Erforderlich | Beschreibung |
|-------|------|----------|-------------|
| `name` | string | ✅ | Eindeutige Kennung (Kleinbuchstaben, Bindestriche) |
| `description` | string | ✅ | Was der Agent tut (1-2 Sätze) |
| `model` | string | ✅ | `haiku`, `sonnet` oder `opus` |
| `capabilities` | array | ❌ | Liste von Agent-Fähigkeiten |
| `tools` | array | ❌ | Erlaubte Claude Code Tools |

## Fähigkeiten und Tools

### Fähigkeiten definieren

Fähigkeiten beschreiben, was der Agent auf hoher Ebene tun kann:

```yaml
capabilities:
  - code_validation      # Code-Qualität prüfen
  - schema_checking      # Datenstrukturen validieren
  - format_verification  # Dateiformate validieren
  - security_audit       # Sicherheitsprobleme finden
```

### Tools spezifizieren

Beschränke, welche Tools der Agent nutzen kann:

```yaml
tools:
  - Read      # Dateien lesen
  - Bash      # Befehle ausführen
  - Grep      # Inhalte durchsuchen
  - Glob      # Dateien finden
  # NO Write, NO Edit (nur-lesen Agent)
```

**Tool-Kategorien:**

- **Nur-Lesen**: `Read`, `Grep`, `Glob`, `Bash` (sichere Abfragen)
- **Schreiben**: `Write`, `Edit`, `NotebookEdit` (Dateien ändern)
- **Ausführung**: `Bash` (Befehle ausführen)
- **Web**: `WebFetch`, `WebSearch` (Internetzugriff)

## Agent-Body-Struktur

Definiere nach dem Frontmatter das Verhalten des Agents:

```markdown
# {Agent Name}

## Role
Klare Aussage zur Identität und dem Zweck des Agents.

## Approach
Schritt-für-Schritt-Methode, die der Agent befolgt.

## Capabilities
Detaillierte Erklärung, was der Agent tun kann.

## Guidelines
Richtlinien für das Verhalten des Agents.

## Output Format
Wie der Agent seine Antworten strukturieren sollte.
```

## Registrierungsschritte

Nachdem du deine Agent-Datei erstellt hast, registriere sie im System:

### 1. Statistiken aktualisieren

```bash
# _stats.json
{
  "agents": 66  # Zähler erhöhen
}
```

### 2. Zum Context Router hinzufügen

```json
// _graph/cache/context-router.json
{
  "routes": {
    "validation": {
      "keywords": ["validate", "check", "verify"],
      "primary": {
        "agents": ["validator"]
      }
    }
  }
}
```

### 3. Knowledge Graph Node erstellen

```json
// _graph/knowledge-nodes.json
{
  "id": "agent-validator",
  "type": "agent",
  "name": "validator",
  "description": "Validates code, configs, and data structures",
  "domain": ["quality", "verification"],
  "tags": ["agent", "validation", "quality-control"]
}
```

### 4. Graph Edges hinzufügen

```json
// _graph/edges.json
{
  "from": "agent-validator",
  "to": "command-validate",
  "type": "used_by",
  "strength": 0.9
}
```

### 5. SYSTEM-MAP aktualisieren

```markdown
<!-- .claude/SYSTEM-MAP.md -->
| Agent | Model | Zweck |
|-------|-------|---------|
| validator | haiku | Code- und Konfigurationsvalidierung |
```

## Deinen Agent testen

### Manueller Test

```bash
# Starte einen Task mit deinem Agent
echo "Test validation agent" | claude --agent validator
```

### Via Befehl

Erstelle einen Befehl, der deinen Agent nutzt:

```markdown
---
name: validate
agent: validator
---

Validiere die angegebenen Dateien auf Korrektheit.
```

### Via Delegation

Lass das System zu deinem Agent delegieren:

```markdown
User: "Überprüfe, ob diese Konfiguration gültig ist"
→ Context Scout erkennt "validate"
→ Lädt validator Agent
→ Delegiert Task
```

## Beispiel: Validator Agent erstellen

Lass uns einen vollständigen Validator Agent Schritt für Schritt erstellen.

### Schritt 1: Agent-Datei erstellen

```bash
# .claude/agents/validator.md
```

```markdown
---
name: validator
description: Validates code, configs, and data structures for correctness
model: haiku
capabilities:
  - code_validation
  - schema_checking
  - format_verification
  - style_compliance
tools:
  - Read
  - Bash
  - Grep
  - Glob
---

# Validator Agent

## Role
You are a validation specialist who checks code, configs, and data structures for correctness. You find issues but don't fix them unless asked.

## Approach
1. **Identify**: What needs validation (code, config, data)
2. **Standards**: Determine relevant standards or schemas
3. **Check**: Run appropriate validation tools
4. **Report**: List findings with confidence levels
5. **Suggest**: Provide fix suggestions only if requested

## Capabilities

### Code Validation
- Syntax checking (linters, parsers)
- Style compliance (ESLint, Pylint, etc.)
- Type checking (TypeScript, mypy)
- Import/dependency verification

### Schema Checking
- JSON Schema validation
- TypeScript type definitions
- Database schema consistency
- API contract compliance

### Format Verification
- YAML/TOML/JSON syntax
- Markdown structure
- Configuration file formats
- Data serialization formats

## Guidelines

### DO
- Use appropriate validation tools for the file type
- Report confidence level with each finding (1-100%)
- Distinguish between errors, warnings, and suggestions
- Provide line numbers and context for issues
- Check against project-specific conventions

### DON'T
- Fix issues automatically (only validate)
- Assume standards without checking
- Report false positives as high confidence
- Validate more than requested
- Ignore project-specific rules

## Output Format

```markdown
## Validation Results

**File**: {path}
**Type**: {code|config|data}
**Status**: {PASS|FAIL}

### Errors (blocking issues)
- Line {n}: {description} [Confidence: {%}]

### Warnings (non-blocking issues)
- Line {n}: {description} [Confidence: {%}]

### Suggestions (improvements)
- Line {n}: {description} [Confidence: {%}]
```
```

### Schritt 2: Context Router aktualisieren

Nach Agent-Erstellung registriere ihn im System wie oben beschrieben.

### Schritt 3: Agent testen

Nutze den Agent in Befehlen oder delegiere zu ihm.

## Zusammenhang

- [Befehle schreiben](writing-commands.md) - Befehle, die deinen Agent nutzen
- [System erweitern](extending-system.md) - Integrations-Checkliste
- [Patterns nutzen](using-patterns.md) - Patterns mit Agents anwenden
