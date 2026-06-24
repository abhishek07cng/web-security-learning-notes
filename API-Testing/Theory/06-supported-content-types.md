# Supported Content Types

## Overview

APIs process data differently depending on content type.

---

# Common Types

## JSON

```http
Content-Type: application/json
```

---

## XML

```http
Content-Type: application/xml
```

---

## Form Data

```http
application/x-www-form-urlencoded
```

---

## Multipart

```http
multipart/form-data
```

---

# Why Test Content Types?

Changing content type may:

```text
Trigger Errors
Reveal Information
Bypass Validation
Change Processing Logic
```

---

# Attack Flow

```text
Change Content-Type
        ↓
Different Parser
        ↓
Different Behavior
```

---

# Related Lab

```text
Lab02
```

---

# Key Takeaways

Different parsers may introduce vulnerabilities.