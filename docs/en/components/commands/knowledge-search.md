---
title: knowledge-search
type: command
tags: []
lang: en
confidence: 100
---

# knowledge-search


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

Durchsuche die Knowledge Base semantisch


## System Impact




## Architecture




## Usage


### Examples

#### Example



**Code:**
```bash
Was möchtest du in der Knowledge Base finden?

Beispiele:
- "API Integration" (Thema)
- "Wie optimiere ich Etsy Listings?" (Frage)
- "Prompts für SEO" (Spezifisch)
- "Skills in E-Commerce" (Kategorie)

Deine Suche:
```


#### Example



**Code:**
```bash
=== Suchergebnisse für: "{query}" ===
{anzahl} Ergebnisse gefunden

🎯 Direkt relevant
────────────────────────────────

📄 {Titel} ({type})
   Relevanz: ⭐⭐⭐⭐⭐ (9/10)
   Gefunden in: knowledge/projects/{name}/

   {2-3 Sätze Zusammenfassung was relevant ist}

   Key Insights:
   • {Insight 1}
   • {Insight 2}

   → Ganzes Dokument: knowledge/projects/{path}

📝 {Titel} ({type})
   Relevanz: ⭐⭐⭐⭐ (8/10)
   Gefunden in: knowledge/prompts/

   {Zusammenfassung}

   → Details: knowledge/prompts/{path}

🔗 Verwandt
────────────────────────────────

💡 {Idee-Titel} (Idee)
   Relevanz: ⭐⭐⭐ (6/10)

   {Warum relevant}

   → /idea-work {id}

📦 {Projekt-Name} (Projekt)
   Relevanz: ⭐⭐⭐ (6/10)

   {Relevante Learnings aus diesem Projekt}
```


#### Example



**Code:**
```bash
=== Antwort auf: "{Frage}" ===

💡 Direkte Antwort:
{Synthetisierte Antwort basierend auf gefundenem Wissen}

📚 Quellen:
────────────────────────────────
1. {Quelle 1} ({type})
   {Relevanter Ausschnitt}

2. {Quelle 2} ({type})
   {Relevanter Ausschnitt}

🔧 Praktische Steps:
{Falls anwendbar: konkrete Schritte basierend auf Wissen}

📖 Weitere Ressourcen:
{Links zu verwandten Dokumenten}
```


#### Example



**Code:**
```bash
=== Wissen über: "{Skill}" ===

📊 Dein Status:
{Ob Skill vorhanden, in Entwicklung, oder Gap}

📚 Vorhandenes Wissen:
────────────────────────────────
Projekte wo du {Skill} verwendet hast:
• {Projekt 1} - {was gemacht}
• {Projekt 2} - {was gemacht}

Gespeicherte Patterns:
• {Pattern 1} - {Beschreibung}

Prompts & Resources:
• {Resource 1}

💡 Ideen die {Skill} benötigen:
────────────────────────────────
• {Idee 1} (Potential: 8/10)
• {Idee 2} (Potential: 7/10)

→ Wenn du {Skill} entwickelst, öffnen sich {anzahl} Ideen

📖 Learning-Resources:
{Falls vorhanden in knowledge/resources/}

🎯 Empfohlene nächste Schritte:
{Konkrete Aktionen basierend auf Wissen}
```


#### Example



**Code:**
```bash
Du könntest auch interessiert sein an:
• {Verwandtes Thema 1} - {warum relevant}
• {Verwandtes Thema 2} - {warum relevant}
```


#### Example



**Code:**
```bash
📊 Pattern erkannt:
{Mehrere Ergebnisse zeigen dass...}
Insight: {Was das bedeutet}
```


#### Example



**Code:**
```bash
Nächste Schritte:
[1] Dokument lesen - Zeige vollständigen Inhalt
[2] Verwandtes suchen - Suche weiter zu verwandtem Thema
[3] Neue Suche
[4] Wissen hinzufügen - Falls du etwas zu diesem Thema beitragen willst

Was möchtest du tun?
```


#### Example



**Code:**
```bash
/knowledge-add - Neues Wissen zu diesem Thema hinzufügen
/idea-new - Idee basierend auf diesem Wissen
```


#### Example



**Code:**
```bash
❌ Keine direkten Ergebnisse für "{query}"

Mögliche Gründe:
• Noch kein Wissen zu diesem Thema gespeichert
• Andere Begriffe verwendet (suche nach Synonymen)

Vorschläge:
────────────────────────────────
🔍 Ähnliche Themen in deiner Knowledge Base:
• {Ähnliches Thema 1}
• {Ähnliches Thema 2}

💡 Ideen die verwandt sein könnten:
• {Idee 1}

📝 Möchtest du Wissen zu "{query}" hinzufügen?
→ /knowledge-add

🌐 Oder soll ich im Web nach "{query}" suchen?
→ /web-search {query} (falls verfügbar)
```




## Configuration



## Best Practices




## Related



---

<small>Source: `.claude/commands/knowledge-search.md`</small>
