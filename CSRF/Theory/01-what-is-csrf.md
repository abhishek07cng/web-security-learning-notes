# What is CSRF?

## Overview

CSRF (Cross-Site Request Forgery) is a web security vulnerability where a malicious website tricks a victim's browser into performing unintended actions on another website where the victim is already authenticated.

The attack abuses the trust a web application places in a user's browser session.

---

# Simple Definition

```text
A CSRF attack forces a logged-in victim to send unintended requests to a vulnerable web application.
```

---

# How CSRF Happens

## Example Scenario

1. A user logs into their banking application.
2. The server creates a session cookie.
3. The user visits a malicious website without logging out.
4. The malicious website silently sends a request to the bank.
5. The browser automatically attaches the session cookie.
6. The bank processes the request as legitimate.

---

# Why CSRF Works

CSRF works because browsers automatically attach authentication credentials such as:

- session cookies
- HTTP Basic Authentication
- client certificates

to outgoing requests.

The server cannot easily distinguish between:

- legitimate user requests
- attacker-forged requests

---

# Role of the Same-Origin Policy (SOP)

Interestingly, CSRF exploits browser behavior despite the Same-Origin Policy.

---

## Important Concept

The Same-Origin Policy:

- prevents malicious sites from READING responses
- does NOT prevent browsers from SENDING requests

This means attackers cannot see the response, but they can still trigger actions.

---

# Common Targets of CSRF

CSRF usually targets state-changing actions such as:

```http
POST /change-email
POST /change-password
POST /transfer-funds
DELETE /account
```

---

# Common Authentication Mechanisms Vulnerable to CSRF

| Authentication Mechanism | CSRF Risk |
|---|---|
| Session Cookies | Vulnerable |
| HTTP Basic Authentication | Vulnerable |
| Client Certificates | Vulnerable |
| Bearer Tokens in Authorization Header | Usually Not Vulnerable |

---

# Why Bearer Tokens Resist CSRF

Bearer tokens are usually sent manually using JavaScript:

```http
Authorization: Bearer TOKEN
```

Cross-site pages cannot set these headers due to browser security restrictions.

---

# Key Characteristics of CSRF

- Victim must already be authenticated
- Attack occurs silently
- Victim usually sees nothing
- Browser automatically attaches credentials
- Attacker typically cannot read responses

---

# Real-World Example

## Vulnerable Request

```http
POST /change-email HTTP/1.1
Cookie: session=abc123

email=attacker@evil.com
```

If no CSRF protection exists, an attacker can force the victim's browser to send this request.

---

# Related Labs

- `Labs/lab01-basic-csrf.md`

---

# Related Payloads

- `Payloads/csrf-cheatsheet.md`
- `Payloads/auto-submit-form-payloads.md`

---

# Related Notes

- `Notes/browser-behavior-notes.md`

---

# Key Takeaways

- CSRF abuses browser trust.
- Browsers automatically attach cookies to requests.
- Same-Origin Policy does NOT stop forged requests.
- CSRF targets actions, not data theft directly.

> [!IMPORTANT]
> CSRF is possible because browsers automatically include authentication credentials in requests.