# Users Won't Always Supply Mandatory Input

## Overview

Applications assume required parameters always exist.

Attackers can remove parameters.

---

# Example

Normal Request

```text
username
password
csrf
```

---

Modified Request

```text
username
password
```

---

# Result

Unexpected states may occur.

---

# Common Targets

```text
Coupons
Discount Codes
Security Tokens
Email Fields
```

---

# Attack Flow

```text
Parameter Removed
        ↓
Unexpected Behavior
```

---

# Related Labs

```text
Lab06
Lab08
```

---

# Key Takeaways

Missing input should be handled safely.