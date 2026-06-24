# SSPP In Structured Data

## Overview

JSON and XML objects may allow parameter injection.

---

# Example

Normal JSON:

```json
{
 "username":"wiener"
}
```

Injected:

```json
{
 "username":"wiener",
 "role":"admin"
}
```

---

# Attack Flow

```text
Structured Input
        ↓
Backend Parsing
        ↓
Unexpected Properties
```

---

# Common Targets

```text
JSON APIs
GraphQL APIs
PATCH Requests
PUT Requests
```

---

# Related Lab

```text
Lab03
```

---

# Key Takeaways

Structured formats increase attack surface.