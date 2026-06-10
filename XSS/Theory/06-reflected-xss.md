# Reflected Cross-Site Scripting (Reflected XSS)

## Overview

Reflected XSS occurs when an application receives user-controlled data in an HTTP request and immediately returns that data in the HTTP response without proper sanitization or encoding.

The malicious payload is not stored anywhere on the server.

Instead, it is reflected directly back to the user's browser.

---

# Definition

According to PortSwigger:

> Reflected XSS arises when an application receives data in an HTTP request and includes that data within the immediate response in an unsafe way.

---

# How Reflected XSS Works

## Normal Flow

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

## Vulnerable Flow

```text
Attacker Input
        ↓
Application
        ↓
Payload Reflected
        ↓
Browser Executes Script
```

---

# Example

Request:

```http
GET /search?term=gift
```

Response:

```html
<p>You searched for: gift</p>
```

---

Attacker Payload:

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

Browser executes:

```javascript
alert(1)
```

---

# Key Characteristic

The payload:

```text
Comes From Current HTTP Request
```

and

```text
Is Not Stored
```

---

# Common Sources

```text
Search Parameters
Login Errors
Contact Forms
URL Parameters
Headers
```

---

# Attack Flow

```text
Attacker Creates URL
        ↓
Victim Clicks Link
        ↓
Payload Reflected
        ↓
Browser Executes Script
```

---

# Related Lab

- lab01-reflected-xss-html-context.md

---

# Related Theory

- 07-impact-of-reflected-xss.md
- 08-reflected-xss-contexts.md

---

# Key Takeaways

- Reflected XSS is the most common XSS type.
- Payload comes from the request.
- Victim usually needs to visit an attacker-controlled URL.
- Payload is not stored on the server.