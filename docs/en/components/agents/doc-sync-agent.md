---
title: doc-sync-agent
type: agent
tags: []
lang: en
confidence: 100
---

# doc-sync-agent


## Overview

<div class="component-meta" markdown>
| Attribute | Value |
|-----------|-------|
| **Type** | Agent |
| **Purpose** | Component description |
| **Complexity** | medium |
| **Model** | sonnet |
| **Category** | agents || **Created** | 2026-01-08 |</div>


## What It Does

"Aktualisiert Master-Docs und Knowledge Graph bei Finding-Integration"


## System Impact




## Architecture




## Usage


### Examples

#### Example



**Code:**
```json
{
  "finding": {
    "name": "chunking-strategy",
    "type": "template",
    "path": ".claude/templates/chunking-strategy.md",
    "source_repo": "crawl4ai",
    "tags": ["llm", "chunking", "rag"],
    "description": "Kurze Beschreibung des Findings"
  }
}
```


#### Example



**Code:**
```python
def sync_docs(finding):
    changes = {}

    # 1. README.md Counts
    readme_changes = update_readme_counts(finding)
    changes["README.md"] = readme_changes

    # 2. SYSTEM-MAP.md Entry
    sysmap_changes = update_system_map(finding)
    changes["SYSTEM-MAP.md"] = sysmap_changes

    # 3. Knowledge Graph Node
    graph_changes = create_graph_node(finding)
    changes["_graph/knowledge-nodes.json"] = graph_changes

    # 4. Type-spezifische Updates
    if finding["type"] in ["pattern", "learning"]:
        kb_changes = update_knowledge_index(finding)
        changes["knowledge/index.md"] = kb_changes

    if finding["type"] == "command":
        cmd_changes = update_commands_md(finding)
        changes[".claude/COMMANDS.md"] = cmd_changes

    return {
        "status": "SUCCESS",
        "updated_files": list(changes.keys()),
        "changes": changes
    }
```


#### Example



**Code:**
```python
def update_readme_counts(finding):
    readme = Read("README.md")

    # Finde Stats-Sektion
    stats_section = extract_stats_section(readme)

    # Mapping: type -> count field
    type_to_field = {
        "template": "Templates",
        "pattern": "Patterns",
        "learning": "Learnings",
        "command": "Commands",
        "agent": "Agents"
    }

    field = type_to_field.get(finding["type"])
    if field:
        current_count = extract_count(stats_section, field)
        new_count = current_count + 1

        # Edit: Count erhöhen
        Edit("README.md",
             old_string=f"{field}: {current_count}",
             new_string=f"{field}: {new_count}")

        return {"field": field, "old": current_count, "new": new_count}

    return {"field": None, "skipped": True}
```


#### Example



**Code:**
```python
def update_system_map(finding):
    sysmap = Read(".claude/SYSTEM-MAP.md")

    # 1. Finde passende Tabelle
    section = find_section_for_type(sysmap, finding["type"])

    # 2. Generiere Tabellen-Zeile
    if finding["type"] == "template":
        row = f"| `{finding['name']}` | {finding['description']} | {', '.join(finding['tags'])} |"
    elif finding["type"] == "pattern":
        row = f"| [{finding['name']}]({finding['path']}) | {finding['description']} |"
    elif finding["type"] == "command":
        row = f"| `/{finding['name']}` | {finding['description']} |"
    else:
        row = f"| `{finding['name']}` | {finding['description']} |"

    # 3. Füge Zeile zur Tabelle hinzu (nach Header-Zeile)
    table_end = find_table_end(section)
    Edit(".claude/SYSTEM-MAP.md",
         old_string=table_end,
         new_string=f"{row}\n{table_end}")

    # 4. Changelog Entry
    today = get_date()
    changelog_entry = f"- {today}: Added {finding['type']} `{finding['name']}` from {finding['source_repo']}"

    changelog_section = find_changelog(sysmap)
    Edit(".claude/SYSTEM-MAP.md",
         old_string=changelog_section[:100],
         new_string=f"{changelog_entry}\n{changelog_section[:100]}")

    return {"table": section, "row_added": row, "changelog": changelog_entry}
```


#### Example



**Code:**
```json
{
  "id": "template-chunking-strategy",
  "type": "template",
  "name": "chunking-strategy",
  "description": "...",
  "path": ".claude/templates/chunking-strategy.md",
  "tags": ["llm", "chunking", "rag"],
  "source": "external:crawl4ai",
  "created": "2026-01-08",
  "relations": []
}
```


#### Example



**Code:**
```python
def create_graph_node(finding):
    graph = Read("_graph/knowledge-nodes.json")
    nodes = json.loads(graph)

    # 1. ID generieren
    node_id = f"{finding['type']}-{finding['name']}"

    # 2. Prüfe ob Node existiert
    if any(n["id"] == node_id for n in nodes["nodes"]):
        return {"skipped": True, "reason": "Node exists"}

    # 3. Neuen Node erstellen
    new_node = {
        "id": node_id,
        "type": finding["type"],
        "name": finding["name"],
        "description": finding.get("description", ""),
        "path": finding["path"],
        "tags": finding.get("tags", []),
        "source": f"external:{finding['source_repo']}",
        "created": get_date(),
        "relations": []
    }

    # 4. Zur Liste hinzufügen
    nodes["nodes"].append(new_node)
    nodes["count"] = len(nodes["nodes"])

    # 5. Schreiben
    Write("_graph/knowledge-nodes.json", json.dumps(nodes, indent=2))

    return {"node_id": node_id, "count": nodes["count"]}
```


#### Example



**Code:**
```python
def update_knowledge_index(finding):
    if finding["type"] not in ["pattern", "learning"]:
        return {"skipped": True}

    index = Read("knowledge/index.md")

    # Finde passende Sektion
    if finding["type"] == "pattern":
        section = "## Patterns"
    else:
        section = "## Learnings"

    # Generiere Entry
    entry = f"- [{finding['name']}]({finding['path']}) - {finding['description']}"

    # Füge nach Sektion-Header ein
    section_content = find_section(index, section)
    Edit("knowledge/index.md",
         old_string=section_content[:50],
         new_string=f"{section_content[:50]}\n{entry}")

    return {"section": section, "entry": entry}
```


#### Example



**Code:**
```python
def update_commands_md(finding):
    if finding["type"] != "command":
        return {"skipped": True}

    commands = Read(".claude/COMMANDS.md")

    # Finde passende Kategorie basierend auf Tags
    category = determine_category(finding["tags"])

    # Generiere Command-Entry
    entry = f"""
### /{finding['name']}

{finding['description']}

**Source**: {finding['source_repo']}
"""

    # Füge in Kategorie ein
    category_section = find_section(commands, f"## {category}")
    Edit(".claude/COMMANDS.md",
         old_string=category_section[-50:],
         new_string=f"{category_section[-50:]}\n{entry}")

    return {"category": category, "command": finding["name"]}
```


#### Example



**Code:**
```json
{
  "status": "SUCCESS",
  "updated_files": [
    "README.md",
    "SYSTEM-MAP.md",
    "_graph/knowledge-nodes.json"
  ],
  "changes": {
    "README.md": {
      "field": "Templates",
      "old": 12,
      "new": 13
    },
    "SYSTEM-MAP.md": {
      "table": "Templates",
      "row_added": "| `chunking-strategy` | ... |",
      "changelog": "- 2026-01-08: Added template `chunking-strategy` from crawl4ai"
    },
    "_graph/knowledge-nodes.json": {
      "node_id": "template-chunking-strategy",
      "count": 288
    }
  }
}
```


#### Example



**Code:**
```bash
@doc-sync-agent
{
  "finding": {
    "name": "chunking-strategy",
    "type": "template",
    "path": ".claude/templates/chunking-strategy.md",
    "source_repo": "crawl4ai",
    "tags": ["llm", "chunking", "rag"],
    "description": "Chunking-Strategien für RAG Pipelines"
  }
}
```




## Configuration



## Best Practices




## Related



---

<small>Source: `.claude/agents/doc-sync-agent.md`</small>
