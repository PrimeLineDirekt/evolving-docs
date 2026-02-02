# System erweitern

Das Evolving-System ist für Wachstum ausgelegt. Diese Anleitung zeigt dir, wie du neue Komponenten hinzufügst und dabei die Konsistenz im gesamten System aufrechterhältst.

## Integrations-Matrix

Wenn du eine neue Komponente hinzufügst, muss sie an **mehreren Stellen** registriert werden, um vollständig integriert zu sein.

### Die 7 Registrierungspunkte

| # | Datei | Zweck |
|---|------|---------|
| 1 | `_stats.json` | Zähler aktualisieren (Single Source of Truth) |
| 2 | `_graph/cache/context-router.json` | Via Keywords auffindbar machen |
| 3 | `.claude/detection-index.json` | Natural Language Triggering aktivieren |
| 4 | `_graph/knowledge-nodes.json` | Entity zum Knowledge Graph hinzufügen |
| 5 | `_graph/edges.json` | Mit verwandten Entities verbinden |
| 6 | `.claude/SYSTEM-MAP.md` | Zum Inventar + Changelog hinzufügen |
| 7 | `knowledge/index.md` | Zum KB Index hinzufügen (falls applicable) |

### Was braucht was?

| Komponenten-Typ | 1 | 2 | 3 | 4 | 5 | 6 | 7 |
|----------------|---|---|---|---|---|---|---|
| **Command** | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | - |
| **Agent** | ✅ | ✅ | - | ✅ | ✅ | ✅ | - |
| **Skill** | ✅ | ✅ | - | ✅ | ✅ | ✅ | - |
| **Template** | ✅ | ✅ | - | ✅ | ✅ | ✅ | ✅ |
| **Pattern** | ✅ | ✅ | - | ✅ | ✅ | - | ✅ |
| **Learning** | ✅ | ✅ | - | ✅ | ✅ | - | ✅ |
| **Hook** | ✅ | - | - | - | - | ✅ | - |
| **Rule** | ✅ | ✅ | - | ✅ | - | ✅ | - |
| **Blueprint** | ✅ | ✅ | - | ✅ | ✅ | ✅ | - |

## Schritt-für-Schritt: Einen Command hinzufügen

Lass uns einen kompletten Command zum System hinzufügen.

### 1. Command-Datei erstellen

```bash
# .claude/commands/my-command.md
```

```markdown
---
name: my-command
description: Does something useful
allowed-tools:
  - Read
  - Bash
---

# My Command

## Purpose
Explain what it does and why.

## Steps
1. Do this
2. Then that
3. Finally this
```

### 2. Statistiken aktualisieren

```json
// _stats.json
{
  "commands": 64  // War 63, jetzt 64
}
```

### 3. Context Router Eintrag hinzufügen

```json
// _graph/cache/context-router.json
{
  "routes": {
    "my-feature": {
      "keywords": ["my", "feature", "useful"],
      "primary": {
        "commands": ["/my-command"]
      },
      "confidence_boost": 10
    }
  }
}
```

### 4. Detection Trigger hinzufügen

```json
// .claude/detection-index.json
{
  "commands": [
    {
      "name": "my-command",
      "triggers": [
        "my command",
        "do my thing",
        "run my feature"
      ],
      "confidence": {
        "high": ["my command", "/my-command"],
        "medium": ["do my thing"],
        "low": ["my feature"]
      }
    }
  ]
}
```

### 5. Knowledge Node erstellen

```json
// _graph/knowledge-nodes.json
{
  "nodes": [
    {
      "id": "command-my-command",
      "type": "command",
      "name": "/my-command",
      "description": "Does something useful",
      "domain": ["utilities"],
      "tags": ["command", "utility", "helper"],
      "created": "2026-02-03"
    }
  ]
}
```

### 6. Graph Edges hinzufügen

```json
// _graph/edges.json
{
  "edges": [
    {
      "from": "command-my-command",
      "to": "agent-helper",
      "type": "delegates_to",
      "strength": 0.8
    },
    {
      "from": "command-my-command",
      "to": "pattern-react",
      "type": "applies",
      "strength": 0.6
    }
  ]
}
```

### 7. SYSTEM-MAP aktualisieren

```markdown
<!-- .claude/SYSTEM-MAP.md -->

## Commands (64)

| Command | Zweck |
|---------|---------|
| /my-command | Does something useful |
| ... | ... |

## Changelog

### 2026-02-03
- Hinzugefügt `/my-command` für nützliche Funktionalität
```

### 8. Integration testen

```bash
# Direkte Invokation
/my-command

# Natürliche Sprache
"Run my command"
→ Sollte /my-command erkennen und anbieten

# Via Context Scout
User erwähnt "my feature"
→ Context Router sollte Command laden
```

## Schritt-für-Schritt: Einen Agent hinzufügen

### 1. Agent-Datei erstellen

```bash
# .claude/agents/my-agent.md
```

```markdown
---
name: my-agent
description: Specialized agent for X
model: sonnet
capabilities:
  - capability_1
  - capability_2
tools:
  - Read
  - Bash
---

# My Agent

## Role
You are a specialist in X.

## Approach
1. Analyze
2. Execute
3. Report
```

### 2. Statistiken aktualisieren

```json
// _stats.json
{
  "agents": 66  // War 65, jetzt 66
}
```

### 3. Context Router Eintrag hinzufügen

```json
// _graph/cache/context-router.json
{
  "routes": {
    "my-specialty": {
      "keywords": ["specialty", "expert"],
      "primary": {
        "agents": ["my-agent"]
      }
    }
  }
}
```

### 4. Knowledge Node erstellen

```json
// _graph/knowledge-nodes.json
{
  "id": "agent-my-agent",
  "type": "agent",
  "name": "my-agent",
  "description": "Specialized agent for X",
  "domain": ["specialty"],
  "tags": ["agent", "specialist"],
  "model": "sonnet"
}
```

### 5. Graph Edges hinzufügen

```json
// _graph/edges.json
{
  "from": "agent-my-agent",
  "to": "command-analyze",
  "type": "used_by",
  "strength": 0.9
}
```

### 6. SYSTEM-MAP aktualisieren

```markdown
<!-- .claude/SYSTEM-MAP.md -->

## Agents (66)

| Agent | Model | Zweck |
|-------|-------|---------|
| my-agent | sonnet | Spezialisiert auf X |
```

### 7. Delegation Config hinzufügen

```json
// _graph/cache/delegation-config.json
{
  "task_types": {
    "my_specialty": {
      "agent": "my-agent",
      "model": "sonnet",
      "keywords": ["specialty", "expert"]
    }
  }
}
```

## Schritt-für-Schritt: Ein Pattern hinzufügen

### 1. Pattern-Datei erstellen

```bash
# knowledge/patterns/my-pattern.md
```

```markdown
# My Pattern

## Core Loop
1. Step 1
2. Step 2
3. Repeat

## When to Use
Situations where this excels.

## When NOT to Use
Anti-patterns.
```

### 2. Statistiken aktualisieren

```json
// _stats.json
{
  "patterns": 8  // Erhöhen
}
```

### 3. Context Router Eintrag hinzufügen

```json
// _graph/cache/context-router.json
{
  "routes": {
    "my-approach": {
      "keywords": ["approach", "methodology"],
      "primary": {
        "patterns": ["my-pattern"]
      }
    }
  }
}
```

### 4. Knowledge Node erstellen

```json
// _graph/knowledge-nodes.json
{
  "id": "pattern-my-pattern",
  "type": "pattern",
  "name": "my-pattern",
  "description": "Pattern for X",
  "domain": ["methodology"],
  "tags": ["pattern", "approach"]
}
```

### 5. Graph Edges hinzufügen

```json
// _graph/edges.json
{
  "from": "pattern-my-pattern",
  "to": "pattern-related",
  "type": "similar_to",
  "strength": 0.7
}
```

### 6. Knowledge Index aktualisieren

```markdown
<!-- knowledge/index.md -->

## Patterns

- [My Pattern](patterns/my-pattern.md) - Pattern for X
```

### 7. Pattern Zusammenfassung erstellen

```json
// .claude/summaries/patterns/my-pattern.json
{
  "name": "my-pattern",
  "description": "Pattern for X",
  "core_loop": "Step 1 → Step 2 → Repeat",
  "when_to_use": ["Situation A", "Situation B"],
  "when_not": ["Anti-pattern"],
  "related": ["related-pattern"]
}
```

## Neue Komponenten-Typen hinzufügen

Um einen völlig neuen Komponenten-Typ hinzuzufügen:

### 1. Komponenten Schema definieren

```markdown
<!-- knowledge/references/schemas/my-type-schema.md -->

# My Type Schema

## Required Fields
- name (string)
- description (string)
- ...

## Optional Fields
- ...

## File Structure
File location and format
```

### 2. Stats Schema aktualisieren

```json
// _stats.json
{
  "my_types": 0  // Neuen Zähler hinzufügen
}
```

### 3. Zum Context Router hinzufügen

```json
// _graph/cache/context-router.json
{
  "component_types": {
    "my_type": {
      "primary_key": "my_types",
      "file_pattern": "path/to/*.md"
    }
  }
}
```

### 4. Node-Typ definieren

```json
// _graph/knowledge-nodes.json
{
  "node_types": {
    "my_type": {
      "required_fields": ["id", "name", "description"],
      "optional_fields": ["domain", "tags"]
    }
  }
}
```

### 5. Template erstellen

```bash
# knowledge/templates/my-type-template.md
```

### 6. In SYSTEM-MAP dokumentieren

```markdown
<!-- .claude/SYSTEM-MAP.md -->

## My Types (0)

New component type for...

| Name | Description |
|------|-------------|
| TBD | TBD |
```

## Deine Erweiterung testen

### 1. Verifikations-Checkliste

Nach dem Hinzufügen einer Komponente, überprüfe:

- [ ] Stats Zähler aktualisiert
- [ ] Context Router hat Eintrag
- [ ] Detection Index hat Trigger (falls Command)
- [ ] Knowledge Graph Node existiert
- [ ] Edges verbinden zu verwandten Nodes
- [ ] SYSTEM-MAP.md aktualisiert
- [ ] KB Index aktualisiert (falls applicable)

### 2. Integrations-Tests

```bash
# Teste Context Router
"Use my feature"
→ Sollte deine Komponente laden

# Teste Detection (Commands)
"Run my command"
→ Sollte /my-command anbieten

# Teste Graph Abfragen
# Überprüfe ob Node erreichbar ist
grep "my-component" _graph/knowledge-nodes.json
grep "my-component" _graph/edges.json
```

### 3. Konsistenz-Check

Führe den eingebauten Konsistenz-Checker aus:

```bash
/check-consistency
```

Dies validiert:
- Stats entsprechen aktuellen Dateianzahl
- Alle Router-Einträge haben entsprechende Dateien
- Alle Graph-Nodes haben gültige Referenzen
- Keine verwaisten Edges

## Konsistenz bewahren

### Automatisierte Hooks

Das System hat Hooks, die Konsistenz durchsetzen:

```bash
# .claude/hooks/auto-cross-reference.sh
# Trigger bei Dateierstellung/Löschung
# Erinnert an Master-Docs Aktualisierung
```

### Manuelles Audit

Überprüfe regelmäßig Konsistenz:

```bash
# Zähle aktuelle Dateien vs Stats
ls .claude/commands/*.md | wc -l
# Vergleiche mit _stats.json "commands" Wert

# Überprüfe Router-Abdeckung
# Jeder Command sollte Router-Eintrag haben
```

### Update-Strategie

Bei Aktualisierung mehrerer Dateien:

1. **Batch Updates**: Aktualisiere alle 7 Punkte in einer Session
2. **Atomare Commits**: Ein Commit pro hinzugefügte Komponente
3. **Verifikation**: Teste vorher und nachher
4. **Dokumentation**: Aktualisiere Changelog

## Häufige Fallstricke

### ❌ Partielle Integration

```
Command-Datei erstellt ✅
Stats aktualisiert ✅
Context Router vergessen ❌
→ Komponente unsichtbar für Context Scout!
```

### ❌ Inkonsistente Benennung

```
Datei: my-cool-command.md
Node ID: command-my_cool_cmd
Router: "my-command"
→ Nichts funktioniert zusammen!
```

### ❌ Fehlende Edges

```
Node erstellt ✅
Keine Edges ❌
→ Komponente isoliert, keine Beziehungen!
```

### ❌ Veraltete Stats

```
3 Commands hinzugefügt
Zähler aktualisierung vergessen
→ Stats weichen ab von Realität!
```

## Zusammenhang

- [Agents erstellen](creating-agents.md) - Agent-spezifische Integration
- [Befehle schreiben](writing-commands.md) - Befehl-spezifische Integration
- [Architektur Überblick](../architecture/index.md) - System-Struktur
- [Knowledge Graph](../architecture/knowledge-graph.md) - Graph Details
