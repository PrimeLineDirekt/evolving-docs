---
title: Erste Schritte
description: In Minuten mit Evolving durchstarten
---

# Erste Schritte

Diese Anleitung hilft dir bei der Installation, Konfiguration und den ersten Schritten mit dem Evolving System.

## Voraussetzungen

Bevor du beginnst, stelle sicher dass du hast:

- **Claude Code CLI** installiert und authentifiziert
- **Git** zum Klonen des Repositories
- **Python 3.12+** für Generation Scripts (optional)

## Schnellstart

### 1. Repository klonen

```bash
git clone https://github.com/neoforce/evolving.git
cd evolving
```

### 2. Konfiguration verlinken (Empfohlen)

Für die beste Erfahrung, verlinke das `.claude` Verzeichnis:

```bash
# Bestehende Config sichern falls vorhanden
mv ~/.claude ~/.claude.backup

# Symlink erstellen
ln -s $(pwd)/.claude ~/.claude
```

### 3. Claude Code starten

```bash
claude
```

Das war's! Claude lädt das Evolving System automatisch über die CLAUDE.md Datei.

## Was beim Start passiert

Bei Session-Start macht Evolving:

1. **Domain Memory laden** - Liest aktiven Projekt-Status aus `_memory/`
2. **Context Router initialisieren** - Bereitet Keyword-zu-Ressource Mapping vor
3. **Hooks aktivieren** - Aktiviert event-getriggerte Verhaltensweisen
4. **Status ankündigen** - Zeigt aktuelles Projekt, Phase und nächste Schritte

## Deine ersten Commands

Probiere diese Commands um das System zu erkunden:

```
/health-dashboard     # Schnelle System-Übersicht
/context-stats        # Context Window Nutzung
/inventory-report     # Vollständiges Komponenten-Inventar
```

## Nächste Schritte

- [Installations-Details](installation.md) - Vollständige Installationsanleitung
- [Schnellstart Tutorial](quick-start.md) - Praktische Einführung
- [Konfiguration](configuration.md) - Setup anpassen

## Hilfe benötigt?

- Schau in den [Architektur](../architecture/index.md) Bereich um zu verstehen wie alles funktioniert
- Durchsuche [Komponenten](../components/index.md) um zu sehen was verfügbar ist
- Lies die [Anleitungen](../guides/index.md) für spezifische Aufgaben
