# How Does SameSite Work?

## Overview

SameSite controls whether browsers send cookies during cross-site requests.

---

# Setting SameSite

Example:

```http
Set-Cookie:
session=abc123;
SameSite=Strict
```

---

# Available Modes

```text
Strict
Lax
None
```

---

# SameSite=Strict

Browser behavior:

```text
Cross-Site Request
        ↓
Cookie Blocked
```

Most secure mode.

---

# SameSite=Lax

Cookies sent only if:

1. GET request
2. Top-level navigation

---

## Example

```html
<a href="https://target.com">
```

Cookie sent.

---

## Not Allowed

```html
<form method="POST">
```

Cookie blocked.

---

# SameSite=None

Disables SameSite restrictions.

Browser always sends cookies.

---

# Important Requirement

```http
SameSite=None
```

must be paired with:

```http
Secure
```

or browsers reject it. :contentReference[oaicite:2]{index=2}

---

# Chrome Default

```text
No SameSite Attribute
        ↓
SameSite=Lax
```

---

# Security Comparison

| Mode | Cross-Site Cookies |
|--------|--------|
| Strict | Never |
| Lax | GET Navigation Only |
| None | Always |

---

# Key Takeaways

- Strict is strongest.
- Lax is browser default.
- None disables protection.