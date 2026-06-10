# XSS Proof of Concept (PoC)

## Overview

Before proving impact, security researchers first confirm that JavaScript execution is possible.

This is called:

```text
Proof of Concept (PoC)
```

---

# Traditional Payload

```html
<script>alert(1)</script>
```

Purpose:

```text
Verify JavaScript Execution
```

---

# Why alert()?

Advantages:

- Simple
- Safe
- Easy to notice
- Short payload

---

# Chrome Limitation

Modern Chrome restricts:

```text
Cross-Origin Iframes
```

from calling:

```javascript
alert()
```

in some situations.

---

# Alternative Payload

```javascript
print()
```

PortSwigger recommends:

```javascript
print()
```

for affected labs.

---

# Common PoC Payloads

## Basic Alert

```html
<script>alert(1)</script>
```

---

## Print

```html
<script>print()</script>
```

---

## Domain Verification

```javascript
alert(document.domain)
```

---

## HTML Event Handler

```html
<img src=x onerror=alert(1)>
```

---

# Important Note

PoC payloads are used only to:

```text
Confirm Vulnerability
```

not demonstrate real impact.

---

# Related Labs

- Lab01
- Lab02

---

# Key Takeaways

- alert() remains the most common XSS PoC.
- print() may be needed in Chrome-based labs.
- Successful JavaScript execution confirms XSS.