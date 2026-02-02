---
title: Anleitungen
description: Schritt-für-Schritt Tutorials für häufige Aufgaben
---

# Anleitungen

Praktische Anleitungen um das Beste aus dem Evolving System herauszuholen.

## Erste Schritte

| Anleitung | Beschreibung | Zeit |
|-----------|--------------|------|
| [Schnellstart](../getting-started/quick-start.md) | Deine erste Session mit Evolving | 5 Min |
| [Konfiguration](../getting-started/configuration.md) | Setup anpassen | 10 Min |

## Komponenten erstellen

| Anleitung | Beschreibung | Zeit |
|-----------|--------------|------|
| [Agents erstellen](creating-agents.md) | Autonome Task-Ausführer bauen | 15 Min |
| [Commands schreiben](writing-commands.md) | Benutzeraufrufbare Aktionen hinzufügen | 10 Min |
| [Patterns verwenden](using-patterns.md) | Wiederverwendbare Lösungen anwenden | 10 Min |
| [System erweitern](extending-system.md) | Neue Fähigkeiten hinzufügen | 20 Min |

## Mit Memory arbeiten

| Anleitung | Beschreibung | Zeit |
|-----------|--------------|------|
| Domain Memory Basics | Projekt-Status verfolgen | 10 Min |
| Experience Memory | Aus Lösungen lernen | 15 Min |
| Session Handoffs | Kontext erhalten | 5 Min |

## Agent Workflows

| Anleitung | Beschreibung | Zeit |
|-----------|--------------|------|
| Delegation Patterns | Wann und wie delegieren | 15 Min |
| Multi-Agent Tasks | Agent Swarms koordinieren | 20 Min |
| Review Pipelines | Automatischer Code Review | 10 Min |

## Automatisierung

| Anleitung | Beschreibung | Zeit |
|-----------|--------------|------|
| Hook-Entwicklung | Event-Trigger erstellen | 15 Min |
| Workflow Detection | Natürlichsprachliche Commands | 10 Min |
| Auto-Learning Setup | Rules aus Korrekturen generieren | 10 Min |

## Best Practices

### Do

- ✅ Mit Domain Memory für Projekt-Tracking starten
- ✅ Delegation für Multi-File Tasks nutzen
- ✅ Hooks für repetitive Checks einsetzen
- ✅ Auto-generierte Rules regelmäßig prüfen

### Don't

- ❌ Alles beim Session-Start laden
- ❌ Triviale 1-2 Zeilen Änderungen delegieren
- ❌ Hook-Warnungen ignorieren
- ❌ Den Verifikationsschritt überspringen

## Kurzreferenz

### Häufige Commands

```bash
/health-dashboard     # System-Health
/context-stats        # Token-Nutzung
/inventory-report     # Alle Komponenten
/whats-next          # Handoff erstellen
```

### Delegation Score

| Faktor | Punkte |
|--------|--------|
| Scope > 2 Dateien | +2 |
| Bulk-Operation | +2 |
| Research-Task | +2 |
| Code Review | +2 |
| Kritische Keywords | -10 |
| User will sehen | -5 |

**Score ≥ 3 = Delegieren**

### Memory-Pfade

```
_memory/
├── index.json           # Aktiver Context
├── projects/{name}.json # Projekt-Status
├── experiences/         # Erlernte Lösungen
└── workflows/active.json
```

## Mehr benötigt?

- Durchsuche [Komponenten](../components/index.md) für verfügbare Tools
- Prüfe [Architektur](../architecture/index.md) für System-Design
- Erkunde [Features](../features/index.md) für Fähigkeiten

## Anleitungen beitragen

Hast du einen Workflow der gut funktioniert? Überlege eine Anleitung beizutragen:

1. In Markdown schreiben
2. Praktische Beispiele einschließen
3. Zeit zum Abschließen schätzen
4. Via PR einreichen

Wir freuen uns über Community-Beiträge!
