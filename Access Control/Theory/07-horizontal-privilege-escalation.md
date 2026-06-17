# Horizontal Privilege Escalation

## Overview

Horizontal Privilege Escalation occurs when a user accesses another user's resources.

---

# Example

User:

```text
wiener
```

---

Own Account:

```text
/my-account?id=wiener
```

---

Modified Request:

```text
/my-account?id=carlos
```

---

# Vulnerability

Application validates:

```text
User Logged In
```

but fails to validate:

```text
Ownership
```

---

# Typical Targets

```text
Profiles
Invoices
Orders
Messages
Documents
API Keys
```

---

# Common Indicators

## Numeric IDs

```text
?id=1001
```

↓

```text
?id=1002
```

---

## GUIDs

```text
?id=a23f8e91
```

---

## Usernames

```text
?user=wiener
```

↓

```text
?user=carlos
```

---

# Real Impact

```text
Data Disclosure
Account Manipulation
Sensitive Information Exposure
```

---

# Bug Bounty Mental Model

Ask:

```text
Can I Replace
My Identifier
With Another User's?
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

- Authentication is not enough.
- Ownership validation is critical.
- Most IDOR vulnerabilities are horizontal escalation.