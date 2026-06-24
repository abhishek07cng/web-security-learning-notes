# Mass Assignment Vulnerabilities

## Overview

Mass assignment occurs when APIs automatically bind user-supplied data to object properties.

---

# Example

Backend Object:

```text
username
email
password
isAdmin
```

User Interface exposes:

```text
username
email
password
```

Hidden field:

```text
isAdmin
```

still exists.

---

# Attack Flow

```text
User Input
        ↓
Automatic Binding
        ↓
Hidden Property Modified
        ↓
Privilege Escalation
```

---

# Indicators

```text
JSON APIs
PUT Requests
PATCH Requests
```

---

# Related Lab

```text
Lab03
```

---

# Key Takeaways

Never expose sensitive properties directly to automatic binding.