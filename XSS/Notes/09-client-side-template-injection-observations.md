# Client-Side Template Injection Observations

## Observation 1

CSTI often appears before traditional XSS.

---

## Observation 2

Detection is extremely easy:

```html
{{7*7}}
```

---

## Observation 3

Many developers assume:

```text
HTML Encoding
```

prevents execution.

It does not stop template evaluation.

---

## Observation 4

Frameworks create:

```text
New Attack Surface
```

beyond normal HTML.

---

## Observation 5

AngularJS expressions can become:

```text
Sandbox Escape
        ↓
XSS
```

---

## Observation 6

orderBy repeatedly appears as an execution sink.

---

## Observation 7

CSP reduces risk but does not eliminate exploitation possibilities.

---

# Personal Revision Formula

```text
Template Found
        ↓
{{7*7}}
        ↓
Framework Detected
        ↓
Sandbox Escape
        ↓
Execution
```