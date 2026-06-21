# Preventing File Execution In User Directories

## Overview

Uploaded files should never be executable.

---

# Secure Design

Store uploads:

```text
Outside Web Root
```

instead of:

```text
Inside Public Directories
```

---

# Alternative Protection

Web server configuration should disable execution inside upload directories.

---

# Defense In Depth

```text
Validation
+
Safe Storage
+
Execution Disabled
```

---

# Why Important?

Even if validation fails:

```text
Execution Prevented
```

---

# Related Labs

```text
Lab03
Lab04
```

---

# Key Takeaways

- Prevent execution even after upload.
- Storage location is critical.