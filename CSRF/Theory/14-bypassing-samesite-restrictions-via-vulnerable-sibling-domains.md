# Bypassing SameSite Restrictions via Vulnerable Sibling Domains

## Overview

SameSite cookies are designed to reduce the risk of CSRF attacks by restricting when browsers send cookies during cross-site requests.

However, SameSite protections can often be bypassed if an attacker gains code execution on a vulnerable sibling domain belonging to the same site.

This commonly occurs through vulnerabilities such as:

- Cross-Site Scripting (XSS)
- Cross-Site WebSocket Hijacking (CSWSH)
- Open Redirects
- Client-Side Redirect Gadgets

---

# Same-Site vs Same-Origin

Understanding this distinction is critical.

---

## Same-Origin

An origin consists of:

```text
Scheme + Host + Port
```

Example:

```text
https://app.example.com
https://admin.example.com
```

Result:

```text
Same-Origin ❌
```

---

## Same-Site

A site consists of:

```text
Scheme + eTLD+1
```

Example:

```text
https://app.example.com
https://admin.example.com
```

Result:

```text
Same-Site ✅
```

---

# Why This Matters

SameSite cookies use:

```text
Same-Site
```

logic.

They do NOT use:

```text
Same-Origin
```

logic.

Therefore:

```text
cms.example.com
        ↓
target.example.com
```

is considered:

```text
Same-Site
```

even though it is:

```text
Cross-Origin
```

---

# The Security Assumption

SameSite assumes:

```text
All Subdomains Are Trusted
```

This assumption is often incorrect.

---

# Vulnerable Sibling Domains

A sibling domain is another subdomain within the same site.

Example:

```text
target.example.com
cms.example.com
blog.example.com
staging.example.com
```

---

# Attack Scenario

Suppose:

```text
target.example.com
```

is secure.

But:

```text
cms.example.com
```

contains:

```text
Reflected XSS
```

An attacker can execute JavaScript from:

```text
cms.example.com
```

and interact with:

```text
target.example.com
```

as a same-site request.

---

# SameSite Strict Bypass

Normally:

```text
attacker.com
        ↓
target.com
```

Cookies blocked.

---

But:

```text
cms.target.com
        ↓
target.com
```

Cookies sent.

---

# Cross-Site WebSocket Hijacking (CSWSH)

CSWSH is essentially:

```text
CSRF For WebSockets
```

The attacker forces the victim's browser to establish a WebSocket connection using the victim's authenticated session.

---

# Why WebSockets Are Interesting

WebSocket connections begin as HTTP requests.

Example:

```http
GET /chat HTTP/1.1
Upgrade: websocket
```

If this handshake lacks CSRF protection:

```text
CSWSH Possible
```

---

# Why Plain CSWSH May Fail

Suppose attacker hosts:

```text
attacker.net
```

and executes:

```javascript
new WebSocket(
'wss://target.example.com/chat'
);
```

Browser behavior:

```text
Cross-Site Request
        ↓
SameSite=Strict
        ↓
Session Cookie Blocked
```

Attack fails.

---

# Using a Vulnerable Sibling Domain

Suppose XSS exists on:

```text
cms.example.com
```

Now JavaScript executes from:

```text
cms.example.com
```

and opens:

```javascript
new WebSocket(
'wss://target.example.com/chat'
);
```

Browser sees:

```text
Same-Site Request
```

Therefore:

```text
Session Cookie Included
```

Attack succeeds.

---

# Typical Attack Chain

```text
Attacker Website
        ↓
Redirect To Vulnerable Sibling Domain
        ↓
XSS Executes
        ↓
Open WebSocket To Target
        ↓
Session Cookie Sent
        ↓
Victim Data Accessed
```

---

# Common Sources Of Sibling Domains

## CORS Headers

Example:

```http
Access-Control-Allow-Origin:
https://cms.example.com
```

may reveal hidden subdomains.

---

## Certificate Transparency Logs

Useful resources:

```text
crt.sh
```

---

## Subdomain Enumeration

Tools:

```text
subfinder
amass
assetfinder
```

---

# Real-World Testing Checklist

```text
[ ] Enumerate subdomains
[ ] Identify sibling domains
[ ] Search for XSS
[ ] Search for redirect gadgets
[ ] Search for CSWSH
[ ] Test SameSite assumptions
```

---

# Related Lab

- `lab09-samesite-strict-bypass-via-sibling-domain.md`

---

# Related Payloads

- `cswsh-methodology.md`
- `samesite-bypass-techniques.md`

---

# Key Takeaways

- SameSite uses Site, not Origin.
- A vulnerable sibling domain can completely undermine SameSite protections.
- XSS on any trusted subdomain may compromise the entire site.
- CSWSH is effectively CSRF targeting WebSocket handshakes.

> [!WARNING]
> SameSite=Strict is not a complete CSRF defense if an attacker can execute JavaScript on any sibling domain within the same site.