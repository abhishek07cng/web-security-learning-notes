# File Uploads Without RCE

## Overview

Not all upload vulnerabilities result in:

```text
Remote Code Execution
```

However, they may still be severe.

---

# Stored XSS

SVG Payload:

```html
<svg onload=alert(1)>
```

---

# XXE

Office files:

```text
DOCX
SVG
XML
```

may trigger XML parsing.

---

# Information Disclosure

Files may expose:

```text
Sensitive Documents
Source Code
API Keys
```

---

# DoS

Large uploads may consume:

```text
CPU
Memory
Disk Space
```

---

# Malware Hosting

Attackers can upload:

```text
Phishing Files
Malicious Documents
```

---

# File Overwrite

Upload:

```text
config.php
```

may replace existing files.

---

# Severity Ladder

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

# Key Takeaways

- Lack of RCE does not mean low impact.
- Upload vulnerabilities often chain with other bugs.