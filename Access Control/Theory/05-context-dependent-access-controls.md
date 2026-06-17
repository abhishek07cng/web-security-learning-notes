# Context-Dependent Access Controls

## Overview

Context-Dependent Access Controls restrict actions based on:

```text
Application State
```

rather than user role.

---

# Example Workflow

```text
Step 1
Add Item To Cart
        ↓
Step 2
Checkout
        ↓
Step 3
Payment
```

---

After Payment:

```text
Cart Modification
Should Be Blocked
```

---

# Why This Exists

Applications often require:

```text
Correct Order Of Operations
```

---

# Vulnerability

Occurs when:

```text
User Skips Steps
```

or

```text
Directly Accesses Final Action
```

---

# Example

Admin Role Change Process:

```text
Step 1
Choose User
        ↓
Step 2
Confirm Change
        ↓
Step 3
Apply Change
```

---

If Step 3 lacks checks:

```text
Attacker Directly Sends
Final Request
```

---

# Common Indicators

```text
Multi-Step Forms
Checkout Workflows
Role Changes
Password Reset Processes
Approval Flows
```

---

# Related Labs

```text
Lab12
```

---

# Key Takeaways

- Every step must validate authorization.
- Never assume previous steps were completed.