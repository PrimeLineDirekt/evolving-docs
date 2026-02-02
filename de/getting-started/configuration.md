# Konfiguration

Lerne wie du das Evolving System für deine Bedürfnisse anpasst.

## Konfigurations-Dateien Überblick

Das Evolving System nutzt mehrere Konfigurations-Dateien, jede mit einem spezifischen Zweck:

| Datei | Zweck | Geltungsbereich |
|------|---------|-------|
| `CLAUDE.md` | Projekt-Level Instruktionen | Pro Projekt |
| `~/.claude/CLAUDE.md` | Globale User-Instruktionen | Alle Projekte |
| `.claude/hooks/*.{sh,py}` | Automation und Quality Gates | Systemweit |
| `_memory/index.json` | Aktiver Context-Tracking | Pro Projekt |
| `_graph/cache/*.json` | Routing und Indexierung | Systemweit |
| `_stats.json` | Komponenten-Inventar | Systemweit |

## CLAUDE.md Anpassung

### Projekt-Level Konfiguration

Erstelle eine `CLAUDE.md` in deinem Projekt-Root um das Verhalten anzupassen:

```markdown
# Mein Projekt

## User: DeinName

Rolle/Kontext über dich

## Session-Verhalten

### Memory-Ort
- Domain Memory: `_memory/`
- Knowledge Base: `knowledge/`

### Projekt-spezifische Regeln
- Immer TypeScript strict mode nutzen
- Bevorzuge functional components in React
- Test-Coverage Minimum: 80%

## Tech Stack
- Frontend: React + TypeScript + Tailwind
- Backend: Node.js + Express
- Datenbank: PostgreSQL + Prisma
- Testing: Vitest + React Testing Library
```

### Globale User-Konfiguration

Deine `~/.claude/CLAUDE.md` gilt für ALLE Projekte:

```markdown
# Global Claude Configuration

## User: Robin

AI-First Developer | Ort | Projekte: X, Y, Z
**Stil**: Sparring > Ja-Sagen | Chain of Thought | 80/20 Fokus

## Core Principles

### Sparring > Ja-Sagen
- Radikale Ehrlichkeit
- Annahmen hinterfragen
- Konstruktive Kritik

### 80/20 Prinzip
- Fokus auf High-Impact
- Over-Engineering vermeiden

## Default-Verhalten
- Immer Reasoning erklären (Chain of Thought)
- Deutsch für Kommunikation, Englisch für Code
- Bevorzuge Delegation für Exploration-Tasks
```

**Priorität**: Projekt `CLAUDE.md` überschreibt globale Einstellungen.

## Hook-Konfiguration

Hooks laufen automatisch um Qualität durchzusetzen und Workflows zu automatisieren.

### Verfügbare Hooks

Befinden sich in `.claude/hooks/`:

| Hook | Trigger | Zweck |
|------|---------|--------|
| `check-comments.py` | Write/Edit | Verhindere Over-Commenting (>25%) |
| `delegation-enforcer.py` | Session-Ende | Tracke Delegation-Gaps |
| `auto-cross-reference.sh` | Write/Edit | Erkenne Doc-Sync-Bedarf |
| `session-summary.sh` | Session-Ende | Erstelle Handoff falls Arbeit geleistet |
| `todo-enforcer.sh` | Session-Ende | Warne über unvollständige Todos |

### Hooks konfigurieren

Hooks nutzen Konfiguration aus ihren Docstrings oder separaten Config-Dateien:

**Beispiel: check-comments.py Threshold**
```python
# .claude/hooks/check-comments.py
MAX_COMMENT_RATIO = 0.25  # 25% max

# Zum Anpassen:
# Editiere diesen Wert direkt in der Hook-Datei
```

**Beispiel: delegation-enforcer.py Config**
```python
# Nutzt _graph/cache/delegation-config.json
{
  "task_types": {
    "exploration": {
      "agent": "Explore",
      "model": "haiku",
      "keywords": ["find", "search", "explore"]
    }
  }
}
```

### Hooks deaktivieren

Um einen Hook temporär zu deaktivieren:

```bash
# Umbenennen mit .disabled Extension
mv .claude/hooks/check-comments.py .claude/hooks/check-comments.py.disabled
```

Um wieder zu aktivieren:
```bash
mv .claude/hooks/check-comments.py.disabled .claude/hooks/check-comments.py
```

**Warnung**: Deaktivieren von Quality-Hooks (`check-comments.py`) kann zu verschlechterter Code-Qualität führen.

## MCP Server Setup

Das Evolving System kann mit MCP (Model Context Protocol) Servern für erweiterte Fähigkeiten integriert werden.

### Firecrawl Integration

Für Web Scraping und Content-Extraktion:

```bash
# MCP Server installieren
npm install -g @modelcontextprotocol/server-firecrawl

# In Claude Code Einstellungen konfigurieren
# Zu ~/.claude/mcp-servers.json hinzufügen:
{
  "firecrawl": {
    "command": "mcp-server-firecrawl",
    "env": {
      "FIRECRAWL_API_KEY": "dein-api-key"
    }
  }
}
```

**Nutzung**: Tools wie `firecrawl_scrape`, `firecrawl_search` werden verfügbar.

### Custom MCP Server

Erstelle projekt-spezifische MCP Server:

```bash
# In deinem Projekt
mkdir mcp-servers
cd mcp-servers

# Server erstellen
npm init -y
npm install @modelcontextprotocol/sdk

# server.js implementieren
# In ~/.claude/mcp-servers.json registrieren
```

Siehe [MCP Dokumentation](https://modelcontextprotocol.io/) für Details.

## Memory System Setup

### Projekt-Memory Initialisierung

Erstelle Memory-Struktur für ein neues Projekt:

```bash
# Verzeichnisse erstellen
mkdir -p _memory/projects
mkdir -p _memory/analytics
mkdir -p _memory/experiences

# Index erstellen
cat > _memory/index.json << 'EOF'
{
  "active_context": {
    "project": "mein-projekt",
    "workflow": null,
    "last_updated": "2024-02-03T10:00:00Z"
  }
}
EOF

# Projekt-Memory erstellen
cat > _memory/projects/mein-projekt.json << 'EOF'
{
  "name": "mein-projekt",
  "description": "Projekt-Beschreibung",
  "current_phase": "Setup",
  "goals": [],
  "features": {},
  "state": {
    "current_phase": "Setup",
    "blockers": []
  },
  "progress": [],
  "failures": []
}
EOF
```

Oder nutze den `/project-new` Command um dies zu automatisieren.

### Experience Memory Konfiguration

Experiences zerfallen über Zeit basierend auf Trust und Relevanz:

**Decay-Konfiguration** in `_memory/experiences/SCHEMA.md`:
```markdown
Decay-Faktoren:
- trust_level: high (1.0), medium (0.8), low (0.5)
- age_factor: Exponentieller Zerfall über 30 Tage
- effective_relevance = base * decay * trust
```

**Standard-Thresholds**:
- Lade Experiences mit `effective_relevance > 30`
- Archiviere falls `< 10` und Alter > 60 Tage

Zum Anpassen, modifiziere die Bootup-Logik in `.claude/rules/domain-memory-bootup.md`.

### Knowledge Graph Setup

Der Knowledge Graph benötigt initiale Indexierung:

```bash
# Indices generieren (zukünftige Automation)
# Aktuell: Stelle sicher dass diese Dateien existieren:
ls _graph/
# Sollte zeigen:
# - nodes.json
# - edges.json
# - taxonomy.json
# - index/by-type.json
# - index/by-domain.json
# - cache/context-router.json
```

Aktualisiere `_graph/cache/context-router.json` um Keyword-Routing anzupassen:

```json
{
  "routes": {
    "debugging": {
      "keywords": ["debug", "bug", "error", "fix"],
      "primary": [
        "knowledge/rules/debugging/observe-before-editing.md",
        "knowledge/rules/debugging/evidence-before-claims.md"
      ],
      "secondary": [
        "knowledge/patterns/systematic-debugging-pattern.md"
      ]
    }
  }
}
```

## Erweiterte Konfiguration

### Task-Persistenz

Aktiviere persistente Task-Listen über Terminal-Sessions:

```bash
# Zu ~/.bashrc oder ~/.zshrc hinzufügen
export CLAUDE_CODE_TASK_LIST_ID=evolving

# Neu laden
source ~/.bashrc
```

**Effekt**: Tasks überleben Terminal-Schließung und Wiedereröffnung.

### Context Budget Limits

Konfiguriere Degradation-Thresholds in `_graph/cache/orchestration-config.json`:

```json
{
  "context_thresholds": {
    "warning": 0.7,
    "critical": 0.85,
    "max_summary_only": 0.9
  },
  "model_limits": {
    "opus": 200000,
    "sonnet": 180000
  }
}
```

### Delegation-Scoring

Passe Delegation-Entscheidungen an in `_graph/cache/delegation-config.json`:

```json
{
  "score_factors": {
    "scope_multi_file": 2,
    "bulk_operation": 2,
    "research_task": 2
  },
  "score_threshold": 3,
  "task_types": {
    "exploration": {
      "agent": "Explore",
      "model": "haiku",
      "traits": null
    }
  }
}
```

### Plain-Text Detection Tuning

Passe Command-Detection Confidence an in `.claude/detection-index.json`:

```json
{
  "commands": [
    {
      "name": "idea-new",
      "triggers": ["neue idee", "ich habe eine idee"],
      "confidence_boost": 10,
      "anti_patterns": ["keine ideen", "schlechte idee"]
    }
  ]
}
```

**Confidence-Levels**:
- `9-10`: Auto-Suggest (hohe Confidence)
- `6-8`: User fragen (mittel)
- `1-5`: Ignorieren (niedrig)

## Konfigurations-Best-Practices

### Tu das
- Halte Projekt-`CLAUDE.md` fokussiert auf projekt-spezifische Regeln
- Nutze globale `~/.claude/CLAUDE.md` für persönliche Präferenzen
- Teste Hook-Änderungen zuerst an unkritischen Dateien
- Dokumentiere custom MCP Server im Projekt-README
- Version-Kontrolle `CLAUDE.md` und `_memory/` Struktur

### Tu das nicht
- API-Keys in Konfiguration hardcoden (nutze Umgebungsvariablen)
- Hooks deaktivieren ohne ihren Zweck zu verstehen
- Manuell `_stats.json` editieren (lass Hooks es verwalten)
- Hook-Warnungen ignorieren - sie verhindern Probleme
- Über-Konfigurieren - starte einfach, füge bei Bedarf hinzu

## Validierung

Nach Konfigurations-Änderungen, verifiziere:

```bash
# Prüfe ob Symlinks noch funktionieren
ls -la ~/.claude/

# Verifiziere dass Hooks ausführbar sind
ls -la .claude/hooks/*.{sh,py}

# Teste Memory-Bootup
# Starte Claude Code und prüfe auf:
# "Projekt: {name} | Phase: {phase}"

# Verifiziere MCP Server
# In Claude Code Session:
# Prüfe ob verfügbare Tools MCP-bereitgestellte enthalten
```

## Nächste Schritte

- [Core Concepts](../core-concepts/index.md) - System verstehen
- [Architektur](../architecture/index.md) - Wie alles zusammenpasst
- [Guides](../guides/creating-commands.md) - Custom-Komponenten erstellen

## Problemlösung

### "Konfiguration nicht geladen"

**Problem**: Projekt-`CLAUDE.md` Änderungen nicht reflektiert

**Lösung**: Starte Claude Code Session neu - Config wird beim Start gelesen.

### "Hook fehlgeschlagen mit Import-Fehler"

**Problem**: Python-Dependencies fehlen

**Lösung**:
```bash
# Python-Version prüfen
python --version  # Muss 3.12+ sein

# Hook-Syntax verifizieren
python .claude/hooks/check-comments.py --help
```

### "MCP Server antwortet nicht"

**Problem**: MCP Tools nicht verfügbar

**Lösung**:
```bash
# Prüfe ob Server läuft
ps aux | grep mcp-server

# Prüfe Konfiguration
cat ~/.claude/mcp-servers.json

# Claude Code neu starten
```

## Konfigurations-Checkliste

Bevor du mit Entwicklung beginnst:

- [ ] Projekt-`CLAUDE.md` erstellt und angepasst
- [ ] Globale `~/.claude/CLAUDE.md` reflektiert deine Präferenzen
- [ ] Hooks sind ausführbar (`chmod +x`)
- [ ] Memory-Struktur initialisiert (`_memory/`)
- [ ] Knowledge Graph indexiert (`_graph/`)
- [ ] MCP Server konfiguriert (falls benötigt)
- [ ] Task-Persistenz aktiviert (optional)
- [ ] Konfiguration validiert

Du bist jetzt bereit das vollständig konfigurierte Evolving System zu nutzen!
