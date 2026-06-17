# Horizontal Access Controls

## Overview

Horizontal Access Controls prevent users from accessing other users' resources.

---

# Example

User:

```text
wiener
```

---

Can Access:

```text
/my-account?id=wiener
```

---

Should NOT Access:

```text
/my-account?id=carlos
```

---

# Horizontal Privilege Escalation

Occurs when:

```text
User A
        ↓
Accesses
        ↓
User B Data
```

---

# Typical Targets

```text
Account Pages
Orders
Invoices
Messages
Documents
API Keys
```

---

# Common Vulnerability

## IDOR

Example:

```text
?id=123
```

changed to:

```text
?id=124
```

---

# GUID-Based IDs

Example:

```text
?id=ea6f9f34-c321
```

---

May still be exploitable if:

```text
GUID Leaked Elsewhere
```

---

# Related Labs

```text
Lab07
Lab08
Lab09
```

---

# Key Takeaways

- Same role ≠ Same permissions.
- Ownership checks must be enforced.