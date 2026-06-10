# Stored Cross-Site Scripting (Stored XSS)

## Overview

Stored XSS (also known as Persistent XSS or Second-Order XSS) occurs when attacker-controlled input is stored by the application and later displayed to users without proper sanitization or encoding.

Unlike Reflected XSS, the payload remains inside the application until it is removed.

---

# Definition

According to PortSwigger:

> Stored XSS arises when an application receives data from an untrusted source and includes that data within later HTTP responses in an unsafe way.

---

# Why It Is Called Stored XSS

The payload is:

```text
Submitted
        ↓
Stored
        ↓
Displayed Later
        ↓
Executed
```

instead of:

```text
Submitted
        ↓
Immediately Reflected
        ↓
Executed
```

---

# How Stored XSS Works

## Legitimate User

User submits:

```text
This article was helpful.
```

Application stores:

```text
This article was helpful.
```

Database:

```text
Comment Saved
```

---

## Attacker

Attacker submits:

```html
<script>alert(1)</script>
```

Application stores:

```html
<script>alert(1)</script>
```

Database:

```text
Malicious Payload Saved
```

---

## Victim

Victim visits page.

Response:

```html
<p>
<script>alert(1)</script>
</p>
```

Browser executes:

```javascript
alert(1)
```

---

# Attack Flow

```text
Attacker Submits Payload
        ↓
Application Stores Payload
        ↓
Victim Loads Page
        ↓
Payload Returned
        ↓
JavaScript Executes
```

---

# Common Entry Points

```text
Comment Systems
Forums
Chat Applications
Profile Fields
Reviews
Support Tickets
Admin Logs
```

---

# Real World Examples

## Blog Comment

```html
<script>alert(1)</script>
```

posted as comment.

---

## User Profile

```html
<img src=x onerror=alert(1)>
```

saved in profile bio.

---

## Chat Application

```html
<script>alert(1)</script>
```

sent to all users.

---

# Why Stored XSS Is Dangerous

The payload:

```text
Lives Inside Application
```

and automatically attacks:

```text
Future Visitors
```

---

# Related Theory

- 12-impact-of-stored-xss.md
- 13-testing-for-stored-xss.md

---

# Related Lab

- lab02-stored-xss-html-context.md

---

# Key Takeaways

- Stored XSS persists inside the application.
- Victims do not need to click attacker links.
- Every visitor may become a victim.
- Stored XSS is generally more severe than Reflected XSS.