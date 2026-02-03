---
title: observation-compression-pattern
type: pattern
tags: []
lang: en
confidence: 100
---

# observation-compression-pattern


## Overview

<div class="component-meta" markdown>
| Attribute | Value |
|-----------|-------|
| **Type** | Pattern |
| **Purpose** | Component description |
| **Complexity** | medium |
| **Model** | sonnet |
| **Category** | patterns |</div>


## What It Does




## System Impact




## Architecture




## Usage


### Examples

#### Example



**Code:**
```bash
Standard Claude Code Session:
- Tool Output: ~2000-10000 Tokens pro Ausführung
- 50 Tool Uses = Context Window erschöpft
- Komplexität: O(N²) - Claude re-synthetisiert alle vorherigen Outputs
```


#### Example



**Code:**
```bash
Tool Output (~5000 Tokens)
         ↓
    AI Compression
         ↓
Observation (~500 Tokens)
         ↓
75-95% Token-Reduktion
```


#### Example



**Code:**
```typescript
interface Observation {
  id: string;
  type: 'decision' | 'bugfix' | 'feature' | 'refactor' | 'discovery' | 'change';
  title: string;           // ~10 Tokens
  subtitle?: string;       // ~20 Tokens
  narrative?: string;      // ~100-200 Tokens
  facts?: string[];        // ~100-200 Tokens
  files?: string[];        // ~20 Tokens
  timestamp: number;
}
```


#### Example



**Code:**
```bash
Du bist ein Observer der Tool-Ausführungen in semantische Observations komprimiert.

REGELN:
1. Fokus auf DELIVERABLES: Was wurde GEBAUT/GEFIXT/GELERNT?
2. NICHT dokumentieren was du tust, sondern was passiert ist
3. Verwende Action Verbs: implemented, fixed, deployed, configured
4. Max 500 Tokens pro Observation

GUTE Observation: "Authentication unterstützt jetzt OAuth2 mit Google Provider"
SCHLECHTE Observation: "Ich habe mir den Auth-Code angesehen"
```


#### Example



**Code:**
```xml
<tool_execution>
  <tool_name>Edit</tool_name>
  <timestamp>2025-12-16T14:30:00Z</timestamp>
  <working_directory>/project/src</working_directory>
  <input>
    {"file_path": "auth/oauth.ts", "old_string": "...", "new_string": "..."}
  </input>
  <outcome>
    File edited successfully. Added OAuth2 configuration...
  </outcome>
</tool_execution>
```


#### Example



**Code:**
```xml
<observation>
  <type>feature</type>
  <title>Added OAuth2 authentication with Google provider</title>
  <subtitle>Passport.js integration for social login</subtitle>
  <narrative>
    Implemented OAuth2 support using passport-google-oauth20.
    Users can now sign in with their Google accounts.
  </narrative>
  <facts>
    - Created auth/oauth.ts with passport configuration
    - Added GOOGLE_CLIENT_ID to environment
    - Extended User model with provider field
  </facts>
  <files>src/auth/oauth.ts, src/models/user.ts</files>
</observation>
```


#### Example



**Code:**
```typescript
const CHARS_PER_TOKEN = 4;

function estimateTokens(text: string): number {
  return Math.ceil(text.length / CHARS_PER_TOKEN);
}

function calculateObservationCost(obs: Observation): number {
  const content = [
    obs.title,
    obs.subtitle || '',
    obs.narrative || '',
    (obs.facts || []).join(' '),
    (obs.files || []).join(', ')
  ].join(' ');

  return estimateTokens(content);
}
```


#### Example



**Code:**
```bash
#!/bin/bash
# PostToolUse Hook für Observation Compression

read -r input

tool_name=$(echo "$input" | jq -r '.tool_name')
tool_output=$(echo "$input" | jq -r '.tool_response')

# Nur für bestimmte Tools
case "$tool_name" in
  Write|Edit|Bash)
    # Token-Schätzung
    tokens=$(echo "$tool_output" | wc -c)
    tokens=$((tokens / 4))

    if [ "$tokens" -gt 500 ]; then
      # Kompression triggern
      echo '{"compress": true, "estimated_tokens": '$tokens'}'
    fi
    ;;
esac
```


#### Example



**Code:**
```json
{
  "type": "observation",
  "compressed_from": "Edit tool output",
  "original_tokens": 2500,
  "compressed_tokens": 450,
  "compression_ratio": "82%"
}
```


#### Example



**Code:**
```bash
Standard Mode:
  Full Context → O(N²) → ~50 Tool Uses

Endless Mode:
  Compressed Observations → O(N) → ~1000+ Tool Uses
  Full Outputs → Archived to Disk
```


#### Example



**Code:**
```bash
Tool: Edit
File: src/auth/oauth.ts
Diff:
-// TODO: Add OAuth
+import passport from 'passport';
+import { Strategy as GoogleStrategy } from 'passport-google-oauth20';
+
+passport.use(new GoogleStrategy({
+    clientID: process.env.GOOGLE_CLIENT_ID,
+    clientSecret: process.env.GOOGLE_CLIENT_SECRET,
+    callbackURL: "/auth/google/callback"
+  },
+  function(accessToken, refreshToken, profile, cb) {
+    User.findOrCreate({ googleId: profile.id }, function (err, user) {
+      return cb(err, user);
+    });
+  }
+));
+
+export const googleAuth = passport.authenticate('google', { scope: ['profile', 'email'] });
+export const googleCallback = passport.authenticate('google', { failureRedirect: '/login' });

~1200 Tokens
```


#### Example



**Code:**
```bash
[feature] OAuth2 authentication with Google
- Added passport-google-oauth20 integration
- Created googleAuth and googleCallback exports
- Uses GOOGLE_CLIENT_ID from environment
Files: src/auth/oauth.ts

~80 Tokens (93% Reduktion)
```




## Configuration



## Best Practices




## Related


---

<small>Source: `knowledge/patterns/observation-compression-pattern.md`</small>
