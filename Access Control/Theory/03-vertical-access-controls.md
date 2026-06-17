# Vertical Access Controls

## Overview

Vertical Access Controls restrict functionality based on user privileges.

---

# Example Roles

```text
Administrator
Manager
Employee
Customer
```

---

# Example Permissions

| Role | Permissions |
|--------|--------|
| Admin | Manage Users |
| Manager | Manage Team |
| Employee | View Own Data |
| Customer | View Own Account |

---

# Example

Admin Panel:

```text
/admin
```

---

Expected:

```text
Admin → Allowed

User → Denied
```

---

# Broken Vertical Access Control

Occurs when:

```text
Normal User
        ↓
Accesses Admin Functionality
```

---

# Common Causes

## Hidden Links

Admin page exists but not linked.

Example:

```text
/admin
```

---

## Obscure URLs

Example:

```text
/admin-panel-7f8g9h
```

---

## Cookie-Based Roles

Example:

```http
admin=false
```

changed to:

```http
admin=true
```

---

## Role Parameters

Example:

```json
{
  "roleid": 1
}
```

changed to:

```json
{
  "roleid": 2
}
```

---

# Related Labs

```text
Lab01
Lab02
Lab03
Lab04
```

---

# Key Takeaways

- Hidden functionality is not protected functionality.
- Roles should be enforced server-side.