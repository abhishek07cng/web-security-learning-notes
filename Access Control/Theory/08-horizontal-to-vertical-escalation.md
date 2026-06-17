# Horizontal To Vertical Privilege Escalation

## Overview

This occurs when:

```text
Horizontal Access
        ↓
Leads To
        ↓
Admin Access
```

---

# Attack Flow

```text
User A
        ↓
Access User B Data
        ↓
Find Admin Information
        ↓
Become Administrator
```

---

# Example

User:

```text
wiener
```

---

Accesses:

```text
administrator
```

profile.

---

Obtains:

```text
Admin Password
Admin API Key
Admin Session
```

---

# Why Dangerous?

Because:

```text
Horizontal
        ↓
Becomes
        ↓
Vertical
```

---

# Common Scenarios

## Password Disclosure

```text
View Admin Password
```

---

## API Keys

```text
View Admin API Token
```

---

## Session Disclosure

```text
Steal Admin Session
```

---

# Bug Bounty Mental Model

Always ask:

```text
What Valuable Data
Exists In Other Accounts?
```

---

# Related Labs

```text
Lab10
```

---

# Key Takeaways

- Not all horizontal vulnerabilities stop at data leakage.
- Always check whether exposed data enables privilege escalation.