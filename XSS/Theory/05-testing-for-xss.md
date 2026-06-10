# Testing For XSS

## Overview

Finding XSS is a systematic process.

The goal is to determine:

```text
Can attacker-controlled input
become executable JavaScript?
```

---

# Step 1 - Find Entry Points

Potential sources:

```text
URL Parameters
POST Data
Headers
Cookies
Profile Fields
Comments
Search Boxes
```

---

# Step 2 - Submit Probe Value

Example:

```text
a3f8kz92
```

Purpose:

```text
Track Reflection
```

---

# Step 3 - Search Response

Questions:

```text
Is Input Reflected?
Where Is It Reflected?
```

---

# Step 4 - Identify Context

Possible contexts:

| Context | Example |
|----------|----------|
| HTML | `<p>test</p>` |
| Attribute | `<input value="test">` |
| JavaScript | `var x="test"` |

---

# Step 5 - Test Payload

## HTML Context

```html
<script>alert(1)</script>
```

---

## Attribute Context

```html
" onmouseover="alert(1)
```

---

## JavaScript Context

```javascript
";alert(1);//
```

---

# Step 6 - Verify Execution

Test:

```javascript
alert(document.domain)
```

or

```javascript
print()
```

inside browser.

---

# XSS Testing Workflow

```text
Find Entry Point
        ↓
Inject Probe Value
        ↓
Locate Reflection
        ↓
Identify Context
        ↓
Craft Payload
        ↓
Test In Repeater
        ↓
Verify In Browser
```

---

# Personal Revision Note

Always ask:

```text
Where Does My Input End Up?
```

This question usually determines:

```text
Payload Choice
Bypass Strategy
Exploitation Method
```

---

# Related Theory

- 06-reflected-xss.md
- 09-testing-for-reflected-xss.md
- 13-testing-for-stored-xss.md

---

# Key Takeaways

- Context determines payload.
- Reflection alone is not XSS.
- Browser confirmation is essential.
- Burp Repeater is your best friend during XSS testing.