# SSPP In REST Paths

## Overview

User input may become part of internal REST URLs.

---

# Example

```text
/api/users/wiener
```

Manipulation:

```text
../admin
```

or

```text
../forgot-password
```

---

# Attack Flow

```text
Path Parameter
        ↓
Internal API
        ↓
Unexpected Endpoint
```

---

# Common Targets

```text
Password Reset
Admin APIs
Version APIs
Internal Services
```

---

# Related Lab

```text
Lab05
```

---

# Key Takeaways

REST path construction should never trust user input.