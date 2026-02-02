---
title: Prompt Patterns
description: Wiederverwendbare Ansätze für komplexe KI-Aufgaben
---

# Prompt Patterns

Prompt Patterns sind wiederverwendbare Ansätze zur Lösung komplexer Probleme mit KI. Das Evolving System enthält 59 Patterns, die automatisch basierend auf Kontext angewendet werden können.

## Was sind Prompt Patterns?

Traditionelles Prompt Engineering fokussiert auf einzelne Interaktionen. Prompt Patterns sind **Multi-Turn-Frameworks**, die KI durch komplexes Reasoning führen:

- **Reflection** - Iterative Selbstkritik und Verfeinerung
- **React** - Über das Problem nachdenken, dann handeln
- **Tree of Thoughts** - Multiple Lösungspfade erkunden
- **Blackboard** - Multi-Agent-Kollaboration

## Pattern-Architektur

### Drei-Schicht-Ladung

```
Layer 1: Detection (Auto)
  ↓ Keywords matchen
Layer 2: Summary (300 Tokens)
  ↓ Mehr Details benötigt
Layer 3: Full Pattern (3K Tokens)
```

**Ergebnis:** 90% Token-Ersparnis durch progressive Disclosure

## Verfügbare Patterns

### Reasoning Patterns

#### Reflection Pattern

**Zweck:** Iterative Selbstverbesserung durch Kritik

**Core Loop:**
1. Lösung generieren
2. Selbstkritik
3. Basierend auf Kritik verfeinern
4. 2-3 Mal wiederholen

**Wann nutzen:**
- Kreative Arbeit (Prompts, Content)
- Design-Entscheidungen
- Optimierungsprobleme

**Beispiel:**

```
User: "Verbessere dieses API-Design"

Iteration 1:
  Generieren → Endpoints reviewen
  Kritik → Pagination fehlt, keine Versionierung
  Verfeinern → /v1/ Prefix hinzufügen, ?page= Params

Iteration 2:
  Kritik → Error Responses unklar
  Verfeinern → Error Codes, Beschreibungen hinzufügen

Iteration 3:
  Kritik → Gut genug
  Final → Ausliefern
```

#### React Pattern

**Zweck:** Vor dem Handeln nachdenken

**Core Loop:**
1. **Reason** - Problem analysieren
2. **Act** - Eine Aktion ausführen
3. **Observe** - Ergebnisse prüfen
4. Bei Bedarf wiederholen

**Wann nutzen:**
- Debugging
- Explorative Aufgaben
- Multi-Step Problem-Solving

**Beispiel:**

```
User: "Fixe diesen Login-Bug"

Reason: Login schlägt fehl → Könnte Auth, DB oder Session sein
Act: Auth-Service Logs prüfen
Observe: Auth erfolgreich, JWT gültig

Reason: Auth OK → Muss Session oder DB sein
Act: Session Storage prüfen
Observe: Session nicht persistiert

Reason: Gefunden! Session Middleware fehlt
Act: Session Middleware hinzufügen
Observe: Login funktioniert ✓
```

#### Tree of Thoughts

**Zweck:** Multiple Lösungspfade erkunden

**Core Loop:**
1. 3 Lösungszweige generieren
2. Jeden Zweig evaluieren
3. Vielversprechendsten erweitern
4. Finale Lösungen vergleichen

**Wann nutzen:**
- Architektur-Entscheidungen
- Multiple gültige Ansätze
- High-Stakes Entscheidungen

**Beispiel:**

```
User: "Wähle Datenbank für neues Projekt"

Zweig 1: PostgreSQL
  Pro: Relational, ACID, bekannt
  Contra: Skalierungs-Komplexität

Zweig 2: MongoDB
  Pro: Flexibles Schema, horizontal skalierbar
  Contra: Keine ACID-Garantien

Zweig 3: Supabase (Postgres + APIs)
  Pro: Built-in Auth, Realtime, gehostet
  Contra: Vendor Lock-in

Evaluieren: Supabase gewinnt für MVP-Speed
Entscheidung: Supabase nutzen, später migrieren möglich
```

### Creation Patterns

#### Step-by-Step Refinement

**Zweck:** Komplexe Artefakte inkrementell bauen

**Core Loop:**
1. Outline entwerfen
2. Sektion für Sektion füllen
3. Jede reviewen und verfeinern
4. Integrieren und polieren

**Wann nutzen:**
- Lange Dokumente
- Komplexe Code-Module
- System-Designs

### Debugging Patterns

#### Systematic Debugging

**Zweck:** Evidenz-basiertes Bug-Fixing

**Core Loop:**
1. Issue reproduzieren
2. Evidenz sammeln (Logs, Stack Traces)
3. Hypothese bilden
4. Hypothese testen
5. Fixen wenn bestätigt

**Wann nutzen:**
- Bug Fixing
- Performance-Issues
- Unerwartetes Verhalten

**Beispiel:**

```
User: "App crasht beim Startup"

Reproduzieren: Ja, crasht jedes Mal
Evidenz: Stack Trace zeigt auf config.load()
Hypothese: Ungültige Config-Datei
Testen: config.json Syntax prüfen
Bestätigen: Fehlende Closing Brace
Fixen: Closing Brace hinzufügen
Verifizieren: App startet ✓
```

#### Observe Before Editing

**Zweck:** Verstehen bevor ändern

**Core Loop:**
1. Relevanten Code lesen
2. Root Cause identifizieren
3. Minimale Änderung planen
4. Änderung machen
5. Fix verifizieren

**Wann nutzen:**
- IMMER vor Code-Edits
- Verhindert Shotgun-Debugging
- Reduziert Regressionen

### Collaboration Patterns

#### Blackboard Pattern

**Zweck:** Multi-Agent Problem-Solving

**Core Loop:**
1. Shared Workspace definieren (Blackboard)
2. Jeder Agent trägt Expertise bei
3. Agents lesen Beiträge anderer
4. Iterieren bis Lösung entsteht

**Wann nutzen:**
- Komplexe Multi-Domain-Probleme
- Parallele Exploration
- Experten-Koordination

## Pattern-Erkennung

### Automatisches Laden

System erkennt Patterns basierend auf Keywords:

```json
{
  "pattern": "reflection",
  "keywords": ["verbessern", "verfeinern", "optimieren", "besser"],
  "confidence": 85,
  "action": "auto_load"
}
```

**Confidence-Level:**
- **80-100%** - Auto-load Summary
- **50-79%** - User zuerst fragen
- **0-49%** - Nicht laden

### Manueller Override

Pattern erzwingen:

```bash
# Reflection Pattern nutzen
User: "Nutze Reflection Pattern um das zu verbessern"

# Tree-of-Thoughts nutzen
User: "Erkunde Alternativen mit Tree-of-Thoughts"
```

## Custom Patterns erstellen

### Pattern Template

```markdown
---
title: Mein Custom Pattern
category: reasoning
triggers: [custom, pattern, keywords]
---

# Mein Custom Pattern

## Core Loop
1. Dein Schritt 1
2. Dein Schritt 2
3. Wiederholen

## Wann nutzen
- Situation wo das hilft

## Wann NICHT nutzen
- Wenn es nicht passt

## Config
- iterations: 3
```

### Registrierungs-Schritte

1. **Pattern-Datei erstellen**
   ```bash
   knowledge/patterns/mein-pattern.md
   ```

2. **Zum Knowledge Graph hinzufügen**
   ```json
   {
     "id": "pattern-mein-pattern",
     "type": "pattern",
     "tags": ["reasoning", "custom"]
   }
   ```

3. **Context Route hinzufügen**
   ```json
   {
     "route": "custom",
     "keywords": ["custom", "pattern"],
     "primary": ["mein-pattern"]
   }
   ```

## Best Practices

### DO

✅ **System Patterns erkennen lassen**
```
User: "Verbessere dieses Design"
→ System lädt Reflection Pattern automatisch
```

✅ **Kompatible Patterns kombinieren**
```
tree-of-thoughts (Optionen erkunden)
  ↓
reflection (Gewinner verfeinern)
```

### DON'T

❌ **Patterns erzwingen die nicht passen**
```
User: "Nutze Blackboard für simple Task"
→ Overkill, direkte Ausführung besser
```

❌ **Mutex Patterns kombinieren**
```
reflection + react gleichzeitig
→ Konfliktierender Ansatz
```

## Nächste Schritte

- [Context Routing](../architecture/context-routing.md) - Wie Erkennung funktioniert
