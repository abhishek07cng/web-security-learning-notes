# Users Won't Always Follow Intended Sequence

## Overview

Applications expect users to follow:

```text
Step 1
Step 2
Step 3
```

Attackers skip steps.

---

# Example

Password Reset Flow

```text
Request Token
        ↓
Verify Token
        ↓
Reset Password
```

---

Attacker:

```text
Skip Verification
        ↓
Reset Password
```

---

# Attack Flow

```text
Step Skipped
        ↓
State Broken
        ↓
Logic Flaw
```

---

# Related Labs

```text
Lab10
Lab11
```

---

# Key Takeaways

Every step must validate state independently.