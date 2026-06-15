# Protecting Against Clickjacking Using CSP

## Overview

Clickjacking occurs when a victim interacts with a hidden frame.

---

# CSP Protection

Use:

```http
frame-ancestors
```

directive.

---

# Block All Framing

```http
frame-ancestors 'none'
```

---

# Allow Same Origin Only

```http
frame-ancestors 'self'
```

---

# Allow Specific Domains

```http
frame-ancestors
'self'
https://example.com
```

---

# Why Better Than X-Frame-Options

Supports:

```text
Multiple Domains
Wildcards
Frame Hierarchy Validation
```

---

# Recommended Configuration

```http
frame-ancestors 'none'
```

for highly sensitive pages.

---

# Key Takeaways

- CSP provides modern clickjacking protection.
- More flexible than X-Frame-Options.