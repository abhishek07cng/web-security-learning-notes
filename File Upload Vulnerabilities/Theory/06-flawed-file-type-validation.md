# Flawed File Type Validation

## Overview

Many applications attempt to validate uploaded files based on:

```text
Extension
MIME Type
Magic Bytes
```

Improper validation can often be bypassed.

---

# Common Validation Mechanisms

## Extension Validation

Example:

```text
.jpg
.png
.gif
```

---

## MIME Type Validation

Example:

```http
Content-Type: image/jpeg
```

---

## Magic Byte Validation

Example:

JPEG files begin with:

```text
FF D8 FF
```

---

# Why It Fails

Attackers control:

```text
Filename
Content-Type Header
```

and may even bypass:

```text
Magic Byte Checks
```

using polyglot files.

---

# Example

Application expects:

```http
Content-Type:image/jpeg
```

Attacker changes:

```http
Content-Type:image/jpeg
```

while uploading:

```text
shell.php
```

---

# Attack Flow

```text
Weak Validation
        ↓
Malicious File Accepted
        ↓
Code Execution
```

---

# Related Labs

```text
Lab02
Lab06
```

---

# Key Takeaways

- MIME type should never be trusted.
- Multiple layers of validation are required.