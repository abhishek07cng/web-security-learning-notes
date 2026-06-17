# Vertical Privilege Escalation

## Overview

Vertical Privilege Escalation occurs when a lower-privileged user gains access to functionality intended for higher-privileged users.

---

# Access Control Hierarchy

```text
Administrator
        ↑
Manager
        ↑
Employee
        ↑
User
```

---

# Vulnerability

Occurs when:

```text
User
        ↓
Accesses Admin Functionality
```

---

# Common Examples

## Admin Panels

```text
/admin
```

---

## User Management

```text
Delete Users
Create Users
Modify Roles
```

---

## Sensitive Reports

```text
Financial Data
Audit Logs
```

---

# Typical Causes

## Hidden URLs

```text
/admin
```

not linked but still accessible.

---

## Client-Side Checks

```javascript
if(admin)
```

---

## Cookie-Based Roles

```http
admin=false
```

changed to:

```http
admin=true
```

---

## Parameter-Based Roles

```json
{
"roleid":1
}
```

changed to:

```json
{
"roleid":2
}
```

---

# Bug Bounty Mental Model

Ask:

```text
Can A User
Reach Admin Functionality
Directly?
```

---

# Related Labs

```text
Lab01
Lab02
Lab03
Lab04
Lab05
Lab06
```

---

# Key Takeaways

- Authorization must be enforced server-side.
- Hidden functionality is not security.
- Client-side role checks are ineffective.