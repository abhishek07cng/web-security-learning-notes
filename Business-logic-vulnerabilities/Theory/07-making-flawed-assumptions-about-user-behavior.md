# Making Flawed Assumptions About User Behavior

## Overview

Applications often assume users follow the intended workflow.

Attackers do not.

---

# Example

Normal Flow:

```text
Add Item
        ↓
Checkout
        ↓
Payment
        ↓
Confirmation
```

---

Attacker:

```text
Skip Payment
        ↓
Reach Confirmation
```

---

# Root Cause

Developers assume:

```text
UI Controls User Actions
```

but attackers use:

```text
Burp Repeater
```

---

# Related Labs

```text
Lab10
Lab11
```

---

# Key Takeaways

Never trust the sequence enforced by the interface.