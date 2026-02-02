# Patterns nutzen

Patterns sind bewährte Problemlösungsansätze, die dir helfen, komplexe Aufgaben systematisch anzugehen. Diese Anleitung zeigt dir, wann und wie du Patterns effektiv anwendest.

## Was sind Patterns?

Patterns sind wiederverwendbare mentale Modelle für die Bewältigung verschiedener Arten von Problemen:

- **Reflection Pattern**: Iterative Selbstverbesserung durch Kritik
- **ReAct Pattern**: Denken + Handeln in Zyklen
- **Tree of Thoughts**: Mehrere Lösungswege erkunden
- **Chain of Thought**: Schritt-für-Schritt Denken
- **Ensemble Pattern**: Mehrere Agents, verschiedene Perspektiven
- **Blackboard Pattern**: Gemeinsamer Arbeitsbereich für Zusammenarbeit

**Ort**: `knowledge/patterns/`

## Das richtige Pattern finden

### Nach Problemtyp

| Problemtyp | Empfohlenes Pattern |
|--------------|-------------------|
| **Bestehende Lösung verbessern** | Reflection |
| **Komplexes Problem debuggen** | ReAct |
| **Kritische Entscheidung** | Tree of Thoughts |
| **Multi-Perspektiv Analyse** | Ensemble |
| **Komplexes Denken** | Chain of Thought |
| **Team-Koordination** | Blackboard |

### Nach Task-Charakteristiken

```
Iteration/Verfeinerung nötig? → Reflection
Exploration/Experimentieren nötig? → ReAct
Optionen evaluieren? → Tree of Thoughts
Mehrere Sichtweisen nötig? → Ensemble
Komplexität aufschlüsseln? → Chain of Thought
Agent-Koordination nötig? → Blackboard
```

### Via Context Router

Das System kann Patterns automatisch vorschlagen:

```
User: "Verbessere diesen Code"
→ Context Scout erkennt "improve"
→ Lädt Reflection Pattern (Vertrauen: 85%)
→ Wende iterative Verfeinerung an
```

**Konfiguration**: `_graph/cache/context-router.json`

## Pattern-Struktur

Jedes Pattern folgt diesem Format:

```markdown
# {Pattern Name}

## Core Loop
{Die fundamentale Iterations-Schleife}

## When to Use
{Situationen wo dieses Pattern brilliert}

## When NOT to Use
{Anti-Patterns und falsche Situationen}

## Steps
1. {Phase 1}
2. {Phase 2}
...

## Example
{Konkrete Anwendung}

## Related
{Links zu ähnlichen Patterns}
```

## Patterns Schritt für Schritt anwenden

### 1. Dein Problem identifizieren

```markdown
Problem: "Mein API Design funktioniert, fühlt sich aber umständlich an"

Charakteristiken:
- Bestehende Lösung ✓
- Verfeinerung nötig ✓
- Keine klaren Bugs ✓
- Verbesserung gewünscht ✓

→ Pattern: Reflection
```

### 2. Pattern Kontext laden

```bash
# Manuell
Read knowledge/patterns/reflection-pattern.md

# Automatisch (via Context Scout)
User: "Verfeinere dieses API Design"
→ System lädt Reflection Pattern Zusammenfassung
```

### 3. Pattern Schritte befolgen

**Reflection Pattern Beispiel:**

```markdown
## Schritt 1: Initialzustand
Aktuelles API:
```typescript
class UserAPI {
  getUser(id: string): Promise<User>
  updateUser(id: string, data: Partial<User>): Promise<User>
  deleteUser(id: string): Promise<void>
}
```

## Schritt 2: Selbstkritik
Probleme:
- Inkonsistente Fehlerbehandlung (wirft vs. gibt null zurück)
- Keine Eingabevalidierung
- Fehlende Batch-Operationen
- Keine Caching-Strategie

## Schritt 3: Verfeinerung
```typescript
class UserAPI {
  // Konsistenter Result<T, E> Return-Typ
  async getUser(id: string): Promise<Result<User, APIError>>

  // Eingabevalidierung via Schema
  async updateUser(
    id: string,
    data: UpdateUserSchema
  ): Promise<Result<User, ValidationError>>

  // Soft Delete mit Grund
  async deleteUser(
    id: string,
    reason: string
  ): Promise<Result<void, APIError>>

  // Neu: Batch Operationen
  async getUsers(ids: string[]): Promise<Result<User[], APIError>>
}
```

## Schritt 4: Neubewertung
Verbesserungen:
✅ Konsistente Fehlerbehandlung
✅ Eingabevalidierung
✅ Batch-Operationen
✅ Bessere Typ-Sicherheit

Verbleibende Probleme:
- Caching-Strategie noch nicht definiert
- Rate Limiting nicht adressiert

## Schritt 5: Iterieren (falls nötig)
Weitere Verfeinerung...
```

### 4. Wisse, wann du aufhörst

Höre mit Iterieren auf, wenn:
- ✅ Kernprobleme gelöst
- ✅ Abnehmende Erträge (< 10% Verbesserung pro Zyklus)
- ✅ Zeit/Context Budget überschritten
- ✅ Benutzer zufrieden mit Ergebnis

## Patterns kombinieren

Patterns können zusammen verwendet werden:

### Sequenzielle Kombination

```
Tree of Thoughts → Reflection
(Optionen erkunden) → (Gewählte Option verfeinern)

ReAct → Reflection
(Problem erkunden) → (Lösung verfeinern)
```

### Parallele Kombination

```
Ensemble + Chain of Thought
(Mehrere Agents nutzen jeweils strukturiertes Denken)

Blackboard + ReAct
(Gemeinsamer Arbeitsbereich, wo Agents erkunden)
```

### Beispiel: Komplexes Feature Design

```markdown
## Phase 1: Exploration (Tree of Thoughts)
Generiere 3 Design-Ansätze:
1. Event-driven Architektur
2. Microservices
3. Monolithisch mit Modulen

Evaluiere jeden gegen Kriterien...
Wähle: Modularer Monolith

## Phase 2: Verfeinerung (Reflection)
Initialer Design:
{Module, APIs, Datenfluss}

Kritik → Verfeinern → Neubewertung
Iteriere 3x bis solide

## Phase 3: Implementierung (ReAct)
Gedanke: "Beginne mit Core-Modul"
Aktion: Implementiere Core
Beobachtung: Funktioniert, aber Coupling eng
Gedanke: "Führe Interfaces ein"
Aktion: Abstraktions-Schicht hinzufügen
...
```

## Wann NICHT Patterns nutzen

### Anti-Patterns

❌ **Einfache Aufgaben über-engineern**
```
User: "Fixe diesen Typo"
Falsch: Reflection Pattern anwenden (3 Iterationen für einen Typo!)
Richtig: Einfach fixieren
```

❌ **Pattern um des Patterns willen**
```
User: "Lese diese Datei"
Falsch: Tree of Thoughts (erkunde 5 Wege zum Lesen!)
Richtig: Direktes Read Tool
```

❌ **Context Budget ignorieren**
```
Context: 85% voll
Falsch: Ensemble Pattern starten (starte 5 Agents)
Richtig: Single-Agent mit klarer Einschränkung
```

### Entscheidungs-Matrix

| Task Komplexität | Pattern? | Warum |
|----------------|----------|-----|
| Trivial (1-2 Schritte) | ❌ Nein | Overhead > Wert |
| Einfach (3-5 Schritte) | ❌ Nein | Direkter Ansatz schneller |
| Moderat (6-10 Schritte) | ✅ Vielleicht | Falls Unsicherheit/Mehrdeutigkeit |
| Komplex (10+ Schritte) | ✅ Ja | Struktur verhindert Chaos |

## Praktische Beispiele

### Beispiel 1: Reflection Pattern für Code Review

```markdown
**Problem**: Review Auth Service Implementierung

**Pattern**: Reflection

**Anwendung**:

Zyklus 1:
- Code lesen
- Kritik: Fehlende Eingabevalidierung
- Verfeinern: Zod Schemas hinzufügen
- Neubewertung: Besser, aber Fehlerbehandlung schwach

Zyklus 2:
- Kritik: Generische Fehlermeldungen
- Verfeinern: Spezifische Error Types hinzufügen
- Neubewertung: Gut, aber kein Logging

Zyklus 3:
- Kritik: Kein Audit Trail
- Verfeinern: Strukturiertes Logging hinzufügen
- Neubewertung: Solide! Shipped es.
```

### Beispiel 2: ReAct Pattern für Debugging

```markdown
**Problem**: API gibt 500 Error intermittierend zurück

**Pattern**: ReAct

**Anwendung**:

Gedanke: "Überprüfe Server Logs"
Aktion: Lese logs/error.log
Beobachtung: "Database Timeout Errors"

Gedanke: "Überprüfe DB Connection Pool"
Aktion: Lese config/database.ts
Beobachtung: "Pool Größe = 5, wahrscheinlich zu klein"

Gedanke: "Überprüfe gleichzeitige Request-Anzahl"
Aktion: Bash: grep "concurrent" logs/access.log
Beobachtung: "Peak = 50 Requests/sec"

Gedanke: "5 Verbindungen für 50 req/sec = Engpass"
Aktion: Aktualisiere Pool-Größe auf 20
Beobachtung: "Error-Rate fällt auf nahe Null"

Ergebnis: Problem identifiziert und gelöst
```

### Beispiel 3: Tree of Thoughts für Architektur

```markdown
**Problem**: Design Authentifizierungs-System

**Pattern**: Tree of Thoughts

**Anwendung**:

Branch 1: JWT-basiert
- Pros: Zustandslos, skalierbar
- Cons: Schwer zu widerrufen, Token-Größe
- Punkte: 7/10

Branch 2: Session-basiert
- Pros: Einfacher Widerruf, kleine Cookies
- Cons: Server-Zustand, Redis Abhängigkeit
- Punkte: 6/10

Branch 3: Hybrid (JWT + Refresh Tokens)
- Pros: Best of both, widerrufbar
- Cons: Komplexer
- Punkte: 9/10

Entscheidung: Wähle Branch 3 (Hybrid)

Nächstes: Wende Reflection an um Hybrid Design zu verfeinern
```

## Pattern Discovery

### Via Auto-Detection

```
User-Input → Keywords extrahiert → Context Router Match → Pattern geladen

Beispiel:
"Wie kann ich das verbessern?"
→ Keywords: ["improve", "refine"]
→ Match: Reflection Pattern (Vertrauen: 90%)
→ Auto-load Zusammenfassung
```

### Via Manuelle Auswahl

```bash
# Liste verfügbare Patterns
/list-patterns

# Wende spezifisches Pattern an
"Nutze Reflection Pattern um diesen Code zu verbessern"

# Oder direkter Verweis
Read knowledge/patterns/reflection-pattern.md
```

### Via Agent Empfehlung

Agents können Patterns empfehlen:

```
Explorer Agent: "Dieses Problem hat mehrere gültige Ansätze.
                 Erwäge Tree of Thoughts Pattern zu nutzen."
```

## Zusammenhang

- [Pattern Katalog](../architecture/context-routing.md) - Alle verfügbaren Patterns
- [Context Router](../architecture/context-routing.md) - Auto-Detection
- [Befehle schreiben](writing-commands.md) - Patterns in Befehlen nutzen
- [Agents erstellen](creating-agents.md) - Agents die Patterns anwenden
