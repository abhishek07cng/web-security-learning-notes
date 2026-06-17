# What Is Access Control?

## Overview

Access Control determines:

```text
Who
        ↓
Can Access
        ↓
What Resources
        ↓
And Perform Which Actions
```

within an application.

---

# Relationship With Authentication

Access control depends on:

```text
Authentication
        ↓
Session Management
        ↓
Access Control
```

---

## Authentication

Answers:

```text
Who Are You?
```

Example:

```text
Username + Password
```

---

## Session Management

Answers:

```text
Which Requests Belong To You?
```

Example:

```http
Cookie: session=abc123
```

---

## Access Control

Answers:

```text
What Are You Allowed To Do?
```

Examples:

```text
View Profile
Delete User
Access Admin Panel
Change Roles
```

---

# Why Access Control Matters

Without proper access control:

```text
Users Access Other Accounts
Users Become Admins
Sensitive Data Exposed
```

---

# Common Consequences

```text
Privilege Escalation
Account Takeover
Data Leakage
Unauthorized Actions
```

---

# Example

Normal User:

```text
Can View Own Account
```

---

Admin User:

```text
Can Manage Users
Can Delete Accounts
Can Change Roles
```

---

# Broken Access Control

Occurs when:

```text
Application Fails To Enforce
Authorization Rules
```

---

# Key Takeaways

- Authentication ≠ Authorization.
- Access control decides what actions are permitted.
- Broken access control is often critical.