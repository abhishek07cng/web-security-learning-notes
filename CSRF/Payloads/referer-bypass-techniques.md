# Referer Bypass Techniques

## Overview

Many applications use Referer validation for CSRF protection.

Weak implementations are often bypassable.

---

# Technique 1 - Missing Referer

Application Logic:

```python
if referer:
    validate()
else:
    allow()
```

---

## Detection

```http
Referer:
https://evil.com
```

Rejected.

---

Remove Referer entirely.

```http
(No Referer Header)
```

Accepted.

---

## Exploit

```html
<meta name="referrer"
content="no-referrer">
```

---

# Technique 2 - Query String Injection

Weak Validation:

```text
Contains target.com
```

---

Payload:

```http
Referer:
https://evil.com?target.com
```

---

# Technique 3 - Subdomain Injection

Payload:

```http
Referer:
https://target.com.evil.com
```

---

# Technique 4 - Path Injection

Payload:

```http
Referer:
https://evil.com/target.com
```

---

# Technique 5 - Fragment Injection

Payload:

```http
Referer:
https://evil.com/#target.com
```

---

# Technique 6 - unsafe-url

Browsers may remove:

```text
Query Strings
```

from Referer.

---

Force full URL:

```html
<meta name="referrer"
content="unsafe-url">
```

---

# Testing Workflow

```text
Valid Referer
↓
Invalid Referer
↓
Missing Referer
↓
Query Injection
↓
Subdomain Injection
↓
Path Injection
```

---

# Related Labs

- lab11-referer-validation-depends-on-header-being-present.md
- lab12-csrf-with-broken-referer-validation.md

---

# Key Takeaways

- Referer validation is often implemented incorrectly.
- String matching is not hostname validation.
- Browser behavior affects exploit reliability.