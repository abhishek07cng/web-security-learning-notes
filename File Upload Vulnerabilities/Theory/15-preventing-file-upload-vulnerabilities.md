# Preventing File Upload Vulnerabilities

## Principle 1

Use:

```text
Whitelists
```

instead of:

```text
Blacklists
```

---

Allowed:

```text
.jpg
.png
.gif
.pdf
```

---

## Principle 2

Validate:

```text
Extension
MIME Type
Magic Bytes
Contents
```

together.

---

## Principle 3

Store Uploads:

```text
Outside Web Root
```

---

## Principle 4

Disable Script Execution.

---

## Principle 5

Rename Uploaded Files.

Instead of:

```text
shell.php
```

store:

```text
83af2f1.jpg
```

---

## Principle 6

Restrict Permissions.

Example:

```text
Read Only
```

---

## Principle 7

Scan Files.

Examples:

```text
ClamAV
Antivirus
Malware Scanners
```

---

## Principle 8

Limit:

```text
File Size
File Type
Number Of Uploads
```

---

## Principle 9

Perform Security Checks Atomically.

Avoid:

```text
Race Conditions
```

---

# Defense In Depth

```text
Whitelist
        +
Content Validation
        +
Storage Outside Web Root
        +
No Execution
        +
Scanning
```

---

# Secure Upload Formula

```text
Validate
        ↓
Rename
        ↓
Store Safely
        ↓
Restrict Execution
```

---

# Key Takeaways

- Assume users upload malicious files.
- Multiple defensive layers are required.
- No single validation is sufficient.