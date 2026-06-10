# Testing For Reflected XSS

## Overview

Testing reflected XSS is a structured process.

The goal is to identify:

```text
User Input
        ↓
Reflection
        ↓
Executable JavaScript
```

---

# Step 1 - Find Entry Points

Check:

```text
URL Parameters
POST Data
Headers
Cookies
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

# Step 3 - Locate Reflection

Search response for:

```text
a3f8kz92
```

---

# Step 4 - Determine Context

Possible contexts:

```text
HTML
Attribute
JavaScript
URL
```

---

# Step 5 - Select Payload

## HTML

```html
<script>alert(1)</script>
```

---

## Attribute

```html
" onmouseover="alert(1)
```

---

## JavaScript

```javascript
";alert(1);//
```

---

# Step 6 - Test In Repeater

Observe:

```text
Filtering
Encoding
Reflection
```

---

# Step 7 - Verify In Browser

Use:

```javascript
alert(document.domain)
```

or

```javascript
print()
```

---

# Testing Workflow

```text
Find Entry Point
        ↓
Inject Probe
        ↓
Find Reflection
        ↓
Determine Context
        ↓
Craft Payload
        ↓
Verify Execution
```

---

# Practical Methodology

```text
Reflection
≠ Vulnerability

Execution
= Vulnerability
```

---

# Related Lab

- lab01-reflected-xss-html-context.md

---

# Key Takeaways

- Reflection is only the first step.
- Context determines payload.
- Browser confirmation is essential.