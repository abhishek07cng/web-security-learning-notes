# Race Conditions

## Overview

Race conditions occur when:

```text
Validation
        ↓
Storage
        ↓
Security Processing
```

are not atomic.

---

# Typical Flow

```text
Upload File
        ↓
Stored Temporarily
        ↓
Virus Scan
        ↓
Deletion
```

---

# Vulnerability

During the short window:

```text
Temporary File Exists
```

attackers may access it.

---

# Attack Flow

```text
Upload Shell
        ↓
Repeated Requests
        ↓
Execute Before Removal
```

---

# Why It Happens

Operations occur in:

```text
Separate Threads
Separate Processes
```

---

# Tools

```text
Turbo Intruder
Burp Repeater
Parallel Requests
```

---

# Related Lab

```text
Lab07
```

---

# Key Takeaways

- Timing matters.
- Temporary files may become exploitable.