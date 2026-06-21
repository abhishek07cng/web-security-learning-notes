# Flawed Content Validation

## Overview

Some applications validate uploaded files using:

```text
Magic Bytes
File Signatures
Contents
```

---

# Problem

Attackers can create:

```text
Polyglot Files
```

that contain:

```text
Valid Image Data
+
Server-side Code
```

---

# Example Structure

```text
JPEG Header
        +
Server-side Script
```

---

# Why It Works

Application sees:

```text
Valid Image
```

while the server may interpret executable parts.

---

# Attack Flow

```text
Magic Byte Validation
        ↓
Polyglot Upload
        ↓
Execution
```

---

# Related Lab

```text
Lab06
```

---

# Key Takeaways

- Magic byte validation alone is insufficient.
- Polyglot files bypass content checks.