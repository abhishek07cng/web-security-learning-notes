# How To Prevent XSS

## Defense In Depth

Preventing XSS requires:

```text
Output Encoding
+
Input Validation
+
CSP
```

---

# 1. Encode Output

Always encode according to context.

---

## HTML Context

Convert:

```html
<
>
```

into:

```html
&lt;
&gt;
```

---

## JavaScript Context

Convert:

```javascript
<
>
```

into:

```javascript
\u003c
\u003e
```

---

# 2. Validate Input

Prefer:

```text
Whitelist
```

over:

```text
Blacklist
```

---

Good:

```text
Allow Only HTTPS URLs
```

---

Bad:

```text
Block javascript:
```

---

# 3. Secure Frameworks

Use:

```text
Twig
Jinja
React
```

with automatic escaping.

---

# 4. Deploy CSP

Example:

```http
default-src 'self';
script-src 'self';
object-src 'none';
frame-src 'none';
base-uri 'none';
```

---

# 5. Use HttpOnly Cookies

Protect:

```javascript
document.cookie
```

from theft.

---

# 6. Sanitize HTML Carefully

Prefer:

```text
DOMPurify
```

over custom filters.

---

# XSS Prevention Checklist

```text
Output Encoding
Input Validation
Whitelist Approach
Secure Frameworks
HttpOnly
CSP
Regular Security Testing
```

---

# Key Takeaways

- Output encoding is the most important defense.
- CSP is the last line of defense.
- Defense should be layered.