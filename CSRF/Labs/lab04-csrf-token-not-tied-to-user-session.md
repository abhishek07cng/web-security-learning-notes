# Lab04 - CSRF Token Not Tied To User Session

## Objective

Exploit a CSRF vulnerability where CSRF tokens are valid across different user sessions.

---

# Lab Difficulty

```text
Practitioner
```

---

# Vulnerability Overview

The application uses CSRF tokens but fails to bind them to individual user sessions.

As a result:

```text
Any Valid Token
        ↓
Accepted By Any User
```

---

# Root Cause

The application maintains a global pool of valid CSRF tokens.

Instead of validating:

```text
Session ↔ Token
```

it only checks:

```text
Token Exists
```

---

# Analysis

Account A:

```text
wiener:peter
```

CSRF Token:

```text
ABC123
```

---

Account B:

```text
carlos:montoya
```

Replace Account B token with:

```text
ABC123
```

Request accepted.

---

# Attack Methodology

```text
Login As Attacker
        ↓
Obtain Valid Token
        ↓
Create CSRF Payload
        ↓
Embed Attacker Token
        ↓
Victim Executes Request
        ↓
Request Accepted
```

---

# Exploitation Steps

### Step 1

Login as:

```text
wiener:peter
```

---

### Step 2

Capture email change request.

---

### Step 3

Copy CSRF token.

---

### Step 4

Login as:

```text
carlos:montoya
```

---

### Step 5

Replace Carlos token with Wiener's token.

---

### Step 6

Observe:

```text
Request Accepted
```

---

### Step 7

Generate CSRF PoC using attacker's token.

---

### Step 8

Host exploit.

---

### Step 9

Deliver exploit.

---

# Why The Attack Works

The application validates:

```text
Token Valid?
```

but never verifies:

```text
Token Belongs To Session?
```

---

# Mitigation

Applications should:

- Bind tokens to user sessions
- Generate unique session-specific tokens
- Invalidate reused tokens

---

# Related Theory

- `07-what-is-a-csrf-token.md`
- `08-common-flaws-in-csrf-token-validation.md`

---

# Related Payloads

- `csrf-token-analysis-notes.md`
- `csrf-token-bypass-techniques.md`

---

# Key Learnings

- Tokens must be session-specific.
- Token existence alone is insufficient.
- Session binding is a critical security requirement.

> [!WARNING]
> Accepting tokens from different users completely breaks CSRF protection.