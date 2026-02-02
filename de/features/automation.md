# Automatisierung

Evolving automatisiert repetitive Workflows durch Hooks, Natural Language Detection, Self-Learning, Documentation Sync, Session Evaluation und Spaced Repetition.

---

## Hook System

### Was es macht

Führt automatisierte Checks und Aktionen bei Key Lifecycle Events aus (vor/nach Tool Nutzung, Session Start/End).

### Hook-Kategorien

**22 aktive Hooks** in 4 Kategorien:

| Kategorie | Hooks | Zweck |
|----------|-------|---------|
| **Validation** (6) | check-comments, todo-enforcer, delegation-enforcer, etc. | Qualitätsstandards durchsetzen |
| **Sync** (4) | auto-cross-reference, doc-sync, knowledge-sync | Docs konsistent halten |
| **Analysis** (7) | correction-detector, context-warning, subagent-router, etc. | Patterns erkennen, Verbesserungen vorschlagen |
| **Memory** (5) | session-summary, usage-tracker, experience-suggest, etc. | Tracking und Learning |

### Wie es funktioniert

```
Tool Execution (e.g., Write)
     │
     ▼
┌──────────────────────────┐
│ PreToolUse Hooks         │
│                          │
│ • todo-enforcer          │
│   (check open todos)     │
│                          │
│ • check-comments         │
│   (validate comment %)   │
└──────────┬───────────────┘
           │
           ▼
    Tool Executes
           │
           ▼
┌──────────────────────────┐
│ PostToolUse Hooks        │
│                          │
│ • auto-cross-reference   │
│   (sync docs)            │
│                          │
│ • delegation-enforcer    │
│   (track hints)          │
└──────────────────────────┘
```

### Konfiguration

**Speicherort**: `.claude/hooks/`

**Hook Metadata**:
```json
{
  "name": "check-comments",
  "lifecycle": "PreToolUse",
  "tools": ["Write", "Edit"],
  "priority": 5,
  "config": {
    "max_comment_percentage": 25,
    "action_on_fail": "block"
  }
}
```

### Beispiel

**Write Hook Flow**:
```
Claude: Edit("auth.ts", ...)
     │
     ▼
┌──────────────────────────┐
│ check-comments.py        │
│                          │
│ Analyzes code:           │
│ • Lines: 100             │
│ • Comments: 30           │
│ • Percentage: 30%        │
│                          │
│ → EXCEEDS 25% threshold  │
│ → BLOCK with message     │
└──────────┬───────────────┘
           │
           ▼
Claude receives:
  "⚠️ BLOCK: 30% comments (max 25%)
   Refactor: Use self-documenting code"

Claude must:
  → Reduce comments
  → Re-attempt Write
  → Hook passes → Write succeeds
```

**Session End Hook**:
```
Session ending
     │
     ▼
┌──────────────────────────┐
│ session-summary.sh       │
│                          │
│ Creates handoff if:      │
│ • Commits made, OR       │
│ • Handoff created        │
│                          │
│ Otherwise: Skip          │
└──────────┬───────────────┘
           │
           ▼
Handoff created:
  _handoffs/2026-02-03-feature-x.md
```

**Relevant**: `.claude/hooks/README.md`

---

## Workflow Detection

### Was es macht

Erkennt Workflow-Trigger aus natürlicher Sprache und schlägt geeignete Commands vor.

### Wie es funktioniert

```
User: "I have a new idea"
     │
     ▼
┌──────────────────────────┐
│ 1. Keyword Extraction    │
│    ["new", "idea"]       │
└──────────┬───────────────┘
           │
           ▼
┌──────────────────────────┐
│ 2. Detection Index Match │
│    .claude/detection-    │
│    index.json            │
│                          │
│    Match: /idea-new      │
│    Confidence: 95%       │
└──────────┬───────────────┘
           │
           ▼
┌──────────────────────────┐
│ 3. Confidence Check      │
│                          │
│ ≥ 80%: Suggest command   │
│ 50-79%: Ask if meant     │
│ < 50%: Ignore            │
└──────────┬───────────────┘
           │ 95% (HIGH)
           ▼
┌──────────────────────────┐
│ 4. User Prompt           │
│                          │
│ "Soll ich /idea-new      │
│  nutzen?"                │
│                          │
│ Wait for confirmation    │
└──────────────────────────┘
```

### Konfiguration

**Detection Index**: `.claude/detection-index.json`

```json
{
  "commands": [
    {
      "command": "/idea-new",
      "keywords": ["idea", "new", "brainstorm"],
      "patterns": [
        "I have a(n)? (new )?idea",
        "brainstorm(ing)?",
        "let's think about"
      ],
      "confidence_base": 80,
      "anti_keywords": ["old", "previous", "existing"]
    }
  ]
}
```

### Beispiel

**High Confidence (95%)**:
```
User: "I have a new idea for authentication"

System:
  → Keywords: ["new", "idea"]
  → Pattern match: "I have a new idea"
  → Confidence: 95%
  → Suggests: "Soll ich /idea-new nutzen?"

User: "yes"

System:
  → Executes /idea-new workflow
```

**Medium Confidence (65%)**:
```
User: "Maybe we should plan this better"

System:
  → Keywords: ["plan"]
  → No exact pattern match
  → Confidence: 65%
  → Asks: "Meinst du /plan?"

User: "no, just thinking out loud"

System:
  → Continues normal conversation
```

**Low Confidence (30%)**:
```
User: "The plan seems good"

System:
  → Keywords: ["plan"]
  → Context: not a request
  → Confidence: 30%
  → No suggestion (responds normally)
```

**Relevant**: `.claude/rules/workflow-detection.md`

---

## Auto-Learning

### Was es macht

Generiert neue Rules aus User-Korrektionen und speichert sie als Candidates für manuelle Review und Promotion.

### Wie es funktioniert

```
User Corrects Claude
     │
     ▼
┌──────────────────────────┐
│ 1. Hook Detection        │
│    correction-detector.py│
│                          │
│    Recognizes:           │
│    • assumption errors   │
│    • scope issues        │
│    • over-engineering    │
│    • misunderstandings   │
└──────────┬───────────────┘
           │
           ▼
┌──────────────────────────┐
│ 2. Suggestion            │
│                          │
│ "💡 This could be a rule!│
│  Category: assumption    │
│  Create rule?"           │
└──────────┬───────────────┘
           │
     User confirms?
      /          \
    YES           NO
     │             │
     ▼             ▼
  Generate       Skip
     │
     ▼
┌──────────────────────────┐
│ 3. Context Extraction    │
│                          │
│ • Last 3-5 turns         │
│ • Original action        │
│ • Corrected action       │
│ • Category from hook     │
└──────────┬───────────────┘
           │
           ▼
┌──────────────────────────┐
│ 4. Rule Generation       │
│                          │
│ Template:                │
│ • Title                  │
│ • Category               │
│ • Pattern (do)           │
│ • Anti-pattern (don't)   │
│ • Example                │
└──────────┬───────────────┘
           │
           ▼
┌──────────────────────────┐
│ 5. Save as CANDIDATE     │
│                          │
│ knowledge/rules/staging/ │
│ {category}-{slug}-       │
│ {date}.md                │
│                          │
│ Status: candidate        │
│ Confidence: 30           │
└──────────────────────────┘
```

### Konfiguration

**Keine Konfiguration** - ausgelöst durch correction-detector.py Hook.

**Rule Lifecycle**:
```
candidate (manual review needed)
     │
     │ /rules-review promote {id}
     ▼
trial (loaded, passive tracking)
     │
     │ 3+ successful applications
     ▼
stable (production)
```

### Beispiel

**Correction Szenario**:
```
Claude: [Reads file without checking if exists]
        Read("config.json")

Error: File not found

User: "Check if file exists first with ls!"

System:
  → correction-detector.py triggers
  → Category: assumption
  → Suggests: "💡 Create rule?"

User: "yes"

System generates:
  File: assumption-check-file-exists-20260203.md
  Title: "Verify file existence before reading"
  Pattern: "Use ls/glob to check file exists"
  Anti-pattern: "Assume file exists based on memory"
  Example: [Concrete example from conversation]
  Status: candidate
```

**Manual Review**:
```
User: "/rules-review list --status=CANDIDATE"

System shows:
  1. assumption-check-file-exists-20260203
     Applied: 0 times
     Age: 1 day

User: "/rules-review promote 1"

System:
  → Status: candidate → trial
  → Will load at next session start
  → Begins passive tracking
```

**Trial zu Stable**:
```
Session 1: Rule applied, no correction → success_count: 1
Session 2: Rule applied, no correction → success_count: 2
Session 3: Rule applied, no correction → success_count: 3

Automatic promotion:
  → Status: trial → stable
  → Moved to knowledge/rules/debugging/
  → Now part of core system
```

**Relevant**: `.claude/rules/auto-rule-generation.md`

---

## Doc Sync

### Was es macht

Updated automatisch Master-Dokumentation (README, SYSTEM-MAP, COMMANDS) wenn strukturelle Änderungen passieren.

### Wie es funktioniert

```
Structural Change
(Command/Agent/Pattern created)
     │
     ▼
┌──────────────────────────┐
│ 1. Hook Detection        │
│    auto-cross-reference  │
│    .sh                   │
│                          │
│ "⚠️ SYNC CHECK: Command" │
└──────────┬───────────────┘
           │
           ▼
┌──────────────────────────┐
│ 2. Decision              │
│                          │
│ Documentable change?     │
│ • New component? ✓       │
│ • Changed counts? ✓      │
│ • Just bugfix? ✗         │
└──────────┬───────────────┘
           │ YES
           ▼
┌──────────────────────────┐
│ 3. Update Master Docs    │
│                          │
│ • COMMANDS.md (+entry)   │
│ • README.md (+count)     │
│ • SYSTEM-MAP.md (+entry) │
│ • detection-index.json   │
└──────────┬───────────────┘
           │
           ▼
┌──────────────────────────┐
│ 4. Single Commit         │
│                          │
│ "docs: Add /new-command  │
│  to master documents"    │
└──────────────────────────┘
```

### Konfiguration

**Hook Speicherort**: `.claude/hooks/auto-cross-reference.sh`

**Sync Matrix**:

| Change Type | Updates |
|-------------|---------|
| Command | COMMANDS.md, README.md, SYSTEM-MAP.md, detection-index.json |
| Agent | SYSTEM-MAP.md, README.md |
| Pattern | SYSTEM-MAP.md, README.md, knowledge/index.md |
| Template | SYSTEM-MAP.md, README.md, knowledge/index.md |

### Beispiel

**Neuer Command erstellt**:
```
Write(.claude/commands/new-feature.md)
     │
     ▼
Hook triggers:
  "⚠️ SYNC CHECK: Command - new-feature.md"

Claude automatically:
  1. Reads COMMANDS.md → current count: 47
  2. Adds entry:
     ## /new-feature
     **Category**: Feature Development
     **Description**: ...
  3. Updates count: 47 → 48
  4. Updates SYSTEM-MAP.md commands table
  5. Updates README.md count
  6. Updates detection-index.json with keywords
  7. Commits: "docs: Add /new-feature to master documents"
  8. Informs user: "Master docs updated for /new-feature"
```

**Keine User-Intervention nötig** - komplett automatisch.

**Relevant**: `.claude/rules/proactive-doc-sync.md`

---

## Session Evaluation

### Was es macht

Evaluiert abgeschlossene Sessions mit 5-Kriterien Rubric und speichert Ergebnisse in Experience Memory.

### Wie es funktioniert

```
Session Start
     │
     ▼
┌──────────────────────────┐
│ Check for Unrated        │
│ Sessions                 │
│                          │
│ knowledge/sessions/      │
│ *pending*.md             │
└──────────┬───────────────┘
           │
   Found pending?
      /         \
    YES          NO
     │            │
     ▼            ▼
  Offer        Continue
  Evaluation   Normally
     │
     ▼
┌──────────────────────────┐
│ User Accepts?            │
│                          │
│ "3 unrated sessions.     │
│  Quick eval? (30s each)" │
└──────────┬───────────────┘
           │ YES
           ▼
┌──────────────────────────┐
│ For Each Session:        │
│                          │
│ 1. Read session file     │
│ 2. Read commits          │
│ 3. Read handoff          │
│                          │
│ 4. Rate 5 criteria:      │
│    • Completeness (20%)  │
│    • Depth (25%)         │
│    • Tone (15%)          │
│    • Scope (20%)         │
│    • Missed Opp. (20%)   │
│                          │
│ 5. Calculate score       │
│    (weighted average)    │
└──────────┬───────────────┘
           │
           ▼
┌──────────────────────────┐
│ Save to Experience       │
│                          │
│ MCP: experience_create   │
│ • type: session_eval     │
│ • scores: {...}          │
│ • overall: 4.2/5         │
│ • strengths: [...]       │
│ • weaknesses: [...]      │
└──────────┬───────────────┘
           │
           ▼
┌──────────────────────────┐
│ Cleanup                  │
│                          │
│ Delete session file      │
│ (data in Experience now) │
└──────────────────────────┘
```

### Konfiguration

**Rubric Weights**:
```json
{
  "criteria": {
    "completeness": 0.20,
    "depth": 0.25,
    "tone": 0.15,
    "scope": 0.20,
    "missed_opportunities": 0.20
  },
  "thresholds": {
    "excellent": 4.0,
    "good": 3.5,
    "needs_improvement": 3.0
  }
}
```

### Beispiel

**Evaluation Flow**:
```
Session: 2026-02-03 (Feature Implementation)

Commits: 3
Files changed: 5
Handoff: Created

Evaluation:
  Completeness: 5/5 (all tasks done)
  Depth: 4/5 (thorough, could add more tests)
  Tone: 5/5 (professional, clear)
  Scope: 4/5 (stayed focused, minor scope creep)
  Missed Opportunities: 3/5 (could have refactored adjacent code)

Weighted Score:
  (5×0.20) + (4×0.25) + (5×0.15) + (4×0.20) + (3×0.20)
  = 1.0 + 1.0 + 0.75 + 0.8 + 0.6
  = 4.15/5

Experience saved:
  type: session_eval
  overall: 4.15
  summary: "Good feature work, focused execution"
  strengths: ["Complete", "Good tone", "Stayed on track"]
  weaknesses: ["Could improve adjacent code", "More tests needed"]

Session file deleted (data preserved in Experience)
```

**Score-basierte Aktionen**:

| Score | Aktion |
|-------|--------|
| 4.0-5.0 | Nur loggen |
| 3.0-3.9 | Angebot: "Learning extrahieren?" |
| < 3.0 | Proaktiv Learning vorschlagen |

**Relevant**: `.claude/rules/session-evaluation.md`

---

## Spaced Repetition

### Was es macht

Plant Reviews von Experiences und Rules mit Spaced Repetition Algorithmus um Learning zu verstärken.

### Wie es funktioniert

```
Experience Created
     │
     │ interval: 3 days
     ▼
┌──────────────────────────┐
│ First Review             │
│                          │
│ "Remember this solution?"│
│                          │
│ [C]onfirm / [S]kip       │
└──────────┬───────────────┘
           │
     User: Confirm
           │
           ▼
┌──────────────────────────┐
│ Update Interval          │
│                          │
│ interval *= 2.5          │
│ 3 days → 7.5 days        │
└──────────┬───────────────┘
           │
     7.5 days later
           │
           ▼
┌──────────────────────────┐
│ Second Review            │
│                          │
│ User: Confirm            │
│ interval *= 2.5          │
│ 7.5 → 18.75 days         │
└──────────┬───────────────┘
           │
     18.75 days later
           │
           ▼
┌──────────────────────────┐
│ Third Review             │
│                          │
│ User: Confirm            │
│ interval *= 2.5          │
│ 18.75 → 46.9 days        │
└──────────────────────────┘

Eventually: interval > 90 days → archived
```

### Konfiguration

**Multipliers**:
```json
{
  "spaced_repetition": {
    "intervals": {
      "initial": 3,
      "max": 90
    },
    "multipliers": {
      "confirm": 2.5,
      "practice": 2.0,
      "skip": 0.8,
      "skip_all": 1.0
    }
  }
}
```

### Beispiel

**Session-Start Review**:
```
Session starts at 2026-02-10
     │
     ▼
Spaced Rep Collector runs:
  → 3 items due for review

System:
  "📚 Review-Check (3 fällig):
   1. [EXP] Supabase RLS fix (due 2026-02-09)
   2. [RULE] Advanced debugging (due 2026-02-10)
   3. [EXPLORE] Hook system (due 2026-02-08)

   [C]onfirm / [P]ractice / [S]kip / [SA]skip-all"

User: "c c s"

System updates:
  1. Supabase RLS: interval 7 → 17.5 days
  2. Advanced debugging: interval 5 → 12.5 days
  3. Hook system: interval 10 → 8 days (skip penalty)

Next reviews:
  1. 2026-02-27
  2. 2026-02-22
  3. 2026-02-18
```

**Manual Review**:
```
User: "/review"

System:
  Shows all items due + overdue
  Allows bulk review
  Updates intervals based on responses
```

**Relevant**: `.claude/rules/domain-memory-bootup.md` (Phase 4a)

---

## Zusammenfassung

Automatisierung bietet:
- **Hook System**: 22 Hooks für Validation, Sync, Analysis, Memory
- **Workflow Detection**: Natural Language → Command-Vorschläge
- **Auto-Learning**: User-Korrektionen → Candidate Rules
- **Doc Sync**: Automatische Master-Doc Updates
- **Session Evaluation**: 5-Kriterien Rubric → Experience Memory
- **Spaced Repetition**: Learning-Verstärkung mit Interval-Skalierung

**Ergebnis**: System verbessert sich selbst, erhält Konsistenz, lernt aus Interaktionen.
