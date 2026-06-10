# What is Cross-Site Scripting (XSS)?

## Overview

Cross-Site Scripting (XSS) is a web security vulnerability that allows an attacker to inject malicious JavaScript into a web application and execute it in another user's browser.

XSS breaks the trust between a website and its users.

---

# Definition

According to PortSwigger:

> Cross-Site Scripting (XSS) is a web security vulnerability that allows an attacker to compromise the interactions users have with a vulnerable application.

---

# Why XSS Is Dangerous

When JavaScript executes inside a victim's browser, it runs with the permissions of the vulnerable website.

As a result, an attacker may:

- Act as the victim user
- Access sensitive information
- Modify application data
- Perform actions on behalf of the victim
- Capture credentials
- Deliver further attacks

---

# How XSS Breaks Browser Security

Modern browsers use:

```text
Same Origin Policy (SOP)
```

to isolate websites from one another.

Example:

```text
google.com
cannot access
facebook.com
```

directly.

---

With XSS:

```text
Attacker Injects Script
        ↓
Script Executes On Victim Site
        ↓
Browser Trusts Script
        ↓
Same Origin Policy Bypassed
```

---

# Types of XSS

## Reflected XSS

Payload comes from:

```text
Current HTTP Request
```

Example:

```text
/search?q=<script>alert(1)</script>
```

---

## Stored XSS

Payload comes from:

```text
Database
```

Example:

```text
Comment Section
Profile Bio
Forum Post
```

---

## DOM-Based XSS

Payload is processed by:

```text
Client-Side JavaScript
```

instead of the server.

---

# Real World Targets

Common locations:

```text
Search Bars
Comment Sections
Chat Applications
Support Tickets
Profile Pages
Admin Panels
```

---

# Attack Flow

```text
Attacker Supplies Payload
        ↓
Application Processes Input
        ↓
Payload Returned To User
        ↓
Browser Executes JavaScript
        ↓
Attacker Gains Control
```

---

# Related Theory

- 02-how-does-xss-work.md
- 03-impact-of-an-xss-attack.md

---

# Key Takeaways

- XSS allows execution of attacker-controlled JavaScript.
- XSS targets application users.
- XSS is one of the most common web vulnerabilities.
- XSS often leads to account compromise.