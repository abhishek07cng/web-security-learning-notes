# How Does CSRF Work?

## Overview

CSRF works by abusing the browser's automatic credential handling behavior.

If specific conditions are met, attackers can force authenticated victims to perform unintended actions.

---

# The 3 Required Conditions for CSRF

For a CSRF attack to succeed, THREE conditions must exist simultaneously.

---

# 1. Relevant Action

There must be a meaningful action worth exploiting.

Examples:

- changing email addresses
- changing passwords
- transferring funds
- modifying permissions

---

# 2. Cookie-Based Session Handling

The application must rely on authentication credentials automatically attached by the browser.

Common vulnerable mechanisms:

- session cookies
- HTTP Basic Authentication
- client certificates

---

# 3. No Unpredictable Parameters

The attacker must be able to fully construct the request.

---

## Vulnerable Example

```http
POST /change-email

email=attacker@evil.com
```

---

## More Secure Example

```http
POST /change-password

current-password=SECRET
new-password=test123
```

If unpredictable information is required, CSRF becomes much harder.

---

# Full CSRF Attack Flow

```text
Victim logs into legitimate site
        ↓
Session cookie stored in browser
        ↓
Victim visits malicious website
        ↓
Malicious page sends forged request
        ↓
Browser automatically attaches session cookie
        ↓
Server processes request as legitimate
```

---

# Important Browser Behavior

The browser automatically sends cookies:

```text
WITHOUT checking whether the request originated from a trusted site.
```

This is the core behavior CSRF exploits.

---

# Example Vulnerable Request

```http
POST /email/change HTTP/1.1
Cookie: session=abc123

email=attacker@evil.com
```

---

# Why Same-Origin Policy Does Not Stop CSRF

The Same-Origin Policy:

- blocks malicious sites from READING responses
- does NOT block request sending

This allows forged requests to succeed silently.

---

# SameSite Cookie Discussion

Modern browsers often use:

```text
SameSite=Lax
```

by default.

This helps reduce CSRF risk by limiting when cookies are attached to cross-site requests.

---

# Authentication Mechanism Comparison

| Mechanism | CSRF Risk |
|---|---|
| Session Cookies | Vulnerable |
| HTTP Basic Auth | Vulnerable |
| Client Certificates | Vulnerable |
| Bearer Tokens | Usually Safer |

---

# Related Theory

- `Theory/01-what-is-csrf.md`

---

# Related Payloads

- `Payloads/csrf-test-checklist.md`
- `Payloads/csrf-token-analysis-notes.md`

---

# Related Notes

- `Notes/browser-behavior-notes.md`

---

# Key Takeaways

- CSRF relies on browser credential automation.
- Three conditions must exist simultaneously.
- Same-Origin Policy does not prevent forged requests.

> [!IMPORTANT]
> If any one of the required conditions is broken, CSRF usually fails.