---
title: iterative-retrieval-pattern
type: pattern
tags: []
lang: en
confidence: 100
---

# iterative-retrieval-pattern


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
Input:
├─ Suchziel (z.B. "authentication handling")
├─ Kontextmarker (z.B. "recent changes", "error pattern")
├─ Excluded Paths (z.B. node_modules, .git)
└─ Max Files zu returnen (z.B. 10)

Output:
└─ [{ file: "path", confidence: 0.X }, ...]
```


#### Example



**Code:**
```bash
Sende an Sub-Agent:
"Find all files related to user authentication.
 Focus on login flow, session management, token validation.
 Exclude: node_modules, dist, .git
 Return max 10 files with confidence scores."
```


#### Example



**Code:**
```json
[
  { file: "src/auth/login.ts", relevance: 0.95, reason: "core login logic" },
  { file: "src/auth/middleware.ts", relevance: 0.88, reason: "auth validation" },
  { file: "src/session/session.ts", relevance: 0.82, reason: "session handling" },
  { file: "src/utils/token.ts", relevance: 0.75, reason: "JWT operations" },
  { file: "src/user/user.ts", relevance: 0.62, reason: "user data model" }
]
```


#### Example



**Code:**
```bash
Aktuelle Funde: [login.ts, middleware.ts, session.ts]

Gap 1: "Session validation unclear"
  → Neue Keywords: "validateSession", "sessionMiddleware", "jwt-verify"

Gap 2: "Token refresh not visible"
  → Neue Keywords: "refreshToken", "tokenRefresh", "reauth"

Gap 3: "Error handling strategy unclear"
  → Neue Keywords: "authError", "UnauthorizedError", "AuthException"
```


#### Example



**Code:**
```bash
Identified Gaps:
1. Session validation (need middleware files)
2. Token refresh mechanism (need refresh handlers)
3. Error handling (need custom error classes)

Refined Keywords:
- Original: ["auth", "login", "session", "token"]
- Added: ["middleware", "refresh", "error", "unauthorized"]
- Result: ["auth", "login", "session", "token", "middleware", "refresh", "error"]
```


#### Example



**Code:**
```bash
Cycle N:
┌─────────────────────┐
│ 1. DISPATCH         │ ← Neue Keywords senden
│    (verfeinerte)    │
└────────┬────────────┘
         │
         ▼
┌─────────────────────┐
│ 2. EVALUATE         │ ← Files neu bewerten
└────────┬────────────┘
         │
         ▼
┌─────────────────────┐
│ 3. REFINE           │ ← Gaps neu identifizieren
│    oder TERMINATE?  │
└────────┬────────────┘
         │
    Terminiert?
    /       \
  JA        NEIN
   │         │
   ▼         ▼
 RETURN   NEXT CYCLE
```


#### Example



**Code:**
```bash
Cycle 1:
  - EVALUATE findet: 4 Files mit relevance >= 0.7
  - TERMINATE: ✅ Relevance Threshold erreicht

Cycle 1 (Alternative):
  - EVALUATE findet: 2 Files mit relevance >= 0.7
  - REFINE identifiziert keine neuen Keywords
  - TERMINATE: ✅ No New Gaps

Cycle 3:
  - Alle anderen Kriterien nicht erfüllt
  - TERMINATE: ✅ Max Cycles (3) erreicht
```


#### Example



**Code:**
```bash
┌─────────────────────────────────────────────────────────────┐
│                   ITERATIVE RETRIEVAL FLOW                  │
└─────────────────────────────────────────────────────────────┘

Input: Search Goal + Context Markers
       ↓
   ╔═══════════════════════════════════════════════════════╗
   ║          CYCLE 1: Initial Exploration                 ║
   ╠═══════════════════════════════════════════════════════╣
   ║                                                        ║
   ║  [1] DISPATCH                                         ║
   ║      Keywords: ["auth", "login", "session", "token"]  ║
   ║      ↓                                                 ║
   ║  [2] EVALUATE                                         ║
   ║      Found 5 files                                    ║
   ║      ├─ auth.ts (0.95) ✅                              ║
   ║      ├─ session.ts (0.82) ✅                           ║
   ║      ├─ token.ts (0.75) ✅                             ║
   ║      ├─ user.ts (0.62)                                ║
   ║      └─ config.ts (0.45)                              ║
   ║      ↓                                                 ║
   ║  [3] REFINE                                           ║
   ║      Gaps found:                                      ║
   ║      ├─ Session validation unclear                    ║
   ║      ├─ Token refresh not visible                     ║
   ║      └─ Error handling strategy unclear               ║
   ║      ↓                                                 ║
   ║  [4] CHECK TERMINATION                               ║
   ║      ├─ Relevance >= 0.7? 3 files ✅                  ║
   ║      ├─ Self-report sufficient? ❌                     ║
   ║      ├─ No new gaps? ❌                                ║
   ║      └─ Max cycles (1/3)? ❌                           ║
   ║      → CONTINUE                                        ║
   ║                                                        ║
   ╠═══════════════════════════════════════════════════════╣
   ║          CYCLE 2: Gap-Driven Refinement                ║
   ╠═══════════════════════════════════════════════════════╣
   ║                                                        ║
   ║  [1] DISPATCH (refined)                               ║
   ║      Keywords: [+ "middleware", "refresh", "error"]   ║
   ║      ↓                                                 ║
   ║  [2] EVALUATE                                         ║
   ║      Found 4 new files                                ║
   ║      ├─ authMiddleware.ts (0.93) ✅                    ║
   ║      ├─ tokenRefresh.ts (0.88) ✅                      ║
   ║      ├─ authError.ts (0.81) ✅                         ║
   ║      └─ errorHandler.ts (0.68)                        ║
   ║      ↓                                                 ║
   ║  [3] REFINE                                           ║
   ║      Gaps found:                                      ║
   ║      ├─ Permission check logic unclear                ║
   ║      └─ Rate limiting mechanism unclear               ║
   ║      ↓                                                 ║
   ║  [4] CHECK TERMINATION                               ║
   ║      ├─ Relevance >= 0.7? 6 files ✅                  ║
   ║      └─ TERMINATE: Threshold met!                     ║
   ║                                                        ║
   ╚═══════════════════════════════════════════════════════╝
       ↓
   RESULT: 6 files with high relevance
   Files ready for deep analysis
```


#### Example



**Code:**
```bash
DISPATCH
├─ Goal: "authentication flow, login failures"
├─ Context: "recent bug report: users locked after 3 failed logins"
└─ Keywords: ["auth", "login", "session", "token", "failure"]

EVALUATE
├─ src/auth/login.ts (0.95) - core login handler
├─ src/auth/session.ts (0.88) - session management
├─ src/auth/jwt.ts (0.82) - token operations
├─ src/user/user.ts (0.65) - user data
└─ src/config/auth.config.ts (0.52) - configuration

REFINE - Gaps identified:
├─ Gap 1: "Login attempt tracking unclear"
│  → Add keywords: ["attempt", "counter", "lock", "rate-limit"]
├─ Gap 2: "Error responses unclear"
│  → Add keywords: ["error", "exception", "unauthorized"]
└─ Gap 3: "Middleware validation missing"
│  → Add keywords: ["middleware", "validate", "check"]

CHECK TERMINATION
├─ 3+ files with relevance >= 0.7? YES (3 files)
├─ Self-report sufficient? NO
├─ No new gaps? NO
├─ Max cycles (1/3)? NO
└─ ACTION: CONTINUE
```


#### Example



**Code:**
```bash
DISPATCH (refined keywords)
├─ New keywords: ["attempt", "counter", "lock", "rate-limit", "middleware", "error"]
└─ Searching for: attempt tracking, rate limiting, validation

EVALUATE (new search)
├─ src/auth/attemptCounter.ts (0.93) - login attempt tracking
├─ src/auth/rateLimiter.ts (0.90) - rate limiting logic
├─ src/auth/authMiddleware.ts (0.87) - validation middleware
├─ src/error/AuthError.ts (0.85) - auth exceptions
└─ src/config/lockout.config.ts (0.78) - lockout settings

REFINE - Gaps identified:
├─ Gap 1: "Lockout reset mechanism unclear"
│  → Add keyword: ["reset", "unlock", "clear"]
├─ Gap 2: "Admin unlock functionality"
│  → Add keyword: ["admin", "force-unlock", "override"]
└─ Gap 3: "Audit logging"
│  → Add keyword: ["audit", "log", "track"]

CHECK TERMINATION
├─ 3+ files with relevance >= 0.7? YES (6 files total)
├─ Self-report sufficient? NO
├─ No new gaps? NO
├─ Max cycles (2/3)? NO
└─ ACTION: CONTINUE
```


#### Example



**Code:**
```bash
DISPATCH (fully refined)
├─ New keywords: ["reset", "unlock", "admin", "audit", "log"]
└─ Searching for: unlock mechanisms, admin overrides, audit trails

EVALUATE (final search)
├─ src/admin/unlockUser.ts (0.91) - admin unlock endpoint
├─ src/auth/lockoutReset.ts (0.88) - automatic reset logic
├─ src/audit/authAudit.ts (0.86) - audit logging
└─ src/utils/adminCheck.ts (0.79) - admin verification

REFINE - Gaps identified:
├─ No significant gaps remaining
└─ System understanding is sufficient

CHECK TERMINATION
├─ 3+ files with relevance >= 0.7? YES (9 files total)
├─ Self-report sufficient? YES
├─ No new gaps? YES
├─ TERMINATE: Multiple criteria met!
└─ ACTION: RETURN RESULTS
```


#### Example



**Code:**
```bash
9 files collected with high relevance (>= 0.7):
├─ Core Authentication (3 files)
│  ├─ auth/login.ts (0.95)
│  ├─ auth/session.ts (0.88)
│  └─ auth/jwt.ts (0.82)
├─ Security Controls (3 files)
│  ├─ auth/attemptCounter.ts (0.93)
│  ├─ auth/rateLimiter.ts (0.90)
│  └─ auth/authMiddleware.ts (0.87)
├─ Error Handling (2 files)
│  ├─ error/AuthError.ts (0.85)
│  └─ auth/lockoutReset.ts (0.88)
└─ Admin & Audit (1 file)
   └─ admin/unlockUser.ts (0.91)

Ready for detailed analysis of login failure mechanism.
```


#### Example



**Code:**
```bash
User: "Login failures increased 10% last week"

Iterative Retrieval:
→ Dispatch: authentication, login, error, recent
→ Evaluate: auth.ts (0.95), session.ts (0.88), logging.ts (0.72)
→ Refine: identify gaps in rate limiting, monitoring
→ Loop 2: rate-limiter.ts (0.91), monitor.ts (0.84)
→ Terminate: sufficient context for root cause analysis
```


#### Example



**Code:**
```bash
Developer: "How to add 2FA to existing auth system?"

Iterative Retrieval:
→ Dispatch: auth, login, session, token
→ Evaluate: core auth files found
→ Refine: identify gaps in user preferences, secrets storage
→ Loop 2: user-settings.ts, secrets.ts found
→ Loop 3: identify integration points
→ Terminate: architecture understood
```


#### Example



**Code:**
```bash
Task: "Refactor auth module to new pattern"

Iterative Retrieval:
→ Dispatch: components using auth, imports, references
→ Evaluate: find all dependent modules
→ Refine: identify indirect dependencies
→ Loop 2: discover deeper chains
→ Terminate: full dependency graph available
```


#### Example



**Code:**
```bash
User: "Find all places where user tokens are validated"

Explore Agent:
1. DISPATCH: ["token", "validation", "check", "verify"]
2. EVALUATE: finds 5 core files
3. REFINE: identifies gaps in middleware, interceptors
4. LOOP 2: finds 3 additional files
5. TERMINATE: returns 8-file context with high confidence
```


#### Example



**Code:**
```bash
User: "Why are database queries timing out in production?"

Debugger Agent:
1. DISPATCH: ["database", "query", "timeout", "pool", "connection"]
2. EVALUATE: finds database layer files
3. REFINE: identifies gaps in monitoring, pool management
4. LOOP 2: finds pool config, monitoring setup
5. LOOP 3: finds recent changes to connection limits
6. TERMINATE: context sufficient for RCA
```


#### Example



**Code:**
```bash
→ Erhöhe Relevance-Threshold in EVALUATE
→ Oder: Verfeinere Keywords um zu fokussieren
→ Max Ziel: 5-10 files bei Termination
```


#### Example



**Code:**
```bash
→ Keywords sind zu spezifisch
→ Cycle 2: Neue Suchstrategie (breitere Keywords)
→ Fallback: Manueller Exploration starten
```


#### Example



**Code:**
```bash
→ Codebase-Struktur unklar
→ Feature könnte nicht existieren
→ Cycle 3: Sub-Agent sollte explizites "not found" melden
```




## Configuration



## Best Practices




## Related


---

<small>Source: `knowledge/patterns/iterative-retrieval-pattern.md`</small>
