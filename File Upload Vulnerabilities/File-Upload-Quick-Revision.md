# File Upload Quick Revision

## Most Dangerous Outcome

```text
Remote Code Execution
```

---

## Common Validation Types

### Extension

```text
.php
.jpg
.png
```

---

### MIME Type

```http
Content-Type
```

---

### Magic Bytes

```text
File Signatures
```

---

## Common Bypasses

### Extension Tricks

```text
Double Extensions
Mixed Case
Trailing Dot
```

---

### MIME Spoofing

```http
image/jpeg
```

---

### Polyglot Files

```text
Image
+
Server-side Script
```

---

### Path Traversal

```text
Escape Upload Folder
```

---

### Race Conditions

```text
Access Before Deletion
```

---

### PUT Upload

```http
PUT
```

---

## Severity Ladder

```text
DoS
        ↓
Stored XSS
        ↓
Information Disclosure
        ↓
File Overwrite
        ↓
RCE
```

---

# Personal Formula

```text
Upload
        ↓
Store
        ↓
Access
        ↓
Execute
```

---

# Top Lessons From PortSwigger

1. Never trust file extensions.
2. MIME types are attacker-controlled.
3. Blacklists fail.
4. Storage location matters.
5. Polyglot files bypass magic-byte checks.
6. Race conditions create execution windows.
7. RCE requires:

```text
Upload
+
Access
+
Execution
```