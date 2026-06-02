# SameSite Observations

## Purpose

Revision Notes

Contains practical observations encountered during SameSite testing.

---

# Observation 1

Many applications rely solely on:

```text
SameSite
```

instead of implementing CSRF tokens.

This is dangerous.

---

# Observation 2

Chrome automatically applies:

```text
SameSite=Lax
```

when developers omit the attribute.

---

# Observation 3

Lax still allows:

```text
GET Navigation
```

with cookies.

---

# Observation 4

Method override parameters often enable:

```text
Lax Bypass
```

Examples:

```http
_method=POST
```

---

# Observation 5

Client-side redirects are significantly more dangerous than server-side redirects.

---

# Observation 6

A redirect gadget plus path traversal often becomes:

```text
SameSite Strict Bypass
```

---

# Observation 7

Same-Site does NOT mean Same-Origin.

This distinction frequently appears in advanced CSRF labs.

---

# Observation 8

Applications often trust:

```text
Subdomains
```

too much.

Compromised sibling domains may enable attacks.

---

# Observation 9

Most successful SameSite bypasses involve:

```text
Browser Behavior Abuse
```

rather than direct cookie attacks.

---

# Common Testing Checklist

- Check SameSite attribute
- Check GET endpoints
- Check method override
- Check redirect gadgets
- Check client-side navigation
- Check sibling domains

---

# Key Takeaway

SameSite is a valuable security layer, but understanding browser behavior is essential for identifying bypass opportunities.