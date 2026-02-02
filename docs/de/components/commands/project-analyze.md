---
title: project-analyze
type: command
tags: []
lang: en
confidence: 100
---

# project-analyze


## Overview

<div class="component-meta" markdown>
| Attribute | Value |
|-----------|-------|
| **Type** | Command |
| **Purpose** | Component description |
| **Complexity** | medium |
| **Model** | sonnet |
| **Category** | commands |</div>


## What It Does

Analysiere externe Codebase mit Context-Management und n8n-Support


## System Impact




## Architecture




## Usage


### Examples

#### Example



**Code:**
```bash
/project-analyze /Users/username/projects/auswanderungs-ki
/project-analyze ~/projects/my-app --refresh
/project-analyze /path/to/project --deep
```


#### Example



**Code:**
```python
def validate_codebase_path(path):
    # 1. Expand path (~ zu absolute path)
    expanded_path = os.path.expanduser(path)

    # 2. Check if path exists
    if not os.path.exists(expanded_path):
        return {
            "valid": False,
            "error": f"Pfad existiert nicht: {expanded_path}"
        }

    # 3. Check if directory
    if not os.path.isdir(expanded_path):
        return {
            "valid": False,
            "error": f"Pfad ist keine Directory: {expanded_path}"
        }

    # 4. Check if accessible
    if not os.access(expanded_path, os.R_OK):
        return {
            "valid": False,
            "error": f"Keine Leseberechtigung für: {expanded_path}"
        }

    return {
        "valid": True,
        "absolute_path": os.path.abspath(expanded_path)
    }
```


#### Example



**Code:**
```python
def generate_project_slug(codebase_path):
    # Use directory name as base
    dir_name = os.path.basename(codebase_path)

    # Clean slug
    slug = dir_name.lower()
    slug = re.sub(r'[^a-z0-9-]', '-', slug)
    slug = re.sub(r'-+', '-', slug)  # Multiple dashes to single
    slug = slug.strip('-')

    return slug
```


#### Example



**Code:**
```python
context_dir = f"knowledge/external-projects/{slug}/"
context_file = f"{context_dir}context.json"

if os.path.exists(context_file) and not args.refresh:
    # Context exists, load it
    context = load_context(context_file)

    # Inform user
    print(f"""
✅ Context gefunden für '{context['project_name']}'
📅 Letzte Analyse: {context['last_analyzed']}
📊 Health Score: {context['quality_scores']['overall_health']}/10

Wähle:
[1] Incremental Update (empfohlen) - Nur Änderungen analysieren
[2] Quick Status - Context laden, Status anzeigen (keine Analyse)
[3] Full Refresh - Komplette Neuanalyse (--refresh)

""")

    user_choice = wait_for_user_input()

    if user_choice == "2":
        return display_status_from_context(context)
    elif user_choice == "3":
        args.refresh = True
else:
    # First-time analysis
    print(f"""
🆕 Erste Analyse für '{slug}'

Ich werde:
1. ✅ Codebase-Struktur scannen
2. 📦 Dependencies analysieren
3. 🏗️ Architektur mappen
4. 🔍 n8n Workflows suchen (falls vorhanden)
5. 📊 Code-Quality bewerten
6. 💾 Context für künftige Sessions speichern

Geschätzte Dauer: 2-4 Minuten

Fortfahren? (ja/nein)
""")

    if not user_confirms():
        return "Analyse abgebrochen"
```


#### Example



**Code:**
```bash
mkdir -p knowledge/external-projects/{slug}/sessions
mkdir -p knowledge/external-projects/{slug}/n8n-workflows/workflows
```


#### Example



**Code:**
```bash
knowledge/external-projects/{slug}/
├── analysis-report.md
├── context.json
├── architecture.md
├── dependencies.json
├── upgrade-plan.md
├── n8n-workflows/
│   ├── analysis-report.md
│   ├── recommendations.md
│   └── workflows/
│       ├── workflow-1.json
│       └── workflow-2.json
└── sessions/
    └── YYYY-MM-DD-{topic}.md
```


#### Example



**Code:**
```python
analysis_depth = "standard"  # Default

if args.quick:
    analysis_depth = "quick"
elif args.deep:
    analysis_depth = "deep"

# Override by context for incremental
if context_exists and not args.refresh:
    analysis_depth = "incremental"
```


#### Example



**Code:**
```bash
@codebase-analyzer-agent
{
  "codebase_path": "{absolute_path}",
  "project_name": "{extracted_or_provided}",
  "analysis_depth": "{quick|standard|deep|incremental}",
  "focus_areas": ["architecture", "dependencies", "quality", "patterns", "security", "n8n"],
  "context_path": "knowledge/external-projects/{slug}/",
  "force_refresh": {boolean},
  "detect_n8n": true,
  "constraints": {
    "time_limit": {minutes based on depth}
  }
}
```


#### Example



**Code:**
```json
{
  "workflow_directory": "/path/to/auswanderungs-ki/workflows/",
  "workflow_files": [
    "/path/to/.../profile-analysis.json",
    "/path/to/.../visa-recommendation.json"
  ],
  "n8n_version": "1.15.0",
  "integration_context": {
    "webhook_calls": [
      {
        "file": "src/app/api/profile/route.ts",
        "line": 42,
        "url": "https://app.n8n.cloud/webhook/profile-analysis",
        "method": "POST",
        "payload_structure": {
          "userId": "string",
          "profileData": "object"
        }
      }
    ],
    "expected_responses": [
      {
        "webhook": "profile-analysis",
        "expected_fields": ["analysis", "recommendations", "score"],
        "data_types": {
          "analysis": "object",
          "recommendations": "array",
          "score": "number"
        }
      }
    ]
  },
  "frontend_expectations": {
    "data_structures": ["ProfileAnalysisResponse interface"],
    "error_handling": "try-catch with fallback"
  },
  "context_path": "knowledge/external-projects/auswanderungs-ki/"
}
```


#### Example



**Code:**
```bash
@n8n-expert-agent
{
  ... n8n_context from above ...
}
```


#### Example



**Code:**
```json
{
  "workflow_analysis": {
    "total_workflows": 29,
    "healthy": 24,
    "issues_found": 12,
    "critical_issues": 2
  },
  "integration_status": {
    "frontend_alignment": "good",
    "webhook_mapping": "complete",
    "data_structure_matches": true
  },
  "best_practices_score": 7.5,
  "recommendations_count": 15,
  "files_written": [
    "knowledge/external-projects/auswanderungs-ki/n8n-workflows/analysis-report.md",
    "knowledge/external-projects/auswanderungs-ki/n8n-workflows/recommendations.md"
  ]
}
```


#### Example



**Code:**
```markdown
# ✅ Analyse abgeschlossen: {PROJECT_NAME}

**Path**: `{codebase_path}`
**Analysis Type**: {FULL|INCREMENTAL}
**Duration**: {X} Sekunden
**Tokens Used**: {Y}

---

## 📊 Overall Health

**Codebase**: {X}/10 {🟢|🟡|🟠|🔴}
**n8n Workflows**: {X}/10 {🟢|🟡|🟠|🔴} (falls detected)
**Integration**: {X}/10 {🟢|🟡|🟠|🔴} (falls n8n)

---

## 🎯 Top 3 Priorities

1. **{ACTION_1}** ({CATEGORY})
   - Impact: {HIGH|MEDIUM|LOW}
   - Effort: {X} hours/days
   - Severity: {CRITICAL|HIGH|MEDIUM|LOW}

2. **{ACTION_2}** ({CATEGORY})
   - ...

3. **{ACTION_3}** ({CATEGORY})
   - ...

---

## 🏗️ Architektur

**Pattern**: {DETECTED_PATTERN}
**Tech Stack**: {MAIN_TECH}
**Components**: {COUNT} Dateien, {COUNT} Zeilen

{Falls n8n detected:}
**n8n Integration**:
- Workflows: {COUNT}
- Webhooks: {COUNT}
- Health: {SCORE}/10

---

## 📦 Dependencies

**Total**: {COUNT} ({OUTDATED} outdated)
**Critical Updates**: {COUNT}
**Vulnerabilities**: {COUNT}

---

## 📝 Reports generiert

Alle Details findest du hier:

📄 **Main Report**: `knowledge/external-projects/{slug}/analysis-report.md`
🏗️ **Architecture**: `knowledge/external-projects/{slug}/architecture.md`
📦 **Dependencies**: `knowledge/external-projects/{slug}/dependencies.json`
🚀 **Upgrade Plan**: `knowledge/external-projects/{slug}/upgrade-plan.md`

{Falls n8n detected:}
🔧 **n8n Analysis**: `knowledge/external-projects/{slug}/n8n-workflows/analysis-report.md`
💡 **n8n Recommendations**: `knowledge/external-projects/{slug}/n8n-workflows/recommendations.md`

💾 **Context gespeichert**: Nächste Analyse wird viel schneller (incremental update)!

---

## 🚀 Nächste Schritte

**Möchtest du**:
1. Details zu einem spezifischen Issue sehen?
2. Mit den Verbesserungen starten? (⚠️ erfordert explizite Genehmigung!)
3. Eine Session starten um daran zu arbeiten?

**Sage einfach**:
- "Zeig mir {issue}"
- "Starte mit Phase 1" (nach Genehmigung)
- "Arbeite an {slug}"
```


#### Example



**Code:**
```bash
session_file="knowledge/external-projects/{slug}/sessions/$(date +%Y-%m-%d)-analysis.md"
```


#### Example



**Code:**
```markdown
# Analysis Session: {PROJECT_NAME}

**Date**: {TIMESTAMP}
**Type**: {FULL|INCREMENTAL|QUICK|DEEP}
**Duration**: {X} seconds

## What was analyzed
- Codebase structure: {YES/NO}
- Dependencies: {YES/NO}
- Architecture: {YES/NO}
- n8n Workflows: {YES/NO - COUNT}

## Key Findings
1. {FINDING_1}
2. {FINDING_2}
3. {FINDING_3}

## Actions Taken
- Context updated: {YES/NO}
- Reports generated: {LIST}
- Recommendations provided: {COUNT}

## Next Steps
{NEXT_ACTIONS}

---

**Context**: knowledge/external-projects/{slug}/context.json
**Reports**: knowledge/external-projects/{slug}/
```


#### Example



**Code:**
```bash
❌ Fehler: Codebase-Pfad nicht gefunden

Pfad: {provided_path}

Überprüfe:
- Ist der Pfad korrekt?
- Existiert das Verzeichnis?
- Hast du Leserechte?

Gib den korrekten Pfad an oder nutze Tab-Completion.
```


#### Example



**Code:**
```bash
⚠️ Analyse teilweise fehlgeschlagen

Erfolgreich:
- {COMPLETED_PHASES}

Fehlgeschlagen:
- {FAILED_PHASE}: {ERROR}

Report wurde mit verfügbaren Daten erstellt.

Möchtest du:
[1] Mit partial analysis fortfahren
[2] Analysis abbrechen
```


#### Example



**Code:**
```bash
⚠️ n8n-Analyse fehlgeschlagen

Grund: {ERROR}

Codebase-Analyse wurde komplett durchgeführt.
n8n-spezifische Analyse konnte nicht abgeschlossen werden.

Report verfügbar ohne n8n-Details.
```


#### Example



**Code:**
```bash
User: "Analysiere /Users/me/projects/auswanderungs-ki"

Du: "🆕 Erste Analyse für 'auswanderungs-ki'..."
    (Invokes @codebase-analyzer-agent)

Codebase-Analyzer:
    Phase 1: Scanning... Next.js 15 detected, n8n workflows found!
    Phase 5: Invoking @n8n-expert-agent...

n8n-Expert:
    Analyzing 29 workflows...
    Fetching n8n docs...
    12 issues found, 15 recommendations generated

Du: "✅ Analyse abgeschlossen!
    Codebase: 8/10 🟢
    n8n Workflows: 7/10 🟡

    Top 3 Priorities:
    1. Fix 2 critical n8n workflow issues
    2. Update 12 outdated dependencies
    3. Improve error handling in API routes"
```


#### Example



**Code:**
```bash
User: "Check mal auswanderungs-ki status"

Du: "✅ Context gefunden!
    Letzte Analyse: vor 3 Tagen
    [1] Incremental Update
    [2] Quick Status
    [3] Full Refresh"

User: "1"

Du: (Loads context, detects changes via git)
    "📊 Änderungen erkannt:
    - 12 commits seit letzter Analyse
    - 8 Dateien geändert
    - package.json updated (dependencies changed)"

    (Invokeiert @codebase-analyzer-agent mit incremental mode)

    "✅ Incremental Update abgeschlossen (42 Sekunden)

    Neu seit letzter Analyse:
    - 3 Dependencies updated ✅
    - 1 neuer n8n Workflow
    - 2 neue Funktionen im Frontend

    Health: 8/10 → 8.5/10 🟢 (verbessert!)"
```




## Configuration



## Best Practices




## Related



---

<small>Source: `.claude/commands/project-analyze.md`</small>
