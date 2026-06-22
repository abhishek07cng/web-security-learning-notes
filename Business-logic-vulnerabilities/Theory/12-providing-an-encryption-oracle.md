# Providing An Encryption Oracle

## Overview

Applications sometimes expose encrypted values and reveal information about them.

This behavior creates:

```text
Encryption Oracle
```

---

# Problem

Attackers repeatedly manipulate encrypted values and observe responses.

---

# Attack Flow

```text
Modify Ciphertext
        ↓
Observe Response
        ↓
Learn Information
        ↓
Bypass Security
```

---

# Related Lab

```text
Lab14
```

---

# Key Takeaways

Error messages and different responses can leak sensitive information.