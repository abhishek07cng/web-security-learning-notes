# What is DOM-Based XSS?

## Overview

DOM-Based Cross-Site Scripting (DOM XSS) is a type of XSS vulnerability where the attack is executed entirely within the victim's browser.

Unlike Reflected XSS and Stored XSS, the payload never passes through the server.

The browser's JavaScript reads attacker-controlled data from a source and writes it into a dangerous sink.

---

# Core Concept

```text
Source
    ↓
JavaScript Processing
    ↓
Dangerous Sink
    ↓
JavaScript Execution
```

---

# Difference From Traditional XSS

## Reflected XSS

```text
Request
    ↓
Server
    ↓
Response
    ↓
Browser
```

---

## Stored XSS

```text
Request
    ↓
Database
    ↓
Response
    ↓
Browser
```

---

## DOM XSS

```text
Request
    ↓
Browser JavaScript
    ↓
DOM Manipulation
    ↓
Execution
```

No server-side processing is required.

---

# Example

```javascript
document.getElementById(
"output"
).innerHTML =
location.hash;
```

---

URL:

```text
https://site.com/#<img src=1 onerror=alert(1)>
```

---

Flow:

```text
location.hash
        ↓
innerHTML
        ↓
HTML Parsing
        ↓
alert(1)
```

---

# Why DOM XSS Is Difficult

The payload may never appear:

```text
In Burp Response
In View Source
```

because execution occurs after JavaScript modifies the page.

---

# Key Difference

For DOM XSS:

```text
DevTools Elements
```

is often more useful than:

```text
View Source
```

---

# Related Theory

- 15-sources-and-sinks.md
- 16-testing-dom-xss.md

---

# Key Takeaways

- DOM XSS is entirely client-side.
- The server may never see the payload.
- Source → Sink is the most important concept.
- DevTools is critical during testing.