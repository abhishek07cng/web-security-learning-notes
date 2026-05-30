# Lab03 - CSRF Where Token Validation Depends On Token Being Present

## Objective

Exploit a CSRF vulnerability by removing the CSRF token parameter entirely.

---

# Vulnerability Overview

The application validates CSRF tokens only when the token parameter exists.

If the parameter is removed:

```text
Validation Skipped
```

---

# Root Cause

The application performs:

```text
IF Token Exists
    Validate Token
ELSE
    Accept Request
```

instead of:

```text
Token Required
```

---

# Analysis

Request with invalid token:

```http
csrf=fake123
```

Rejected.

---

Request without token:

```http
email=attacker@evil.com
```

Accepted.

---

# Attack Methodology

```text
Capture Request
        ↓
Remove Token Parameter
        ↓
Verify Acceptance
        ↓
Generate PoC
        ↓
Deliver Attack
```

---

# Exploitation Steps

1. Capture email change request.

2. Modify token.

```text
Rejected
```

3. Remove entire csrf parameter.

```text
Accepted
```

4. Generate PoC.

5. Host exploit.

6. Deliver to victim.

---

# Why The Attack Works

The application incorrectly assumes:

```text
Missing Token
        ↓
No Validation Needed
```

---

# Mitigation

Applications should:

- Require tokens
- Reject missing tokens
- Validate every request

---

# Related Theory

- `08-common-flaws-in-csrf-token-validation.md`

---

# Key Learnings

- Missing token must always cause rejection.
- Optional CSRF validation is ineffective.

> [!IMPORTANT]
> A missing token should be treated exactly like an invalid token.