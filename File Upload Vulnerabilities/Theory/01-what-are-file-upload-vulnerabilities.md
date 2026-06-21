# What Are File Upload Vulnerabilities?

## Overview

File upload vulnerabilities occur when an application allows users to upload files without properly validating:

```text
Filename
Extension
MIME Type
Contents
Size
Storage Location
```

This may allow attackers to upload dangerous files.

---

# Typical Flow

```text
User Uploads File
        ↓
Server Validates File
        ↓
File Stored
        ↓
File Accessed
```

If validation is weak:

```text
Malicious File Uploaded
        ↓
Executed By Server
        ↓
Remote Code Execution
```

---

# Why File Uploads Are Dangerous

Attackers may upload:

```text
PHP Files
JSP Files
ASPX Files
Python Scripts
SVG Files
XML Files
```

---

# Common Impacts

```text
Remote Code Execution
Stored XSS
XXE
File Overwrite
Information Disclosure
Denial Of Service
```

---

# Worst Case Scenario

```text
Upload PHP Web Shell
        ↓
Execute Commands
        ↓
Full Server Compromise
```

---

# Key Takeaways

- File uploads are high-risk functionality.
- Improper validation can lead to complete compromise.