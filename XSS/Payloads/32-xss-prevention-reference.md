# XSS Prevention Reference

## Rule 1

Encode Output.

---

### HTML Context

```html
<
>
```

↓

```html
&lt;
&gt;
```

---

### Attribute Context

Encode:

```html
"
'
<
>
```

---

### JavaScript Context

Encode:

```javascript
\u003c
\u003e
```

---

# Rule 2

Use Whitelisting.

---

Good:

```text
Allow HTTPS URLs
```

---

Bad:

```text
Block javascript:
```

---

# Rule 3

Use Secure Frameworks.

Examples:

```text
React
Twig
Jinja
```

---

# Rule 4

Deploy CSP.

---

# Rule 5

Use HttpOnly.

---

# Rule 6

Use DOMPurify.

---

# Defense In Depth

```text
Input Validation
        +
Output Encoding
        +
CSP
        +
HttpOnly
```

---

# Personal Revision Note

```text
Output Encoding
```

is the most important XSS defense.