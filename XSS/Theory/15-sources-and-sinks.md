# Sources and Sinks

## Overview

DOM XSS revolves around two concepts:

```text
Source
    ↓
Sink
```

Understanding these is essential for finding DOM vulnerabilities.

---

# What Is A Source?

A source is a location where attacker-controlled data enters the application.

---

## Common Sources

### location.search

Contains:

```text
Everything after ?
```

Example:

```text
?q=test
```

---

### location.hash

Contains:

```text
Everything after #
```

Example:

```text
#test
```

---

### location.pathname

Contains:

```text
URL Path
```

---

### document.referrer

Contains:

```text
Previous Page
```

---

### document.cookie

Contains:

```text
Browser Cookies
```

---

### window.name

Contains:

```text
Persistent Window Data
```

---

### postMessage

Contains:

```text
Messages From Other Windows
```

---

# What Is A Sink?

A sink is a location where data becomes dangerous.

---

# HTML Sinks

```javascript
innerHTML
outerHTML
document.write()
```

---

# JavaScript Execution Sinks

```javascript
eval()
setTimeout()
setInterval()
Function()
```

---

# URL Sinks

```javascript
location.href
location.assign()
```

---

# jQuery Sinks

```javascript
$()
.html()
.attr()
```

---

# Attack Flow

```text
Attacker Input
        ↓
Source
        ↓
JavaScript
        ↓
Sink
        ↓
Execution
```

---

# Example

```javascript
document.write(
location.search
);
```

---

URL:

```text
?q=<script>alert(1)</script>
```

---

Flow:

```text
location.search
        ↓
document.write()
        ↓
Execution
```

---

# Related Theory

- 16-testing-dom-xss.md

---

# Key Takeaways

- Sources introduce attacker data.
- Sinks create exploitation opportunities.
- DOM XSS always requires a source and a sink.