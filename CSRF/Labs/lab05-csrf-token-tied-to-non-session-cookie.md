# Lab05 - CSRF Token Tied To Non-Session Cookie

## Objective

Exploit a CSRF vulnerability where the CSRF token is tied to a separate cookie instead of the authenticated session.

---

# Lab Difficulty

```text
Practitioner
```

---

# Vulnerability Overview

The application binds:

```text
CSRF Token
        ↓
csrfKey Cookie
```

instead of:

```text
CSRF Token
        ↓
Session Cookie
```

This allows attackers to inject their own csrfKey cookie and matching token.

---

# Root Cause

Two independent mechanisms exist:

```text
Session Management
        ↓
session Cookie

CSRF Protection
        ↓
csrfKey Cookie
```

The two systems are not integrated.

---

# Analysis

Request:

```http
Cookie:
session=XXXX
csrfKey=YYYY

csrf=ZZZZ
```

---

Changing:

```text
session Cookie
```

logs user out.

---

Changing:

```text
csrfKey Cookie
```

only invalidates token.

---

This indicates:

```text
Token ↔ csrfKey
```

but NOT:

```text
Token ↔ Session
```

---

# Attack Methodology

```text
Obtain Valid Token
        ↓
Obtain Matching csrfKey
        ↓
Inject csrfKey Cookie
        ↓
Submit Matching Token
        ↓
Validation Passes
```

---

# Exploitation Steps

### Step 1

Capture update email request.

---

### Step 2

Determine:

```text
csrfKey ↔ csrf Token
```

relationship.

---

### Step 3

Use second account.

---

### Step 4

Swap:

```text
csrfKey
csrf Token
```

from attacker account.

---

### Step 5

Observe:

```text
Request Accepted
```

---

### Step 6

Identify search functionality vulnerable to CRLF injection.

---

### Step 7

Inject cookie:

```http
Set-Cookie: csrfKey=ATTACKER_KEY
```

---

### Step 8

Create exploit containing:

```html
<img src="COOKIE_INJECTION_URL"
onerror="document.forms[0].submit()">
```

---

### Step 9

Submit matching token.

---

### Step 10

Deliver exploit.

---

# Why The Attack Works

The application validates:

```text
csrfKey ↔ csrf Token
```

but never checks:

```text
Session ↔ Token
```

---

# Mitigation

Applications should:

- Bind tokens directly to sessions
- Prevent arbitrary cookie injection
- Implement SameSite protections

---

# Related Theory

- `08-common-flaws-in-csrf-token-validation.md`

---

# Related Payloads

- `csrf-token-bypass-techniques.md`
- `csrf-token-analysis-notes.md`

---

# Key Learnings

- Token binding must use authenticated sessions.
- Separate cookie-based validation is dangerous.
- Cookie injection often leads to CSRF bypass.

> [!IMPORTANT]
> CSRF protection should always be integrated with session management.