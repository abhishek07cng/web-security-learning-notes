# Email Address Parser Discrepancies

## Overview

Different components may parse email addresses differently.

---

# Example

Validation Layer:

```text
Blocks External Email
```

---

Backend Parser:

```text
Accepts Modified Format
```

---

# Result

Security Restrictions Bypassed.

---

# Attack Flow

```text
Different Parsing Rules
        ↓
Validation Bypass
        ↓
Unexpected Access
```

---

# Related Lab

```text
Lab15
```

---

# Key Takeaways

Never assume different systems interpret input identically.