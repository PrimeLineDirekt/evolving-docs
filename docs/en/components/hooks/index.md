---
title: Hooks
lang: en
---

# Hooks

Documentation for all hooks in the Evolving system.

## At a Glance

<div class="component-grid" markdown>
<div class="component-card">
<h3>22</h3>
<p>Total Hooks</p>
</div>
</div>


## All Hook

### A

- [Auto Archival](auto-archival.md) - Auto-Archival Hook Central orchestrator for automated data cleanup and archival.
Runs at Stop events- [Auto Cross Reference](auto-cross-reference.md) -  Auto Cross-Reference Hook (v4.0) Auto-syncs Master Documents after structural changes  Trigger: Pos
### C

- [Code Review Reminder](code-review-reminder.md) - PostToolUse Hook: Code Review Reminder
Triggers after Write/Edit on code files to remind about featu- [Context Monitor](context-monitor.md) - Context Monitor v2 - StatusLine with Context Budget Awareness  Format: 145K 72% | Evolving | Opus | - [Context Warning](context-warning.md) - Context Warning Hook - PreToolUse (v4 - Progressive Escalation) Warnt bei hohem Context % mit progre- [Correction Detector](correction-detector.md) - Correction Detector Hook - Self-Evolving System Detects user corrections in prompts and offers to ge
### D

- [Delegation Enforcer](delegation-enforcer.md) - Delegation Enforcer Hook (Multi-Event) Supports multiple hook events:
- UserPromptSubmit: Enforces d
### G

- [Graph Update](graph-update.md) -  Graph Update Hook (v1.0) Flags when knowledge graph needs updating after Write/Edit operations  Tri
### I

- [Inventory Update](inventory-update.md) - Inventory Update Hook Trigger: Nach Write/Edit in .claude/ oder knowledge/rules/ Aktion: component-c
### L

- [Ledger Auto Save](ledger-auto-save.md) -  Ledger Auto-Save Hook (v2 - Dynamic Snapshot) Generates fresh CURRENT.md from memory sources at ses
### N

- [Notification Sound](notification-sound.md) - Notification Sound Hook - Debug Version Log dass Hook getriggert wurde
### R

- [Ralph Loop Stop](ralph-loop-stop.md) -  Ralph Loop Stop Hook Prevents session exit when a ralph-loop is active Feeds the SAME prompt back t
### S

- [Security Tier Check](security-tier-check.md) - Security Tier Check Hook for Claude Code
PreToolUse hook that checks Bash commands against security - [Session End Cleanup](session-end-cleanup.md) -  Session End Cleanup Hook Archives session-specific security approvals when session ends  Usage: Cal- [Session Summary](session-summary.md) -  Session Summary Hook (Smart Version v2) Creates session summary ONLY when NEW meaningful work was d- [Session Task Sync](session-task-sync.md) - session-task-sync.sh - Syncs completed tasks to Memory on session end Trigger: Stop Event Purpose: B- [Subagent Router](subagent-router.md) - SubagentStop Router Hook for Claude Code
========================================= Automatically rou
### T

- [Template Reminder](template-reminder.md) - Template Sync Reminder Hook Triggers when new generic content is created that might be relevant for - [Tmux Hint](tmux-hint.md) - tmux-hint.py - Suggest tmux for long-running dev servers Hook: PreToolUse (Bash)
Trigger: When start
### U

- [Usage Tracker](usage-tracker.md) - usage-tracker.py - Track all tool usage with detailed analytics Hook: PostToolUse (for ALL tools) Lo- [Utils](utils.md) - Shared utilities for Evolving hooks Source this file: source "$(dirname "$0")/utils.sh" ============
### W

- [Weekly Inventory Check](weekly-inventory-check.md) - Weekly inventory check reminder.
Trigger: SessionStart Reminds user to run /tool-map for system inte



