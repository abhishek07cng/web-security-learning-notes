# Failing To Handle Unconventional Input

## Overview

Developers often assume users provide reasonable input.

Attackers supply:

```text
Negative Numbers
Huge Values
Zero
Unexpected Formats
```

---

# Example

Quantity:

```text
-1
```

may produce:

```text
Negative Price
```

---

# Integer Problems

```text
Overflow
Underflow
Rounding Errors
```

can create unexpected behavior.

---

# Attack Flow

```text
Unexpected Input
        ↓
Unexpected State
        ↓
Broken Logic
```

---

# Related Labs

```text
Lab03
Lab04
Lab12
Lab13
```

---

# Key Takeaways

Attackers intentionally violate assumptions.