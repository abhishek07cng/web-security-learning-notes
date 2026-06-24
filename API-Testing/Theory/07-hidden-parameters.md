# Hidden Parameters

## Overview

Applications often expose parameters that are not visible in the user interface.

These parameters may still be accepted by the API.

---

# Sources

```text
JavaScript Files
Proxy History
Swagger Documentation
Error Messages
Responses
```

---

# Examples

```text
isAdmin
role
discount
debug
price
```

---

# Attack Flow

```text
Endpoint
        ↓
Hidden Parameter
        ↓
Unexpected Functionality
```

---

# Discovery Techniques

```text
Parameter Guessing
Param Miner
Documentation
Response Analysis
```

---

# Related Lab

```text
Lab03
```

---

# Key Takeaways

Hidden parameters often expose dangerous functionality.