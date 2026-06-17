# Access Control Security Models

## Overview

Access controls are commonly divided into three categories:

```text
Vertical
Horizontal
Context-Dependent
```

---

# Access Control Model

```text
User
        ↓
Authentication
        ↓
Authorization Check
        ↓
Resource Access
```

---

# 1. Vertical Access Control

Restricts functionality based on:

```text
User Role
```

---

Example:

```text
Admin → Delete Users

User → Cannot Delete Users
```

---

# 2. Horizontal Access Control

Restricts access between users of the same role.

---

Example:

```text
User A
        ↓
Can View Own Profile

User A
        ↓
Cannot View User B Profile
```

---

# 3. Context-Dependent Access Control

Restricts actions based on:

```text
Application State
```

---

Example:

```text
Shopping Cart
        ↓
Payment Completed
        ↓
Cart Cannot Be Modified
```

---

# Why These Models Matter

Most access control bugs occur because:

```text
One Of These Checks
Is Missing
```

---

# Key Takeaways

- Vertical = Role-Based Restrictions.
- Horizontal = Ownership Restrictions.
- Context-Dependent = Workflow Restrictions.