# Preventing Access Control Vulnerabilities

## Overview

Broken Access Control is consistently one of the most critical web security issues.

Prevention requires:

```text
Deny By Default
+
Server-Side Enforcement
+
Consistent Validation
```

---

# Principle 1

## Deny By Default

Users should receive:

```text
No Access
```

unless explicitly authorized.

---

# Principle 2

## Validate Server-Side

Never trust:

```text
JavaScript
Cookies
Hidden Fields
Headers
URLs
```

---

Authorization decisions belong on:

```text
Server
```

---

# Principle 3

## Centralize Access Control

Avoid:

```text
Authorization Logic
Scattered Everywhere
```

---

Prefer:

```text
Single Authorization Layer
```

---

# Principle 4

## Enforce Ownership Checks

Example:

```text
User A
Cannot Access
User B Resources
```

---

# Principle 5

## Validate Every Request

Do not assume:

```text
User Previously Passed Checks
```

---

Every request must verify:

```text
Authentication
Authorization
Ownership
```

---

# Principle 6

## Avoid Security Through Obscurity

Bad:

```text
/admin-7f9a2x
```

---

Good:

```text
Proper Authorization Checks
```

---

# Principle 7

## Log Authorization Failures

Monitor:

```text
403 Responses
Privilege Escalation Attempts
IDOR Enumeration
```

---

# Secure Access Control Model

```text
Request
        ↓
Authentication
        ↓
Authorization
        ↓
Ownership Validation
        ↓
Resource Access
```

---

# Bug Bounty Perspective

Most Critical Findings Come From:

```text
IDOR
Admin Access
Role Manipulation
Workflow Bypass
```

because authorization is often overlooked.

---

# Key Takeaways

- Deny by default.
- Validate every request.
- Never trust client-controlled data.
- Centralized authorization is easier to secure.