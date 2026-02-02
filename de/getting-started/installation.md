# Installation

Diese Anleitung führt dich durch die Installation und Einrichtung des Evolving Systems.

## Voraussetzungen

Bevor du beginnst, stelle sicher, dass folgendes installiert ist:

- **Claude Code CLI**: Das offizielle Claude CLI Tool
  - Installation: `npm install -g @anthropic-ai/claude-code`
  - Verifizierung: `claude --version`

- **Git**: Für Versionskontrolle und Repository-Cloning
  - Verifizierung: `git --version`

- **Python 3.12+**: Erforderlich für Hooks und Automation Scripts
  - Verifizierung: `python --version`

- **Node.js 18+**: Für MCP Server und einige Automatisierungen
  - Verifizierung: `node --version`

## Installationsschritte

### 1. Repository klonen

```bash
# Clone an deinen bevorzugten Ort
cd ~/Buisiness  # oder dein bevorzugtes Verzeichnis
git clone <repository-url> Evolving
cd Evolving
```

### 2. Symlinks erstellen

Das Evolving System nutzt Symlinks, um Komponenten global über alle Projekte verfügbar zu machen.

```bash
# Symlink-Verzeichnis erstellen falls nicht vorhanden
mkdir -p ~/.claude

# Symlinks für alle Komponenten erstellen
ln -s "$(pwd)/.claude/commands" ~/.claude/commands
ln -s "$(pwd)/.claude/agents" ~/.claude/agents
ln -s "$(pwd)/.claude/skills" ~/.claude/skills
ln -s "$(pwd)/.claude/rules" ~/.claude/rules
ln -s "$(pwd)/.claude/blueprints" ~/.claude/blueprints
ln -s "$(pwd)/.claude/hooks" ~/.claude/hooks
```

**Warum Symlinks?**
- Macht alle 47+ Commands in jedem Projekt verfügbar
- Zentralisiert Updates - einmal ändern, überall wirksam
- Ermöglicht projektspezifische Overrides bei Bedarf

### 3. Installation verifizieren

```bash
# Symlinks prüfen
ls -la ~/.claude/

# Du solltest sehen:
# commands -> /pfad/zu/Evolving/.claude/commands
# agents -> /pfad/zu/Evolving/.claude/agents
# skills -> /pfad/zu/Evolving/.claude/skills
# rules -> /pfad/zu/Evolving/.claude/rules
# blueprints -> /pfad/zu/Evolving/.claude/blueprints
# hooks -> /pfad/zu/Evolving/.claude/hooks

# Komponenten-Anzahl prüfen
wc -l _stats.json

# Sollte Stats für alle Komponenten zeigen
```

### 4. Umgebungsvariablen einrichten (Optional)

Für persistente Task-Listen über Sessions hinweg:

```bash
# Zu ~/.bashrc oder ~/.zshrc hinzufügen
export CLAUDE_CODE_TASK_LIST_ID=evolving

# Shell neu laden
source ~/.bashrc  # oder source ~/.zshrc
```

## Problemlösung

### Symlinks funktionieren nicht

**Problem**: Commands werden in neuen Projekten nicht erkannt

**Lösung**:
```bash
# Symlinks verifizieren
ls -la ~/.claude/

# Falls defekt, neu erstellen
rm -rf ~/.claude/commands ~/.claude/agents  # etc.
# Dann Schritt 2 erneut ausführen
```

### Python-Versionsprobleme

**Problem**: Hooks schlagen mit Import-Fehlern fehl

**Lösung**:
```bash
# Python-Version prüfen
python --version

# Falls < 3.12, neuere Version installieren
# macOS mit Homebrew:
brew install python@3.12

# PATH aktualisieren falls nötig
export PATH="/opt/homebrew/opt/python@3.12/bin:$PATH"
```

### Berechtigungsfehler

**Problem**: Kann keine Symlinks erstellen oder Hooks ausführen

**Lösung**:
```bash
# Hooks ausführbar machen
chmod +x .claude/hooks/*.sh
chmod +x .claude/hooks/*.py

# Falls Symlink-Erstellung fehlschlägt, Verzeichnisberechtigungen prüfen
ls -la ~/.claude/
```

### Detection Index nicht gefunden

**Problem**: Plain-Text Command Detection funktioniert nicht

**Lösung**:
```bash
# Detection Index verifizieren
cat .claude/detection-index.json

# Falls fehlend, neu generieren (Command kommt in zukünftiger Version)
# Aktuell: Stelle sicher, dass du das vollständige Repository geklont hast
```

## Nächste Schritte

- [Quick Start Guide](./quick-start.md) - Deine erste Session
- [Konfiguration](./configuration.md) - System anpassen
- [Architektur-Überblick](../architecture/index.md) - System verstehen

## Verifizierungs-Checkliste

Bevor du fortfährst, verifiziere:

- [ ] Claude Code CLI installiert und verfügbar
- [ ] Repository erfolgreich geklont
- [ ] Symlinks in `~/.claude/` erstellt
- [ ] Python 3.12+ verfügbar
- [ ] Hooks sind ausführbar (`chmod +x`)
- [ ] `_stats.json` lesbar und enthält Komponenten-Counts
- [ ] `.claude/detection-index.json` existiert

Wenn alle Prüfungen bestanden sind, bist du bereit für den [Quick Start Guide](./quick-start.md)!
