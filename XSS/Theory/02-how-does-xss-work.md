# How Does XSS Work?

## Overview

XSS works when an application takes attacker-controlled input and returns it to a user's browser without proper sanitization or encoding.

The browser interprets the malicious input as executable code.

---

# Normal Flow

```text
User Input
        ↓
Application
        ↓
Response
        ↓
Browser Displays Data
```

---

# Vulnerable Flow

```text
Attacker Input
        ↓
Application
        ↓
Malicious Script Returned
        ↓
Browser Executes Script
```

---

# Example

User searches:

```text
gift
```

Request:

```http
GET /search?term=gift
```

Response:

```html
<p>You searched for: gift</p>
```

---

# Malicious Input

Attacker submits:

```html
<script>alert(1)</script>
```

Request:

```http
GET /search?term=<script>alert(1)</script>
```

Response:

```html
<p>You searched for:
<script>alert(1)</script>
</p>
```

---

# Browser Interpretation

Browser sees:

```html
<script>
alert(1)
</script>
```

and executes it.

---

# Why Browser Executes It

The browser cannot distinguish between:

```text
Developer Code
```

and

```text
Attacker-Supplied Code
```

when both appear inside the page source.

---

# Attack Flow

```text
Attacker Creates Payload
        ↓
Application Reflects Payload
        ↓
Victim Loads Page
        ↓
Browser Executes Script
        ↓
Attacker Achieves Goal
```

---

# Related Theory

- 01-what-is-xss.md
- 03-impact-of-an-xss-attack.md

---

# Key Takeaways

- XSS occurs when input becomes executable code.
- Browsers trust code returned by websites.
- Proper output encoding prevents most XSS vulnerabilities.