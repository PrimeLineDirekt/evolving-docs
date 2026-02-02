# Quick Start Guide

Sei in 5 Minuten startklar mit Evolving.

## Deine erste Session

### 1. Claude Code starten

```bash
cd /pfad/zu/deinem/projekt
claude
```

Claude erkennt automatisch das Evolving System über die Symlinks in `~/.claude/`.

### 2. Domain Memory Bootup

Bei jedem Session-Start wird Claude:

1. `_memory/index.json` lesen um das aktive Projekt zu finden
2. Projekt-State aus `_memory/projects/{active}.json` laden
3. Den aktuellen Kontext ansagen

**Beispiel-Output:**
```
Projekt: evolving-system | Phase: Documentation
Letzter Stand: Created architecture overview
Nächster Schritt: Create getting-started guides
```

Das ist der **Domain Memory Bootup** - Claude erinnert sich wo du aufgehört hast!

### 3. Einen einfachen Command ausprobieren

Lass uns verfügbare Commands erkunden:

```
Du: "zeig mir alle commands"
```

Claude erkennt dies als Trigger für `/commands-list` und fragt:

```
Das klingt nach dem /commands-list Command.
Soll ich es ausführen?
```

Tippe `ja` um fortzufahren. Du siehst eine kategorisierte Liste aller 47+ Commands.

### 4. Plain-Text Detection nutzen

Statt `/command-name` zu tippen, kannst du natürliche Sprache verwenden:

**Beispiele:**

| Du sagst | Claude erkennt | Was passiert |
|---------|---------------|--------------|
| "Ich habe eine neue Idee" | `/idea-new` | Erstellt Idee im Knowledge Graph |
| "Zeig meine Ideen" | `/idea-list` | Listet alle getrackte Ideen |
| "Starte Planning Mode" | `/plan` | Aktiviert Plan Mode |
| "Erstelle einen neuen Command" | `/command-new` | Führt dich durch Command-Erstellung |

**Regel:** Claude führt NIEMALS automatisch aus. Es fragt immer zuerst um Bestätigung.

### 5. Deine erste Aufgabe

Lass uns einen einfachen Learning-Eintrag erstellen:

```
Du: "Ich habe etwas Neues über Git Hooks gelernt"

Claude: "Das klingt nach /learning-new. Soll ich es nutzen?"

Du: "ja"

Claude: [Führt /learning-new Command aus]
Was hast du gelernt? [...]
```

Folge den Prompts um dein Learning zu dokumentieren. Es wird:
- In `knowledge/learnings/` gespeichert
- Zum Knowledge Graph hinzugefügt
- Für zukünftige Suche indexiert

### 6. Deinen Fortschritt prüfen

Sieh was du erreicht hast:

```
Du: "zeig mir meinen aktuellen Fortschritt"

Claude: [Liest _memory/projects/{active}.json]

"Recent progress:
- 2024-02-03: Created getting-started guides
- 2024-02-02: Implemented documentation system
- 2024-02-01: Set up MCP integration"
```

## Output verstehen

### Hook-Nachrichten

Du wirst Hook-Nachrichten während Operationen sehen:

```
✓ PASS: comment-density acceptable (15%)
✓ PASS: delegation hints present
⚠ SYNC CHECK: Command - new-command.md
```

**Was sie bedeuten:**
- **PASS**: Quality Check erfolgreich
- **BLOCK**: Quality Check fehlgeschlagen, Aktion verhindert
- **SYNC CHECK**: Master Docs müssen möglicherweise aktualisiert werden
- **INFO**: Informationsnachricht

### Agent Delegation

Wenn Claude an spezialisierte Agents delegiert:

```
[Delegating to Explore agent with haiku model...]
```

**Warum Delegation?**
- Frischer Context (kein Session-History Overhead)
- Spezialisierte Expertise (Debugging, Exploration, Review)
- Kosteneffizient (Haiku für einfache Tasks, Sonnet für komplexe)

### Context Scout

Vor der Antwort führt Claude Context Scout aus um relevante Patterns/Rules zu laden:

```
[Context Scout: Matched 'debugging' → loading observe-before-editing.md]
```

Das passiert automatisch - keine Aktion von dir nötig.

## Häufige Workflows

### Ein neues Feature starten

```
Du: "Ich möchte User-Authentifizierung implementieren"

Claude: [Context Scout lädt relevante Patterns]
        "Das klingt nach /plan. Soll ich Planning Mode starten?"

Du: "ja"

Claude: [Tritt in Plan Mode ein]
        "Beschreibe die Feature-Anforderungen..."
```

### Ein Problem debuggen

```
Du: "Der Login-Endpoint schlägt fehl"

Claude: [Context Scout lädt Debugging-Rules]
        [Delegiert an Explore Agent um Codebase zu analysieren]

        "Problem gefunden in src/auth.ts Zeile 42..."
```

### Eine Entscheidung dokumentieren

```
Du: "Wir haben uns entschieden Supabase statt Firebase zu nutzen"

Claude: "Das klingt nach /decision-new. Soll ich es nutzen?"

Du: "ja"

Claude: [Führt dich durch Decision-Dokumentation]
```

## Nächste Schritte

Jetzt wo du deine erste Session abgeschlossen hast:

1. **Commands erkunden**: Versuche `/commands-list` um alle verfügbaren Commands zu sehen
2. **Anpassen**: Schau dir den [Konfigurations-Guide](./configuration.md) an
3. **Patterns lernen**: Lies über [Prompt Patterns](../core-concepts/prompt-patterns.md)
4. **Memory verstehen**: Deep Dive in [Domain Memory](../core-concepts/domain-memory.md)

## Tipps für Erfolg

### Tu das
- Nutze natürliche Sprache - Plain-Text Detection funktioniert super
- Lass Domain Memory deinen Fortschritt tracken
- Vertraue dem Delegation-System - Agents sind spezialisiert
- Review Hook-Nachrichten - sie verhindern Qualitätsprobleme

### Tu das nicht
- Manuell `_stats.json` updaten - lass Hooks das erledigen
- Domain Memory Bootup-Ansagen überspringen - sie sind Kontext!
- Gegen das System kämpfen - wenn Claude ein Pattern vorschlägt, probier es
- Commands auto-executen - Bestätigung ist ein Safety Feature

## Hilfe bekommen

### In-Session Hilfe

```
Du: "erkläre Domain Memory"

Claude: [Context Scout lädt domain-memory-bootup.md]
        [Erklärt das Konzept mit Beispielen]
```

### Command-spezifische Hilfe

```
Du: "wie funktioniert /plan?"

Claude: [Liest .claude/commands/plan.md]
        [Erklärt Nutzung, Beispiele, Optionen]
```

### Dokumentation durchsuchen

Alle Dokumentation ist in `docs/`:
- **Core Concepts**: `docs/de/core-concepts/`
- **Architektur**: `docs/de/architecture/`
- **Guides**: `docs/de/guides/`

## Problemlösung

### "Command nicht erkannt"

**Problem**: Plain-Text Trigger hat nicht funktioniert

**Lösung**: Versuche expliziter zu sein:
```
Statt: "zeig Zeug"
Versuche: "zeig mir alle Commands"
Oder: "/commands-list"
```

### "Kein aktives Projekt"

**Problem**: Domain Memory Bootup fehlgeschlagen

**Lösung**:
```
Stelle sicher dass _memory/index.json existiert mit active_context.project
Oder erstelle ein neues Projekt via /project-new
```

### "Hook fehlgeschlagen"

**Problem**: Ein Hook hat eine Operation blockiert

**Lösung**: Lies die Hook-Nachricht - sie erklärt warum:
```
✗ BLOCK: comment-density too high (75%)
→ Fix: Reduziere Kommentare, verbessere selbst-dokumentierenden Code
```

## Du bist bereit!

Du weißt jetzt:
- ✅ Wie Domain Memory funktioniert
- ✅ Wie man Plain-Text Commands nutzt
- ✅ Wie Delegation dir hilft
- ✅ Wie man Fortschritt trackt
- ✅ Wo man Hilfe bekommt

Fang an zu erkunden! Das System wird dich durch jeden Workflow führen.

**Empfohlene erste Commands zum Ausprobieren:**
1. `/commands-list` - Siehe alle verfügbaren Commands
2. `/idea-new` - Tracke eine neue Idee
3. `/learning-new` - Dokumentiere etwas das du gelernt hast
4. `/plan` - Plane dein nächstes Feature

Happy evolving! 🚀
