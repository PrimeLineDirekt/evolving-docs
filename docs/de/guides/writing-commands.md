# Befehle schreiben

Befehle sind die primäre Möglichkeit, wie Benutzer mit dem Evolving-System interagieren. Diese Anleitung zeigt dir, wie du leistungsstarke, auffindbare Befehle erstellst, die nahtlos integriert werden.

## Befehls-Dateistruktur

Befehle befinden sich in `.claude/commands/` und verwenden Markdown-Format mit YAML-Frontmatter:

```markdown
---
name: status
description: Show current project status and health
allowed-tools:
  - Read
  - Bash
  - Grep
args:
  - name: detail
    description: Level of detail (quick|full)
    required: false
    default: quick
---

# Status Command

## Purpose
Display the current state of the active project including progress, issues, and next steps.

## Steps

1. **Load Domain Memory**
   - Read `_memory/index.json` → active project
   - Read `_memory/projects/{active}.json` → state

2. **Check Git Status**
   - Run `git status --short`
   - Count uncommitted changes

3. **Analyze Task State**
   - Load active tasks (if any)
   - Count pending vs completed

4. **Report Health**
   - Recent failures
   - Known blockers
   - Recommendations

## Output Format

```
📊 Project: {name}
Phase: {current_phase}
Progress: {completed}/{total} features

🔧 Uncommitted Changes: {count}
📋 Active Tasks: {pending}/{total}

⚠️ Issues: {count}
💡 Next: {recommendation}
```

## Examples

```bash
# Quick status (default)
/status

# Detailed status
/status full
```
```

## Erforderliche Frontmatter-Felder

| Feld | Typ | Erforderlich | Beschreibung |
|-------|------|----------|-------------|
| `name` | string | ✅ | Befehlsname (Kleinbuchstaben, kein Schrägstrich) |
| `description` | string | ✅ | Was der Befehl tut (1-2 Sätze) |
| `allowed-tools` | array | ❌ | Tools, die der Befehl nutzen kann |
| `args` | array | ❌ | Befehlsargumente/Optionen |
| `agent` | string | ❌ | Vordefinierter Agent zum Delegieren |

## Argumente und Optionen

Definiere Befehlsargumente für Flexibilität:

```yaml
args:
  - name: target          # Positionelles Argument
    description: Was zu analysieren
    required: true

  - name: depth           # Optionales Argument mit Standard
    description: Analysetiefe
    required: false
    default: shallow

  - name: format          # Auswahlargument
    description: Ausgabeformat
    required: false
    default: markdown
    choices: [markdown, json, yaml]
```

**Verwendung:**
```bash
/analyze src/auth.ts          # Nur target
/analyze src/auth.ts deep     # target + depth
/analyze src/auth.ts deep json # Alle Argumente
```

## Befehls-Body-Struktur

Definiere nach dem Frontmatter das Befehlsverhalten:

```markdown
# {Befehlsname}

## Purpose
Warum dieser Befehl existiert und welches Problem er löst.

## Steps
1. **Schritttitel**: Was zu tun ist
   - Details
   - Unterabschnitte

2. **Nächster Schritt**: Weiter...

## Output Format
Wie Ergebnisse dem Benutzer präsentiert werden sollten.

## Examples
Konkrete Verwendungsbeispiele mit Erklärungen.

## Notes
Spezialfälle, Warnungen oder zusätzlicher Kontext.
```

## Detection Index Registrierung

Mache deinen Befehl durch natürliche Sprache auffindbar:

### 1. Zum Detection Index hinzufügen

```json
// .claude/detection-index.json
{
  "commands": [
    {
      "name": "status",
      "triggers": [
        "status",
        "project status",
        "current state",
        "what's the status",
        "show me progress"
      ],
      "confidence": {
        "high": ["status", "project status"],
        "medium": ["current state", "show progress"],
        "low": ["what's going on", "update"]
      }
    }
  ]
}
```

### 2. Vertrauensstufen

| Level | Vertrauen | Verhalten |
|-------|------------|----------|
| **high** | 90-100% | Biete Befehl sofort an |
| **medium** | 60-89% | Frage "Meinst du /befehl?" |
| **low** | 30-59% | Nicht vorschlagen (mehrdeutig) |

### 3. Trigger-Muster

```json
{
  "triggers": [
    "exact phrase",                    // Exakte Übereinstimmung
    "pattern with {variable}",         // Variablenteile
    "starts with this",                // Präfix-Übereinstimmung
    "contains keyword anywhere"        // Enthält Übereinstimmung
  ]
}
```

## Integrations-Schritte

Nachdem du deinen Befehl erstellt hast, integriere ihn:

### 1. Statistiken aktualisieren

```json
// _stats.json
{
  "commands": 64  // Zähler erhöhen
}
```

### 2. Zum Context Router hinzufügen

```json
// _graph/cache/context-router.json
{
  "routes": {
    "project-status": {
      "keywords": ["status", "progress", "health"],
      "primary": {
        "commands": ["/status"]
      }
    }
  }
}
```

### 3. Knowledge Graph Node erstellen

```json
// _graph/knowledge-nodes.json
{
  "id": "command-status",
  "type": "command",
  "name": "/status",
  "description": "Show current project status",
  "domain": ["project-management"],
  "tags": ["command", "status", "reporting"]
}
```

### 4. Graph Edges hinzufügen

```json
// _graph/edges.json
{
  "from": "command-status",
  "to": "memory-domain",
  "type": "reads_from",
  "strength": 1.0
}
```

### 5. COMMANDS.md aktualisieren

```markdown
<!-- .claude/COMMANDS.md -->
### /status
Zeige aktuellen Projektstatus und Systemgesundheit an.

**Args**: `[detail]` (quick|full)
**Beispiel**: `/status full`
```

## Befehlstypen

### 1. Query Befehle
Lese und berichte Informationen (keine Nebenwirkungen).

```yaml
name: list-agents
allowed-tools: [Read, Grep]
```

### 2. Action Befehle
Führe Operationen durch (ändere Status).

```yaml
name: create-agent
allowed-tools: [Write, Edit, Bash]
```

### 3. Delegation Befehle
Delegiere zu spezialisierten Agents.

```yaml
name: review-code
agent: code-reviewer
```

### 4. Workflow Befehle
Multi-Schritt-Orchestrierung.

```yaml
name: feature-complete
allowed-tools: [Read, Write, Bash, Task]
```

## Richtlinien

### TU das

- ✅ Mit klarem Zweck beginnen
- ✅ In nummerierte Schritte unterteilen
- ✅ Ausgabeformat spezifizieren
- ✅ Verwendungsbeispiele liefern
- ✅ Grenzfälle handhaben
- ✅ Im Detection Index registrieren
- ✅ Zum Knowledge Graph hinzufügen

### TU DAS NICHT

- ❌ Befehle zu viel tun lassen
- ❌ Tools nicht als erlaubt angeben
- ❌ Fehlerbehandlung überspringen
- ❌ Vergiss nicht, Statistiken zu aktualisieren
- ❌ Destruktive Operationen ohne Bestätigung nutzen
- ❌ Befehlfunktionalität duplizieren

## Beispiel: Status Befehl erstellen

Lass uns einen kompletten Status Befehl Schritt für Schritt erstellen.

### Schritt 1: Befehlsdatei erstellen

```bash
# .claude/commands/status.md
```

```markdown
---
name: status
description: Show current project status, progress, and health metrics
allowed-tools:
  - Read
  - Bash
  - Grep
args:
  - name: detail
    description: Level of detail (quick|full)
    required: false
    default: quick
---

# Status Command

## Purpose
Provide a quick overview of the current project state including progress, git status, active tasks, and any issues or blockers.

## Steps

### 1. Load Domain Memory
```bash
Read _memory/index.json
Extract: active_context.project
```

```bash
Read _memory/projects/{active}.json
Extract:
  - goals
  - current_phase
  - features (status counts)
  - recent_progress (last 3 entries)
  - known failures
```

### 2. Check Git Status
```bash
Bash: git status --short --branch
Count:
  - Uncommitted changes (M, A, D)
  - Untracked files (??)
  - Branch ahead/behind
```

### 3. Load Active Tasks (if exists)
```bash
TaskList
Count:
  - Pending tasks
  - In-progress tasks
  - Completed tasks (this session)
```

### 4. Analyze Health

**Signals:**
- Recent failures > 2 → ⚠️ Warning
- Uncommitted changes > 10 → 💡 Suggest commit
- No progress entries recent → 💡 Suggest update

### 5. Generate Report

**Quick Mode:**
```
📊 Project: {name}
Phase: {current_phase}
Features: {passing}/{total} passing

🔧 Changes: {uncommitted}
📋 Tasks: {pending} pending

Next: {next_step}
```

**Full Mode:**
```
📊 PROJECT STATUS

Project: {name}
Phase: {current_phase}
Started: {start_date}

🎯 GOALS
{goals list}

✨ FEATURES ({passing}/{total} passing)
✅ {passing features}
🔄 {in_progress features}
❌ {failing features}

📝 RECENT PROGRESS
{last 3 progress entries}

🔧 GIT STATUS
Branch: {branch} [{ahead/behind}]
Uncommitted: {count}
Untracked: {count}

📋 ACTIVE TASKS
Pending: {count}
In Progress: {count}
Completed: {count}

⚠️ ISSUES
{known failures}

💡 NEXT STEPS
{next_step recommendations}
```

## Examples

```bash
# Quick status
/status

# Full detailed status
/status full
```

## Notes

- Gracefully handle missing files (fresh project)
- Show "No active project" if index.json missing
- Cache-friendly (reads only, no writes)
```

### Schritt 2: Im Detection Index registrieren

```json
// .claude/detection-index.json
{
  "commands": [
    {
      "name": "status",
      "triggers": [
        "status",
        "project status",
        "current status",
        "what's the status",
        "show me status",
        "show progress",
        "project health",
        "where are we"
      ],
      "confidence": {
        "high": ["status", "project status", "/status"],
        "medium": ["current status", "show progress", "project health"],
        "low": ["where are we", "what's up"]
      }
    }
  ]
}
```

### Schritt 3: Befehl testen

```bash
# Direkte Invokation
/status

# Natürliche Sprache (sollte erkennen)
"Show me the project status"
→ Claude: "Did you mean /status?"

# Mit Argumenten
/status full
```

## Zusammenhang

- [Agents erstellen](creating-agents.md) - Für Delegation Befehle
- [Patterns nutzen](using-patterns.md) - Patterns in Befehlen anwenden
- [System erweitern](extending-system.md) - Integrations-Checkliste
