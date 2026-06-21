# Impact Of File Upload Vulnerabilities

## Impact Depends On

### 1. Validation Weakness

```text
Extension
MIME Type
Content
Filename
Size
```

---

### 2. Server Configuration

```text
Can Uploaded Files Execute?
```

---

# Worst Case

```text
Remote Code Execution (RCE)
```

Server-side code uploaded by an attacker may execute on the server.

---

# Other Impacts

## File Overwrite

Attackers may replace existing files.

---

## Path Traversal

Files may be written outside intended directories.

---

## Stored XSS

Malicious SVG files can execute JavaScript inside browsers.

---

## XXE

XML-based documents may trigger XML parsers.

---

## Denial Of Service

Large uploads can consume:

```text
Disk Space
Memory
CPU
```

---

# Severity Ladder

```text
DoS
        ↓
Information Disclosure
        ↓
Stored XSS
        ↓
File Overwrite
        ↓
Remote Code Execution
```

---

# Key Takeaways

- RCE is the most severe outcome.
- File uploads may enable multiple attack chains.