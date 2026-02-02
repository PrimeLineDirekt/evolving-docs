---
title: health-dashboard
type: command
tags: []
lang: en
confidence: 100
---

# health-dashboard


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

Quick visual health overview - alle Key Metrics auf einen Blick


## System Impact




## Architecture




## Usage


### Examples

#### Example



**Code:**
```bash
git status --porcelain | wc -l
```


#### Example



**Code:**
```bash
╔═══════════════════════════════════════════════════════╗
║            EVOLVING HEALTH DASHBOARD                  ║
╠═══════════════════════════════════════════════════════╣
║ COMPONENTS                                            ║
║   {icon} Memory Files    {icon} Knowledge Graph       ║
║   {icon} Detection Index {icon} Ideas Storage         ║
║   {icon} Experience Storage                           ║
╠═══════════════════════════════════════════════════════╣
║ METRICS                                               ║
║   Projects: {active}/{total}    Ideas: {count}        ║
║   Experiences: {count}          Commands: {count}     ║
║   Agents: {count}               Skills: {count}       ║
╠═══════════════════════════════════════════════════════╣
║ STATUS                                                ║
║   Git: {clean/N changes}        Health: {score}       ║
╚═══════════════════════════════════════════════════════╝
```


#### Example



**Code:**
```bash
╔═══════════════════════════════════════════════════════╗
║            EVOLVING HEALTH DASHBOARD                  ║
╠═══════════════════════════════════════════════════════╣
║ COMPONENTS                                            ║
║   ✅ Memory Files    ✅ Knowledge Graph               ║
║   ✅ Detection Index ✅ Ideas Storage                 ║
║   ✅ Experience Storage                               ║
╠═══════════════════════════════════════════════════════╣
║ METRICS                                               ║
║   Projects: 2 active    Ideas: 42                     ║
║   Experiences: 27       Commands: 63                  ║
║   Agents: 12            Skills: 8                     ║
╠═══════════════════════════════════════════════════════╣
║ STATUS                                                ║
║   Git: clean            Health: 5/5 ✅                ║
╚═══════════════════════════════════════════════════════╝
```


#### Example



**Code:**
```bash
⚠️ Issues detected:
  - {component}: {issue description}

Run /system-health for detailed diagnostics.
```




## Configuration



## Best Practices




## Related



---

<small>Source: `.claude/commands/health-dashboard.md`</small>
